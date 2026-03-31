###############
# boolean
###############
is_ready = True
print(is_ready)
print(type(is_ready))

print  (True + True + True - False)
###############
# none
###############
result = None
print(result)
print(type(result))

my_weapon = None # "" , 0 과는 다름
if my_weapon is None: # 파이썬 관례
    print("공격 : 맨주먹으로 하기!")

my_weapon = "칼"
if my_weapon is not None:
    print(f"공격 : {my_weapon}으로 하기!")
