/*
문제유형 : Map

TEST CASE

INPUT : ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]	
RESULT : ["Prodo님이 들어왔습니다.", "Ryan님이 들어왔습니다.", "Prodo님이 나갔습니다.", "Prodo님이 들어왔습니다."]

https://programmers.co.kr/learn/courses/30/lessons/42888
*/

import java.util.*;

class Solution {
    public String[] solution(String[] record) {
        String[] answer = {};
        Map name = new HashMap<>();
        List<String> result = new ArrayList<>();

        for(String r : record){
            String[] sp = r.split(" ");
            
            if("Leave".equals(sp[0])) continue;
            else name.put(sp[1],sp[2]);
        }
        
        for(String r : record){
            String[] sp = r.split(" ");
            
            if("Change".equals(sp[0])) continue;
            if("Enter".equals(sp[0])){
                result.add(name.get(sp[1])+"님이 들어왔습니다.");
            }else if("Leave".equals(sp[0])){
                result.add(name.get(sp[1])+"님이 나갔습니다.");
            }
        }
        answer = result.toArray(answer);
        
        return answer;
    }
}
