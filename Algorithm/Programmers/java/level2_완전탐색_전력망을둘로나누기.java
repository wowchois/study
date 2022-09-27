/*
프로그래머스 level2 완전탐색

n	wires	result
9	[[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]	3
4	[[1,2],[2,3],[3,4]]	0
7	[[1,2],[2,7],[3,7],[3,4],[4,5],[6,7]]	1

https://school.programmers.co.kr/learn/courses/30/lessons/86971

1. 간선 관리하는 인접행렬 생성
2. 선 하나씩 끊고(양방향 모두) 끊어진 노드에서 연결된 노드 개수 체크 (bfs)
2-1. 연결된 노드는 모두 que에 추가, 방문했던 노드는 방문관리 배열에서 1로 변경 (방문한 노드 건너뛰기)
3. 끊어진 노드에 연결된 개수와 answer 최솟값 업데이트
4. 끊긴 노드 다시 연결 -> 다른 노드 확인하려고
*/

import java.util.*;

class Solution {
    static int[][] coords; 
    public int solution(int n, int[][] wires) {
        int answer = n;
        coords = new int[n+1][n+1]; //인접행렬 (1행 0000000, 2행 0000000, ..., n행 0000000)
        
        for(int[] w : wires){ //간선 1로 표시
            coords[w[0]][w[1]] = 1;
            coords[w[1]][w[0]] = 1;
        }
        
        for(int i=0; i < wires.length; i++){
            int x = wires[i][0];
            int y = wires[i][1];
            
            coords[x][y] = 0; //연결끊기
            coords[y][x] = 0;
            
            answer = Math.min(answer,bfs(n,x));
            
            coords[x][y] = 1; //다시연결하기
            coords[y][x] = 1;
        }
        
        return answer;
    }
    
    public int bfs(int n, int x){
        int cnt = 1;
        int[] visit = new int[n+1]; //방문한 노드 체크
        Queue<Integer> que = new LinkedList(); //x와 연결된 노드 모두 추가
        que.offer(x);
        
        while(!que.isEmpty()){
            int point = que.poll();
            visit[point] = 1;
            
            for(int i=0; i <= n; i++){
                //System.out.println("##"+point+"/"+i+"/"+coords[point][i]+"/"+ Arrays.toString(visit));
                if(visit[i] == 1) continue;
                if(coords[point][i] == 1){ //point와 연결된 노드
                    que.offer(i);
                    cnt++;
                }
            }
        }
        
        return (int) Math.abs(n-2*cnt); //answer = (n-cnt) - cnt => n-2*cnt
    }
}




//Fail

import java.util.*;

class Solution {
    public int solution(int n, int[][] wires) {
        int answer = -1;
        int min = 0;
        
        for(int i=0; i < n-1; i++){
            int w1 = wires[i][0];
            int w2 = wires[i][1];
            
            System.out.println("target : "+w1+"/"+w2);
            
            int start = i;
            int idx = 1;
            int cnt = 1;
            while(idx < n-2){
                start++;
                if(start >= n-2) start = 0;
                
                System.out.println(start+"/"+idx+"/"+wires[start][0]+"/"+wires[start][1]);
                
                if(w1 == wires[start][0] || w1 == wires[start][1]){
                    cnt++;
                }
                idx++;
            }
            
            min = Math.abs(n - (2 * cnt));
            answer = answer == -1 ? min : Math.min(answer,min);
            
            System.out.println(cnt+"//"+min+"//"+answer);
        }
        
        return answer;
    }
}
