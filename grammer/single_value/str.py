str1 = "Hello"
str2 = 'Python'
print(str1, str2)

print ("-" * 20)

# 문자열 연산
print("안녕" + "하세요")
print ('ㅋ' * 3 )

# 길이 & 인덱싱 
text = "Hello"
print (f"원본{text}")
print (f"길이{len(text)}")
print (f"첫글자{text[0]}")
print (f"마지막글자{text[-1]}")

# 슬라이싱 [시작:끝] - 끝 번호는 포함 안됨
print (f"Hello의 두번째 글자부터 끝까지: {text[1:]}")
print (f"Hello의 처음부터 세번째 글자까지: {text[:3]}")