def compute_recall(result_list, right_list, recall_k = [1,5,10]): 
    # result_list [[4,2,6,1,5], [...], ...]
    # right_list [[2,...], [.], ...]
    recall_list = [0 for k in range(len(recall_k))]
    for i in range(len(result_list)):
        a_right = right_list[i]
        a_result = result_list[i]
        # 算recall
        for j in range(len(recall_k)):
            recall_list[j] += len(set(a_result[:recall_k[j]]) & set(a_right)) / len(a_right)

    recall_list = list(map(lambda x: x/len(result_list), recall_list))
    return recall_list

def compute_MRR(result_list, right_list): 
    # result_list [[4,2,6,1,5], [...], ...]
    # right_list [[2,...], [.], ...]
    MRR10 = 0
    for i in range(len(result_list)):
        a_right = right_list[i]
        a_result = result_list[i]
        for rank, item in enumerate(a_result[:10]):
            if item in a_right:
                MRR10 += 1.0 / (rank + 1.0)
                break
    MRR10 = MRR10 / len(result_list)
    return MRR10

def compute_right_rank(result_list, right_list):
    right_rank = 0
    for i in range(len(result_list)):
        a_right = right_list[i]
        a_result = result_list[i]
        if a_right[0] in a_result and a_right[1] in a_result:
            if a_result.index(a_right[1]) < a_result.index(a_right[0]):
                right_rank += 1
        elif a_right[1] in a_result:
            right_rank += 1
    right_rank = right_rank/len(result_list)
    return right_rank