## JPA

### ORM (Object Relational Mapping)
> 객체 관계 매핑.
> 객체 - 저장소 연결이 ORM(=JPA 인터페이스)이다.   
객체와 DB는 다르다. (객체는 매핑작업이 필요, DB는 객체처럼 사용 못함.)   


### JPA
: JPA저장소(영속성 컨텍스트)에서 데이터 있으면 DB까지 안가고 가져온다.  
데이터가 없으면 DB에서 select 해오고 저장소에 캐싱을 해 놓는다.  
hibernate는 JPA인터페이스 중 하나이며, JPA는 인터페이스를 모은것이다.    


- select시 같은 트랜잭션 애 엔티티 동일성 보장
: 같은 트랜잭션 내에서만 저장소가 유지된다. (서버 여러개 띄웠는데, 서버단위로 저장소가 유지되면 데이터가 깨진다.)  

- DB 격리수준 read commit이어도 repeatable read로 데이터 보장된다. (캐싱작업 떄문에 보장되지만, 캐싱을 일부러 날리는 경우가 있어서 무조건 보장은 아님.)   
 
> read committed : 가장 보편적인 격리수준.
>> 커밋되기 전엔 이전 데이터로 조회. (격리수준이 높아지면 비용이 많이든다.)   
>> 문제점 : 데이터가 변경됬는데, 트랜잭션이 길면 정합성이 깨진다.

> repeatable read : 트랜잭션 id별로 격리  
> phantom read : 특별한 경우 안씀.   


- 커밋 전까지 쿼리를 모아놓은다. (write지연 됨. 커넥션 한번에 연결 )

- update,delete 실행은 바로 커밋해서 row lock최소화한다.


### JPA 연관관계
- @OneToOne : 일대일
- @OneToMany : 일대다  
- @ManyToOne : 다대일
- @ManyToMany : 다대다
> @ManyToMany 경우 하나의 매핑 테이블을 만들어서   
> @OneToMany - @ManyToOne - @OneToMany 이런식으로 연결해서 만드는 것을 권장한다.   


#### fetch type (연관관계 타입)
- eager로딩 : 사용과 상관없이 한번에 전체 로딩 (원치않을때 n번 쿼리가 실행된다. -> 권장하지않는다.)    
- lazy로딩 : 사용할때까지 변수 할당하지 않고 사용할때 로딩 (권장)   

> 통계처리경우 jpa보다 jdbc template으로 사용하는게 성능이점이 있을 수 있다. (대부분 문제는 없지만, 복잡해지면 쿼리 튜닝이 필요할 수 있음.)


- @ManyToOne 말고 fk - id 사용하는 경우는 서비스가 나눠져있는 경우. (ex : MSA)
그 경우 해당 서비스에 연관되는 도메인이 하나 더 생성.    
(order, user 2개 서비스가 나눠지면, order-user, user 이렇게 됨.)   



