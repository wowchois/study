/*
프로그래머스 level2 greedy

name	return
"JEROEN"	56
"JAN"	23
"AAA" 0
"BBBAAAAAAAB" 8

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
                //System.out.println(next);
                next++;
            }
            minMove = Math.min(minMove, i+i+(len - next)); //왼쪽에서 가다가 A만나면 다시 뒤로간 경우 (i+i 가 뒤로 다시돌아간 수)
            minMove = Math.min(minMove, ((len - next) * 2) + i); //뒤에서부터 움직일 경우 
            //i = 처음(왼쪽)부터 오른쪽 A만나기 직전까지 이동한 수
            //next = 연속적으로 A가 있는 수
            //len - next = 연속된 A가 끝나고 이후에 몇개의 문자가 남았는지의 수
            // BBBAAAAAAAB 경우 i = 2, next = 10 
            //len - next = 11 - 10 = 1 => 마지막 B하나 남아있음. (뒤에서부터 시작하면 더 작게 움직일 수 있음)
            
            //System.out.println("minMove : "+ i +"/"+ next  +"/ " + minMove);
        }
        answer += minMove;
        
        return answer;
    }
}
