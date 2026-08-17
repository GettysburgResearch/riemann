#include "mpfr_min.h"
#include <algorithm>
#include <array>
#include <cstdint>
#include <cstdio>
#include <cstdlib>
#include <string>
#include <utility>
#include <vector>

static constexpr mpfr_prec_t PREC=256;
struct I {
  mpfr_t lo,hi;
  I(){mpfr_init2(lo,PREC);mpfr_init2(hi,PREC);mpfr_set_ui(lo,0,MPFR_RNDN);mpfr_set_ui(hi,0,MPFR_RNDN);}
  I(const I&)=delete; I& operator=(const I&)=delete;
  ~I(){mpfr_clear(lo);mpfr_clear(hi);}
};
static void add_pos(I&sum,const I&t){mpfr_add(sum.lo,sum.lo,t.lo,MPFR_RNDD);mpfr_add(sum.hi,sum.hi,t.hi,MPFR_RNDU);}
static void add_neg(I&sum,const I&t){mpfr_sub(sum.lo,sum.lo,t.hi,MPFR_RNDD);mpfr_sub(sum.hi,sum.hi,t.lo,MPFR_RNDU);}
static int qstar(unsigned m){if(m==2)return 15;if(m==3)return 6;if(m==4)return 3;if(m>=5)return 6;return 0;}
static std::vector<std::pair<unsigned long,int>> divisors(unsigned long lim){
  static const unsigned ps[]={2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61};
  std::vector<std::pair<unsigned long,int>> a{{1,1}};
  for(unsigned p:ps){size_t z=a.size(); for(size_t i=0;i<z;i++){auto [d,s]=a[i]; if(d<=lim/p)a.push_back({d*p,-s});}}
  std::sort(a.begin(),a.end()); return a;
}
static void term_interval(I&out,unsigned X,unsigned long n,unsigned q,const I&log4){
  mpfr_t nn,xx,ratlo,rathi,hlo,hhi,slo,shi,tmp;
  for(auto *v:{nn,xx,ratlo,rathi,hlo,hhi,slo,shi,tmp})mpfr_init2(v,PREC);
  mpfr_set_ui(nn,n,MPFR_RNDN); mpfr_set_ui(xx,X,MPFR_RNDN);
  mpfr_sqrt(slo,nn,MPFR_RNDD); mpfr_sqrt(shi,nn,MPFR_RNDU);
  if(4*n<=X){mpfr_set(hlo,log4.lo,MPFR_RNDD);mpfr_set(hhi,log4.hi,MPFR_RNDU);}else{
    mpfr_div(ratlo,xx,nn,MPFR_RNDD); mpfr_div(rathi,xx,nn,MPFR_RNDU);
    mpfr_log(hlo,ratlo,MPFR_RNDD); mpfr_log(hhi,rathi,MPFR_RNDU);
  }
  mpfr_mul_ui(tmp,hlo,q,MPFR_RNDD); mpfr_div(out.lo,tmp,shi,MPFR_RNDD);
  mpfr_mul_ui(tmp,hhi,q,MPFR_RNDU); mpfr_div(out.hi,tmp,slo,MPFR_RNDU);
  for(auto *v:{nn,xx,ratlo,rathi,hlo,hhi,slo,shi,tmp})mpfr_clear(v);
}
static std::string fmt(mpfr_srcptr x){char b[256];mpfr_snprintf(b,sizeof(b),"%.70RNf",x);return b;}
int main(){
  const unsigned X=184;
  I log4; mpfr_t four; mpfr_init2(four,PREC); mpfr_set_ui(four,4,MPFR_RNDN);
  mpfr_log(log4.lo,four,MPFR_RNDD);mpfr_log(log4.hi,four,MPFR_RNDU);mpfr_clear(four);
  I F,M,t;
  auto ds=divisors(X/2);
  unsigned terms=0;
  for(auto [d,sgn]:ds){
    for(unsigned m=2;d*m<=X;m++){
      int q=qstar(m); if(!q)continue; term_interval(t,X,d*m,q,log4);
      add_pos(M,t); if(sgn>0)add_pos(F,t);else add_neg(F,t); terms++;
    }
  }
  mpfr_t e40lo,e40hi,e50lo,e20hi,tmp,ratio_lo,ratio_hi;
  for(auto *v:{e40lo,e40hi,e50lo,e20hi,tmp,ratio_lo,ratio_hi})mpfr_init2(v,PREC);
  mpfr_mul_ui(tmp,F.lo,40,MPFR_RNDD);mpfr_sub(e40lo,tmp,M.hi,MPFR_RNDD);
  mpfr_mul_ui(tmp,F.hi,40,MPFR_RNDU);mpfr_sub(e40hi,tmp,M.lo,MPFR_RNDU);
  mpfr_mul_ui(tmp,F.lo,50,MPFR_RNDD);mpfr_sub(e50lo,tmp,M.hi,MPFR_RNDD);
  mpfr_mul_ui(tmp,F.hi,20,MPFR_RNDU);mpfr_sub(e20hi,tmp,M.lo,MPFR_RNDU);
  mpfr_div(ratio_lo,F.lo,M.hi,MPFR_RNDD);mpfr_div(ratio_hi,F.hi,M.lo,MPFR_RNDU);
  bool pass=mpfr_cmp_si(e40hi,0)<0 && mpfr_cmp_si(e50lo,0)>0 && mpfr_cmp_si(e20hi,0)<0;
  std::printf("{\n");
  std::printf("  \"schema\": \"riemann.x97350.bias-x184.mpfr.v1\",\n");
  std::printf("  \"mpfr_version\": \"%s\",\n",mpfr_get_version());
  std::printf("  \"precision_bits\": 256,\n  \"X\": 184,\n  \"terms\": %u,\n",terms);
  std::printf("  \"F_interval\": [\"%s\", \"%s\"],\n",fmt(F.lo).c_str(),fmt(F.hi).c_str());
  std::printf("  \"M_interval\": [\"%s\", \"%s\"],\n",fmt(M.lo).c_str(),fmt(M.hi).c_str());
  std::printf("  \"ratio_interval\": [\"%s\", \"%s\"],\n",fmt(ratio_lo).c_str(),fmt(ratio_hi).c_str());
  std::printf("  \"40F_minus_M_interval\": [\"%s\", \"%s\"],\n",fmt(e40lo).c_str(),fmt(e40hi).c_str());
  std::printf("  \"50F_minus_M_lower\": \"%s\",\n",fmt(e50lo).c_str());
  std::printf("  \"20F_minus_M_upper\": \"%s\",\n",fmt(e20hi).c_str());
  std::printf("  \"verdict\": \"%s\"\n}\n",pass?"PASS_DIRECTED_COUNTEREXAMPLE_TO_ONE_OVER_40":"FAIL");
  for(auto *v:{e40lo,e40hi,e50lo,e20hi,tmp,ratio_lo,ratio_hi})mpfr_clear(v);
  return pass?0:2;
}
