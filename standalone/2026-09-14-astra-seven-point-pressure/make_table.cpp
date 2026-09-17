// Rigorous MPFR primitives and complete cell/point bounds.
#include <algorithm>
#include <array>
#include <cmath>
#include <fstream>
#include <iostream>
#include <limits>
#include <stdexcept>
#include <string>
#include <utility>
extern "C" {
typedef long mpfr_prec_t; typedef long mpfr_exp_t;
typedef struct {mpfr_prec_t _mpfr_prec; int _mpfr_sign; mpfr_exp_t _mpfr_exp; unsigned long *_mpfr_d;} __mpfr_struct;
typedef __mpfr_struct mpfr_t[1]; typedef __mpfr_struct *mpfr_ptr; typedef const __mpfr_struct *mpfr_srcptr;
typedef enum {MPFR_RNDN=0,MPFR_RNDZ,MPFR_RNDU,MPFR_RNDD,MPFR_RNDA,MPFR_RNDF} mpfr_rnd_t;
void mpfr_init2(mpfr_ptr,mpfr_prec_t); void mpfr_clear(mpfr_ptr);
int mpfr_set(mpfr_ptr,mpfr_srcptr,mpfr_rnd_t); int mpfr_set_si(mpfr_ptr,long,mpfr_rnd_t);
int mpfr_add(mpfr_ptr,mpfr_srcptr,mpfr_srcptr,mpfr_rnd_t); int mpfr_sub(mpfr_ptr,mpfr_srcptr,mpfr_srcptr,mpfr_rnd_t);
int mpfr_mul(mpfr_ptr,mpfr_srcptr,mpfr_srcptr,mpfr_rnd_t); int mpfr_div(mpfr_ptr,mpfr_srcptr,mpfr_srcptr,mpfr_rnd_t);
int mpfr_neg(mpfr_ptr,mpfr_srcptr,mpfr_rnd_t); int mpfr_sqrt(mpfr_ptr,mpfr_srcptr,mpfr_rnd_t);
int mpfr_sin(mpfr_ptr,mpfr_srcptr,mpfr_rnd_t); int mpfr_cos(mpfr_ptr,mpfr_srcptr,mpfr_rnd_t);
int mpfr_const_pi(mpfr_ptr,mpfr_rnd_t); double mpfr_get_d(mpfr_srcptr,mpfr_rnd_t);
int mpfr_cmp(mpfr_srcptr,mpfr_srcptr); int mpfr_cmp_si(mpfr_srcptr,long); const char *mpfr_get_version(void);
}
#ifndef TABLE_PREC
#define TABLE_PREC 160
#endif
static const mpfr_prec_t PREC=TABLE_PREC;
static_assert(sizeof(long)==8 && sizeof(__mpfr_struct)==32, "This header-free MPFR ABI targets LP64 Linux");
struct I {
 mpfr_t l,h;
 I(long n=0){mpfr_init2(l,PREC);mpfr_init2(h,PREC);mpfr_set_si(l,n,MPFR_RNDD);mpfr_set_si(h,n,MPFR_RNDU);}
 I(const I&b):I(){mpfr_set(l,b.l,MPFR_RNDD);mpfr_set(h,b.h,MPFR_RNDU);}
 I&operator=(const I&b){if(this!=&b){mpfr_set(l,b.l,MPFR_RNDD);mpfr_set(h,b.h,MPFR_RNDU);}return *this;}
 ~I(){mpfr_clear(l);mpfr_clear(h);}
 double low()const{return mpfr_get_d(l,MPFR_RNDD);} double high()const{return mpfr_get_d(h,MPFR_RNDU);}
};
I operator+(const I&a,const I&b){I c;mpfr_add(c.l,a.l,b.l,MPFR_RNDD);mpfr_add(c.h,a.h,b.h,MPFR_RNDU);return c;}
I operator-(const I&a,const I&b){I c;mpfr_sub(c.l,a.l,b.h,MPFR_RNDD);mpfr_sub(c.h,a.h,b.l,MPFR_RNDU);return c;}
I operator-(const I&a){I c;mpfr_neg(c.l,a.h,MPFR_RNDD);mpfr_neg(c.h,a.l,MPFR_RNDU);return c;}
I operator*(const I&a,const I&b){I c;mpfr_t t;mpfr_init2(t,PREC);mpfr_srcptr aa[2]={a.l,a.h},bb[2]={b.l,b.h};
 mpfr_mul(c.l,a.l,b.l,MPFR_RNDD);mpfr_mul(c.h,a.l,b.l,MPFR_RNDU);
 for(int i=0;i<2;i++)for(int j=0;j<2;j++){mpfr_mul(t,aa[i],bb[j],MPFR_RNDD);if(mpfr_cmp(t,c.l)<0)mpfr_set(c.l,t,MPFR_RNDD);mpfr_mul(t,aa[i],bb[j],MPFR_RNDU);if(mpfr_cmp(t,c.h)>0)mpfr_set(c.h,t,MPFR_RNDU);}mpfr_clear(t);return c;}
I operator/(const I&a,const I&b){if(mpfr_cmp_si(b.l,0)<=0&&mpfr_cmp_si(b.h,0)>=0)throw std::runtime_error("zero denominator");I r;I one(1);mpfr_div(r.l,one.l,b.h,MPFR_RNDD);mpfr_div(r.h,one.h,b.l,MPFR_RNDU);return a*r;}
I sq(const I&a){if(mpfr_cmp_si(a.l,0)>=0){I c;mpfr_mul(c.l,a.l,a.l,MPFR_RNDD);mpfr_mul(c.h,a.h,a.h,MPFR_RNDU);return c;}if(mpfr_cmp_si(a.h,0)<=0)return sq(-a);I c;mpfr_t t;mpfr_init2(t,PREC);mpfr_mul(c.h,a.l,a.l,MPFR_RNDU);mpfr_mul(t,a.h,a.h,MPFR_RNDU);if(mpfr_cmp(t,c.h)>0)mpfr_set(c.h,t,MPFR_RNDU);mpfr_clear(t);return c;}
I root(const I&a){if(mpfr_cmp_si(a.l,0)<0)throw std::runtime_error("negative root");I c;mpfr_sqrt(c.l,a.l,MPFR_RNDD);mpfr_sqrt(c.h,a.h,MPFR_RNDU);return c;}
I absI(const I&a){if(mpfr_cmp_si(a.l,0)>=0)return a;if(mpfr_cmp_si(a.h,0)<=0)return -a;I c;mpfr_neg(c.h,a.l,MPFR_RNDU);if(mpfr_cmp(a.h,c.h)>0)mpfr_set(c.h,a.h,MPFR_RNDU);return c;}
I trig(const I&a,bool cosine){I c,width;mpfr_sub(width.h,a.h,a.l,MPFR_RNDU);
 if(cosine){mpfr_cos(c.l,a.l,MPFR_RNDD);mpfr_cos(c.h,a.l,MPFR_RNDU);}else{mpfr_sin(c.l,a.l,MPFR_RNDD);mpfr_sin(c.h,a.l,MPFR_RNDU);}
 mpfr_sub(c.l,c.l,width.h,MPFR_RNDD);mpfr_add(c.h,c.h,width.h,MPFR_RNDU);
 if(mpfr_cmp_si(c.l,-1)<0)mpfr_set_si(c.l,-1,MPFR_RNDD);if(mpfr_cmp_si(c.h,1)>0)mpfr_set_si(c.h,1,MPFR_RNDU);return c;}
I rational(long a,long b){return I(a)/I(b);}
I hull(const I&a,const I&b){I c;mpfr_set(c.l,a.l,MPFR_RNDD);mpfr_set(c.h,b.h,MPFR_RNDU);return c;}
struct Kernel {I pi,q,c,half;Kernel():half(rational(1,2)){mpfr_const_pi(pi.l,MPFR_RNDD);mpfr_const_pi(pi.h,MPFR_RNDU);q=root(half);c=q*trig(q,true)/trig(q,false);}
 std::array<I,3> eval(const I&x){I a=pi*x,S=trig(a,false),C=trig(a,true),D=sq(a)-half,N=c*a*S-half*C;
 I N1=(c+half)*S+c*a*C,N2=(I(2)*c+half)*C-c*a*S;
 I k=N/D,k1=pi*(N1*D-I(2)*a*N)/sq(D);
 I k2=sq(pi)*(N2*sq(D)-I(2)*N*D-I(4)*a*N1*D+I(8)*sq(a)*N)/(sq(D)*D);
 return {k,k1,k2};}
};
#ifndef KERNEL_NO_MAIN
int main(int argc,char**argv){try{if(argc!=2)throw std::runtime_error("usage: make_table output");
 const int grid=4000,len=48016;Kernel K;std::ofstream out(argv[1]);if(!out)throw std::runtime_error("cannot write");
 out<<"MPFR_KERNEL_V1 "<<grid<<" "<<len<<" "<<PREC<<"\n"<<std::hexfloat;
 I radius=rational(1,2*grid);for(int j=0;j<=2*len;j++){
  auto a=K.eval(rational(j,2*grid));I w=sq(a[0]),dw=I(2)*a[0]*a[1];
  if(j==0){w=I(1);dw=I(0);} // normalized defining integral
  out<<w.low()<<" "<<w.high()<<" "<<dw.low()<<" "<<dw.high()<<"\n";
 }
 for(int i=0;i<len;i++){
  auto a=K.eval(rational(2*i+1,2*grid));I err=absI(a[1])*radius+sq(K.pi)*sq(radius)/I(2);
  I amin=absI(a[0])-err; double wl=0;if(mpfr_cmp_si(amin.l,0)>0) {I b;mpfr_set(b.l,amin.l,MPFR_RNDD);mpfr_set(b.h,amin.l,MPFR_RNDU);wl=sq(b).low();}
  double d2=-INFINITY;
  if(i>=3800){auto v=K.eval(hull(rational(i,grid),rational(i+1,grid)));I d2i=I(2)*(sq(v[1])+v[0]*v[2]);d2=d2i.low();}
  out<<wl<<" "<<d2<<"\n";
 }
 out.close();if(!out)throw std::runtime_error("write failed");
 std::cerr<<"MPFR "<<mpfr_get_version()<<"; precision "<<PREC<<"; point rows "<<2*len+1<<"; cell rows "<<len<<"\n";
 }catch(const std::exception&e){std::cerr<<e.what()<<"\n";return 2;}}

#endif
