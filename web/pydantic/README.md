# Pydantic

데이터 검증 라이브러리

1. Schema / 데이터 유효성 검사
2. 정규식, 내장 검증로직( Email 등) 지원
3. Serialization / Deserialization (JSON / Dict 변환)
4. FastAPI , LangChain 데이터 구조 정의에서 다 사용함

---

모든곳에서 다 써야하는가?

Client의 입력데이터는 검증이 필요하지만 DB의 데이터는 이미 검증된 데이터가 저장된다.
따라서 Pydantic은 입력검증만, 비즈니스 로직 검증은 Service Layer에서 처리한다.

Client <-> FastAPI : Pydantic
FastAPI <-> DB : dataclass
