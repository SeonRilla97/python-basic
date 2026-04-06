import requests

def login_to_keycloak(keycloak_url, realm_name, client_id, client_secret, username, password):
    """
    Direct Access Grants (Resource Owner Password Credentials) 방식을 사용하여
    마치 사용자가 로그인하는 것처럼 Keycloak에 직접 아이디/비밀번호를 보내고 Token을 받아오는 함수입니다.
    """
    # Keycloak의 Token 발급 엔드포인트 URL 조합
    token_url = f"{keycloak_url}/realms/{realm_name}/protocol/openid-connect/token"
    
    # Keycloak에 보낼 데이터 구성 (Form Data 형식)
    payload = {
        "grant_type": "password",
        "client_id": client_id,
        "username": username,
        "password": password,
    }
    
    # Keycloak Client 설정에서 "Client authentication"이 On(Confidential)으로 되어 있다면 아래 주석 해제
    if client_secret:
        payload["client_secret"] = client_secret

    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }

    try:
        # Keycloak 서버로 POST 요청 전송
        response = requests.post(token_url, data=payload, headers=headers)
        
        # HTTP 응답 코드가 200번대가 아닐 경우 에러 발생
        response.raise_for_status() 
        
        # JSON 형태의 응답을 파이썬 딕셔너리로 변환
        token_data = response.json()
        print("✅ 로그인 성공! Keycloak으로부터 Token을 성공적으로 발급받았습니다.\n")
        
        return {
            "access_token": token_data.get("access_token"),
            "refresh_token": token_data.get("refresh_token"),
            "id_token": token_data.get("id_token"),
            "expires_in": token_data.get("expires_in")
        }
        
    except requests.exceptions.RequestException as e:
        print(f"❌ 로그인 실패: {e}")
        # Keycloak이 반환한 구체적인 에러 메시지가 있다면 출력
        if 'response' in locals() and response is not None:
             print(f"상세 에러 내용: {response.text}")
        return None
