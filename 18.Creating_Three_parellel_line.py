n = 5
for i in range(n):
    for j in range(n):
        if i == n//2 or i ==0 or i ==n-1:
            print("*",end="")
        else:
            print("",end="")
    print()