#include "mpfr_min.h"
#include <algorithm>
#include <array>
#include <cassert>
#include <cmath>
#include <cstdint>
#include <cstdlib>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <limits>
#include <sstream>
#include <stdexcept>
#include <string>
#include <utility>
#include <vector>

using u128 = unsigned __int128;

static constexpr mpfr_prec_t PREC = 256;
static constexpr std::uint64_t FINITE_N = 1000000;
static constexpr std::uint64_t TAIL_N = 1000000;
static constexpr long double INF = std::numeric_limits<long double>::infinity();

struct I { long double lo, hi; };

static long double dn(long double x) { return std::nextafterl(x, -INF); }
static long double up(long double x) { return std::nextafterl(x, INF); }
static I exact(long double x) { return {x,x}; }
static I add(I a,I b){return {dn(a.lo+b.lo),up(a.hi+b.hi)};}
static I sub(I a,I b){return {dn(a.lo-b.hi),up(a.hi-b.lo)};}
static I mul(I a,I b){
  long double v[4]={a.lo*b.lo,a.lo*b.hi,a.hi*b.lo,a.hi*b.hi};
  long double lo=*std::min_element(v,v+4), hi=*std::max_element(v,v+4);
  return {dn(lo),up(hi)};
}
static I scale(I a,long double c){ return c>=0? I{dn(a.lo*c),up(a.hi*c)} : I{dn(a.hi*c),up(a.lo*c)}; }
static long double abs_up(I a){ return up(std::max(std::fabsl(a.lo),std::fabsl(a.hi))); }

struct M {
  mpfr_t x;
  M(){mpfr_init2(x,PREC);} ~M(){mpfr_clear(x);} M(const M&)=delete; M& operator=(const M&)=delete;
};

static std::string s128(u128 x){
  if(x==0)return "0"; std::string s; while(x){s.push_back(char('0'+x%10));x/=10;} std::reverse(s.begin(),s.end()); return s;
}
static void set128(mpfr_ptr z,u128 x,mpfr_rnd_t r){std::string s=s128(x); if(mpfr_set_str(z,s.c_str(),10,r))throw std::runtime_error("mpfr_set_str");}

struct Prim { I invsqrt, logv, log_over_sqrt, sqrtv; };

static Prim primitive_u128(u128 n){
  M x,sl,su,ilo,ihi,ll,lh,tlo,thi;
  set128(x.x,n,MPFR_RNDN);
  mpfr_sqrt(sl.x,x.x,MPFR_RNDD); mpfr_sqrt(su.x,x.x,MPFR_RNDU);
  mpfr_ui_div(ilo.x,1,su.x,MPFR_RNDD); mpfr_ui_div(ihi.x,1,sl.x,MPFR_RNDU);
  mpfr_log(ll.x,x.x,MPFR_RNDD); mpfr_log(lh.x,x.x,MPFR_RNDU);
  mpfr_div(tlo.x,ll.x,su.x,MPFR_RNDD); mpfr_div(thi.x,lh.x,sl.x,MPFR_RNDU);
  return {{mpfr_get_ld(ilo.x,MPFR_RNDD),mpfr_get_ld(ihi.x,MPFR_RNDU)},
          {mpfr_get_ld(ll.x,MPFR_RNDD),mpfr_get_ld(lh.x,MPFR_RNDU)},
          {mpfr_get_ld(tlo.x,MPFR_RNDD),mpfr_get_ld(thi.x,MPFR_RNDU)},
          {mpfr_get_ld(sl.x,MPFR_RNDD),mpfr_get_ld(su.x,MPFR_RNDU)}};
}
static Prim primitive_u64(std::uint64_t n){return primitive_u128((u128)n);}

static I rational_log(std::uint64_t num,std::uint64_t den){
  M x,y,ll,lh; mpfr_set_ui(x.x,num,MPFR_RNDN); mpfr_div_ui(y.x,x.x,den,MPFR_RNDN);
  mpfr_log(ll.x,y.x,MPFR_RNDD); mpfr_log(lh.x,y.x,MPFR_RNDU);
  return {mpfr_get_ld(ll.x,MPFR_RNDD),mpfr_get_ld(lh.x,MPFR_RNDU)};
}
static I rational_sqrt(std::uint64_t num,std::uint64_t den){
  M x,y,ll,lh; mpfr_set_ui(x.x,num,MPFR_RNDN); mpfr_div_ui(y.x,x.x,den,MPFR_RNDN);
  mpfr_sqrt(ll.x,y.x,MPFR_RNDD); mpfr_sqrt(lh.x,y.x,MPFR_RNDU);
  return {mpfr_get_ld(ll.x,MPFR_RNDD),mpfr_get_ld(lh.x,MPFR_RNDU)};
}
static I zeta_half(){
  M one,s,zl,zh; mpfr_set_ui(one.x,1,MPFR_RNDN); mpfr_div_ui(s.x,one.x,2,MPFR_RNDN);
  mpfr_zeta(zl.x,s.x,MPFR_RNDD); mpfr_zeta(zh.x,s.x,MPFR_RNDU);
  return {mpfr_get_ld(zl.x,MPFR_RNDD),mpfr_get_ld(zh.x,MPFR_RNDU)};
}

static int qstar(std::uint64_t n){if(n==2)return 15;if(n==3)return 6;if(n==4)return 3;if(n>=5)return 6;return 0;}
static std::array<int,18> primes(){return {2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61};}

static I compact_C0(const std::vector<Prim>& prim){
  I z=zeta_half(); I b=add(scale(z,6),exact(-7.5L)); b=add(b,scale(prim[2].invsqrt,9));
  return mul(b,prim[4].logv);
}

static void certify_compact_error(const std::vector<Prim>& prim,I C0,long double &sample_abs,long double &deriv_abs,long double &coverage){
  sample_abs=0;
  const std::uint64_t DEN=100;
  for(std::uint64_t num=2*DEN;num<=16*DEN;++num){
    I A=exact(0);
    for(std::uint64_t m=2;m<=15;++m){
      if(num < m*DEN) continue;
      I H;
      if(num >= 4*m*DEN) H=prim[4].logv; else H=rational_log(num,m*DEN);
      A=add(A,scale(mul(prim[m].invsqrt,H),qstar(m)));
    }
    I sq=rational_sqrt(num,DEN);
    I E=sub(sub(A,scale(sq,12)),C0);
    sample_abs=std::max(sample_abs,abs_up(E));
  }
  deriv_abs=0;
  for(std::uint64_t k=2;k<16;++k){
    I C=exact(0);
    for(std::uint64_t m=2;m<=k;++m){
      if(4*m<=k) continue;
      C=add(C,scale(prim[m].invsqrt,qstar(m)));
    }
    I c_over_y={dn(C.lo/(k+1.0L)),up(C.hi/k)};
    I six_over_sqrt={dn(6.0L/prim[k+1].sqrtv.hi),up(6.0L/prim[k].sqrtv.lo)};
    I D=sub(c_over_y,six_over_sqrt); deriv_abs=std::max(deriv_abs,abs_up(D));
  }
  coverage=up(sample_abs+deriv_abs/100.0L);
  if(!(coverage<5.0L))throw std::runtime_error("compact error bound failed");
}

static std::vector<long long> coeff(std::uint64_t N,bool signed_conv){
  std::vector<long long> c(N+1,0); for(std::uint64_t n=2;n<=N;++n)c[n]=qstar(n);
  for(int p:primes()){
    for(std::uint64_t k=N/p;k>=1;--k){
      c[p*k]+=(signed_conv?-1:1)*c[k];
      if(k==1)break;
    }
  }
  return c;
}

struct ScanResult {long double minlo=INF,minhi=INF;std::uint64_t arg=0;};
static ScanResult scan_sequence(const std::vector<long long>& b,const std::vector<Prim>& prim,I L4,std::uint64_t lo,std::uint64_t hi,bool require_positive=true){
  std::vector<I>S(hi+1),LS(hi+1);S[0]=LS[0]=exact(0);
  for(std::uint64_t n=1;n<=hi;++n){
    I w=scale(prim[n].invsqrt,(long double)b[n]); I wl=scale(prim[n].log_over_sqrt,(long double)b[n]);
    S[n]=add(S[n-1],w); LS[n]=add(LS[n-1],wl);
  }
  ScanResult r;
  for(std::uint64_t N=lo;N<=hi;++N){
    std::uint64_t k=N/4; I a=mul(L4,S[k]); I mid=mul(prim[N].logv,sub(S[N],S[k])); I tail=sub(LS[N],LS[k]); I d=sub(add(a,mid),tail);
    if(d.lo<r.minlo){r.minlo=d.lo;r.minhi=d.hi;r.arg=N;}
    if(require_positive && !(d.lo>0)){
      std::ostringstream os;os<<"finite interval failed at N="<<N<<" ["<<std::setprecision(20)<<d.lo<<","<<d.hi<<"]";throw std::runtime_error(os.str());
    }
  }
  return r;
}

struct Div {u128 d;int mu;};
static std::vector<Div> divisors(){std::vector<Div> v{{1,1}};for(int p:primes()){std::size_t n=v.size();for(std::size_t i=0;i<n;++i)v.push_back({v[i].d*(u128)p,-v[i].mu});}std::sort(v.begin(),v.end(),[](auto&a,auto&b){return a.d<b.d;});return v;}
static I ratio_i128(long a,u128 d){
  M ma,md,lo,hi;mpfr_set_si(ma.x,a,MPFR_RNDN);set128(md.x,d,MPFR_RNDN);mpfr_div(lo.x,ma.x,md.x,MPFR_RNDD);mpfr_div(hi.x,ma.x,md.x,MPFR_RNDU);return {mpfr_get_ld(lo.x,MPFR_RNDD),mpfr_get_ld(hi.x,MPFR_RNDU)};
}
struct TailState{I s1=exact(0),ss=exact(0),sa=exact(0);long double minlo=INF;u128 left=0,right=0;};
static long double tail_bound(I s1,I ss,I sa,u128 x){I sq=primitive_u128(x).sqrtv;I lead=scale(mul(sq,s1),12);long double v=dn(dn(lead.lo-20.0L*abs_up(ss))-5.0L*sa.hi);return v;}
static void add_div(TailState&st,const Div&dv,long a){Prim p=primitive_u128(dv.d);st.s1=add(st.s1,ratio_i128(a,dv.d));st.ss=add(st.ss,scale(p.invsqrt,(long double)a));st.sa=add(st.sa,scale(p.invsqrt,(long double)std::labs(a)));}
static void certify_tail(const std::vector<Div>&v,TailState&low,TailState&upst){
  for(std::size_t i=0;i<v.size();++i){
    add_div(low,v[i],42L*v[i].mu-1L);add_div(upst,v[i],1L-8L*v[i].mu);
    u128 l=2*v[i].d;u128 r=(i+1<v.size()?2*v[i+1].d:0);
    if(r && r<=TAIL_N)continue; if(l<TAIL_N)l=TAIL_N;
    auto check=[&](TailState&st){long double vl=tail_bound(st.s1,st.ss,st.sa,l);long double vv=vl;if(r){long double vr=tail_bound(st.s1,st.ss,st.sa,r);vv=std::min(vl,vr);}else{if(!(st.s1.lo>0))throw std::runtime_error("final S1 not positive");}
      if(vv<st.minlo){st.minlo=vv;st.left=l;st.right=r;} if(!(vv>0)){std::ostringstream os;os<<"tail failed ["<<s128(l)<<","<<(r?s128(r):"inf")<<") bound="<<std::setprecision(20)<<vv;throw std::runtime_error(os.str());}};
    check(low);check(upst);
  }
}

int main(int argc,char**argv){
  static_assert(std::numeric_limits<long double>::digits>=64,"long double precision too small");
  std::string out=(argc>1?argv[1]:"results/verification.json");
  std::cerr<<"MPFR "<<mpfr_get_version()<<" precision="<<PREC<<"\n";
  std::vector<Prim> prim(FINITE_N+1);prim[1]=primitive_u64(1);for(std::uint64_t n=2;n<=FINITE_N;++n)prim[n]=primitive_u64(n);
  I L4=prim[4].logv;I C0=compact_C0(prim);long double samp,deriv,cov;certify_compact_error(prim,C0,samp,deriv,cov);
  auto f=coeff(FINITE_N,true),m=coeff(FINITE_N,false);
  std::vector<long long> baseF(FINITE_N+1),baseDiff(FINITE_N+1),oldb(FINITE_N+1),lowb(FINITE_N+1),upb(FINITE_N+1);
  for(std::uint64_t n=0;n<=FINITE_N;++n){baseF[n]=f[n];baseDiff[n]=m[n]-f[n];oldb[n]=40*f[n]-m[n];lowb[n]=42*f[n]-m[n];upb[n]=m[n]-8*f[n];}
  ScanResult b1=scan_sequence(baseF,prim,L4,3,66);ScanResult b2=scan_sequence(baseDiff,prim,L4,5,66);ScanResult old=scan_sequence(oldb,prim,L4,67,FINITE_N,false);if(!(old.minhi<0))throw std::runtime_error("old 1/40 witness did not certify negative");ScanResult lo=scan_sequence(lowb,prim,L4,67,FINITE_N);ScanResult hi=scan_sequence(upb,prim,L4,67,FINITE_N);
  auto dv=divisors();TailState tl,tu;certify_tail(dv,tl,tu);
  std::ofstream os(out);if(!os)throw std::runtime_error("open output");os<<std::setprecision(20);
  os<<"{\n";
  os<<"  \"classification\": \"PASS_T97400_REPAIRED_P61_BIAS\",\n";
  os<<"  \"mpfr_version\": \""<<mpfr_get_version()<<"\",\n";
  os<<"  \"precision_bits\": "<<PREC<<",\n";
  os<<"  \"long_double_mantissa_bits\": "<<std::numeric_limits<long double>::digits<<",\n";
  os<<"  \"finite_end\": "<<FINITE_N<<",\n";
  os<<"  \"compact_C0_interval\": ["<<(double)C0.lo<<", "<<(double)C0.hi<<"],\n";
  os<<"  \"compact_error_sample_abs_upper\": "<<(double)samp<<",\n";
  os<<"  \"compact_error_derivative_upper\": "<<(double)deriv<<",\n";
  os<<"  \"compact_error_coverage_upper\": "<<(double)cov<<",\n";
  os<<"  \"base_F_min\": {\"N\": "<<b1.arg<<", \"lower\": "<<(double)b1.minlo<<"},\n";
  os<<"  \"base_M_minus_F_min\": {\"N\": "<<b2.arg<<", \"lower\": "<<(double)b2.minlo<<"},\n";
  os<<"  \"old_40F_minus_M_min\": {\"N\": "<<old.arg<<", \"lower\": "<<(double)old.minlo<<", \"upper\": "<<(double)old.minhi<<"},\n";
  os<<"  \"finite_42F_minus_M_min\": {\"N\": "<<lo.arg<<", \"lower\": "<<(double)lo.minlo<<", \"upper\": "<<(double)lo.minhi<<"},\n";
  os<<"  \"finite_M_minus_8F_min\": {\"N\": "<<hi.arg<<", \"lower\": "<<(double)hi.minlo<<", \"upper\": "<<(double)hi.minhi<<"},\n";
  os<<"  \"tail_42F_minus_M_min\": {\"left\": \""<<s128(tl.left)<<"\", \"right\": \""<<(tl.right?s128(tl.right):"inf")<<"\", \"lower\": "<<(double)tl.minlo<<"},\n";
  os<<"  \"tail_M_minus_8F_min\": {\"left\": \""<<s128(tu.left)<<"\", \"right\": \""<<(tu.right?s128(tu.right):"inf")<<"\", \"lower\": "<<(double)tu.minlo<<"},\n";
  os<<"  \"divisor_count\": "<<dv.size()<<",\n";
  os<<"  \"claimed_old_one_over_40\": false,\n";
  os<<"  \"repaired_one_over_42\": true,\n";
  os<<"  \"RH_established_by_replay\": false\n";
  os<<"}\n";
  std::cerr<<"PASS_T97400_REPAIRED_P61_BIAS\n";
  std::cerr<<"min finite low N="<<lo.arg<<" lower="<<lo.minlo<<" tail="<<tl.minlo<<"\n";
}
