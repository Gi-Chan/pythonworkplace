def merge_sort(lst, p, r) : # A[p..r]을 오름차순 정렬한다.
    if (p < r) : 
        q = (p + r) // 2  
        # q는 p, r의 중간 지점
        merge_sort(lst, p, q)    # 전반부 정렬
        merge_sort(lst, q + 1, r)  # 후반부 정렬
        merge(lst, p, q, r)      # 병합 

# A[p..q]와 A[q+1..r]을 병합하여 A[p..r]을 오름차순 정렬된 상태로 만든다.
# A[p..q]와 A[q+1..r]은 이미 오름차순으로 정렬되어 있다.
def merge(lst, p, q, r) :
    tmp = []
    i = p
    j = q + 1
    t = 1
    while (i <= q and j <= r):
        if (lst[i] <= lst[j]):
            tmp.append(lst[i])
            i+=1
            # tmp[t] = A[i]; t++; i++;
        else:
            tmp.append(lst[j])
            j+=1    
             # tmp[t] = A[j]; t++; j++;    
    while (i <= q):  # 왼쪽 배열 부분이 남은 경우
        tmp.append(lst[j])
        i+=1
    while (j <= r):  # 오른쪽 배열 부분이 남은 경우
        tmp.append(lst[j])
        j+=1
    i = p
    t = 0
    cnt=0
    while (i <= r):  # 결과를 A[p..r]에 저장
        lst[i] = tmp[t]; 
        cnt+=1
        if cnt==7:
            break
        t+=1
        i+=1
        
arr = [4, 5, 1, 3, 2]
n = 5
k = 7
print(merge_sort(arr,0,n-1))