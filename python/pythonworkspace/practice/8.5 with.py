# import pickle

# with open("profile.pickle", "rb") as profile_file: 
# # ㄴprofile.pickle 파일을 열어서 profile_file 이라는 변수로 저장함 
#     print(pickle.load(profile_file)) 
# 파일 close 할 필요 없음


# 2줄로 파일 만들어서 내용 쓰기
# with open("study.txt", "w", encoding="utf8") as study_file:
#     study_file.write("파이썬을 열심히 공부하고 있어요")

with open("study.txt", "r", encoding="utf8") as study_file:
    print(study_file.read())