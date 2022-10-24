## static과 singleton차이

### static
: static클래스를 말하며, 애플리케이션 시작할 때 한 번 정적 메모리로 바로 로딩된다.     
정적 메모리에 로딩되서 thread관리가 어렵다.   
static메서드에서 인스턴스는 사용이 불가능하다.   

```java
public class Test {
  private static String staticStr = "static!"; //static변수 
  
  String instanceStr = "instance!"; //instance변수
  
  public static String getTest() {
    String areaStr = "now area"; //지역변수 사용가능
    instanceStr = "test"; //ERROR : instance변수 사용 불가능 (class가 만들어질 때 생기는 인스턴스 변수이다.)
    
    return staticStr; //static변수 사용가능
  }

}
```


### 싱글톤
: 단 하나의 객체만을 가지는 패턴.   
하나의 인스턴스를 생성해 사용하고 공유하는 디자인 패턴. (인스턴스 필요 시, 생성이 아닌 공유의 방식)    
객체를 생성한다면 이미 생성된 객체를 반환하거나, 호출 시 생성한다.   
인터페이스 구현이 가능하고 확장이 가능하다.  
싱글톤에서 멀티톤(여러 객체 반환)은 불가능하다.   
ex : logger, util클래스  

- util클래스
```java
public class DateUtil {
  private static DateUtil instance; //객체를 생성 후 static변수에 저장. 
  
  private DateUtil() {
    //private생성자 : DateUtil을 다른 클래스에서 초기화 못하게 방지.
  }
  
  public static DateUtil getInstance() {
    if(instance == null) { //없으면 그때 생성
      instance = new DateUtil();
    }
    return instance; //생성된 객체 반환 (instance공유)
  }
}
```

- 사용
```java

DateUtil dateUtil1 = DateUtil.getInstance();
DateUtil dateUtil2 = DateUtil.getInstance();

System.out.println(dateUtil1 == dateUtil2);  //true (두 인스턴스는 같은 instance로 주소 공유한다.)

```


### 차이
- static은 정적 메모리에 로드되어 양이 많은 경우, 한 번에 로딩되고   
싱글톤은 lazy로딩이 가능하다.   

- static은 인터페이스 구현이 불가능하지만 싱글톤은 가능하다.  

- static은 stack메모리, 싱글톤은 heap메모리.  
- 
