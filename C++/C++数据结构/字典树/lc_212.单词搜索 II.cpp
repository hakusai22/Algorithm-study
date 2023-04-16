#include <bits/stdc++.h>

using namespace std;

/*
    -*- coding: utf-8 -*-
    @Author  : wheat
    @Time    : 2023/01/05 23:35
*/

int main() {

    return 0;
}

class Solution {
private:
    unordered_set<string> us;
    vector<vector<char>> board;
    vector<pair<int, int>> direction;
    int rows;
    int cols;
    bool visited[12][12];
    vector<string> ans;

public:
    vector<string> findWords(vector<vector<char>> &_board, vector<string> &words) {
        board = _board;
        direction = {{1,  0},
                     {0,  1},
                     {-1, 0},
                     {0,  -1}};
        rows = board.size();
        cols = board[0].size();
        for (string word: words) {
            us.insert(word);
        }
        string path;
        for (int r = 0; r < rows; r++) {
            for (int c = 0; c < cols; c++) {
                visited[r][c] = true;
                path += board[r][c];
                dfs(r, c, path);
                path = "";
                visited[r][c] = false;
            }
        }
        return ans;
    }

    void dfs(int row, int col, string &path) {
        if (path.length() > 10) return;
        if (us.count(path) == 1) {
            ans.push_back(path);
            us.erase(path);
        }
        for (pair<int, int> dir: direction) {
            int nr = row + dir.first;
            int nc = col + dir.second;
            if (0 <= nr && nr < rows && 0 <= nc && nc < cols) {
                if (!visited[nr][nc]) {
                    visited[nr][nc] = true;
                    path += board[nr][nc];
                    dfs(nr, nc, path);
                    path.erase(path.size() - 1);
                    visited[nr][nc] = false;
                }
            }
        }
    }
};

