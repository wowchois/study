# JAVA 알고리즘

### 문자열 배열에 문자열 포함 여부 체크

```java
String[] test = {"test1","test2"};
String msg = "test2";

Arrays.ofList(test).contains(msg); // Boolean return

```

### 형 변환

- String[] <-> List<String>
  
  ```java
  import java.util.Arrays;
  import java.util.List;
  import java.util.ArrayList;
  
  String[] answer = {};
  List<String> result = new ArrayList<>();
  result.add("1");
  
  answer = result.toArray(answer); // list -> array
  //answer => ["1"]
  
  String[] testArray = {"1","2"};
  List<String> test = new ArrayList<>(Arrays.asList(testArray)); //array -> list
  test.add("3");
  
  // test => ["1","2","3"]
  ```
- List -> String[]
  ```java
  result.stream().mapToInt(i -> i).toArray();
  ```
  
- int[] -> string[]
```java
int[] numbers = {3,2,45};
String[] strArray = Arrays.stream(numbers).mapToObj(String::valueOf).toArray(String[]::new);

System.out.println(Arrays.toString(strArray));
```
  

- 문자열

```java
String msg = "test";

msg.charAt(i); //i번째 문자열 리턴

```
  
  
### 정렬
```java
Arrays.sort();
```

- Collections sort
```java
List<Integer> vList = new ArrayList(values.keySet());
Collections.sort(vList, (o1,o2) -> values.get(o2) - values.get(o1));
```

- Comparator
: 내림차순 정렬에 많이 사용.  
```java
import java.util.Comparator
```


### HashMap

```java

Map<String,Integer> test = new HashMap();

// 값 있으면 가져오고 없으면 기본값 세팅 
test.put("key", test.getOrDefault("key", 0));
```

```java
Map<String,Integer> test = new HashMap();

// map으로 stream 처리
String value = test.entrySet()
                    .stream()
                    .filter(info -> info.getValue() > 0)
                    .map(Map.Entry::getKey)
                    .findFirst().get();

// List로 가져오는 경우
import java.util.stream.Collectors;

List valueList = test.entrySet()
                    .stream()
                    .filter(info -> info.getValue() > 0)
                    .map(Map.Entry::getKey)
                    .collect(Collectors.toList()); // return : []

```
```java

//map에 key가 포함되어있는지 확인
map.containsKey("keyName"); //return : true, false

```


### heap
```java

```
