tc = int(input())

for i in range(tc):

    test_lst =[]

    n = int(input())
    for j in range(n):
        test_lst.append(list(map(str, input().split())))
    
    ans_lst = []
    for k in range(n):
        if 'YES' in test_lst[k]:
            ap_lst = list(map(int, test_lst[k][:4]))

            for kk in range(4):
                if ap_lst[kk] not in ans_lst:
                    ans_lst.append(ap_lst[kk])

        elif 'NO' in test_lst[k]:
            mi_lst = list(map(int, test_lst[k][:4]))

            for kk in range(4):
                if mi_lst[kk] in ans_lst:
                    ans_lst.remove(mi_lst[kk])
                
    print(i+1, ans_lst.pop())