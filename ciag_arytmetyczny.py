a, n, r = input().split()
a = int(a)
n = int(n)
r = int(r)
x = 0

while x < n:
    print(a, end=" ")
    a+=r
    x+=1

