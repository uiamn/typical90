#include<stdio.h>
#include<vector>
#include<string>
#include <iostream>

bool is_valid(std::string s, int len) {
    int open_cnt = 0;
    int close_cnt = 0;

    for(int i=0; i<len; i++) {
        if (s[i] == '(') open_cnt++;
        else close_cnt++;

        if (close_cnt > open_cnt) return false;
    }

    return open_cnt == close_cnt;
}

int main() {
    int N;
    scanf("%d", &N);

    std::vector<std::string> res = {""};
    if(N%2==1) return 0;

    for(int i=0; i<N; i++) {
        std::vector<std::string> tmp = {};
        for(auto s: res) {
            tmp.push_back(s+"(");
            tmp.push_back(s+")");
        }
        res = tmp;
    }

    for(auto a: res) if(is_valid(a, N)) std::cout << a << std::endl;

    return 0;
}
