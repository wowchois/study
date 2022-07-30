

import java.util.*;

class Solution {
    public String solution(String[] participant, String[] completion) {
        Map<String,Integer> partiMap = new HashMap<>();
        
        for(String s : participant){
            partiMap.put(s,partiMap.getOrDefault(s,0) + 1);
        }
        for(String c : completion){
            partiMap.put(c,partiMap.getOrDefault(c,0) - 1);
        }
        /*
        String answer = "";
        for(String k : partiMap.keySet()){
            if(partiMap.get(k) > 0){
                answer = k;
                break;
            }
        }
        */
        String answer = partiMap.entrySet()
            .stream()
            .filter(info -> info.getValue() > 0)
            .map(Map.Entry::getKey)
            .findFirst().get();
        
        return answer;
    }
}
