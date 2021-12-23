import re

def allConstructBrute(target, word_bank):
    if target == '':
        return True
    for words in word_bank:
        if re.search(r'^{}'.format(words), target):
            if allConstructBrute(re.sub(r'^{}'.format(words), '', target), word_bank):
                return True
    return False


def allConstruct(target, word_bank, memo):
    if target in memo:
        return memo[target]
    if target == '':
        return [[]]
    all_ways = []
    for words in word_bank:
        if re.search(r'^{}'.format(words), target):
            ways = allConstruct(re.sub(r'^{}'.format(words), '', target), word_bank, memo)
            all_ways += [[words] + x for x in ways]
    memo[target] = all_ways
    return all_ways


if __name__ == '__main__':
    # print(canConstructBrute('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd']))
    # print(canConstructBrute('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar']))
    # print(canConstructBrute('enterapotentpot', ['a', 'p', 'ent', 'enter', 'ot', 'o', 't']))
    # print(canConstructBrute('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef', ['e', 'ee', 'eee', 'eeee', 'eeeee', 'eeeeee']))
    print(allConstruct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd'], {}))
    print(allConstruct('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar'], {}))
    print(allConstruct('enterapotentpot', ['a', 'p', 'ent', 'enter', 'ot', 'o', 't'], {}))
    print(allConstruct('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef', ['e', 'ee', 'eee', 'eeee', 'eeeee', 'eeeeee'], {}))