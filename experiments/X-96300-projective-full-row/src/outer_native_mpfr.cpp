#pragma STDC FENV_ACCESS ON
#include <boost/numeric/interval.hpp>
#include <boost/numeric/interval/hw_rounding.hpp>
#include <boost/numeric/interval/rounded_arith.hpp>
#include <cmath>
#include <iostream>
#include <iomanip>
#include <vector>
#include "mpfr_min.h"
namespace bn=boost::numeric; namespace il=boost::numeric::interval_lib;
using Round=il::save_state<il::rounded_arith_std<long double>>;
using Policies=il::policies<Round,il::checking_strict<long double>>;
using PI=bn::interval<long double,Policies>; using I=typename il::unprotect<PI>::type;
static I sq_ui(unsigned long n){mpfr_t x,y;mpfr_init2(x,256);mpfr_init2(y,256);mpfr_set_ui(x,n,MPFR_RNDN);mpfr_sqrt(y,x,MPFR_RNDD);auto a=mpfr_get_ld(y,MPFR_RNDD);mpfr_sqrt(y,x,MPFR_RNDU);auto b=mpfr_get_ld(y,MPFR_RNDU);mpfr_clear(y);mpfr_clear(x);return I(a,b);}
static I lg_ui(unsigned long n){if(n==1)return I(0);mpfr_t x,y;mpfr_init2(x,256);mpfr_init2(y,256);mpfr_set_ui(x,n,MPFR_RNDN);mpfr_log(y,x,MPFR_RNDD);auto a=mpfr_get_ld(y,MPFR_RNDD);mpfr_log(y,x,MPFR_RNDU);auto b=mpfr_get_ld(y,MPFR_RNDU);mpfr_clear(y);mpfr_clear(x);return I(a,b);}
static int mobius(int n){int mu=1;for(int p=2;p*p<=n;p++)if(n%p==0){n/=p;mu=-mu;if(n%p==0)return 0;while(n%p==0)n/=p;}if(n>1)mu=-mu;return mu;}
static I qcoef(int j,int m){if(m<j)return I(0);if(m==j)return I(j+1)/I(j-1);if(m==j+1)return -I((j+1)*(j-2))/I(j*(j-1));return I(2)/I(j*(j-1));}
int main(){Round guard;std::vector<I> sq(68),lg(68);for(int n=1;n<=67;n++){sq[n]=sq_ui(n);lg[n]=lg_ui(n);} long double minlo=1e300L;int minN=0,minj=0;unsigned checks=0;
 for(int N=1;N<=67;N++)for(int j=2;j<=66;j++){
  I c(0);for(int k=1;k<=N/j;k++){int mu=mobius(k);if(!mu)continue;for(int m=j;k*m<=N;m++){I qc=qcoef(j,m);if(qc.lower()==0&&qc.upper()==0)continue;int n=k*m;I term=I(mu)*qc/sq[n]*(lg[N]-lg[n]);c+=term;}}
  if(N<=j){if(c.lower()<-1e-18L){std::cerr<<"triangular fail";return 2;}}
  else {if(c.lower()<=0){std::cerr<<std::setprecision(24)<<"nonpositive N="<<N<<" j="<<j<<" ["<<c.lower()<<","<<c.upper()<<"]\n";return 3;} if(c.lower()<minlo){minlo=c.lower();minN=N;minj=j;}}
  checks++;
 }
 std::cout<<std::setprecision(24)<<"{\n  \"classification\": \"PASS_MPFR_DIRECTED_OUTER_NATIVE_ROW_1_TO_67\",\n  \"mpfr_version\": \""<<mpfr_get_version()<<"\",\n  \"endpoint_row_checks\": "<<checks<<",\n  \"minimum_positive_lower_bound\": \""<<minlo<<"\",\n  \"minimum_endpoint\": "<<minN<<",\n  \"minimum_row\": "<<minj<<",\n  \"cell_argument\": \"on each [N,N+1], c_X(j) is affine in log X; endpoint positivity covers the full real cell\",\n  \"rh_established_by_replay\": false\n}\n";
}
