word_list=list(input())
tag=False
word=''
words=''
for i in word_list:
  
    ## tag가 false 면 i 뒤에 word를 붙인다 (거꾸로 붙이는 거)
    if tag==False:
        if i=='<':
            tag=True
            word=word+i
        #중간점검
        elif i==' ':
            word=word+i
            words=words+word
            word=''
        else:
            word=i+word

    # tag가 true면 word 뒤에 i 를 붙임 (정상적으로 붙인느 거)
    elif tag==True:
        word=word+i
        if i=='>':
            tag=False
            words=words+word
            word=''

print(words+word)