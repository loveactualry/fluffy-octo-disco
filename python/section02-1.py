# Section02-1
# 파이썬 기초 코딩
# print 구문의 이해

# 기본출력
print('Hello Python!')
print("Hello Python!")
print("""hello python!""")
print('''Hello Python!''')

print()


# Seprataor 옵션 사용

print('T', 'E', 'S', 'T', sep='')
print('2019', '02','19', sep='-')
print('niceman', 'goolge.com', sep='@')

# end 옵션 사용
print('welcome to ', end='')
print('the black parade', end='')
print('piano notes')
print('test')

# format 사용
print('{} and {}'.format('You', 'Me'))
print("{0} and {1} and {0}".format('You', 'Me'))
print("{a} ar {b}".format(a= 'you', b = 'Me'))

print("%s's favorite number is %d" %('Eunki', 7)) #%s 문자, %d 일반 정수, %f 실수,

print("Test1: %5d, Price: %4.2f" %(776, 6534.123)) # 5d인 경우 다섯자리 숫자의 정수가 온다고 지정. 세자리 네자리 등등
print("Test1: {0: 5d}, Price: {1: 4.2f}".format(776, 6534.123)) 
print("Test1: {a: 5d}, price: {b: 4.2f}".format(a=776, b =6534.123))

# 이스케이프 코드

print("'you'")
print('\'you\'')
print("""'you'""")
print('\\you\\\n\n\n\n\n\n\n')
print('\t\t\t\ttest')