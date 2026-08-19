#include <bits/stdc++.h>
using namespace std; using u128=unsigned __int128; using i128=__int128;
static string s128(i128 x){if(!x)return"0";bool neg=x<0;u128 y=neg?(u128)(-x):(u128)x;string s;while(y){s.push_back(char('0'+y%10));y/=10;}if(neg)s.push_back('-');reverse(s.begin(),s.end());return s;}
int main(int argc,char**argv){
 if(argc<3){cerr<<"usage L R\n";return 2;} uint32_t L=strtoul(argv[1],0,10),R=strtoul(argv[2],0,10); if(!L||L>R)return 2;
 constexpr uint32_t P=67; constexpr int K=40; const uint64_t S=1ULL<<K; const u128 S2=(u128)1<<(2*K);
 size_t B=(size_t)R-L+1; vector<uint32_t> rad(B,1); vector<int8_t> mu(B,1);
 uint32_t lim=sqrt((long double)R); vector<bool> comp(lim+1); vector<uint32_t> ps;
 for(uint32_t i=2;i<=lim;i++){if(!comp[i]){ps.push_back(i); if((uint64_t)i*i<=lim)for(uint64_t j=(uint64_t)i*i;j<=lim;j+=i)comp[j]=true;}}
 for(uint32_t p:ps){ if(p==2||p==P)continue; uint64_t st=((uint64_t)L+p-1)/p*p; for(uint64_t n=st;n<=R;n+=p){size_t i=n-L; mu[i]=-mu[i]; rad[i]*=p;} uint64_t pp=(uint64_t)p*p; st=((uint64_t)L+pp-1)/pp*pp; for(uint64_t n=st;n<=R;n+=pp)mu[n-L]=0; }
 i128 lo=0,hi=0,minlo=0,minhi=0; uint32_t minlo_n=L,minhi_n=L; bool have=false; uint64_t nonzero=0; long double approx=0,amin=1e100L; uint32_t an=L;
 const int c2[4]={2,-5,4,-1}; const int cp[3]={1,-2,1};
 for(uint32_t n=L;;n++){
   size_t i=(size_t)n-L; uint32_t m=n; unsigned raw_e2=__builtin_ctz(m); unsigned e2=raw_e2>3?4:raw_e2; m >>= raw_e2; unsigned ep=0; while(m%P==0){m/=P;ep++; if(ep>2)break;}
   int mur=mu[i]; if(mur && rad[i]!=m) mur=-mur;
   int b=0; if(n==1)b+=6; if(n==P)b-=6; if(e2<=3 && ep<=2) b += -3*c2[e2]*cp[ep]*mur;
   if(b){nonzero++; long double est=(long double)S/sqrt((long double)n); uint64_t q=(uint64_t)floor(est); auto ok=[&](uint64_t v){return (u128)v*v*n<=S2;}; while(q<S&&ok(q+1))q++; while(!ok(q))q--; if(b>0){lo+=(i128)b*q;hi+=(i128)b*(q+1);}else{lo+=(i128)b*(q+1);hi+=(i128)b*q;} approx+=(long double)b/sqrtl((long double)n);}
   if(n>=2){ if(!have||lo<minlo){minlo=lo;minlo_n=n;} if(!have||hi<minhi){minhi=hi;minhi_n=n;} if(!have||approx<amin){amin=approx;an=n;} have=true; }
   if(n==R)break;
 }
 cout<<setprecision(30)<<"L "<<L<<"\nR "<<R<<"\nscale "<<S<<"\nnonzero "<<nonzero<<"\n";
 cout<<"relative_min_lower_num "<<s128(minlo)<<"\nrelative_min_lower "<<(double)((long double)minlo/S)<<" at "<<minlo_n<<"\n";
 cout<<"relative_min_upper_num "<<s128(minhi)<<"\nrelative_min_upper "<<(double)((long double)minhi/S)<<" at "<<minhi_n<<"\n";
 cout<<"delta_lower_num "<<s128(lo)<<"\ndelta_upper_num "<<s128(hi)<<"\n";
 cout<<"approx_relative_min "<<(double)amin<<" at "<<an<<"\napprox_delta "<<(double)approx<<"\n";
}
