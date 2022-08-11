/*
프로그래머스 level2 greedy

people	limit	return
[70, 50, 80, 50]	100	3
[70, 80, 50]	100	3

https://school.programmers.co.kr/learn/courses/30/lessons/42885

1. people 오름차순 정렬
2. left와 right로 적은값 + 많은값으로 limit 비교한다.
3. 무게가 limit이상이면 pass
*/


import java.util.*;

class Solution {
    public int solution(int[] people, int limit) {
        int answer = 0;
        Arrays.sort(people);
        
        int left = 0;
        int right = people.length - 1;
        
        while(left <= right){
            if(people[left] + people[right] <= limit){
                left++;
                right--;
            }else{
                right--;
            }
            answer++;
        }
        
        return answer;
    }
}
