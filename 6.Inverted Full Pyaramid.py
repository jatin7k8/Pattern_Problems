n = int(input())
for i in range(n,0,-1):
    for j in range(1,n-i+3):
        print(end=" ")
    for k in range(1,i+1):
        print("*",end=" ")
    print()

n = int(input())
for i in range(1,n+1):
    print(" "*(n-i) +"* "*i)

n = int(input())
for i in range(n,0,-1):
    print(" "*(n-i) +" *"*i)