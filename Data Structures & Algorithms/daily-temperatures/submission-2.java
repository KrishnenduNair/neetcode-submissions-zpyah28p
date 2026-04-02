class Solution {
    public int[] dailyTemperatures(int[] temperatures) {
        Deque<Integer> stack = new ArrayDeque<>();
        int n = temperatures.length;
        int[] res = new int[n];
        int increase = 0;

        for(int i=0;i<=n-1;i++){
            while (!stack.isEmpty() && temperatures[stack.peek()] < temperatures[i]){
                int index = stack.pop();
                res[index] = i - index; 
            } 
            stack.push(i);
        }
        return res;
    }
}
