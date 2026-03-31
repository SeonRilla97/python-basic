# 순서 X, 중복 불가 - 데이터가 있나? 없나? 

# 1. 셋 생성
fruits = {"사과","바나나","포도","사과"}
print(f'과일 셋 : {fruits}')

# [주의] 빈 Set 생성 시 set() 사용
empty_set = set()
empty = {}
print(f'타입 : {type(empty_set)}')
print(f'타입 : {type(empty)}')

print ('-' * 40)

# 추가
fruits.add("오렌지")
print(f'오렌지 추가 후 : {fruits}')

# 삭제 (Set 삭제 시 discard 사용 권장)
### remove : 없는 데이터 삭제 시 에러 발생
fruits.remove("바나나")
print(f'바나나 삭제 후 : {fruits}')
### discard : 없는 데이터 삭제 시 에러 없음
fruits.discard("망고")
print(f'망고 삭제 후 : {fruits}')

# 리스트 중복 제거  (리스트 -> 셋 -> 리스트)
numbers = [1,2,2,2,2,2,3,4,5,5,6,4,3]
unique_numbers = list(set(numbers))
print(f'중복 제거 후 : {unique_numbers}')

# 합집합, 교집합, 차집합
set_a = {1,2,3,4}
set_b = {3,4,5,6}

print(f'합집합 : {set_a | set_b}')
print(f'교집합 : {set_a & set_b}')
print(f'차집합 : {set_a - set_b}')
