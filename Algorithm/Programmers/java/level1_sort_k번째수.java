/*
프로그래머스 level1 - sort

array	commands	return
[1, 5, 2, 6, 3, 7, 4]	[[2, 5, 3], [4, 4, 1], [1, 7, 3]]	[5, 6, 3]

https://school.programmers.co.kr/learn/courses/30/lessons/42748
*/

import java.util.*;

class Solution {
    public int[] solution(int[] array, int[][] commands) {
        List<Integer> answer = new ArrayList();

        for(int[] sp : commands){
            List<Integer> numList = new ArrayList();
            
            for(int i=0; i < array.length; i++){
                if(i >= sp[0]-1 && i < sp[1]) numList.add(array[i]);
            }
            Collections.sort(numList, (o1,o2) -> o1 - o2);
            answer.add(numList.get(sp[2]-1));
        }
        
        return answer.stream().mapToInt(i -> i).toArray();
    }
}
