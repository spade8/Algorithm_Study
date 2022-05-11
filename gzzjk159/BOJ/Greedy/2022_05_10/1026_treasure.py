import sys

input = sys.stdin.readline

n = int(input().strip())

a = list(map(int, input().strip().split()))
b = list(map(int, input().strip().split()))

a.sort()
b.sort(reverse=True)

sum = 0

for i in range(n):
    sum += a[i]*b[i]

print(sum)