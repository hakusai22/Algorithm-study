package 比赛.LeetCode周赛.第80场双;
import java.util.Arrays;

class B_6096 {
  public int[] successfulPairs(int[] spells, int[] potions, long success) {
    int[] res = new int[spells.length];
    Arrays.sort(potions);
    for (int i = 0; i < spells.length; i++) {
      long temp = spells[i];
      int l = 0, r = potions.length;
      while (l < r) {
        int m = (l + r)/2;
        if (temp * (long) potions[m] >= success) {
          r = m;
        } else {
          l = m+1;
        }
      }
      res[i]=potions.length-l;
    }
    return res;
  }
}