#include <bits/stdc++.h>
#include <algorithm>

int main(){
    int N;
    std::cin >> N;

    // imos 法といふらしい
    std::vector<std::vector<int>> imos = {};
    for(int i=0; i<1001; i++) {
        std::vector<int> row(1001, 0);
        imos.push_back(row);
    }

    for(int i=0; i<N; i++) {
        int lx, ly, rx, ry;
        std::cin >> lx >> ly >> rx >> ry;
        imos[lx][ly] += 1;
        imos[rx][ry] += 1;
        imos[rx][ly] -= 1;
        imos[lx][ry] -= 1;
    }

    for(int i=0; i<1001; i++) {
        for(int j=1; j<1001; j++) {
            imos[i][j] += imos[i][j-1];
        }
    }

    for(int j=0; j<1001; j++) {
        for(int i=1; i<1001; i++) {
            imos[i][j] += imos[i-1][j];
        }
    }

    std::vector<int> n_papers(N+1, 0);
    for(int i=0; i<1000; i++) for(int j=0; j<1000; j++) {
        n_papers[imos[i][j]]++;
    }

    for(int n=1; n<=N; n++) std::cout << n_papers[n] << std::endl;
}
