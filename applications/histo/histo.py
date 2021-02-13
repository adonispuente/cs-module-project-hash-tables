# Your code here
def hash_count(s):
    with open(s) as f:
        words = f.read()

    cache = {}
    punctuation = '\":;,.-+=/\\|[]\{\}()*^&'

    no_punction = ""
    # remove punctuation
    for c in words:
        if c not in punctuation:
            no_punction = no_punction + c
        # need to set it to a new variable, not sure why
    res = no_punction.split()

    for c in res:
        if c not in cache:
            cache[c] = '#'
        else:
            cache[c] += '#'
    # return cache

# returns it organized but not sorted
    # for i in cache:
    #     print(i, cache[i])
    sort_cache = sorted(cache.items(), key=lambda x: x[1], reverse=True)
    for i in sort_cache:
        print(i[0], i[1])

        # better but cant get it to work

    #      sort_cache = sorted(cache.items(), key=lambda x: (-len(x[1]), x[0])

    # for words in sort_cache:
    #     print(f'{word}  {reps}')


# if __name__ == "__main__":
#     print(hash_count('robin.txt'))
hash_count('robin.txt')
