'''
Python 의 캡슐화

1. _ (관용적 - 실제 언어적인 지원이 아님)
2. __ (Name Mangling - 실제 언어적인 지원)
3. @property (Getter, Setter) => 서비스 로직에서 마치 필드를 사용하는것처럼 보이는게 진짜 맞는 방식인지?


결론 : 관용적 방법인 _ 로 필드를 구성, 메서드로 로직을 열면된다.
    - 보기 싫다면 Java나 Go로 갈것
'''
class Student:
    def __init__(self, name, gpa):
        # 1. 변수 앞에 __(언더바 2개)를 붙여서 비공개(Private)로 만듦
        # 외부에서 self.__name으로 직접 접근 불가
        self.__name = name 
        self.__gpa = gpa 

    # 2. 읽기 전용 속성 (Getter)
    # @property를 붙이면 메서드를 '변수처럼' 호출할 수 있음 (괄호 생략)
    @property
    def name(self):
        return self.__name

    # 3. 읽기/쓰기 속성 (Getter + Setter)
    # 학점(gpa)은 조회도 가능하고 수정도 가능해야 함
    @property
    def gpa(self):
        return self.__gpa

    # Setter: 값을 대입할 때 자동으로 실행되는 메서드
    # 여기서 유효성 검사(Validation) 로직을 수행함
    @gpa.setter
    def gpa(self, value):
        # 검증 로직: 학점은 0.0 ~ 4.5 사이여야 함
        if value < 0.0 or value > 4.5:
            print(f"🚫 오류: 학점은 0.0 ~ 4.5 사이여야 합니다. (입력값: {value})")
            return
        
        self.__gpa = value
        print(f"✅ 학점이 {value}로 안전하게 수정되었습니다.")

print("=== 2. 캡슐화 적용 (데이터 보호) ===")
std = Student("영희", 3.5)

# (1) @property 덕분에 메서드를 변수처럼 사용 (Getter 호출)
# std.name() 이라고 쓰지 않음!
print(f"학생 이름: {std.name}") 
print(f"현재 학점: {std.gpa}")

# (2) 값 변경 시도 (Setter 호출)
print("\n[테스트 1] 정상 범위 학점 입력")
std.gpa = 4.0  # 변수에 값을 넣는 것처럼 보이지만, 실제로는 @gpa.setter 메서드가 실행됨

# (3) 잘못된 값 입력 시도 (유효성 검사 작동)
print("\n[테스트 2] 비정상 학점 입력 (999.0)")
std.gpa = 999.0  # Setter 내부의 if문에서 걸러짐 (값 변경 안 됨)
print(f"-> 변경 확인: {std.gpa} (그대로 유지됨)")

# (4) 읽기 전용 속성 변경 시도
print("\n[테스트 3] 이름(Read-only) 변경 시도")
try:
    std.name = "해커"  # name에는 @setter를 만들지 않았으므로 수정 불가
except AttributeError as e:
    print(f"🚫 오류 발생: {e}")
    print("-> 이름은 읽기 전용이라 변경할 수 없습니다.")

# (5) 비공개 변수 직접 접근 시도
print("\n[테스트 4] __gpa 직접 접근 시도")
try:
    print(std.__gpa)
except AttributeError:
    print("🚫 오류: 'Student' object has no attribute '__gpa'")
    print("-> 외부에서는 __ 변수를 볼 수 없습니다. (정보 은닉)")

# (6) Name Mangling 확인 (비밀의 문)
# 파이썬은 내부적으로 이름을 '_클래스명__변수명'으로 바꿉니다.
# 강제로 접근하려면 할 수는 있지만, "건드리지 말라"는 약속입니다.
print(f"\n[참고] 실제 저장된 이름: {std._Student__gpa}")