#include "mpfr_min.h"
#include <algorithm>
#include <cmath>
#include <cstdint>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <limits>
#include <sstream>
#include <stdexcept>
#include <string>
#include <vector>

static constexpr mpfr_prec_t PREC = 256;
static constexpr long double INF = std::numeric_limits<long double>::infinity();
struct I { long double lo, hi; };
static long double dn(long double x){return std::nextafterl(x,-INF);}
static long double up(long double x){return std::nextafterl(x, INF);}
static I zero(){return {0.0L,0.0L};}
static I add(I a,I b){return {dn(a.lo+b.lo),up(a.hi+b.hi)};}
static I sub(I a,I b){return {dn(a.lo-b.hi),up(a.hi-b.lo)};}
static I mul(I a,I b){long double v[4]={a.lo*b.lo,a.lo*b.hi,a.hi*b.lo,a.hi*b.hi};return {dn(*std::min_element(v,v+4)),up(*std::max_element(v,v+4))};}
static I scale(I a,long long c){if(c>=0)return {dn(a.lo*c),up(a.hi*c)};return {dn(a.hi*c),up(a.lo*c)};}
struct M{mpfr_t x;M(){mpfr_init2(x,PREC);}~M(){mpfr_clear(x);}M(const M&)=delete;M&operator=(const M&)=delete;};
static I invsqrt(unsigned long n){M x,slo,shi,lo,hi;mpfr_set_ui(x.x,n,MPFR_RNDN);mpfr_sqrt(slo.x,x.x,MPFR_RNDD);mpfr_sqrt(shi.x,x.x,MPFR_RNDU);mpfr_ui_div(lo.x,1,shi.x,MPFR_RNDD);mpfr_ui_div(hi.x,1,slo.x,MPFR_RNDU);return {dn(mpfr_get_ld(lo.x,MPFR_RNDD)),up(mpfr_get_ld(hi.x,MPFR_RNDU))};}
static I logui(unsigned long n){M x,lo,hi;mpfr_set_ui(x.x,n,MPFR_RNDN);mpfr_log(lo.x,x.x,MPFR_RNDD);mpfr_log(hi.x,x.x,MPFR_RNDU);return {dn(mpfr_get_ld(lo.x,MPFR_RNDD)),up(mpfr_get_ld(hi.x,MPFR_RNDU))};}
static std::vector<int> primes_upto(int n){std::vector<bool>s(n+1,true);s[0]=s[1]=false;for(int p=2;p*p<=n;++p)if(s[p])for(int k=p*p;k<=n;k+=p)s[k]=false;std::vector<int>v;for(int i=2;i<=n;++i)if(s[i])v.push_back(i);return v;}
static long long qstar(int n){if(n==2)return 15;if(n==3)return 6;if(n==4)return 3;if(n>=5)return 6;return 0;}
static std::vector<long long> base_q(int N){std::vector<long long>c(N+1);for(int n=1;n<=N;++n)c[n]=qstar(n);return c;}
static void euler_factor(std::vector<long long>&c,int p){int N=(int)c.size()-1;for(int k=N/p;k>=1;--k)c[p*k]-=c[k];}
static std::vector<long long> p61_coeff(int N){auto c=base_q(N);for(int p:primes_upto(61))euler_factor(c,p);return c;}
static std::vector<long long> native_coeff(int N){auto c=base_q(N);for(int p:primes_upto(N))euler_factor(c,p);return c;}
static std::vector<long long> depth2_coeff(int N,const std::vector<long long>&b){auto c=b;for(int p:primes_upto(N)){if(p<67)continue;for(int k=1;k<=N/p;++k)c[p*k]-=b[k];}return c;}
static I evaluate(int X,const std::vector<long long>&c,const std::vector<I>&isq,const std::vector<I>&logs){I out=zero();I lx=logs[X],l4=logs[4];for(int n=1;n<=X;++n){long long a=c[n];if(!a)continue;I h;if(4LL*n<=X)h=l4;else h=sub(lx,logs[n]);out=add(out,scale(mul(isq[n],h),a));}return out;}
static std::string js(I x){std::ostringstream o;o<<std::setprecision(21)<<"["<<x.lo<<","<<x.hi<<"]";return o.str();}
int main(int argc,char**argv){
 std::string out=(argc>1?argv[1]:"results/finite-certificates.json");
 const int N=61841;
 std::cerr<<"MPFR "<<mpfr_get_version()<<" precision="<<PREC<<"\n";
 std::vector<I>isq(N+1),logs(N+1);isq[1]=invsqrt(1);logs[1]=zero();
 for(int n=2;n<=N;++n){isq[n]=invsqrt(n);logs[n]=logui(n);}
 auto b=p61_coeff(N);auto nat=native_coeff(N);auto c2=depth2_coeff(N,b);
 struct Rec{int X;I base,curr,native;};std::vector<Rec>rs;
 for(int X:{184,32605,32606,61841})rs.push_back({X,evaluate(X,b,isq,logs),evaluate(X,c2,isq,logs),evaluate(X,nat,isq,logs)});
 if(!(rs[0].curr.lo>0 && rs[0].native.lo>0 && rs[0].base.lo-rs[0].native.hi>1.36L))throw std::runtime_error("X184 gate");
 if(!(rs[1].curr.lo>0 && rs[2].curr.hi<0))throw std::runtime_error("C2 sign-change gate");
 if(!(rs[3].curr.hi<-21.3L && rs[3].native.lo>9.5L && rs[3].base.lo-rs[3].native.hi>378.0L))throw std::runtime_error("X61841 gate");
 std::ofstream f(out);f<<"{\n  \"classification\": \"PASS_T97700_DIRECTED_FINITE_STRESS_CASES\",\n  \"mpfr_version\": \""<<mpfr_get_version()<<"\",\n  \"precision_bits\": "<<PREC<<",\n  \"records\": [\n";
 for(size_t i=0;i<rs.size();++i){f<<"    {\"X\": "<<rs[i].X<<", \"P61_base\": "<<js(rs[i].base)<<", \"depth2_current\": "<<js(rs[i].curr)<<", \"native_scalar\": "<<js(rs[i].native)<<"}"<<(i+1<rs.size()?",":"")<<"\n";}
 f<<"  ],\n  \"certified\": [\"X184 native coefficient retained\", \"C2(32605)>0>C2(32606)\", \"C2(61841)<-21.3\", \"native_scalar(61841)>9.5\"],\n  \"rh_established\": false\n}\n";
 std::cout<<"PASS_T97700_DIRECTED_FINITE_STRESS_CASES\n";
}
