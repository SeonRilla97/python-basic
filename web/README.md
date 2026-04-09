[FastAPI 완벽 가이드](https://www.inflearn.com/course/fastapi-%EC%99%84%EB%B2%BD-%EA%B0%80%EC%9D%B4%EB%93%9C/dashboard?cid=334741)

### 파이썬 기본 환경 구성

venv는 Git에 올라가지 않으니 이를 ./web 디렉토리에서 실행하여 구성할것

```
[가상환경 생성]
    python -m venv .venv

[가상환경 사용]
    source .venv/Scripts/activate  # [Windows Git Bash]

[가상환경 사용 안함]
    deactivate

[VSCode Python 가상환경 설정]
    ctrl + shift + p -> Python: Select Interpreter
    .venv/Scripts/python.exe을 선택

```

### 프로젝트 개발 환경 구성

```
[pip 업그레이드]
    python -m pip install --upgrade pip


[Lib 설치]
    pip install -r requirements.txt



[FastAPI 실행]
    - web 디렉토리에서 실행 (venv 실행 됐는지 확인 필요)
    - ASIG 규약을 준수한 uvicorn으로 서버를 실행한다.
    - pycache 폴더를 생성하지 않도록 한다.

    python -B -m uvicorn main:app --port=8081 --reload


[참고 :: Lib 추가]
    pip freeze > requirements.txt
```
