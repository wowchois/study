/*
프로그래머스 level3 greedy 

크루스칼 알고리즘

n	costs	return
4	[[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]	4

https://school.programmers.co.kr/learn/courses/30/lessons/42861
*/

import java.util.*;

class Solution {
    public int solution(int n, int[][] costs) {
        int answer = 0;
        int[] parent = new int[n];
        
        for(int i=0; i<n;i++) parent[i] = i;
        
        //비용으로 오름차순 정렬
        Arrays.sort(costs, (c1,c2) -> c1[2]-c2[2]); 
        
        for(int i=0; i<costs.length; i++){
            if(getParent(parent,costs[i][0]) != getParent(parent,costs[i][1])){ //같으면 노드roop가 생기기 때문에 달라야 한다.
                answer += costs[i][2];
                union(parent,costs[i][0],costs[i][1]); //부모노드로 합치기
            }
        }
        
        return answer;
    }
    
    //부모 노트 확인
    private int getParent(int[] parent, int node){
        if(parent[node] == node) return node;
        return getParent(parent, parent[node]);
    }
    //노드 합치기 (연결된 노드에서 cost가 낮은 노드의 부모에 속하게 합치기)
    public void union(int[] parent, int node1, int node2){
        int n1 = getParent(parent, node1);
        int n2 = getParent(parent, node2);
        
        if(n1 < n2) parent[n2] = n1;
        else parent[n1] = n2;
        
        //System.out.println(Arrays.toString(parent)); // [0,0,2,3] 이런식으로 변경됨.
    }
}
