package leetcode周赛.第285场;

class Solution {
    public int countCollisions(String directions) {
        int l = 0, r = directions.length() - 1;
        int res = 0;
        while(l <= r && directions.charAt(l) == 'L') l ++;
        while(l <= r && directions.charAt(r) == 'R') r --;
        for(int i = l; i <= r; i ++){
            if(directions.charAt(i) == 'L' || directions.charAt(i) == 'R'){
                res ++;
            }
        }
        return res;
    }
}