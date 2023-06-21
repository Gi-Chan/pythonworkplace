
t = int(input())


for i in range(t):
    s = input()
    # s를 슬라이싱하며 슬라이딩 된것의 합을 리스트에 넣고 min값 출력하자
    sum_s = []
    for j in range(1, len(s)):
        s_1 = int(s[:j])
        s_2 = int(s[j:])
        # print(s_1+s_2)
        sum_s.append(s_1+s_2)
    print(f'#{i}', min(sum_s))
    
