#include <bits/stdc++.h>

using namespace std;

/*
    -*- coding: utf-8 -*-
    @Author  : wink
    @Time    : 2023/04/03 13:46
    优先队列底层是用二叉堆实现的(大根堆)
*/

int main() {
    //1.定义
    priority_queue<int> myPriorityQueue;

    //2.获得队列长度，目前还没有任何元素进队，所以应该为0
    cout << "the size of myPriorityQueue: " << myPriorityQueue.size() << endl;

    //3.入队，数字1-9入队
    for (int i = 1; i < 10; i++) {
        myPriorityQueue.push(i);
    }

    //4.访问队列长度、优先级最高元素
    cout << "the size of myPriorityQueue: " << myPriorityQueue.size() << endl;;
    cout << "the top of myPriorityQueue: " << myPriorityQueue.top() << endl;

    //5.访问整个队列并计算总和
    int sum = 0;
    while (!myPriorityQueue.empty()) {
        int tmp = myPriorityQueue.top(); //记录优先级最高元素
        sum += tmp;
        cout << tmp << " ";
        myPriorityQueue.pop();
    }
    cout << endl;
    cout << "sum: " << sum << endl;

    //6.判断优先队列是否为空，由于上个操作删除了队列中的所有元素，故现在队列为空
    if (myPriorityQueue.empty()) {
        cout << "myPriorityQueue is empty." << endl;
    }

    //7.1交换两个队列元素
    priority_queue<int> foo;
    priority_queue<int> bar;
    foo.push(10);
    foo.push(20);
    foo.push(30);
    bar.push(100);
    bar.push(200);
    bar.emplace(2421);
// 	foo.swap(bar);
    swap(foo, bar);
    //7.2输出交换后的各个队列的元素
    cout << "foo: ";
    while (!foo.empty()) {
        int tmp1 = foo.top();
        cout << tmp1 << " ";
        foo.pop();
    }
    cout << endl;
    cout << "bar: ";
    while (!bar.empty()) {
        int tmp2 = bar.top();
        cout << tmp2 << " ";
        bar.pop();
    }
    return 0;
}

