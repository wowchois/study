
/*
프로그래머스 level2 완전탐색 - 점화식

word	result
"AAAAE"	6
"AAAE"	10
"I"	1563
"EIO"	1189

https://school.programmers.co.kr/learn/courses/30/lessons/84512

1. A,AA,..., AAAE,..., AAAI, ..., AAE,...  
 규칙에서 5자리수가 바뀌는 간격은 +1, 4번째 자리가 바뀌는 간격은 +6, 3번째 간격은 31, ... => f(n) = f(n-1) + 5^n
2. 
*/

import java.util.*;

class Solution {
    public int solution(String word) {
        String str = "AEIOU";
        int answer = word.length();
        int[] term = {781, 156, 31, 6, 1}; //f(n) = f(n-1) + 5*i
        
        for(int i=0; i < word.length(); i++){
            answer += (term[i] * str.indexOf(word.charAt(i)));
        }

        return answer;
    }
}
