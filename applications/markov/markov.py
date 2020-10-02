import random


def word_makers(s):

    # Read in all the words in one go
    with open(s) as f:
        words = f.read()

# TODO: analyze which words can follow other words

# add all words to a dictionary, with the value being none, no dups
    cache = {}
    res = words.split()

    for i in range(len(res) - 1):
        if i < len(res):
            if res[i] not in cache:
                cache[res[i]] = [res[i + 1]]
            else:
                cache[res[i]].append(res[i + 1])

    print(cache)


word_makers("input.txt")

# TODO: construct 5 random sentences
# Your code here
