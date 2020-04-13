# section08
# 파이썬 모듈과 패키지

# 패키지 예제
# 상대 경로
# .. : 부모 디렉토리
# . : 현재 디렉토리

# 사용1 (클래스)

from pkg.fibonacci import Fibonacci

Fibonacci.fib(300)

print("ex1 : ", Fibonacci.fib2(400))
print("ex1 : ", Fibonacci().title) # 인스턴스화 하고 호출

# 사용2(클래스, 권장하지는 않음)

from pkg.fibonacci import *

Fibonacci.fib(300)

print("ex2 : ", Fibonacci.fib2(600))
print("ex2 : ", Fibonacci().title) # 인스턴스화 하고 호출


# 사용3(클래스, 권장)

from pkg.fibonacci import Fibonacci as fb # alias 만들어줌

fb.fib(1000)

print("ex3 : ", Fibonacci.fib2(600))
print("ex3 : ", Fibonacci().title) # 인스턴스화 하고 호출


# 사용4(함수)
import pkg.calculations as c

print("ex4 :", c.add(10, 100))
print("ex4 :", c.mul(10, 300))

# 사용5(함수)
from pkg.calculations import div as d # 필요한 것만
print("ex5 :", int(d(100,10)))

# 사용6

import pkg.prints as p
import builtins
p.prt1()
p.prt2()
print(dir(builtins))