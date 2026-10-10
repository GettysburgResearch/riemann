/*
 * s6_gauss.c -- normalized sextic Gauss sums at primes of Z[omega] (EMPIRICAL numerics only;
 * double precision, NOT directed or certified).  Used by s6_theta_bias.py (SEXTIC_THETA_S6.md).
 *
 * Conventions = a2/eis.py (the Oct 5 manuscript):  pi primary (= 1 mod 3), chi_pi(x) = (x/pi)_6
 * = zeta^k with zeta = e^{i pi/3} = 1 + omega and x^{(N pi - 1)/6} == (1+omega)^k mod pi;
 * e(z/n) = exp(2 pi i d / N n) where z * conj(n) = c + d*omega.
 * Output, for each prime: G_j(pi) = N(pi)^{-1/2} sum_{x mod pi} chi_pi(x)^j e(x/pi), j = 1..5.
 *
 * Input (stdin): lines "kind p a b", kind 0 = split (N pi = p prime, pi = a + b omega primary),
 *                kind 1 = inert (pi = -q, a = -q, b = 0, p = q).
 * Output (stdout): "a b N re1 im1 re2 im2 ... re5 im5" with %.17g.
 *
 * Split prime: O/pi = Z/p, omega == r = -a b^{-1} (mod p); e(x/pi) = exp(-2 pi i b x / p).
 * Inert prime pi = -q: O/q = F_{q^2}, residues u + v omega; e(z/pi) = exp(-2 pi i v / q).
 * Method: discrete-log (mod 6) table from a primitive root, then 6 bins of additive characters.
 * Build: gcc -O2 -o s6_gauss s6_gauss.c -lm
 */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <math.h>
#include <complex.h>

static int64_t pw(int64_t b, int64_t e, int64_t m) {
    int64_t r = 1 % m; b %= m; if (b < 0) b += m;
    while (e) { if (e & 1) r = (__int128)r * b % m; b = (__int128)b * b % m; e >>= 1; }
    return r;
}
static int factor(int64_t n, int64_t *f) {          /* distinct prime factors */
    int k = 0;
    for (int64_t d = 2; d * d <= n; d++) if (n % d == 0) { f[k++] = d; while (n % d == 0) n /= d; }
    if (n > 1) f[k++] = n;
    return k;
}
/* --- Z[omega]/q arithmetic, element (u,v) = u + v omega, omega^2 = -1 - omega --- */
static void zmul(int64_t a, int64_t b, int64_t c, int64_t d, int64_t q, int64_t *x, int64_t *y) {
    int64_t X = (a * c - b * d) % q, Y = (a * d + b * c - b * d) % q;
    if (X < 0) X += q; if (Y < 0) Y += q; *x = X; *y = Y;
}
static void zpow(int64_t a, int64_t b, int64_t e, int64_t q, int64_t *x, int64_t *y) {
    int64_t ru = 1, rv = 0, bu = ((a % q) + q) % q, bv = ((b % q) + q) % q;
    while (e) { if (e & 1) zmul(ru, rv, bu, bv, q, &ru, &rv); zmul(bu, bv, bu, bv, q, &bu, &bv); e >>= 1; }
    *x = ru; *y = rv;
}

int main(void) {
    int kind; int64_t p, a, b;
    const double TP = 2.0 * M_PI;
    double complex zeta[6];
    for (int k = 0; k < 6; k++) zeta[k] = cexp(I * M_PI * k / 3.0);
    while (scanf("%d %ld %ld %ld", &kind, &p, &a, &b) == 4) {
        double complex bins[6] = {0};
        int k0 = -1; double Nn;
        if (kind == 0) {
            int64_t f[64]; int nf = factor(p - 1, f), g;
            for (g = 2;; g++) { int ok = 1; for (int i = 0; i < nf; i++) if (pw(g, (p - 1) / f[i], p) == 1) { ok = 0; break; } if (ok) break; }
            int64_t binv = pw(((b % p) + p) % p, p - 2, p);
            int64_t r = ((-a % p) + p) % p * binv % p;                 /* omega mod pi */
            int64_t t = pw(g, (p - 1) / 6, p), z = (1 + r) % p, zk = 1;
            for (int k = 0; k < 6; k++) { if (zk == t) { k0 = k; break; } zk = zk * z % p; }
            unsigned char *ind = malloc(p);
            int64_t x = 1;
            for (int64_t j = 0; j < p - 1; j++) { ind[x] = (unsigned char)(j % 6); x = x * g % p; }
            int64_t bm = ((b % p) + p) % p;
            double complex w = cexp(-I * TP * (double)bm / (double)p), zz = 1.0;
            for (int64_t xx = 1; xx < p; xx++) {
                if ((xx & 255) == 0) zz = cexp(-I * TP * (double)((__int128)bm * xx % p) / (double)p);
                else zz *= w;
                bins[ind[xx]] += zz;
            }
            free(ind); Nn = (double)p;
        } else {
            int64_t q = p, n2 = q * q - 1, f[64]; int nf = factor(n2, f);
            int64_t gu = 0, gv = 0, found = 0;
            for (gu = 0; gu < q && !found; gu++) for (gv = 1; gv < q; gv++) {
                int ok = 1; int64_t x, y;
                for (int i = 0; i < nf; i++) { zpow(gu, gv, n2 / f[i], q, &x, &y); if (x == 1 && y == 0) { ok = 0; break; } }
                if (ok) { found = 1; break; }
            }
            gu--;                                                       /* undo loop increment */
            int64_t tx, ty; zpow(gu, gv, n2 / 6, q, &tx, &ty);
            int64_t zu = 1, zv = 0;                                     /* powers of zeta = 1 + omega */
            for (int k = 0; k < 6; k++) { if (zu == tx && zv == ty) { k0 = k; break; } zmul(zu, zv, 1, 1, q, &zu, &zv); }
            unsigned char *ind = malloc(q * q);
            int64_t xu = 1, xv = 0;
            for (int64_t j = 0; j < n2; j++) { ind[xu * q + xv] = (unsigned char)(j % 6); zmul(xu, xv, gu, gv, q, &xu, &xv); }
            double complex ev[4096]; if (q >= 4096) { fprintf(stderr, "q too large\n"); return 1; }
            for (int64_t v = 0; v < q; v++) ev[v] = cexp(-I * TP * (double)v / (double)q);
            for (int64_t u = 0; u < q; u++) for (int64_t v = 0; v < q; v++) if (u || v) bins[ind[u * q + v]] += ev[v];
            free(ind); Nn = (double)(q * q);
        }
        if (k0 < 0) { fprintf(stderr, "k0 failure at %ld\n", p); return 1; }
        printf("%ld %ld %.0f", a, b, Nn);
        for (int j = 1; j <= 5; j++) {
            double complex G = 0;
            for (int k = 0; k < 6; k++) G += zeta[(j * k0 * k) % 6] * bins[k];
            G /= sqrt(Nn);
            printf(" %.17g %.17g", creal(G), cimag(G));
        }
        printf("\n");
    }
    return 0;
}
