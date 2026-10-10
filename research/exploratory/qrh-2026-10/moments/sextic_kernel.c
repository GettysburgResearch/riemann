/*
 * sextic_kernel.c -- inner loops for moments.py / balanced.py (EMPIRICAL numerics only).
 *
 * Evaluates Dirichlet-polynomial rows
 *     F(u) = sum_{nodes j} w[j] * chi_{n_j}(u),   chi_n = prod_{p | n} (u/p)_6,
 * for u = a + b*omega on horizontal lattice segments, where the squarefree
 * ideals n_j are given as a prefix tree: node j = node parent[j] times prime
 * pidx[j] (node 0 is the root n = 1, which has weight w[0]).
 *
 * Sextic symbols are read from the discrete-log-mod-6 tables built by
 * eisenstein.py (validated there against exact u^{(Np-1)/6} mod p):
 *   split prime  (kind 0): code = tab[(a + b*r) mod p], negated for conj(pi);
 *   inert prime  (kind 1): code = tab[(a mod q)*q + (b mod q)].
 * Codes 0..5 mean zeta^k (zeta = e^{i pi/3}); 32 means the value 0.
 * Code sums along a tree path are < 256 for <= 7 prime factors; a sum >= 32
 * means chi_n(u) = 0.
 *
 * Also: a random-model sampler (sample_model) that replaces chi_p(u) by
 * independent X_p, X_p = 0 with probability 1/Np and uniform on mu_6
 * otherwise.  Its 2k-th moments (k <= 5) are exactly the "diagonal"
 * sum_r c_k(r)^2 prod_{p|r}(1 - 1/Np).
 *
 * Build: gcc -O3 -march=native -shared -fPIC -o sextic_kernel.so sextic_kernel.c -lm
 */
#include <stdint.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

#define ZERO 32
#define SEG 128

static const double ZRE[6] = {1.0, 0.5, -0.5, -1.0, -0.5, 0.5};
static const double ZIM[6] = {0.0, 0.86602540378443864676, 0.86602540378443864676,
                              0.0, -0.86602540378443864676, -0.86602540378443864676};

static inline int64_t pmod(int64_t x, int64_t m) {
    int64_t r = x % m;
    return r < 0 ? r + m : r;
}

/* one u: traverse the tree with the given code row c[0..np) */
static inline void eval_tree(int nn, const int32_t *parent, const int32_t *pidx,
                             const double *w, const uint8_t *c, uint8_t *s,
                             double *bins, double *are, double *aim) {
    memset(bins, 0, 256 * sizeof(double));
    s[0] = 0;
    bins[0] += w[0];
    for (int j = 1; j < nn; j++) {
        uint8_t v = (uint8_t)(s[parent[j]] + c[pidx[j]]);
        s[j] = v;
        bins[v] += w[j];
    }
    double re = 0.0, im = 0.0;
    for (int v = 0; v < ZERO; v++) {
        re += bins[v] * ZRE[v % 6];
        im += bins[v] * ZIM[v % 6];
    }
    *are = re;
    *aim = im;
}

/*
 * Segments: for t in [0, nseg): u = a + b*omega, b = sb[t], a = sa0[t] .. sa0[t]+slen[t]-1.
 * Output written consecutively (segment after segment) into are/aim.
 */
void eval_segments(int np, const int32_t *kind, const int64_t *mod, const int64_t *rr,
                   const int64_t *off, const uint8_t *neg, const uint8_t *tables,
                   int nn, const int32_t *parent, const int32_t *pidx, const double *w,
                   int64_t nseg, const int64_t *sb, const int64_t *sa0, const int64_t *slen,
                   double *are, double *aim) {
    uint8_t negmap[256];
    for (int v = 0; v < 256; v++) negmap[v] = ZERO;
    for (int v = 0; v < 6; v++) negmap[v] = (uint8_t)((6 - v) % 6);
    uint8_t *codes = (uint8_t *)malloc((size_t)SEG * (size_t)np);
    uint8_t *s = (uint8_t *)malloc((size_t)nn);
    double bins[256];
    int64_t outpos = 0;
    for (int64_t t = 0; t < nseg; t++) {
        int64_t b = sb[t];
        for (int64_t a0 = sa0[t]; a0 < sa0[t] + slen[t]; a0 += SEG) {
            int64_t L = sa0[t] + slen[t] - a0;
            if (L > SEG) L = SEG;
            for (int i = 0; i < np; i++) {
                const uint8_t *tab = tables + off[i];
                int64_t m = mod[i];
                if (kind[i] == 0) {
                    int64_t idx = pmod(a0 + pmod(b, m) * rr[i], m);
                    if (neg[i]) {
                        for (int64_t j = 0; j < L; j++) {
                            codes[j * np + i] = negmap[tab[idx]];
                            if (++idx == m) idx = 0;
                        }
                    } else {
                        for (int64_t j = 0; j < L; j++) {
                            codes[j * np + i] = tab[idx];
                            if (++idx == m) idx = 0;
                        }
                    }
                } else {
                    int64_t xa = pmod(a0, m), yb = pmod(b, m);
                    for (int64_t j = 0; j < L; j++) {
                        codes[j * np + i] = tab[xa * m + yb];
                        if (++xa == m) xa = 0;
                    }
                }
            }
            for (int64_t j = 0; j < L; j++) {
                eval_tree(nn, parent, pidx, w, codes + j * np, s, bins,
                          are + outpos, aim + outpos);
                outpos++;
            }
        }
    }
    free(codes);
    free(s);
}

/* ---------------- random model ---------------- */
static inline uint64_t splitmix64(uint64_t *x) {
    uint64_t z = (*x += 0x9E3779B97F4A7C15ULL);
    z = (z ^ (z >> 30)) * 0xBF58476D1CE4E5B9ULL;
    z = (z ^ (z >> 27)) * 0x94D049BB133111EBULL;
    return z ^ (z >> 31);
}

/* nsamp samples of |F|^2 with X_p random; pzero[i] = 1/N(p_i). */
void sample_model(int np, const double *pzero, int nn, const int32_t *parent,
                  const int32_t *pidx, const double *w, int64_t nsamp, uint64_t seed,
                  double *abs2) {
    uint8_t *c = (uint8_t *)malloc((size_t)np);
    uint8_t *s = (uint8_t *)malloc((size_t)nn);
    double bins[256];
    uint64_t st = seed;
    uint64_t *thr = (uint64_t *)malloc(sizeof(uint64_t) * (size_t)np);
    for (int i = 0; i < np; i++) thr[i] = (uint64_t)(pzero[i] * 18446744073709551615.0);
    for (int64_t t = 0; t < nsamp; t++) {
        for (int i = 0; i < np; i++) {
            uint64_t z = splitmix64(&st);
            if (z < thr[i]) {
                c[i] = ZERO;
            } else {
                uint64_t y = splitmix64(&st);
                c[i] = (uint8_t)(y % 6);
            }
        }
        double re, im;
        eval_tree(nn, parent, pidx, w, c, s, bins, &re, &im);
        abs2[t] = re * re + im * im;
    }
    free(c);
    free(s);
    free(thr);
}
