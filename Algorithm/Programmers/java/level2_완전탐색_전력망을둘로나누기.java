



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
