n = int(input())

for i in range(n):
    for j in range(n):
        for k in range(n):
            print(f'{chr(ord("a") + i)}{chr(ord("a") + j)}{chr(ord("a") + k)}')
            