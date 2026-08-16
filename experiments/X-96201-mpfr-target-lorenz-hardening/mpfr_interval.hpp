#pragma once
#include <mpfr.h>
#include <boost/numeric/interval.hpp>

template<class Interval>
static Interval mpfr_sqrt_interval(const Interval& x) {
    mpfr_t a,b,r;
    mpfr_init2(a,256); mpfr_init2(b,256); mpfr_init2(r,256);
    mpfr_set_ld(a,x.lower(),MPFR_RNDN);
    mpfr_set_ld(b,x.upper(),MPFR_RNDN);
    mpfr_sqrt(r,a,MPFR_RNDD);
    long double lo=mpfr_get_ld(r,MPFR_RNDD);
    mpfr_sqrt(r,b,MPFR_RNDU);
    long double hi=mpfr_get_ld(r,MPFR_RNDU);
    mpfr_clear(a); mpfr_clear(b); mpfr_clear(r);
    return Interval(lo,hi);
}

template<class Interval>
static Interval mpfr_log_interval(const Interval& x) {
    mpfr_t a,b,r;
    mpfr_init2(a,256); mpfr_init2(b,256); mpfr_init2(r,256);
    mpfr_set_ld(a,x.lower(),MPFR_RNDN);
    mpfr_set_ld(b,x.upper(),MPFR_RNDN);
    mpfr_log(r,a,MPFR_RNDD);
    long double lo=mpfr_get_ld(r,MPFR_RNDD);
    mpfr_log(r,b,MPFR_RNDU);
    long double hi=mpfr_get_ld(r,MPFR_RNDU);
    mpfr_clear(a); mpfr_clear(b); mpfr_clear(r);
    return Interval(lo,hi);
}
