#fibonacci series
# 1,1,2,3,5,8

num = int(input("enter any number:"))
n1 = 0
n2 = 1
sum = 0
if num <= 0:
    print("pls enter number greater than zero")
else:
    for i in range(0,num):
        print(sum)
        n1 = n2
        n2 = sum
        sum = n1+n2