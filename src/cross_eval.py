import json
import numpy as np
import time
from tqdm import tqdm
from sentence_transformers import CrossEncoder
from utils import *

model_path = "input cross-encoder model path here"

model = CrossEncoder(model_path, max_length=512)

with open("src/data/corpus.json", "r") as file:
    corpus = json.load(file)

with open("src/data/test_manual_final.json", "r") as file:
    test_manual = json.load(file)

results = []
for q in tqdm(test_manual):
    query = q["ExcluQ"]
    pairs = [(query, corpus[index]) for index in len(corpus)] # To improve efficiency, we recommend first retrieve 100 documents using BM25, followed and then rerank with the cross-encoder model
    start_time = time.time()
    scores = model.predict(pairs)
    print(f"Time Cost: {time.time() - start_time}")
    # Get the index of top 10 documents
    top_k_indices = np.argsort(scores)[::-1][:10]
    results.append(top_k_indices.tolist())

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