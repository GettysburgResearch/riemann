#define _GNU_SOURCE
#include <quadmath.h>
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <stdbool.h>
#include <string.h>
#include <math.h>
#include <mpfr.h>

typedef __float128 q;
typedef struct{q re,im;} qc;
typedef struct{qc c;q r;} disc;
static const q U=0x1p-112Q; /* conservative: machine epsilon, twice unit roundoff */
static inline qc qadd(qc a,qc b){return(qc){a.re+b.re,a.im+b.im};}
static inline qc qsub(qc a,qc b){return(qc){a.re-b.re,a.im-b.im};}
static inline qc qmul(qc a,qc b){return(qc){a.re*b.re-a.im*b.im,a.re*b.im+a.im*b.re};}
static inline qc qscale(qc a,q s){return(qc){a.re*s,a.im*s};}
static inline q qabs_c(qc a){return hypotq(a.re,a.im);}
static inline disc dadd(disc a,disc b,int subtract){
 qc c=subtract?qsub(a.c,b.c):qadd(a.c,b.c);
 q r=a.r+b.r+64*U*(qabs_c(a.c)+qabs_c(b.c)+a.r+b.r+1);
 return(disc){c,r};
}
static inline disc dmul(disc a,disc b){
 qc c=qmul(a.c,b.c); q aa=qabs_c(a.c),bb=qabs_c(b.c);
 q r=aa*b.r+bb*a.r+a.r*b.r+256*U*(aa+a.r)*(bb+b.r)+1e-4900Q;
 return(disc){c,r};
}
static inline disc dscale(disc a,q s){return(disc){qscale(a.c,s),fabsq(s)*a.r};}

/* Minimal MPFR interval layer. */
typedef struct{mpfr_t lo,hi;} iv;
static const mpfr_prec_t PREC=256;
static void iv_init(iv*x){mpfr_init2(x->lo,PREC);mpfr_init2(x->hi,PREC);}static void iv_clear(iv*x){mpfr_clear(x->lo);mpfr_clear(x->hi);} 
static void iv_copy(iv*z,const iv*a){mpfr_set(z->lo,a->lo,MPFR_RNDD);mpfr_set(z->hi,a->hi,MPFR_RNDU);} 
static void iv_set_ui(iv*x,unsigned long v){mpfr_set_ui(x->lo,v,MPFR_RNDD);mpfr_set_ui(x->hi,v,MPFR_RNDU);} 
static void iv_set_str10(iv*x,const char*s){mpfr_set_str(x->lo,s,10,MPFR_RNDD);mpfr_set_str(x->hi,s,10,MPFR_RNDU);} 
static void iv_pi(iv*x){mpfr_const_pi(x->lo,MPFR_RNDD);mpfr_const_pi(x->hi,MPFR_RNDU);} 
static void iv_add(iv*z,const iv*a,const iv*b){mpfr_t l,h;mpfr_init2(l,PREC);mpfr_init2(h,PREC);mpfr_add(l,a->lo,b->lo,MPFR_RNDD);mpfr_add(h,a->hi,b->hi,MPFR_RNDU);mpfr_set(z->lo,l,MPFR_RNDD);mpfr_set(z->hi,h,MPFR_RNDU);mpfr_clear(l);mpfr_clear(h);} 
static void iv_sub(iv*z,const iv*a,const iv*b){mpfr_t l,h;mpfr_init2(l,PREC);mpfr_init2(h,PREC);mpfr_sub(l,a->lo,b->hi,MPFR_RNDD);mpfr_sub(h,a->hi,b->lo,MPFR_RNDU);mpfr_set(z->lo,l,MPFR_RNDD);mpfr_set(z->hi,h,MPFR_RNDU);mpfr_clear(l);mpfr_clear(h);} 
static void iv_neg(iv*z,const iv*a){mpfr_t l,h;mpfr_init2(l,PREC);mpfr_init2(h,PREC);mpfr_neg(l,a->hi,MPFR_RNDD);mpfr_neg(h,a->lo,MPFR_RNDU);mpfr_set(z->lo,l,MPFR_RNDD);mpfr_set(z->hi,h,MPFR_RNDU);mpfr_clear(l);mpfr_clear(h);} 
static void iv_mul(iv*z,const iv*a,const iv*b){
 mpfr_t dl[4],du[4];for(int i=0;i<4;i++){mpfr_init2(dl[i],PREC);mpfr_init2(du[i],PREC);}mpfr_srcptr av[2]={a->lo,a->hi},bv[2]={b->lo,b->hi};int n=0;
 for(int i=0;i<2;i++)for(int j=0;j<2;j++){mpfr_mul(dl[n],av[i],bv[j],MPFR_RNDD);mpfr_mul(du[n],av[i],bv[j],MPFR_RNDU);n++;}
 int il=0,iu=0;for(int i=1;i<4;i++){if(mpfr_cmp(dl[i],dl[il])<0)il=i;if(mpfr_cmp(du[i],du[iu])>0)iu=i;}mpfr_set(z->lo,dl[il],MPFR_RNDD);mpfr_set(z->hi,du[iu],MPFR_RNDU);for(int i=0;i<4;i++){mpfr_clear(dl[i]);mpfr_clear(du[i]);}
}
static void iv_div_pos(iv*z,const iv*a,const iv*b){
 if(mpfr_cmp_ui(b->lo,0)<=0){fprintf(stderr,"nonpositive divisor\n");exit(2);}iv inv;iv_init(&inv);mpfr_ui_div(inv.lo,1,b->hi,MPFR_RNDD);mpfr_ui_div(inv.hi,1,b->lo,MPFR_RNDU);iv_mul(z,a,&inv);iv_clear(&inv);
}
static void iv_mul_ui(iv*z,const iv*a,unsigned long n){mpfr_mul_ui(z->lo,a->lo,n,MPFR_RNDD);mpfr_mul_ui(z->hi,a->hi,n,MPFR_RNDU);} 
static void iv_div_ui(iv*z,const iv*a,unsigned long n){mpfr_div_ui(z->lo,a->lo,n,MPFR_RNDD);mpfr_div_ui(z->hi,a->hi,n,MPFR_RNDU);} 
static void iv_scale2(iv*z,const iv*a,long e){mpfr_mul_2si(z->lo,a->lo,e,MPFR_RNDD);mpfr_mul_2si(z->hi,a->hi,e,MPFR_RNDU);} 
static void iv_square(iv*z,const iv*a){
 if(mpfr_cmp_ui(a->lo,0)<=0 && mpfr_cmp_ui(a->hi,0)>=0){mpfr_set_ui(z->lo,0,MPFR_RNDD);mpfr_t x,y;mpfr_init2(x,PREC);mpfr_init2(y,PREC);mpfr_sqr(x,a->lo,MPFR_RNDU);mpfr_sqr(y,a->hi,MPFR_RNDU);if(mpfr_cmp(x,y)>0)mpfr_set(z->hi,x,MPFR_RNDU);else mpfr_set(z->hi,y,MPFR_RNDU);mpfr_clear(x);mpfr_clear(y);}else{mpfr_t x1,x2,y1,y2;mpfr_init2(x1,PREC);mpfr_init2(x2,PREC);mpfr_init2(y1,PREC);mpfr_init2(y2,PREC);mpfr_sqr(x1,a->lo,MPFR_RNDD);mpfr_sqr(x2,a->hi,MPFR_RNDD);mpfr_sqr(y1,a->lo,MPFR_RNDU);mpfr_sqr(y2,a->hi,MPFR_RNDU);if(mpfr_cmp(x1,x2)<0)mpfr_set(z->lo,x1,MPFR_RNDD);else mpfr_set(z->lo,x2,MPFR_RNDD);if(mpfr_cmp(y1,y2)>0)mpfr_set(z->hi,y1,MPFR_RNDU);else mpfr_set(z->hi,y2,MPFR_RNDU);mpfr_clear(x1);mpfr_clear(x2);mpfr_clear(y1);mpfr_clear(y2);}
}
static void iv_mid_radius(mpfr_t m,mpfr_t r,const iv*a){mpfr_add(m,a->lo,a->hi,MPFR_RNDN);mpfr_div_2si(m,m,1,MPFR_RNDN);mpfr_t x,y;mpfr_init2(x,PREC);mpfr_init2(y,PREC);mpfr_sub(x,m,a->lo,MPFR_RNDU);mpfr_sub(y,a->hi,m,MPFR_RNDU);if(mpfr_cmp(x,y)>0)mpfr_set(r,x,MPFR_RNDU);else mpfr_set(r,y,MPFR_RNDU);mpfr_clear(x);mpfr_clear(y);} 
static void iv_sin_lip(iv*z,const iv*a){mpfr_t m,r,l,h;mpfr_init2(m,PREC);mpfr_init2(r,PREC);mpfr_init2(l,PREC);mpfr_init2(h,PREC);iv_mid_radius(m,r,a);mpfr_sin(l,m,MPFR_RNDD);mpfr_sin(h,m,MPFR_RNDU);mpfr_sub(z->lo,l,r,MPFR_RNDD);mpfr_add(z->hi,h,r,MPFR_RNDU);mpfr_clear(m);mpfr_clear(r);mpfr_clear(l);mpfr_clear(h);} 
static void iv_cos_lip(iv*z,const iv*a){mpfr_t m,r,l,h;mpfr_init2(m,PREC);mpfr_init2(r,PREC);mpfr_init2(l,PREC);mpfr_init2(h,PREC);iv_mid_radius(m,r,a);mpfr_cos(l,m,MPFR_RNDD);mpfr_cos(h,m,MPFR_RNDU);mpfr_sub(z->lo,l,r,MPFR_RNDD);mpfr_add(z->hi,h,r,MPFR_RNDU);mpfr_clear(m);mpfr_clear(r);mpfr_clear(l);mpfr_clear(h);} 
static void iv_log_ui(iv*z,unsigned long n){mpfr_t x;mpfr_init2(x,PREC);mpfr_set_ui(x,n,MPFR_RNDN);mpfr_log(z->lo,x,MPFR_RNDD);mpfr_log(z->hi,x,MPFR_RNDU);mpfr_clear(x);} 
static void iv_sqrt_ui(iv*z,unsigned long n){mpfr_t x;mpfr_init2(x,PREC);mpfr_set_ui(x,n,MPFR_RNDN);mpfr_sqrt(z->lo,x,MPFR_RNDD);mpfr_sqrt(z->hi,x,MPFR_RNDU);mpfr_clear(x);} 
static void iv_to_q(const iv*a,q*center,q*radius){q l=mpfr_get_float128(a->lo,MPFR_RNDD),h=mpfr_get_float128(a->hi,MPFR_RNDU);*center=(l+h)/2;*radius=(h-l)/2+32*U*(fabsq(l)+fabsq(h)+1e-4900Q);} 
static disc rect_to_disc(const iv*re,const iv*im){q cr,rr,ci,ri;iv_to_q(re,&cr,&rr);iv_to_q(im,&ci,&ri);return(disc){{cr,ci},hypotq(rr,ri)+16*U*(fabsq(cr)+fabsq(ci)+1)};} 
static void printq(const char*n,q x){char b[256];quadmath_snprintf(b,sizeof b,"%.45Qg",x);printf("%s=%s\n",n,b);} 

static void fft_disc(disc*a,size_t n,int inverse,disc*wlen){
 for(size_t i=1,j=0;i<n;i++){size_t bit=n>>1;for(;j&bit;bit>>=1)j^=bit;j^=bit;if(i<j){disc t=a[i];a[i]=a[j];a[j]=t;}}
 int stage=0;for(size_t len=2;len<=n;len<<=1,stage++){
  disc wl=wlen[stage];if(!inverse)wl.c.im=-wl.c.im;
  for(size_t i=0;i<n;i+=len){disc w={ {1,0},0};for(size_t j=0;j<len/2;j++){disc u=a[i+j],v=dmul(a[i+j+len/2],w);a[i+j]=dadd(u,v,0);a[i+j+len/2]=dadd(u,v,1);w=dmul(w,wl);}}
 }
 if(inverse)for(size_t i=0;i<n;i++)a[i]=dscale(a[i],1/(q)n);
}

typedef struct{int n,p;q wc,wr,lnc,lnr;}event;static int cmp_event(const void*A,const void*B){int a=((event*)A)->n,b=((event*)B)->n;return(a>b)-(a<b);} 
static uint8_t*sieve(int lim){uint8_t*a=malloc((size_t)lim+1);memset(a,1,(size_t)lim+1);a[0]=a[1]=0;for(int p=2;(long long)p*p<=lim;p++)if(a[p])for(long long v=(long long)p*p;v<=lim;v+=p)a[v]=0;return a;}
static void real_mul(q ac,q ar,q bc,q br,q*cc,q*rr){*cc=ac*bc;*rr=fabsq(ac)*br+fabsq(bc)*ar+ar*br+32*U*(fabsq(ac)+ar)*(fabsq(bc)+br)+1e-4900Q;}
static void cubic_interval(const disc*s,size_t n,q step,q y,q yr,q deriv1,q deriv4,q tail0,q*outc,q*outr){
 q pos=y/step,fi=floorq(pos),t=pos-fi;long long i=(long long)fi;long long idx[4]={(i-1+(long long)n)%n,(i+(long long)n)%n,(i+1)%n,(i+2)%n};
 q L[4]={-t*(t-1)*(t-2)/6,(t+1)*(t-1)*(t-2)/2,-(t+1)*t*(t-2)/2,(t+1)*t*(t-1)/6};q c=0,r=0;
 for(int j=0;j<4;j++){c+=L[j]*s[idx[j]].c.re;r+=fabsq(L[j])*s[idx[j]].r+16*U*fabsq(L[j]*s[idx[j]].c.re);}
 q interp=(3.0Q/128.0Q)*step*step*step*step*deriv4;
 r+=deriv1*yr+interp+tail0+128*U*(fabsq(c)+1);
 *outc=c;*outr=r;
}

int main(int argc,char**argv){int powN=18,K=4096,Jdy=64;if(argc>1)powN=atoi(argv[1]);if(argc>2)K=atoi(argv[2]);size_t N=(size_t)1<<powN;if(K>=(int)N/2)return 2;q P=8,step=P/(q)N;
 // exact dyadic x
 q x=(q)8578244975439ULL/(q)549755813888ULL;
 iv pi,gamma[5],rnotch[5],S,hiv,two,tmp;iv_init(&pi);iv_pi(&pi);iv_init(&S);iv_set_ui(&S,1);iv_init(&hiv);iv_log_ui(&hiv,4);iv_init(&two);iv_set_ui(&two,2);iv_init(&tmp);
 const char*zs[5]={"14.13472514173469379045725198356247","21.02203963877155499262847959389690","25.01085758014568876321379099256282","30.42487612585951321031189753058409","32.93506158773918969066236896407490"};
 for(int j=0;j<5;j++){iv_init(&gamma[j]);iv_set_str10(&gamma[j],zs[j]);iv_init(&rnotch[j]);iv_mul_ui(&tmp,&pi,2);iv_div_pos(&rnotch[j],&tmp,&gamma[j]);iv_add(&S,&S,&rnotch[j]);}
 q Sc,Sr,hc,hr;iv_to_q(&S,&Sc,&Sr);iv_to_q(&hiv,&hc,&hr);
 disc*a=calloc(N,sizeof(disc));q deriv1=0,deriv4=0;
 // coefficients k=0..K
 for(int k=0;k<=K;k++){
  iv re,im,prod,omega,arg,sn,sq,phase,cs,ss,amp,one,delta,tailfac;iv_init(&re);iv_init(&im);iv_init(&prod);iv_set_ui(&prod,1);iv_init(&omega);iv_mul_ui(&omega,&pi,(unsigned long)k);iv_div_ui(&omega,&omega,4);iv_init(&arg);iv_init(&sn);iv_init(&sq);iv_init(&phase);iv_init(&cs);iv_init(&ss);iv_init(&amp);iv_init(&one);iv_set_ui(&one,1);iv_init(&delta);iv_init(&tailfac);
  if(k>0){
   for(int j=0;j<5;j++){iv_mul(&arg,&omega,&rnotch[j]);iv_div_ui(&arg,&arg,2);iv_sin_lip(&sn,&arg);iv_div_pos(&sn,&sn,&arg);iv_square(&sq,&sn);iv_mul(&prod,&prod,&sq);}
   for(int j=1;j<=Jdy;j++){iv_scale2(&arg,&omega,-(j+1));iv_sin_lip(&sn,&arg);iv_div_pos(&sn,&sn,&arg);iv_square(&sq,&sn);iv_mul(&prod,&prod,&sq);}
   // omitted dyadic squared-product <= omega^2 4^-J /36
   iv_square(&delta,&omega);iv_scale2(&delta,&delta,-2*Jdy);iv_div_ui(&delta,&delta,36);iv_sub(&tailfac,&one,&delta);if(mpfr_cmp_ui(tailfac.lo,0)<0)mpfr_set_ui(tailfac.lo,0,MPFR_RNDD);mpfr_set_ui(tailfac.hi,1,MPFR_RNDU);iv_mul(&prod,&prod,&tailfac);
  }
  iv_div_ui(&amp,&prod,8);iv_mul(&phase,&omega,&S);iv_neg(&phase,&phase);iv_cos_lip(&cs,&phase);iv_sin_lip(&ss,&phase);iv_mul(&re,&amp,&cs);iv_mul(&im,&amp,&ss);disc cd=rect_to_disc(&re,&im);cd=dscale(cd,(q)N);a[k]=cd;if(k)a[N-k]=(disc){{cd.c.re,-cd.c.im},cd.r};
  q absup=mpfr_get_float128(amp.hi,MPFR_RNDU);q omup=mpfr_get_float128(omega.hi,MPFR_RNDU);q mult=k?2:1;deriv1+=mult*absup*omup;deriv4+=mult*absup*omup*omup*omup*omup;
  iv_clear(&re);iv_clear(&im);iv_clear(&prod);iv_clear(&omega);iv_clear(&arg);iv_clear(&sn);iv_clear(&sq);iv_clear(&phase);iv_clear(&cs);iv_clear(&ss);iv_clear(&amp);iv_clear(&one);iv_clear(&delta);iv_clear(&tailfac);
 }
 // analytic Fourier tails, safe pi>3; J=10
 q tail0=1.4e-29Q,tail4=1.5e-15Q;deriv4+=tail4;
 // stage roots from MPFR intervals
 int stages=powN;disc*wlen=calloc(stages,sizeof(disc));size_t len=2;for(int s=0;s<stages;s++,len<<=1){iv angle,cs,ss,den;iv_init(&angle);iv_init(&cs);iv_init(&ss);iv_init(&den);iv_mul_ui(&angle,&pi,2);iv_set_ui(&den,(unsigned long)len);iv_div_pos(&angle,&angle,&den);iv_cos_lip(&cs,&angle);iv_sin_lip(&ss,&angle);wlen[s]=rect_to_disc(&cs,&ss);iv_clear(&angle);iv_clear(&cs);iv_clear(&ss);iv_clear(&den);}fft_disc(a,N,1,wlen);
 q maxgridr=0,maximag=0;for(size_t i=0;i<N;i++){if(a[i].r>maxgridr)maxgridr=a[i].r;if(fabsq(a[i].c.im)>maximag)maximag=fabsq(a[i].c.im);}
 // event manifest
 int limit=1500000; /* x<16 and support starts at 2, so exp(x-2)<exp(14)<2e6 */ uint8_t*is=sieve(limit);size_t cap=100000,ne=0;event*ev=malloc(cap*sizeof(event));for(int p=2;p<=limit;p++)if(is[p]){iv lp;iv_init(&lp);iv_log_ui(&lp,(unsigned long)p);q lpc,lpr;iv_to_q(&lp,&lpc,&lpr);long long v=p;while(v<=limit){if(ne==cap){cap*=2;ev=realloc(ev,cap*sizeof(event));}iv ln,sqv,w;iv_init(&ln);iv_init(&sqv);iv_init(&w);iv_log_ui(&ln,(unsigned long)v);iv_sqrt_ui(&sqv,(unsigned long)v);iv_div_pos(&w,&lp,&sqv);q wc,wr,lnc,lnr;iv_to_q(&w,&wc,&wr);iv_to_q(&ln,&lnc,&lnr);ev[ne++]=(event){(int)v,p,wc,wr,lnc,lnr};iv_clear(&ln);iv_clear(&sqv);iv_clear(&w);if(v>limit/p)break;v*=p;}iv_clear(&lp);}qsort(ev,ne,sizeof(event),cmp_event);
 q maxsupc=2+2*Sc+hc,maxsupr=2*Sr+hr; q sumc=0,sumr=0,comp=0,sumw=0;size_t cnt=0,c1n=0,c2n=0;
 for(size_t ii=0;ii<ne;ii++){
  q uc=x-ev[ii].lnc,ur=ev[ii].lnr;if(uc+ur<2||uc-ur>maxsupc+maxsupr)continue;q gc=0,gr=0;
  q y1=uc-2,y1r=ur,y2=uc-hc-2,y2r=ur+hr;
  if(y1+y1r>=0&&y1-y1r<=2*Sc+2*Sr){q c,r;cubic_interval(a,N,step,y1,y1r,deriv1,deriv4,tail0,&c,&r);gc+=c;gr+=r;c1n++;}
  if(y2+y2r>=0&&y2-y2r<=2*Sc+2*Sr){q c,r;cubic_interval(a,N,step,y2,y2r,deriv1,deriv4,tail0,&c,&r);gc-=2*c;gr+=2*r+16*U*fabsq(2*c);c2n++;}
  q tc,tr;real_mul(ev[ii].wc,ev[ii].wr,gc,gr,&tc,&tr);q yy=tc-comp,tt=sumc+yy;comp=(tt-sumc)-yy;sumc=tt;sumr+=tr+16*U*(fabsq(sumc)+fabsq(tc)+1);sumw+=ev[ii].wc;cnt++;
 }
 printf("pow=%d K=%d terms=%zu c1=%zu c2=%zu\n",powN,K,cnt,c1n,c2n);printq("S_center",Sc);printq("S_radius",Sr);printq("deriv1",deriv1);printq("deriv4",deriv4);printq("max_grid_radius",maxgridr);printq("max_grid_imag",maximag);printq("sumweights",sumw);printq("prime_center",sumc);printq("prime_radius",sumr);printq("prime_lower",sumc-sumr);printq("prime_upper",sumc+sumr);
 // cleanup omitted for brevity
 return 0;
}
