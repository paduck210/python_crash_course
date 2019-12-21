from collections import Counter

def duplicate_encode(word):
    count_list = Counter(word.lower())
    return ''.join('(' if count_list[i] == 1 else ")" for i in word)

