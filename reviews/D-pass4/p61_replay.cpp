// Independent P61 bias replay: directed MPFR primitives, then integer intervals.
// No upstream producer; closed coefficient formula replaces its prime convolution.
#include "mpfr_abi.h"
#include <boost/multiprecision/cpp_int.hpp>
#include <algorithm>
#include <array>
#include <fstream>
#include <iostream>
#include <stdexcept>
#include <string>
#include <vector>
using Big=boost::multiprecision::cpp_int;using Int=__int128_t;using UInt=__uint128_t;
constexpr int BITS=48;constexpr Int Q=Int(1)<<BITS;constexpr unsigned LIMIT=1000000;
void require(bool ok,const char*m){if(!ok)throw std::runtime_error(m);}
std::string dec(UInt n){if(!n)return "0";std::string s;while(n){s.push_back(char('0'+n%10));n/=10;}std::reverse(s.begin(),s.end());return s;}
std::string decs(Int n){return n<0?"-"+dec(UInt(-n)):dec(UInt(n));}
Int plus(Int a,Int b){Int c;require(!__builtin_add_overflow(a,b,&c),"add overflow");return c;}
Int times(Int a,Int b){Int c;require(!__builtin_mul_overflow(a,b,&c),"product overflow");return c;}
template<class T>struct Box{T lo{},hi{};};using I=Box<Int>;using J=Box<Big>;
I add(I a,I b){return {plus(a.lo,b.lo),plus(a.hi,b.hi)};}I sub(I a,I b){return {plus(a.lo,-b.hi),plus(a.hi,-b.lo)};}
I scale(I a,Int n){return n>=0?I{times(a.lo,n),times(a.hi,n)}:I{times(a.hi,n),times(a.lo,n)};}
I mul(I a,I b){Int v[]={times(a.lo,b.lo),times(a.lo,b.hi),times(a.hi,b.lo),times(a.hi,b.hi)};return {*std::min_element(v,v+4),*std::max_element(v,v+4)};}
Int absmax(I a){return std::max(a.lo<0?-a.lo:a.lo,a.hi<0?-a.hi:a.hi);}
J add(J a,J b){return {a.lo+b.lo,a.hi+b.hi};}J scale(J a,int n){return n>=0?J{a.lo*n,a.hi*n}:J{a.hi*n,a.lo*n};}
J mul(J a,J b){Big v[]={a.lo*b.lo,a.lo*b.hi,a.hi*b.lo,a.hi*b.hi};return {*std::min_element(v,v+4),*std::max_element(v,v+4)};}
Big absmax(J a){Big l=a.lo<0?-a.lo:a.lo,h=a.hi<0?-a.hi:a.hi;return std::max(l,h);}
struct Primitive{
 mpfr_t x,xlo,xhi,slo,shi,llo,lhi,tmp;mpz_t zi;
 Primitive(){for(auto p:{x,xlo,xhi,slo,shi,llo,lhi,tmp})mpfr_init2(p,256);mpz_init(zi);}
 ~Primitive(){for(auto p:{x,xlo,xhi,slo,shi,llo,lhi,tmp})mpfr_clear(p);mpz_clear(zi);}
 I small(mpfr_srcptr l,mpfr_srcptr h){mpfr_mul_2ui(tmp,l,BITS,MPFR_RNDD);long a=mpfr_get_si(tmp,MPFR_RNDD);mpfr_mul_2ui(tmp,h,BITS,MPFR_RNDU);long b=mpfr_get_si(tmp,MPFR_RNDU);return {a,b};}
 Big integer(mpfr_srcptr a,mpfr_rnd_t r){mpfr_mul_2ui(tmp,a,96,r);mpfr_get_z(zi,tmp,r);std::vector<char>s(mpz_sizeinbase(zi,10)+4);mpz_get_str(s.data(),10,zi);return Big(s.data());}
 J big(mpfr_srcptr l,mpfr_srcptr h){return {integer(l,MPFR_RNDD),integer(h,MPFR_RNDU)};}
 void rational(unsigned n,unsigned d){mpfr_set_ui(x,n,MPFR_RNDN);mpfr_div_ui(xlo,x,d,MPFR_RNDD);mpfr_div_ui(xhi,x,d,MPFR_RNDU);}
 I root(unsigned n,unsigned d=1){rational(n,d);mpfr_sqrt(slo,xlo,MPFR_RNDD);mpfr_sqrt(shi,xhi,MPFR_RNDU);return small(slo,shi);}
 I log(unsigned n,unsigned d=1){rational(n,d);mpfr_log(llo,xlo,MPFR_RNDD);mpfr_log(lhi,xhi,MPFR_RNDU);return small(llo,lhi);}
 std::array<I,3>atom(unsigned n){mpfr_set_ui(x,n,MPFR_RNDN);mpfr_sqrt(slo,x,MPFR_RNDD);mpfr_sqrt(shi,x,MPFR_RNDU);mpfr_ui_div(xlo,1,shi,MPFR_RNDD);mpfr_ui_div(xhi,1,slo,MPFR_RNDU);I inv=small(xlo,xhi);mpfr_log(llo,x,MPFR_RNDD);mpfr_log(lhi,x,MPFR_RNDU);I l=small(llo,lhi);mpfr_div(xlo,llo,shi,MPFR_RNDD);mpfr_div(xhi,lhi,slo,MPFR_RNDU);return {inv,l,small(xlo,xhi)};}
 I zhalf(){rational(1,2);mpfr_zeta(llo,xlo,MPFR_RNDD);mpfr_zeta(lhi,xhi,MPFR_RNDU);return small(llo,lhi);}
 void large(UInt n){auto s=dec(n);require(mpfr_set_str(x,s.c_str(),10,MPFR_RNDN)==0,"large input");}
 std::array<J,2>tailatom(UInt n){large(n);mpfr_ui_div(xlo,1,x,MPFR_RNDD);mpfr_ui_div(xhi,1,x,MPFR_RNDU);J inv=big(xlo,xhi);mpfr_sqrt(slo,x,MPFR_RNDD);mpfr_sqrt(shi,x,MPFR_RNDU);mpfr_ui_div(xlo,1,shi,MPFR_RNDD);mpfr_ui_div(xhi,1,slo,MPFR_RNDU);return {inv,big(xlo,xhi)};}
 J largeroot(UInt n){large(n);mpfr_sqrt(slo,x,MPFR_RNDD);mpfr_sqrt(shi,x,MPFR_RNDU);return big(slo,shi);}
};
const std::array<unsigned,18>PS={2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61};
struct Prefix{I inv,log;};struct Minimum{bool set=false;I value;unsigned arg=0;void put(I v,unsigned n){if(!set||v.lo<value.lo){set=true;value=v;arg=n;}}};
struct Divisor{UInt n;int mu;};struct Tail{J inv,isqrt,absolute;bool set=false;Big minimum;UInt left=0,right=0;unsigned slabs=0;};
void push(Tail&t,const std::array<J,2>&a,int c){t.inv=add(t.inv,scale(a[0],c));t.isqrt=add(t.isqrt,scale(a[1],c));t.absolute=add(t.absolute,scale(a[1],c<0?-c:c));}
Big bound(const Tail&t,J sq){const Big q=Big(1)<<96;return 12*mul(sq,t.inv).lo-20*absmax(t.isqrt)*q-5*t.absolute.hi*q;}
void jsonbox(std::ostream&o,I x){o<<"[\""<<decs(x.lo)<<"\",\""<<decs(x.hi)<<"\"]";}
int main(int argc,char**argv){try{
 require(sizeof(long)==8,"64-bit long required");require(mpfr_get_version()[0]=='4',"MPFR4 ABI required");
 Primitive p;std::vector<std::array<I,3>>prim(LIMIT+1);for(unsigned n=1;n<=LIMIT;++n)prim[n]=p.atom(n);
 std::vector<unsigned>omega(LIMIT+1),rest(LIMIT+1);std::vector<int>muP(LIMIT+1,1);for(unsigned n=1;n<=LIMIT;++n)rest[n]=n;
 for(unsigned q:PS)for(unsigned n=q;n<=LIMIT;n+=q){++omega[n];if(n%(q*q)==0)muP[n]=0;else muP[n]*=-1;while(rest[n]%q==0)rest[n]/=q;}
 for(unsigned n=1;n<=LIMIT;++n)if(rest[n]!=1)muP[n]=0;
 std::vector<Prefix>F(LIMIT+1),M(LIMIT+1);std::array<Minimum,5>minima;unsigned finite_checks=0;
 for(unsigned n=1;n<=LIMIT;++n){
  auto dmu=[&](unsigned q){return n%q==0?muP[n/q]:0;};auto ind=[&](unsigned q){return n%q==0&&muP[n/q]!=0?1:0;};
  long f=6*(omega[n]==0)-6*dmu(1)+9*dmu(2)-3*dmu(4),m=6*(1L<<omega[n])-6*ind(1)+9*ind(2)-3*ind(4);
  F[n]={add(F[n-1].inv,scale(prim[n][0],f)),add(F[n-1].log,scale(prim[n][2],f))};M[n]={add(M[n-1].inv,scale(prim[n][0],m)),add(M[n-1].log,scale(prim[n][2],m))};
  auto observe=[&](const std::vector<Prefix>&P){unsigned k=n/4;return sub(add(mul(prim[4][1],P[k].inv),mul(prim[n][1],sub(P[n].inv,P[k].inv))),scale(sub(P[n].log,P[k].log),Q));};
  I v=observe(F),w=observe(M);
  if(n>=3&&n<=66){require(v.lo>0,"initial F");minima[0].put(v,n);++finite_checks;}
  if(n>=5&&n<=66){I d=sub(w,v);require(d.lo>0,"initial M-F");minima[1].put(d,n);++finite_checks;}
  if(n>=67){I a=sub(scale(v,42),w),b=sub(w,scale(v,8)),c=sub(scale(v,40),w);require(a.lo>0&&b.lo>0,"finite inequalities");minima[2].put(a,n);minima[3].put(b,n);minima[4].put(c,n);finite_checks+=2;}
 }
 require(minima[4].value.hi<0,"1/40 counterexample");
 I c0=mul(add(add(scale(p.zhalf(),6),I{-15*Q/2,-15*Q/2}),scale(prim[2][0],9)),prim[4][1]);require(absmax(c0)<20*Q*Q,"C0 bound");Int compact_max=0;unsigned compact_n=0;
 for(unsigned n=200;n<=1600;++n){I A{};for(unsigned j=2;j<=16;++j){if(n<100*j)continue;unsigned w=j==2?15:j==4?3:6;I h=n>=400*j?prim[4][1]:p.log(n,100*j);A=add(A,scale(mul(prim[j][0],h),w));}I er=sub(sub(A,scale(p.root(n,100),12*Q)),c0);Int a=absmax(er);if(a>compact_max){compact_max=a;compact_n=n;}}
 require(compact_max*4<13*Q*Q,"sample error <13/4");require(13*100+4*36<20*100,"Lipschitz extension <5");
 std::vector<Divisor>ds{{1,1}};for(unsigned q:PS){size_t n=ds.size();for(size_t i=0;i<n;++i){UInt v;require(!__builtin_mul_overflow(ds[i].n,UInt(q),&v),"divisor overflow");ds.push_back({v,-ds[i].mu});}}
 std::sort(ds.begin(),ds.end(),[](auto a,auto b){return a.n<b.n;});require(ds.size()==(1u<<18),"divisor count");
 Tail ta,tb;for(size_t j=0;j<ds.size();++j){auto a=p.tailatom(ds[j].n);push(ta,a,42*ds[j].mu-1);push(tb,a,1-8*ds[j].mu);UInt l=2*ds[j].n,r=j+1<ds.size()?2*ds[j+1].n:0;if(r&&r<=LIMIT)continue;l=std::max(l,UInt(LIMIT));J sl=p.largeroot(l),sr=r?p.largeroot(r):J{};
  for(Tail*t:{&ta,&tb}){Big b=bound(*t,sl);if(r){Big c=bound(*t,sr);if(c<b)b=c;}else require(t->inv.lo>0,"last slope");require(b>0,"tail inequality");++t->slabs;if(!t->set||b<t->minimum){t->set=true;t->minimum=b;t->left=l;t->right=r;}}
 }
 std::ofstream file;std::ostream*out=&std::cout;if(argc>1){file.open(argv[1]);require(bool(file),"output");out=&file;}auto&o=*out;
 o<<"{\n\"schema\":\"reviewer-D.P61.integer-interval-replay.v1\",\n\"status\":\"PASS\",\n\"mpfr_version\":\""<<mpfr_get_version()<<"\",\n\"primitive_precision\":256,\n\"finite_endpoint\":"<<LIMIT<<",\n\"finite_inequalities_checked\":"<<finite_checks<<",\n\"finite_denominator\":\""<<decs(Q*Q)<<"\",\n\"finite_minima\":[\n";
 for(size_t i=0;i<minima.size();++i){o<<"{\"test\":"<<i<<",\"N\":"<<minima[i].arg<<",\"numerator_interval\":";jsonbox(o,minima[i].value);o<<"}"<<(i+1<minima.size()?",\n":"\n");}
 o<<"],\n\"compact_C0_numerators\":";jsonbox(o,c0);o<<",\n\"compact_sample_upper_numerator\":\""<<decs(compact_max)<<"\",\n\"compact_sample_arg_numerator_over_100\":"<<compact_n<<",\n\"compact_samples\":1401,\n\"compact_Lipschitz_bound\":36,\n\"divisor_count\":"<<ds.size()<<",\n\"tail_denominator\":\""<<(Big(1)<<192)<<"\",\n\"tail_minima\":[\n";
 for(int i=0;i<2;++i){auto&t=i?tb:ta;o<<"{\"test\":"<<i<<",\"left\":\""<<dec(t.left)<<"\",\"right\":\""<<(t.right?dec(t.right):"infinity")<<"\",\"lower_numerator\":\""<<t.minimum<<"\",\"slabs_checked\":"<<t.slabs<<"}"<<(i==0?",\n":"\n");}
 o<<"],\n\"analytic_ramp_input\":\"L-93600 as reconstructed in Reviewer D R21\",\n\"global_bias\":\"1/42 <= F/M <= 1/8 for x>=67\",\n\"RH_proved\":false\n}\n";return 0;
}catch(const std::exception&e){std::cerr<<"REJECTED: "<<e.what()<<"\n";return 2;}}
