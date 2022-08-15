#include <bits/stdc++.h>
#define ll long long int

std::vector<std::vector<ll>> NCK = {};

ll nCk(int n, int k) {
    if (k == 0) return 1;
    else if (n == k) return 1;
    else {
        if (NCK[n][k] != -1) return NCK[n][k];
        auto nck = nCk(n-1, k) + nCk(n-1, k-1);
        NCK[n][k] = nck;
        return nck;
    }
}


ll solve(int n, std::vector<ll> A, int K, ll P, std::vector<ll> subsums) {
    // 品物 1, ..., n から K 個選んで合計 P 円以下にする方法は何通りあるか返す
    if (P < 0) return 0;
    if (K == 0) return 1;
    if (n < K) return 0;

    if (n == 1) {
        if (A[1] <= P) return 1;
        else return 0;
    }

    if (K == 1) {
        ll ans = 0;
        for (int i=1; i<=n; i++) if (A[i] <= P) ans += 1;
        return ans;
    }

    if (n == K) {
        if (subsums[n] <= P) return 1;
        else return 0;
    }

    if (subsums[n] <= P) {
        return nCk(n, K);
    }

    return solve(n-1, A, K-1, P-A[n], subsums) + solve(n-1, A, K, P, subsums);
}

int main(){
    ll N, K, P;
    std::cin >> N >> K >> P;

    for(int i=0; i<N+1; i++) {
        std::vector<ll> po;
        for(int j=0; j<K+1; j++) po.push_back(-1);
        NCK.push_back(po);
    }

    ll a;
    std::vector<ll> A = {0};
    for(int i=0; i<N; i++) {
        std::cin >> a;
        A.push_back(a);
    }

    std::sort(A.begin(), A.end());
    ll subsum = 0;
    std::vector<ll> subsums = {};
    for(auto a: A) {
        subsum += a;
        subsums.push_back(subsum);
    }

    auto ans = solve(N, A, K, P, subsums);
    std::cout << ans << std::endl;

    return 0;
}
