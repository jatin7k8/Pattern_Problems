n = 11
for i in range(1,n+1):
    for j in range(1,n+1):
        # if i == 1 or j == n or i == n or j == 1:
        if i == j or i +j ==n+1 or j == n or i == 1 or j == 1 or i ==n :
            print("*",end="")
        else:
            print(" ",end="")
    print()