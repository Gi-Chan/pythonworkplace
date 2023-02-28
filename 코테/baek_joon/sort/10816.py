def dic(lst):
    counts = {}
    for x in lst:
        if x in counts:
            counts[x] +=1
        else:
            counts[x] = 1
    return counts

n= int(input())
lst= list(map(int, input().split()))
m= int(input())
lst2= list(map(int, input().split()))
dict = dic(lst)

for i in lst2:
    if i in dict:
        print(dict[i], end=' ')
    else:
        print(0, end=' ')