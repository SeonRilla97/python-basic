class Lecture:
    def __init__(self, title):
        self.title = title

    def print_info(self):
        print(self.title)

    def no_self_method():
        print("self가 없는 메서드")

my_lec = Lecture("파이썬")
my_lec.print_info()

# my_lec.no_self_method() # 에러 발생
Lecture.no_self_method()