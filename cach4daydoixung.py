def reverse(s):
    s = "".join(reversed(s))
    return s
s = ["abaca","acbbc","acca","abba"]
for i in s:
    if reverse(i) in s:
        print(reverse(i))