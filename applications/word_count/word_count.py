
def word_count(s):
    cache = {}
    punctuation = '\":;,.-+=/\\|[]\{\}()*^&'

    no_punction = ""
    # remove punctuation
    for c in s:
        if c not in punctuation:
            no_punction = no_punction + c
    # need to set it to a new variable, not sure why
    res = no_punction.split()

    for c in res:
        if c.lower() not in cache:
            cache[c.lower()] = 1
        else:
            cache[c.lower()] += 1
    return cache


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count(
        'This is a test of the emergency broadcast network. This is only a test.'))
