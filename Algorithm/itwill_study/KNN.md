# KNN Algorithms
> K Nearest Neighbor 약자로, 가장 가까운 거리의 이웃으로 분류.   
> (머신러닝 지도학습의 분류에 해당되는 알고리즘이다.)   

K값에 따라서 분류를 하며 K값이 찾으려는 분류들 개수.   
새로운 데이터를 분류한다고 하면, K값에 해당하는 데이터들 중 가장 많이 분류된 데이터를 기준으로 분류된다.    

  
  
K값이 너무 작으면 세밀하게 분류해서 오버피팅  
(과대적합 - 신경망 학습이 과하게 이뤄져서 새로운 데이터에 대한 학습이 제대로 안이뤄진다.) 이 일어나며,   
K값이 너무 크면 대충 분류해서 언더피팅(과소적합 - 학습을 제대로 못하는 상황)이 일어난다.   



### 머신러닝 종류
- KNN - 유클리드 거리 계산
- 나이브 베이즈 - 확률
- 의사결정트리 - 엔트로피
- 회귀 - 회귀 방정식
- 서포트 벡터 머신 - SVM 공식
- 아프리오리 - 신뢰도,연관도 구하는 공식
- K-means - 유클리드 거리 계산


### KNN 분류 알고리즘 (유클리드 거리 계산)

```python

#case 1
from collections import Counter

def knn(x,y,label,f,k) :
    dist = [(((f[0]-x[i])**2) + ((f[1]-y[i])**2))**0.5 for i in range(len(x))]
    
    box = dict(zip(dist, label))
    box = sorted(box.items())
    
    rank_k = [j[1] for j in box[:k]]
    cnt = Counter(rank_k)
    
    return list(cnt.keys())[0]

```

```python
x = [8,2,7,7,3,1]
y = [5,3,10,3,8,1]
label=['과일','단백질','채소','과일','채소','단백질']
tomato =[6,4]

knn(x,y,label,tomato,k=3)

```
결과 : '과일' 분류



```python
#case 2
import numpy as np

def my_knn(x,y,label, new, k=3):       
    distances = [((tomato[0]-x[i])**2 + (tomato[1]-y[i])**2)**0.5 for i in range(len(label))]   
    distances_sorted_with_k = sorted(distances)[:k]
    label_near = [label[distances.index(i)] for i in distances_sorted_with_k]    
    label_set = list(set(label))
    label_count = [label_near.count(i) for i in label_set]
   
    return label_set[np.argmax(label_count)]

```



```python
x = [8,2,7,7,3,1]
y = [5,3,10,3,8,1]
label=['과일','단백질','채소','과일','채소','단백질']
tomato =[6,4]

my_knn(x,y,label,tomato,3)
```

결과 : '과일' 분류



