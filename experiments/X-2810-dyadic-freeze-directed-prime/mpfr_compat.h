#ifndef RIEMANN_MPFR_COMPAT_H
#define RIEMANN_MPFR_COMPAT_H
#if defined(__has_include)
#  if __has_include(<mpfr.h>)
#    include <mpfr.h>
#    define RIEMANN_HAVE_SYSTEM_MPFR_H 1
#  endif
#endif
#ifndef RIEMANN_HAVE_SYSTEM_MPFR_H
/* Minimal MPFR 4 ABI declarations for build environments that ship the runtime
   library without development headers. Production builds should prefer the
   official mpfr.h. */
typedef long int mpfr_prec_t;
typedef long int mpfr_exp_t;
typedef unsigned long mp_limb_t;
typedef struct {
  mpfr_prec_t _mpfr_prec;
  int _mpfr_sign;
  mpfr_exp_t _mpfr_exp;
  mp_limb_t *_mpfr_d;
} __mpfr_struct;
typedef __mpfr_struct mpfr_t[1];
typedef __mpfr_struct *mpfr_ptr;
typedef const __mpfr_struct *mpfr_srcptr;
typedef enum {
  MPFR_RNDN=0, MPFR_RNDZ=1, MPFR_RNDU=2,
  MPFR_RNDD=3, MPFR_RNDA=4, MPFR_RNDF=5
} mpfr_rnd_t;
extern void mpfr_init2(mpfr_ptr, mpfr_prec_t);
extern void mpfr_clear(mpfr_ptr);
extern int mpfr_set(mpfr_ptr, mpfr_srcptr, mpfr_rnd_t);
extern int mpfr_set_ui(mpfr_ptr, unsigned long, mpfr_rnd_t);
extern int mpfr_set_si(mpfr_ptr, long, mpfr_rnd_t);
extern int mpfr_set_str(mpfr_ptr, const char*, int, mpfr_rnd_t);
extern int mpfr_set_d(mpfr_ptr, double, mpfr_rnd_t);
extern int mpfr_add(mpfr_ptr, mpfr_srcptr, mpfr_srcptr, mpfr_rnd_t);
extern int mpfr_sub(mpfr_ptr, mpfr_srcptr, mpfr_srcptr, mpfr_rnd_t);
extern int mpfr_mul(mpfr_ptr, mpfr_srcptr, mpfr_srcptr, mpfr_rnd_t);
extern int mpfr_mul_ui(mpfr_ptr, mpfr_srcptr, unsigned long, mpfr_rnd_t);
extern int mpfr_div(mpfr_ptr, mpfr_srcptr, mpfr_srcptr, mpfr_rnd_t);
extern int mpfr_div_2ui(mpfr_ptr, mpfr_srcptr, unsigned long, mpfr_rnd_t);
extern int mpfr_sqrt(mpfr_ptr, mpfr_srcptr, mpfr_rnd_t);
extern int mpfr_log(mpfr_ptr, mpfr_srcptr, mpfr_rnd_t);
extern int mpfr_sin(mpfr_ptr, mpfr_srcptr, mpfr_rnd_t);
extern int mpfr_cos(mpfr_ptr, mpfr_srcptr, mpfr_rnd_t);
extern int mpfr_const_pi(mpfr_ptr, mpfr_rnd_t);
extern int mpfr_cmp(mpfr_srcptr, mpfr_srcptr);
extern int mpfr_cmp_si(mpfr_srcptr, long);
extern long mpfr_get_si(mpfr_srcptr, mpfr_rnd_t);
extern double mpfr_get_d(mpfr_srcptr, mpfr_rnd_t);
#endif
#endif
