import os

# 1. 새로운 폴더를 만들고 그 안에 이미지 넣기

# # 폴더 이름
# folder_name = "moveis_images"
# os.mkdir(folder_name)

# # 코드 실행 후 디렉토리 변경
# location = os.getcwd() + "\\{}".format(folder_name)
# os.chdir(location)

# # 디렉토리 변경 후 파일 생성
# with open("1.txt", "w", encoding="utf8") as f:
#     f.write("hello world")


# 2. 폴더가 많으면 지저분하니 코드 공부 파일 안에 넣기


# 먼저 폴더 이동하기.
location = os.getcwd() + "\\webscraping_basic"
os.chdir(location) # 디렉토리 이동

# 폴더 생성
folder_name = "moveis_images"
os.mkdir(folder_name)

# 그 다음 또 이동
location = location + "\\{}".format(folder_name)
os.chdir(location)

# 디렉토리 변경 후 파일 생성
with open("1.txt", "w", encoding="utf8") as f:
    f.write("hello world")