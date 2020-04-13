# section 10
# 파이썬 예외처리의 이해

# 예외 종류
# 문법적으로 에러가 없지만, 코드 실행(런타임) 프로세스에서 발생하는 예외 처리도 중요
# linter : 코드 스타일, 문법 체크 


# SyntaxError : 잘못된 문법
print('test')

if True:
    pass

# x => y

# Name error : 참조변수 없음

a = 10
b = 15

# print(c)

# ZeropDivisonError : 0 나누기 에러
# print(10 / 0)

# IndexError : 인덱스 범위 오버

x = [10, 20, 30]
print(x[0])
# print(x[3])

# KeyError

dic = {'name': 'kim', 'Age': 33, 'City': "Seoul"}

# print(dic['hobby'])
print(dic.get('hobby'))


# AttributeError : 모듈, 클래스에 있는 잘못된 속성 사용시에 예외
import time
print(time.time())
# print(time.month())

# ValueError : 참조 값이 없을 때 발생
x = [1, 5, 9]

# x.remove(10)
# x.index(10)

# FileNotFoundError

# f = open('test.txt', 'r') # 예외 발생

# TypeError

x = [1, 2]
y = (1, 2)
z = 'test'

# print(x + y) # 예외
# print(x + z)

print(x + list(y)) # 예외

# 항상 예외가 발생하지 않을 것으로 가정하고 먼저 코딩
# 그 후 런타임 예외 발생시 예외 처리 코딩 권장(EAPP 코딩 스타일)

# 예외 처리 기본
# try : 에러가 발생할 가능성이 있는 코드 실행
# except : 에러명 1
# except : 에러명 2
# else : 에러가 발생하지 않았을 경우 실행
# finally : 항상 실행


# 예제1

name = ['Kim', 'Lee', 'Park']

try:
    z = 'Kim' # cho 예외발생
    x = name.index(z)
    print('{} Found it! in name'.format(z, x+1))
except ValueError: # value error 발생 예상
    print("not found it! - Ocurred ValueError!")
else:
    print('ok! else!')

# 예제 2


try:
    z = 'Jin'
    x = name.index(z)
    print('{} Found it! in name'.format(z, x+1))
except ValueError: # value error 발생 예상
    print("not found it! - Ocurred Error!")
else:
    print('ok! else!')



# 예제3

try:
    z = 'Kim'
    x = name.index(z)
    print('{} Found it! in name'.format(z, x+1))
except ValueError: # value error 발생 예상
    print("not found it! - Ocurred ValueError!")
else:
    print('ok! else!')
finally:
    print("finally ok!") # 전부 다 실행 에러 발생 여부 상관하지 않고 실행

# 예제 4
# 예외 처리는 하지 않지만, 무조건 수행되는 코딩 패턴

try:
    print('try')
finally:
    print('OK, Finally!')

# 예제 5

try:
    z = 'Kim'
    x = name.index(z)
    print('{} Found it! in name'.format(z, x+1))
# 계층적 에러 처리 순서를 주의해야 한다. Exception이 먼저면 안됨.

except ValueError as l: # value error 발생 예상
    print("not found it! - Ocurred ValueError!")
    # print(l) # alias를 l로 주고 print문 적용해줘도 된다.

except IndexError: # value error 발생 예상
    print("not found it! - Ocurred IndexError!")

except Exception: # value error 발생 예상
    print("not found it! - Ocurred Error!")
else:
    print('ok! else!')
finally:
    print("finally ok!")


# 예제6
# 예외 발생 : raise
# raise 키워드로 예외 직접 발생

try:
    a = '333'
    if a == 'Kim':
        print('ok 허가!')
    else:
        raise ValueError
except ValueError:
    print('문제 발생')
except Exception as f:
    print(f)
else:
    print('Ok!')




























