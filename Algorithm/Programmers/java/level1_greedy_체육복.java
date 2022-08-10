/*
프로그래머스 level1 탐욕

n	lost	reserve	return
5	[2, 4]	[1, 3, 5]	5
5	[2, 4]	[3]	4
3	[3]	[1]	2
*/

// 통과 case
import java.util.*;

class Solution {
    public int solution(int n, int[] lost, int[] reserve) {
        int answer = 0;
        int[] result = new int[n+2];

        for(int l : lost) result[l]--;
        for(int r : reserve) result[r]++;
        
        for(int i=1; i <= n; i++){
            if(result[i] != 1) continue;
            if(result[i-1] == -1){
                result[i-1]++;
                result[i]--;
            }else if(result[i+1] == -1){
                result[i+1]++;
                result[i]--;
            }
        }
        
        for(int i=1; i <= n; i++){
            if(result[i] > -1) answer++;   
        }
        
        return answer;
    }
}


// case 17~20 실패 
import java.util.*;

class Solution {
    public int solution(int n, int[] lost, int[] reserve) {
        int answer = 0;
        int[] result = new int[n];

        Arrays.fill(result, 1);
        Arrays.sort(lost);
        Arrays.sort(reserve);
        
        for(int l : lost) result[l-1] -= 1;
        for(int r : reserve) result[r-1] += 1;
        for(int i=0; i < n; i++){
            if(result[i] > 0) continue;
            if(i+1 < n && result[i+1] == 2){
                result[i+1] -= 1;
                result[i] += 1;
            }else if(i-1 > 0 && result[i-1] == 2){
                result[i-1] -= 1;
                result[i] += 1;
            } 
        }
        
        System.out.println(Arrays.toString(result));
        
        for(int i : result){
            if(i == 0) continue;
            answer += 1;
        }
        
        return answer;
    }
}
