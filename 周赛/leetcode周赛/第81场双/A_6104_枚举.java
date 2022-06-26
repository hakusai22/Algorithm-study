/**
 * Copyright (c) 2022, Bongmi
 * All rights reserved
 * Author: yinpeng@bongmi.com
 */

public class A_6104_枚举 {
  public static int countAsterisks(String s) {
    char[] chars = s.toCharArray();
    int res = 0;
    int count = 0;
    for (int i = 0; i < chars.length; i++) {
      if (count == 0 && chars[i] == '*') {
        res++;
      }
      if (chars[i] == '|') {
        count = (count + 1) % 2;
      }
    }
    return res;
  }

  public static void main(String[] args) {
    System.out.println(countAsterisks("l|*e*et|c**o|*de|"));
  }
}
