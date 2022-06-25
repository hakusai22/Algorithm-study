/**
 * @author Fomalhaut
 * @date 2022/6/24
 * @desc 731. 我的日程安排表 II
 */
public class Q731 {


    public static void main(String[] args) {
        MyCalendarTwo MyCalendar = new MyCalendarTwo();
        System.out.println(MyCalendar.book(10, 20));    // true
        System.out.println(MyCalendar.book(50, 60));    // true
        System.out.println(MyCalendar.book(10, 40));    // true
        System.out.println(MyCalendar.book(5, 15));     // false
        System.out.println(MyCalendar.book(5, 10));     // true
        System.out.println(MyCalendar.book(25, 55));    // true
    }

    static class MyCalendarTwo {
        /*
        这题也可以用线段树进行求解:start与end的范围为[0,1e9]
        不过相比于Q729 我的日程安排表I 这里要维护的val为区间的最大值max
        当区间的最大值>=2就说明已经有两个重叠的预订,第3个预订就不能book了
        查询和更新一次时间复杂度为:O(logN) 空间复杂度为O(MlogN),M为操作次数
         */

        /*
        节点类
         */
        static class Node {
            int ls, rs, add, max;   // ls, rs 为左右子节点在tr中索引(触手); add 懒标记; max 维护区间最大值
        }

        int N = (int) 1e9, M = 120010, cnt = 1; // N 区间范围; M 节点个数; cnt 节点在tr中的索引
        Node[] tr = new Node[M];

        public MyCalendarTwo() {
            tr[0] = new Node(); // 创建根节点
        }

        /*
        更新区间[l,r] 值为val
         */
        public void update(int u, int lc, int rc, int l, int r, int val) {
            // [l,r]在u表示的区间内
            if (lc >= l && rc <= r) {
                tr[u].add += val;   // 懒标记要累计(例如覆盖了2次)
                // 最大值是max(curVal,curVal+val)=curVal+val -> max += val;
                tr[u].max += val;
                return; // 结束
            }
            // [l,r]不在u内
            lazyCreate(u);  // 动态开点
            pushDown(u);    // 下传懒标记
            int mid = lc + (rc - lc) / 2;
            if (l <= mid) update(tr[u].ls, lc, mid, l, r, val); // 占据到左子树
            if (r > mid) update(tr[u].rs, mid + 1, rc, l, r, val);  // 占据到右子树
            pushUp(u);  // 回溯
        }

        /*
       查询区间[l,r]的最大值
         */
        public int query(int u, int lc, int rc, int l, int r) {
            if (lc >= l && rc <= r) return tr[u].max;
            lazyCreate(u);  // 冬天开点
            pushDown(u);    // 下传懒标记
            int mid = lc + (rc - lc) / 2, res = 0;
            if (l <= mid) res = query(tr[u].ls, lc, mid, l, r);
            if (r > mid) res = Math.max(res, query(tr[u].rs, mid + 1, rc, l, r));   // 记得取左右子节点的最大值
            return res; // 返回最大值
        }

        /*
        按需动态开点
         */
        public void lazyCreate(int u) {
            if (tr[u].ls == 0) {    // 左子节点不存在 -> 创建并构建连接
                tr[u].ls = cnt++;
                tr[tr[u].ls] = new Node();
            }
            if (tr[u].rs == 0) {
                tr[u].rs = cnt++;
                tr[tr[u].rs] = new Node();
            }
        }

        /*
        下传懒标记
         */
        public void pushDown(int u) {
            int v = tr[u].add;  // 节点u下传下来的懒标记
            if (v != 0) {   // 当且仅当懒标记不为0才进行下传
                // 下传懒标记至子节点(累计)
                tr[tr[u].ls].add += v;
                tr[tr[u].rs].add += v;
                // 更新左右子节点的值(累计)
                tr[tr[u].ls].max += v;
                tr[tr[u].rs].max += v;
                tr[u].add = 0;  // 下传懒标记完成撤销u的懒标记
            }
        }

        /*
        回溯更新u的最大值
         */
        public void pushUp(int u) {
            tr[u].max = Math.max(tr[tr[u].ls].max, tr[tr[u].rs].max);
        }

        public boolean book(int start, int end) {
            // 最大值>=2说明区间[start,end-1]存在某个点覆盖了2次
            if (query(0, 0, N, start, end - 1) >= 2) return false;
            update(0, 0, N, start, end - 1, 1);
            return true;
        }
    }

}