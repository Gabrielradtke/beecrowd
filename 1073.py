# 5 < N < 2000
n = int(input())

for i in range(1, n+1):
    if i % 2 == 0:
        res = i * n
        print(f'{i} ^ 2 = {res}')