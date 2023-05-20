package 比赛.LeetCode周赛.第80场双;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Set;

/**
 * Copyright (c) 2022, Bongmi
 * All rights reserved
 * Author: yinpeng@bongmi.com
 */

public class C_6097 {
  public static boolean matchReplacement(String s, String sub,
      char[][] mappings) {
    HashMap<Character, Set<Character>> map = new HashMap<>();
    for (int i = 0; i < mappings.length; i++) {
      if (map.containsKey(mappings[i][0])) {
        Set<Character> characters = map.get(mappings[i][0]);
        characters.add(mappings[i][1]);
        map.put(mappings[i][0], characters);
      } else {
        Set<Character> characters = new HashSet<>();
        characters.add(mappings[i][1]);
        map.put(mappings[i][0], characters);
      }
    }
    if(s.contains(sub)){
      return true;
    }

    int l = 0, r = sub.length() - 1;
    while (r <= s.length() - 1) {
      String substring = s.substring(l, r + 1);
      for (int i = 0; i <= substring.length() - 1; i++) {
        if (substring.charAt(i) != sub.charAt(i)) {
          if (map.containsKey(sub.charAt(i))) {
            Set<Character> characters = map.get(sub.charAt(i));
            if (!characters.contains(substring.charAt(i))) {
              break;
            }
          }else {
            break;
          }
        }
        if (i == substring.length() - 1) {
          return true;
        }
      }
      l++;
      r++;
    }
    return false;
  }

  public static void main(String[] args) {
    String s = "fooleetbar", sub = "f00l";
    char[][] mappings = new char[][]{{'o', '0'}};
    boolean b = matchReplacement(s, sub, mappings);
    System.out.println(b);
  }
}
