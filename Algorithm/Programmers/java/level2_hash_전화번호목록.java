/*
프로그래머스 고득점 kit - hash level2

phone_book	return
["119", "97674223", "1195524421"]	false
["123","456","789"]	true
["12","123","1235","567","88"]	false

https://school.programmers.co.kr/learn/courses/30/lessons/42577
*/

import java.util.*;

class Solution {
    public boolean solution(String[] phone_book) {
        boolean answer = true;
        Map<String,Integer> phoneMap = new HashMap();
        
        for(String p : phone_book){
            phoneMap.put(p, phoneMap.getOrDefault(p, 1));
        }
        for(String p : phone_book){
            String txt = "";
            for(int i=0; i < p.length(); i++){
                txt += p.charAt(i);
                if(phoneMap.containsKey(txt) && !p.equals(txt)){
                    return false;
                }
            }
        }
        
        return answer;
    }
}
