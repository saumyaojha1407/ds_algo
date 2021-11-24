

def sub_array(idx, arr):
    left, right = idx, None
    max_arr = 0
    count_0, count_1 = 0, 0
    while left >=0:
        if arr[left] == 0:
            count_0 +=1
        else:
            count_1 +=1
        if count_0 == count_1 and count_0+count_1>max_arr:
            max_arr = count_0 + count_1
            right = left
        left -=1
    return max_arr, right


##brute force
def find_max_sub_array_brute(arr):
    max_array = 0
    start = None
    end = None
    for i in range(len(arr)):
        local_max, start_coord = sub_array(i, arr)
        if start_coord and local_max > max_array:
            max_array = local_max
            start = start_coord
            end = i

    return start, end


def find_max_sub_array_hashmap(arr):
    cumu_dict = {}
    cumulative_sum = 0
    final_max = 0
    end = None
    for idx, i in enumerate(arr):
        if i == 1:
            cumulative_sum += 1
        else:
            cumulative_sum -= 1
        if cumulative_sum == 0:
            final_max = idx + 1
            end = idx
        if cumulative_sum in cumu_dict:
            if idx - cumu_dict[cumulative_sum]> final_max:
                final_max = idx -cumu_dict[cumulative_sum]
                end = idx
        else:
            cumu_dict[cumulative_sum] = idx
    if end:
        return end-final_max+1, end
    return end


if __name__ == '__main__':
    print(find_max_sub_array_hashmap([1, 0, 1, 1, 1, 0, 0]))
    print(find_max_sub_array_hashmap([1, 1, 1, 1]))
    print(find_max_sub_array_hashmap([0, 0, 1, 1, 0]))
    print(find_max_sub_array_hashmap([1, 0, 0, 1, 0, 1, 1]))