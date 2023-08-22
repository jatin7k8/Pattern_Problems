n = int(input())
for i in range(1,n+1):
    print(" "*(n-i)+"*"*i)

# 2nd methode
n = 5
for i in range(n):
    for j in range(i,n-1):
        print(" ",end="")
    for k in range(i+1):
        print("*",end="")
    print()