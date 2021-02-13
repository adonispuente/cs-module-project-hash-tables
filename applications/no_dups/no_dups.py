def no_dups(s):
    cache = {}

    res = s.split()
    for c in res:
        if c not in cache:
            cache[c] = c

    return ' '.join(cache)

    # cache = []
    # # count = 0

    # res = s.split()
    # for c in res:
    #     if c not in cache:
    #         cache.append(c)

    # return ' '.join(cache)


if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))
