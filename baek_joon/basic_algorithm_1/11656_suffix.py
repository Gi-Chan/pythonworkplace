word = input()
arr= []
for i in range(len(word)):
    
    # 슬라이싱을 통해 앞에서 부터 지워나간다
    arr.append(word[i:])

# sorted하면 사전순으로정렬됨
for i in sorted(arr):
    print(i)