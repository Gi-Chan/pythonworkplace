

# 짝수 홀수 나누기

# 짝수는 다 더하기
# 홀수는 따로 리스트를 만들기
# 1. 홀수의 리스트 길이가 짝수면 다 더한다
# 2. 홀수의 리스트가 홀수이면 in값을 빼고 다 더한다.
n = int(input())
candy = list(map(int,input().split()))
even_sum=0
odd_sum=0
odd_list = []

for i in range(n):

    if candy[i]%2==0:
        even_sum+=candy[i]
    else:
        odd_list.append(candy[i])

if len(odd_list) %2==0:
    odd_sum = sum(odd_list)
else:
    odd_list.pop(odd_list.index(min(odd_list)))
    odd_sum = sum(odd_list)
print(even_sum+odd_sum)

lst = []
print(sum(lst))