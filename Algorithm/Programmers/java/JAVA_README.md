# JAVA 알고리즘

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
  
