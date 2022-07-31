/*
프로그래머스 고득점kit - hash level2

https://school.programmers.co.kr/learn/courses/30/lessons/42578

clothes	return
[["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]	5
[["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]	3

*/

import java.util.*;

class Solution {
    public int solution(String[][] clothes) {
        int answer = 1;
        Map<String,Integer> cMap = new HashMap();
        
        for(String[] c : clothes){
            cMap.put(c[1],cMap.getOrDefault(c[1],0) + 1);
        }
                
        for(String key : cMap.keySet()){
            answer *= cMap.get(key) + 1;
        }
        
        return answer-1;
    }
}
