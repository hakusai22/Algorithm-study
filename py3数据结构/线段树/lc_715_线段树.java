class SegTree{
    int l,r;//表示的是这个闭区间代表的左右边界
    SegTree left,right;
    boolean covered;//区间内的数字是否都被覆盖了
    public SegTree(int l,int r){
        this.l=l;
        this.r=r;
        this.covered=false;
    }
    public SegTree(int l,int r,boolean covered){
        this.l=l;
        this.r=r;
        this.covered=covered;
    }
}
class RangeModule {
    SegTree st;
    public RangeModule() {
        st=new SegTree(0,(int)1e9);
    }

    public void addRange(int left, int right) {
        addNum(st,left,right-1);
    }
    void addNum(SegTree t,int a,int b){
        //此方法在线段树中添加闭区间[a,b]
        int l=t.l,r=t.r,mid=(l+r)>>1;
        if(t.covered){return;}//区间内数字已经全部存在，无需进一步操作
        if(l>=a&&r<=b){
            //完全精准覆盖（所有添加操作最后一步都会到这里），此时只需要把这个区间设为true，删除所有子区间即可
            t.covered=true;
            t.left=t.right=null;
        }
        else if(b<=mid){
            //只更新左半边即可
            if(t.left==null){t.left=new SegTree(l,mid);}
            addNum(t.left,a,b);
        }
        else if(a>mid){
            //只更新右半边即可
            if(t.right==null){t.right=new SegTree(mid+1,r);}
            addNum(t.right,a,b);
        }
        else{
            //同时更新左右半边
            if(t.left==null){t.left=new SegTree(l,mid);}
            if(t.right==null){t.right=new SegTree(mid+1,r);}
            addNum(t.left,a,mid);
            addNum(t.right,mid+1,b);
        }
    }

    public boolean queryRange(int left, int right) {
        return allCovered(st,left,right-1);
    }
    boolean allCovered(SegTree t,int a,int b){
        //此方法判断在闭区间[a,b]的所有数字是否都存在
        if(t==null){return false;}
        int l=t.l,r=t.r,mid=(l+r)>>1;
        if(t.covered){return true;}//所有的判断操作最后叶处都会分为这样的小操作
        if(b<=mid){return allCovered(t.left,a,b);}//在左边判断
        else if(a>mid){return allCovered(t.right,a,b);}//在右边判断
        return allCovered(t.left,a,mid)&&allCovered(t.right,mid+1,b);//在两边判断
    }

    public void removeRange(int left, int right) {
        removeNum(st,left,right-1);
    }
    void removeNum(SegTree t,int a,int b){
        //此方法移除树内闭区间[a,b]的所有数字
        if(t==null){return;}//区间不存在，说明本来就不存在这些数字
        int l=t.l,r=t.r,mid=(l+r)>>1;
        if(l>b||r<a){return;}
        if(l>=a&&r<=b){
            //如果删除的区间完全包括树的区间，那么设为false后，删除所有子区间
            t.left=t.right=null;
        }
        else if(t.covered){
            //此时线段树区间大于删除区间且区间内数字都存在，那么需要恢复左右子树后进行操作
            t.left=new SegTree(l,mid,true);
            t.right=new SegTree(mid+1,r,true);
            if(b<=mid){
                //需要处理左半部分，但是需要保持右半部分的情况与t相同，剩余的部分要纹丝不动
                removeNum(t.left,a,b);
            }
            else if(a>mid){
                //需要处理右半部分，但是需要保持左半部分的情况与t相同，剩余的部分要纹丝不动
                removeNum(t.right,a,b);
            }
            else{
                //需要处理左右两部分
                removeNum(t.left,a,mid);
                removeNum(t.right,mid+1,b);
            }
        }
        else{
            //此时树内的数字不全存在，需要进一步看左右子树的情况后再进行操作
            if(b<=mid){removeNum(t.left,a,b);}
            else if(a>mid){removeNum(t.right,a,b);}
            else{
                removeNum(t.left,a,mid);
                removeNum(t.right,mid+1,b);
            }
        }
        t.covered=false;//这个区间内的数字已经不全存在，因此要设成false
    }
}

