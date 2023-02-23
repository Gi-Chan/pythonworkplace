n = input()
replace_alpha = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

"""
https://ooyoung.tistory.com/74
위 블로그를 참고해서 풀었다.

변경해야할 문자가 총 8개 이므로 배열에 담는다.

크로아티아 알파벳 배열을 돌며 
입력받은 문자열 중 크로아티아 알파벳에 해당되는 게 있으면
해당하는 문자열은 크로아티아 알파벳 기준 1글자이므로
'@'로 대체한다.


"""

for i in replace_alpha:
    n = n.replace(i, "@")

print(len(n))