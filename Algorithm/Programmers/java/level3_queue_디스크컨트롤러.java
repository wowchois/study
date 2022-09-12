/*
프로그래머스 level3 queue

jobs	return
[[0, 3], [1, 9], [2, 6]]	9

https://school.programmers.co.kr/learn/courses/30/lessons/42627
*/

import java.util.*;
class Solution {
    public int solution(int[][] jobs) {
        int endTime = 0;
        int sum = 0;
        int idx = 0;
        int time = 0;
        Arrays.sort(jobs, (o1,o2)->o1[0]-o2[0]); //시간순 정렬
        
        PriorityQueue<int[]> pque = new PriorityQueue<>((o1,o2)->o1[1]-o2[1]);
        
        while(time < jobs.length){
            while(idx < jobs.length && jobs[idx][0] <= endTime){
                pque.offer(jobs[idx++]);
            }
            
            if(pque.isEmpty()) endTime = jobs[idx][0];
            else{
                int[] now = pque.poll();
                endTime += now[1];
                sum += endTime - now[0];
                time++;
            }
        }
        /*
             end[1] sum+=end-[0]
        0 3 : 3     3-0=3
        2 6 : 3+6   9-2=7    
        1 9 : 3+6+9 18-1=17 
        */
        
        return sum / jobs.length;
    }
}
