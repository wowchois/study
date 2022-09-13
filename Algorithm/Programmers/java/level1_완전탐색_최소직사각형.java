/*
프로그래머스 level1 완전탐색 

명함 번호	가로 길이	세로 길이
1	60	50
2	30	70
3	60	30
4	80	40

https://school.programmers.co.kr/learn/courses/30/lessons/86491
*/

import java.util.*;

class Solution {
    public int solution(int[][] sizes) {
        int maxW = 0;
        int maxH = 0;
        
        for(int[] size : sizes){
            int cMax = Math.max(size[0],size[1]);
            int cMin = Math.min(size[0],size[1]);
            maxW = Math.max(maxW,cMax);
            maxH = Math.max(maxH,cMin);
        }
        
        return maxW * maxH;
    }
}


class Solution {
    public int solution(int[][] sizes) {
        
        return Arrays.stream(sizes).reduce((o1,o2) -> new int[]{
            Math.max(Math.max(o1[0],o1[1]),Math.max(o2[0],o2[1])), Math.max(Math.min(o1[0],o1[1]),Math.min(o2[0],o2[1]))
        }).map(i -> i[0]*i[1])
            .get();
    }
}
