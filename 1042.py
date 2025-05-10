a, b, c = map(int,input().split())

if a < b and a < c:
    pri = a
elif a < b and a > c:
    seg = b
elif b > a and b < c: