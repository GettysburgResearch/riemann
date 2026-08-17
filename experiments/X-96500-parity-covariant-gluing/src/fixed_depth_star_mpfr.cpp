#include <algorithm>
#include <cmath>
#include <cstdlib>
#include <iomanip>
#include <iostream>
#include <stdexcept>
#include <string>
#include <utility>
#include <vector>
#include "mpfr_min.h"

extern "C" {
int mpfr_set(mpfr_ptr, mpfr_srcptr, mpfr_rnd_t);
int mpfr_set_si(mpfr_ptr, long, mpfr_rnd_t);
int mpfr_add(mpfr_ptr, mpfr_srcptr, mpfr_srcptr, mpfr_rnd_t);
int mpfr_sub(mpfr_ptr, mpfr_srcptr, mpfr_srcptr, mpfr_rnd_t);
int mpfr_mul(mpfr_ptr, mpfr_srcptr, mpfr_srcptr, mpfr_rnd_t);
int mpfr_div(mpfr_ptr, mpfr_srcptr, mpfr_srcptr, mpfr_rnd_t);
int mpfr_neg(mpfr_ptr, mpfr_srcptr, mpfr_rnd_t);
int mpfr_cmp(mpfr_srcptr, mpfr_srcptr);
int mpfr_cmp_si(mpfr_srcptr, long);
}

static constexpr mpfr_prec_t PREC = 256;

class R {
 public:
  mpfr_t x;
  R() { mpfr_init2(x, PREC); mpfr_set_ui(x, 0, MPFR_RNDN); }
  explicit R(unsigned long v) { mpfr_init2(x, PREC); mpfr_set_ui(x, v, MPFR_RNDN); }
  R(const R& o) { mpfr_init2(x, PREC); mpfr_set(x, o.x, MPFR_RNDN); }
  R(R&& o) noexcept { mpfr_init2(x, PREC); mpfr_set(x, o.x, MPFR_RNDN); }
  R& operator=(const R& o) { if (this != &o) mpfr_set(x, o.x, MPFR_RNDN); return *this; }
  R& operator=(R&& o) noexcept { if (this != &o) mpfr_set(x, o.x, MPFR_RNDN); return *this; }
  ~R() { mpfr_clear(x); }
};

struct I {
  R lo, hi;
  I() = default;
  explicit I(long v) { mpfr_set_si(lo.x, v, MPFR_RNDN); mpfr_set_si(hi.x, v, MPFR_RNDN); }
  static I ui(unsigned long v) {
    I a; mpfr_set_ui(a.lo.x, v, MPFR_RNDN); mpfr_set_ui(a.hi.x, v, MPFR_RNDN); return a;
  }
  static I rational(long num, unsigned long den) {
    if (den == 0) throw std::runtime_error("zero denominator");
    I a; R nlo, nhi, d;
    mpfr_set_si(nlo.x, num, MPFR_RNDD); mpfr_set_si(nhi.x, num, MPFR_RNDU);
    mpfr_set_ui(d.x, den, MPFR_RNDN);
    mpfr_div(a.lo.x, nlo.x, d.x, MPFR_RNDD);
    mpfr_div(a.hi.x, nhi.x, d.x, MPFR_RNDU);
    return a;
  }
};

static I add(const I& a, const I& b) {
  I c; mpfr_add(c.lo.x, a.lo.x, b.lo.x, MPFR_RNDD); mpfr_add(c.hi.x, a.hi.x, b.hi.x, MPFR_RNDU); return c;
}
static I neg(const I& a) {
  I c; mpfr_neg(c.lo.x, a.hi.x, MPFR_RNDD); mpfr_neg(c.hi.x, a.lo.x, MPFR_RNDU); return c;
}
static I sub(const I& a, const I& b) { return add(a, neg(b)); }

static void min_assign(R& out, const R& a) { if (mpfr_cmp(a.x, out.x) < 0) mpfr_set(out.x, a.x, MPFR_RNDD); }
static void max_assign(R& out, const R& a) { if (mpfr_cmp(a.x, out.x) > 0) mpfr_set(out.x, a.x, MPFR_RNDU); }

static I mul(const I& a, const I& b) {
  R l1,l2,l3,l4,h1,h2,h3,h4;
  mpfr_mul(l1.x,a.lo.x,b.lo.x,MPFR_RNDD); mpfr_mul(l2.x,a.lo.x,b.hi.x,MPFR_RNDD);
  mpfr_mul(l3.x,a.hi.x,b.lo.x,MPFR_RNDD); mpfr_mul(l4.x,a.hi.x,b.hi.x,MPFR_RNDD);
  mpfr_mul(h1.x,a.lo.x,b.lo.x,MPFR_RNDU); mpfr_mul(h2.x,a.lo.x,b.hi.x,MPFR_RNDU);
  mpfr_mul(h3.x,a.hi.x,b.lo.x,MPFR_RNDU); mpfr_mul(h4.x,a.hi.x,b.hi.x,MPFR_RNDU);
  I c; mpfr_set(c.lo.x,l1.x,MPFR_RNDD); min_assign(c.lo,l2); min_assign(c.lo,l3); min_assign(c.lo,l4);
  mpfr_set(c.hi.x,h1.x,MPFR_RNDU); max_assign(c.hi,h2); max_assign(c.hi,h3); max_assign(c.hi,h4);
  return c;
}
static I reciprocal_positive(const I& a) {
  if (mpfr_cmp_si(a.lo.x,0) <= 0) throw std::runtime_error("nonpositive reciprocal interval");
  I c; R one(1); mpfr_div(c.lo.x,one.x,a.hi.x,MPFR_RNDD); mpfr_div(c.hi.x,one.x,a.lo.x,MPFR_RNDU); return c;
}
static I div_positive(const I& a, const I& b) { return mul(a, reciprocal_positive(b)); }

static I sqrt_ui(unsigned long n) {
  I a; R x(n); mpfr_sqrt(a.lo.x,x.x,MPFR_RNDD); mpfr_sqrt(a.hi.x,x.x,MPFR_RNDU); return a;
}
static I invsqrt_ui(unsigned long n) { return reciprocal_positive(sqrt_ui(n)); }
static I log_ui(unsigned long n) {
  I a; R x(n); mpfr_log(a.lo.x,x.x,MPFR_RNDD); mpfr_log(a.hi.x,x.x,MPFR_RNDU); return a;
}

static bool is_prime(int n) {
  if (n < 2) return false;
  if (n % 2 == 0) return n == 2;
  for (int d=3; 1LL*d*d<=n; d+=2) if (n%d==0) return false;
  return true;
}

struct DivMu { int d; int mu; };

class Certificate {
 public:
  int X;
  std::vector<I> invsqrt, logs, prefix_s, prefix_l;
  std::vector<DivMu> small_divs;
  std::vector<int> rough_primes;

  explicit Certificate(int x): X(x), invsqrt(x+1), logs(x+1), prefix_s(x+1), prefix_l(x+1) {
    prefix_s[0]=I(0); prefix_l[0]=I(0);
    for (int n=1;n<=X;n++) {
      invsqrt[n]=invsqrt_ui(n); logs[n]=log_ui(n);
      prefix_s[n]=add(prefix_s[n-1],invsqrt[n]);
      prefix_l[n]=add(prefix_l[n-1],mul(logs[n],invsqrt[n]));
    }
    std::vector<DivMu> ds{{1,1}};
    const int sp[] = {2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61};
    for (int p:sp) {
      auto old=ds;
      for (auto z:old) if (1LL*z.d*p<=X) ds.push_back({z.d*p,-z.mu});
    }
    std::sort(ds.begin(),ds.end(),[](auto a,auto b){return a.d<b.d;});
    small_divs=std::move(ds);
    for (int p=67;p<=X;p++) if (is_prime(p)) rough_primes.push_back(p);
  }

  I log_ratio(int numerator, int denominator) const {
    if (denominator<=0 || denominator>numerator) throw std::runtime_error("bad log ratio");
    return sub(logs[numerator],logs[denominator]);
  }

  I qrow(int denom, int j) const {
    int N=X/denom;
    if (N<j) return I(0);
    I A=I::rational(j+1,j-1);
    I B=I::rational((j+1)*(j-2),j*(j-1));
    I C=I::rational(2,j*(j-1));
    I ans=mul(mul(A,invsqrt[j]),log_ratio(X,denom*j));
    if (N>=j+1 && j>2) ans=sub(ans,mul(mul(B,invsqrt[j+1]),log_ratio(X,denom*(j+1))));
    if (N>=j+2) {
      I sd=sub(prefix_s[N],prefix_s[j+1]);
      I ld=sub(prefix_l[N],prefix_l[j+1]);
      I logy=log_ratio(X,denom);
      ans=add(ans,mul(C,sub(mul(logy,sd),ld)));
    }
    return ans;
  }

  I finite_euler(int outer_denom, int j) const {
    I ans(0);
    for (auto z:small_divs) {
      long long den=1LL*outer_denom*z.d;
      if (den*j>X) break;
      I term=mul(invsqrt[z.d],qrow((int)den,j));
      if (z.mu<0) term=neg(term);
      ans=add(ans,term);
    }
    return ans;
  }

  std::pair<I,int> star(int j) const {
    I ans=finite_euler(1,j); int cnt=0;
    for (int p:rough_primes) {
      if (1LL*p*j>X) break;
      ans=sub(ans,mul(invsqrt[p],finite_euler(p,j)));
      cnt++;
    }
    return {ans,cnt};
  }
};

static long double lo_ld(const I& a){return mpfr_get_ld(a.lo.x,MPFR_RNDD);}
static long double hi_ld(const I& a){return mpfr_get_ld(a.hi.x,MPFR_RNDU);}

int main() {
  const int X=200000;
  Certificate c(X);
  auto [r2,n2]=c.star(2); auto [r3,n3]=c.star(3);
  if (mpfr_cmp_si(r2.hi.x,-11)>=0) { std::cerr<<"row2 upper bound not below -11\n"; return 2; }
  if (mpfr_cmp_si(r3.hi.x,-2)>=0) { std::cerr<<"row3 upper bound not below -2\n"; return 3; }
  std::cout<<std::setprecision(30);
  std::cout<<"{\n"
    <<"  \"classification\": \"PASS_MPFR_DIRECTED_TWO_LEVEL_STAR_NEGATIVITY\",\n"
    <<"  \"mpfr_version\": \""<<mpfr_get_version()<<"\",\n"
    <<"  \"precision_bits\": "<<PREC<<",\n"
    <<"  \"endpoint\": "<<X<<",\n"
    <<"  \"row_2\": {\"lower\": \""<<lo_ld(r2)<<"\", \"upper\": \""<<hi_ld(r2)<<"\", \"rough_primes\": "<<n2<<"},\n"
    <<"  \"row_3\": {\"lower\": \""<<lo_ld(r3)<<"\", \"upper\": \""<<hi_ld(r3)<<"\", \"rough_primes\": "<<n3<<"},\n"
    <<"  \"certified\": \"A_2(200000)<-11 and A_3(200000)<-2\",\n"
    <<"  \"rh_established_by_replay\": false\n"
    <<"}\n";
  return 0;
}
