class Solution {
    public int lastStoneWeight(int[] stones) {
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        int first_largest;
        int second_largest;
        int res = 0;
        for(int i:stones){
            pq.add(-i);
        }
        while(pq.size()>1){
            first_largest = Math.abs(pq.poll());
            second_largest = Math.abs(pq.poll());
            System.out.println(first_largest+" "+second_largest);
            if(first_largest!=second_largest){
                pq.offer(-(first_largest-second_largest));
            }
        }
        if(!pq.isEmpty()){
            res = pq.peek();
        }
        return Math.abs(res);
    }
}
