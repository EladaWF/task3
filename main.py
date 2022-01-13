# https://codeforces.com/problemset/problem/546/A
a, b, c = map(int, input().split())
count = 0
for i in range(1, c+1):
    count += a*i
if count-b <= 0:
    print(0)
else:
    print(count-b)