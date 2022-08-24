/*
프로그래머스 level1 stack

arr	answer
[1,1,3,3,0,1,1]	[1,3,0,1]
[4,4,4,3,3]	[4,3]

https://school.programmers.co.kr/learn/courses/30/lessons/12906
*/

import java.util.*;

public class Solution {
    public int[] solution(int[] arr) {
        Stack<Integer> stack = new Stack();
        
        for(int i : arr){
            if(!stack.empty() && stack.peek() == i) continue;
            stack.push(i);
        }

        return stack.stream().mapToInt(i->i).toArray();
    }
}
