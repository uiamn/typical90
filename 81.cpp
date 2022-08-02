#include <bits/stdc++.h>
#include <algorithm>

int main(){
    int N, K;
    std::cin >> N >> K;
    int d = K / 2;
    int size = 5002;

    std::vector<std::vector<int>> imos = {};
    for(int i=0; i<size; i++) {
        std::vector<int> row(size, 0);
        imos.push_back(row);
    }

    for(int i=0; i<N; i++) {
        int A, B;
        std::cin >> A >> B;
        int lx = std::max(A - d, 0);
        int ly = std::max(B - d, 0);
        int rx = std::min(A + d + 1 + (K%2), size-1);
        int ry = std::min(B + d + 1 + (K%2), size-1);

        imos[lx][ly] += 1;
        imos[rx][ry] += 1;
        imos[rx][ly] -= 1;
        imos[lx][ry] -= 1;
    }

    for(int i=0; i<size; i++) {
        for(int j=1; j<size; j++) {
            imos[i][j] += imos[i][j-1];
        }
    }

    for(int j=0; j<size; j++) {
        for(int i=1; i<size; i++) {
            imos[i][j] += imos[i-1][j];
        }
    }

    int ans = 0;

    for(int i=0; i<size-1; i++) for(int j=0; j<size-1; j++) {
        ans = std::max(ans, imos[i][j]);
    }

    std::cout << ans << std::endl;
}
