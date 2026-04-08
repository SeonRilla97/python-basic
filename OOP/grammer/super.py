# 1. 부모 클래스 정의
class Parent:
    def __init__(self):
        self.money = 10000  # 부모가 가진 돈
        print("👴 [Parent] 생성자 실행: 부모의 돈(10000원) 세팅 완료")

# 2. 문제 상황: super()를 안 쓴 자식 (나쁜 예)
# -> 부모의 __init__을 덮어써버림 (Overriding)
class BadChild(Parent):
    def __init__(self):
        # super().__init__()  <-- 이 줄을 빼먹음!
        self.hobby = "게임"
        print("👶 [BadChild] 생성자 실행: 자식의 취미(게임) 세팅 완료")

# 3. 해결책: super()를 쓴 자식 (좋은 예)
class GoodChild(Parent):
    def __init__(self):
        # 1. 부모님, 먼저 오셔서 기본 세팅(money) 해주세요!
        super().__init__()
        
        # 2. 이제 제 것(hobby)을 세팅합니다.
        self.hobby = "코딩"
        print("🧑‍🎓 [GoodChild] 생성자 실행: 자식의 취미(코딩) 세팅 완료")


# ==========================================
# 4. 실행 및 테스트
# ==========================================

print("\n=== 1. 나쁜 자식 테스트 (super 누락) ===")
bad = BadChild()
print(f"취미: {bad.hobby}") # 자식 변수는 있음

try:
    # 부모의 변수(money)를 찾으려고 하면 에러 발생!
    print(f"용돈: {bad.money}") 
except AttributeError as e:
    print(f"🚨 에러 발생: {e}")
    print("-> 부모의 __init__이 실행되지 않아 'money' 변수가 없습니다!")


print("\n=== 2. 착한 자식 테스트 (super 사용) ===")
good = GoodChild()
print(f"취미: {good.hobby}")
print(f"용돈: {good.money}") # 부모 변수도 정상적으로 존재함
print("-> 성공! 부모의 돈과 자식의 취미를 모두 가집니다.")