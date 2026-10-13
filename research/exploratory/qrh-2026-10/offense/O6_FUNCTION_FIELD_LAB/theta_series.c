/* theta_series.c -- the lab dual sums B_h(d) = sum_{n monic sqfree, deg n = d} chi0(Res(n,n')) conj chi_n(h)
 * as a function of the column degree d, for all monic h of degree <= kmax.  EXACT (counts of sixth roots).
 * Over F_q(T) the Gauss-sum Dirichlet series sum_d B_h(d) x^d is rational (Hoffstein 1992); this prints the
 * sequence so that its vanishing / polar pattern in d can be read off.
 * Output per (deg h = k, d): number of h with B_h(d) != 0, sum_h |B_h(d)|^2, diagonal sum_h #{n:(n,h)=1},
 * and for h = 1 the value B_1(d) = a + b*omega.
 * Usage: theta_series q dmax kmax
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
typedef long long ll;
static int q; static int dlog6[64], inv_[64];
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
int main(int argc, char **argv) {
  q = atoi(argv[1]); int dmax = atoi(argv[2]); int kmax = atoi(argv[3]);
  int g = 2; for (;; g++) { int ok = 1; for (int e = 1; e < q - 1; e++) if (powm(g, e) == 1) { ok = 0; break; } if (ok) break; }
  dlog6[0] = -1; { int x = 1; for (int e = 0; e < q - 1; e++) { dlog6[x] = e % 6; x = x * g % q; } }
  for (int a = 1; a < q; a++) inv_[a] = powm(a, q - 2);
  ll nh = 0; ll cap = 0; { ll t = 1; for (int k = 0; k <= kmax; k++) { cap += t; t *= q; } }
  poly *H = malloc(sizeof(poly) * cap); int *hk = malloc(sizeof(int) * cap);
  { for (int k = 0; k <= kmax; k++) { ll t = 1; for (int i = 0; i < k; i++) t *= q; for (ll i = 0; i < t; i++) { decode(i, k, &H[nh]); hk[nh] = k; nh++; } } }
  ll (*cnt)[6] = malloc(sizeof(ll[6]) * nh); ll *cop = malloc(sizeof(ll) * nh);
  static const int w[6] = {2, 1, -1, -2, -1, 1};
  static const int W1[6] = {1, 1, 0, -1, -1, 0}, W2[6] = {0, 1, 1, 0, -1, -1};
  printf("# q=%d g=%d columns: d k #h #h_with_B!=0 sum|B_h|^2 sum_h#{n:(n,h)=1}   and lines 'B1 d a b' for h=1\n", q, g);
  for (int d = 1; d <= dmax; d++) {
    memset(cnt, 0, sizeof(ll[6]) * nh); memset(cop, 0, sizeof(ll) * nh);
    ll nd = 1; for (int i = 0; i < d; i++) nd *= q;
    for (ll idx = 0; idx < nd; idx++) {
      poly n; decode(idx, d, &n); poly dn; memset(&dn, 0, sizeof dn); dn.deg = d - 1;
      for (int i = 1; i <= d; i++) dn.c[i - 1] = (i % q) * n.c[i] % q;
      while (dn.deg >= 0 && dn.c[dn.deg] == 0) dn.deg--;
      int r = resultant(&n, &dn); if (!r) continue; int an = dlog6[r];
      for (ll j = 0; j < nh; j++) { int s = resultant(&n, &H[j]); if (!s) continue; cop[j]++; cnt[j][(an - dlog6[s] + 12) % 6]++; }
    }
    for (int k = 0; k <= kmax; k++) {
      ll tot = 0, nz = 0, hh = 0; long double E = 0; ll DD = 0;
      for (ll j = 0; j < nh; j++) { if (hk[j] != k) continue; hh++;
        __int128 s = 0; for (int e = 0; e < 6; e++) for (int f = 0; f < 6; f++) s += (__int128)cnt[j][e] * cnt[j][f] * w[(e - f + 6) % 6];
        s /= 2; if (s) nz++; E += (long double)s; DD += cop[j]; (void)tot; }
      printf("%d %d %lld %lld %.0Lf %lld\n", d, k, hh, nz, E, DD);
    }
    ll a = 0, b = 0; for (int e = 0; e < 6; e++) { a += cnt[0][e] * W1[e]; b += cnt[0][e] * W2[e]; }
    printf("B1 %d %lld %lld\n", d, a, b); fflush(stdout);
  }
  return 0;
}
