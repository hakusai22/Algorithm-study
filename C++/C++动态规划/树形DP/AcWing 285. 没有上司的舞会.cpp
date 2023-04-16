#include <bits/stdc++.h>

using namespace std;

/*
    -*- coding: utf-8 -*-
    @Author  : wheat
    @Time    : 2023/02/03 16:47
*/

/**
 """
    Ural 大学有 N 名职员，编号为 1∼N
    他们的关系就像一棵以校长为根的树，父节点就是子节点的直接上司。
    每个职员有一个快乐指数，用整数 Hi给出，其中 1≤i≤N
    现在要召开一场周年庆宴会，不过，没有职员愿意和直接上司一起参会。
    在满足这个条件的前提下，主办方希望邀请一部分职员参会，使得所有参会职员的快乐指数总和最大，求这个最大值。

    //f[u][1]:以u为根节点的子树并且包括u的总快乐指数，
    //f[u][0]:以u为根节点并且不包括u的总快乐指数;
"""
 */

const int N = 6010;
int n;
int happy[N]; //每个职工的高兴度
int f[N][2]; //上面有解释哦~
int e[N], ne[N], h[N], idx; //链表，用来模拟建一个树
bool has_father[N]; //判断当前节点是否有父节点

//f[u][1]:以u为根节点的子树并且包括u的总快乐指数，
//f[u][0]:以u为根节点并且不包括u的总快乐指数;
void add(int a, int b) { //邻接表建图
    e[idx] = b, ne[idx] = h[a], h[a] = idx++;
}

void dfs(int u) { //开始求解题目
    f[u][1] = happy[u]; //如果选当前节点u，就可以把f[u,1]先怼上他的高兴度
    for (int i = h[u]; ~i; i = ne[i]) { //从头节点开始遍历邻接表
        int j = e[i]; //取出相连点所存的值 （点的编号）
        dfs(j); //回溯
        //状态转移部分，上面有详细讲解~
        f[u][0] += max(f[j][1], f[j][0]); //u可以作为j和u的上司的中间人，j来不来都可以
        f[u][1] += f[j][0]; //u是j的上司，存在领导关系，所以一定不能让j来
    }
}

int main() {
    scanf("%d", &n);
    for (int i = 1; i <= n; i++) scanf("%d", &happy[i]); //输入每个人的高兴度
    memset(h, -1, sizeof h); //把h都赋值为-1
    for (int i = 1; i < n; i++) {
        int a, b; //对应题目中的L,K,表示b是a的上司
        scanf("%d%d", &a, &b); //输入~
        has_father[a] = true; //说明a他有爸爸（划掉）上司
        add(b, a); //把a加入到b的后面
    }
    int root = 1; //用来找根节点
    while (has_father[root]) root++; //找根节点
    dfs(root); //从根节点开始搜索
    printf("%d\n", max(f[root][0], f[root][1])); //输出不选根节点与选根节点的最大值
    return 0;
}

