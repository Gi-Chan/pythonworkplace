a,b = map(int, input().split())

if b>a:
    a,b=b,a
max=a
min=b
'''
<유클리드 호제법>
a와 b의 최대 공약수 G는 
a%b(a를 b로 나눈 나머지)의 최대공약수
G'가 같다.(a>b)
이때 b가 0일때 a값이 최대공약수

최소 공배수는 a*b/(최대공약수)
'''

# 최대 공약수
while min!=0:
    max =max %min
    max,min = min,max
print(max)
    
# 최소 공배수
print(int(a*b/max))