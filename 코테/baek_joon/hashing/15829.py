l = int(input())
# -96
w_list =[*input()]
m = 1234567891
sum=0

for i in range(len(w_list)):
    ar =ord(w_list[i])-96 # 해당 알파벳에 아스키코드 -96 < 이거하면 a가 1, b가 2 ...
    sum += (ar)*(31**i) 

print(sum% m)