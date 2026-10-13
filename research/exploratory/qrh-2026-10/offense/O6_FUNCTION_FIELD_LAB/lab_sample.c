/* lab_sample.c -- N uniformly random monic rows u of ONE exact degree m (m >= 7: members of infinite
 * monodromy). Each A_u(d) is EXACT: L(x,psi_u) = sum_k c_k x^k with c_k = sum_{deg n = k} chi0(Res(u,n))
 * computed by direct enumeration of monic n, deg n < m, then 1/L to degree dmax in Z[omega].
 * The average over sampled rows is a Monte Carlo estimate of the row average (EMPIRICAL).
 * Usage: lab_sample q m dmax N seed
 * Output per d: d N sum|A|^2/q^d sum(|A|^2/q^d)^2 sum coprime_sqfree(u,d)/q^d max|A|^2/q^d
 * (shared code below is copied from lab_core.c, whose header follows)
 * lab_core.c -- exact sextic Moebius family over F_q[T], q prime, q = 1 mod 6.
 *
 * A_u(d) = sum_{n monic, deg n = d} mu(n) chi_n(u),  chi_n(u) = (u/n)_6 = chi0(Res(n,u)),
 * chi0(a) = zeta6^{dlog_g(a)}  (g = least primitive root mod q).
 * Reciprocity: chi_n(u) = chi0(-1)^{deg n deg u} psi_u(n), psi_u(n) = chi0(Res(u,n)) is a
 * Dirichlet character mod u, so A_u(d) = chi0(-1)^{d deg u} [x^d] 1/L(x,psi_u).
 * L(x,psi_u) is computed EXACTLY in Z[omega] from its Euler product over primes P,
 * deg P < deg u (it is a polynomial of degree < deg u unless psi_u is trivial, i.e. u = v^6).
 * All arithmetic is integer (Z[omega], __int128). Output: M2(d;m) = sum_{u monic, deg u <= m}
 * |A_u(d)|^2, the exact diagonal Diag(d;m) = sum_u #{n sqfree, deg d, (n,u)=1}, max_u |A_u|^2,
 * and per-degree row counts.  Usage: lab_core q mmax dmax
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef __int128 i128;
typedef long long ll;
static int q, mmax, dmax;
static int dlog6[64];          /* dlog mod 6, -1 for 0 */
static int inv_[64];

/* polynomial: coeff array c[0..deg], deg<0 means zero */
typedef struct { int deg; int c[16]; } poly;

static void decode(ll idx, int k, poly *p) { /* monic of degree k, idx = lower coeffs base q */
  p->deg = k; for (int i = 0; i < k; i++) { p->c[i] = idx % q; idx /= q; } p->c[k] = 1; }

static int powm(int a, int e) { int r = 1; a %= q; if (a < 0) a += q; while (e > 0) { if (e & 1) r = r * a % q; a = a * a % q; e >>= 1; } return r; }

/* resultant Res(A,B) = lc(A)^{deg B} prod_{A(t)=0} B(t), returned mod q */
static int resultant(const poly *A0, const poly *B0) {
  poly A = *A0, B = *B0; int res = 1;
  while (1) {
    if (B.deg < 0) return 0;
    if (A.deg == 0) return powm(A.c[0], B.deg) * res % q;
    if (B.deg == 0) return powm(B.c[0], A.deg) * res % q;
    /* R = B mod A */
    int n = A.deg, m = B.deg; poly R = B; int ilc = inv_[A.c[n]];
    for (int i = R.deg; i >= n; i--) {
      int f = R.c[i] * ilc % q; if (!f) continue;
      for (int j = 0; j <= n; j++) R.c[i - n + j] = (R.c[i - n + j] - f * A.c[j]) % q, R.c[i-n+j] += (R.c[i-n+j] < 0 ? q : 0);
    }
    int r = (R.deg < n ? R.deg : n - 1); while (r >= 0 && R.c[r] == 0) r--; R.deg = r;
    if (r < 0) return 0;
    /* Res(A,B) = lc(A)^{m-r} Res(A,R);  Res(A,R) = (-1)^{n r} Res(R,A) */
    res = res * powm(A.c[n], m - r) % q;
    if ((n * r) & 1) res = (q - res) % q;
    B = A; A = R;   /* now compute Res(R, A_old) */
  }
}

/* Z[omega] arithmetic, omega^2 = -1 - omega */
typedef struct { i128 a, b; } zw;
static const zw Z6[6] = { {1,0},{1,1},{0,1},{-1,0},{-1,-1},{0,-1} };
static inline zw mul(zw x, zw y) { zw r; r.a = x.a*y.a - x.b*y.b; r.b = x.a*y.b + x.b*y.a - x.b*y.b; return r; }
static inline zw add(zw x, zw y) { zw r = {x.a+y.a, x.b+y.b}; return r; }
static inline i128 nrm(zw x) { return x.a*x.a - x.a*x.b + x.b*x.b; }

static void pr128(FILE *f, i128 v) { char buf[64]; int i = 63; buf[i] = 0; int neg = v < 0; if (neg) v = -v; if (v == 0) buf[--i] = '0'; while (v > 0) { buf[--i] = '0' + (int)(v % 10); v /= 10; } if (neg) buf[--i] = '-'; fputs(buf + i, f); }


int main(int argc, char **argv) {
  q = atoi(argv[1]); int m = atoi(argv[2]); dmax = atoi(argv[3]); ll NS = atoll(argv[4]); srand48(atol(argv[5]));
  int g = 2; for (;; g++) { int ok = 1; for (int e = 1; e < q - 1; e++) if (powm(g, e) == 1) { ok = 0; break; } if (ok) break; }
  dlog6[0] = -1; { int x = 1; for (int e = 0; e < q - 1; e++) { dlog6[x] = e % 6; x = x * g % q; } }
  for (int a = 1; a < q; a++) inv_[a] = powm(a, q - 2);
  int D = dmax + 1;
  double *S1 = calloc(D, sizeof(double)), *S2 = calloc(D, sizeof(double)), *SC = calloc(D, sizeof(double)), *MX = calloc(D, sizeof(double));
  zw *L = malloc(sizeof(zw) * (m + 1)); zw *inv = malloc(sizeof(zw) * (D + 1)); i128 *cop = malloc(sizeof(i128) * (D + 1));
  i128 *sq = calloc(D + 1, sizeof(i128)); { i128 qp = 1; sq[0] = 1; for (int j = 1; j <= dmax; j++) { i128 prev = qp; qp *= q; sq[j] = (j == 1) ? q : qp - prev; } }
  ll tm = 1; for (int i = 0; i < m; i++) tm *= q;
  ll nsq = 0;
  for (ll s = 0; s < NS; s++) {
    ll idx = (ll)(drand48() * (double)tm); if (idx >= tm) idx = tm - 1;
    poly u; decode(idx, m, &u);
    /* character sums c_k for k < m, and degrees of prime factors (via linear/small factor detection: gcd test with each monic n of deg <= m/2 that is irreducible is costly; instead use L itself) */
    for (int k = 0; k < m; k++) { L[k].a = L[k].b = 0; }
    L[0].a = 1;
    int zero_lin = 0;
    for (int k = 1; k < m; k++) { ll t = 1; for (int i = 0; i < k; i++) t *= q; ll cnt[6] = {0,0,0,0,0,0};
      for (ll j = 0; j < t; j++) { poly n; decode(j, k, &n); int r = resultant(&u, &n); if (!r) continue; cnt[dlog6[r]]++; }
      zw acc = {0, 0}; for (int e = 0; e < 6; e++) { acc.a += (i128)cnt[e] * Z6[e].a; acc.b += (i128)cnt[e] * Z6[e].b; }
      L[k] = acc; (void)zero_lin; }
    /* squarefree test for the coprime count: we need prod over P|u (1+x^{deg P})^{-1}; get prime-factor
       degrees from the factorization by trial division with monic irreducibles found on the fly is costly,
       so we compute the coprime-squarefree count directly from the Euler-free identity
       #{n sqfree deg d,(n,u)=1} = [x^d] (1-qx^2)/(1-qx) / prod_{P|u}(1+x^{deg P}); prime factor degrees
       are obtained by distinct-degree factorization: deg-j part = gcd(u, T^{q^j} - T). */
    int fdeg[32], nf = 0;
    { /* distinct-degree factorization */
      poly f = u; poly x; memset(&x, 0, sizeof x); x.deg = 1; x.c[1] = 1; poly h = x; /* h = T^{q^j} mod f */
      for (int j = 1; 2 * j <= f.deg || (f.deg > 0 && j <= f.deg); j++) {
        if (f.deg <= 0) break;
        /* h = h^q mod f */
        poly r; memset(&r, 0, sizeof r); r.deg = 0; r.c[0] = 1; poly b = h; int e = q;
        while (e) { if (e & 1) { poly z; memset(&z, 0, sizeof z); z.deg = r.deg + b.deg; for (int i = 0; i <= r.deg; i++) for (int k2 = 0; k2 <= b.deg; k2++) z.c[i + k2] = (z.c[i + k2] + r.c[i] * b.c[k2]) % q;
              /* reduce z mod f */ for (int i = z.deg; i >= f.deg; i--) { int c = z.c[i] * inv_[f.c[f.deg]] % q; if (c) for (int k2 = 0; k2 <= f.deg; k2++) { z.c[i - f.deg + k2] = (z.c[i - f.deg + k2] - c * f.c[k2]) % q; if (z.c[i - f.deg + k2] < 0) z.c[i - f.deg + k2] += q; } }
              int dd = f.deg - 1; while (dd >= 0 && z.c[dd] == 0) dd--; z.deg = dd < 0 ? 0 : dd; r = z; }
          e >>= 1; if (!e) break;
          poly z; memset(&z, 0, sizeof z); z.deg = 2 * b.deg; for (int i = 0; i <= b.deg; i++) for (int k2 = 0; k2 <= b.deg; k2++) z.c[i + k2] = (z.c[i + k2] + b.c[i] * b.c[k2]) % q;
          for (int i = z.deg; i >= f.deg; i--) { int c = z.c[i] * inv_[f.c[f.deg]] % q; if (c) for (int k2 = 0; k2 <= f.deg; k2++) { z.c[i - f.deg + k2] = (z.c[i - f.deg + k2] - c * f.c[k2]) % q; if (z.c[i - f.deg + k2] < 0) z.c[i - f.deg + k2] += q; } }
          int dd = f.deg - 1; while (dd >= 0 && z.c[dd] == 0) dd--; z.deg = dd < 0 ? 0 : dd; b = z; }
        h = r;
        /* g = gcd(f, h - T) */
        poly hm = h; if (hm.deg < 1) { for (int i = hm.deg + 1; i <= 1; i++) hm.c[i] = 0; hm.deg = 1; } hm.c[1] = (hm.c[1] - 1 + q) % q;
        { int dd = hm.deg; while (dd >= 0 && hm.c[dd] == 0) dd--; hm.deg = dd; }
        poly A = f, B = hm;
        while (B.deg >= 0) { /* A mod B */
          poly R = A; int ilc = inv_[B.c[B.deg]];
          for (int i = R.deg; i >= B.deg; i--) { int c = R.c[i] * ilc % q; if (!c) continue; for (int k2 = 0; k2 <= B.deg; k2++) { R.c[i - B.deg + k2] = (R.c[i - B.deg + k2] - c * B.c[k2]) % q; if (R.c[i - B.deg + k2] < 0) R.c[i - B.deg + k2] += q; } }
          int dd = (R.deg < B.deg ? R.deg : B.deg - 1); while (dd >= 0 && R.c[dd] == 0) dd--; R.deg = dd; A = B; B = R; }
        int gdeg = A.deg; /* gcd degree */
        if (gdeg > 0) { int cntp = gdeg / j; for (int t2 = 0; t2 < cntp; t2++) fdeg[nf++] = j;
          /* f = f / gcd: divide f by monic A */
          int ilc = inv_[A.c[A.deg]]; poly Q2; memset(&Q2, 0, sizeof Q2); Q2.deg = f.deg - A.deg; poly R = f;
          for (int i = R.deg; i >= A.deg; i--) { int c = R.c[i] * ilc % q; Q2.c[i - A.deg] = c; if (!c) continue; for (int k2 = 0; k2 <= A.deg; k2++) { R.c[i - A.deg + k2] = (R.c[i - A.deg + k2] - c * A.c[k2]) % q; if (R.c[i - A.deg + k2] < 0) R.c[i - A.deg + k2] += q; } }
          f = Q2; /* h stays T^{q^j} mod old f; reduce mod new f */
          for (int i = h.deg; i >= f.deg && f.deg > 0; i--) { int c = h.c[i] * inv_[f.c[f.deg]] % q; if (c) for (int k2 = 0; k2 <= f.deg; k2++) { h.c[i - f.deg + k2] = (h.c[i - f.deg + k2] - c * f.c[k2]) % q; if (h.c[i - f.deg + k2] < 0) h.c[i - f.deg + k2] += q; } }
          { int dd = f.deg - 1; if (dd < 0) dd = 0; while (dd > 0 && h.c[dd] == 0) dd--; h.deg = dd; }
          /* repeated factors: keep dividing while gcd persists is not needed for the coprime count (only the set of primes matters),
             but f may still contain the same primes; remove them by repeated gcd at the same j */
          j--; continue;
        }
      }
      if (f.deg > 0) fdeg[nf++] = f.deg;
    }
    /* sixth power check not needed for m not divisible by 6 (u = v^6 impossible); for 6|m test directly */
    int is6 = 0; if (m % 6 == 0) { int kv = m / 6; ll tv = 1; for (int i = 0; i < kv; i++) tv *= q;
      for (ll iv = 0; iv < tv && !is6; iv++) { poly v; decode(iv, kv, &v); poly w; memset(&w, 0, sizeof w); w.deg = 0; w.c[0] = 1;
        for (int s6 = 0; s6 < 6; s6++) { poly z; memset(&z, 0, sizeof z); z.deg = w.deg + v.deg; for (int a = 0; a <= w.deg; a++) for (int b2 = 0; b2 <= v.deg; b2++) z.c[a + b2] = (z.c[a + b2] + w.c[a] * v.c[b2]) % q; w = z; }
        int same = 1; for (int i = 0; i <= m; i++) if (w.c[i] != u.c[i]) same = 0; if (same) is6 = 1; } }
    if (is6) { s--; continue; }
    inv[0].a = 1; inv[0].b = 0;
    for (int j = 1; j <= dmax; j++) { zw t = {0, 0}; for (int i = 1; i <= j && i < m; i++) t = add(t, mul(L[i], inv[j - i])); inv[j].a = -t.a; inv[j].b = -t.b; }
    for (int j = 0; j <= dmax; j++) cop[j] = sq[j];
    for (int f2 = 0; f2 < nf; f2++) for (int j = fdeg[f2]; j <= dmax; j++) cop[j] -= cop[j - fdeg[f2]];
    double qd = 1; for (int d = 0; d <= dmax; d++) { double v = (double)nrm(inv[d]) / qd; S1[d] += v; S2[d] += v * v; SC[d] += (double)cop[d] / qd; if (v > MX[d]) MX[d] = v; qd *= q; }
    nsq++;
  }
  printf("# q=%d m=%d N=%lld  columns: d N S1=sum|A|^2/q^d S2=sum(|A|^2/q^d)^2 SC=sum coprime_sqfree/q^d max\n", q, m, nsq);
  for (int d = 0; d <= dmax; d++) printf("%d %lld %.10g %.10g %.10g %.6g\n", d, nsq, S1[d], S2[d], SC[d], MX[d]);
  return 0;
}
