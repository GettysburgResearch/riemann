/* dual_energy.c -- the Oct 5 Step 3 dual family in the function-field lab, EXACT.
 *
 * After Poisson in u and Moebius absorption (mu(n) g_n(chi_n) = (-g_1)^d chi0(Res(n,n')), see
 * gauss_exact.py), the coprime-pair block of M2 is  q^{M-d} sum_{h in V_{2d-M}} sum_{(a,b)=1} beta_h(a) conj beta_h(b),
 * beta_h(n) = chi0(D_n) conj(chi_n(h)),  D_n = Res(n,n'),  n monic squarefree of degree d.
 * The Oct 5 positivity step bounds it by the full dual mean square
 *     E(K) = sum_{h in V_K, h != 0} |B_h|^2,   B_h = sum_n beta_h(n),   K = 2d - M,
 * whose diagonal is DD(K) = sum_h #{n : (n,h)=1}.  We output E and DD per exact degree of h
 * (monic h only; |B_{ch}| = |B_h| for c in F_q^*, so the full sums are (q-1) times these).
 * Usage: dual_energy q d Kmax
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
typedef long long ll;
typedef __int128 i128;
static int q;
static int dlog6[64], inv_[64];
typedef struct { int deg; int c[24]; } poly;
static int powm(int a, int e) { int r = 1; a %= q; if (a < 0) a += q; while (e > 0) { if (e & 1) r = r * a % q; a = a * a % q; e >>= 1; } return r; }
static void decode(ll idx, int k, poly *p) { memset(p, 0, sizeof *p); p->deg = k; for (int i = 0; i < k; i++) { p->c[i] = idx % q; idx /= q; } p->c[k] = 1; }
static int resultant(const poly *A0, const poly *B0) {
  poly A = *A0, B = *B0; int res = 1;
  while (1) {
    if (B.deg < 0) return 0;
    if (A.deg == 0) return powm(A.c[0], B.deg) * res % q;
    if (B.deg == 0) return powm(B.c[0], A.deg) * res % q;
    int n = A.deg, m = B.deg; poly R = B; int ilc = inv_[A.c[n]];
    for (int i = R.deg; i >= n; i--) { int f = R.c[i] * ilc % q; if (!f) continue;
      for (int j = 0; j <= n; j++) { int v = (R.c[i - n + j] - f * A.c[j]) % q; R.c[i - n + j] = v < 0 ? v + q : v; } }
    int r = (R.deg < n ? R.deg : n - 1); while (r >= 0 && R.c[r] == 0) r--; R.deg = r;
    if (r < 0) return 0;
    res = res * powm(A.c[n], m - r) % q; if ((n * r) & 1) res = (q - res) % q;
    B = A; A = R;
  }
}
static void pr128(i128 v) { char buf[64]; int i = 63; buf[i] = 0; int neg = v < 0; if (neg) v = -v; if (v == 0) buf[--i] = '0'; while (v > 0) { buf[--i] = '0' + (int)(v % 10); v /= 10; } if (neg) buf[--i] = '-'; fputs(buf + i, stdout); }
int main(int argc, char **argv) {
  q = atoi(argv[1]); int d = atoi(argv[2]); int Kmax = atoi(argv[3]);
  int g = 2; for (;; g++) { int ok = 1; for (int e = 1; e < q - 1; e++) if (powm(g, e) == 1) { ok = 0; break; } if (ok) break; }
  dlog6[0] = -1; { int x = 1; for (int e = 0; e < q - 1; e++) { dlog6[x] = e % 6; x = x * g % q; } }
  for (int a = 1; a < q; a++) inv_[a] = powm(a, q - 2);
  ll nd = 1; for (int i = 0; i < d; i++) nd *= q;
  poly *N = malloc(sizeof(poly) * nd); int *an = malloc(sizeof(int) * nd); ll nn = 0;
  for (ll idx = 0; idx < nd; idx++) { poly n; decode(idx, d, &n); poly dn; memset(&dn, 0, sizeof dn); dn.deg = d - 1;
    for (int i = 1; i <= d; i++) dn.c[i - 1] = (i % q) * n.c[i] % q;
    while (dn.deg >= 0 && dn.c[dn.deg] == 0) dn.deg--;
    int r = resultant(&n, &dn); if (r == 0) continue; N[nn] = n; an[nn] = dlog6[r]; nn++; }
  fprintf(stderr, "q=%d d=%d squarefree columns=%lld\n", q, d, nn);
  /* Z[omega] via counts of 6th roots: B = sum zeta^e  -> |B|^2 = sum_{e,f} c_e c_f Re(zeta^{e-f}) ; use integer formula */
  printf("# q=%d d=%d ncols=%lld  columns: k(deg h) nrows_monic E_k DD_k   [E_k=sum_{h monic deg k}|B_h|^2, DD_k=sum_h #{n:(n,h)=1}]\n", q, d, nn);
  for (int k = 0; k <= Kmax; k++) {
    ll nh = 1; for (int i = 0; i < k; i++) nh *= q;
    i128 E = 0, DD = 0;
    for (ll ih = 0; ih < nh; ih++) {
      poly h; decode(ih, k, &h); ll c[6] = {0,0,0,0,0,0}; ll cop = 0;
      for (ll j = 0; j < nn; j++) { int r = resultant(&N[j], &h); if (!r) continue; cop++;
        int e = (an[j] - dlog6[r] + 12) % 6; c[e]++; }
      /* B = sum_e c_e zeta6^e ; |B|^2 = sum_{e,f} c_e c_f cos(pi(e-f)/3) = (1/2) sum c_e c_f w(e-f), w = 2,1,-1,-2,-1,1 */
      static const int w[6] = {2, 1, -1, -2, -1, 1}; i128 s = 0;
      for (int e = 0; e < 6; e++) for (int f = 0; f < 6; f++) s += (i128)c[e] * c[f] * w[(e - f + 6) % 6];
      E += s / 2; DD += cop;
    }
    printf("%d %lld ", k, nh); pr128(E); putchar(' '); pr128(DD); putchar('\n'); fflush(stdout);
  }
  return 0;
}
