/*
프로그래머스 level2 greedy

name	return
"JEROEN"	56
"JAN"	23
"AAA" 0

https://school.programmers.co.kr/learn/courses/30/lessons/42860
*/

import java.util.*;

class Solution {
    public int solution(String name) {
        int answer = 0;
        int next = 0;
        int len = name.length();
        int minMove = len - 1;
        
        for(int i=0; i < name.length(); i++){
            answer += Math.min(name.charAt(i)-'A', 'Z'-name.charAt(i) + 1); //위/아래
            
            next = i+1;
            while(next < len && name.charAt(next) == 'A'){ //연속된 A체크
                next++;
                //System.out.println(next);
            }
            minMove = Math.min(minMove, i+i+(len - next));
            minMove = Math.min(minMove, ((len - next) * 2) + i);
            //System.out.println("minMove : " + minMove);
        }
        answer += minMove;
        
        return answer;
    }
}
