/*
프로그래머스 java level2

number	k	return
"1924"	2	"94"
"1231234"	3	"3234"
"4177252841"	4	"775841"

https://school.programmers.co.kr/learn/courses/30/lessons/42883
*/

/*
설명 : 
4177252841  10자리 - 4개 = 6개남아야함

1. 4177252841 -> 41772 뒤에 5자리 남김 
: 제일 큰 수 7, 제외 수 41, 남는 수 72 / answer : 7

(마지막 5자리 남기는 이유 : 111112 경우 마지막 2가 제일 커서 2 앞 모두 제외하고 2를 뺴면 뒤에 4자리만 남아서 6자리를 완성할 수 없다.)

2. 7252841 -> 725 뒤에 4자리 남김    
: 제일 큰 수 7, 제외 수 : x, 남는 수 25 / answer : 77

3. 252841 -> 252 3자리 남김 
: 제일 큰 수 5, 제외 수 2, 남는 수 2 / answer : 775

4. 2841 -> 28 2자리 남김
: 제일 큰 수 8, 제외 수 2, 남는 수 x / answer : 7758

5. 41 -> 4 1자리 남김
: 제일 큰 수 4, 제외 수 x, 남는 수 x / answer : 77584

6. 1 / answer : 775841
*/


class Solution {
    public String solution(String number, int k) {
        StringBuilder answer = new StringBuilder("");
        int answerLen = number.length() - k;
        int leftNumLen = k + 1;
        int start = 0;
        
        while(answer.length() < answerLen){
            int max = 0;
            for(int i=start; i < leftNumLen; i++){
                if(max < number.charAt(i) - '0'){
                    max = number.charAt(i) - '0';
                    start = i+1;
                }
            }
            answer.append(max);
            leftNumLen++;
        }
        
        return answer.toString();
    }
}




