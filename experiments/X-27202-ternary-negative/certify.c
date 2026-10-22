#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
#include <gmp.h>

typedef long mpfr_prec_t;
typedef long mpfr_exp_t;
typedef struct { mpfr_prec_t _mpfr_prec; int _mpfr_sign; mpfr_exp_t _mpfr_exp; mp_limb_t *_mpfr_d; } __mpfr_struct;
typedef __mpfr_struct mpfr_t[1];
typedef const __mpfr_struct *mpfr_srcptr;
typedef __mpfr_struct *mpfr_ptr;
extern void mpfr_init2(mpfr_ptr, mpfr_prec_t);
extern void mpfr_clear(mpfr_ptr);
extern int mpfr_set_ui(mpfr_ptr, unsigned long, int);
extern int mpfr_set_si(mpfr_ptr, long, int);
extern int mpfr_set(mpfr_ptr, mpfr_srcptr, int);
extern int mpfr_add(mpfr_ptr, mpfr_srcptr, mpfr_srcptr, int);
extern int mpfr_sub(mpfr_ptr, mpfr_srcptr, mpfr_srcptr, int);
extern int mpfr_mul(mpfr_ptr, mpfr_srcptr, mpfr_srcptr, int);
extern int mpfr_mul_si(mpfr_ptr, mpfr_srcptr, long, int);
extern int mpfr_div(mpfr_ptr, mpfr_srcptr, mpfr_srcptr, int);
extern int mpfr_div_ui(mpfr_ptr, mpfr_srcptr, unsigned long, int);
extern int mpfr_ui_div(mpfr_ptr, unsigned long, mpfr_srcptr, int);
extern int mpfr_sqrt(mpfr_ptr, mpfr_srcptr, int);
extern int mpfr_log(mpfr_ptr, mpfr_srcptr, int);
extern int mpfr_neg(mpfr_ptr, mpfr_srcptr, int);
extern int mpfr_cmp(mpfr_srcptr, mpfr_srcptr);
extern int mpfr_cmp_ui(mpfr_srcptr, unsigned long);
extern long double mpfr_get_ld(mpfr_srcptr, int);
extern size_t __gmpfr_out_str(FILE*, int, size_t, mpfr_srcptr, int);

#define RNDN 0
#define RNDZ 1
#define RNDU 2
#define RNDD 3
#define RNDA 4

typedef struct { mpfr_t lo; mpfr_t hi; } iv;
#ifndef CERT_PREC
#define CERT_PREC 512
#endif
static mpfr_prec_t PREC=CERT_PREC;

static void iv_init(iv *x){mpfr_init2(x->lo,PREC);mpfr_init2(x->hi,PREC);} 
static void iv_clear(iv *x){mpfr_clear(x->lo);mpfr_clear(x->hi);} 
static void iv_zero(iv *x){mpfr_set_ui(x->lo,0,RNDN);mpfr_set_ui(x->hi,0,RNDN);} 
static void iv_set(iv *z,const iv *x){mpfr_set(z->lo,x->lo,RNDD);mpfr_set(z->hi,x->hi,RNDU);} 
static void iv_set_ui(iv *x,unsigned long a){mpfr_set_ui(x->lo,a,RNDN);mpfr_set_ui(x->hi,a,RNDN);} 
static void iv_add(iv *z,const iv *a,const iv *b){mpfr_add(z->lo,a->lo,b->lo,RNDD);mpfr_add(z->hi,a->hi,b->hi,RNDU);} 
static void iv_sub(iv *z,const iv *a,const iv *b){mpfr_sub(z->lo,a->lo,b->hi,RNDD);mpfr_sub(z->hi,a->hi,b->lo,RNDU);} 
static void iv_neg(iv *z,const iv *a){mpfr_neg(z->lo,a->hi,RNDD);mpfr_neg(z->hi,a->lo,RNDU);} 
static void minset(mpfr_ptr z, mpfr_srcptr x){if(mpfr_cmp(x,z)<0)mpfr_set(z,x,RNDD);} 
static void maxset(mpfr_ptr z, mpfr_srcptr x){if(mpfr_cmp(x,z)>0)mpfr_set(z,x,RNDU);} 
static void iv_mul(iv *z,const iv *a,const iv *b){
  mpfr_t t; mpfr_init2(t,PREC);
  mpfr_mul(z->lo,a->lo,b->lo,RNDD);
  mpfr_mul(t,a->lo,b->hi,RNDD); minset(z->lo,t);
  mpfr_mul(t,a->hi,b->lo,RNDD); minset(z->lo,t);
  mpfr_mul(t,a->hi,b->hi,RNDD); minset(z->lo,t);
  mpfr_mul(z->hi,a->lo,b->lo,RNDU);
  mpfr_mul(t,a->lo,b->hi,RNDU); maxset(z->hi,t);
  mpfr_mul(t,a->hi,b->lo,RNDU); maxset(z->hi,t);
  mpfr_mul(t,a->hi,b->hi,RNDU); maxset(z->hi,t);
  mpfr_clear(t);
}
static void iv_mul_si(iv *z,const iv *a,long k){
  if(k>=0){mpfr_mul_si(z->lo,a->lo,k,RNDD);mpfr_mul_si(z->hi,a->hi,k,RNDU);} 
  else {mpfr_mul_si(z->lo,a->hi,k,RNDD);mpfr_mul_si(z->hi,a->lo,k,RNDU);} 
}
static void iv_sqrt_ui(iv *z,unsigned long a){mpfr_set_ui(z->lo,a,RNDN);mpfr_sqrt(z->lo,z->lo,RNDD);mpfr_set_ui(z->hi,a,RNDN);mpfr_sqrt(z->hi,z->hi,RNDU);} 
static void iv_inv_pos(iv *z,const iv *a){mpfr_ui_div(z->lo,1,a->hi,RNDD);mpfr_ui_div(z->hi,1,a->lo,RNDU);} 
static void iv_invsqrt_ui(iv *z,unsigned long a){iv t;iv_init(&t);iv_sqrt_ui(&t,a);iv_inv_pos(z,&t);iv_clear(&t);} 
static void iv_log_ui(iv *z,unsigned long a){mpfr_set_ui(z->lo,a,RNDN);mpfr_log(z->lo,z->lo,RNDD);mpfr_set_ui(z->hi,a,RNDN);mpfr_log(z->hi,z->hi,RNDU);} 
static void iv_log_ratio_ui(iv *z,unsigned long a,unsigned long b){
  mpfr_set_ui(z->lo,a,RNDN);mpfr_div_ui(z->lo,z->lo,b,RNDD);mpfr_log(z->lo,z->lo,RNDD);
  mpfr_set_ui(z->hi,a,RNDN);mpfr_div_ui(z->hi,z->hi,b,RNDU);mpfr_log(z->hi,z->hi,RNDU);
}
static void iv_print(const char *name,const iv *x){
  printf("%s_lo=",name); __gmpfr_out_str(stdout,10,0,x->lo,RNDD); printf("\n");
  printf("%s_hi=",name); __gmpfr_out_str(stdout,10,0,x->hi,RNDU); printf("\n");
  printf("%s_ld=[%.21Le, %.21Le]\n",name,mpfr_get_ld(x->lo,RNDD),mpfr_get_ld(x->hi,RNDU));
}

static int *mobius_sieve(int N){
  int *mu=calloc(N+1,sizeof(int)); int *lp=calloc(N+1,sizeof(int)); int *pr=malloc((N+1)*sizeof(int)); int pc=0;
  if(!mu||!lp||!pr){fprintf(stderr,"alloc fail\n");exit(2);} mu[1]=1;
  for(int i=2;i<=N;i++){
    if(lp[i]==0){lp[i]=i;pr[pc++]=i;mu[i]=-1;}
    for(int z=0;z<pc;z++){int p=pr[z]; long long v=(long long)i*p; if(v>N)break; lp[v]=p; if(p==lp[i]){mu[v]=0;break;} else mu[v]=-mu[i];}
  }
  free(lp);free(pr);return mu;
}

int main(int argc,char **argv){
  const int X=10000000; const int n0=63; const int YMAX=X/n0;
  int *mu=mobius_sieve(YMAX);
  iv *P0=malloc((YMAX+1)*sizeof(iv)); iv *P1=malloc((YMAX+1)*sizeof(iv));
  if(!P0||!P1){fprintf(stderr,"P alloc fail\n");return 2;}
  for(int i=0;i<=YMAX;i++){iv_init(&P0[i]);iv_init(&P1[i]);}
  iv_zero(&P0[0]);iv_zero(&P1[0]);
  iv invs,logk,term0,term1,tmp;
  iv_init(&invs);iv_init(&logk);iv_init(&term0);iv_init(&term1);iv_init(&tmp);
  for(int k=1;k<=YMAX;k++){
    iv_invsqrt_ui(&invs,k); iv_log_ui(&logk,k); iv_mul(&term1,&logk,&invs); iv_set(&term0,&invs);
    if(mu[k]<0){iv_neg(&tmp,&term0);iv_set(&term0,&tmp);iv_neg(&tmp,&term1);iv_set(&term1,&tmp);} else if(mu[k]==0){iv_zero(&term0);iv_zero(&term1);} 
    iv_add(&P0[k],&P0[k-1],&term0); iv_add(&P1[k],&P1[k-1],&term1);
  }
  int32_t *c=calloc((size_t)X+1,sizeof(int32_t)); if(!c){fprintf(stderr,"c alloc fail\n");return 2;} c[n0]=1;
  for(int m=n0+1;m<=X;m++){int a=(m+2)/3,b=m-a; long long v=(long long)c[a]+c[b]; if(v>INT32_MAX){fprintf(stderr,"overflow\n");return 3;} c[m]=(int32_t)v;}
  iv sum,lr,br,im,u,scaled;
  iv_init(&sum);iv_init(&lr);iv_init(&br);iv_init(&im);iv_init(&u);iv_init(&scaled);iv_zero(&sum);
  long long nz=0; int32_t prev=0; long long maxc=0;
  for(int m=n0;m<=X;m++){
    int32_t cm=c[m]; if(cm>maxc)maxc=cm; long diff=(long)cm-(long)prev; prev=cm; if(diff==0)continue; nz++;
    int y=X/m;
    iv_log_ratio_ui(&lr,X,m);
    iv_mul(&br,&lr,&P0[y]);
    iv_sub(&br,&br,&P1[y]);
    iv_invsqrt_ui(&im,m);
    iv_mul(&u,&br,&im);
    iv_mul_si(&scaled,&u,diff);
    iv_add(&sum,&sum,&scaled);
  }
  printf("X=%d n=%d YMAX=%d nonzero_diffs=%lld max_c=%lld\n",X,n0,YMAX,nz,maxc);
  iv_print("A63",&sum);
  int neg = mpfr_cmp_ui(sum.hi,0)<0;
  printf("CERTIFIED_NEGATIVE=%s\n",neg?"YES":"NO");
  return neg?0:1;
}
