import pickle
# profile_file = open("profile.pickle", "wb") # w는 읽기 b는 바이너리 라는건데 피클은 이게 있어야함
# profile = {"이름":"정의찬", "나이":24, "취미":["축구", "요리", "웃음"]}
# print(profile)
# pickle.dump(profile, profile_file) # profile 에 있는 정보를 file 에 저장
# profile_file.close()


profile_file = open("profile.pickle", "rb")
profile = pickle.load(profile_file) # file 에 있는 정보를 profile 에 불러오기
print(profile)
profile_file.close()