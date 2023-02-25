music = list(map(int, input().split()))
as_cnt=0
de_cnt=0
for i in range(1,9):
    if i==music[i-1]:
        as_cnt+=1
    if (9-i)==music[i-1]:
        de_cnt+=1
    
if as_cnt==8:
    print('ascending')
elif de_cnt==8:
    print('descending')
else:
    print('mixed')