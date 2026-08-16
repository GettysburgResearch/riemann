#include <boost/numeric/interval.hpp>
#include <iomanip>
#include <iostream>
#include "mpfr_interval.hpp"
using I=boost::numeric::interval<long double>;
int main(){
  I two(2.0L),three(3.0L);
  I a=mpfr_sqrt_interval(two);
  I b=mpfr_log_interval(three);
  std::cout<<std::setprecision(30)
           <<a.lower()<<" "<<a.upper()<<"\n"
           <<b.lower()<<" "<<b.upper()<<"\n";
  if(!(a.lower()<a.upper() && b.lower()<b.upper())) return 2;
  return 0;
}
