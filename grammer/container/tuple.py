# 튜플 만들어
my_tuple = (1,2,3)
print(f'튜플 : {my_tuple}')
print(f'타입 : {type(my_tuple)}')

# 괄호 없어도 가능 (자동 패킹)
no_bracket = 1,2,3
print(f'괄호 없는 튜플 : {no_bracket}')
print(f'타입 : {type(no_bracket)}')

# 데이터 1개
not_tuple = (1)
one_tuple = (1,)
print(f'데이터 1개 : {not_tuple}')
print(f'데이터 1개 튜플 : {one_tuple}')
print(f'타입 : {type(not_tuple)}')
print(f'타입 : {type(one_tuple)}')

# 불변성 - 수정 불가
print (f'첫번째 값 : {my_tuple[0]}')
# my_tuple[0] = 10 # 에러 발생

### 튜플 사용법

# 1. 조회
data = (1,2,3,4,5,1,2,1,2,1)
print(f'1 개수 : {data.count(1)}개')

# 2. 위치 찾기
print(f'3의 index : {data.index(3)}')

# 3. len
print(f'데이터 개수 : {len(data)}개')

# 4. 포함 여부
print(f'2 포함 여부 : {2 in data}')
print(f'15 포함 여부 : {15 in data}')

# 5. 패킹 & 언패킹
packed = 100, 200
a, b = packed

x= 5; y=10
print(f'스왑 전 x: {x}, y: {y}')
x, y = y, x
print(f'스왑 후 x: {x}, y: {y}')
