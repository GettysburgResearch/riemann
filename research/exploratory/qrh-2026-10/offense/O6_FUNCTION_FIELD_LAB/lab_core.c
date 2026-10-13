/* lab_core.c -- exact sextic Moebius family over F_q[T], q prime, q = 1 mod 6.
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
  q = atoi(argv[1]); mmax = atoi(argv[2]); dmax = atoi(argv[3]);
  int g = 2; for (;; g++) { int ok = 1; for (int e = 1; e < q - 1; e++) if (powm(g, e) == 1) { ok = 0; break; } if (ok) break; }
  dlog6[0] = -1; { int x = 1; for (int e = 0; e < q - 1; e++) { dlog6[x] = e % 6; x = x * g % q; } }
  for (int a = 1; a < q; a++) inv_[a] = powm(a, q - 2);
  int chi0m1 = dlog6[q - 1]; /* chi0(-1) exponent: 0 or 3 */
  /* primes of degree < mmax: enumerate monic, test irreducible by trial division with smaller primes */
  int maxp = mmax - 1; ll np = 0, cap = 1; for (int k = 1; k <= maxp; k++) { ll t = 1; for (int i = 0; i < k; i++) t *= q; cap += t; }
  poly *P = malloc(sizeof(poly) * (cap + 1));
  for (int k = 1; k <= maxp; k++) { ll t = 1; for (int i = 0; i < k; i++) t *= q;
    for (ll idx = 0; idx < t; idx++) { poly u; decode(idx, k, &u); int irr = 1;
      for (ll j = 0; j < np && 2 * P[j].deg <= k; j++) if (resultant(&P[j], &u) == 0) { irr = 0; break; }
      if (irr) P[np++] = u; } }
  fprintf(stderr, "q=%d g=%d primes(deg<=%d)=%lld\n", q, g, maxp, np);
  /* accumulators */
  int D = dmax + 1;
  i128 *M2 = calloc((size_t)D * (mmax + 1), sizeof(i128));     /* by exact deg u */
  i128 *DG = calloc((size_t)D * (mmax + 1), sizeof(i128));
  double *MX = calloc((size_t)D * (mmax + 1), sizeof(double));
  ll *rows = calloc(mmax + 1, sizeof(ll));
  /* sqfree count generating series: S(x) = (1-qx^2)/(1-qx) coefficients */
  i128 *sq = calloc(D + 1, sizeof(i128)); { i128 qp = 1; for (int j = 0; j <= dmax; j++) { sq[j] = (j == 0) ? 1 : (j == 1 ? q : qp * q - qp / q * q * 0); if (j >= 2) sq[j] = qp * q - qp; qp *= q; } }
  /* recompute sq properly: sq[0]=1, sq[1]=q, sq[j]=q^j - q^{j-1} */
  { i128 qp = 1; sq[0] = 1; for (int j = 1; j <= dmax; j++) { i128 prev = qp; qp *= q; sq[j] = (j == 1) ? q : qp - prev; } }
  FILE *fl = fopen(argc > 4 ? argv[4] : "/dev/null", "w"); /* optional per-row dump (small q^m only) */
  zw *L = malloc(sizeof(zw) * (mmax + 2)); zw *inv = malloc(sizeof(zw) * (D + 1));
  i128 *cop = malloc(sizeof(i128) * (D + 1)); int *fdeg = malloc(sizeof(int) * 64);
  for (int k = 0; k <= mmax; k++) {
    ll t = 1; for (int i = 0; i < k; i++) t *= q; rows[k] = t;
    for (ll idx = 0; idx < t; idx++) {
      poly u; decode(idx, k, &u);
      /* L(x,psi_u) mod x^k via Euler product, and prime factor degrees */
      for (int i = 0; i < k; i++) L[i].a = L[i].b = 0; L[0].a = 1;
      int nf = 0, sumfdeg = 0, trivial = 1;
      for (ll j = 0; j < np && P[j].deg < k; j++) {
        int r = resultant(&u, &P[j]);            /* psi_u(P) = chi0(Res(u,P)) */
        if (r == 0) { fdeg[nf++] = P[j].deg; sumfdeg += P[j].deg; continue; }
        int e = dlog6[r]; if (e) trivial = 0;
        int dp = P[j].deg;
        /* multiply L by 1/(1 - z x^dp) = sum z^i x^{i dp} */
        for (int i = dp; i < k; i++) { L[i] = add(L[i], mul(Z6[e], L[i - dp])); }
      }
      if (k > 0 && nf == 0) { fdeg[nf++] = k; sumfdeg = k; } /* u irreducible */
      /* trivial psi_u happens only for u = v^6; detect: all psi(P)=1 for deg P<k is not enough in general,
         so test u = v^6 directly when 6 | k */
      int is6 = 0;
      if (k % 6 == 0) { /* check u is a 6th power: brute force v monic deg k/6 */
        int kv = k / 6; ll tv = 1; for (int i = 0; i < kv; i++) tv *= q;
        for (ll iv = 0; iv < tv && !is6; iv++) { poly v; decode(iv, kv, &v); poly w; w.deg = 0; w.c[0] = 1;
          for (int s = 0; s < 6; s++) { poly z; memset(&z, 0, sizeof z); z.deg = w.deg + v.deg;
            for (int a = 0; a <= w.deg; a++) for (int b = 0; b <= v.deg; b++) z.c[a+b] = (z.c[a+b] + w.c[a]*v.c[b]) % q; w = z; }
          int same = (w.deg == u.deg); for (int i = 0; same && i <= k; i++) if (w.c[i] != u.c[i]) same = 0; if (same) is6 = 1; }
      }
      (void)trivial;
      /* 1/L coefficients */
      if (is6 || k == 0) { /* 1/L = (1 - q x) prod_{P|u} (1 - x^{deg P})^{-1} */
        for (int j = 0; j <= dmax; j++) { inv[j].a = (j == 0) ? 1 : (j == 1 ? -q : 0); inv[j].b = 0; }
        for (int f = 0; f < nf && k > 0; f++) for (int j = fdeg[f]; j <= dmax; j++) inv[j] = add(inv[j], inv[j - fdeg[f]]);
      } else {
        inv[0].a = 1; inv[0].b = 0;
        for (int j = 1; j <= dmax; j++) { zw s = {0, 0};
          for (int i = 1; i <= j && i < k; i++) s = add(s, mul(L[i], inv[j - i]));
          inv[j].a = -s.a; inv[j].b = -s.b; }
      }
      /* coprime-sqfree counts: S(x) / prod_{P|u}(1 + x^{deg P}) */
      for (int j = 0; j <= dmax; j++) cop[j] = sq[j];
      for (int f = 0; f < nf; f++) for (int j = fdeg[f]; j <= dmax; j++) cop[j] -= cop[j - fdeg[f]];
      for (int d = 0; d <= dmax; d++) {
        i128 n2 = nrm(inv[d]);
        M2[(size_t)d * (mmax + 1) + k] += n2; DG[(size_t)d * (mmax + 1) + k] += cop[d];
        double v = (double)n2; if (v > MX[(size_t)d * (mmax + 1) + k]) MX[(size_t)d * (mmax + 1) + k] = v;
      }
      if (argc > 4) { fprintf(fl, "%d %lld %d", k, idx, is6); for (int d = 0; d <= dmax; d++) { fputc(' ', fl); pr128(fl, inv[d].a); fputc(',', fl); pr128(fl, inv[d].b); } fputc('\n', fl); }
    }
    fprintf(stderr, "done deg %d\n", k);
  }
  /* print per exact degree k: d k rows M2 Diag max */
  printf("# q=%d g=%d chi0(-1)exp=%d  columns: d k rows M2_k Diag_k maxA2_k\n", q, g, chi0m1);
  for (int d = 0; d <= dmax; d++) for (int k = 0; k <= mmax; k++) {
    printf("%d %d %lld ", d, k, rows[k]); pr128(stdout, M2[(size_t)d*(mmax+1)+k]); putchar(' ');
    pr128(stdout, DG[(size_t)d*(mmax+1)+k]); printf(" %.6e\n", MX[(size_t)d*(mmax+1)+k]); }
  if (argc > 4) fclose(fl);
  return 0;
}
