import java.util.ArrayDeque;
import java.util.Deque;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Set;

/**
 * Copyright (c) 2022, Bongmi
 * All rights reserved
 * Author: yinpeng@bongmi.com
 */

public class lcp_07_BFS {

  public int numWays(int n, int[][] rs, int k) {
    Map<Integer, Set<Integer>> map = new HashMap<>();
    for (int[] r : rs) {
      int a = r[0], b = r[1];
      Set<Integer> s = map.getOrDefault(a, new HashSet<>());
      s.add(b);
      map.put(a, s);
    }
    Deque<Integer> d = new ArrayDeque<>();
    d.addLast(0);
    while (!d.isEmpty() && k-- > 0) {
      int size = d.size();
      while (size-- > 0) {
        int poll = d.pollFirst();
        Set<Integer> es = map.get(poll);
        if (es == null) continue;
        for (int next : es) {
          d.addLast(next);
        }
      }
    }
    int ans = 0;
    while (!d.isEmpty()) {
      if (d.pollFirst() == n - 1) ans++;
    }
    return ans;
  }
}
