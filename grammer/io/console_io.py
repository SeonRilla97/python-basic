import datetime

name =input ("이름이 뭐예요?\n") # 홍길동
user_year =input ("몇 년생인가요?\n") # 1997
print(f"반갑습니다 {name}님은 {datetime.date.today().year - int(user_year)+1}살이시군요!")