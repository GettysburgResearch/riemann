/* carrier_stream.c -- complete prime-power lag accumulator for the D-0801
 * piecewise autocorrelation carrier family, with carrier phases evaluated to
 * double-double accuracy through an exact integer argument decomposition.
 *
 * Agent:  opus5-01
 * Issue:  #55 / #28
 * Claims: D-0801, L-0801 (object), L-5601 (error model)
 *
 * WHAT IT COMPUTES
 * ----------------
 * For a cutoff c = 10^k, K cells and a rational carrier T = Tn/Td, it computes
 * the complete lag coefficients of L-0801,
 *
 *      z_d = sum_{q = p^a <= c}  b_q * exp(-i T log q) * tau_d(r_q),
 *      b_q = Lambda(q) / (pi sqrt q),  r_q = K log q / log c,
 *      tau_d(r) = (1 - |r - d|)_+,     0 <= d < K,
 *
 * so that for any vector v with lag autocorrelations c_d the normalized
 * complete prime Rayleigh value of L-0801 is exactly
 *
 *      v^* S_K v = sum_{d=0}^{K-1} Re( z_d * c_d ).
 *
 * It also accumulates the positive weights W_d = sum_q b_q tau_d(r_q) and
 * Btot = sum_q b_q, which are the only inputs the L-5601 error model needs to
 * turn the floating output into a rigorous enclosure.
 *
 * WHY THE PHASE DECOMPOSITION IS NEEDED
 * -------------------------------------
 * T log q is of size ~1.2e14 at the target parameters.  Reducing it modulo
 * 2 pi in long double (64-bit significand) leaves an absolute phase error of
 * order 1e-5 radians, which is the same size as the quantity being measured.
 * Here q is an exact integer below 2^37, so we write
 *
 *      q = 2^e * y_j * (1 + z),   y_j = 1 + j/65536,   |z| <= 2^-17,
 *
 * where e, j and the exact rational z are obtained from integer operations
 * only.  Then
 *
 *      T log q  =  e*(T log 2) + (T log y_j) + T*log(1+z),
 *
 * the first two summands are read from tables reduced modulo 2 pi once and for
 * all at 300 bits with MPFR, and the third is under 4e7 in magnitude and is
 * evaluated by a double-double log1p series.  The resulting phase error is
 * below 1e-20 radians.
 *
 * BUILD
 *   gcc -O3 -march=native -mfma -std=c11 carrier_stream.c -o carrier_stream \
 *       -lmpfr -lgmp -lpthread -lm
 */

#define _GNU_SOURCE
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
#include <math.h>
#include <pthread.h>
#include <mpfr.h>

#include "dd.h"

/* ------------------------------------------------------------------ */
/* Parameters                                                          */
/* ------------------------------------------------------------------ */

#ifndef JBITS
#define JBITS      16
#endif
#define JSIZE      (1 << JBITS)          /* 65536 mantissa table steps    */
#ifndef TRIGBITS
#define TRIGBITS   12
#endif
#define TRIGSIZE   (1 << TRIGBITS)       /* 4096 phase table steps        */
#define MAXEXP     60
#define SEGWORDS   (1u << 18)            /* numbers per sieve segment     */
#define MPFR_PREC  300

static int      K_CELLS   = 1024;
static uint64_t CUTOFF    = 0;           /* c = 10^k, exact integer       */
static int      CUTPOW10  = 11;
static int      NTHREADS  = 4;

/* Tables built once with MPFR. */
static dd  TAB_B[JSIZE + 1];             /* (T log y_j) mod 2pi           */
static dd  TAB_LOGY[JSIZE + 1];          /* log y_j                       */
static dd  TAB_A[MAXEXP + 1];            /* (e T log 2) mod 2pi           */
static dd  TAB_SIN[TRIGSIZE];            /* sin(2 pi idx / TRIGSIZE)      */
static dd  TAB_COS[TRIGSIZE];
static dd  TAB_ANG[TRIGSIZE];            /* 2 pi idx / TRIGSIZE           */
static dd  LOGC_INV_K;                   /* K / log c                     */
static dd  LOG2_DD, TWO_PI, INV_TWO_PI, INV_PI, T_DD;
static dd  LOGSER[7];                    /* 1, -1/2, 1/3, ... , -1/6      */
static dd  TRIG_STEP;                    /* 2 pi / TRIGSIZE               */

/* ------------------------------------------------------------------ */
/* Accumulators                                                        */
/* ------------------------------------------------------------------ */

typedef struct {
    dd *re, *im, *w;
    dd  btot;
    uint64_t nprime, npower;
} acc_t;

static void acc_init(acc_t *a) {
    a->re = calloc((size_t)K_CELLS, sizeof(dd));
    a->im = calloc((size_t)K_CELLS, sizeof(dd));
    a->w  = calloc((size_t)K_CELLS, sizeof(dd));
    a->btot = dd_of(0.0);
    a->nprime = a->npower = 0;
}

static void acc_merge(acc_t *dst, const acc_t *src) {
    for (int d = 0; d < K_CELLS; d++) {
        dst->re[d] = dd_add(dst->re[d], src->re[d]);
        dst->im[d] = dd_add(dst->im[d], src->im[d]);
        dst->w[d]  = dd_add(dst->w[d],  src->w[d]);
    }
    dst->btot   = dd_add(dst->btot, src->btot);
    dst->nprime += src->nprime;
    dst->npower += src->npower;
}

/* ------------------------------------------------------------------ */
/* MPFR helpers                                                        */
/* ------------------------------------------------------------------ */

static dd dd_from_mpfr(mpfr_t x) {
    dd r;
    mpfr_t t;
    mpfr_init2(t, MPFR_PREC);
    r.hi = mpfr_get_d(x, MPFR_RNDN);
    mpfr_sub_d(t, x, r.hi, MPFR_RNDN);
    r.lo = mpfr_get_d(t, MPFR_RNDN);
    mpfr_clear(t);
    return r;
}

static void build_tables(uint64_t tnum, uint64_t tden) {
    mpfr_t T, twopi, tmp, y, lg, prod, q, half;
    mpfr_inits2(MPFR_PREC, T, twopi, tmp, y, lg, prod, q, half, (mpfr_ptr)0);

    mpfr_set_uj(T, (uintmax_t)tnum, MPFR_RNDN);
    mpfr_div_ui(T, T, (unsigned long)tden, MPFR_RNDN);
    T_DD = dd_from_mpfr(T);

    mpfr_const_pi(twopi, MPFR_RNDN);
    mpfr_mul_2ui(twopi, twopi, 1, MPFR_RNDN);
    TWO_PI = dd_from_mpfr(twopi);
    mpfr_ui_div(tmp, 1, twopi, MPFR_RNDN);
    INV_TWO_PI = dd_from_mpfr(tmp);
    mpfr_const_pi(tmp, MPFR_RNDN);
    mpfr_ui_div(tmp, 1, tmp, MPFR_RNDN);
    INV_PI = dd_from_mpfr(tmp);

    mpfr_set_ui(tmp, 2, MPFR_RNDN);
    mpfr_log(tmp, tmp, MPFR_RNDN);
    LOG2_DD = dd_from_mpfr(tmp);

    /* K / log(10^k) */
    mpfr_set_ui(tmp, 10, MPFR_RNDN);
    mpfr_log(tmp, tmp, MPFR_RNDN);
    mpfr_mul_ui(tmp, tmp, (unsigned long)CUTPOW10, MPFR_RNDN);   /* log c */
    mpfr_ui_div(tmp, (unsigned long)K_CELLS, tmp, MPFR_RNDN);
    LOGC_INV_K = dd_from_mpfr(tmp);

    /* (e T log 2) mod 2 pi */
    for (int e = 0; e <= MAXEXP; e++) {
        mpfr_set_ui(tmp, 2, MPFR_RNDN);
        mpfr_log(tmp, tmp, MPFR_RNDN);
        mpfr_mul_ui(tmp, tmp, (unsigned long)e, MPFR_RNDN);
        mpfr_mul(prod, T, tmp, MPFR_RNDN);
        mpfr_fmod(q, prod, twopi, MPFR_RNDN);
        if (mpfr_sgn(q) < 0) mpfr_add(q, q, twopi, MPFR_RNDN);
        TAB_A[e] = dd_from_mpfr(q);
    }

    /* log y_j and (T log y_j) mod 2 pi for y_j = 1 + j/65536 */
    for (int j = 0; j <= JSIZE; j++) {
        mpfr_set_ui(y, (unsigned long)(JSIZE + j), MPFR_RNDN);
        mpfr_div_ui(y, y, (unsigned long)JSIZE, MPFR_RNDN);   /* exact */
        mpfr_log(lg, y, MPFR_RNDN);
        TAB_LOGY[j] = dd_from_mpfr(lg);
        mpfr_mul(prod, T, lg, MPFR_RNDN);
        mpfr_fmod(q, prod, twopi, MPFR_RNDN);
        if (mpfr_sgn(q) < 0) mpfr_add(q, q, twopi, MPFR_RNDN);
        TAB_B[j] = dd_from_mpfr(q);
    }

    /* trigonometric anchor table */
    mpfr_div_ui(tmp, twopi, TRIGSIZE, MPFR_RNDN);
    TRIG_STEP = dd_from_mpfr(tmp);
    for (int i = 0; i < TRIGSIZE; i++) {
        mpfr_mul_ui(tmp, twopi, (unsigned long)i, MPFR_RNDN);
        mpfr_div_ui(tmp, tmp, TRIGSIZE, MPFR_RNDN);
        TAB_ANG[i] = dd_from_mpfr(tmp);
        mpfr_sin(lg, tmp, MPFR_RNDN); TAB_SIN[i] = dd_from_mpfr(lg);
        mpfr_cos(lg, tmp, MPFR_RNDN); TAB_COS[i] = dd_from_mpfr(lg);
    }

    /* log(1+z)/z series coefficients 1, -1/2, 1/3, -1/4, 1/5, -1/6, 1/7 */
    for (int i = 0; i < 7; i++) {
        mpfr_set_si(tmp, (i % 2 == 0) ? 1 : -1, MPFR_RNDN);
        mpfr_div_ui(tmp, tmp, (unsigned long)(i + 1), MPFR_RNDN);
        LOGSER[i] = dd_from_mpfr(tmp);
    }

    mpfr_clears(T, twopi, tmp, y, lg, prod, q, half, (mpfr_ptr)0);
}

/* ------------------------------------------------------------------ */
/* Core per-term kernel                                                */
/* ------------------------------------------------------------------ */

/* Exact decomposition q = 2^e * y_j * (1+z), returns log q and the phase. */
static inline void decompose(uint64_t q, dd *logq, dd *theta) {
    int e = 63 - __builtin_clzll(q);
    uint64_t base = (uint64_t)1 << e;
    uint64_t t = q << JBITS;                          /* exact, < 2^54 */
    uint64_t jj = (t + (base >> 1)) >> e;             /* round to table */
    int j = (int)(jj - (uint64_t)JSIZE);
    if (j < 0) j = 0;
    if (j > JSIZE) j = JSIZE;
    uint64_t den = ((uint64_t)JSIZE + (uint64_t)j) << e;
    int64_t num = (int64_t)t - (int64_t)den;

    dd z = dd_div_dd_exact((double)num, (double)den);

    /* log(1+z) by Horner on the alternating series */
    dd P = LOGSER[6];
    for (int i = 5; i >= 0; i--) P = dd_add(dd_mul(P, z), LOGSER[i]);
    dd l1 = dd_mul(z, P);

    *logq = dd_add(dd_add(dd_mul_d(LOG2_DD, (double)e), TAB_LOGY[j]), l1);

    /* phase */
    dd C = dd_mul(T_DD, l1);
    dd S = dd_add(dd_add(TAB_A[e], TAB_B[j]), C);
    double n = nearbyint(S.hi * INV_TWO_PI.hi);
    dd th = dd_sub(S, dd_mul_d(TWO_PI, n));
    if (th.hi < 0.0)             th = dd_add(th, TWO_PI);
    if (th.hi >= TWO_PI.hi)      th = dd_sub(th, TWO_PI);
    *theta = th;
}

/* sin and cos of a reduced angle in [0, 2pi) via the anchor table. */
static inline void sincos_dd(dd th, dd *s, dd *c) {
    int idx = (int)nearbyint(th.hi / TRIG_STEP.hi);
    /* The anchor nearest to an angle just below 2*pi is 2*pi itself, which is
     * not in the table; wrap the angle instead of the index, otherwise the
     * residual delta jumps from ~0 to ~2*pi and the series is meaningless. */
    if (idx >= TRIGSIZE) { th = dd_sub(th, TWO_PI); idx = 0; }
    if (idx < 0) idx = 0;
    dd delta = dd_sub(th, TAB_ANG[idx]);
    double x = delta.hi + delta.lo;
    double x2 = x * x;
    /* sin x, and cos x - 1, both tiny (|x| <= pi/4096) */
    double sd = x * (1.0 + x2 * (-1.0 / 6.0 + x2 * (1.0 / 120.0 - x2 / 5040.0)));
    double wd = x2 * (-0.5 + x2 * (1.0 / 24.0 - x2 / 720.0));
    dd S0 = TAB_SIN[idx], C0 = TAB_COS[idx];
    double corS = S0.hi * wd + C0.hi * sd;
    double corC = C0.hi * wd - S0.hi * sd;
    *s = dd_add_d(S0, corS);
    *c = dd_add_d(C0, corC);
}

/* Add one prime power q = p^a with Lambda(q) = log(q)/a. */
static inline void add_term(acc_t *A, uint64_t q, int a) {
    dd logq, th;
    decompose(q, &logq, &th);

    dd s, c;
    sincos_dd(th, &s, &c);

    /* amplitude b = Lambda(q) / (pi sqrt q) */
    double x0 = 1.0 / sqrt((double)q);
    dd p2 = two_prod(x0, x0);
    dd qq = two_prod((double)q, p2.hi);
    qq.lo += (double)q * p2.lo;
    qq = quick_two_sum(qq.hi, qq.lo);
    double rr = (1.0 - qq.hi) - qq.lo;
    dd rsq = quick_two_sum(x0, x0 * rr * 0.5);
    dd lam = (a == 1) ? logq : dd_div(logq, dd_of((double)a));
    dd b = dd_mul(dd_mul(lam, INV_PI), rsq);

    /* r = K log q / log c, split into lag and fraction */
    dd r = dd_mul(logq, LOGC_INV_K);
    double fl = floor(r.hi);
    dd f = dd_add_d(r, -fl);
    int d = (int)fl;
    if (f.hi < 0.0) { d -= 1; f = dd_add_d(f, 1.0); }
    if (f.hi >= 1.0) { d += 1; f = dd_add_d(f, -1.0); }
    if (d < 0 || d >= K_CELLS) return;      /* q >= c cannot occur */

    dd w1 = dd_mul(b, f);
    dd w0 = dd_sub(b, w1);

    A->re[d] = dd_add(A->re[d], dd_mul(w0, c));
    A->im[d] = dd_sub(A->im[d], dd_mul(w0, s));
    A->w[d]  = dd_add(A->w[d], w0);
    if (d + 1 < K_CELLS) {
        A->re[d + 1] = dd_add(A->re[d + 1], dd_mul(w1, c));
        A->im[d + 1] = dd_sub(A->im[d + 1], dd_mul(w1, s));
        A->w[d + 1]  = dd_add(A->w[d + 1], w1);
    }
    A->btot = dd_add(A->btot, b);
}

/* ------------------------------------------------------------------ */
/* Segmented sieve                                                     */
/* ------------------------------------------------------------------ */

static uint32_t *base_primes = NULL;
static uint32_t  base_count  = 0;

static void build_base_primes(uint64_t limit) {
    uint32_t n = (uint32_t)limit + 1;
    unsigned char *sv = calloc(n, 1);
    for (uint64_t i = 2; i * i <= limit; i++)
        if (!sv[i]) for (uint64_t j = i * i; j <= limit; j += i) sv[j] = 1;
    base_count = 0;
    for (uint32_t i = 2; i <= (uint32_t)limit; i++) if (!sv[i]) base_count++;
    base_primes = malloc(sizeof(uint32_t) * base_count);
    uint32_t k = 0;
    for (uint32_t i = 2; i <= (uint32_t)limit; i++) if (!sv[i]) base_primes[k++] = i;
    free(sv);
}

typedef struct { uint64_t lo, hi; acc_t acc; int tid; } job_t;

static void *worker(void *arg) {
    job_t *J = (job_t *)arg;
    acc_init(&J->acc);

    uint64_t lo = J->lo, hi = J->hi;
    if (lo < 3) lo = 3;
    if (lo % 2 == 0) lo++;
    if (hi <= lo) return NULL;

    unsigned char *sieve = malloc(SEGWORDS / 2 + 1);
    uint64_t *next = malloc(sizeof(uint64_t) * base_count);

    /* first odd multiple of p that is >= max(lo, p*p) */
    for (uint32_t i = 1; i < base_count; i++) {          /* skip p = 2 */
        uint64_t p = base_primes[i];
        uint64_t start = p * p;
        if (start < lo) {
            start = ((lo + p - 1) / p) * p;
            if ((start & 1ULL) == 0) start += p;
        }
        next[i] = start;
    }

    for (uint64_t seg = lo; seg < hi; seg += SEGWORDS) {
        uint64_t segend = seg + SEGWORDS;
        if (segend > hi) segend = hi;
        size_t cnt = (size_t)((segend - seg + 1) / 2);
        memset(sieve, 0, cnt);
        for (uint32_t i = 1; i < base_count; i++) {
            uint64_t p = base_primes[i];
            uint64_t m = next[i];
            if (m >= segend) continue;
            for (; m < segend; m += 2 * p) sieve[(m - seg) >> 1] = 1;
            next[i] = m;
        }
        for (size_t t = 0; t < cnt; t++) {
            if (!sieve[t]) {
                uint64_t q = seg + 2 * (uint64_t)t;
                add_term(&J->acc, q, 1);
                J->acc.nprime++;
            }
        }
    }
    free(sieve);
    free(next);
    return NULL;
}

/* ------------------------------------------------------------------ */
/* Output                                                              */
/* ------------------------------------------------------------------ */

static void print_dd(FILE *f, dd v) { fprintf(f, "[\"%a\",\"%a\"]", v.hi, v.lo); }

int main(int argc, char **argv) {
    uint64_t tnum = 94184072727073ULL, tden = 20ULL;
    const char *out = "stream.json";
    for (int i = 1; i < argc; i++) {
        if (!strcmp(argv[i], "--cutoff-power10")) CUTPOW10 = atoi(argv[++i]);
        else if (!strcmp(argv[i], "--cells"))     K_CELLS  = atoi(argv[++i]);
        else if (!strcmp(argv[i], "--carrier-num")) tnum   = strtoull(argv[++i], 0, 10);
        else if (!strcmp(argv[i], "--carrier-den")) tden   = strtoull(argv[++i], 0, 10);
        else if (!strcmp(argv[i], "--threads"))   NTHREADS = atoi(argv[++i]);
        else if (!strcmp(argv[i], "--out"))       out      = argv[++i];
        else { fprintf(stderr, "unknown option %s\n", argv[i]); return 2; }
    }
    CUTOFF = 1;
    for (int i = 0; i < CUTPOW10; i++) CUTOFF *= 10ULL;
    /* The exact decomposition needs q<<JBITS to fit in uint64 and needs
     * N = q*J - (J+j)*2^e and D = (J+j)*2^e to be exact binary64 integers.
     * |N| <= 2^{e-1} and D has at most JBITS+1 significant bits, so the binding
     * constraint is the shift: q < 2^{63-JBITS}.  A margin of two bits is kept. */
    if (CUTOFF >= (1ULL << (61 - JBITS))) {
        fprintf(stderr, "cutoff too large for the exact decomposition at JBITS=%d\n",
                JBITS);
        return 2;
    }

    build_tables(tnum, tden);

    uint64_t root = (uint64_t)sqrtl((long double)CUTOFF) + 2;
    while (root * root > CUTOFF) root--;
    build_base_primes(root);

    acc_t total; acc_init(&total);

    /* q = 2 is the only even prime */
    add_term(&total, 2, 1);
    total.nprime++;

    /* higher prime powers p^a <= c, a >= 2 (each counted once) */
    for (uint32_t i = 0; i < base_count; i++) {
        uint64_t p = base_primes[i];
        __uint128_t q = (__uint128_t)p * p;
        int a = 2;
        while (q <= (__uint128_t)CUTOFF) {
            add_term(&total, (uint64_t)q, a);
            total.npower++;
            q *= p; a++;
        }
    }

    pthread_t th[64];
    job_t jobs[64];
    if (NTHREADS > 64) NTHREADS = 64;
    /* split by cube-root-like weighting is unnecessary: marking cost is
       proportional to length, so equal length ranges balance well. */
    for (int t = 0; t < NTHREADS; t++) {
        jobs[t].lo = 3 + (uint64_t)((__uint128_t)(CUTOFF - 3) * t / NTHREADS);
        jobs[t].hi = 3 + (uint64_t)((__uint128_t)(CUTOFF - 3) * (t + 1) / NTHREADS);
        jobs[t].tid = t;
    }
    jobs[NTHREADS - 1].hi = CUTOFF + 1;      /* inclusive cutoff */
    for (int t = 0; t < NTHREADS; t++) pthread_create(&th[t], NULL, worker, &jobs[t]);
    for (int t = 0; t < NTHREADS; t++) {
        pthread_join(th[t], NULL);
        acc_merge(&total, &jobs[t].acc);
    }

    FILE *f = fopen(out, "w");
    if (!f) { perror("cannot open output file"); return 3; }
    fprintf(f, "{\n  \"schema\": \"riemann.x5601-carrier-stream.v1\",\n");
    fprintf(f, "  \"cutoff_power10\": %d,\n  \"cutoff\": %llu,\n  \"cells\": %d,\n",
            CUTPOW10, (unsigned long long)CUTOFF, K_CELLS);
    fprintf(f, "  \"carrier_numerator\": %llu,\n  \"carrier_denominator\": %llu,\n",
            (unsigned long long)tnum, (unsigned long long)tden);
    fprintf(f, "  \"prime_count\": %llu,\n  \"higher_prime_power_count\": %llu,\n",
            (unsigned long long)total.nprime, (unsigned long long)total.npower);
    fprintf(f, "  \"total_terms\": %llu,\n",
            (unsigned long long)(total.nprime + total.npower));
    fprintf(f, "  \"amplitude_total\": "); print_dd(f, total.btot); fprintf(f, ",\n");
    fprintf(f, "  \"jbits\": %d,\n  \"trigbits\": %d,\n", JBITS, TRIGBITS);
    fprintf(f, "  \"z_real\": [\n");
    for (int d = 0; d < K_CELLS; d++) {
        fprintf(f, "    "); print_dd(f, total.re[d]);
        fprintf(f, d + 1 < K_CELLS ? ",\n" : "\n");
    }
    fprintf(f, "  ],\n  \"z_imag\": [\n");
    for (int d = 0; d < K_CELLS; d++) {
        fprintf(f, "    "); print_dd(f, total.im[d]);
        fprintf(f, d + 1 < K_CELLS ? ",\n" : "\n");
    }
    fprintf(f, "  ],\n  \"weight\": [\n");
    for (int d = 0; d < K_CELLS; d++) {
        fprintf(f, "    "); print_dd(f, total.w[d]);
        fprintf(f, d + 1 < K_CELLS ? ",\n" : "\n");
    }
    fprintf(f, "  ]\n}\n");
    fclose(f);
    fprintf(stderr, "primes=%llu powers=%llu total=%llu\n",
            (unsigned long long)total.nprime, (unsigned long long)total.npower,
            (unsigned long long)(total.nprime + total.npower));
    return 0;
}
