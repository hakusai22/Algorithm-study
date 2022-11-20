class lc_307_线段树板子 {
    Node[] tr;
    class Node {
        int l, r, v;
        Node(int _l, int _r) {
            l = _l; r = _r;
        }
    }
  //从编号为 u 的节点开始，构造范围为 [l,r] 的树节点
    void build(int u, int l, int r) {
        tr[u] = new Node(l, r);
        if (l == r) return;
      // 中间值 进行递归构建 <<1 左移一位 相当于乘以2
        int mid = l + r >> 1;
        //2*u l mid
        build(u << 1, l, mid);
        //2*u+1 mid+1 r
        build(u << 1 | 1, mid + 1, r);
    }

  //从编号为 u 的节点开始，在 x 位置增加 v
    void update(int u, int x, int v) {
        //叶子结点+v
        if (tr[u].l == x && tr[u].r == x) {
            tr[u].v += v;
            return ;
        }
        //往上更新值
      //mid
        int mid = tr[u].l + tr[u].r >> 1;
      //2*u 左边
        if (x <= mid) update(u << 1, x, v);
      //2*u+1 右边
        else update(u << 1 | 1, x, v);
        pushup(u);
    }

    //往上更新值
    void pushup(int u) {
        tr[u].v = tr[u << 1].v + tr[u << 1 | 1].v;
    }

  //从编号为 u 的节点开始，查询 [l, r] 区间和为多少
    int query(int u, int l, int r) {
        if (l <= tr[u].l && tr[u].r <= r) return tr[u].v;
            //mid
        int mid = tr[u].l + tr[u].r >> 1;
        int ans = 0;
            //2*u
        if (l <= mid) ans += query(u << 1, l, r);
            //2*u+1
        if (r > mid) ans += query(u << 1 | 1, l, r);
        return ans;
    }


    int[] nums;
    public lc_307_线段树板子(int[] _nums) {
        nums = _nums;
        int n = nums.length;
        tr = new Node[n * 4];
        build(1, 1, n);
        for (int i = 0; i < n; i++) update(1, i + 1, nums[i]);
    }
    public void update(int index, int val) {
        update(1, index + 1, val - nums[index]);
        nums[index] = val;
    }
    public int sumRange(int left, int right) {
        return query(1, left + 1, right + 1);
    }
}