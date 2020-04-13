# Section06
# 파이썬 함수식 및 람다(lambda)


# 함수 정의 방법
# def 함수명(parameter):
#   code

# 함수 호출
# 함수명(parameter)

# 함수 선언 위치 중요

def hello(world):
    print("Hello  ", world)



hello("Python")
hello(7777)


# 예제2
def hello_return(world):
    val = "Hello " + str(world)
    return val

str = hello_return("Python!!!!!!!!")
print(str)


# 예제3(다중리턴)
def func_mul(x):
    y1 = x * 100
    y2 = x * 200
    y3 = x * 300
    return y1, y2, y3

val1, va12, val3 = func_mul(100)
print(type(val1), val1, va12, val3)

# 예제4(데이터 타입 변환)
def func_mul2(x):
    y1 = x * 100
    y2 = x * 200
    y3 = x * 300
    return (y1, y2, y3) # 리스트나 튜플 등으로 반환


lt = func_mul2(100)
print(lt, type(lt))

# 예제 4
# *args, *wkargs

def args_func(*args):
    print(type(args))

args_func('kim', 'park', 'lee')

# 다양한 매개 변수 형태로 함수의 흐름이 변한다. 튜플 형태로 변환

def args_func2(*args): # 가변 튜플 여러개
    for i, v in enumerate(range(1,10)):
        print(i, v)

# kwargs

def kwargs_func(**kwargs): # ** 딕셔너리
    for k, v in kwargs.items(): # key와 value 가져오기
        print(k, v)

kwargs_func(name1='kim')
kwargs_func(name1='kim', name2='park', name3='lee')

## 32강...!

# 전체 혼합
def example_mul(arg1, arg2, *args, **kwargs): # 가변인자 입력
    print(arg1, arg2, args, kwargs)

example_mul(10, 20)
example_mul(10, 20, 'park', 'kim', age1=24, age2=34) # 튜플 딕셔너리 등으로 포함 가능. 효율적인 코드로.


# 예제 5
# 중첩함수(클로저)

def nested_func(num):
    def func_in_func(num):
        print('>>>', num) # 여기는 함수 선언만.
    print("in func") # 그다음에 in func 실행해준다.
    func_in_func(num + 10000) # num 에 숫자를 더해준다.  그리고 func_in_func로 num이 넘어가 20000을 출력해준다.

nested_func(10000)

# 예제 6
# 힌트
def func_mul3(x : int) -> list:
    y1 = x * 100
    y2 = x * 200
    y3 = x * 300
    return (y1, y2, y3) # 리스트나 튜플 등으로 반환

print(func_mul(5.0))

# 람다식 예제
# 람다식 : 메모리 절약, 가독성 향상. 코드 간결
# 함수는 객체 생성 -> 리소스(메모리) 할당
# 람다는 즉시 실행(Heap 초기화) -> 메모리 초기화

# 일반적 함수 -> 변수 할당
def mul_10(num : int) -> int:
    return num * 10

var_func = mul_10
print(var_func)
print(type(var_func))

print(var_func(10))

lambda_mul_10 = lambda num : num * 10

print('>>>', lambda_mul_10(10))

def func_final(x, y, func):
    print(x * y * func(10))

func_final(10, 10, lambda_mul_10)

print(func_final(10, 10, lambda x : x * 1000))

# 1000 * 10 (람다에서) -> 10000 * 10 * 10 1000000 이 된다.
