'''
오버라이딩
덕타이핑
'''

def pay(method, amount):
    if method =="CARD":
        print("카드 결제")
    elif method =="BANK":
        print("계좌 이체 결제")
    elif method =="PAYPAL":
        print("페이팔 결제")
    elif method =="KAKAO":
        print("카카오페이 결제")
    else:
        print("잘못된 결제 수단입니다.")


class Payment:
    def pay(self, amount):
        pass

class CardPayment(Payment):
    def pay(self, amount):
        print("카드 결제")

class BankPayment(Payment):
    def pay(self, amount):
        print("계좌 이체 결제")

class PaypalPayment(Payment):
    def pay(self, amount):
        print("페이팔 결제")

class KakaoPayment(Payment):
    def pay(self, amount):
        print("카카오페이 결제")

class NaverPayment(Payment):
    def pay(self, amount):
        print("네이버페이 결제")

# 덕타이핑 - pay 메서드만 있으면 됨 (상속 없어도 Pay라는 행위를 하면 Pay를 할 수 있다)
class CryptoCurrency:
    def pay(self, amount):
        print("암호화폐 결제")

def pay(method, amount):
    method.pay(amount)

pay(CardPayment(), 1000)
pay(BankPayment(), 2000)
pay(PaypalPayment(), 3000)
pay(KakaoPayment(), 4000)
pay(NaverPayment(), 5000)
pay(CryptoCurrency(), 6000)