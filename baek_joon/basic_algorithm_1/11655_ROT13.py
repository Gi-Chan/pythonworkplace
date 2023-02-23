word= input()
rot = ""

for i in word:
    code=0
    if i.isspace():
        rot +=" "
        continue
    
    elif i.isdigit():
        rot+=str(i)
        continue
    
    if i.islower():
        code = ord(i)
        if ord(i)+13 >122:
            code = code - 26+13
        else:
            code+=13
    elif i.isupper():
        code = ord(i)
        if ord(i)+13 >90:
            code = code - 26+13 
        else:
            code+=13
    rot+=chr(code)

print(rot)