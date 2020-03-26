def daydoixung(x):
    a=[]
    for i in x:
        if i==i[::-1]:
            a.append(i)
    return a
b = ["abccba","acdda","acbba","acca","xxyxx"]
print (daydoixung(b))
