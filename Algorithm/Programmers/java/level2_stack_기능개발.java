/*
프로그래머스 level2 stack/queue

progresses	speeds	return
[93, 30, 55]	[1, 30, 5]	[2, 1]
[95, 90, 99, 99, 80, 99]	[1, 1, 1, 1, 1, 1]	[1, 3, 2]

https://school.programmers.co.kr/learn/courses/30/lessons/42586
*/

import java.util.*;

class Solution {
    public int[] solution(int[] progresses, int[] speeds) {
        List<Integer> answer = new ArrayList();
        int time = 0;
        int max = 0;
        
        for(int i=0; i < progresses.length; i++){
            int work = (int) Math.ceil((100-progresses[i]) / (double) speeds[i]);
            if(max == 0) max = work;
            if(max < work){
                max = work;
                answer.add(time);
                time = 0;
            }
            time++;
        }
        answer.add(time);
        
        return answer.stream().mapToInt(i->i).toArray();
    }
}
