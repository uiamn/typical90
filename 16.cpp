#include <bits/stdc++.h>
#define ll long long int

int main(){
    ll N, A, B, C;
    std::cin >> N;
    std::cin >> A >> B >> C;

    ll answer = 10000;

    ll max_val = std::max({A, B, C});
    ll min_val = std::min({A, B, C});
    ll mid_val = A + B + C - max_val - min_val;

    for(int i=0; i<answer; i++) {
        for(int j=0; j<(answer - i); j++) {
            auto rest = N - max_val*i - mid_val*j;
            if(rest >= 0 && rest % min_val == 0) {
                answer = std::min(answer, i + j + rest / min_val);
            }
        }
    }

    std::cout << answer << std::endl;
}
