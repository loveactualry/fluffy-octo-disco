# Section07-2
# 파이썬 클래스 상세 이해
# 상속, 다중상속

# 예제1
# 상속 기본
# 슈퍼클래스(부모) 및 서브 클래스(자식) -> 모든 속성, 메소드 사용 가능

# 중복 코드 최소화 코드의 생산성..

# 라면 -> 속성(종류, 회사, 맛,  면 종류, 이름) : 부모 클래스 

# car class 인스턴스 화
class car:
    """ parent calss """
    def __init__(self, tp, color):
        self.type = tp
        self.color = color

    def show(self):
        return 'Car Class "show method!"'

    
    # 클래스 상속 받아서 car 클래스에 있는 메소드 사용 가능
class BmwCar(car):
    """Sub Class"""
    def __init__(self, car_name, tp, color):
        super().__init__(tp, color) # 부모가 super class
        self.car_name = car_name # 물려 받을거는 받고 내가 사용할거는 사용.
    
    def show_model(self) -> None:
        return "Your Car Name : %s"% self.car_name

# super calss car, subclass BenzCar, BmwCar
class BenzCar(car):
    """Sub Class"""
    def __init__(self, car_name, tp, color):
        super().__init__(tp, color) # 부모가 super class
        self.car_name = car_name # 물려 받을거는 받고 내가 사용할거는 사용.
    
    def show_model(self) -> None:
        return "Your Car Name : %s"% self.car_name

    def show(self):
        print(super().show()) # 부모 클래스 소환
        return 'Car Info : %s %s %s' % (self.car_name, self.type, self.color)


# 일반 사용
# 부모와 자식 다 가져올 수 있다.

model1 = BmwCar('520d', 'sedan', 'red')

print(model1.color) # Super
print(model1.type) # Super
print(model1.car_name) #Sub
print(model1.show()) # Super class에 구현 되어 있다.
print(model1.show_model())  # Sub
print(model1.__dict__) # 부모와 자식 상속을 다 받음을 확인 가능

print()

# Method Overriding(오버라이딩)
model2 = BenzCar("220d", "suv", "black")
print(model2.show()) # 현재 메소드는 sub class에 가지고 온 것. 상속 받을 것 가지고 오고 새로 추가할 것을 가지고 온다. 목적에 맞게 재구현

# Parent Method Call
model3 = BenzCar("350s", "sedan", "silver")
print(model3.show()) # 부모 클래스도 소환된다.

# Inheritance Info(상속정보)
print(BmwCar.mro()) # 상속관계 보기
print(BenzCar.mro())

# 예제2
# 다중 상속

class X():
    pass

class Y():
    pass

class Z():
    pass

class A(X, Y):
    pass

class B(Y, Z):
    pass

class M(B, A, Z):  # 모든 클래스 사용 가능 다중 상속
    pass

print()

print(M.mro())
print(A.mro())