/*
프로그래머스 level3 greedy 

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
            if(getParent(parent,costs[i][0]) != getParent(parent,costs[i][1])){
                answer += costs[i][2];
                union(parent,costs[i][0],costs[i][1]);
            }
        }
        
        return answer;
    }
    
    private int getParent(int[] parent, int node){
        if(parent[node] == node) return node;
        return getParent(parent, parent[node]);
    }
    public void union(int[] parent, int node1, int node2){
        int n1 = getParent(parent, node1);
        int n2 = getParent(parent, node2);
        
        if(n1 < n2) parent[n2] = n1;
        else parent[n1] = n2;
        
        //System.out.println(Arrays.toString(parent));
    }
}
