# Section09
# 파일 읽기, 쓰기
# 읽기 모드 : r, 쓰기 모드(기존 파일 삭제):w, 추가모드(파일 생성 또는 추가) : a
# .. : 상대경로, . : 절대 경로


# 파일 읽기
# 예제 1
f = open('./resource/review.txt', 'r')
content = f.read()
print(content)
print(dir(f))
# 반드시 close 리소스 반환
f.close()

print("--------------")

# 예제2
with open('./resource/review.txt', 'r') as f:
     # with를 쓰면 close를 안해도 된다.
     c = f.read()
     print(list(c))
     print(iter(c))


print("-----------------")
print("-----------------")

# 예제3
with open('./resource/review.txt', 'r') as f:
    for c in f:
      print(c.strip())


print("-----------------")
print("-----------------")


# 예제4
with open('./resource/review.txt', 'r') as f:
    content = f.read()
    print(">", content)
    content = f.read()
    print(">", content) # 내용이 없음 한줄 한줄 읽는다.


print("-----------------")
print("-----------------")


# 예제5
with open('./resource/review.txt', 'r') as f:
    line = f.readline()
#    print(line)  # 한줄만 읽는다.  
    while line: # 라인별로 읽고 한줄한줄 읽는다. 없으면 0이 되어서 아웃
        print(line, end= '#####')
        line = f.readline()


print("-----------------")
print("-----------------")


# 예제6
with open('./resource/review.txt', 'r') as f:
    contents = f.readlines()
    print(contents)


print("-----------------")
print("-----------------")


# 예제6
with open('./resource/review.txt', 'r') as f:
    contents = f.readlines()
    print(contents)
    for c in contents:
        print(c, end = ' ***** ')
    # readlines는 리스트를 리턴한다.



print("-----------------")
print("-----------------")


# 예제7
score = []
with open('./resource/score.txt', 'r') as f:

    for line in f:
        score.append(int(line))
    print(score)

print('Average : {: 6.3}'.format(sum(score)/len(score)))

# 파일 쓰기

# 예제1
with open('./resource/text1.txt','w') as f:
    f.write('Niceman!\n')

# 에제2
with open('./resource/text1.txt', 'a') as f:
    f.write('Goodman!\n')


# 예제3

from random import randint

with open('./resource/text2.txt','w') as f:
    for cnt in range(6):
        f.write(str(randint(1, 50)))
        f.write('\n')

# 예제4
# writeline : 리스트 -> 파일 저장
with open('./resource/text3.txt','w') as f:
    list = ['kim\n', 'Park\n', 'cho\n ']
    f.writelines(list)

# 예제5
with open('./resource/text4.txt','w') as f:
    print('test contents1!', file = f)
    print('test contents2!', file = f) # 파일로 직접 쓴다. 로그성 파일 적을 때 한다.

    #read로 읽고 for문으로 반복한다.
