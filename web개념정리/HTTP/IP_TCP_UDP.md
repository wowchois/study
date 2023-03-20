## IP프로토콜
- 비연결성 : 패킷을 받을 대상이 없거나, 서비스가 안되고 있어도 패킷이 전송됨.   
- 비신뢰성 : 패킷의 손실이나 순서오류가 있어도 복구가 안됨.     
- 프로그램 구분 : 같은 ip경우 서비스 구별이 안됨.    

## TCP
: 전송제어 프로토콜   

전송하려는 패킷 +=> TCP정보 +=> IP정보 씌워서 전송 +=> 이더넷프레임(mac정보)  ==> 전송
  
IP패킷 : 출발/목적지 IP정보
TCP정보 : 출발/목적지 PORT 정보, 순서/검증 정보


* 특징   
> 연결지향 3way Handshake   
> 데이터 전달/순서 보증   
>   현재 대부분 TCP사용   


### 3way Handshake

client ------- server
1. SYN (접속요청)           client -> server
2. SYN + ACK (접속요청+수락) server -> client
3. ACK (수락 + 데이터 같이 전송)               client -> server

