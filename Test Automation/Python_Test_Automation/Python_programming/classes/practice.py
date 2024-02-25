from collections import Counter
def findSubstring(s, words):
    if not s or not words:
        return []

    word_len = len(words[0])
    word_count = len(words)
    total_len = word_len * word_count
    result = []

    words_counter = Counter(words)

    for i in range(len(s) - total_len + 1):
        substring = s[i:i + total_len] # s[0:6]:barfoo
        substring_counter = Counter([substring[j:j + word_len] for j in range(0, total_len, word_len)])# bar :1,foo:1


        if substring_counter == words_counter:
            result.append(i)

    return result

# Example usage:
s = "barfoothefoobarman"
words = ["foo", "bar"]
output = findSubstring(s, words)
print(output)

w=['foo', 'bar','foo','bar','foo']
print(Counter(w))

