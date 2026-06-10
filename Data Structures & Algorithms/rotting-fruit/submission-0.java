class Solution {
    public int orangesRotting(int[][] grid) {
        int freshOrange = 0;
        int timeCount = 0;
        Queue<int[]> queue = new LinkedList<>();
        int[][] directions = new int[][]{{0,1},{1,0},{-1,0},{0,-1}};
        for(int i=0;i<grid.length;i++){
            for(int j=0;j<grid[0].length;j++){
                if(grid[i][j]==1){
                    freshOrange++;
                }
                if(grid[i][j]==2){
                    queue.offer(new int[] {i,j});
                }
            }
        }
        if(freshOrange==0){
            return 0;
        }
        while(!queue.isEmpty() && freshOrange > 0){
            int size = queue.size();
            for(int k=0;k<size;k++){
                int[] rowcol = queue.poll();
                for(int[] dir:directions){
                    int new_r = rowcol[0]+dir[0];
                    int new_c = rowcol[1]+dir[1];
                    if(new_r>=0 && new_r<grid.length && new_c>=0 && new_c<grid[0].length){
                        if(grid[new_r][new_c]==1){
                            grid[new_r][new_c]=2;
                            freshOrange--;
                            queue.offer(new int[] {new_r,new_c});
                        }
                    }
                }
            }
            timeCount++;
        }
        if(freshOrange==0){
            return timeCount;
        }
        else{
            return -1;
        }
    }
}