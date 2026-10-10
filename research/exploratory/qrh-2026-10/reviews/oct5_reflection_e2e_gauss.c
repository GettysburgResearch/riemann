/* oct5_reflection_e2e_gauss.c -- unnormalised cubic Gauss sums for primary primes of Z[omega].
 * Status: EXPLORATORY helper for OCT5_REFLECTION_E2E.md.  FLOAT (ordinary double), not certified.
 * Convention (same as reviews/oct5_r3_theta_checks.py g1_prime):
 *   g1(p) = sum_{x mod p} (x/p)_3 * echeck(x/p),  echeck(z) = exp(2 pi i (z + conj z)),
 *   (x/p)_3 = omega^k with x^{(Np-1)/3} == omega^k mod p.
 * Input  (stdin): lines "a b" = primary prime a + b*omega (split: N(p) = q prime, b != 0;
 *                 inert: b = 0, a = -q with q = 2 or q == 2 mod 3).
 * Output (stdout, text): "a b re im" per prime.
 * Phases use a two-level exact table cis(j*B/q) * cis(i/q), so no rotation drift.
 * Build: gcc -O2 -o gauss oct5_reflection_e2e_gauss.c -lm
 */
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <stdint.h>

typedef long long ll;
static ll pw(ll b, ll e, ll m){ ll r=1; b%=m; if(b<0)b+=m; while(e){ if(e&1) r=(__int128)r*b%m; b=(__int128)b*b%m; e>>=1;} return r; }
static int factor_small(ll n, ll *ps){ int k=0; for(ll d=2; d*d<=n; d++){ if(n%d==0){ ps[k++]=d; while(n%d==0) n/=d; } } if(n>1) ps[k++]=n; return k; }

#define BLK 1024
static double *T1r,*T1i,*T2r,*T2i; static ll T1n=0;
static void tables(ll q){
  ll n1 = q/BLK + 2;
  if(n1 > T1n){ T1r=realloc(T1r,n1*sizeof(double)); T1i=realloc(T1i,n1*sizeof(double)); T1n=n1; }
  if(!T2r){ T2r=malloc(BLK*sizeof(double)); T2i=malloc(BLK*sizeof(double)); }
  for(ll j=0;j<n1;j++){ double t=2*M_PI*(double)((j*BLK)%q)/(double)q; T1r[j]=cos(t); T1i[j]=sin(t); }
  for(ll i=0;i<BLK;i++){ double t=2*M_PI*(double)i/(double)q; T2r[i]=cos(t); T2i[i]=sin(t); }
}
static inline void cis_idx(ll idx, double *re, double *im){
  ll j=idx/BLK, i=idx%BLK; double a=T1r[j], b=T1i[j], c=T2r[i], d=T2i[i];
  *re=a*c-b*d; *im=a*d+b*c;
}

/* F_q[omega] arithmetic, omega^2 = -1 - omega */
static void fmul(ll q, ll x1, ll x2, ll y1, ll y2, ll *z1, ll *z2){
  ll a = (x1*y1 - x2*y2) % q; ll b = (x1*y2 + x2*y1 - x2*y2) % q;
  if(a<0)a+=q; if(b<0)b+=q; *z1=a; *z2=b;
}
static void fpow(ll q, ll x1, ll x2, ll e, ll *z1, ll *z2){
  ll r1=1,r2=0,b1=x1%q,b2=x2%q; if(b1<0)b1+=q; if(b2<0)b2+=q;
  while(e){ if(e&1) fmul(q,r1,r2,b1,b2,&r1,&r2); fmul(q,b1,b2,b1,b2,&b1,&b2); e>>=1; }
  *z1=r1; *z2=r2;
}

int main(void){
  ll a,b; double om_r=-0.5, om_i=sqrt(3.0)/2;
  double Wr[3]={1,om_r,om_r}, Wi[3]={0,om_i,-om_i};
  while(scanf("%lld %lld",&a,&b)==2){
    double S[3][2]={{0,0},{0,0},{0,0}};
    if(b!=0){
      ll q = a*a - a*b + b*b;
      ll binv = pw(((b%q)+q)%q, q-2, q);
      ll r = ((-a%q+q)%q) * binv % q;            /* omega == r mod p */
      if((r*r + r + 1) % q != 0){ fprintf(stderr,"bad r %lld %lld\n",a,b); return 1; }
      ll ps[64]; int np=factor_small(q-1,ps); ll g=2;
      for(;;g++){ int ok=1; for(int i=0;i<np;i++) if(pw(g,(q-1)/ps[i],q)==1){ok=0;break;} if(ok)break; }
      ll t = pw(g,(q-1)/3,q); int kg = (t==1)?0:((t==r)?1:2);
      if(kg==2 && t != r*r%q){ fprintf(stderr,"bad kg\n"); return 1; }
      if(kg==0){ fprintf(stderr,"generator?\n"); return 1; }
      tables(q);
      ll mult = ((2*a - b) % q + q) % q;
      /* iterate y = g^k * mult directly; fast modmul via double reciprocal (q < 2^26, products < 2^52) */
      double qinv = 1.0/(double)q;
      ll y = mult; int e = 0;
      for(ll k=0;k<q-1;k++){
        double re,im; cis_idx(y,&re,&im);
        S[e][0]+=re; S[e][1]+=im;
        e += kg; if(e>=3) e-=3;
        ll t = y*g; ll kq = (ll)((double)t*qinv); t -= kq*q; while(t<0) t+=q; while(t>=q) t-=q; y = t;
      }
    } else {
      ll q = -a;  /* p = -q */
      ll Q = q*q - 1; ll ps[64]; int np=factor_small(Q,ps);
      ll g1=-1,g2=-1;
      for(ll u=0;u<q && g1<0;u++) for(ll v=1;v<q;v++){
        int ok=1; for(int i=0;i<np;i++){ ll z1,z2; fpow(q,u,v,Q/ps[i],&z1,&z2); if(z1==1&&z2==0){ok=0;break;} }
        if(ok){ g1=u; g2=v; break; }
      }
      ll t1,t2; fpow(q,g1,g2,Q/3,&t1,&t2);
      int kg = (t1==1&&t2==0)?0:((t1==0&&t2==1)?1:(((t1==q-1)&&(t2==q-1))?2:-1));
      if(kg<=0){ fprintf(stderr,"inert kg fail q=%lld (%lld,%lld)\n",q,t1,t2); return 1; }
      tables(q);
      ll x1=1,x2=0;
      for(ll k=0;k<Q;k++){
        ll idx = ((-(2*x1 - x2)) % q + q) % q;
        double re,im; cis_idx(idx,&re,&im);
        int e=(int)((k*kg)%3); S[e][0]+=re; S[e][1]+=im;
        fmul(q,x1,x2,g1,g2,&x1,&x2);
      }
    }
    double gr=0,gi=0;
    for(int e=0;e<3;e++){ gr += Wr[e]*S[e][0]-Wi[e]*S[e][1]; gi += Wr[e]*S[e][1]+Wi[e]*S[e][0]; }
    printf("%lld %lld %.17g %.17g\n",a,b,gr,gi);
  }
  return 0;
}
