#11866번 요세푸스 문제
#121808KB 176ms

N,K = map(int,input().split())
arr = list(range(N,0,-1))
result = []

idx = 0
while len(arr) > 0 :
  if idx == K-1 : 
    idx = 0
    result.append(arr[-1])
    arr.pop()
  else :
    arr.insert(0,arr[-1])
    arr.pop()
    idx += 1

result = list(map(str,result))

print('<'+', '.join(result)+'>')