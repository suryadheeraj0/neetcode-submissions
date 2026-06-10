class Solution {
    public int maxAreaOfIsland(int[][] grid) {
        Queue<int[]> queue = new LinkedList<>();
        int[][] directions = new int[][]{{0,1},{1,0},{0,-1},{-1,0}};
        int res = 0;
        for(int i=0;i<grid.length;i++){
            for(int j=0;j<grid[0].length;j++){
                if(grid[i][j]==1){
                    grid[i][j]=0;
                    queue.offer(new int[] {i,j});
                    res = Math.max(res,count_max_area(grid, queue, directions));
                }
            }
        }
        return res;
    }

    public int count_max_area(int[][] grid, Queue<int[]> queue, int[][] directions){
        int count_area = 1;
        while(!queue.isEmpty()){
            int[] rowcol = queue.poll();
            for(int[] dir:directions){
                int new_r = rowcol[0]+dir[0];
                int new_c = rowcol[1]+dir[1];

                if(new_r>=0 && new_r<grid.length && new_c>=0 && new_c<grid[0].length){
                    if(grid[new_r][new_c]==1){
                        count_area++;
                        grid[new_r][new_c]=0;
                        queue.add(new int[] {new_r,new_c});
                    }
                }
            }
        }
        return count_area;
    }
}