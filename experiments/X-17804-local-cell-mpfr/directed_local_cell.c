#define _GNU_SOURCE
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <stdbool.h>
#include <string.h>
#include <math.h>
#include <gmp.h>

#include <mpfr.h>

typedef struct { mpfr_t lo, hi; } iv;
static mpfr_prec_t PREC = 384;
static void iv_init(iv *x){ mpfr_init2(x->lo,PREC); mpfr_init2(x->hi,PREC); }
static void iv_clear(iv *x){ mpfr_clear(x->lo); mpfr_clear(x->hi); }
static void iv_zero(iv *x){ mpfr_set_ui(x->lo,0,MPFR_RNDD); mpfr_set_ui(x->hi,0,MPFR_RNDU); }
static void iv_copy(iv *z,const iv*a){ mpfr_set(z->lo,a->lo,MPFR_RNDD); mpfr_set(z->hi,a->hi,MPFR_RNDU); }
static void iv_set_q(iv*x,const mpq_t q){ mpfr_set_q(x->lo,q,MPFR_RNDD); mpfr_set_q(x->hi,q,MPFR_RNDU); }
static void iv_set_ui(iv*x,unsigned long u){ mpfr_set_ui(x->lo,u,MPFR_RNDD); mpfr_set_ui(x->hi,u,MPFR_RNDU); }
static void iv_add(iv*z,const iv*a,const iv*b){ mpfr_add(z->lo,a->lo,b->lo,MPFR_RNDD); mpfr_add(z->hi,a->hi,b->hi,MPFR_RNDU); }
static void iv_sub(iv*z,const iv*a,const iv*b){ mpfr_sub(z->lo,a->lo,b->hi,MPFR_RNDD); mpfr_sub(z->hi,a->hi,b->lo,MPFR_RNDU); }
static void iv_mul(iv*z,const iv*a,const iv*b){
    mpfr_t dl[4],du[4]; for(int i=0;i<4;i++){mpfr_init2(dl[i],PREC);mpfr_init2(du[i],PREC);} 
    const __mpfr_struct *av[2]={a->lo,a->hi}, *bv[2]={b->lo,b->hi}; int n=0;
    for(int i=0;i<2;i++)for(int j=0;j<2;j++){mpfr_mul(dl[n],av[i],bv[j],MPFR_RNDD);mpfr_mul(du[n],av[i],bv[j],MPFR_RNDU);n++;}
    int il=0,iu=0; for(int i=1;i<4;i++){if(mpfr_cmp(dl[i],dl[il])<0)il=i;if(mpfr_cmp(du[i],du[iu])>0)iu=i;}
    mpfr_set(z->lo,dl[il],MPFR_RNDD);mpfr_set(z->hi,du[iu],MPFR_RNDU);
    for(int i=0;i<4;i++){mpfr_clear(dl[i]);mpfr_clear(du[i]);}
}
static void iv_mul_ui(iv*z,const iv*a,unsigned long n){
    if(mpfr_cmp_ui(a->lo,0)>=0){mpfr_mul_ui(z->lo,a->lo,n,MPFR_RNDD);mpfr_mul_ui(z->hi,a->hi,n,MPFR_RNDU);} 
    else if(mpfr_cmp_ui(a->hi,0)<=0){mpfr_mul_ui(z->lo,a->lo,n,MPFR_RNDD);mpfr_mul_ui(z->hi,a->hi,n,MPFR_RNDU);} 
    else {mpfr_mul_ui(z->lo,a->lo,n,MPFR_RNDD);mpfr_mul_ui(z->hi,a->hi,n,MPFR_RNDU);} }
static void iv_div_pos(iv*z,const iv*a,const iv*b){
    if(mpfr_cmp_ui(b->lo,0)<=0){fprintf(stderr,"nonpositive divisor\n");exit(2);} iv inv;iv_init(&inv);
    mpfr_t one;mpfr_init2(one,PREC);mpfr_set_ui(one,1,MPFR_RNDN);
    mpfr_div(inv.lo,one,b->hi,MPFR_RNDD);mpfr_div(inv.hi,one,b->lo,MPFR_RNDU);iv_mul(z,a,&inv);
    mpfr_clear(one);iv_clear(&inv);
}
static void iv_log_ui(iv*z,unsigned long n){mpfr_t a;mpfr_init2(a,PREC);mpfr_set_ui(a,n,MPFR_RNDN);mpfr_log(z->lo,a,MPFR_RNDD);mpfr_log(z->hi,a,MPFR_RNDU);mpfr_clear(a);} 
static void iv_sqrt_ui(iv*z,unsigned long n){mpfr_t a;mpfr_init2(a,PREC);mpfr_set_ui(a,n,MPFR_RNDN);mpfr_sqrt(z->lo,a,MPFR_RNDD);mpfr_sqrt(z->hi,a,MPFR_RNDU);mpfr_clear(a);} 

typedef struct { mpq_t knot, coeff; double kd; } termq;
static int cmp_term(const void*A,const void*B){return mpq_cmp(((const termq*)A)->knot,((const termq*)B)->knot);} 
static void qmul_ui(mpq_t z,const mpq_t a,unsigned long n){mpq_set(z,a);mpz_mul_ui(mpq_numref(z),mpq_numref(z),n);mpq_canonicalize(z);}
static void qdiv_ui(mpq_t z,const mpq_t a,unsigned long n){mpq_set(z,a);mpz_mul_ui(mpq_denref(z),mpq_denref(z),n);mpq_canonicalize(z);}
static unsigned long binom(int n,int k){ if(k<0||k>n)return 0; if(k>n-k)k=n-k; unsigned long r=1; for(int i=1;i<=k;i++)r=r*(unsigned long)(n-k+i)/(unsigned long)i; return r; }

typedef struct { iv knot; double kd; iv c[24]; } segment;

static void make_base_terms(termq *raw, int *nraw){
    const char *rn[5]={"35218599699163919097920611990","23680158309013251518610419821","19903564882942428266376244912","16361783185744983922054900136","15114750136364744335442418335"};
    mpq_t rr[5],norm,tmp; for(int j=0;j<5;j++){mpq_init(rr[j]);mpq_set_str(rr[j],rn[j],10);mpz_mul_2exp(mpq_denref(rr[j]),mpq_denref(rr[j]),96);mpq_canonicalize(rr[j]);}
    mpq_init(norm); mpq_set_ui(norm,1,1); for(int j=0;j<24;j++)qmul_ui(norm,norm,12); for(int j=2;j<=23;j++)qdiv_ui(norm,norm,(unsigned long)j);
    mpq_init(tmp); int at=0;
    for(int mask=0;mask<32;mask++){
        mpq_t s;mpq_init(s);mpq_set_ui(s,0,1);int parity=0;
        for(int j=0;j<5;j++)if(mask&(1<<j)){mpq_add(s,s,rr[j]);parity^=1;}
        for(int k=0;k<=24;k++){
            termq *t=&raw[at++];mpq_init(t->knot);mpq_init(t->coeff);
            mpq_set_ui(t->knot,2,1);mpq_add(t->knot,t->knot,s);mpq_set_ui(tmp,(unsigned long)k,12);mpq_add(t->knot,t->knot,tmp);
            mpq_set(t->coeff,norm);qmul_ui(t->coeff,t->coeff,binom(24,k));qdiv_ui(t->coeff,t->coeff,32);
            if((parity+k)&1)mpq_neg(t->coeff,t->coeff);
            t->kd=mpq_get_d(t->knot);
        }
        mpq_clear(s);
    }
    *nraw=at;mpq_clear(tmp);mpq_clear(norm);for(int j=0;j<5;j++)mpq_clear(rr[j]);
}

static segment *build_segments(int *nout){
    termq *raw=calloc(800,sizeof(termq));int nr=0;make_base_terms(raw,&nr);qsort(raw,nr,sizeof(termq),cmp_term);
    for(int i=1;i<nr;i++)if(mpq_cmp(raw[i-1].knot,raw[i].knot)>=0){fprintf(stderr,"duplicate/nonordered knot\n");exit(3);} 
    segment *seg=calloc(nr,sizeof(segment)); for(int i=0;i<nr;i++){iv_init(&seg[i].knot);iv_set_q(&seg[i].knot,raw[i].knot);seg[i].kd=raw[i].kd;for(int m=0;m<24;m++)iv_init(&seg[i].c[m]);}
    iv cur[24];for(int m=0;m<24;m++){iv_init(&cur[m]);iv_zero(&cur[m]);}
    iv add;iv_init(&add);iv_set_q(&add,raw[0].coeff);iv_add(&cur[23],&cur[23],&add);for(int m=0;m<24;m++)iv_copy(&seg[0].c[m],&cur[m]);
    for(int i=1;i<nr;i++){
        mpq_t dq;mpq_init(dq);mpq_sub(dq,raw[i].knot,raw[i-1].knot);iv d;iv_init(&d);iv_set_q(&d,dq);
        iv dp[24];for(int q=0;q<24;q++){iv_init(&dp[q]);iv_zero(&dp[q]);}iv_set_ui(&dp[0],1);for(int q=1;q<24;q++)iv_mul(&dp[q],&dp[q-1],&d);
        iv nxt[24];for(int m=0;m<24;m++){iv_init(&nxt[m]);iv_zero(&nxt[m]);}
        for(int j=0;j<24;j++)for(int m=0;m<=j;m++){iv z,t;iv_init(&z);iv_init(&t);iv_mul(&z,&cur[j],&dp[j-m]);iv_mul_ui(&t,&z,binom(j,m));iv_add(&nxt[m],&nxt[m],&t);iv_clear(&z);iv_clear(&t);} 
        iv_set_q(&add,raw[i].coeff);iv_add(&nxt[23],&nxt[23],&add);
        for(int m=0;m<24;m++){iv_copy(&cur[m],&nxt[m]);iv_copy(&seg[i].c[m],&nxt[m]);iv_clear(&nxt[m]);iv_clear(&dp[m]);}
        iv_clear(&d);mpq_clear(dq);
    }
    iv_clear(&add);for(int m=0;m<24;m++)iv_clear(&cur[m]);
    for(int i=0;i<nr;i++){mpq_clear(raw[i].knot);mpq_clear(raw[i].coeff);}free(raw);*nout=nr;return seg;
}

static long AMBIGUITIES=0;
static int find_segment(segment*seg,int n,const iv*u){
    double mid=(mpfr_get_d(u->lo,MPFR_RNDN)+mpfr_get_d(u->hi,MPFR_RNDN))*0.5;int lo=0,hi=n;
    while(lo<hi){int m=(lo+hi)/2;if(seg[m].kd<=mid)lo=m+1;else hi=m;}int i=lo-1;if(i<0)return -1;
    if(mpfr_cmp(u->lo,seg[i].knot.hi)<0){AMBIGUITIES++;fprintf(stderr,"ambiguous left knot at %d\n",i);return -2;}
    if(i+1<n && mpfr_cmp(u->hi,seg[i+1].knot.lo)>=0){AMBIGUITIES++;fprintf(stderr,"ambiguous right knot at %d\n",i);return -2;}
    return i;
}
static void eval_base(iv*out,segment*seg,int n,const iv*u){
    int i=find_segment(seg,n,u);if(i==-1){iv_zero(out);return;}if(i==-2)exit(4);
    if(i==n-1 && mpfr_cmp(u->lo,seg[n-1].knot.hi)>0){iv_zero(out);return;}
    iv t;iv_init(&t);iv_sub(&t,u,&seg[i].knot);iv val,tmp;iv_init(&val);iv_init(&tmp);iv_copy(&val,&seg[i].c[23]);
    for(int m=22;m>=0;m--){iv_mul(&tmp,&val,&t);iv_add(&val,&tmp,&seg[i].c[m]);}
    iv_copy(out,&val);iv_clear(&t);iv_clear(&val);iv_clear(&tmp);
}

static uint8_t *sieve(int n){uint8_t*s=malloc((size_t)n+1);memset(s,1,(size_t)n+1);s[0]=s[1]=0;for(int p=2;(long long)p*p<=n;p++)if(s[p])for(long long v=(long long)p*p;v<=n;v+=p)s[v]=0;return s;}

int main(int argc,char**argv){if(argc>1)PREC=atol(argv[1]);int nseg=0;segment*seg=build_segments(&nseg);
    mpq_t xq;mpq_init(xq);mpq_set_str(xq,"17730793345827",10);mpz_mul_2exp(mpq_denref(xq),mpq_denref(xq),40);mpq_canonicalize(xq);iv x,h;iv_init(&x);iv_init(&h);iv_set_q(&x,xq);iv_log_ui(&h,4);
    const int MAXN=1364177;
    iv lm,lnext,xm2,two;iv_init(&lm);iv_init(&lnext);iv_init(&xm2);iv_init(&two);iv_log_ui(&lm,MAXN);iv_log_ui(&lnext,MAXN+1);iv_set_ui(&two,2);iv_sub(&xm2,&x,&two);
    if(mpfr_cmp(lm.hi,xm2.lo)>0 || mpfr_cmp(lnext.lo,xm2.hi)<=0){fprintf(stderr,"MAXN support assertion failed\n");return 5;}
    iv_clear(&lm);iv_clear(&lnext);iv_clear(&xm2);iv_clear(&two);
    uint8_t*sv=sieve(MAXN);iv total;iv_init(&total);iv_zero(&total);long long count=0;
    for(int p=2;p<=MAXN;p++)if(sv[p]){
        iv logp;iv_init(&logp);iv_log_ui(&logp,(unsigned long)p);long long v=p;
        while(v<=MAXN){iv logn,u,uh,f1,f2,twof2,win,sq,w,term;iv_init(&logn);iv_init(&u);iv_init(&uh);iv_init(&f1);iv_init(&f2);iv_init(&twof2);iv_init(&win);iv_init(&sq);iv_init(&w);iv_init(&term);
            iv_log_ui(&logn,(unsigned long)v);iv_sub(&u,&x,&logn);iv_sub(&uh,&u,&h);
            eval_base(&f1,seg,nseg,&u);eval_base(&f2,seg,nseg,&uh);iv_mul_ui(&twof2,&f2,2);iv_sub(&win,&f1,&twof2);
            if(mpfr_cmp_ui(win.lo,0)!=0 || mpfr_cmp_ui(win.hi,0)!=0){iv_sqrt_ui(&sq,(unsigned long)v);iv_div_pos(&w,&logp,&sq);iv_mul(&term,&w,&win);iv_add(&total,&total,&term);count++;}
            iv_clear(&logn);iv_clear(&u);iv_clear(&uh);iv_clear(&f1);iv_clear(&f2);iv_clear(&twof2);iv_clear(&win);iv_clear(&sq);iv_clear(&w);iv_clear(&term);
            if(v>MAXN/p)break;v*=p;
        }
        iv_clear(&logp);
    }
    if(nseg!=800 || count!=103384 || AMBIGUITIES!=0){fprintf(stderr,"structural count mismatch: segments=%d terms=%lld ambiguities=%ld\n",nseg,count,AMBIGUITIES);return 6;}
    printf("schema=riemann.x17804-local-cell-mpfr.v1 precision=%ld segments=%d terms=%lld ambiguities=%ld\n",(long)PREC,nseg,count,AMBIGUITIES);mpfr_printf("prime_lower=%.150Re\n",total.lo);mpfr_printf("prime_upper=%.150Re\n",total.hi);
    free(sv);for(int i=0;i<nseg;i++){iv_clear(&seg[i].knot);for(int m=0;m<24;m++)iv_clear(&seg[i].c[m]);}free(seg);iv_clear(&total);iv_clear(&x);iv_clear(&h);mpq_clear(xq);return 0;
}
