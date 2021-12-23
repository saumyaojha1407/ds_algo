import sys

class MaxHeap:
    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.size = 0
        self.Heap = [0] * (self.maxsize + 1)
        self.Heap[0] = sys.maxsize
        self.FRONT = 1

    def parent(self, pos):
        return pos // 2

    def leftChild(self, pos):
        return 2 * pos

def max_freq_word(list_of_words, k):
    dict_words = {}
    for word in list_of_words:
        if word.lower() in dict_words:
            dict_words[word.lower()] += 1
        else:
            dict_words[word.lower()] = 1
    max_freq = 0
    output_word = []
    # dict_words = dict(sorted(dict_words.items(), key=lambda item: item[1], reverse=True))
    for key, value in dict_words.items():
        if k:
            output_word.append(key)
            k -= 1
        else:
            break

    return output_word


print(max_freq_word(["Hello", "Hi", "Hello", "world", "Hello", "Hi"], 2))