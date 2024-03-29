# AWS구조와 기술 책 정리 - 01

## AWS
: 클라우드 컴퓨팅 서비스.  
서버/네트워크 등 인터넷 서비스를 제공하며, 언제 어디서든 접속이 가능한 서비스.  

### 특징
- 시스템 일체를 사용 : OS,웹 서버, DB 등 소프트웨어를 통째로 사용할 수 있다.  
- 서비스 조합이 쉬움 : 서버만 사용하거나, 네트워크 연동 등 165개의 서비스를 제공해서 조합할 수 있다.
- 사용한 만큼 요금을 지불 : 사용한 서비스의 사용한 시간만큼 요금 지불
- 글로벌 보안 규정을 준수
- 글로벌 확장이 쉬움 : aws region이 국제적으로 존재해 가까운 지역의 서비스를 시작할 수 있다. 

웹 서버 구축 시, 조합되는 서비스
> 서버(EC2)  
> 서버OS(AMI)  
> IP주소(Elastic IP)  
> 스토리지(S3)  
> 도메인(Route 53)  
> DB서버(RDS)  

### AWS에서 제공하는 서비스
#### EC2 (Amazon Elastic Compute Cloud)
: 컴퓨터 용량을 제공하는 서비스 (서버 + OS + 소프트웨어)  
자유롭게 설치하고 시스템 구축할 수 있다. (이미 세팅된 서버 사용 가능)  
성능은 가변적이며, 일지정지 중에는 언제든 성능 조절 가능.  

#### S3 (Amazon Simple Storage Service)
: Object Storage Service이다.  
30웹 서버, 파일 서버용 파일들을 보관하는 저장소.  
스토리지는 장애에 강하고 다른 서비스와 연동하는 기능도 가지고 있다.  
파일 크기는 최대 5TB이며, 전체 용량 제한은 없다.  

#### VPN
: AWS계정 전용의 가상 네트워크이다.  
네트워크, 서브넷의 범위, 라우팅 테이블이나 게이트웨이 등을 설정하고 VM환경을 구성한다.  

#### RDS
: AWS의 관계형 데이터베이스이다.  
Aurora, PostgreSQL, MySQL, MariaDB, Oracle, SQL server 6종류의 DB를 클라우드에서 이용할 수 있는 서비스.  

#### Route 53
: DNS(Domain Name Server) 기능을 제공한다.  

#### Elastic IP
: 서버의 정적 공인 IP주소를 제공한다.  
EC2 + ELB(Elastic Load Balancing)와 조합해서 사용   

#### Amazon Managed Blockchain
: 블록체인 네트워크를 생성, 관리할 수 있다.  
데이터 위조/변조를 확인하는 기반으로 이용.  



