// DSE27: exact short-prefix Mertens recurrence; optional independent full sieve.
// No numerical zeta values and no floating arithmetic enter this executable.
#include <algorithm>
#include <cstdint>
#include <iostream>
#include <stdexcept>
#include <string>
#include <unordered_map>
#include <vector>
using I = std::int64_t;
using U = unsigned __int128;
static std::string dec(U x) {
    std::string s;
    do {s.push_back(char('0' + x % 10)); x /= 10;} while (x);
    std::reverse(s.begin(),s.end()); return s;
}
static std::vector<int> seed_mu(int n) {
    std::vector<int> a(n+1,1), primes;
    std::vector<bool> composite(n+1,false);
    a[0]=0;
    for(int i=2;i<=n;++i){
        if(!composite[i]){primes.push_back(i); a[i]=-1;}
        for(int p:primes){
            I v=I(i)*p; if(v>n)break;
            composite[v]=true;
            if(i%p==0){a[v]=0;break;}
            a[v]=-a[i];
        }
    }
    return a;
}
struct Recurrence {
    int y; std::vector<I> initial;
    std::unordered_map<I,I> cache;
    I blocks=0;
    explicit Recurrence(int cutoff):y(cutoff),initial(y+1,0){
        auto a=seed_mu(y);
        for(int k=1;k<=y;++k)initial[k]=initial[k-1]+a[k];
    }
    I value(I n){
        if(n<=y)return initial.at(n);
        auto it=cache.find(n); if(it!=cache.end())return it->second;
        I v=1;
        for(I lo=2;lo<=n;){
            I q=n/lo, hi=n/q;
            v-=(hi-lo+1)*value(q);lo=hi+1;++blocks;
        }
        cache.emplace(n,v);return v;
    }
};
int main(int argc,char** argv){
    try{
        bool full=argc==2 && std::string(argv[1])=="--full-check";
        if(argc>2 || (argc==2&&!full))throw std::runtime_error("bad arguments");
        int y,count;
        if(!(std::cin>>y>>count)||y<1||y>4095||count<1||count>40000)
            throw std::runtime_error("bounded integer input required");
        I B=I(y+1)*(y+1)-1;
        std::vector<I> points(count),values(count);
        for(int i=0;i<count;++i){
            if(!(std::cin>>points[i])||points[i]<1||points[i]>B||
               (i && points[i]<=points[i-1]))throw std::runtime_error("bad coordinate");
        }
        std::string extra;if(std::cin>>extra)throw std::runtime_error("trailing input");
        Recurrence rec(y);
        for(int i=0;i<count;++i)values[i]=rec.value(points[i]);
        // The following full-length source is used ONLY for an independent
        // finite comparison, never by the short-prefix recurrence above.
        U energy_lo=0,energy_hi=0;
        if(full){
            std::vector<signed char>a(B+1,1);a[0]=0;
            std::vector<bool> prime(B+1,true);prime[0]=prime[1]=false;
            for(I p=2;p<=B;++p)if(prime[p]){
                for(I k=p;k<=B;k+=p){a[k]=-a[k];if(k>p)prime[k]=false;}
                for(I k=p*p;k<=B;k+=p*p)a[k]=0;
            }
            I m=0;int j=0;const U scale=U(1)<<64;
            for(I k=1;k<=B;++k){
                m+=a[k];
                if(j<count && points[j]==k){
                    if(m!=values[j])throw std::runtime_error("independent sample mismatch");
                    ++j;
                }
                U numerator=U(m<0?-m:m)*U(m<0?-m:m)*scale;
                U denominator=U(k)*U(k+1);
                energy_lo+=numerator/denominator;
                energy_hi+=numerator/denominator+(numerator%denominator!=0);
            }
            if(j!=count)throw std::runtime_error("incomplete sample coverage");
        }
        std::cout<<"{\"samples\":[";
        for(int i=0;i<count;++i){if(i)std::cout<<',';std::cout<<values[i];}
        std::cout<<"],\"recurrence_arguments\":"<<rec.cache.size()
                 <<",\"quotient_blocks\":"<<rec.blocks
                 <<",\"full_sieve_checked\":"<<(full?"true":"false");
        if(full)std::cout<<",\"full_energy_bits\":64,\"full_energy_enclosure\":[\""
                         <<dec(energy_lo)<<"\",\""<<dec(energy_hi)<<"\"]";
        std::cout<<"}\n";
    }catch(const std::exception& e){std::cerr<<e.what()<<'\n';return 1;}
}
