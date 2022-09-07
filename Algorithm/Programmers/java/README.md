# JAVA 알고리즘

- 크루스칼 알고리즘 [예제](level3_greedy_섬연결하기.java)
- [Stack](#stack)
- [Heap](#heap)
- [Queue](#queue)

## 고려할 사항
- 문자열 이어붙이는 경우 : StringBuilder 사용하기! (+로 이어붙이면, 메모리 할당되서 시간초과 발생)
- int숫자 나눗셈 경우, 그냥 나누면 결과가 int형으로 리턴되서 double처리가 필요하다! -> (double) 2 / 4 


### Math
- 올림 : Math.ceil()
- 반올림 : Math.round()
- 버림 : Math.floor()

### 문자 / 문자열

- contains : 문자열 배열에 문자열 포함 여부 체크
```java
String[] test = {"test1","test2"};
String msg = "test2";

Arrays.ofList(test).contains(msg); // Boolean return
```

- charAt : 문자열에 문자 하나 출력

- "123".charAt(0) - '0' : 문자를 숫자로 변경 -> return int형 숫자

### Array
- fill 배열 채우기
```java
int[] result = new int[5];
Arrays.fill(result, 1); //[1,1,1,1,1] 
```

### 형 변환

- String[] <-> List<String>

```java
String[] answer = {};
List<String> result = new ArrayList<>();
result.add("1");

answer = result.toArray(answer); // list -> array
//answer => ["1"]

String[] testArray = {"1","2"};
List<String> test = new ArrayList(Arrays.asList(testArray)); //array -> list
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
  
- Array sort [예시](./level2_sort_가장큰수.java)
```java
  String[] strArray = {"3", "30", "34", "5", "9"};
  
  //1. String 정렬
  Arrays.sort(strArray, (o1,o2) -> (o1+o2).compareTo(o2+o1)); //오름차순
  Arrays.sort(strArray, (o1,o2) -> (o1+o2).compareTo(o2+o1)); //내림차순
```
- int[]는 그냥 정렬.
```java
int[] intArray = {1,2,3};
Arrays.sort(intArray);
Arrays.sort(intArray, (o1,o2) -> o2-o1); //내림차순
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

- map으로 stream 처리
```java
Map<String,Integer> test = new HashMap();

String value = test.entrySet()
                    .stream()
                    .filter(info -> info.getValue() > 0)
                    .map(Map.Entry::getKey)
                    .findFirst().get();
                    //.collect(Collectors.toList()); // List casee, return : []
```

- map에 key가 포함되어있는지 확인
```java
map.containsKey("keyName"); //return : true, false
```


### stack
```java
Stack<Integer> stack = new Stack();

stack.push(1);
stack.pop(); //최상위값 출력+제거
stack.peek(); //최상위값 출력
stack.contains(1); //true/false
stack.size();
stack.empty(); //true/false
stack.clear();
```

### queue
```java
Queue<Integer> que = new LinkedList();

que.offer(1); //que.add();
que.peek(); //처음 값 참조
que.size();
que.poll(); //처음 값 빼서 출력.
que.isEmpty(); 
```

### PriorityQueue
  : 기본 오름차순이다.   
```java
PriorityQueue<Integer> pque = new PriorityQueue(); //오름차순
PriorityQueue<Integer> pque = new PriorityQueue(Collections.reverseOrder()); //내림차순
```



