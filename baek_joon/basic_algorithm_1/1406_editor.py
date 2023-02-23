import sys

word = sys.stdin.readline().strip()
left_word = list(word)
right_word = []


n=int(sys.stdin.readline())
for i in range(n):
    com = sys.stdin.readline().split()
    
    if com[0]=='L':
        if len(left_word)>0:
            right_word.append(left_word.pop())
    elif com[0]=='D':
        if len(right_word)>0:
            left_word.append(right_word.pop())
    elif com[0]=='B':
        if len(left_word)>0:
            left_word.pop()
    elif com[0]=='P':
        left_word.append(com[1])


p_word = left_word+list(reversed(right_word))

for i in p_word:
    print(i,end='')