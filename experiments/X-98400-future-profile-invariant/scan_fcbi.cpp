#include <algorithm>
#include <cmath>
#include <cstdint>
#include <iomanip>
#include <iostream>
#include <unordered_map>
#include <vector>

int main(int argc,char**argv){
    int N=100000000;
    if(argc>1) N=std::stoi(argv[1]);
    int M=(int)std::sqrt((long double)N);
    while((int64_t)(M+1)*(M+1)<=N) ++M;
    while((int64_t)M*M>N) --M;

    std::vector<int> vals;
    vals.reserve(2*M+10);
    for(int x=1;x<=M;++x) vals.push_back(x);
    for(int k=M;k>=1;--k) vals.push_back(N/k);
    std::sort(vals.begin(),vals.end());
    vals.erase(std::unique(vals.begin(),vals.end()),vals.end());
    std::unordered_map<int,int> idx;
    idx.reserve(vals.size()*2);
    for(int i=0;i<(int)vals.size();++i) idx[vals[i]]=i;

    std::vector<bool> isprime(N+1,true);
    isprime[0]=isprime[1]=false;
    for(int i=2;(int64_t)i*i<=N;++i) if(isprime[i])
        for(int64_t j=(int64_t)i*i;j<=N;j+=i) isprime[(size_t)j]=false;
    std::vector<int> primes;
    for(int p=3;p<=N;p+=2) if(isprime[p]) primes.push_back(p);

    auto base=[](int x){
        long double b=1.0L;
        if(x>=2) b-=2.5L/std::sqrt(2.0L);
        if(x>=4) b+=1.0L;
        if(x>=8) b-=0.5L/std::sqrt(8.0L);
        return b;
    };
    std::vector<long double> B(vals.size());
    for(size_t i=0;i<vals.size();++i) B[i]=base(vals[i]);

    long double min_slack=1e100L,max_boundary=-1e100L;
    int min_p=0,min_x=0,max_p=0,max_x=0;
    uint64_t updates=0;
    for(auto it=primes.rbegin();it!=primes.rend();++it){
        int p=*it;
        long double inv=1.0L/std::sqrt((long double)p);
        int first=(int)(std::lower_bound(vals.begin(),vals.end(),p)-vals.begin());
        for(int i=(int)vals.size()-1;i>=first;--i){
            int x=vals[i], y=x/p;
            auto jt=idx.find(y);
            if(jt==idx.end()) return 2;
            long double nb=B[i]-inv*B[jt->second];
            B[i]=nb;
            long double slack=1.0L-nb;
            if(x>1 && slack<min_slack){min_slack=slack;min_p=p;min_x=x;}
            if(x>1 && nb>max_boundary){max_boundary=nb;max_p=p;max_x=x;}
            ++updates;
        }
    }

    std::cout<<std::setprecision(21);
    std::cout<<"{\n";
    std::cout<<"  \"schema\": \"riemann.x98400.fcbi-diagnostic.v1\",\n";
    std::cout<<"  \"classification\": \"DIAGNOSTIC_ONLY\",\n";
    std::cout<<"  \"proves_all_scale\": false,\n";
    std::cout<<"  \"arithmetic\": \"long_double_not_directed\",\n";
    std::cout<<"  \"horizon\": "<<N<<",\n";
    std::cout<<"  \"sqrt_horizon\": "<<M<<",\n";
    std::cout<<"  \"quotient_coordinates\": "<<vals.size()<<",\n";
    std::cout<<"  \"odd_primes\": "<<primes.size()<<",\n";
    std::cout<<"  \"updates\": "<<updates<<",\n";
    std::cout<<"  \"minimum_slack\": \""<<min_slack<<"\",\n";
    std::cout<<"  \"minimum_witness\": {\"prime\": "<<min_p<<", \"coordinate\": "<<min_x<<"},\n";
    std::cout<<"  \"maximum_boundary\": \""<<max_boundary<<"\",\n";
    std::cout<<"  \"maximum_witness\": {\"prime\": "<<max_p<<", \"coordinate\": "<<max_x<<"},\n";
    std::cout<<"  \"final_root_boundary\": \""<<B[idx[N]]<<"\"\n";
    std::cout<<"}\n";
}
