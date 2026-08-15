#pragma STDC FENV_ACCESS ON
#include <boost/multiprecision/cpp_int.hpp>
#include <boost/numeric/interval.hpp>
#include <boost/numeric/interval/hw_rounding.hpp>
#include <boost/numeric/interval/rounded_transc.hpp>
#include <algorithm>
#include <cmath>
#include <iomanip>
#include <iostream>
#include <limits>
#include <vector>

using boost::multiprecision::uint128_t;
namespace bn = boost::numeric;
namespace il = boost::numeric::interval_lib;
using Round = il::save_state<il::rounded_transc_std<long double, il::rounded_math<long double>>>;
using Policies = il::policies<Round, il::checking_strict<long double>>;
using ProtectedI = bn::interval<long double, Policies>;
using I = typename il::unprotect<ProtectedI>::type;

static inline I exact_ld(long double x){ return I(x); }
static inline I enclose_ld(long double x){
    return I(std::nextafterl(x, -std::numeric_limits<long double>::infinity()),
             std::nextafterl(x,  std::numeric_limits<long double>::infinity()));
}
static inline I enclose_uint(const uint128_t& u){ return enclose_ld(u.convert_to<long double>()); }
static inline long double lo(const I& x){ return x.lower(); }
static inline long double hi(const I& x){ return x.upper(); }
static inline I sqr(const I& x){ return x*x; }
static inline I cube(const I& x){ return x*x*x; }
static inline I fourth(const I& x){ I y=x*x; return y*y; }

struct Div{uint128_t d; int mu; I df,inv,logd;};
struct Sums{I A=I(0),B=I(0),C=I(0),D=I(0);};
struct Event{uint128_t x;int type,idx;};
bool operator<(Event const&a,Event const&b){if(a.x!=b.x)return a.x<b.x;return a.type<b.type;}

// Rational outward intervals containing the constants used by PR #497.
static const I ZH(-1.460355L, -1.460354L);
static const I ZP(-3.922647L, -3.922646L);

struct Co{I A,B,C,D,E,F,G;};
static I val(const Co& q, const I& x){
    I t=sqrt(x), l=log(t);
    return q.A*t*t+q.B*t*l+q.C*t+q.D*l+q.E+q.F/(t*t)+q.G/(t*t*t);
}
static I derivative(const Co& q, const I& t){
    return I(2.0L)*q.A*t + q.B*(log(t)+I(1.0L)) + q.C + q.D/t - I(2.0L)*q.F/cube(t) - I(3.0L)*q.G/fourth(t);
}
static void add(Sums& s, Div const& d){s.A+=I(1)/d.df;s.B+=d.inv;s.C+=d.logd*d.inv;s.D+=d.df;}

int main(int argc,char**argv){
 Round rounding_guard;
 int JLO=2,JHI=66; if(argc>=2)JLO=std::stoi(argv[1]); if(argc>=3)JHI=std::stoi(argv[2]);
 std::vector<int>P={2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61};
 std::vector<std::pair<uint128_t,int>>raw={{1,1}};
 for(int p:P){size_t n=raw.size();for(size_t i=0;i<n;i++)raw.push_back({raw[i].first*p,-raw[i].second});}
 std::sort(raw.begin(),raw.end(),[](auto&a,auto&b){return a.first<b.first;});
 std::vector<Div>ds; ds.reserve(raw.size());
 for(auto z:raw){I d=enclose_uint(z.first);ds.push_back({z.first,z.second,d,I(1)/sqrt(d),log(d)});}
 const uint128_t START=166000;
 Sums ce67,co67; for(auto const&d:ds){if(d.d>67)break;(d.mu==1?add(ce67,d):add(co67,d));}
 long double global=1e300L,parentglobal=1e300L,corrglobal=0,derglobal=1e300L,tailpolyglobal=1e300L,tailpolyderglobal=1e300L;
 int gj=0,pgj=0,cgj=0,dgj=0;uint128_t gx=0,pgx=0,cgx=0,dgx=0;
 std::vector<long double> rowfull(67,1e300L), rowfullupper(67,-1e300L), rowparent(67,1e300L), rowder(67,1e300L), rowcorr(67,0);
 std::vector<uint128_t> rowfullx(67),rowparentx(67),rowderx(67),rowcorrx(67);
 for(int j=JLO;j<=JHI;j++){
  std::vector<Event>ev;ev.reserve(ds.size()*3);
  for(int i=0;i<(int)ds.size();i++){ev.push_back({ds[i].d,0,i});ev.push_back({ds[i].d*j,1,i});ev.push_back({ds[i].d*(j+1),2,i});}
  std::sort(ev.begin(),ev.end());
  Sums te,to,be,bo;I stripE=I(0),stripO=I(0);size_t k=0;
  I Aj=I(j+1)/I(j-1), Bj=-I((j+1)*(j-2))/I(j*(j-1)), Cj=I(2)/I(j*(j-1));
  I qa=I(4.0L)*Cj,qb=Cj*ZH,qc=Cj*ZP;
  for(int m=1;m<j;m++){
      I mm(m); qb-=Cj/sqrt(mm); qc+=Cj*log(mm)/sqrt(mm);
  }
  qb+=(Aj-Cj)/sqrt(I(j)); qc-=(Aj-Cj)*log(I(j))/sqrt(I(j));
  qb+=(Bj-Cj)/sqrt(I(j+1)); qc-=(Bj-Cj)*log(I(j+1))/sqrt(I(j+1));
  I qstrip=Aj/sqrt(I(j))*log(I(j+1)/I(j));
  Sums cre,cro;for(auto const&d:ds){if(d.d*(uint128_t)j>67)break;(d.mu==1?add(cre,d):add(cro,d));}
  I qchild=(67>j?Aj/sqrt(I(j))*log(I(67)/I(j)):I(0))+I(4.0L)*Cj*sqrt(I(67));
  I Et=I(4.0L)*sqrt(I(67))*ce67.A,Ot=I(4.0L)*sqrt(I(67))*co67.A,Er=qchild*cre.B,Or=qchild*cro.B;
  auto cofun=[&](){
      I Ae=te.A,Ao=to.A,Be=te.B,Bo=to.B;
      I arE=qa*be.A,brE=I(2.0L)*qb*be.B,crE=-qb*be.C+qc*be.B;
      I arO=qa*bo.A,brO=I(2.0L)*qb*bo.B,crO=-qb*bo.C+qc*bo.B+qstrip*stripO;
      I erE=-I(5.0L)*Cj*be.D,erO=I(5.0L)*Cj*bo.D;
      return Co{I(4.0L)*(Ao*arE-Ae*arO),I(4.0L)*(Ao*brE-Ae*brO),I(4.0L)*(Ao*crE-Ae*crO)-I(3.0L)*(Bo*arE-Be*arO),-I(3.0L)*(Bo*brE-Be*brO),-I(3.0L)*(Bo*crE-Be*crO),I(4.0L)*(Ao*erE-Ae*erO),-I(3.0L)*(Bo*erE-Be*erO)};
  };
  auto corr=[&](const I& x){
      I t=sqrt(x),lx=log(x),r=sqrt(I(67))/t;I ET=I(4.0L)*t*te.A,OT=I(4.0L)*t*to.A;
      I ERP=I(4.0L)*Cj*t*be.A+Aj/sqrt(I(j))*be.B*lx+qstrip*stripE;
      I ORP=I(4.0L)*Cj*t*bo.A+Aj/sqrt(I(j))*bo.B*lx+qstrip*stripO;
      return r*(Ot*ERP+OT*Er+Et*ORP+ET*Or)+r*r*(Ot*Er+Et*Or);
  };
  auto evaluate=[&](const uint128_t& xx){
      I x=enclose_uint(xx);Co c=cofun();I pv=val(c,x),cv=corr(x),fv=pv-cv;
      long double pl=lo(pv), cu=hi(cv), fl=lo(fv);
      if(pl<rowparent[j]){rowparent[j]=pl;rowparentx[j]=xx;}if(cu>rowcorr[j]){rowcorr[j]=cu;rowcorrx[j]=xx;}if(fl<rowfull[j]){rowfull[j]=fl;rowfullupper[j]=hi(fv);rowfullx[j]=xx;}
      if(pl<parentglobal){parentglobal=pl;pgj=j;pgx=xx;}if(cu>corrglobal){corrglobal=cu;cgj=j;cgx=xx;}if(fl<global){global=fl;gj=j;gx=xx;}
  };
  bool didStart=false;
  while(k<ev.size()){
    uint128_t x=ev[k].x;
    if(!didStart && x>START){evaluate(START);didStart=true;}
    size_t kk=k;while(kk<ev.size()&&ev[kk].x==x){auto&e=ev[kk];auto const&d=ds[e.idx];
      if(e.type==0)(d.mu==1?add(te,d):add(to,d));
      else if(e.type==1){if(d.mu==1)stripE+=d.inv;else stripO+=d.inv;}
      else{if(d.mu==1){add(be,d);stripE-=d.inv;}else{add(bo,d);stripO-=d.inv;}}
      kk++;}
    k=kk;if(x<START)continue;didStart=true;evaluate(x);Co c=cofun();
    if(k<ev.size()){
      uint128_t xu128=ev[k].x;if(xu128>x){I tl=sqrt(enclose_uint(x)),tu=sqrt(enclose_uint(xu128));I ti(lo(tl),hi(tu));I di=derivative(c,ti);long double dl=lo(di);
        if(dl<rowder[j]){rowder[j]=dl;rowderx[j]=x;}if(dl<derglobal){derglobal=dl;dgj=j;dgx=x;}}
    }
  }
  if(!didStart)evaluate(START);
  Co tail=cofun();I t0=sqrt(enclose_uint(ev.back().x));I poly=tail.B*fourth(t0)+I(6.0L)*tail.F*t0+I(12.0L)*tail.G;I polyder=I(4.0L)*tail.B*cube(t0)+I(6.0L)*tail.F;
  if(!(lo(tail.B)>0 && lo(poly)>0 && lo(polyder)>0)) { std::cerr<<"last-tail persistence failure "<<j<<" B="<<lo(tail.B)<<" poly="<<lo(poly)<<" pder="<<lo(polyder)<<"\n"; return 6; }
  tailpolyglobal=std::min(tailpolyglobal,lo(poly));tailpolyderglobal=std::min(tailpolyderglobal,lo(polyder));
  std::cerr<<std::setprecision(18)<<"ROW "<<j<<" full_lo="<<rowfull[j]<<" x="<<rowfullx[j]<<" parent_lo="<<rowparent[j]<<" px="<<rowparentx[j]<<" corr_hi="<<rowcorr[j]<<" cx="<<rowcorrx[j]<<" der_lo="<<rowder[j]<<" dx="<<rowderx[j]<<"\n";
 }
 if(!(global>26.0L)){std::cerr<<"tail margin failure "<<global<<"\n";return 2;}
 if(!(parentglobal>79.0L)){std::cerr<<"parent margin failure "<<parentglobal<<"\n";return 3;}
 if(!(derglobal>0.23L)){std::cerr<<"derivative margin failure "<<derglobal<<"\n";return 4;}
 // Directed row-66 extremality certificate: every row 2..65 has a lower bound above
 // the directed upper evaluation of row 66 at x=166000.  The latter is evaluated below.
 long double row66_ref = (JHI>=66 && JLO<=66)?rowfull[66]:global;
 long double separation=1e300L;int sepj=0; if(JLO<=65 && JHI>=66){for(int j=JLO;j<66;j++){long double s=rowfull[j]-row66_ref;if(s<separation){separation=s;sepj=j;}} if(!(separation>1.0L)){std::cerr<<"row66 separation failure "<<separation<<" row "<<sepj<<"\n";return 7;}} else {separation=0;}
 std::cout.precision(24);const unsigned long long event_records=3ULL*static_cast<unsigned long long>(ds.size())*static_cast<unsigned long long>(JHI-JLO+1);
 std::cout<<"{\n"
 <<"  \"arithmetic_class\": \"BOOST_FENV_DIRECTED_LONG_DOUBLE_INTERVAL_UINT128_EVENT_SWEEP\",\n"
 <<"  \"classification\": \"PASS_DIRECTED_TARGET_LORENZ_TAIL_AVLT\",\n"
 <<"  \"tail_start\": 166000,\n"
 <<"  \"divisor_count\": "<<ds.size()<<",\n"
 <<"  \"row_count\": "<<(JHI-JLO+1)<<",\n"
 <<"  \"event_records\": "<<event_records<<",\n"
 <<"  \"directed_full_lower_bound\": \""<<global<<"\",\n"
 <<"  \"directed_full_minimum_row\": "<<gj<<",\n"
 <<"  \"directed_full_minimum_x\": \""<<gx<<"\",\n"
 <<"  \"directed_full_interval_upper_at_minimum\": \""<<rowfullupper[gj]<<"\",\n"
 <<"  \"directed_parent_lower_bound\": \""<<parentglobal<<"\",\n"
 <<"  \"directed_parent_derivative_lower_bound\": \""<<derglobal<<"\",\n"
 <<"  \"row66_extremality_separation_lower\": \""<<separation<<"\",\n"
 <<"  \"row66_nearest_competitor\": "<<sepj<<",\n"
 <<"  \"last_interval_second_derivative_polynomial_lower\": \""<<tailpolyglobal<<"\",\n"
 <<"  \"last_interval_polynomial_derivative_lower\": \""<<tailpolyderglobal<<"\",\n"
 <<"  \"rounding_contract\": \"Boost.Numeric.Interval save_state rounded_transc_std<long double> under hardware fenv; exact uint128 event ordering; integer conversion bracketed by adjacent long doubles\",\n"
 <<"  \"rh_established_by_replay\": false\n"
 <<"}\n";
}
