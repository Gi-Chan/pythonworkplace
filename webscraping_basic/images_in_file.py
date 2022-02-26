import os

# 폴더 이름
folder_name = "moveis_images"
os.mkdir(folder_name)

# 코드 실행 후 디렉토리 변경
location = os.getcwd() + "\\{}".format(folder_name)
os.chdir(location)

# 디렉토리 변경 후 파일 생성
with open("1.txt", "w", encoding="utf8") as f:
    f.write("hello world")