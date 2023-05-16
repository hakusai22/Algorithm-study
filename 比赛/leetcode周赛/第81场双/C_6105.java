package 比赛.LeetCode周赛.第81场双;
/**
 * Copyright (c) 2022, Bongmi
 * All rights reserved
 * Author: yinpeng@bongmi.com
 */

public class C_6105 {

//      0->0: (0 ^ 0) & 0 = 0
//      0->1: (1 ^ 0) & 1 = 1
//      1->0: (0 ^ 1) & 0 = 0
//      1->1: (1 ^ 1) & 1 = 0
//
//      1.如果二进制中第i位，没有一个数是1，那就无论如何运算第i位都是0。
//      2.如果二进制中第i位，所有数都是1，则取任意一个数对其他数进行题目指定运算，把其他数的第i位变成0，而自身第i位仍然是1，此时其他数对应位置全是0，无法把自身第i位变成0。
//      3.如果二进制中第i位，有0有1，则对应第二种情况的中间过程。
//
//  综上，只要存在某个数，第i位是1，那么返回值的第i位一定就是1。
//  对所有数逐位或运算。

  public int maximumXOR(int[] nums) {
    int ans = 0;
    for (int v : nums) {
      ans |= v;
    }
    return ans;

  }
}
