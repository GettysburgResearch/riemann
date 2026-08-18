#include "mpfr_min.h"
#include <zlib.h>
#include <algorithm>
#include <array>
#include <cassert>
#include <cmath>
#include <cstdint>
#include <cstdio>
#include <cstdlib>
#include <filesystem>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <map>
#include <memory>
#include <numeric>
#include <set>
#include <sstream>
#include <stdexcept>
#include <string>
#include <tuple>
#include <utility>
#include <vector>

using u128=unsigned __int128;
namespace fs=std::filesystem;
static constexpr mpfr_prec_t PREC=320;

struct IV {
  mpfr_t lo,hi;
  IV(){mpfr_init2(lo,PREC);mpfr_init2(hi,PREC);mpfr_set_ui(lo,0,MPFR_RNDN);mpfr_set_ui(hi,0,MPFR_RNDN);}
  IV(const IV&o){mpfr_init2(lo,PREC);mpfr_init2(hi,PREC);mpfr_set(lo,o.lo,MPFR_RNDN);mpfr_set(hi,o.hi,MPFR_RNDN);}
  IV(IV&&o) noexcept {mpfr_init2(lo,PREC);mpfr_init2(hi,PREC);mpfr_swap(lo,o.lo);mpfr_swap(hi,o.hi);}
  IV& operator=(const IV&o){if(this!=&o){mpfr_set(lo,o.lo,MPFR_RNDN);mpfr_set(hi,o.hi,MPFR_RNDN);}return *this;}
  IV& operator=(IV&&o) noexcept {if(this!=&o){mpfr_swap(lo,o.lo);mpfr_swap(hi,o.hi);}return *this;}
  ~IV(){mpfr_clear(lo);mpfr_clear(hi);}
};

static IV from_ui(unsigned long x){IV r;mpfr_set_ui(r.lo,x,MPFR_RNDN);mpfr_set_ui(r.hi,x,MPFR_RNDN);return r;}
static IV from_si(long x){IV r;mpfr_set_si(r.lo,x,MPFR_RNDN);mpfr_set_si(r.hi,x,MPFR_RNDN);return r;}
static std::string u128s(u128 x){if(x==0)return "0";std::string s;while(x){s.push_back(char('0'+x%10));x/=10;}std::reverse(s.begin(),s.end());return s;}
static IV from_u128(u128 x){IV r;std::string s=u128s(x);if(mpfr_set_str(r.lo,s.c_str(),10,MPFR_RNDN)||mpfr_set_str(r.hi,s.c_str(),10,MPFR_RNDN))throw std::runtime_error("mpfr_set_str");return r;}
static IV add(const IV&a,const IV&b){IV r;mpfr_add(r.lo,a.lo,b.lo,MPFR_RNDD);mpfr_add(r.hi,a.hi,b.hi,MPFR_RNDU);return r;}
static IV sub(const IV&a,const IV&b){IV r;mpfr_sub(r.lo,a.lo,b.hi,MPFR_RNDD);mpfr_sub(r.hi,a.hi,b.lo,MPFR_RNDU);return r;}
static IV neg(const IV&a){IV r;mpfr_neg(r.lo,a.hi,MPFR_RNDD);mpfr_neg(r.hi,a.lo,MPFR_RNDU);return r;}
static void min_set(mpfr_ptr z,mpfr_srcptr x){if(mpfr_cmp(x,z)<0)mpfr_set(z,x,MPFR_RNDN);} 
static void max_set(mpfr_ptr z,mpfr_srcptr x){if(mpfr_cmp(x,z)>0)mpfr_set(z,x,MPFR_RNDN);} 
static IV mul(const IV&a,const IV&b){
 IV r;mpfr_t t;mpfr_init2(t,PREC);
 mpfr_mul(r.lo,a.lo,b.lo,MPFR_RNDD);
 mpfr_mul(t,a.lo,b.hi,MPFR_RNDD);min_set(r.lo,t);
 mpfr_mul(t,a.hi,b.lo,MPFR_RNDD);min_set(r.lo,t);
 mpfr_mul(t,a.hi,b.hi,MPFR_RNDD);min_set(r.lo,t);
 mpfr_mul(r.hi,a.lo,b.lo,MPFR_RNDU);
 mpfr_mul(t,a.lo,b.hi,MPFR_RNDU);max_set(r.hi,t);
 mpfr_mul(t,a.hi,b.lo,MPFR_RNDU);max_set(r.hi,t);
 mpfr_mul(t,a.hi,b.hi,MPFR_RNDU);max_set(r.hi,t);
 mpfr_clear(t);return r;
}
static IV inv(const IV&a){if(mpfr_cmp_ui(a.lo,0)<=0)throw std::runtime_error("nonpositive inverse");IV one=from_ui(1),r;mpfr_div(r.lo,one.lo,a.hi,MPFR_RNDD);mpfr_div(r.hi,one.hi,a.lo,MPFR_RNDU);return r;}
static IV divi(const IV&a,const IV&b){return mul(a,inv(b));}
static IV sqrt_i(const IV&a){if(mpfr_cmp_ui(a.lo,0)<0)throw std::runtime_error("negative sqrt");IV r;mpfr_sqrt(r.lo,a.lo,MPFR_RNDD);mpfr_sqrt(r.hi,a.hi,MPFR_RNDU);return r;}
static IV log_i(const IV&a){if(mpfr_cmp_ui(a.lo,0)<=0)throw std::runtime_error("nonpositive log");IV r;mpfr_log(r.lo,a.lo,MPFR_RNDD);mpfr_log(r.hi,a.hi,MPFR_RNDU);return r;}
static IV scale_si(const IV&a,long c){if(c>=0){IV r;mpfr_mul_ui(r.lo,a.lo,(unsigned long)c,MPFR_RNDD);mpfr_mul_ui(r.hi,a.hi,(unsigned long)c,MPFR_RNDU);return r;}return neg(scale_si(a,-c));}
static IV rat(long n,unsigned long d){IV r=from_si(n);IV den=from_ui(d);return divi(r,den);}
static bool positive(const IV&a){return mpfr_cmp_ui(a.lo,0)>0;}
static bool negative(const IV&a){return mpfr_cmp_ui(a.hi,0)<0;}
static double mid_d(const IV&a){return 0.5*(mpfr_get_d(a.lo,MPFR_RNDN)+mpfr_get_d(a.hi,MPFR_RNDN));}
static std::string fmt(mpfr_srcptr x,int digits=66){std::vector<char>b((size_t)digits+64);std::string spec="%."+std::to_string(digits)+"Rg";mpfr_snprintf(b.data(),b.size(),spec.c_str(),x);return b.data();}
static std::string lo_s(const IV&a,int d=66){return fmt(a.lo,d);}static std::string hi_s(const IV&a,int d=66){return fmt(a.hi,d);}
static IV log4_i(){IV r;mpfr_const_log2(r.lo,MPFR_RNDD);mpfr_mul_ui(r.lo,r.lo,2,MPFR_RNDD);mpfr_const_log2(r.hi,MPFR_RNDU);mpfr_mul_ui(r.hi,r.hi,2,MPFR_RNDU);return r;}
static IV zeta_half_i(){IV h=rat(1,2),r;mpfr_zeta(r.lo,h.lo,MPFR_RNDD);mpfr_zeta(r.hi,h.hi,MPFR_RNDU);return r;}

static std::vector<int> primes_upto(int B){std::vector<int>p;for(int n=2;n<=B;n++){bool ok=true;for(int q:p){if(1LL*q*q>n)break;if(n%q==0){ok=false;break;}}if(ok)p.push_back(n);}return p;}
static int muP(int64_t t,const std::vector<int>&ps){if(t<1)return 0;int s=1;for(int p:ps){if(t%p==0){t/=p;s=-s;if(t%p==0)return 0;}}return t==1?s:0;}
static int coeff_a(int n,const std::vector<int>&ps){bool cop=true;int om=0;for(int p:ps)if(n%p==0){cop=false;om++;}(void)om;int a=6*(cop?1:0)-6*muP(n,ps);if(n%2==0)a+=9*muP(n/2,ps);if(n%4==0)a-=3*muP(n/4,ps);return a;}
static int coeff_b(int n,const std::vector<int>&ps){int om=0;for(int p:ps)if(n%p==0)om++;auto ind=[&](int64_t t){return muP(t,ps)!=0?1:0;};int b=6*(1<<om)-6*ind(n);if(n%2==0)b+=9*ind(n/2);if(n%4==0)b-=3*ind(n/4);return b;}

struct Prefix {
 int N;std::vector<IV> Sa,Ta,Sb,Tb,logs;
 Prefix(int B,int n):N(n),Sa(n+1),Ta(n+1),Sb(n+1),Tb(n+1),logs(n+1){
  auto ps=primes_upto(B);logs[1]=from_ui(0);
  for(int k=1;k<=n;k++){
   IV x=from_ui(k),sq=sqrt_i(x),iw=inv(sq);if(k>1)logs[k]=log_i(x);
   int ca=coeff_a(k,ps),cb=coeff_b(k,ps);if(cb<ca)throw std::runtime_error("b-a coefficient negative");IV wa=scale_si(iw,ca), wb=scale_si(iw,cb);
   Sa[k]=add(Sa[k-1],wa);Sb[k]=add(Sb[k-1],wb);
   Ta[k]=add(Ta[k-1],mul(wa,logs[k]));Tb[k]=add(Tb[k-1],mul(wb,logs[k]));
  }
 }
 std::pair<IV,IV> eval(int x,const IV&log4)const{
  if(x<=2)return {from_ui(0),from_ui(0)};
  int q=x/4;IV lx=logs[x];
  IV F=add(mul(log4,Sa[q]),sub(mul(lx,sub(Sa[x],Sa[q])),sub(Ta[x],Ta[q])));
  IV M=add(mul(log4,Sb[q]),sub(mul(lx,sub(Sb[x],Sb[q])),sub(Tb[x],Tb[q])));
  return {F,M};
 }
};

static gzFile gzopen_checked(const fs::path&p){gzFile f=gzopen(p.string().c_str(),"wb1");if(!f)throw std::runtime_error("gzopen "+p.string());return f;}
static void gzline(gzFile f,const std::string&s){if(gzwrite(f,s.data(),(unsigned)s.size())!=(int)s.size())throw std::runtime_error("gzwrite");}

struct CaseSummary {
 int B,start,compact_end,min_x,max_x;size_t base_cells,compact_cells,tail_events;
 IV min_ratio,max_ratio,Fmin,Mmin,diff40,diff42,min_left_derivative,min_right_derivative,phi_min,phi_max,tail_lower_min,tail_upper_min;
 std::string phi_min_x,phi_max_x,tail_lower_x,tail_upper_x;
};

static void upd_add(IV&a,const IV&b){a=add(a,b);}static void upd_sub(IV&a,const IV&b){a=sub(a,b);}
static CaseSummary compact_case(int B,int start,int end,const fs::path&out,const IV&log4){
 auto ps=primes_upto(B);CaseSummary S{};S.B=B;S.start=start;S.compact_end=end;S.min_x=(B==61?184:104);S.max_x=(B==61?67:41);S.base_cells=start-1;S.compact_cells=end-start;
 IV low=(B==61?rat(1199,50000):rat(17,500)),upper=(B==61?rat(9,200):rat(8,125));IV sepmin=(B==61?rat(2399,100000):rat(427,12500));IV sepmax=rat(63,1000);
 gzFile base=gzopen_checked(out/("base_p"+std::to_string(B)+".tsv.gz"));gzline(base,"cell\tleft_F_lo\tleft_F_hi\tright_F_lo\tright_F_hi\tleft_MminusF_lo\tleft_MminusF_hi\tright_MminusF_lo\tright_MminusF_hi\n");
 gzFile comp=gzopen_checked(out/("compact_p"+std::to_string(B)+".tsv.gz"));gzline(comp,"cell\tleft_ratio_lo\tleft_ratio_hi\tright_ratio_lo\tright_ratio_hi\n");
 IV Sa,Ta,Ca,Sb,Tb,Cb;IV prevF,prevM,prevR;bool have=false;
 for(int x=1;x<=end;x++){
  IV xx=from_ui(x),lx=(x==1?from_ui(0):log_i(xx)),iw=inv(sqrt_i(xx));int ca=coeff_a(x,ps),cb=coeff_b(x,ps);if(cb<ca)throw std::runtime_error("b-a coefficient negative");IV wa=scale_si(iw,ca),wb=scale_si(iw,cb);upd_add(Sa,wa);upd_add(Sb,wb);upd_add(Ta,mul(wa,lx));upd_add(Tb,mul(wb,lx));
  if(x%4==0){int n=x/4;IV iwn=scale_si(iw,2),ln=sub(lx,log4);IV za=scale_si(iwn,coeff_a(n,ps)),zb=scale_si(iwn,coeff_b(n,ps));upd_sub(Sa,za);upd_sub(Sb,zb);upd_sub(Ta,mul(za,ln));upd_sub(Tb,mul(zb,ln));upd_add(Ca,za);upd_add(Cb,zb);}
  IV F=add(sub(mul(Sa,lx),Ta),mul(Ca,log4)),M=add(sub(mul(Sb,lx),Tb),mul(Cb,log4));if(x<=2){F=from_ui(0);M=from_ui(0);}IV f0=sub(mul(Ca,log4),Ta),m0=sub(mul(Cb,log4),Tb),deriv=sub(mul(Sa,m0),mul(Sb,f0));if(x==S.min_x-1){S.min_left_derivative=deriv;if(!negative(deriv))throw std::runtime_error("minimum left-cell derivative");}if(x==S.min_x){S.min_right_derivative=deriv;if(!positive(deriv))throw std::runtime_error("minimum right-cell derivative");}IV R;if(x>=start){if(!positive(M))throw std::runtime_error("M positive");R=divi(F,M);if(!positive(sub(F,mul(low,M)))||!positive(sub(mul(upper,M),F)))throw std::runtime_error("compact rational bounds");if(x!=S.min_x&&!positive(sub(F,mul(sepmin,M))))throw std::runtime_error("unique min separator");if(B==37&&x!=S.max_x&&!positive(sub(mul(sepmax,M),F)))throw std::runtime_error("unique max separator");}
  if(x==S.min_x){S.Fmin=F;S.Mmin=M;S.min_ratio=R;if(B==61){S.diff40=sub(F,mul(rat(1,40),M));S.diff42=sub(F,mul(rat(1,42),M));if(!negative(S.diff40)||!positive(S.diff42))throw std::runtime_error("x184 checks");}}
  if(x==S.max_x)S.max_ratio=R;
  if(have){int n=x-1;IV dprev=sub(prevM,prevF),dcur=sub(M,F);if(n<start){if(mpfr_cmp_si(prevF.lo,0)<0||mpfr_cmp_si(F.lo,0)<0)throw std::runtime_error("base F positivity");std::ostringstream z;z<<n<<'\t'<<lo_s(prevF)<<'\t'<<hi_s(prevF)<<'\t'<<lo_s(F)<<'\t'<<hi_s(F)<<'\t'<<lo_s(dprev)<<'\t'<<hi_s(dprev)<<'\t'<<lo_s(dcur)<<'\t'<<hi_s(dcur)<<'\n';gzline(base,z.str());}else{std::ostringstream z;z<<n<<'\t'<<lo_s(prevR,48)<<'\t'<<hi_s(prevR,48)<<'\t'<<lo_s(R,48)<<'\t'<<hi_s(R,48)<<'\n';gzline(comp,z.str());}}
  prevF=F;prevM=M;prevR=R;have=true;
 }
 gzclose(base);gzclose(comp);return S;
}

struct DivRec {u128 d;int sign;IV invsqrt,invd,logd,w,wlog;};
static std::vector<DivRec> divisors_for(int B){
 auto ps=primes_upto(B);std::vector<DivRec>v;v.reserve(1u<<ps.size());DivRec one;one.d=1;one.sign=1;one.invsqrt=from_ui(1);one.invd=from_ui(1);one.logd=from_ui(0);one.w=from_ui(1);one.wlog=from_ui(0);v.push_back(std::move(one));
 for(int p:ps){size_t m=v.size();IV pp=from_ui(p),ip=inv(pp),isp=inv(sqrt_i(pp)),lp=log_i(pp);for(size_t i=0;i<m;i++){DivRec z;z.d=v[i].d*p;z.sign=-v[i].sign;z.invsqrt=mul(v[i].invsqrt,isp);z.invd=mul(v[i].invd,ip);z.logd=add(v[i].logd,lp);z.w=(z.sign>0?z.invsqrt:neg(z.invsqrt));z.wlog=mul(z.w,z.logd);v.push_back(std::move(z));}}
 return v;
}
struct Event{u128 x;uint32_t idx;uint8_t type;};
static bool evless(const Event&a,const Event&b){if(a.x!=b.x)return a.x<b.x;if(a.type!=b.type)return a.type<b.type;return a.idx<b.idx;}
static IV eval_phi_log(const IV&A,const IV&B,const IV&C,const IV&lx,const IV&log4){return add(sub(mul(A,lx),B),mul(C,log4));}

static void phi_sweep(int B,const std::vector<DivRec>&divs,const fs::path&out,const IV&log4,CaseSummary&S){
 std::vector<Event>ev;ev.reserve(divs.size()*2);for(uint32_t i=0;i<divs.size();i++){ev.push_back({divs[i].d,i,0});ev.push_back({divs[i].d*4,i,1});}std::sort(ev.begin(),ev.end(),evless);
 IV A,Bs,C;bool init=false;double mn=0,mx=0;gzFile f=gzopen_checked(out/("phi_p"+std::to_string(B)+".tsv.gz"));gzline(f,"event\thull_lo_RNDD\thull_hi_RNDU\tcontinuity_overlap\n");
 for(const auto&e:ev){const auto&r=divs[e.idx];IV lx=(e.type==0?r.logd:add(r.logd,log4));IV L=eval_phi_log(A,Bs,C,lx,log4);if(e.type==0){upd_add(A,r.w);upd_add(Bs,r.wlog);}else{upd_sub(A,r.w);upd_sub(Bs,r.wlog);upd_add(C,r.w);}IV R=eval_phi_log(A,Bs,C,lx,log4);
  if(mpfr_cmp(L.hi,R.lo)<0||mpfr_cmp(R.hi,L.lo)<0)throw std::runtime_error("phi one-sided continuity intervals disjoint");IV H;mpfr_set(H.lo,(mpfr_cmp(L.lo,R.lo)<0?L.lo:R.lo),MPFR_RNDN);mpfr_set(H.hi,(mpfr_cmp(L.hi,R.hi)>0?L.hi:R.hi),MPFR_RNDN);IV lim=rat(3,2);if(!positive(add(H,lim))||!positive(sub(lim,H)))throw std::runtime_error("phi 3/2");double m=mid_d(H);if(!init||m<mn){mn=m;S.phi_min=H;S.phi_min_x=u128s(e.x);}if(!init||m>mx){mx=m;S.phi_max=H;S.phi_max_x=u128s(e.x);}init=true;
  std::ostringstream z;z<<u128s(e.x)<<'\t'<<lo_s(H,44)<<'\t'<<hi_s(H,44)<<"\t1\n";gzline(f,z.str());
 }
 gzclose(f);
}

struct TailSums{IV A,B,C,D,D2,D4;unsigned long N=0;};
static void tail_update(TailSums&s,const DivRec&r,uint8_t t){if(t==0){IV sinvd=(r.sign>0?r.invd:neg(r.invd));upd_add(s.A,sinvd);upd_add(s.B,r.w);upd_add(s.C,r.invd);upd_add(s.D,r.invsqrt);s.N++;}else if(t==1)upd_add(s.D2,r.invsqrt);else upd_add(s.D4,r.invsqrt);}
struct TailBounds { mpfr_t lower,upper,clow,cup; TailBounds(){mpfr_init2(lower,PREC);mpfr_init2(upper,PREC);mpfr_init2(clow,PREC);mpfr_init2(cup,PREC);} ~TailBounds(){mpfr_clear(lower);mpfr_clear(upper);mpfr_clear(clow);mpfr_clear(cup);} };
struct TailConst { IV r,u,log4,kappa,cphi,k9log,k6log,k15log,sqrt2; };
static void prod_lower(mpfr_ptr z,const IV&a,const IV&b){mpfr_t t;mpfr_init2(t,PREC);mpfr_mul(z,a.lo,b.lo,MPFR_RNDD);mpfr_mul(t,a.lo,b.hi,MPFR_RNDD);min_set(z,t);mpfr_mul(t,a.hi,b.lo,MPFR_RNDD);min_set(z,t);mpfr_mul(t,a.hi,b.hi,MPFR_RNDD);min_set(z,t);mpfr_clear(t);}
static void prod_upper(mpfr_ptr z,const IV&a,const IV&b){mpfr_t t;mpfr_init2(t,PREC);mpfr_mul(z,a.lo,b.lo,MPFR_RNDU);mpfr_mul(t,a.lo,b.hi,MPFR_RNDU);max_set(z,t);mpfr_mul(t,a.hi,b.lo,MPFR_RNDU);max_set(z,t);mpfr_mul(t,a.hi,b.hi,MPFR_RNDU);max_set(z,t);mpfr_clear(t);}
static void tail_bounds(const TailSums&s,const IV&sx,const TailConst&c,TailBounds&o){
 mpfr_t t1,t2,t3,nsup,fl,mu,fu,ml;for(auto*z:{t1,t2,t3,nsup,fl,mu,fu,ml})mpfr_init2(z,PREC);
 // N/sqrt(x), outward upper bound.
 mpfr_set_ui(t1,s.N,MPFR_RNDN);mpfr_div(nsup,t1,sx.lo,MPFR_RNDU);
 // F lower = 12 sqrt(x) A + 6 kappa B - N/sqrt(x) - C_phi.
 prod_lower(t1,sx,s.A);mpfr_mul_ui(t1,t1,12,MPFR_RNDD);
 prod_lower(t2,c.kappa,s.B);mpfr_mul_ui(t2,t2,6,MPFR_RNDD);
 mpfr_add(fl,t1,t2,MPFR_RNDD);mpfr_sub(fl,fl,nsup,MPFR_RNDD);mpfr_sub(fl,fl,c.cphi.hi,MPFR_RNDD);
 // M upper = 12 sqrt(x) C + N/sqrt(x) + (9/sqrt2) log4 D2.
 prod_upper(t1,sx,s.C);mpfr_mul_ui(t1,t1,12,MPFR_RNDU);prod_upper(t2,c.k9log,s.D2);
 mpfr_add(mu,t1,nsup,MPFR_RNDU);mpfr_add(mu,mu,t2,MPFR_RNDU);
 mpfr_mul(t3,c.r.hi,mu,MPFR_RNDU);mpfr_sub(o.lower,fl,t3,MPFR_RNDD);
 // F upper.
 prod_upper(t1,sx,s.A);mpfr_mul_ui(t1,t1,12,MPFR_RNDU);prod_upper(t2,c.kappa,s.B);mpfr_mul_ui(t2,t2,6,MPFR_RNDU);
 mpfr_add(fu,t1,t2,MPFR_RNDU);mpfr_add(fu,fu,nsup,MPFR_RNDU);mpfr_add(fu,fu,c.cphi.hi,MPFR_RNDU);
 // M lower.
 prod_lower(t1,sx,s.C);mpfr_mul_ui(t1,t1,12,MPFR_RNDD);prod_lower(t2,c.kappa,s.D);mpfr_mul_ui(t2,t2,6,MPFR_RNDD);
 mpfr_add(ml,t1,t2,MPFR_RNDD);mpfr_sub(ml,ml,nsup,MPFR_RNDD);
 prod_upper(t1,c.k6log,s.D);mpfr_sub(ml,ml,t1,MPFR_RNDD);prod_upper(t1,c.k15log,s.D4);mpfr_sub(ml,ml,t1,MPFR_RNDD);
 mpfr_mul(t3,c.u.lo,ml,MPFR_RNDD);mpfr_sub(o.upper,t3,fu,MPFR_RNDD);
 // Derivative coefficients.
 mpfr_mul(t1,c.r.hi,s.C.hi,MPFR_RNDU);mpfr_sub(o.clow,s.A.lo,t1,MPFR_RNDD);
 mpfr_mul(t1,c.u.lo,s.C.lo,MPFR_RNDD);mpfr_sub(o.cup,t1,s.A.hi,MPFR_RNDD);
 for(auto*z:{t1,t2,t3,nsup,fl,mu,fu,ml})mpfr_clear(z);
}
static void set_point_iv(IV&v,mpfr_srcptr x){mpfr_set(v.lo,x,MPFR_RNDN);mpfr_set(v.hi,x,MPFR_RNDN);}
static void tail_sweep(int B,long start,const std::vector<DivRec>&divs,const fs::path&out,const IV&log4,const IV&kappa,CaseSummary&S){
 std::vector<Event>ev;ev.reserve(divs.size()*3);for(uint32_t i=0;i<divs.size();i++){ev.push_back({divs[i].d,i,0});ev.push_back({divs[i].d*2,i,1});ev.push_back({divs[i].d*4,i,2});}std::sort(ev.begin(),ev.end(),evless);
 TailConst c;c.r=(B==61?rat(2399,100000):rat(17,500));c.u=(B==61?rat(9,200):rat(8,125));c.log4=log4;c.kappa=kappa;IV nine=from_ui(9);c.sqrt2=sqrt_i(from_ui(2));c.k9log=mul(divi(nine,c.sqrt2),log4);c.k6log=mul(from_ui(6),log4);c.k15log=mul(rat(3,2),log4);c.cphi=mul(rat(3,2),add(rat(15,2),divi(nine,c.sqrt2)));
 TailSums sums;gzFile f=gzopen_checked(out/("tail_p"+std::to_string(B)+".tsv.gz"));gzline(f,"event\tlower_left_RNDD\tlower_right_RNDD\tupper_left_RNDD\tupper_right_RNDD\n");
 bool minit=false,uinit=false;double lmin=0,umin=0;size_t count=0,pos=0;u128 st=(u128)start;
 auto record=[&](TailBounds&m,const std::string&x){
  if(mpfr_cmp_ui(m.lower,0)<=0||mpfr_cmp_ui(m.upper,0)<=0||mpfr_cmp_ui(m.clow,0)<=0||mpfr_cmp_ui(m.cup,0)<=0)throw std::runtime_error("tail margin/derivative");
  double lm=mpfr_get_d(m.lower,MPFR_RNDN),um=mpfr_get_d(m.upper,MPFR_RNDN);
  if(!minit||lm<lmin){lmin=lm;set_point_iv(S.tail_lower_min,m.lower);S.tail_lower_x=x;minit=true;}
  if(!uinit||um<umin){umin=um;set_point_iv(S.tail_upper_min,m.upper);S.tail_upper_x=x;uinit=true;}
 };
 // Initialize every event strictly below the analytic-tail splice.
 while(pos<ev.size()&&ev[pos].x<st){size_t j=pos+1;while(j<ev.size()&&ev[j].x==ev[pos].x)j++;for(size_t k=pos;k<j;k++)tail_update(sums,divs[ev[k].idx],ev[k].type);pos=j;}
 // Certify the splice point itself, even when it is not an activation event.
 {IV sx=sqrt_i(from_ui((unsigned long)start));TailBounds Z;tail_bounds(sums,sx,c,Z);record(Z,std::to_string(start));std::ostringstream z;z<<"START:"<<start<<'\t'<<fmt(Z.lower,30)<<'\t'<<fmt(Z.lower,30)<<'\t'<<fmt(Z.upper,30)<<'\t'<<fmt(Z.upper,30)<<'\n';gzline(f,z.str());}
 while(pos<ev.size()){size_t j=pos+1;while(j<ev.size()&&ev[j].x==ev[pos].x)j++;const Event& rep=ev[pos];const DivRec& rd=divs[rep.idx];IV base_sqrt=inv(rd.invsqrt);IV sx=(rep.type==0?base_sqrt:(rep.type==1?mul(c.sqrt2,base_sqrt):scale_si(base_sqrt,2)));TailBounds L;tail_bounds(sums,sx,c,L);for(size_t k=pos;k<j;k++)tail_update(sums,divs[ev[k].idx],ev[k].type);TailBounds R;tail_bounds(sums,sx,c,R);
  record(L,u128s(ev[pos].x));record(R,u128s(ev[pos].x));
  std::ostringstream z;z<<u128s(ev[pos].x)<<'\t'<<fmt(L.lower,30)<<'\t'<<fmt(R.lower,30)<<'\t'<<fmt(L.upper,30)<<'\t'<<fmt(R.upper,30)<<'\n';gzline(f,z.str());count++;pos=j;
 }
 gzclose(f);S.tail_events=count;
}

static std::string ivjson(const IV&x){return std::string("{\"lo\":\"")+lo_s(x)+"\",\"hi\":\""+hi_s(x)+"\"}";}

int main(int argc,char**argv){try{
 if(argc!=2){std::cerr<<"usage: certify OUTDIR\n";return 2;}fs::path out=argv[1];fs::create_directories(out);IV log4=log4_i(),kappa=mul(zeta_half_i(),log4);
 CaseSummary p61=compact_case(61,67,22000,out,log4);auto* d61=new std::vector<DivRec>(divisors_for(61));phi_sweep(61,*d61,out,log4,p61);tail_sweep(61,22000,*d61,out,log4,kappa,p61);
 CaseSummary p37=compact_case(37,41,84000,out,log4);auto* d37=new std::vector<DivRec>(divisors_for(37));phi_sweep(37,*d37,out,log4,p37);tail_sweep(37,84000,*d37,out,log4,kappa,p37);
 // Low-child discrepancy at X=184.
 std::vector<int>rp={67,71,73,79,83,89};IV D;for(int p:rp){IV pp=from_ui(p),term=mul(divi(rat(15,1),sqrt_i(from_ui(2))),mul(inv(sqrt_i(pp)),log_i(divi(from_ui(92),pp))));D=add(D,term);}IV full=sub(p61.Fmin,D);if(!positive(D)||!positive(full))throw std::runtime_error("low child mismatch");
 std::ofstream js(out/"verification.raw.json");js<<"{\n\"schema\":\"riemann.x97620.annular-bias.v2\",\n\"verdict\":\"PASS_EXACT_ANNULAR_BIAS_AND_P37_CONTRACTION_CERTIFICATE\",\n\"frozen_pr565_head\":\"339e3367660f40c74795802a6f8170b15e19b13a\",\n";
 auto emit=[&](const char*name,const CaseSummary&s,bool comma){js<<"\""<<name<<"\":{\"base_cells\":"<<s.base_cells<<",\"compact_cells\":"<<s.compact_cells<<",\"tail_events\":"<<s.tail_events<<",\"minimum_x\":"<<s.min_x<<",\"minimum_ratio\":"<<ivjson(s.min_ratio)<<",\"minimum_left_cell_derivative\":"<<ivjson(s.min_left_derivative)<<",\"minimum_right_cell_derivative\":"<<ivjson(s.min_right_derivative)<<",\"maximum_x\":"<<s.max_x<<",\"maximum_ratio\":"<<ivjson(s.max_ratio)<<",\"phi_min\":"<<ivjson(s.phi_min)<<",\"phi_min_x\":\""<<s.phi_min_x<<"\",\"phi_max\":"<<ivjson(s.phi_max)<<",\"phi_max_x\":\""<<s.phi_max_x<<"\",\"tail_min_lower_margin\":"<<ivjson(s.tail_lower_min)<<",\"tail_min_lower_x\":\""<<s.tail_lower_x<<"\",\"tail_min_upper_margin\":"<<ivjson(s.tail_upper_min)<<",\"tail_min_upper_x\":\""<<s.tail_upper_x<<"\"}"<<(comma?",\n":"\n");};
 emit("p61",p61,true);emit("p37",p37,true);js<<"\"x184\":{\"F\":"<<ivjson(p61.Fmin)<<",\"M\":"<<ivjson(p61.Mmin)<<",\"ratio\":"<<ivjson(p61.min_ratio)<<",\"F_minus_M_over_40\":"<<ivjson(p61.diff40)<<",\"F_minus_M_over_42\":"<<ivjson(p61.diff42)<<",\"discarded_low_children\":"<<ivjson(D)<<",\"true_full_scalar\":"<<ivjson(full)<<"},\n\"rational_moats\":{\"p61_lower\":\"1199/50000\",\"p61_above_one_over_42\":\"179/1050000\",\"p61_upper\":\"9/200\",\"p37_lower\":\"17/500\",\"p37_upper\":\"8/125\"},\n\"rh_established_by_replay\":false\n}\n";js.close();
 std::cout<<"PASS_EXACT_ANNULAR_BIAS_AND_P37_CONTRACTION_CERTIFICATE\n";return 0;
 }catch(const std::exception&e){std::cerr<<"FAIL: "<<e.what()<<"\n";return 1;}}
