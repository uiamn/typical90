#include <bits/stdc++.h>
#include <atcoder/scc>

#define ll long long int

int main() {
    int N, M;
    std::cin >> N >> M;

    atcoder::scc_graph g(N+1);

    for(int i=0; i<M; i++) {
        int a, b;
        std::cin >> a >> b;
        g.add_edge(a, b);
    }

    auto components = g.scc();

    ll ans = 0;
    for(auto c: components) {
        auto s = c.size();
        ans += s * (s-1) / 2;
    }

    printf("%lld\n", ans);
}
