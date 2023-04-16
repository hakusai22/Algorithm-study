#include <bits/stdc++.h>

using namespace std;

/*
    -*- coding: utf-8 -*-
    @Author  : wheat
    @Time    : 2023/01/17 16:47
*/

/**
 # 数组
    int a[n]; //创建大小为n的数组, 下标范围[0,n-1]
    memset(a, 0, sizeof(a)); // 初始化所有元素为0

 Vector
    # 初始化
    vector<int> a;  //开一个vector，没有容量  vector<int> a(n);  //开一个大小为n的vector，值为初始值(0或其他)
    vector<int> a(n,x);	//开一个大小为n的vector，并全部复制为x //vector<int> b(a);  //开一个vector名字为b并将a的值全部复制给b
    vector<int> b(a.begin(),a.end());  //同上 vector<int> b(&a[0],&a[5]);  //同上

    v.push_back(1); //给数组末尾增加元素1，数组长度增加1 v.pop_back();	//删除数组末尾元素，数组长度-1，注意在数组不为空的情况下进行
    v.empty(); // 返回数组是否为空 v.size(); // 返回数组中的元素个数

    # 二维数组
        vector<vector<int> > a;  //初始化二维数组  vector<vector<int> > a(10,vector<int> (10,0));  //创建一个10行10列的数组

    # 字符串
        s.length();//返回字符串大小 s.push_back(char);//在尾部插入一字符 s.append(string);//在s后追加字符串
        s.substr(int left,int length);	//从下标left开始往后截取length个长度  sort(s.begin(),s.end());	//按照字典序进行排序，包前不包后
        s.compare(left1,right1,str,left2,right2);	//若不填left与right，则默认为整个字符串
        s.erase(iterator);	//删除迭代器所指的字符  s.erase(int left,int length);	//删除从下标left开始往后length个字符
        s.replace(int left,int length,string target);//将下标从left往后的length个字符替换为target
        s.find(string);	//查找目标字符串第一次出现的下标位置 s.find(char,index);	//从index下标开始查找字符第一次出现的位置

    # 栈 stack<int> s1;	//声明一个栈
        s1.empty();//判断是否为空 s1.pop();//出栈但不返回值 s1.push(int);//入栈 s1.size();//返回栈元素个数 s1.top();//取栈顶元素

    # 队列
        queue<int> q; // 初始化一个队列 q.push(1); // 入队，向队尾增加元素1 q.front(); // 返回当前队列头元素值，注意在队列不为空的情况下进行
        q.pop(); // 出队，弹出队头元素 q.empty(); // 返回当前队列是否为空 q.size(); // 返回当前队列的元素个数

    # 排序
        sort(arr,arr+length,less<int>());		//对arr数组从小到大排序[默认] sort(arr,arr+length,greater<int>());	//从大到小排序

    # 优先队列 priority_queue
        大顶堆 priority_queue<int> max_heap; //priority_queue<int, vector<int>, less<int>> max_heap;
        小顶堆 priority_queue<int, vector<int>, greater<int>> min_heap;
        priority_queue<int> pq; // 初始化一个大顶堆  pq.push(1); // 向堆中插入一个元素 pq.top(); // 返回堆顶元素值
        pq.pop(); // 移除堆顶元素 pq.empty(); // 返回当前堆是否为空 pq.size(); // 返回当前堆中元素个数

    # 哈希表：unordered_set
        unordered_set<int> s; // 创建哈希表 s.insert(1); // 向哈希表中插入元素1
        s.count(1); // 返回哈希表中是否存在元素1 s.size(); // 返回哈希表中元素个数

    # 键值哈希表：unordered_map  unordered_map<int, int> mp; // 创建键值哈希表，第一个类型为key类型，第二个类型为value类型
        mp[1] = 10; // 设定key为1的value为10 mp[1]++; // 设定key为1的value增加1  mp.count(1); // 返回键值哈希表中是否存在键值为1的元素
        mp[1]; // 获取key为1的value，如果不存在，会自动创建key为1，value为默认0 mp.size(); // 返回哈希表中元素个数

    # 红黑树：set set<int> s; // s.insert(1); // 插入元素1  s.count(1); // 返回红黑树中是否存在元素1 //s.size(); 返回红黑树中元素个数

    # 键值红黑树：map  map<int, int> mp; // 创建键值红黑树，第一个类型为key类型，第二个类型为value类型
        mp[1] = 10; // 设定key为1的value为10   mp[1]++; // 设定key为1的value增加1  mp.count(1); // 返回键值红黑树中是否存在键值为1的元素
        mp[1]; // 获取key为1的value，如果不存在，会自动创建key为1，value为默认0 mp.size(); // 返回红黑树中元素个数

    # 数学 max(x, y);min(x, y); abs(x); ceil(x) floor(x) abs(x)
 */


const int N = 210, M = 2e+10, INF = 1e9;

int n, m, k, x, y, z;
int d[N][N];

void floyd() {
    for (int k = 1; k <= n; k++)
        for (int i = 1; i <= n; i++)
            for (int j = 1; j <= n; j++)
                d[i][j] = min(d[i][j], d[i][k] + d[k][j]);
}

int main() {
    cin >> n >> m >> k;
    for (int i = 1; i <= n; i++)
        for (int j = 1; j <= n; j++)
            if (i == j) d[i][j] = 0;
            else d[i][j] = INF;
    while (m--) {
        cin >> x >> y >> z;
        d[x][y] = min(d[x][y], z);
        //注意保存最小的边
    }
    floyd();
    while (k--) {
        cin >> x >> y;
        if (d[x][y] > INF / 2) puts("impossible");
            //由于有负权边存在所以约大过INF/2也很合理
        else cout << d[x][y] << endl;
    }
    return 0;
}

