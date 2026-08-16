#pragma STDC FENV_ACCESS ON
#include <boost/multiprecision/cpp_int.hpp>
#include <boost/numeric/interval.hpp>
#include <boost/numeric/interval/hw_rounding.hpp>
#include <boost/numeric/interval/rounded_arith.hpp>
#include <algorithm>
#include <array>
#include <cmath>
#include <iomanip>
#include <iostream>
#include <limits>
#include <string>
#include <vector>
#include "mpfr_min.h"

using boost::multiprecision::uint128_t;
namespace bn = boost::numeric;
namespace il = boost::numeric::interval_lib;
using Round = il::save_state<il::rounded_arith_std<long double>>;
using Policies = il::policies<Round, il::checking_strict<long double>>;
using ProtectedI = bn::interval<long double, Policies>;
using I = typename il::unprotect<ProtectedI>::type;

static inline long double lo(const I& x){return x.lower();}
static inline long double hi(const I& x){return x.upper();}
static inline I cube(const I& x){return x*x*x;}
static inline I fourth(const I& x){I y=x*x;return y*y;}
static inline I hull2(const I&a,const I&b){return I(std::min(lo(a),lo(b)),std::max(hi(a),hi(b)));}

struct BaseTrans {
    std::array<I,68> sq{};
    std::array<I,68> lg{};
    I sq_start, lg_start;
    std::string version;
};

static I mpfr_sqrt_ui(unsigned long n){
    mpfr_t x,y; mpfr_init2(x,256); mpfr_init2(y,256);
    mpfr_set_ui(x,n,MPFR_RNDN);
    mpfr_sqrt(y,x,MPFR_RNDD); long double a=mpfr_get_ld(y,MPFR_RNDD);
    mpfr_sqrt(y,x,MPFR_RNDU); long double b=mpfr_get_ld(y,MPFR_RNDU);
    mpfr_clear(y); mpfr_clear(x);
    return I(a,b);
}
static I mpfr_log_ui(unsigned long n){
    if(n==1) return I(0);
    mpfr_t x,y; mpfr_init2(x,256); mpfr_init2(y,256);
    mpfr_set_ui(x,n,MPFR_RNDN);
    mpfr_log(y,x,MPFR_RNDD); long double a=mpfr_get_ld(y,MPFR_RNDD);
    mpfr_log(y,x,MPFR_RNDU); long double b=mpfr_get_ld(y,MPFR_RNDU);
    mpfr_clear(y); mpfr_clear(x);
    return I(a,b);
}
static BaseTrans make_base(){
    BaseTrans b; b.version=mpfr_get_version();
    for(int n=1;n<=67;n++){b.sq[n]=mpfr_sqrt_ui(n);b.lg[n]=mpfr_log_ui(n);}
    b.sq_start=mpfr_sqrt_ui(166000); b.lg_start=mpfr_log_ui(166000);
    // Inclusion self-tests that specifically fail under the old singleton contract.
    for(int n: {2,3,5,61,67,166000}){
        I s=(n==166000?b.sq_start:b.sq[n]);
        I l=(n==166000?b.lg_start:b.lg[n]);
        if(!(lo(s)<hi(s)) || !(lo(l)<hi(l))){
            std::cerr<<"MPFR base enclosure singleton failure n="<<n<<"\n"; std::exit(20);
        }
        long double nn=(long double)n;
        if(!(lo(s)*lo(s)<=nn && hi(s)*hi(s)>=nn)){
            std::cerr<<"sqrt containment failure n="<<n<<"\n"; std::exit(21);
        }
    }
    return b;
}

struct Div{uint128_t key;int mu;I d,sq,inv,lg;};
struct Sums{I A=I(0),B=I(0),C=I(0),D=I(0);};
struct Event{uint128_t x;int type,idx;I sq,lg;};
static bool operator<(Event const&a,Event const&b){if(a.x!=b.x)return a.x<b.x;return a.type<b.type;}
static void add(Sums&s,Div const&d){s.A+=I(1)/d.d;s.B+=d.inv;s.C+=d.lg*d.inv;s.D+=d.d;}

static const I ZH(-1.460355L,-1.460354L);
static const I ZP(-3.922647L,-3.922646L);
struct Co{I A,B,C,D,E,F,G;};
static I val(const Co&q,const I&t,const I&logt){
    return q.A*t*t+q.B*t*logt+q.C*t+q.D*logt+q.E+q.F/(t*t)+q.G/(t*t*t);
}
static I derivative(const Co&q,const I&t,const I&logt){
    return I(2)*q.A*t+q.B*(logt+I(1))+q.C+q.D/t-I(2)*q.F/cube(t)-I(3)*q.G/fourth(t);
}

int main(int argc,char**argv){
    Round guard;
    int JLO=2,JHI=66;if(argc>=2)JLO=std::stoi(argv[1]);if(argc>=3)JHI=std::stoi(argv[2]);
    BaseTrans bt=make_base();
    std::vector<int>P={2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61};
    std::vector<Div> ds={{uint128_t(1),1,I(1),I(1),I(1),I(0)}};
    for(int p:P){size_t n=ds.size();for(size_t i=0;i<n;i++){
        auto a=ds[i];
        ds.push_back({a.key*(unsigned)p,-a.mu,a.d*I(p),a.sq*bt.sq[p],a.inv/bt.sq[p],a.lg+bt.lg[p]});
    }}
    std::sort(ds.begin(),ds.end(),[](auto&a,auto&b){return a.key<b.key;});
    const uint128_t START=166000;
    Sums ce67,co67;for(auto const&d:ds){if(d.key>67)break;(d.mu==1?add(ce67,d):add(co67,d));}
    long double global=1e300L,parentglobal=1e300L,corrglobal=0,derglobal=1e300L,tailpolyglobal=1e300L,tailpolyderglobal=1e300L;
    int gj=0,pgj=0,cgj=0,dgj=0;uint128_t gx=0,pgx=0,cgx=0,dgx=0;
    std::vector<long double> rowfull(67,1e300L),rowfullupper(67,-1e300L),rowparent(67,1e300L),rowder(67,1e300L),rowcorr(67,0);
    std::vector<uint128_t> rowfullx(67),rowparentx(67),rowderx(67),rowcorrx(67);
    unsigned long long unique_events_total=0;
    for(int j=JLO;j<=JHI;j++){
        std::vector<Event> ev;ev.reserve(ds.size()*3);
        auto push=[&](int idx,int type,int m){auto const&d=ds[idx];ev.push_back({d.key*(unsigned)m,type,idx,d.sq*bt.sq[m],d.lg+bt.lg[m]});};
        for(int i=0;i<(int)ds.size();i++){push(i,0,1);push(i,1,j);push(i,2,j+1);}
        std::sort(ev.begin(),ev.end());
        Sums te,to,be,bo;I stripE=I(0),stripO=I(0);size_t k=0;
        I Aj=I(j+1)/I(j-1),Bj=-I((j+1)*(j-2))/I(j*(j-1)),Cj=I(2)/I(j*(j-1));
        I qa=I(4)*Cj,qb=Cj*ZH,qc=Cj*ZP;
        for(int m=1;m<j;m++){qb-=Cj/bt.sq[m];qc+=Cj*bt.lg[m]/bt.sq[m];}
        qb+=(Aj-Cj)/bt.sq[j];qc-=(Aj-Cj)*bt.lg[j]/bt.sq[j];
        qb+=(Bj-Cj)/bt.sq[j+1];qc-=(Bj-Cj)*bt.lg[j+1]/bt.sq[j+1];
        I qstrip=Aj/bt.sq[j]*(bt.lg[j+1]-bt.lg[j]);
        Sums cre,cro;for(auto const&d:ds){if(d.key*(unsigned)j>67)break;(d.mu==1?add(cre,d):add(cro,d));}
        I qchild=(67>j?Aj/bt.sq[j]*(bt.lg[67]-bt.lg[j]):I(0))+I(4)*Cj*bt.sq[67];
        I Et=I(4)*bt.sq[67]*ce67.A,Ot=I(4)*bt.sq[67]*co67.A,Er=qchild*cre.B,Or=qchild*cro.B;
        auto cofun=[&](){
            I Ae=te.A,Ao=to.A,Be=te.B,Bo=to.B;
            I arE=qa*be.A,brE=I(2)*qb*be.B,crE=-qb*be.C+qc*be.B;
            I arO=qa*bo.A,brO=I(2)*qb*bo.B,crO=-qb*bo.C+qc*bo.B+qstrip*stripO;
            I erE=-I(5)*Cj*be.D,erO=I(5)*Cj*bo.D;
            return Co{I(4)*(Ao*arE-Ae*arO),I(4)*(Ao*brE-Ae*brO),I(4)*(Ao*crE-Ae*crO)-I(3)*(Bo*arE-Be*arO),-I(3)*(Bo*brE-Be*brO),-I(3)*(Bo*crE-Be*crO),I(4)*(Ao*erE-Ae*erO),-I(3)*(Bo*erE-Be*erO)};
        };
        auto corr=[&](const I&t,const I&logx){
            I r=bt.sq[67]/t;I ET=I(4)*t*te.A,OT=I(4)*t*to.A;
            I ERP=I(4)*Cj*t*be.A+Aj/bt.sq[j]*be.B*logx+qstrip*stripE;
            I ORP=I(4)*Cj*t*bo.A+Aj/bt.sq[j]*bo.B*logx+qstrip*stripO;
            return r*(Ot*ERP+OT*Er+Et*ORP+ET*Or)+r*r*(Ot*Er+Et*Or);
        };
        auto evaluate=[&](const uint128_t&xx,const I&t,const I&logx){
            I logt=logx/I(2);Co c=cofun();I pv=val(c,t,logt),cv=corr(t,logx),fv=pv-cv;
            long double pl=lo(pv),cu=hi(cv),fl=lo(fv);
            if(pl<rowparent[j]){rowparent[j]=pl;rowparentx[j]=xx;}if(cu>rowcorr[j]){rowcorr[j]=cu;rowcorrx[j]=xx;}if(fl<rowfull[j]){rowfull[j]=fl;rowfullupper[j]=hi(fv);rowfullx[j]=xx;}
            if(pl<parentglobal){parentglobal=pl;pgj=j;pgx=xx;}if(cu>corrglobal){corrglobal=cu;cgj=j;cgx=xx;}if(fl<global){global=fl;gj=j;gx=xx;}
        };
        bool didStart=false; I lastSq,lastLg; uint128_t lastKey=0;
        while(k<ev.size()){
            uint128_t x=ev[k].x;
            I sx=ev[k].sq,lx=ev[k].lg;
            size_t kk=k;while(kk<ev.size()&&ev[kk].x==x){sx=hull2(sx,ev[kk].sq);lx=hull2(lx,ev[kk].lg);kk++;}
            if(!didStart && x>START){evaluate(START,bt.sq_start,bt.lg_start);didStart=true;}
            for(size_t h=k;h<kk;h++){auto&e=ev[h];auto const&d=ds[e.idx];
                if(e.type==0)(d.mu==1?add(te,d):add(to,d));
                else if(e.type==1){if(d.mu==1)stripE+=d.inv;else stripO+=d.inv;}
                else{if(d.mu==1){add(be,d);stripE-=d.inv;}else{add(bo,d);stripO-=d.inv;}}
            }
            k=kk;lastSq=sx;lastLg=lx;lastKey=x;unique_events_total++;
            if(x<START)continue;didStart=true;evaluate(x,sx,lx);Co c=cofun();
            if(k<ev.size()){
                uint128_t nx=ev[k].x;I ns=ev[k].sq,nl=ev[k].lg;size_t nh=k+1;while(nh<ev.size()&&ev[nh].x==nx){ns=hull2(ns,ev[nh].sq);nl=hull2(nl,ev[nh].lg);nh++;}
                if(nx>x){I ti(lo(sx),hi(ns));I logti(lo(lx)/2,hi(nl)/2);I di=derivative(c,ti,logti);long double dl=lo(di);if(dl<rowder[j]){rowder[j]=dl;rowderx[j]=x;}if(dl<derglobal){derglobal=dl;dgj=j;dgx=x;}}
            }
        }
        if(!didStart)evaluate(START,bt.sq_start,bt.lg_start);
        Co tail=cofun();I t0=lastSq;I poly=tail.B*fourth(t0)+I(6)*tail.F*t0+I(12)*tail.G;I polyder=I(4)*tail.B*cube(t0)+I(6)*tail.F;
        if(!(lo(tail.B)>0&&lo(poly)>0&&lo(polyder)>0)){std::cerr<<"tail persistence failure row="<<j<<"\n";return 6;}
        tailpolyglobal=std::min(tailpolyglobal,lo(poly));tailpolyderglobal=std::min(tailpolyderglobal,lo(polyder));
        std::cerr<<std::setprecision(18)<<"ROW "<<j<<" full_lo="<<rowfull[j]<<" x="<<rowfullx[j]<<" parent_lo="<<rowparent[j]<<" px="<<rowparentx[j]<<" corr_hi="<<rowcorr[j]<<" cx="<<rowcorrx[j]<<" der_lo="<<rowder[j]<<" dx="<<rowderx[j]<<"\n";
    }
    if(!(global>26)){std::cerr<<"tail margin failure "<<global<<"\n";return 2;}
    if(!(parentglobal>79)){std::cerr<<"parent margin failure "<<parentglobal<<"\n";return 3;}
    if(!(derglobal>0.23L)){std::cerr<<"derivative margin failure "<<derglobal<<"\n";return 4;}
    long double row66_ref=(JHI>=66&&JLO<=66)?rowfullupper[66]:global; // rigorous upper at the row-66 boundary candidate
    long double separation=1e300L;int sepj=0;
    if(JLO<=65&&JHI>=66){for(int j=JLO;j<66;j++){long double s=rowfull[j]-row66_ref;if(s<separation){separation=s;sepj=j;}}if(!(separation>1)){std::cerr<<"row66 separation failure "<<separation<<" row="<<sepj<<"\n";return 7;}}else separation=0;
    unsigned long long event_records=3ULL*ds.size()*(unsigned long long)(JHI-JLO+1);
    std::cout.precision(24);
    std::cout<<"{\n"
      <<"  \"arithmetic_class\": \"MPFR_256_DIRECTED_BASE_PLUS_BOOST_FENV_BASIC_INTERVAL_UINT128_EVENT_SWEEP\",\n"
      <<"  \"classification\": \"PASS_MPFR_BASE_DIRECTED_TARGET_LORENZ_TAIL_AVLT\",\n"
      <<"  \"mpfr_version\": \""<<bt.version<<"\",\n"
      <<"  \"tail_start\": 166000,\n"
      <<"  \"divisor_count\": "<<ds.size()<<",\n"
      <<"  \"row_count\": "<<(JHI-JLO+1)<<",\n"
      <<"  \"event_records\": "<<event_records<<",\n"
      <<"  \"unique_event_groups\": "<<unique_events_total<<",\n"
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
      <<"  \"rounding_contract\": \"MPFR 256-bit RNDD/RNDU enclosures for sqrt/log of base integers 1..67 and 166000; every event sqrt/log derived only by outward basic interval multiplication/addition; no libm transcendental call in the sweep\",\n"
      <<"  \"rh_established_by_replay\": false\n"
      <<"}\n";
}
