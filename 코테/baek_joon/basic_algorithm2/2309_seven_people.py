


arr=[]
for i in range(9):
    arr.append(int(input()))
print(arr)
hap = sum(arr)-100
print(hap)
flag=0
for i in range(9):
    
    for j in range(i):
        if (arr[i]+arr[j])==hap:
            flag=1
            break
    if flag==1:
        arr.pop(i)
        arr.pop(j) 
        break   
            

print(list(sorted(arr)))