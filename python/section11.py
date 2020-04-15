# Section11
# 파이썬 외부 파일 처리
# 파이썬 excel, CSV 파일 읽기 및 쓰기

# CSV : MIME - text/csv

import csv

# 예제1
with open('./resource/sample1.csv', 'r') as f:
    reader = csv.reader(f)
    # next(reader) # 헤더 스킵 한번 더 쓰면 0,1 안읽음
    #확인
    print(reader)
    print(type(reader))
    print(dir(reader))
    
    print()

    # dir 해서 iter 가 있는 것을 확인해 for 문 사용
    for c in reader:
        print(c)

print('_______')

# 예제2
with open('./resource/sample2.csv', 'r') as f:
    reader = csv.reader(f, delimiter ='|')
    # next(reader) # 헤더 스킵 한번 더 쓰면 0,1 안읽음
    #확인
    print(reader)
    print(type(reader))
    print(dir(reader))
    
    print()

    # dir 해서 iter 가 있는 것을 확인해 for 문 사용
    for c in reader:
        print(c)




# 예제 3 (Dict 변환)

with open('./resource/sample1.csv', 'r') as f:
    reader = csv.DictReader(f)

    for c in reader:
        #print(c) # 태그를 가지고 한다.
        for k, v in c.items():
            print(k, v)
        print('-----------------')


# 예제4
w = [[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15],[16,17,18]]

with open('./resource/sample3.csv', 'w', newline='') as f: # newline은 엔터를 한번만 쳐주기. 지금 wrtier와 writerow에서 한번씩 줄 바꿈을 해줘서 두번씩 해주는 상황이 되었음. 그래서 false 해줌
    wt = csv.writer(f)

    for v in w:
        wt.writerow(v)


# 예제5
with open('./resource/sample4.csv', 'w', newline='') as f:
    wt = csv.writer(f)
    wt.writerows(w) # 전부다 읽는 경우.

# XSL, XLSX
# openpyxl, wlsxwriter, xlrd, xlwt, xlutils
# pandas를 주로 사용
# pip install xlrd
# pip install openpyxl
# pip install pandas


import pandas as pd

# sheetname = '시트명' 또는 숫자, header='숫자', skiprow=숫자
xlsx = pd.read_excel('./resource/sample.xlsx')

# 상위 데이터 확인
print(xlsx.head())
print()

print(xlsx.tail())

xlsx.tail()

print(xlsx.shape)

# 엑셀 or csv 다시 쓰기

xlsx.to_excel('./resource/result.xlsx', index=False)
xlsx.to_csv('./resource/result.csv', index=False)



