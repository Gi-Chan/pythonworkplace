
import math
PI = math.pi
class Circle:

    def __init__(self, r=0):
        self.r = r
    
    def getArea(self):
        return PI *self._r * self.r
    
    def getPrimeter(self):
        return 2 * PI * self.r

c1 = Circle(10)
print("원의 면적 : ", c1.getArea())
print("원의 둘레 : ", c1.getPrimeter())


