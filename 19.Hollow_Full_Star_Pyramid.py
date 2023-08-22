n = 5
for i in range(n):
    for j in range(n-i-1):
        print(" ",end="")
    for j in range(2*i + 1):
        if j ==0 or j == 2*i or i == n-1:
            print("*", end="")
        else:
            print(" ",end="")
    print()

## 2nd method

for i in range(1,n+1):
    for j in range(1,n*2):
        if i+j == n+1 or j -i == n-1 or (i ==n and j%2 != 0):
            print("*", end="")
        else:
            print(" ",end="")
    print()