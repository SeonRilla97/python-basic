# 타입 확인 type(데이터)
print(type(10))
print(type("10"))

# 형변환 int(),float(),str()
num_str1 = "10"
num_str2 = "20"
print (num_str1 + num_str2)

num_int1 = int(num_str1)
num_int2 = int(num_str2)
print (num_int1 + num_int2)

# 실무 input()
a = input("첫 번째 숫자 입력하세요: ")
b = input("두 번째 숫자 입력하세요: ")
print( a + b )
real_sum = int(a) + int(b)
print(real_sum)