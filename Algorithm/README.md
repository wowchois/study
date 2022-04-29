### deque
- deque   
: 양방향 queue (앞/뒤 방향에서 요소 출력가능) O(1)    
: stack / queue 처럼 사용할 수 있다.    
(push/pop이 list보다 우수한 속도이다)

```
from collections import deque

t_que = deque(Arr/string)
t_que.append(item) #add right
t_que.appendleft(item) # add left
t_que.pop(item) # pop right
t_que.popleft(item) # pop left

t_que.extend(arr) # arr right 붙이기
t_que.extendleft(arr) # arr left 붙이기

t_que.remove(item) # 찾아서 삭제
t_que.rotate(n) # n만큼 회전 (+ 오른쪽, - 왼쪽)
```

### PriorityQueue
- PriorityQueue    
: 우선순위 queue로 선입선출 구조이다. (First In First Out)   
데이터를 추가한 대로 삭제된다.  
queue의 default size는 무한대이므로, maxsize를 정해줘야 한다.  

```
que = PriorityQueue(maxsize=8)
que.put(1) # add
que.put(2)

que.get() # remove
```



### heapq
- heapq   
: 2진트리 기반 최소heap 자료구조, O(log2N)   
데이터가 채워질때는 왼쪽 아래부터, 오른쪽으로 채워진다. (depth 달리지면 왼쪽 가장 아래부터)  
최대값/최솟값을 빠르게 찾는다. (ex : 10,20,30 -> [10,30,20])
최대힙 : 부모-자식 노드에서 부모가 제일 큰 값 부터 내려감     
최소힙 : 부모-자식 노드에서 부모가 제일 작은 값 부터 내려감    

```
import heapq

arr = []
heapq.heappush(arr,10) # 10을 arr에 추가  
heapq.heappop(arr) # arr의 가장 작은 원소 리턴하고 삭제 / 없을 경우 index error (삭제 안할경우 index접근)

n_arr = [10,30,20]
heapq.heapify(n_arr) # list를 heapq로 변환


[14, 10, 6, 8, 12, 4] 순으로 입력 시,
1. 14
2. 10 - 14 (왼)
3. 6 - 14(왼) 
   6 - 10(오)
4. 6 - 8 - 14(왼) 
   6 - 10(오)
5. 6 - 8(왼) - 14(왼) - 12(왼오) 
   6 - 10(오)
5. 4 - 8(왼) - 14(왼) - 12(왼오) 
   4 - 6(오) - 10(오왼)
   
```



### DFS / BFS
- DFS(Depth First Search)  
: 경로저장/경로의 특징 경우, 검색대상이 큰 경우
- BFS(Breadth First Search)  
: 최단거리 경우 (현재 노드로부터 가까운것 찾기 등), 규모가 안크고 검색대상이 멀지 않은 경우
- 모든지점 방문은 DFS/BFS 상관없음


풀이방식
- DFS : stack / 재귀함수
- BFS : queue



### python 풀이 시 고려할 사항
- 문자열을 [n:m]로 자르는 경우, 문자열 길이 이상 잘라도 출력은 ''이다.  
- dictionary 사용   
  dict.get('key',값이없을때 리턴값) : key값으로 찾는데, 값이 없는 경우 뒤의값으로 return한다.   
  dict.pop('key',값이없을때 리턴값) : .get과 비슷한데, pop을 하면서 리턴한다.   
  'key' in dict : True/False 리턴으로 key 여부 확인   
  .keys() / .values()   
- list(문자열) : 한글자씩 리스트로 리턴된다.
- list 길이가 같은 배열 2개 경우 zip() 으로 묶어서 사용
- for else 문 사용하기

