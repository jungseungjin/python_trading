# {
#   "access_key": "발급 받은 acccess key (필수)",
#   "nonce": "무작위의 UUID 문자열 (필수)",
#   "query_hash": "해싱된 query string (파라미터가 있을 경우 필수)",
#   "query_hash_alg": "query_hash를 생성하는 데에 사용한 알고리즘 (기본값 : SHA512)"
# }

# Python 3

import jwt    # PyJWT 
import uuid
import hashlib
from urllib.parse import urlencode

# query는 dict 타입입니다.
# m = hashlib.sha512()
# m.update(urlencode(query).encode())
# query_hash = m.hexdigest()

payload = {
    'access_key': 'KBUI97KnJZT7ARRW9w0V2jgioE8c79CSDBXaPAC0',#엑세스
    'nonce': str(uuid.uuid4()),
    # 'query_hash': query_hash,
    # 'query_hash_alg': 'SHA512',
}
    
jwt_token = jwt.encode(payload, '48UqnMJOMmkc8EQ60CgSOXyKdZRwreEsSjxZxGVD')#시크릿
authorization_token = 'Bearer {}'.format(jwt_token)



# EXCHANGE API
# [주문 요청]

# 초당 8회, 분당 200회
# [주문 요청 외 API]

# 초당 30회, 분당 900회



# QUOTATION API
# Websocket 연결 요청 수 제한
# 초당 5회, 분당 100회
# REST API 요청 수 제한
# 초당 10회, 분당 600회 (종목, 캔들, 체결, 티커, 호가별 각각 적용)


