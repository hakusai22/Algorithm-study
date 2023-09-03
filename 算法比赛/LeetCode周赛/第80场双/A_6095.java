package 比赛.LeetCode周赛.第80场双;
class A_6095 {
  public boolean strongPasswordCheckerII(String password) {
    boolean a1 = false;
    boolean a2 = false;
    boolean a3 = false;
    boolean a4 = false;

    String a5 = "!@#$%^&*()-+";
    if (password.length() < 8) {
      return false;
    }
    char c1 = 1;
    for (char c : password.toCharArray()) {
      if (c >= 48 && c <= 57) {
        a1 = true;
      }
      if (c >= 65 && c <= 90) {
        a2 = true;
      }
      if (c >= 97 && c <= 122) {
        a3 = true;
      }
      if (a5.contains(String.valueOf(c))) {
        a4 = true;
      }
      if (c == c1) {
        return false;
      }
      c1 = c;
    }
    if (a1 && a2 && a3 && a4) {
      return true;
    }
    return false;
  }
}