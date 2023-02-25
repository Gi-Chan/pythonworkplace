# 참고 https://wook-2124.tistory.com/257
# 입력받은 word를 set형태로 변환하여 사용된 알파벳만 걸러냄
word = input().upper()
word_set = list(set(word))
cnt_list=[]
for alpha in word_set:
    cnt = word.count(alpha)
    cnt_list.append(cnt)
# cnt_list에 각 알파벳의 개수를 측정함


if cnt_list.count(max(cnt_list))>=2:
    # count.max(cnt_list)에 max값이 여러개 카운팅 되는걸 배움
    print("?")
else:
    print(word_set[(cnt_list.index(max(cnt_list)))])
    # word_set에서 알파벳개수를 적은 리스트에서 가정 큰 값을 가지는 인덱스를 출력