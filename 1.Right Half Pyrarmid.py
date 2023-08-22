n = int(input())

#1st method
# for i in range(n):
#     print("*"*i)

# 2nd method
for i in range(1, n+1):
    for j in range(1,i+1):
        print("*",end="")
    print()
