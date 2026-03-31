### 순서보다 이름(Key)이 중요할 때
my_profile = {
    "name": "파이썬",
    "age": 25,
    "hobby": "코딩"
}

print(f'내 프로필 {my_profile}')
print(f'타입: {type(my_profile)}')

# 조회 - get 사용
# print(f'이메일: {my_profile["email"]}')  # 없으면 에러남
email = my_profile.get("email") # 없으면 None 반환 
print(f'이메일 : {email }')

print("-" * 40)

# 추가
my_profile['age'] = 26
my_profile['job'] = "개발자"
print(f'추가 후 : {my_profile}')

# 삭제
del my_profile['hobby']
print(f'취미 삭제 후 : {my_profile}')

# Key & Value 따로 보기 
print(f'Key : {my_profile.keys()}')
print(f'Value : {my_profile.values()}')
print(f'Key & Value : {my_profile.items()}')
