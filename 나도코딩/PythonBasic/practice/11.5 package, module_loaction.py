import inspect
import random
from travel import *
trip_to = thailand.ThailandPackage()
trip_to.detail()

# inspect를 호출하고 inspect.getfile(모듈명)을 입력하면 파일 위치 반환

print(inspect.getfile(random))
print(inspect.getfile(thailand))