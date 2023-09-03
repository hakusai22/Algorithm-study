package 比赛.LCCUP;

/*
 * @Author: hakusai
 * @Date: 2023-04-22 17:52:53
 * @LastEditTime: 2023-04-22 21:31:30
 */

 import java.util.*;
 import java.io.*;
 import java.math.*;

class Solution {

	public int[] supplyWagon(int[] supplies) {
		for (int i = (supplies.length + 1) / 2; i > 0; i--) {
			int min = 1;
			for (int j = 2; j < supplies.length; j++) {
				if (supplies[j] + supplies[j - 1] < supplies[min] + supplies[min - 1]) {
					min = j;
				}
			}
			int[] next = new int[supplies.length - 1];
			for (int j = 0; j < supplies.length; j++) {
				next[j < min ? j : j - 1] += supplies[j];
			}
			supplies = next;
		}
		return supplies;
	}
	public static void main(String[] args) {
		比赛.LCCUP.Solution solution = new Solution();
		System.out.println(solution.supplyWagon(new int[]{1,2,3,4,5}));
	}

}

