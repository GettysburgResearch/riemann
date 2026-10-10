/*
 * b2_kernel.c -- inner loops for b2_*.py (EMPIRICAL numerics only; binary64, NOT directed or
 * certified).  Conventions = moments/eisenstein.py and a2/eis.py (OpenAI QRH manuscripts):
 * O = Z[omega], primary = 1 mod 3, chi_p(u) = (u/p)_6 = zeta^k, zeta = e^{i pi/3} = 1 + omega,
 * u^{(Np-1)/6} == zeta^k mod p; codes 0..5 = zeta^k, 32 = value 0 (as in sextic_kernel.c);
 * e(z/n) = exp(2 pi i d/N(n)) where z conj(n) = c + d omega.
 *
 * gauss2_split: gamma_2(pi) = p^{-1/2} sum_{x=1}^{p-1} chi_pi(x)^2 e(x/pi) for split primary
 *   pi = a + b omega, N pi = p prime; residues mod pi are the integers 0..p-1, omega == r =
 *   -a/b (mod p), e(x/pi) = exp(-2 pi i b x/p).  Discrete log mod 3 from a primitive root g;
 *   chi_pi(g) = zeta^t with t = 1 if g^{(p-1)/6} == 1 + r (mod p), else t = 5 (as in
 *   moments/eisenstein.py _split_table).  O(p) per prime.
 *
 * eval_B: B_m^{(k)} = sum_terms w_k(term) chi_c(m) chi_n(m)^3 for rows m = zeta^{um} m' (m'
 *   primary, (m,6) = 1) and terms (c, n) with c squarefree primary (large norm).  chi_c(m) is
 *   evaluated by sextic reciprocity: chi_c(m) = chi_c(zeta)^{um} R(m', c) chi_{m'}(c), with
 *   chi_{m'}(c) = prod_{pi^e || m'} chi_pi(c)^e read from the residue tables of the (small)
 *   row primes; R(m', c) = chi_c(m')/chi_{m'}(c) is the +-1 class table (code 0 or 3) built and
 *   validated in b2_common.py; chi_c(zeta) code = sum_{p | c} (Np - 1)/6.  chi_n(m)^3 codes are
 *   precomputed per (row, n).  K weight vectors are accumulated at once.
 * Build (scratchpad only): gcc -O3 -march=native -fopenmp -shared -fPIC -o b2_kernel.so b2_kernel.c -lm
 */
#include <stdint.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

#define ZERO 32
static const double ZRE[6] = {1.0, 0.5, -0.5, -1.0, -0.5, 0.5};
static const double ZIM[6] = {0.0, 0.86602540378443864676, 0.86602540378443864676,
                              0.0, -0.86602540378443864676, -0.86602540378443864676};

static inline int64_t pmod(int64_t x, int64_t m) { int64_t r = x % m; return r < 0 ? r + m : r; }
static int64_t pw(int64_t b, int64_t e, int64_t m) {
    int64_t r = 1 % m; b = pmod(b, m);
    while (e) { if (e & 1) r = (int64_t)((__int128)r * b % m); b = (int64_t)((__int128)b * b % m); e >>= 1; }
    return r;
}
static int64_t primroot(int64_t p) {
    int64_t f[64]; int k = 0; int64_t n = p - 1;
    for (int64_t d = 2; d * d <= n; d++) if (n % d == 0) { f[k++] = d; while (n % d == 0) n /= d; }
    if (n > 1) f[k++] = n;
    for (int64_t g = 2; g < p; g++) {
        int ok = 1;
        for (int i = 0; i < k; i++) if (pw(g, (p - 1) / f[i], p) == 1) { ok = 0; break; }
        if (ok) return g;
    }
    return -1;
}

void gauss2_split(int64_t np, const int64_t *P, const int64_t *B, const int64_t *R,
                  double *ore, double *oim) {
    int64_t pmax = 0;
    for (int64_t i = 0; i < np; i++) if (P[i] > pmax) pmax = P[i];
    #pragma omp parallel
    {
        uint8_t *cls = (uint8_t *)malloc((size_t)pmax + 1);
        const int BLK = 1024;
        double *sre = (double *)malloc(sizeof(double) * BLK), *sim = (double *)malloc(sizeof(double) * BLK);
        #pragma omp for schedule(dynamic, 4)
        for (int64_t i = 0; i < np; i++) {
            int64_t p = P[i], b = pmod(B[i], p), r = R[i];
            int64_t g = primroot(p);
            int64_t h = pw(g, (p - 1) / 6, p);
            int t = (h == pmod(1 + r, p)) ? 1 : 5;
            int64_t x = 1;
            for (int64_t k = 0; k < p - 1; k++) { cls[x] = (uint8_t)(k % 3); x = (int64_t)((__int128)x * g % p); }
            /* S_j = sum_{x in class j} exp(-2 pi i b x / p); x = BLK*q + j0 */
            double S[3][2] = {{0, 0}, {0, 0}, {0, 0}};
            double th = -2.0 * M_PI / (double)p;
            for (int j = 0; j < BLK; j++) { int64_t e = (int64_t)((__int128)b * j % p); sre[j] = cos(th * e); sim[j] = sin(th * e); }
            for (int64_t q0 = 0; q0 * BLK < p; q0++) {
                int64_t base = (int64_t)((__int128)b * (q0 * BLK) % p);
                double cr = cos(th * base), ci = sin(th * base);
                int64_t jlo = (q0 == 0) ? 1 : 0, jhi = p - q0 * BLK; if (jhi > BLK) jhi = BLK;
                for (int64_t j = jlo; j < jhi; j++) {
                    int c = cls[q0 * BLK + j];
                    S[c][0] += cr * sre[j] - ci * sim[j];
                    S[c][1] += cr * sim[j] + ci * sre[j];
                }
            }
            /* chi^2(g^k) = zeta^{2kt} = omega^{kt}; omega = zeta^2 */
            double re = 0, im = 0;
            for (int c = 0; c < 3; c++) {
                int code = (2 * c * t) % 6;
                re += S[c][0] * ZRE[code] - S[c][1] * ZIM[code];
                im += S[c][0] * ZIM[code] + S[c][1] * ZRE[code];
            }
            double s = 1.0 / sqrt((double)p);
            ore[i] = re * s; oim[i] = im * s;
        }
        free(cls); free(sre); free(sim);
    }
}

/* prime data of row primes (same layout as moments/common.py PrimeData) */
void eval_B(const int32_t *kind, const int64_t *mod, const int64_t *rr, const int64_t *off,
            const uint8_t *neg, const uint8_t *tables,
            int64_t nm, const int32_t *um, const int32_t *mcls, const int64_t *rowptr,
            const int32_t *rp_idx, const int32_t *rp_exp,
            int32_t nn, const uint8_t *ncode, const uint8_t *Rtab,
            int64_t nt, const int64_t *cx, const int64_t *cy, const uint8_t *ucode,
            const int32_t *ccls, const int32_t *nidx,
            int K, const double *wre, const double *wim,
            double *ore, double *oim) {
    uint8_t negmap[256];
    for (int v = 0; v < 256; v++) negmap[v] = ZERO;
    for (int v = 0; v < 6; v++) negmap[v] = (uint8_t)((6 - v) % 6);
    #pragma omp parallel
    {
        double *bins = (double *)malloc(sizeof(double) * 12 * K);
        #pragma omp for schedule(dynamic, 8)
        for (int64_t i = 0; i < nm; i++) {
            memset(bins, 0, sizeof(double) * 12 * K);
            int np = (int)(rowptr[i + 1] - rowptr[i]);
            int32_t pi_[16]; int32_t pe[16];
            for (int j = 0; j < np; j++) { pi_[j] = rp_idx[rowptr[i] + j]; pe[j] = rp_exp[rowptr[i] + j]; }
            const uint8_t *nc = ncode + (size_t)i * nn;
            const uint8_t *Rrow = Rtab + 16 * mcls[i];
            int u = um[i];
            for (int64_t t = 0; t < nt; t++) {
                uint8_t c3 = nc[nidx[t]];
                if (c3 >= ZERO) continue;
                int code = c3 + u * ucode[t] + Rrow[ccls[t]];
                int zero = 0;
                for (int j = 0; j < np; j++) {
                    int q = pi_[j];
                    const uint8_t *tab = tables + off[q];
                    int64_t m = mod[q];
                    uint8_t v;
                    if (kind[q] == 0) {
                        v = tab[pmod(cx[t] + pmod(cy[t], m) * rr[q], m)];
                        if (neg[q]) v = negmap[v];
                    } else {
                        v = tab[pmod(cx[t], m) * m + pmod(cy[t], m)];
                    }
                    if (v >= ZERO) { zero = 1; break; }
                    code += pe[j] * v;
                }
                if (zero) continue;
                code %= 6;
                const double *wr = wre + (size_t)t * K, *wi = wim + (size_t)t * K;
                for (int k = 0; k < K; k++) { bins[12 * k + 2 * code] += wr[k]; bins[12 * k + 2 * code + 1] += wi[k]; }
            }
            for (int k = 0; k < K; k++) {
                double re = 0, im = 0;
                for (int v = 0; v < 6; v++) {
                    double br = bins[12 * k + 2 * v], bi = bins[12 * k + 2 * v + 1];
                    re += br * ZRE[v] - bi * ZIM[v];
                    im += br * ZIM[v] + bi * ZRE[v];
                }
                ore[(size_t)i * K + k] = re; oim[(size_t)i * K + k] = im;
            }
        }
        free(bins);
    }
}
