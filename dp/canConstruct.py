import re

def canConstructBrute(target, word_bank):
    if target == '':
        return True
    for words in word_bank:
        if re.search(r'^{}'.format(words), target):
            if canConstructBrute(re.sub(r'^{}'.format(words), '', target), word_bank):
                return True
    return False


def canConstruct(target, word_bank, memo):
    if target in memo:
        return memo[target]
    if target == '':
        return 1
    total_count = 0
    for words in word_bank:
        if re.search(r'^{}'.format(words), target):
            ways = canConstruct(re.sub(r'^{}'.format(words), '', target), word_bank, memo)
            # if canConstruct(re.sub(r'^{}'.format(words), '', target), word_bank, memo):
            # memo[target] = True
            total_count += ways
    memo[target] = total_count
    return total_count


if __name__ == '__main__':
    # print(canConstructBrute('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd']))
    # print(canConstructBrute('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar']))
    # print(canConstructBrute('enterapotentpot', ['a', 'p', 'ent', 'enter', 'ot', 'o', 't']))
    # print(canConstructBrute('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef', ['e', 'ee', 'eee', 'eeee', 'eeeee', 'eeeeee']))
    print(canConstruct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd'], {}))
    print(canConstruct('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar'], {}))
    print(canConstruct('enterapotentpot', ['a', 'p', 'ent', 'enter', 'ot', 'o', 't'], {}))
    print(canConstruct('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef', ['e', 'ee', 'eee', 'eeee', 'eeeee', 'eeeeee'], {}))