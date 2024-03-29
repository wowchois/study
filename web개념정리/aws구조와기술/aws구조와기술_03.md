# AWS구조와 기술 책 정리 - 03
aws를 사용하기 위한 도구

### aws관리기능
- 관리콘솔 : 서비스 설정화면. 
- CLI : 명령어 조작 관리 콘솔.
- IAM : 서비스 사용을 위한 사용자 계정. (그룹이나 정책을 일괄 관리)
- 비용관리 : 그래프로 비용 확인해서 예산 관리.
- CloudWatch : 감시도구. 임계값 넘는 경우 조치.


### AWS IAM
Identity and Access Management ID와 접속관리의 약어로, aws의 인증 기능이다.  
IAM은 각 서비스에 대한 접속을 관리한다.  
IAM은 별도의 추가 요금없이 AWS계정에서 제공된다.  
- IAM사용자 : 각 유저에게 부여하는 IAM
- IAM역할 : 서비스나 프로그램에 부여하는 IAM

IAM사용자/역할 모두 최소한 기능을 부여하고 필요한 상황에만 전달해 운영해야 한다.  

AWS는 여러개의 EC2 인스턴스나 S3버킷이 존재하기 때문에, 각 서비스에 대해 권한 설정이 힘들다.  
-> 사용자는 IAM그룹으로 관리 (그룹으로 같은 권한 부여함)  

#### IAM정책
: 실행자(사용자,그룹,역할)이 어떤 서비스에 접속할 수 있는지 정책 설정.  
사용자마다 권한부여가 아닌, 정책을 생성해 그 정책안에서 사용자가 행동할 수 있게 적용하는 형태이다.  
-> 권한이 변경되면, 정책에 속한 모든 사용자의 역할이나 권한이 변경되어 관리하기 편하다.  
정책 1개를 여러 사용자, 사용자 1명에게 여러 권한을 줄 수 있다.  

- 자격기반 정책 : 사용자/역할/그룹이 어떤일을 할 수 있는지의 형태로 설정.  
- 리소스 기반 정책 : 서버/폴더에서 어떤것을 허가할지의 형태로 설정.


### AWS CloudWatch
: aws 서비스의 리소스를 모니터링과 관리를 담당.  
각 서비스에서 수치/로그 등을 수집해 기록하고, 로그가 임계값을 넘으면 설정한 동작(EC2 시작/정지, Auto Scaling, Lambda)을 실행하게 한다.  
CPU사용률, 볼륨 읽기/쓰기 횟수, 바이트 수, 네트워크 송수신 패킷 수 등을 감시할 수 있다.  


