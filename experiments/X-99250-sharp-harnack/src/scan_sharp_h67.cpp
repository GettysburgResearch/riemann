#include <bits/stdc++.h>
using namespace std; using u128=unsigned __int128; using i128=__int128;
static string s128(i128 x){if(!x)return"0";bool neg=x<0;u128 y=neg?(u128)(-x):(u128)x;string s;while(y){s.push_back(char('0'+y%10));y/=10;}if(neg)s.push_back('-');reverse(s.begin(),s.end());return s;}
int main(int argc,char**argv){
 if(argc<2){cerr<<"usage: scan_sharp_h67 N [block_size]\n";return 2;}
 uint64_t N=strtoull(argv[1],0,10); uint64_t BS=argc>2?strtoull(argv[2],0,10):2000000;
 if(N<67 || N>200000000ULL || BS==0){cerr<<"require 67 <= N <= 200000000 and block_size > 0\n";return 2;}
 constexpr uint32_t P=67; constexpr int K=50; const uint64_t S=1ULL<<K; const u128 S2=(u128)S*S;
 uint64_t lim=sqrt((long double)N); vector<bool> comp(lim+1); vector<uint32_t> ps;
 for(uint32_t i=2;i<=lim;i++){if(!comp[i]){ps.push_back(i); if((uint64_t)i*i<=lim)for(uint64_t j=(uint64_t)i*i;j<=lim;j+=i)comp[j]=true;}}
 i128 Alo=0,Ahi=0,Blo=0,Bhi=0; i128 global_lo=0, global_hi=0; uint64_t min_n=0; char min_side='L'; bool have=false; long double Aap=0,Bap=0, minap=1e100; uint64_t minap_n=0; char minap_side='L'; uint64_t nonzero=0;
 auto eval=[&](uint64_t xnum,uint64_t n,char side){ // x=xnum integer endpoint with current active coeffs
   long double rest=(long double)S*sqrtl((long double)xnum); if(rest>(long double)numeric_limits<uint64_t>::max()-4){cerr<<"scaled root overflow\n";exit(3);} uint64_t root=(uint64_t)floor(rest); auto rok=[&](uint64_t v){return (u128)v*v<=S2*(u128)xnum;}; while(rok(root+1))root++; while(!rok(root))root--; i128 rl=(i128)root, rh=(i128)root+1;
   i128 plo,phi;
   if(Alo>=0){plo=Alo*rl;phi=Ahi*rh;} else if(Ahi<=0){plo=Alo*rh;phi=Ahi*rl;} else {plo=Alo*rh;phi=Ahi*rh;}
   i128 hlo=4*plo-3*Bhi*(i128)S; i128 hhi=4*phi-3*Blo*(i128)S;
   if(!have||hlo<global_lo){global_lo=hlo;global_hi=hhi;min_n=n;min_side=side;have=true;}
   long double hv=4*sqrtl((long double)xnum)*Aap-3*Bap;
   if(hv<minap){minap=hv;minap_n=n;minap_side=side;}
 };
 for(uint64_t L=1;L<=N;L+=BS){uint64_t R=min(N,L+BS-1);size_t B=R-L+1;vector<uint64_t> rad(B,1);vector<int8_t> mu(B,1);
   for(uint32_t p:ps){if(p==P)continue; uint64_t st=(L+p-1)/p*p; for(uint64_t n=st;n<=R;n+=p){size_t i=n-L;mu[i]=-mu[i];rad[i]*=p;} uint64_t pp=(uint64_t)p*p; if(pp>R)continue; st=(L+pp-1)/pp*pp; for(uint64_t n=st;n<=R;n+=pp)mu[n-L]=0;}
   for(uint64_t n=L;n<=R;n++){size_t i=n-L;uint64_t m=n;int f=0;while(m%P==0){m/=P;f++;if(f>2)break;}int mur=mu[i];if(mur&&rad[i]!=m)mur=-mur;int c=f==0?1:f==1?-2:f==2?1:0;int b=c*mur;
      if(b){nonzero++; uint64_t qa=S/n, ca=qa+(S%n!=0); u128 target=S2; long double est=(long double)S/sqrtl((long double)n);uint64_t qb=(uint64_t)floor(est);auto ok=[&](uint64_t v){return (u128)v*v*n<=target;};while(ok(qb+1))qb++;while(!ok(qb))qb--;uint64_t cb=qb+1;
        if(b>0){Alo+=(i128)b*qa;Ahi+=(i128)b*ca;Blo+=(i128)b*qb;Bhi+=(i128)b*cb;} else {Alo+=(i128)b*ca;Ahi+=(i128)b*qa;Blo+=(i128)b*cb;Bhi+=(i128)b*qb;}
        Aap+=(long double)b/n;Bap+=(long double)b/sqrtl((long double)n);
      }
      if(n>=67){eval(n,n,'L');eval(n+1,n,'R');}
   }
   cerr<<"block "<<L<<"-"<<R<<" min~"<<(double)minap<<" at "<<minap_n<<minap_side<<"\n";
 }
 cout<<setprecision(18);
 cout<<"classification PASS_X99250_SHARP_H67_DIRECTED_SCAN\n";
 cout<<"range_start 67\nrange_end_exclusive "<<(N+1)<<"\n";
 cout<<"N "<<N<<" scale "<<S<<" scale_squared "<<s128((i128)S*(i128)S)<<" nonzero "<<nonzero<<"\n";
 cout<<"min_lower_num "<<s128(global_lo)<<"\nmin_upper_num "<<s128(global_hi)<<"\n";
 long double den=(long double)S*(long double)S;
 cout<<"min_lower "<<(double)((long double)global_lo/den)<<"\nmin_upper "<<(double)((long double)global_hi/den)<<"\n";
 cout<<"minimum_cell "<<min_n<<" minimum_side "<<(min_side=='L'?"LEFT":"RIGHT_LIMIT")<<"\n";
 cout<<"approx_minimum "<<(double)minap<<" approx_cell "<<minap_n<<" approx_side "<<(minap_side=='L'?"LEFT":"RIGHT_LIMIT")<<"\n";
 cout<<"Alo "<<s128(Alo)<<" Ahi "<<s128(Ahi)<<" Blo "<<s128(Blo)<<" Bhi "<<s128(Bhi)<<"\n";
}
