def maxLength(arr):
    ans = 0
    positive, negative = 0,0
    for n in arr:
        if n >0:
            positive = positive + 1
            if negative > 0:
                negative =  negative + 1
            else:
                negative = 0
        elif n<0:
            if negative > 0:
                positive = negative + 1
            else:
                positive = 0
            if positive >0:
                negative = positive +1
            else:
                positive = 1
        else:
            positive, negative = 0,0
        ans = max(ans, positive)
    return ans


if __name__ == '__main__':
    print(maxLength())