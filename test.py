
def wei(height, gender):
    if gender == '남자':
        return height * height *22
    else:
        return 1


height = 167
gender ='남성'
weight = wei(height / 100 , gender)
weight = round(weight, 2)
print(weight)