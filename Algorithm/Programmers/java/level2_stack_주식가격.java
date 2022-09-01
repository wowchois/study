/*
프로그래머스 level2 stack?

prices	return
[1, 2, 3, 2, 3]	[4, 3, 1, 1, 0]

https://school.programmers.co.kr/learn/courses/30/lessons/42584
*/

import java.util.*;

class Solution {
    public int[] solution(int[] prices) {
        int[] answer = new int[prices.length];
        Arrays.fill(answer, 0);
        
        for(int i=0; i < prices.length; i++){
            for(int j=i+1; j < prices.length; j++){
                answer[i] += 1;
                if(prices[i] > prices[j]) break;
            }
        }
        
        return answer;
    }
}
