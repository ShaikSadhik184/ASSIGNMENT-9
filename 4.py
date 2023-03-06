n=int(input("enter the values of N:"))
count = 1
i = 1
while count <= n:
    if i % 2 != 0:
        print(i)
        count += 1
    i += 1