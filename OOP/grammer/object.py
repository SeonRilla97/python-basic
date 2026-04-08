class Lecture:
    def __init__(self, title, teacher, price):
        self.title = title
        self.teacher = teacher
        self.price= price
        self.students   = []

    def info(self):
        print(f"[강의 정보] {self.title} (강사: {self.teacher})")

# 학생 클래스
class Student:
    def __init__(self, name):
        self.name = name
        # 학생은 내가 듣는 강의 목록을 가짐
        self.my_lectures = []

    def study(self):
        print(f"\n📖 {self.name}님이 공부를 시작합니다.")
        for lecture in self.my_lectures:
            print(f" - '{lecture.title}' 복습 중...")

class CourseSystem:    
    # 수강 신청을 처리하는 핵심 메서드  
    # (학생 객체와 강의 객체를 매개변수로 받아서 연결해줌)
    def register_course(self, student, lecture):
        print(f"\n[System] 수강 신청 처리 중... (신청자: {student.name}, 강의: {lecture.title})")
        
        # 객체간 메시지 교환(메서드 호출)으로 상호작용
        # 다른 객체의 데이터에 직접 접근하지 않고, 메서드를 통해서 호출
        # 학생에게 강의 추가
        student.my_lectures.append(lecture)
        
        # 강의 명단에 학생 추가
        lecture.students.append(student)
        
        print("  -> ✔️ 등록이 완료되었습니다.")


print("=== 1. 시스템 및 데이터 객체 생성 ===")
# 관리자(시스템) 생성
my_lms = CourseSystem()

# 강의 생성
python_lec = Lecture("파이썬 기초", "코딩하는기술사", 50000)
java_lec = Lecture("자바의 정석", "이자바", 70000)

# 학생 생성
student1 = Student("철수")
student2 = Student("영희")


print("\n=== 2. 수강 신청 진행 (시스템을 통해서) ===")
# 학생이 직접 강의에 침투하는 게 아니라, 시스템에게 요청함
# my_lms.register_course(누가, 무엇을)

my_lms.register_course(student1, python_lec) # 철수 -> 파이썬
my_lms.register_course(student2, python_lec) # 영희 -> 파이썬
my_lms.register_course(student1, java_lec)   # 철수 -> 자바


print("\n=== 3. 결과 확인 ===")
# 학생은 공부를 한다 (본연의 임무)
student1.study()

# 강의는 수강생 현황을 보여준다
print(f"\n--- '{python_lec.title}' 수강생 현황 ({len(python_lec.students)}명) ---")
for s in python_lec.students:
    print(f"- {s.name}")