/*
프로그래머스 level3 heap-PriorityQueue

operations	return
["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]	[0,0]
["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]	[333, -45]

https://school.programmers.co.kr/learn/courses/30/lessons/42628
*/

import java.util.*;

class Solution {
    public int[] solution(String[] operations) {
        int[] answer = {0,0};
        PriorityQueue<Integer> pque = new PriorityQueue();
        PriorityQueue<Integer> pqueMax = new PriorityQueue(Collections.reverseOrder());
        
        for(String op : operations){
            String[] arr = op.split(" ");
            if("I".equals(arr[0])){
                pque.offer(Integer.parseInt(arr[1]));
                pqueMax.offer(Integer.parseInt(arr[1]));
            }else{
                if(pque.isEmpty()) continue;
                if("D 1".equals(op)){
                    int n = pqueMax.poll();
                    pque.remove(n);
                }else if("D -1".equals(op)){
                    int n = pque.poll();
                    pqueMax.remove(n);
                }
            }
        }
        
        if(pque.isEmpty()) return answer;
        answer[0] = pqueMax.peek();
        answer[1] = pque.peek();

        return answer;
    }

}
