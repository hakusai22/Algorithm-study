package 比赛.LeetCode周赛.第81场双;

public class B_6106_并查集 {

  class UnionFind {
    int[] parent;
    int[] size;
    int n;

    public UnionFind(int n) {
      this.n = n;
      parent = new int[n];
      size = new int[n];
      for (int i = 0; i < n; ++i) {
        parent[i] = i;
        size[i] = 1;
      }
    }

    private int find(int p) {
      if (parent[p] != p) {
        parent[p] = find(parent[p]);
      }
      return parent[p];
    }

    private void union(int p, int q) {
      int pp = find(p);
      int qq = find(q);
      if (pp == qq) return;
      parent[pp] = qq;
      size[qq] += size[pp];
    }
  }

  public long countPairs(int n, int[][] edges) {
    UnionFind union = new UnionFind(n);

    for (int i = 0; i < edges.length; i++) {
      union.union(edges[i][0], edges[i][1]);
    }
    long ans = 0L;
    for (int i = 0; i < n; ++i) {
      ans += n - union.size[union.find(i)];
    }
    return ans / 2;
  }
}
