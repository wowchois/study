## Get
리소스 조회    
서버에 전달할 파라미터를 query String으로 전달   
캐싱이 가능하기 떄문에 조회 데이터는 GET을 권장     

> GET /info/100?param=test1

## Post
요청 데이터 처리 (등록)     
- body를 통해 파라미터 전달해서 데이터 처리를 요청      
(신규 데이터 등록, 변경 프로세스 처리 - 프로세스 진행 할 때도 모두 post)   
- 조회용도지만 json body데이터로 파라미터 받을 때도 사용(Post는 캐싱이 안됨)     

컨트롤URI : 행동에 대한 URI (주문 후 배달시작)    

> POST /change

## Put
리소스를 완전히 대체(덮어씌움, 삭제 후 다시생성), 없으면 생성   
client에서 변경할 데이터를 uri에 지정할 수 있다.

> PUT /change/100    
> param : {"name" : "test", "age" : 3}   

> 변경 param :  {"age" : 3}    
> 결과 : {"age" : 3} 만 조회됨 -> name컬럼 사라짐. (리소스 전체 대체)      

## Patch
리소스 부분 변경   

> PATCH /change/100    
> param : {"age" : 3}   

> 변경 param :  {"age" : 5}    
> 결과 : {"name" : "test", "age" : 5} 리소스 일부 변경         


## Delete
리소스 삭제    

> DELETE /change/100    
> 결과 : 삭제     


## Head
Get과 동일하지만 상태와 헤더만 반환  

## Options
주로 cors 에서 사용.




