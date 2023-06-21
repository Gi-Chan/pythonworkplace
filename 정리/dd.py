n = int(input())
a, b, c, d, e, f = map(int, input().split())

# A부터 F까지의 배수 중에서 가장 작은 공배수를 구합니다.
lcm = a
for x in [b, c, d, e, f]:
    for i in range(2, x+1):
        if lcm % i == 0 and x % i == 0:
            lcm *= i
            x //= i
    lcm *= x

# 공배수로 나눈 몫과 나머지를 구합니다.
q, r = divmod(n, lcm)

# 각 배수에 대해서 연산을 수행합니다.
x = 0
for i in range(1, lcm+1):
    if i % a == 0:
        x += i
    if i % b == 0:
        x %= i
    if i % c == 0:
        x &= i
    if i % d == 0:
        x ^= i
    if i % e == 0:
        x |= i
    if i % f == 0:
        x >>= i

# 몫에 대해서 연산을 수행합니다.
for i in range(1, a+1):
    if i <= r:
        if i % a == 0:
            x += i
        if i % b == 0:
            x %= i
        if i % c == 0:
            x &= i
        if i % d == 0:
            x ^= i
        if i % e == 0:
            x |= i
        if i % f == 0:
            x >>= i

print(x)
