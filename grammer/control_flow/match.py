status = 400


match status:
    case 200:
        print("OK")
    case 400:
        print("Bad Request")
    case 404:
        print("Not Found")
    case 500:
        print("Internal Server Error")
    case _:
        print("Unknown")

# 패턴 매칭

command = ["go","east"]

match command:
    case ["go", direction]:
        print(f"이동합니다 {direction}")
    case ["attack", target]:
        print(f"공격합니다 {target}")
    case _:
        print("알 수 없는 명령어")