#ifndef MPFR_MIN_H
#define MPFR_MIN_H
#include <gmp.h>
#ifdef __cplusplus
extern "C" {
#endif
typedef long mpfr_prec_t;
typedef int mpfr_sign_t;
typedef long mpfr_exp_t;
typedef enum {MPFR_RNDN=0,MPFR_RNDZ=1,MPFR_RNDU=2,MPFR_RNDD=3,MPFR_RNDA=4,MPFR_RNDF=5,MPFR_RNDNA=-1} mpfr_rnd_t;
typedef struct {mpfr_prec_t _mpfr_prec; mpfr_sign_t _mpfr_sign; mpfr_exp_t _mpfr_exp; mp_limb_t *_mpfr_d;} __mpfr_struct;
typedef __mpfr_struct mpfr_t[1];
typedef __mpfr_struct *mpfr_ptr;
typedef const __mpfr_struct *mpfr_srcptr;
void mpfr_init2(mpfr_ptr, mpfr_prec_t);
void mpfr_clear(mpfr_ptr);
int mpfr_set_ui(mpfr_ptr, unsigned long, mpfr_rnd_t);
int mpfr_sqrt(mpfr_ptr, mpfr_srcptr, mpfr_rnd_t);
int mpfr_ui_div(mpfr_ptr, unsigned long, mpfr_srcptr, mpfr_rnd_t);
int mpfr_log(mpfr_ptr, mpfr_srcptr, mpfr_rnd_t);
long double mpfr_get_ld(mpfr_srcptr, mpfr_rnd_t);
#ifdef __cplusplus
}
#endif
#endif
