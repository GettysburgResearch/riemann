#ifndef RIEMANN_X17801_MPFR_MIN_H
#define RIEMANN_X17801_MPFR_MIN_H
#include <gmp.h>
typedef long mpfr_prec_t;
typedef long mpfr_exp_t;
typedef int mpfr_sign_t;
typedef struct { mpfr_prec_t _mpfr_prec; mpfr_sign_t _mpfr_sign; mpfr_exp_t _mpfr_exp; mp_limb_t *_mpfr_d; } __mpfr_struct;
typedef __mpfr_struct mpfr_t[1];
typedef __mpfr_struct *mpfr_ptr;
typedef const __mpfr_struct *mpfr_srcptr;
typedef enum { MPFR_RNDN=0, MPFR_RNDZ=1, MPFR_RNDU=2, MPFR_RNDD=3, MPFR_RNDA=4, MPFR_RNDF=5, MPFR_RNDNA=-1 } mpfr_rnd_t;
extern void mpfr_init2(mpfr_ptr, mpfr_prec_t);
extern void mpfr_clear(mpfr_ptr);
extern int mpfr_set(mpfr_ptr,mpfr_srcptr,mpfr_rnd_t);
extern int mpfr_set_ui(mpfr_ptr,unsigned long,mpfr_rnd_t);
extern int mpfr_set_si(mpfr_ptr,long,mpfr_rnd_t);
extern int mpfr_set_str(mpfr_ptr,const char*,int,mpfr_rnd_t);
extern int mpfr_const_pi(mpfr_ptr,mpfr_rnd_t);
extern int mpfr_add(mpfr_ptr,mpfr_srcptr,mpfr_srcptr,mpfr_rnd_t);
extern int mpfr_sub(mpfr_ptr,mpfr_srcptr,mpfr_srcptr,mpfr_rnd_t);
extern int mpfr_add_ui(mpfr_ptr,mpfr_srcptr,unsigned long,mpfr_rnd_t);
extern int mpfr_sub_ui(mpfr_ptr,mpfr_srcptr,unsigned long,mpfr_rnd_t);
extern int mpfr_sub_si(mpfr_ptr,mpfr_srcptr,long,mpfr_rnd_t);
extern int mpfr_ui_sub(mpfr_ptr,unsigned long,mpfr_srcptr,mpfr_rnd_t);
extern int mpfr_mul(mpfr_ptr,mpfr_srcptr,mpfr_srcptr,mpfr_rnd_t);
extern int mpfr_div(mpfr_ptr,mpfr_srcptr,mpfr_srcptr,mpfr_rnd_t);
extern int mpfr_mul_ui(mpfr_ptr,mpfr_srcptr,unsigned long,mpfr_rnd_t);
extern int mpfr_div_ui(mpfr_ptr,mpfr_srcptr,unsigned long,mpfr_rnd_t);
extern int mpfr_div_si(mpfr_ptr,mpfr_srcptr,long,mpfr_rnd_t);
extern int mpfr_ui_div(mpfr_ptr,unsigned long,mpfr_srcptr,mpfr_rnd_t);
extern int mpfr_mul_2si(mpfr_ptr,mpfr_srcptr,long,mpfr_rnd_t);
extern int mpfr_div_2si(mpfr_ptr,mpfr_srcptr,long,mpfr_rnd_t);
extern int mpfr_neg(mpfr_ptr,mpfr_srcptr,mpfr_rnd_t);
extern int mpfr_abs(mpfr_ptr,mpfr_srcptr,mpfr_rnd_t);
extern int mpfr_log(mpfr_ptr,mpfr_srcptr,mpfr_rnd_t);
extern int mpfr_sqrt(mpfr_ptr,mpfr_srcptr,mpfr_rnd_t);
extern int mpfr_sin(mpfr_ptr,mpfr_srcptr,mpfr_rnd_t);
extern int mpfr_cos(mpfr_ptr,mpfr_srcptr,mpfr_rnd_t);
extern int mpfr_sqr(mpfr_ptr,mpfr_srcptr,mpfr_rnd_t);
extern int mpfr_cmp(mpfr_srcptr,mpfr_srcptr);
extern int mpfr_cmp_ui(mpfr_srcptr,unsigned long);
extern long mpfr_get_si(mpfr_srcptr,mpfr_rnd_t);
extern int mpfr_printf(const char*,...);
#endif
