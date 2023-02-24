
arr =[]
for i in range(5):
    n = int(input())
    arr.append(n)
    
print(int(sum(arr)/len(arr)))

arr.sort()
if len(arr)%2 ==0:
    print(arr[len(arr)//2-1])
else:
    print(arr[len(arr)//2])