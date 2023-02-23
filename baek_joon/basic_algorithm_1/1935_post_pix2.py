n = int(input())
word = list(input())
num =[]
for i in range(n):
    inp = int(input())
    num.append(inp)

stack = []

for i in word:
    if i>='A' and i<='Z':
        stack.append(num[ord(i)-ord('A')])
    
    else:
        num1 = stack.pop()
        num2 = stack.pop()
             
        if i =='*':
            stack.append(num2 *num1)
            
        elif i=='+':
            stack.append(num2+num1)

        elif i=='/':
            stack.append(num2/num1)
        
        elif i=='-':
            stack.append(num2-num1)
            
print("{:.2f}".format(stack[-1]))