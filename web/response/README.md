[구조]

    HTTP_Version Status_Code Status_Text
    Header
    Blank Line
    Body

[예시]

    HTTP/1.1 200 OK
    Content-Type: application/json
    Content-Length: 88
    Date: Wed, 09 Apr 2026 08:47:43 GMT

    {
    "message": "Hello World",
    "status": "success"
    }

[Type]

```
    JsonResponse
    HTMLResponse
    RedirectResponse
    PlainTextResponse
    FileResponse
    StreamingResponse
```

[응답 코드]

```
2xx : 성공
    200 OK : 요청 성공
    201 Created : 생성 성공 (리소스 생성)
    204 No Content : 응답 내용 없음 (리소스 삭제)

3xx : 리다이렉션
    301 Moved Permanently : URL이 영구 이동
    302 Found : Method가 바뀔 때 (스펙 상 명시되어 있지 않지만, 여러 브라우저에서 이를 사용)
    303 See Other : Method가 바뀔 때 (스펙에 명시)
    307 Temporary Redirect : Method가 유지될 때 (스펙에 명시)


4xx : 클라이언트 오류
    400 Bad Request : 잘못된 요청
    401 Unauthorized : 인증 필요
    403 Forbidden : 접근 권한 없음
    404 Not Found : 리소스 없음
    405 Method Not Allowed : 허용되지 않는 메서드
    409 Conflict : 리소스 충돌
    410 Gone : 리소스 영구 삭제
    415 Unsupported Media Type : 지원하지 않는 미디어 타입
    422 Unprocessable Entity : 처리할 수 없는 요청
    429 Too Many Requests : 요청 과다

5xx : 서버 오류
    500 Internal Server Error : 서버 내부 오류
    501 Not Implemented : 서버 미구현
    502 Bad Gateway : 게이트웨이 오류
    503 Service Unavailable : 서비스 일시 중단
    504 Gateway Timeout : 게이트웨이 시간 초과
```
