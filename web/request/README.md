'''
사용자의 요청 형식에 따라 처리하는 방법

[HTTP]
[구성]
Method URL Protocol_version
Header:
blank line
Body:

        [Method]
            GET : 정보 가져오기
            POST : 정보 생성
            PUT : 특정 정보 전체 업데이트
            DELETE : 특정 정보 삭제
            PATCH : 특정 정보 부분 업데이트
            HEAD : 헤더 가져오기
            OPTIONS : 서버가 지원하는 메서드 가져오기


    [예시]
        POST /users/123/posts?sort=desc&page=1 HTTP/1.1
        Host: api.example.com
        Content-Type: application/json
        Authorization: Bearer eyJhbGci...
        Cookie: session=abc123; theme=dark; lang=ko

        {
            "title": "안녕하세요",
            "content": "첫 번째 게시글입니다"
        }

이 중에서 다음을 처리하는 방법을 확인한다. 1. Path Parameter 2. Query Parameter 3. Request Body 4. Form

[Content-Type]
application/json
application/x-www-form-urlencoded
'''
