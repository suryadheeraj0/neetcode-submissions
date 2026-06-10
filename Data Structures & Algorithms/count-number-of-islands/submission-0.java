class Solution {
    public int numIslands(char[][] grid) {
        int m = grid.length;
        int n = grid[0].length;
        int[][] directions = new int[][]{{0,1},{1,0},{0,-1},{-1,0}};
        Queue<int[]> queue = new LinkedList<>();
        int res = 0;
        for(int i=0;i<m;i++){
            for(int j=0;j<n;j++){
                if(grid[i][j]=='1'){
                    queue.offer(new int[]{i,j});
                    count_num_islands(queue, directions, grid);
                    res++;
                }
            }
        }
        return res;
    }

    public void count_num_islands(Queue<int[]> queue, int[][] directions, char[][] grid){
        while(queue.size()!=0){
            int[] rowandcol = queue.poll();
            int r = rowandcol[0];
            int c = rowandcol[1];
            for(int[] dir: directions){
                int new_r = r+dir[0];
                int new_c = c+dir[1];
                if(new_r>=0 && new_r<grid.length && new_c>=0 && new_c<grid[0].length){
                    if(grid[new_r][new_c]=='1'){
                        grid[new_r][new_c]='0';
                        queue.offer(new int[]{new_r,new_c});
                    }
                }
            }
        }
    }
}