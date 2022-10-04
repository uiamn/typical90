#include <bits/stdc++.h>

std::vector<int> cache(400*400, 0);

int cost(int h, int t, std::vector<int> &A) {
    if (cache[t*400+h]) return cache[t*400+h];


    if (t >= A.size() || h >= A.size() - 1) return 0;
    else if (h >= t) return 0;
    else if (t-h == 1) return std::abs(A[t] - A[h]);

    auto result = std::abs(A[h+1] - A[h]) + cost(h+2, t, A);

    for(int i=3; h+i <= t; i+=2) {
        result = std::min(result, std::abs(A[h] - A[h+i]) + cost(h+1, h+i-1, A) + cost(h+i+1, t, A));
    }

    cache[t*400+h] = result;
    return result;
}


int main(){
    int N;
    std::cin >> N;

    std::vector<int> A(2*N, 0);

    for(int i=0; i<2*N; i++) std::cin >> A[i];

    printf("%d\n", cost(0, 2*N-1, A));

    return 0;
}
