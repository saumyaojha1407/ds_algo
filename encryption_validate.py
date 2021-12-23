def encryption_validity(instruction_count, validity_period, keys):
    #     # Write your code here
    freq_dict = {}
    for i in keys:
        if i in freq_dict:
            freq_dict[i]+=1
        else:
            freq_dict[i] = 1
    maxdegree = 0
    dict_keys = {}
    for k in keys:
        degree=0
        if k in dict_keys:
            degree = dict_keys[k]
        else:
            for j in keys:
                if k%j==0:
                    degree=degree+1
            dict_keys[k] = degree
        if degree>maxdegree:
            maxdegree = degree
    print(maxdegree)
    encr_strength = maxdegree * 100000
    prod = instruction_count * validity_period
    if encr_strength > prod:
        a = 0
    else:
        a = 1

    return [a, int(encr_strength)]


if __name__ == '__main__':
    print(encryption_validity(100, 1000, [2,4]))