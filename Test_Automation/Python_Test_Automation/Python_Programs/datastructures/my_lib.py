def frequency_of_words(str):
    l=list(str.split())
    s=set(l)
    d={i:l.count(i) for i in s}
    return d