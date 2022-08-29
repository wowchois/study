/*
프로그래머스 level2 queue

priorities	location	return
[2, 1, 3, 2]	2	1
[1, 1, 9, 1, 1, 1]	0	5

https://school.programmers.co.kr/learn/courses/30/lessons/42587
*/

//1. queue로 푼 경우 
import java.util.*;

class Solution {
    public int solution(int[] priorities, int location) {
        int answer = 0;
        int endIdx = 0;
        Queue<Pair> que = new LinkedList();
        
        for(int i=0; i < priorities.length; i++){
            que.offer(new Pair(i, priorities[i]));
        }
        
        while(!que.isEmpty()){
            Pair nowPair = que.poll();
            Boolean minFlag = isMin(que, nowPair);
            
            if(minFlag){ //뒤에 큰 수가 있는 경우
                que.offer(nowPair);
                continue;
            }
            endIdx++;
            if(nowPair.idx == location) return endIdx;
        }
        
        return answer;
    }
    
    private Boolean isMin(Queue<Pair> que, Pair nowPair){
        Boolean flag = false;
        for(Pair p : que){
            if(nowPair.val < p.val) flag = true;
        }
        return flag;
    }
    
    class Pair{
        int idx;
        int val;
        
        public Pair(int idx, int val){
            this.idx = idx;
            this.val = val;
        }
    }
}



//2. PriorityQueue로 푼 경우 (우선순위 큐)




