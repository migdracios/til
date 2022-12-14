# CS TIL
# 목차


# 데이터베이스
## 트랜잭션에 대해서 설명하고, ACID 규칙에 대해서도 설명하시오
트랜잭션이란 데이터베이스에서 데이터를 삽입, 갱신, 삭제하는 것의 논리적 작업을 완수하기까지의 일련의 과정의 작업 단위입니다.
데이터베이스에서 데이터를 조회한 뒤, 삽입/갱신/삭제를 실행하고 종료하는 것까지의 과정을 말합니다.
트랜잭션은 ACID라는 원자성/일관성/고립성/지속성 이라는 네 가지 특징을 가지고 있습니다.
이는 각각 트랜잭션이 완전히 끝나지 않을 경우 원상태로 돌아가는 것, 트랜잭션이 성공하면 데이터베이스는 모순 없이 일관적이어야 한다는 것, 각 트랜잭션이 연관되어 있지 않다는 것, 트랜잭션이 성공하면 결과를 영구적으로 보장한다는 것을 의미합니다.

## PK와 FK는 무엇입니까?
관계형 데이터베이스에서 레코드들 간의 데이터를 지칭할 수 있도록 식별자가 필요합니다. 이를 컬럼 형식의 데이터로 저장하여 사용하는 것을 키라고 합니다.
이 키는 핵심키와 외래키를 주로 사용하게 됩니다.
PK는 핵심키로, 각 레코드를 구분하는 칼럼 키 입니다. 테이블의 속성과 같은 칼럼으로 포함되어 있으며, 중복과 Null값을 허용하지 않습니다. 하나의 테이블에서 해당 테이블 내부의 레코드를 식별하기 위한 키입니다.
FK는 외래키로, 하나의 테이블에 관계가 있는 테이블의 레코드를 식별하기 위한 키입니다. 마찬가지로 칼럼으로 테이블에 포함되어 있지만, 속해 있는 테이블이 아닌 관계에 해당하는 테이블의 레코드를 식별하는 키입니다.

## HTTP와 HTTPS의 차이는?
HTTP는 서버와 클라이언트 사이의 데이터를 전달하기 위한 프로토콜입니다. Hyper Text Transfer Protocol 이라는 말에 걸맞게 HTML과 같은 텍스트 이상의 데이터를 전달하는 역할을 수행하는 것이 주로 특징입니다. 사용자의 눈에 이따금 보이거나 보이지 않게 데이터를 서버와 주고 받지만, 모두 평문으로 숨기지 않고 전달하기 때문에 일반적인 범주를 벗어나는 사용자의 경우 데이터를 개인 정보와 같은 중요한 내용을 네트워크 상에서 가로채거나, 통신 상대로 위장하거나 변조하는 등의 위험에 노출될 가능성이 높습니다.

이러한 HTTP의 취약점을 보완하기 위해 암호화와 인증, 완전성 보호를 더한 것이 HTTPS입니다. SSL 혹은 TLS라는 프로토콜로 HTTP에서 사용되는 TCP/IP를 대체하여 암호화와 증명서, 안정성 보호를 이용할 수 있게 됩니다. 이로써 클라이언트와 서버간의 데이터 통신이 일어날 때, 탈취/위장/변조의 위험에서 안전성을 보장받게 되는 것입니다. 현재는 이러한 HTTPS를 속도 저하라는 단점을 보완했기에 용도에 맞게 사용하는 것이 아닌 모든 웹페이지를 HTTPS로 적용하는 방향으로 바뀌고 있습니다.


## 3Way Handshake는 무엇입니까?
3way handshake는 데이터를 전달하는 프로토콜인 TCP에서 일어나는 데이터 연결과정을 의미합니다. TCP는 데이터의 발신자와 수신자를 논리적인 경로를 배정하여 연결하여 프로토콜의 신뢰성을 높이게 되는데 이 연결과정을 3way handshake, 연결을 해제하는 과정을 4way handshake라고 합니다. 

3way handshake는 클라이언트가 서버에게 접속 요청 패킷을 보내고 응답을 기다리는 상태, 열린 상태의 서버가 요청을 받고 클라이언트에게 받은 패킷에 요청을 수락하고 받을 준비가 된 상태를 보내는 단계, 클라이언트가 서버로부터의 승인을 확인하고 연결하여 데이터를 보내는 단계로 이루어집니다. 이를 통해서 데이터를 무작정 보내는 것이 아닌 데이터를 받을 준비가 되어 있는 상태를 3단계를 통해 확인하여 보다 신뢰성있는 연결을 맺어주게 되는 방식을 3 way handshake라고 합니다.
