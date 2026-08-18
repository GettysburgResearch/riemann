// Historical exploratory scanner reconstructed from the work transcript.
// WARNING: it generates all P61 divisors in signed long long and can overflow.
// Use scan_p61_bias_corrected.cpp for retained results.
#include <bits/stdc++.h>
using namespace std;
int main(int argc,char**argv){
    int N=argc>1?atoi(argv[1]):5000000;
    vector<int> primes={2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61};
    vector<pair<long long,int>> divs={{1,1}};
    for(int p:primes){int s=divs.size(); for(int i=0;i<s;i++) divs.push_back({divs[i].first*p,-divs[i].second});}
    sort(divs.begin(),divs.end());
    vector<int16_t> f(N+1,0), mcoef(N+1,0);
    auto q=[](int m)->int { if(m<2)return 0; if(m==2)return 15; if(m==3)return 6; if(m==4)return 3; return 6;};
    long long ops=0; int used=0;
    for(auto [d,mu]:divs){
        if(d>N/2) break; used++;
        int maxm=N/d;
        for(int mm=2;mm<=maxm;mm++){
            int n=(int)(d*mm); int qq=q(mm);
            f[n]+=mu*qq; mcoef[n]+=qq; ops++;
        }
    }
    cerr<<"N="<<N<<" divs_used="<<used<<" ops="<<ops<<"\n";
    vector<long double> Sf(N+1),Tf(N+1),Sm(N+1),Tm(N+1);
    for(int n=1;n<=N;n++){
        long double inv=1.0L/sqrtl((long double)n), ln=logl((long double)n);
        Sf[n]=Sf[n-1]+(long double)f[n]*inv;
        Tf[n]=Tf[n-1]+(long double)f[n]*inv*ln;
        Sm[n]=Sm[n-1]+(long double)mcoef[n]*inv;
        Tm[n]=Tm[n-1]+(long double)mcoef[n]*inv*ln;
    }
    long double L4=logl(4.0L), minr=1e100L,maxr=-1e100L;
    int argmin=-1,argmax=-1;
    for(int X=67;X<=N;X++){
        int M=X/4; long double lx=logl((long double)X);
        long double F=L4*Sf[M]+lx*(Sf[X]-Sf[M])-(Tf[X]-Tf[M]);
        long double MM=L4*Sm[M]+lx*(Sm[X]-Sm[M])-(Tm[X]-Tm[M]);
        long double r=F/MM;
        if(r<minr){minr=r;argmin=X;} if(r>maxr){maxr=r;argmax=X;}
    }
    cout<<setprecision(20)<<"minr "<<(double)minr<<" at "<<argmin<<"\n";
    cout<<"maxr "<<(double)maxr<<" at "<<argmax<<"\n";
}
