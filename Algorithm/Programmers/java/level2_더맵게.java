import java.util.PriorityQueue;

class Solution {
    public int solution(int[] scoville, int K) {
        int answer = 0;
        PriorityQueue<Integer> heap = new PriorityQueue<>();
        
        for(int scov : scoville){
            heap.offer(scov);
        }
        while(heap.peek() <= K){
            if(heap.size() == 1) return -1;
            
            int firstMin = heap.poll();
            int secondMin = heap.poll();
            int newScov = firstMin+(secondMin * 2);
            heap.offer(newScov);
            answer++;
        }
        
        return answer;
    }
}
