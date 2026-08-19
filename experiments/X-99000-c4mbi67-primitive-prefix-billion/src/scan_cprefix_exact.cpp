#include <bits/stdc++.h>
using namespace std;
using u128 = unsigned __int128;
using i128 = __int128;

static string to_string_i128(i128 x){
    if(x==0) return "0";
    bool neg=x<0; u128 y=neg? (u128)(-x):(u128)x;
    string s; while(y){s.push_back('0'+(int)(y%10)); y/=10;} if(neg)s.push_back('-'); reverse(s.begin(),s.end()); return s;
}

int main(int argc,char**argv){
 uint32_t N=100000000; if(argc>1) N=strtoul(argv[1],nullptr,10);
 constexpr int K=40; const uint64_t SCALE=1ULL<<K; const u128 SCALE2=(u128)1<<(2*K);
 vector<uint16_t> lp((size_t)N+1,0);
 vector<int8_t> mu((size_t)N+1,0); mu[1]=1;
 vector<uint32_t> primes; primes.reserve((size_t)(N/log((double)max<uint32_t>(N,3))*1.1));
 for(uint32_t i=2;i<=N;++i){
   if(lp[i]==0){ primes.push_back(i); mu[i]=-1; lp[i]=(i<=65534? (uint16_t)i : (uint16_t)65535); }
   uint16_t lim=lp[i];
   for(uint32_t p:primes){
     if(p>lim) break;
     uint64_t v=(uint64_t)i*p; if(v>N) break;
     lp[(size_t)v]=(uint16_t)p;
     if(p==lim) mu[(size_t)v]=0; else mu[(size_t)v]=(int8_t)-mu[i];
   }
 }
 lp.clear(); lp.shrink_to_fit(); primes.clear(); primes.shrink_to_fit();
 i128 lo=0,hi=0,minlo=0,minhi=0; uint32_t minlo_n=1,minhi_n=1; uint64_t nonzero=0; long double approx=0, approx_min=1e100L; uint32_t approx_n=0;
 for(uint32_t n=1;n<=N;++n){
   int aa=(n==1?6:0)-6*(int)mu[n];
   if((n&1)==0) aa+=9*(int)mu[n/2];
   if(n%4==0) aa-=3*(int)mu[n/4];
   if(aa){
     ++nonzero;
     long double est=(long double)SCALE/sqrt((long double)n);
     uint64_t q=(uint64_t)floor(est);
     auto ok_le=[&](uint64_t v)->bool { return (u128)v*(u128)v*(u128)n <= SCALE2; };
     while(q < SCALE && ok_le(q+1)) ++q;
     while(!ok_le(q)) --q;
     if(aa>0){lo+=(i128)aa*(i128)q; hi+=(i128)aa*(i128)(q+1);} 
     else {lo+=(i128)aa*(i128)(q+1); hi+=(i128)aa*(i128)q;}
     approx+=(long double)aa/sqrtl((long double)n);
   }
   if(n>=2){
     if(n==2 || lo<minlo){minlo=lo;minlo_n=n;}
     if(n==2 || hi<minhi){minhi=hi;minhi_n=n;}
     if(approx<approx_min){approx_min=approx;approx_n=n;}
   }
 }
 long double minlo_d=(long double)minlo/(long double)SCALE;
 long double minhi_d=(long double)minhi/(long double)SCALE;
 long double final_lo=(long double)lo/(long double)SCALE;
 long double final_hi=(long double)hi/(long double)SCALE;
 cout<<setprecision(30);
 cout<<"N "<<N<<"\nK "<<K<<"\nscale "<<SCALE<<"\nnonzero "<<nonzero<<"\n";
 cout<<"min_lower_num "<<to_string_i128(minlo)<<"\nmin_lower "<<(double)minlo_d<<" at "<<minlo_n<<"\n";
 cout<<"min_upper_num "<<to_string_i128(minhi)<<"\nmin_upper "<<(double)minhi_d<<" at "<<minhi_n<<"\n";
 cout<<"approx_min "<<(double)approx_min<<" at "<<approx_n<<"\n";
 cout<<"final_lower_num "<<to_string_i128(lo)<<"\nfinal_upper_num "<<to_string_i128(hi)<<"\n";
 cout<<"final_interval ["<<(double)final_lo<<", "<<(double)final_hi<<"]\n";
 cout<<"PASS "<<(minlo>0?"YES":"NO")<<"\n";
}
