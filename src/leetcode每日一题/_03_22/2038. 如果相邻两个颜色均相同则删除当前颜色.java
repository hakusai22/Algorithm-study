class Solution {
    public boolean winnerOfGame(String colors) {
        int s = 0, n = colors.length();
        for(int i = 0, j = 0; i < n; i = j) {
            while(j < n && colors.charAt(j) == colors.charAt(i))
                j++;
            if(j - i >= 3)
                s += colors.charAt(i) == 'A' ? j - i - 2 : i + 2 - j;
        }
        return s > 0;
    }
}


