# Section 04-4
# 파이썬 데이터 타입(자료형)
# 딕셔너리, 집합 자료형

# 딕셔너리(Dictionary) : 순서X, 중복X, 수정o, 삭제O

# Key, Value (Json) -> MongoDB
# 선언
a = {'name': 'kim', 'Phone' : '010-7777-7777', 'birth': 870214,'name': 'Park'}
b = {0: 'Hello Python', 1: 'Hello Coding'}
c = {'arr': [1,2,3,4,5]}

# print(type(a))

# 출력
print(a['name'])
print(a.get('name'))
print(a.get('address'))
print(c['arr'][1:3]) # 슬라이싱 처리

# 딕셔너리 추가
a['address'] = 'Seoul'
print(a)
a['rank'] = [1, 3, 4]
a['rank2'] = (1,2,3)
print(a)

# keys, values, items
print(list(a.keys()))

temp = list(a.keys())
print(temp[1:3])

print(a.values())

print(list(a.values()))

print(list(a.items()))
print(2 in b)
print('name2' not in a)


# 집합(Sets) (순서X, 중복X)
a = set()
b = set([1, 2, 3, 4])
c = set([1, 4, 5, 6, 7])
print(type(a))
print(c)

t = tuple(b)
print(t)
l = list(b)
print(l)

s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4,5,6,7,8,9])
print(s1.intersection(s2))
print(s1 & s2)
print(s1 | s2)
print(s1.union(s2))
print(s1-s2)
print(s1.difference(s2))

# 추가 & 제거
s3 = set([7, 8, 10, 15])

s3.add(18)
s3.add(7)

print(s3)

s3.remove(15)