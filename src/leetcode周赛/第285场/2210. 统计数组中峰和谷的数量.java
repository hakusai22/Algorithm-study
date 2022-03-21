package leetcode周赛.第285场;

class Solution {
    public int countHillValley(int[] nums) {
        int res = 0;
        // 定义一个j用于存储前一个不重复的值的下标
        for(int i = 1,j = 0; i < nums.length-1; i++) {
            if(nums[i] == nums[i+1]) continue;
            if(nums[i] > nums[j] && nums[i] > nums[i+1]) res++;
            if(nums[i] < nums[j] && nums[i] < nums[i+1]) res++;
            j = i;
        }
        return res;
    }
}
