
### 1. 상속 (Is-a) 구현: 공통 분모(Member) 만들기
class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
    
    def login(self):
        print(f"🔑 [Member] {self.name}님이 로그인했습니다.")

# 자식 1: 학생
class Student(Member): # Student is a Member
    def study(self):
        print(f"📖 [Student] {self.name}님이 공부를 합니다.")

# 자식 2: 강사
class Instructor(Member): # Instructor is a Member
    def teach(self):
        print(f"👨‍🏫 [Instructor] {self.name}님이 강의를 합니다.")

### 2. 합성 (Has-a) 구현: 부품(Material) 만들기
class Material:
    def __init__(self, content):
        self.content = content
    
    def download(self):
        print(f"📥 다운로드 중: {self.content}")

class Lecture:
    def __init__(self, title):
        self.title = title
        # Lecture has a Material (강의는 자료를 가짐)
        # 생성자에서 부품 객체를 생성하여 소유
        self.material = Material(title + "_강의자료.pdf")

    def show_material(self):
        print(f"[{self.title}] 자료 확인:")
        self.material.download() # 내 기능이 아니라 부품에게 위임        
        
print("\n=== 1. 상속 관계 확인 (Is-a) ===")
# 학생 생성 (Member의 __init__ 사용)
s = Student("철수", "S001")
s.login() # 부모 기능 사용
s.study() # 내 기능 사용

# 강사 생성
i = Instructor("김강사", "T001")
i.login() # 부모 기능 사용
i.teach() # 내 기능 사용


print("\n=== 2. 포함 관계 확인 (Has-a) ===")
lec = Lecture("파이썬 기초")
lec.show_material() # 내부적으로 Material 객체의 메서드 호출

lec = Lecture("자바 기초")
lec.show_material() # 내부적으로 Material 객체의 메서드 호출        