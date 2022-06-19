#include <bits/stdc++.h>

int main(){
    int N, P, Q;
    std::cin >> N >> P >> Q;

    std::vector<int> vec(N);
    for(int i=0; i<N; i++) {
        int A;
        std::cin >> A;
        vec[i] = A % P;
    }

    long long int ans = 0;
    for(int i=0; i<N-4; i++)
        for(int j=i+1; j<N-3; j++)
            for(int k=j+1; k<N-2; k++)
                for(int l=k+1; l<N-1; l++)
                    for(int m=l+1; m<N; m++) {
                        long long int p = 1;
                        p *= vec[i];
                        p *= vec[j];
                        p %= P;
                        p *= vec[k];
                        p %= P;
                        p *= vec[l];
                        p %= P;
                        p *= vec[m];
                        if(p % P == Q) ans += 1;
                    }

    std::cout << ans << std::endl;
}
