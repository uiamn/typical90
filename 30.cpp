#include <bits/stdc++.h>

std::vector<int> smallest_prime_factors(int n) {
    std::vector<int> spf(n+1);
    for(int i=0; i<=n; i++) spf[i] = i;

    for(int i=2; i*i <= n; i++) {
        if(spf[i] == i) {
            for(int j=i*i; j <= n; j += i) {
                if (spf[j] == j) spf[j] = i;
            }
        }
    }

    return spf;
}

int n_kind_of_prime_factors(int n, std::vector<int> &spf) {
    int n_kind = 0;
    while (n > 1) {
        n_kind++;
        auto p = spf[n];
        while (n % p == 0) n /= p;
    }

    return n_kind;
}

int main(){
    int N, K;
    std::cin >> N >> K;

    auto spf = smallest_prime_factors(N);

    int answer = 0;

    for(int i=2; i<=N; i++) {
        auto n_kind = n_kind_of_prime_factors(i, spf);
        if (n_kind >= K) answer += 1;
    }

    std::cout << answer << std::endl;
    return 0;
}
