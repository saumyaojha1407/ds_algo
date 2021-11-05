def get_top_k(input_array, k):
    max_dict = {}
    top_max = {}
    idx = 0
    for i in input_array:
        if i not in max_dict:
            max_dict[i] = 1
        else:
            max_dict[i] += 1
    inversed_dict = dict(map(reversed, max_dict.items()))
    for key, value in inversed_dict.items():
        if idx < k:
            top_max[key] = value
        idx+=1
    return top_max


print(get_top_k([1,1,1,2,2,3], 2))