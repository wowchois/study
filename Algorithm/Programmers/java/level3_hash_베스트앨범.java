/*
프로그래머스 hash level3

genres	plays	return
["classic", "pop", "classic", "classic", "pop"]	[500, 600, 150, 800, 2500]	[4, 1, 3, 0]

https://school.programmers.co.kr/learn/courses/30/lessons/42579
*/



import java.util.*;
import java.util.stream.Collectors;

class Solution {
    public int[] solution(String[] genres, int[] plays) {
        List<Integer> result = new ArrayList();
        Map<String,Integer> sumMap = new HashMap(); //합계
        Map<String,Map<Integer,Integer>> songMap = new HashMap(); //장르 - (index, number) Map
        
        for(int i=0; i < genres.length; i++){
            Map<Integer,Integer> idxMap = songMap.getOrDefault(genres[i], new HashMap());
            idxMap.put(i, plays[i]);
            songMap.put(genres[i], idxMap); //장르 Map
            sumMap.put(genres[i], sumMap.getOrDefault(genres[i], 0) + plays[i]); //합계
        }
        
        List<String> keyList = new ArrayList(sumMap.keySet());
        Collections.sort(keyList, (o1,o2) -> sumMap.get(o2) - sumMap.get(o1)); //합계 sort
        
        for(String key : keyList){
            Map<Integer,Integer> values = songMap.get(key);
            List<Integer> vList = new ArrayList(values.keySet());
            Collections.sort(vList, (o1,o2) -> values.get(o2) - values.get(o1)); //장르 Map sort
            
            result.add(vList.get(0));
            if(vList.size() > 1) result.add(vList.get(1));
        }
        
        return result.stream().mapToInt(i -> i).toArray();
    }
}
