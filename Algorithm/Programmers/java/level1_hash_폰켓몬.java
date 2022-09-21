/*
프로그래머스 

nums	result
[3,1,2,3]	2
[3,3,3,2,2,4]	3
[3,3,3,2,2,2]	2

https://school.programmers.co.kr/learn/courses/30/lessons/1845
*/

import java.util.*;

class Solution {
    public int solution(int[] nums) {
        int halfN = nums.length / 2;
        Map<Integer,Integer> setN = new HashMap();
        
        for(int n : nums){
            setN.put(n, setN.getOrDefault(n,0)+1);    
        }
        
        return halfN < setN.size() ? halfN : setN.size();
    }
}
