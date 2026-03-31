cart = ["사과","바나나","포도"]

print(cart)
print("-" * 20)

# Insert
cart.append("우유")
print(f'추가 후 카트 확인 : {cart}')

# Update 
cart[1] = "딸기"
print(f'수정 후 카트 확인 : {cart}')
print("-" * 20)

# Read
print(f'중간 2개만 출력: {cart[1:3]}')
print(cart[0])
print(cart[1])
print(cart[-1])

#Delete 
del cart[0]
print(f'삭제 후 카트 확인 : {cart}')