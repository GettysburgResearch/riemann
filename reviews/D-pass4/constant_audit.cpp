// Isolate the serialization issue with a fresh 256-bit directed C0 enclosure.
#include "mpfr_abi.h"
#include <vector>
#include <iostream>
extern "C" {
int mpfr_add(mpfr_ptr,mpfr_srcptr,mpfr_srcptr,mpfr_rnd_t);
int mpfr_sub(mpfr_ptr,mpfr_srcptr,mpfr_srcptr,mpfr_rnd_t);
int mpfr_mul(mpfr_ptr,mpfr_srcptr,mpfr_srcptr,mpfr_rnd_t);
int mpfr_mul_ui(mpfr_ptr,mpfr_srcptr,unsigned long,mpfr_rnd_t);
}
int main(){mpfr_t s,zl,zu,rl,ru,ll,lu,l,h,c;mpz_t n;mpz_init(n);
 for(auto p:{s,zl,zu,rl,ru,ll,lu,l,h,c})mpfr_init2(p,256);
 mpfr_set_ui(s,1,MPFR_RNDN);mpfr_div_ui(s,s,2,MPFR_RNDN);
 mpfr_zeta(zl,s,MPFR_RNDD);mpfr_zeta(zu,s,MPFR_RNDU);
 mpfr_set_ui(s,2,MPFR_RNDN);mpfr_sqrt(rl,s,MPFR_RNDD);mpfr_sqrt(ru,s,MPFR_RNDU);
 mpfr_ui_div(l,9,ru,MPFR_RNDD);mpfr_ui_div(h,9,rl,MPFR_RNDU);
 mpfr_mul_ui(zl,zl,6,MPFR_RNDD);mpfr_mul_ui(zu,zu,6,MPFR_RNDU);
 mpfr_add(l,l,zl,MPFR_RNDD);mpfr_add(h,h,zu,MPFR_RNDU);
 mpfr_set_ui(c,15,MPFR_RNDN);mpfr_div_ui(c,c,2,MPFR_RNDN);
 mpfr_sub(l,l,c,MPFR_RNDD);mpfr_sub(h,h,c,MPFR_RNDU);
 mpfr_set_ui(s,4,MPFR_RNDN);mpfr_log(ll,s,MPFR_RNDD);mpfr_log(lu,s,MPFR_RNDU);
 // Both l,h are negative; the outer log endpoints reverse here.
 mpfr_mul(l,l,lu,MPFR_RNDD);mpfr_mul(h,h,ll,MPFR_RNDU);
 std::cout<<"{\"schema\":\"reviewer-D.C0.directed.v1\",\"denominator_exponent\":200,\"numerators\":[";
 int j=0;for(auto p:{l,h}){auto r=j?MPFR_RNDU:MPFR_RNDD;mpfr_mul_2ui(p,p,200,r);mpfr_get_z(n,p,r);std::vector<char>b(mpz_sizeinbase(n,10)+4);mpz_get_str(b.data(),10,n);std::cout<<'"'<<b.data()<<'"'<<(j++?"":",");}
 std::cout<<"]}\n";mpz_clear(n);for(auto p:{s,zl,zu,rl,ru,ll,lu,l,h,c})mpfr_clear(p);
}
