/*
프로그래머스 level2 stack

s	answer
"()()"	true
"(())()"	true
")()("	false
"(()("	false

https://school.programmers.co.kr/learn/courses/30/lessons/12909

s.substring(i,i+1) 사용 경우, 타임아웃 발생
*/



import java.util.*;

class Solution {
    boolean solution(String s) {
        Stack<Character> stack = new Stack();
        
        for(int i=0; i < s.length(); i++){
            if(!stack.empty() && '(' == stack.peek() && ')' == s.charAt(i)){
                stack.pop();
            }else{
                stack.push(s.charAt(i));
            }
        }

        return stack.empty();
    }
}
