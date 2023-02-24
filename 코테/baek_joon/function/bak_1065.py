

a=int(input())
cnt=0

while a>=1:
    nums = []
    sub = []

    for i in map(int, str(a)):
        nums.append(i)
    nums.append(None)
    for j in range(len(nums)-1):
        if nums[j+1]!=None:
            sub.append(nums[j]-nums[j+1])

    se = set(sub)

    if len(se)<=1:
        cnt+=1
    a-=1

print(cnt)