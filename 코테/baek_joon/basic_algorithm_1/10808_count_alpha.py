word = input()
count =[0]*26
'''
아스키코드 이용
해당 문자 - a에 해당하는 인덱스를 증가시킴

'''

for i in word:
    num = ord(i)-ord('a')
    
    count[num] +=1
    
for j in count:
    print(j, end=' ')