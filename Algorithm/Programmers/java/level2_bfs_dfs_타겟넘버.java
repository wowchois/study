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
                tmp.add(li + n);
                tmp.add(li - n);
            }
            nlist = tmp;
        }
        
        for(int li : nlist){
            if(li == target) answer++;
        }
        
        
        return answer;
    }
}

