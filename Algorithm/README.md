
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


