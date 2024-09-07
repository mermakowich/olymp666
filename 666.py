n, k = map(int, input().split())
a = 1
b = 1
c = 1
s = 0
while a <= n and b <= n and c <= n:
    if (a + b)%k == 0 and (b + c)%k == 0 and (a+c)%k == 0:
        s += 1
