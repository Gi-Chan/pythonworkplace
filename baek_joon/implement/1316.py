n = int(input())
cnt=0

for i in range(n):
    
    word = input()
    flag = 1
    for j in range(len(word)-1):
        if word[j] != word[j+1]: # 현재 알파벳이 다음 알파벳과 다르면 
            for k in range(j+1, len(word)): # 다음 알파벳부터 끝까지 탐색한다.   
                if word[j] == word[k]: # 만약 같은 알파벳이 있으면
                    flag=0 # 플래그로 체크한다.
                    break
    if flag ==1: # 플래그로 체크된 게 없으면 카운터 증가
        cnt+=1
print(cnt)            
