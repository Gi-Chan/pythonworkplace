# 사진 파일 생성 후 파일에 보관하는 법을 알아 보려고 함.

from tkinter import image_names
import requests
from bs4 import BeautifulSoup
import os

# 먼저 폴더 이동하기.
location = os.getcwd() + "\\webscraping_basic"
os.chdir(location) # 디렉토리 이동

# 폴더 생성
folder_name = "moveis_images"
os.mkdir(folder_name)

# 그 다음 또 이동
location = location + "\\{}".format(folder_name)
os.chdir(location)

for year in range(2016, 2021):
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36"}
    url ="https://search.daum.net/search?w=tot&q={}%EB%85%84%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&DA=MOR&rtmaxcoll=MOR".format(year)
    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, "lxml")

    images = soup.find_all("img", attrs={"class":"thumb_img"})

    for idx, image in enumerate(images):
        # print(image["src"])
        image_url = image["src"]
        if image_url.startswith("//"):
            image_url = "https:" + image_url

        print(image_url)
        image_res = requests.get(image_url)
        image_res.raise_for_status()

        with open("movie_{}_{}.jpg".format(year, idx+1), "wb") as f:
            f.write(image_res.content)

        if idx >=4:
            break # 상위 5개 이미지까지만 다운로드