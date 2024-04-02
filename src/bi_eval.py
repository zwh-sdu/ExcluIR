import json
import numpy as np
import os
import time
from tqdm import tqdm
import faiss
import torch
from sentence_transformers import SentenceTransformer
from utils import *

model_path = "input sentence_transformers model path here"

model = SentenceTransformer(model_path)

with open("src/data/corpus.json", "r") as file:
    corpus = json.load(file)

with open("src/data/test_manual_final.json", "r") as file:
    test_manual = json.load(file)

collection = []
with torch.no_grad():
    for sentence in tqdm(corpus):
        sentence_embeddings = model.encode([sentence])
        sentence_embeddings = sentence_embeddings.tolist()
        collection.extend(sentence_embeddings)
collection = np.array(collection, dtype=np.float32)

index_filename = f"index/{model_path}.index"

if not os.path.exists(index_filename):
    index_dir = os.path.dirname(index_filename)
    if not os.path.exists(index_dir):
        os.makedirs(index_dir)
    dim = collection.shape[1]
    t = time.time()
    cpu_index = faiss.index_factory(dim, "Flat", faiss.METRIC_INNER_PRODUCT)
    index = cpu_index
    index.add(collection)
    faiss.write_index(index, index_filename)
    print(f"build index of {len(collection)} instances, time cost ={time.time() - t}")
else:
    index = faiss.read_index(index_filename)

q_embs = []

with torch.no_grad():
    for q in tqdm(test_manual):
        query = [q["ExcluQ"]]
        q_embs.append(model.encode(query)[0])
q_embs = np.array(q_embs)
distance, rank = index.search(q_embs, 10)
rank = rank.tolist()
results = rank

result_list = []
right_list = []
right_list_pos = []
right_list_neg = []
for num, result in enumerate(results):
    result_list.append(results[num])
    right_list.append(test_manual[num]["index"])
    right_list_pos.append(test_manual[num]["index"][1:])
    right_list_neg.append(test_manual[num]["index"][:1])

recall_pos = compute_recall(result_list, right_list_pos)
recall_neg = compute_recall(result_list, right_list_neg)
mrr_pos = compute_MRR(result_list, right_list_pos)
mrr_neg = compute_MRR(result_list, right_list_neg)
rr = compute_right_rank(result_list, right_list)

metric = {}
metric["R@1"] = round(recall_pos[0]*100,2)
metric["MRR@10"] = round(mrr_pos*100,2)
metric["ΔR@1"] = round(recall_pos[0]*100,2) - round(recall_neg[0]*100,2)
metric["ΔMRR@10"] = round(mrr_pos*100,2) - round(mrr_neg*100,2)
metric["RR"] = round(rr*100,2)
print(metric)