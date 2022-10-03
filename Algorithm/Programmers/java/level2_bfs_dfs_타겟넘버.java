/*
프로그래머스 level2 bfs/dfs

numbers	target	return
[1, 1, 1, 1, 1]	3	5
[4, 1, 2, 1]	4	2

https://school.programmers.co.kr/learn/courses/30/lessons/43165

1. list에 더한숫자와 뺀 숫자를 모두 저장하면서 반복.

*/


//BFS 풀이

import java.util.*;

class Solution {
    public int solution(int[] numbers, int target) {
        int answer = 0;
        List<Integer> nlist = new ArrayList();
        nlist.add(0);
        
        for(int n : numbers){
            List<Integer> tmp = new ArrayList();
            for(int li : nlist){
                tmp.add(li + n); //더했을 경우
                tmp.add(li - n); //뺐을 경우
            }
            nlist = tmp;
        }
        
        for(int li : nlist){
            if(li == target) answer++;
        }
        
        
        return answer;
    }
}


// dfs 풀이

import java.util.*;

class Solution {
    int cnt = 0;
    public int solution(int[] numbers, int target) {
        loop(numbers,target,0,0);
        
        return this.cnt;
    }
    
    public void loop(int[] numbers, int target, int result, int depth){
        if(depth == numbers.length){
            if(result == target) this.cnt++;
            return;
        }
        loop(numbers, target, result+numbers[depth], depth+1); //더했을 경우
        loop(numbers, target, result-numbers[depth], depth+1); //뺐을 경우
    }
}


