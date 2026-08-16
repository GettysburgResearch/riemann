#pragma STDC FENV_ACCESS ON
#include <boost/version.hpp>
#include <boost/numeric/interval.hpp>
#include <boost/numeric/interval/hw_rounding.hpp>
#include <boost/numeric/interval/rounded_transc.hpp>
#include <boost/numeric/interval/policies.hpp>
#include <iomanip>
#include <iostream>
namespace bn=boost::numeric;
namespace il=boost::numeric::interval_lib;
using Round=il::save_state<il::rounded_transc_std<long double, il::rounded_math<long double>>>;
using Policies=il::policies<Round, il::checking_strict<long double>>;
using ProtectedI=bn::interval<long double,Policies>;
using I=typename il::unprotect<ProtectedI>::type;
int main(){
  Round guard;
  std::cout << "BOOST_VERSION=" << BOOST_LIB_VERSION << "\n";
  for(long double v: {2.0L,3.0L,67.0L,166000.0L}){
    I q(v); I r=sqrt(q); I l=log(q);
    std::cout << std::setprecision(36)
              << "VALUE=" << std::defaultfloat << v
              << " SQRT_LO=" << std::hexfloat << r.lower()
              << " SQRT_HI=" << r.upper()
              << " LOG_LO=" << l.lower()
              << " LOG_HI=" << l.upper()
              << std::defaultfloat
              << " SQRT_WIDTH=" << (r.upper()-r.lower())
              << " LOG_WIDTH=" << (l.upper()-l.lower()) << "\n";
  }
}
