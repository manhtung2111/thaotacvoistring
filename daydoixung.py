def my_string(X):
    if X == X[::-1]:
        return X
list = ["abccba","acdda","acbba","acca","xxyxx"]
for i in list:
    print(my_string(i))

