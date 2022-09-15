/*
프로그래머스 level2 완전탐색, dfs 

numbers	return
"17"	3
"011"	2

https://school.programmers.co.kr/learn/courses/30/lessons/42839
*/


import java.util.*;

class Solution {
    HashSet<Integer> hashset = new HashSet();
    
    public int solution(String numbers) {
        int answer = 0;
        
        recursive("",numbers);

        return (int) hashset.stream().filter(n -> isTrue(n) == true).count();
    }
    
    public void recursive(String combN, String subN){ //조합 구하기 (재귀)
        //System.out.println(combN + " / " + subN);
        
        if(!"".equals(combN)) hashset.add(Integer.valueOf(combN));
        
        for(int i=0; i < subN.length(); i++){
            recursive(combN + subN.charAt(i), subN.substring(0,i) + subN.substring(i+1));
        }
    }
    
    public Boolean isTrue(int n){ //소수여부 판단
        if(n < 2) return false;
        
        for(int i=2; i <= Math.sqrt(n); i++){ //(int) Math.pow(n,0.5) + 1
            if(n % i == 0) return false;
        }
        return true;
    }
}
