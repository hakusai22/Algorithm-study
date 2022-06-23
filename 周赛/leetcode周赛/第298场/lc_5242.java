class Solution {
	public String greatestLetter(String s) {
		for (char c = 'Z'; c >= 'A'; c--) {
			if (s.indexOf(c) >= 0 && s.indexOf(c - 'A' + 'a') >= 0) {
				return "" + c;
			}
		}
		return "";
	}
}