
## python 풀이 시 고려할 사항
- 문자열을 [n:m]로 자르는 경우, 문자열 길이 이상 잘라도 출력은 ''이다.  
- dictionary 사용   
  dict.get('key',값이없을때 리턴값) : key값으로 찾는데, 값이 없는 경우 뒤의값으로 return한다.   
  dict.pop('key',값이없을때 리턴값) : .get과 비슷한데, pop을 하면서 리턴한다.   
  'key' in dict : True/False 리턴으로 key 여부 확인   
  .keys() / .values()   
- list(문자열) : 한글자씩 리스트로 리턴된다.
- list 길이가 같은 배열 2개 경우 zip() 으로 묶어서 사용
- for else 문 사용하기
- math.ceil() 올림 사용하기
- 정렬 .sort()는 O(nlogn) 이다. (필요할때는 사용하는게 좋다)
- 우선순위가 높은 것부터 처리해야 하는 경우 heap문제가 많음.
- list 의 pop(0) 보다 deque 의 popleft()가 더 빠르다. (pop(0) 시간복잡도 O(n))
- O(logn)과 O(nlogn) 과 엄청난 속도차이가 있다. (n배가 됨)
- python 알파벳은 크기 비교가 가능!!!!! ('x' > 'y' => False 리턴)
- python에서 dictionary로 list로 직접 접근할때 dict key에 list item값이 없는 경우 KeyError 발생하므로, try~except: 처리 필요!  
- zip(*arr) : 2중배열이라면 가로 배열이 세로 배열로 전환된다.
- copy 
-        2차원 경우 target = [item[:] for item in arr] 이렇게 복사하면 메모리 낭비 없이 빠르게 가능.
-        1차원 경우 target = item[:]


### * unpacking
: (),{},[] 괄호를 한번 걷어내는 작업  
ex) zip(*[[1,0.0],[0.0.1],[0,1,0]]) -> *으로 [1,0.0],[0.0.1],[0,1,0]만 남은 상태에서 zip을 하면 tuple로 첫번째요소끼리 묶이고, 두번쨰 요소끼리 묶임  
-> (1,0,0),(0,0,1),(0,1,0) 으로 변환된다.   
2차원 배열 회전 경우  
```
arr = [[0,0,0],[1,0,0],[0,1,1]]   
rotate = [list(reverse(i)) for i in zip(*arr)]
변환 전
[0,0,0],  
[1,0,0],  
[0,1,1]  
변환 후 (시계방향으로 90도 회전) 
[0,1,0],  
[1,0,0],  
[1,0,0]    
```


### stack
: First In Last Out 으로 먼저들어와서 마지막에 나가는 방법  
python 에서는 list()로 풀이하며, pop/append 로 in/out 한다. (접근은 index)  
- 보통 stack문제는 stack 새로운 list 생성하고, 대상 list에서 stack없는 경우 넣고, 들어간 데이터와 비교하면서 같으면 pop 다르면 append 하는 방법   

```

stack = []
stack.append(1)
stack.pop()

stack[0] 
stack[-1]
```


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
t_que.pop() # pop right
t_que.popleft() # pop left

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

(priorityque 보다 heapq가 더 빠르다)

```
import heapq

arr = []
heapq.heapify(arr)
heapq.heappush(arr,10) # 10을 arr에 추가  
heapq.heappop(arr) # arr의 가장 작은 원소 리턴하고 삭제 / 없을 경우 index error (삭제 안할경우 index접근)
heapq.heapreplace(arr,target,target2) pop -> push 순서로 replace된다.
heapq.pushpop(arr,target) #target 을 push -> pop 순서로 진행한다.

#heapify 한 후 arr은 heap이 되어서 작은 숫자부터 자동정렬된다.
arr[0] # => 제일 작은값 출력됨.
arr[0] = 1 => 값 치환만 되고 heap자체에서 정렬은 안해준다!! (pop,push 해야 정렬함!)


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
: 2차원 지도 주어진 경우 DFS/BFS로 풀이 / 그래프 간선 가중치가 같을 때 적합하다. (다른 경우 다익스트라 알고리즘)
#### DFS(Depth First Search)  
: 경로저장/경로의 특징 경우, 검색대상이 큰 경우
#### BFS(Breadth First Search)  
: 최단거리 경우 (현재 노드로부터 가까운것 찾기 등), 규모가 안크고 검색대상이 멀지 않은 경우
- 모든지점 방문은 DFS/BFS 상관없음

풀이방식
- DFS : stack / 재귀함수
- BFS : queue


#### 다익스트라 알고리즘
: 최단 경로 알고리즘   
우선순위 큐로 풀어내며, V(정점의 수), E(간선의 수) -> O(E log V) 시간복잡도를 가진다.   
ex) 문제 - 배달문제  


### 소수 찾기 - 에라토스테네스 
: 소수 여부 판단하는 알고리즘 중 하나

1. N까지의 수를 나열한다.
2. 제일 작은 수 i를 찾는다.
3. i의 배수 수는 모두 지운다. (해당 i는 삭제하지 않는다.)
4. 다음으로 제일 작은 수 j를 찾는다.
5. 3,4번 반복

ex) 2,3,4,5,6,7,8,9  
- 2의 배수 : 4,6,8 삭제
- 3의 배수 : 3,9 삭제
- 5의 배수 : 없음
- 남은 수 : 2,3,5,7  


### 완전탐색
파이썬 라이브러리  

#### combinations
: 모든 경우의 수를 짝지어서 반환  
순서는 고려되지 않고, (1,2)와 (2,1)은 같은것으로 판단해서 (1,2)만 출력된다.   
```
from itertools import combinations

arr = [1,4,2,5,7,8,9,10]
comb = list(combinations(arr,3)) # 3개씩 모든 경우의 수를 tuple로 묶어준다.

# result : 
	[(1, 4, 2), (1, 4, 5), (1, 4, 7), (1, 4, 8), (1, 4, 9), ... (7, 9, 10), (8, 9, 10)]
```

#### permutations
: 모든 경우의 수를 짝지어서 반환  
순서가 고려되며, (1,2)와 (2,1)은 다르게 판단되어 모두 출력.
```
from itertools import permutations

arr = [1,4,2,5,7,8,9,10]
comb = list(permutations(arr,3)) # 3개씩 모든 경우의 수를 tuple로 묶어준다.

# result :
	[(1, 4, 2), (1, 4, 5), (1, 4, 7), (1, 4, 8), (1, 4, 9), (1, 4, 10), (1, 2, 4), (1, 2, 5) ... ]
```

#### product
: 두개 이상의 리스트에서 모든 경우의 수를 짝지어서 반환

```
arr = [[1,2],[1,2,3],[1,2,3]]
list(product(*arr))

결과 : 	
[(1, 1, 1), (1, 1, 2), (1, 1, 3), (1, 2, 1), (1, 2, 2), (1, 2, 3)
, (1, 3, 1), (1, 3, 2), (1, 3, 3), (2, 1, 1), (2, 1, 2), (2, 1, 3)
, (2, 2, 1), (2, 2, 2), (2, 2, 3), (2, 3, 1), (2, 3, 2), (2, 3, 3)]

```


### 백트래킹
: 모든 경우의 수를 탐색하는 알고리즘   
- DFS/BFS 를 이용할 수 있다.
- 효율성을 위해 탐색이 필요없는 부분은 가지치기로 미리 제거한다. -> 가지치기로 백트래킹의 효율성이 결정될 수 있다. !!(중요)
- 탐색에 순환이 있으면 BFS이용하는게 편하다.
- DFS 경우 재귀보다 stack으로 풀기. (파이썬은 재귀 선호하지 않음.)

1. 모든 경우의 수 찾도록 코딩
2. 특정 조건 만족하는 부분만 탐색하고 나머지는 탐색하지 않게 코딩
3. 절대 답이 될 수 없을 때 탐색 종료


### 그리디 - 탐욕 알고리즘
: 매 선택에 최적의 답을 선택하는 알고리즘  
최적의 해를 구하는 알고리즘보다 빠르며, 최적의 해를 구하지는 않음.  
크루스칼/다익스트라 알고리즘에 사용된다.  
ex) 거스름돈 문제 경우, 1860원 -> 돈 큰단위부터 거스름돈을 만든다.  
1000원 1개   
500원 1개  
100원 3개  
50원 1개  
10원 1개  


### 그래프
: 정점과 정점을 연결하는 간선으로 이뤄진 비선형 자료구조  
- 정점은 여러개의 간선을 가지며, 양방향으로 이뤄진다.  
- 각 간선은 가중치를 가질 수 있다.  
- 사이클이 있을 수 있다. 

무방향 그래프 : 간선에 방향이 없어서 양방향으로 취급한다. (A->B),(B->A) 두 방향 고려해야함.  
방향 그래프 : 간선에 방향이 있어서 일방통행이다.  (A->B) 와 (B->A)는 다름  
연결 그래프 : 각 정덤이 서로 모두 이동 가능한 상태이다.  
비연결 그래프 : 특정 정점에는 간선이 존재하지 않는 그래프.  
완전 그래프 : 모든 정점이 모두 연결되어 있는 그래프.  
사이클 그래프 : 특정 정점에서 간선으로 순환이 되고 있는 그래프.  



### 최소신장트리 (크루스칼/프림)
: 그래프 내의 모든 정점을 포함하는 최소 연결 그래프이다.
- 최소한의 간선으로 모든 정점이 연결되어야 한다.
- 모든 가중치들이 최소한이 되어야 한다.
- cycle 발생되면 안된다.





