def reverse(s):
    if len(s) == 0:
        return s
    else:
        return reverse(s[1:]) + s[0]
s = ["abaca","acbbc","acca","abba"]
for i in s:
    if reverse(i) in s:
        print(reverse(i))
#giai thich qua code:
#vd [abcda]
#b1 : kiem tra len co != 0 k: r chuyen sang b2
#func tra ve rev[bcda] + a o cuoi
#b2, tg tu, func tra ve rev[cda] + b+a
#tg tu ta dc reverse can tim