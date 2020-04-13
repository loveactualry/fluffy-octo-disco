for k in q1.keys():
    if k == '가을':
        print(q1[k])
    
for k in q1.items():
    if k == '가을':
        print(q1[k])


for k, v in q2.items():
    if v == '사과':
        print(k, v)
        break
else:
    print("사과 없음")



a = 77
if a >= 81:
    print("A학점")
elif a >= 61:
    print("B학점")
elif a >= 41:
    print("C 학점")
elif a >= 21:
    print("D 학점")
else:
    print("E학점")


a, b, c = 12, 6, 18

best = a

if b > a:
    best = b
if c > b:
    best = c
print('best : ', best)

if int(s[7]) % 2 == 1:
    print("남자")
else:
    print("여자")


for v in q3:
    if v == "정":
        continue
    else:
        print(v, end='')

q5= [x for x in q3 if x != '정']
print(q5)



print()

for n in range(1, 101):
    if n % 2 != 0:
        print(n, end =',')

for v in q4:
    if len(v) >= 5:
        print(v, end=',')

q6 = [x for x in range(1,101) if x %2 != 0]

for v in q5:
    if v.isupper():
        continue
    else:
        print(v, end = ' ')

for v in q6:
    if v.isupper():
        print(v.lower())
    else:
        print(v.upper())


# 리스트 컴프리헨션
a = [1,2,3,4]

numbers = []

for n in range(1,101):
    numbers.append(n)
print(numbers)

numbers2 = [x for x in range(1, 101)]
print(numbers2)

x = [x for x in range(1, 101) if 조건문]
