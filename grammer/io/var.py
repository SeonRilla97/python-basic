# 변수 선언
menu ="아메리카노"
price = 4500
count = 3

# 변수 사용
total = price * count
print(f"주문하신 메뉴는 {menu} {count}잔이고 총 금액은 {total}원입니다.")

# 변수 값 변경 (재할당)
# 가격 인상
price = 5000
total = price * count
print(f"주문하신 메뉴는 {menu} {count}잔이고 총 금액은 {total}원입니다.")

# 상수 (대문자 약속)
TAX_RATE = 0.1
tax = total * TAX_RATE
print(f"세금은 {tax}원입니다.")