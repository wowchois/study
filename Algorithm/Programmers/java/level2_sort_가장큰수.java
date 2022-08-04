/*
프로그래머스 level2 - sort

numbers	return
[6, 10, 2]	"6210"
[3, 30, 34, 5, 9]	"9534330"

https://school.programmers.co.kr/learn/courses/30/lessons/42746

*/

import java.util.*;

class Solution {
    public String solution(int[] numbers) {
        String answer = "";
        String[] strArray = Arrays.stream(numbers)
            .mapToObj(String::valueOf)
            .toArray(String[]::new);
        Arrays.sort(strArray, (o1,o2) -> (o2+o1).compareTo(o1+o2)); //내림차순
        
        if("0".equals(strArray[0])) return "0"; //전체 0인 경우
        
        for(String s : strArray){
            answer += s;
        }

        return answer;
    }
}
