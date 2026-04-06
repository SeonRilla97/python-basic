from auth.users import login_to_keycloak

# Keycloak 환경 설정
# 실제 운영 환경에서는 환경 변수(.env) 등으로 빼서 관리하는 것이 좋습니다.
KEYCLOAK_URL = "https://auth.dev.neopangea.link" # Keycloak 서버 주소
REALM_NAME = "seon-test"                 # 설정하신 Realm 이름
CLIENT_ID = "resource-service"         # 설정하신 Client ID
CLIENT_SECRET = "8Qa5Q2eDSGtldNB4RSIBKdnyHqDa8bNV" # 클라이언트 설정이 Confidential 기능 활성화 시 필요함

if __name__ == "__main__":
    print("===========================================")
    print("      Keycloak 로그인 시뮬레이션 시작      ")
    print("===========================================\n")

    # TODO: Keycloak에 실제로 등록되어 있는 유저의 아이디와 패스워드로 수정 후 실행하세요.
    test_username = "seon"
    test_password = "Tobe0701!"
    
    print(f"[{test_username}] 계정으로 Keycloak 로그인 시도 중...")
    
    tokens = login_to_keycloak(
        keycloak_url=KEYCLOAK_URL,
        realm_name=REALM_NAME,
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        username=test_username,
        password=test_password
    )
    
    if tokens:
        print("\n[발급된 토큰 정보]")
        print("-" * 50)
        print(f"🔑 Access Token: {tokens['access_token'][:80]}... (이하 생략)")
        print("-" * 50)
        print(f"🔄 Refresh Token: {tokens['refresh_token'][:80]}... (이하 생략)")
        print("-" * 50)
        print(f"⏱️ Access Token 만료 시간(초): {tokens['expires_in']}")
        print("-" * 50)
        
        print("\n💡 이제 프론트엔드/클라이언트가 API를 호출할 때, 이 Access Token을 HTTP Header(Authorization: Bearer <token>)에 담아 보내게 됩니다.")
