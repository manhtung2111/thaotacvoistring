def ABC(A,B):
    if B in A: print(B,"nam trong",A)
    A1 = A.split(" ") #tach A thanh 1 list,A1 =list
    print(A1.index(B)) #tim vi tri cua B trong A

A = "tao dang an"
B = "dang"
ABC(A,B)