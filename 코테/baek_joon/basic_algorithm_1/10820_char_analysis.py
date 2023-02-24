import sys



while True:
    words = sys.stdin.readline().rstrip('\n')
    
    if not words:
        break
    small, big, num, space =0,0,0,0
    for i in words:
        if i.islower():
            small+=1
        elif i.isupper():
            big+=1
        elif i.isdigit():
            num+=1
        elif i.isspace():
            space+=1
    print(small, big, num, space) 

