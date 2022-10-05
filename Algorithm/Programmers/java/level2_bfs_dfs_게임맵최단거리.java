/*
프로그래머스 level2 bfs 

maps	answer
[[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]	11
[[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]	-1

https://school.programmers.co.kr/learn/courses/30/lessons/1844

- dfs 경우 모든 경우를 찾아서 타임아웃 발생 가능성이 있다.
- 이 문제는 조건에 만족하면 종료해야 해서 bfs에 적합.
*/


import java.util.*;

class Solution {
    public int solution(int[][] maps) {
        int answer = 0;
        int[] moveX = {1,-1,0,0};
        int[] moveY = {0,0,1,-1};
        int[][] visit = new int[maps.length][maps[0].length];
        visit[0][0] = 1;

        Queue<int[]> que = new LinkedList();
        que.offer(new int[]{0,0});
        
        while(!que.isEmpty()){
            int[] now = que.poll();
            int x = now[1];
            int y = now[0];
            
            for(int i=0; i<4; i++){
                int mx = x + moveX[i];
                int my = y + moveY[i];
                if(mx < 0 || my < 0 
                   || mx >= maps[0].length || my >= maps.length) continue; //이동 못하는 경우
                if(visit[my][mx] == 0 && maps[my][mx] == 1){
                    visit[my][mx] = visit[y][x]+1; //이전이동값+1
                    que.offer(new int[]{my,mx});
                }
            }
        }
        
        answer = visit[maps.length-1][maps[0].length-1];
        
        return answer == 0 ? -1 : answer;
    }
}
