import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Set;

/**
 * Copyright (c) 2022, Bongmi
 * All rights reserved
 * Author: yinpeng@bongmi.com
 */

public class lcp_07_DFS {
  Map<Integer, Set<Integer>> map = new HashMap<>();
  int n, k, ans;

  public int numWays(int _n, int[][] rs, int _k) {
    n = _n;
    k = _k;
    for (int[] r : rs) {
      int a = r[0], b = r[1];
      Set<Integer> s = map.getOrDefault(a, new HashSet<>());
      s.add(b);
      map.put(a, s);
    }
    dfs(0, 0);
    return ans;
  }

  void dfs(int u, int sum) {
    if (sum == k) {
      if (u == n - 1) ans++;
      return;
    }
    Set<Integer> es = map.get(u);
    if (es == null) return;
    for (int next : es) {
      dfs(next, sum + 1);
    }
  }
}
