"""Quiz) 사이트별로 비밀번호를 만들어 주는 프로그램을 작성하시오

예) https://naver.com
규칙1 : http:// 부분은 제외 => naver
규칙2 : 처음 만나는 점(.) 이후 부분은 제외 => naver
규칙3 : 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e' 갯수 + "!"로 구성
            (nav)                   (5)             (1)         (!)

예) 생성된 비밀번호 : nav51!"""

# site = "https://naver.com"
# site = "daum.net"
site = "https://youtube.com"
rule1 = site.replace("https://", "") # 규칙 1
rule2 = rule1[:rule1.find(".")] # 규칙 2

password = rule2[:3] + str(len(rule2)) + str(rule2.count("e")) + "!"

print(f"{site} 의 비밀번호는 {password} 입니다.")

