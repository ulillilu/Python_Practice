#데코레이터를 사용해 게터와 세터 만들기
import math

class Circle:
    #게터와 세터 선언
    def __init__(self, radius):
            self.__radius = radius
    def get_circumference(self):
        return 2 * math.pi * self.__radius
    def get_area(self):
        return math.pi * (self.__radius ** 2)

    def get_radius(self):
        return self.__radius
    def set_radius(self, value):
        self.__radius = value
        
    @property
    def radius(self):
        return self.__radius
    @radius.setter
    def radius(self, value):
        if value <= 0:
            raise TypeError("길이는 양의 숫자여야 합니다.")
        self.__radius = value

print("# 데코레이터를 사용한 Getter와 Setter")
circle = Circle(10)
print("원래 원의 반지름: ", circle.radius)
circle.radius = 2
print("변경된 원의 반지름: ", circle.radius)
print()

print("# 강제로 예외를 발생 시킵니다.")
circle.radius = -10