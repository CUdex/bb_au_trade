# 파이썬에서는 기본적으로 듀플, 리스트, 딕셔너리 구조의 자료구조를 제공한다.
# 그러나 기본적으로 제공하는 자료구조로는 2차원 형태의 자료를 다루는데에는 한계가 존재한다.
# 이를 해결하기 위해서 Pandas라는 모듈을 이용합니다.
# Pandas는 1차원을 위한  series 타입과 2차원을 위한 data frame 타입을 제공하여 이를 활용한다
# 이를 이용하여 엑셀에 저장하거나 그래프로 시각화를 할 수 있다.

# 1차원 데이터 활용을 위해 Pandas의 series를 이용
from pandas import Series

# 리스트를 만들어 Series 생성자로 넘겨주면 Series 객체가 생성됩니다.
data = [100, 200, 300, 400]
s = Series(data)
print(s)

# 날짜와 값을 맵핑하여 Series 객체로 만들기
date = ['2021-01-02', '2021-01-03', '2021-01-04', '2021-01-05']
s2 = Series(data, date)
print(s2)

# Series에서는 딕셔너리와 마찬가지로 속성을 통해 원하는 index or values 값만을 나열할 수 있다.
print(s2.index)
print(s2.values)

# index 값을 이용해 여러개의 값을 한번에 인덱싱 할 수 있다.
print(s2[['2021-01-02', '2021-01-03', '2021-01-04']])

# 슬라이싱의 경우 리스트에서 [시작:끝] 값을 이용하여 슬라이싱을 하면 인덱스 끝은 포함하지 않았지만 Series의 경우 끝도 포함한다.
# 정수 값으로 슬라이딩 하면 마지막 값은 포함되지 않는다.
print(s2['2021-01-02' : '2021-01-05'])
# 정수의 경우 마지막 값은 포함되지 않는다.
print(s2[0:3])

# Series 객체에 값 추가
s2['2021-01-06'] = 600
print(s2)
# 값 삭제 drop의 경우 특정 값만 삭제된 새로운 객체만 리턴
print(s2.drop('2021-01-05'))
# 원본 데이터
print(s2)

# 사칙연산 적용
# 일반적인 리스트의 사칙연산 적용
testData = [100, 200, 300, 400]
listData = []
for val in testData :
    listData.append(val/10)
print(listData)

# Series 객체의 사칙연산 value에 적용
print(s2/10)
