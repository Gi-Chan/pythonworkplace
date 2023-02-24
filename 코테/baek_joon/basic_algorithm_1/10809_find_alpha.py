word = input()
count =[-1]*26
word_arr = []
'''
아스키코드 이용
해당 문자 - a에 해당하는 인덱스를 넣음

'''
cnt=0
for i in word:
    cnt+=1 # 해당 문자가 위치한 인덱스
    
    # i가 word_arr에 있으면 그냥 지나감
    if i in word_arr:
        continue
    
    num = ord(i)-ord('a')
    count[num] +=cnt
    
    # 해당 문자가 처음 발견될 때만 넣음
    word_arr.append(i)
for j in count:
    print(j, end=' ')