// Minimal public MPFR ABI declarations. Use the installed vendor header if available.
#pragma once
#if __has_include(<mpfr.h>)
#include <mpfr.h>
#else
#include <gmp.h>
extern "C" {
typedef long mpfr_prec_t; typedef long mpfr_exp_t;
typedef enum { MPFR_RNDN=0,MPFR_RNDZ=1,MPFR_RNDU=2,MPFR_RNDD=3,MPFR_RNDA=4,MPFR_RNDF=5 } mpfr_rnd_t;
typedef struct {mpfr_prec_t _mpfr_prec;int _mpfr_sign;mpfr_exp_t _mpfr_exp;mp_limb_t *_mpfr_d;} __mpfr_struct;
typedef __mpfr_struct mpfr_t[1];typedef __mpfr_struct* mpfr_ptr;typedef const __mpfr_struct* mpfr_srcptr;
void mpfr_init2(mpfr_ptr,mpfr_prec_t);void mpfr_clear(mpfr_ptr);
int mpfr_set_ui(mpfr_ptr,unsigned long,mpfr_rnd_t);int mpfr_set_str(mpfr_ptr,const char*,int,mpfr_rnd_t);
int mpfr_div_ui(mpfr_ptr,mpfr_srcptr,unsigned long,mpfr_rnd_t);int mpfr_ui_div(mpfr_ptr,unsigned long,mpfr_srcptr,mpfr_rnd_t);
int mpfr_mul_2ui(mpfr_ptr,mpfr_srcptr,unsigned long,mpfr_rnd_t);int mpfr_sqrt(mpfr_ptr,mpfr_srcptr,mpfr_rnd_t);
int mpfr_log(mpfr_ptr,mpfr_srcptr,mpfr_rnd_t);int mpfr_zeta(mpfr_ptr,mpfr_srcptr,mpfr_rnd_t);
int mpfr_div(mpfr_ptr,mpfr_srcptr,mpfr_srcptr,mpfr_rnd_t);long mpfr_get_si(mpfr_srcptr,mpfr_rnd_t);
int mpfr_get_z(mpz_ptr,mpfr_srcptr,mpfr_rnd_t);const char*mpfr_get_version(void);
}
#endif
