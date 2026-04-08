'''
Abstract Base Class 

- 카드 결제는 Pay 구현, 계좌이체 결제는 Pay가 없어 에러나는것을 확인할 수 있음
'''

from abc import ABC, abstractmethod

# 인스턴스 생성 불가, 오버라이딩 강제
class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class CardPayment(Payment):
    def pay(self, amount):
        print("카드 결제")

class BankPayment(Payment):
    def refund(self, amount):
        print("계좌 이체 환불")

def pay(method, amount):
    method.pay(amount)

pay(CardPayment(), 1000)
pay(BankPayment(), 2000)
