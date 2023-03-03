# 구글에 pypi를 검색하면 패키지들을 모아놓은 사이트가 있음 pypi.org

# pip install beautifulsoup4 > 패키지 다운
# pip install --upgrade beautifulsoup4 > 패키지 업그레이드
# pip uninstall beautifulsoup4 > 패키지 삭제
# pip lit > 패키지 목록 출력
from bs4 import BeautifulSoup
soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
print(soup.prettify())