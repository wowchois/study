class Solution {
    public String solution(int[] numbers, String hand) {
        String answer = "";
        int l_hand = 10;
        int r_hand = 12;
        
        for(int n : numbers){
            if(n == 1 || n == 4 || n == 7){
                l_hand = n;
                answer += "L";
            }else if(n == 3 || n == 6 || n == 9){
                r_hand = n;
                answer += "R";
            }else{
                if(n == 0) n = 11;
                
                int l_dist = getDist(l_hand,n);
                int r_dist = getDist(r_hand,n);
                
                if((l_dist < r_dist) 
                   || (l_dist == r_dist && "left".equals(hand))){
                    l_hand = n;
                    answer += "L";
                }else if((l_dist > r_dist) 
                   || (l_dist == r_dist && "right".equals(hand))){
                    r_hand = n;
                    answer += "R";
                }
            }
        }
        return answer;
    }
    
    private int getDist(int now, int move){
        return (Math.abs(now-move) / 3) + (Math.abs(now-move) % 3);
    }
}
