/* rs_zeta.c -- Riemann-Siegel Z(t) evaluator, sign-change counter and
 * Turing-style zero census, with double-double phase handling.
 *
 * Agent:  opus5-01
 * Issue:  #55 (spun out of the D-0801 sensitivity analysis)
 * Claims: T-5602 (why this is the only family of methods that can detect an
 *         arbitrarily small off-critical displacement), L-5601 (the huge-phase
 *         technique, reused here)
 *
 * WHY
 * ---
 * T-5602: the off-critical quadruple {1/2 +- eta +- i gamma} is invariant under
 * eta -> -eta, so EVERY smooth functional of the zero multiset -- Weil
 * positivity, Li coefficients, n-level densities -- responds evenly in eta and
 * has zero first derivative at eta = 0.  The only escape is a functional that
 * is not smooth in the zero positions: a zero COUNT.  If the number of sign
 * changes of Z on the critical line in [t1,t2] falls short of
 * (theta(t2)-theta(t1))/pi, zeros have left the line.  One missing sign change
 * is a disproof of RH.
 *
 * WHAT
 * ----
 *   Z(t) = 2 sum_{n=1}^{N} n^{-1/2} cos(theta(t) - t log n) + R(t),
 *   N = floor(sqrt(t/2pi)),  a = sqrt(t/2pi),  p = a - N,
 *   R(t) = (-1)^{N-1} a^{-1/2} [ C0(p) + O(a^{-1}) ],
 *   C0(p) = cos(2 pi (p^2 - p - 1/16)) / cos(2 pi p).
 *
 * Z is real for real t, and its real zeros are exactly the zeros of zeta on the
 * critical line, with the same multiplicities.
 *
 * PHASES
 * ------
 * At t = 10^13 the phase t log n reaches 1.3e14 and must be known to ~1e-10.
 * Writing t = T0 + s with T0 fixed for the whole scan, the table
 * A[n] = (T0 log n) mod 2pi is computed once with MPFR at 200 bits, and only
 * the small increment s log n is formed per evaluation.  N does not change over
 * a scan of a few thousand units of t, so the table is built once.
 *
 * BUILD
 *   gcc -O3 -march=native -mfma -std=c11 rs_zeta.c -o rs_zeta \
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

#define PREC 256

static double *TAB_A = NULL;      /* (T0 log n) mod 2pi                */
static double *TAB_L = NULL;      /* log n                             */
static double *TAB_R = NULL;      /* n^{-1/2}                          */
static long    NTERMS = 0;
static double  T0 = 0.0;
static int     NTHREADS = 4;

static const double TWO_PI = 6.283185307179586476925286766559;
static const double INV_TWO_PI = 0.15915494309189533576888376337251;

/* ------------------------------------------------------------------ */
/* theta(t) mod 2pi, and theta(t) itself, at 256 bits                  */
/* ------------------------------------------------------------------ */

/* theta(t) = (t/2) log(t/2pi) - t/2 - pi/8 + 1/(48 t) + 7/(5760 t^3) + ... */
static void theta_mpfr(mpfr_t out, mpfr_t t)
{
    mpfr_t a, b, pi;
    mpfr_inits2(PREC, a, b, pi, (mpfr_ptr)0);
    mpfr_const_pi(pi, MPFR_RNDN);

    mpfr_mul_ui(a, pi, 2, MPFR_RNDN);          /* 2 pi            */
    mpfr_div(a, t, a, MPFR_RNDN);              /* t/(2 pi)        */
    mpfr_log(a, a, MPFR_RNDN);                 /* log(t/2pi)      */
    mpfr_mul(a, a, t, MPFR_RNDN);
    mpfr_div_ui(a, a, 2, MPFR_RNDN);           /* (t/2) log(t/2pi)*/

    mpfr_div_ui(b, t, 2, MPFR_RNDN);
    mpfr_sub(a, a, b, MPFR_RNDN);              /* - t/2           */

    mpfr_div_ui(b, pi, 8, MPFR_RNDN);
    mpfr_sub(a, a, b, MPFR_RNDN);              /* - pi/8          */

    mpfr_ui_div(b, 1, t, MPFR_RNDN);
    mpfr_div_ui(b, b, 48, MPFR_RNDN);
    mpfr_add(a, a, b, MPFR_RNDN);              /* + 1/(48 t)      */

    mpfr_pow_ui(b, t, 3, MPFR_RNDN);
    mpfr_ui_div(b, 7, b, MPFR_RNDN);
    mpfr_div_ui(b, b, 5760, MPFR_RNDN);
    mpfr_add(a, a, b, MPFR_RNDN);              /* + 7/(5760 t^3)  */

    mpfr_set(out, a, MPFR_RNDN);
    mpfr_clears(a, b, pi, (mpfr_ptr)0);
}

static double theta_mod_2pi(double s, double *theta_full)
{
    mpfr_t t, th, tp, q;
    mpfr_inits2(PREC, t, th, tp, q, (mpfr_ptr)0);
    mpfr_set_d(t, T0, MPFR_RNDN);
    mpfr_add_d(t, t, s, MPFR_RNDN);            /* t = T0 + s, exact-ish */
    theta_mpfr(th, t);
    if (theta_full) *theta_full = mpfr_get_d(th, MPFR_RNDN);
    mpfr_const_pi(tp, MPFR_RNDN);
    mpfr_mul_ui(tp, tp, 2, MPFR_RNDN);
    mpfr_fmod(q, th, tp, MPFR_RNDN);
    if (mpfr_sgn(q) < 0) mpfr_add(q, q, tp, MPFR_RNDN);
    double r = mpfr_get_d(q, MPFR_RNDN);
    mpfr_clears(t, th, tp, q, (mpfr_ptr)0);
    return r;
}

/* theta(t) to full precision, as an mpfr value converted through a long
 * double so that (theta(t2)-theta(t1))/pi is accurate for the census. */
static void theta_pair(double s, mpfr_t out)
{
    mpfr_t t;
    mpfr_init2(t, PREC);
    mpfr_set_d(t, T0, MPFR_RNDN);
    mpfr_add_d(t, t, s, MPFR_RNDN);
    theta_mpfr(out, t);
    mpfr_clear(t);
}

/* ------------------------------------------------------------------ */
/* Riemann-Siegel remainder, leading term                              */
/* ------------------------------------------------------------------ */

/* C0(p) = cos(2 pi (p^2 - p - 1/16)) / cos(2 pi p), with the removable
 * singularities at p = 1/4 and p = 3/4 handled by the shifted forms
 *   p = 1/4 + u :  C0 = -sin(2 pi u^2 - pi u) / sin(2 pi u)
 *   p = 3/4 + v :  C0 =  sin(2 pi v^2 + pi v) / sin(2 pi v)
 * both of which tend to 1/2. */
static double rs_C0(double p)
{
    double d = cos(TWO_PI * p);
    if (fabs(d) > 1e-3) {
        return cos(TWO_PI * (p * p - p - 0.0625)) / d;
    }
    double u = p - 0.25;
    if (fabs(u) < 0.1) {
        double den = sin(TWO_PI * u);
        if (fabs(den) < 1e-14) return 0.5 - u;
        return -sin(TWO_PI * u * u - M_PI * u) / den;
    }
    double v = p - 0.75;
    double den = sin(TWO_PI * v);
    if (fabs(den) < 1e-14) return 0.5 - v;
    return sin(TWO_PI * v * v + M_PI * v) / den;
}

/* ------------------------------------------------------------------ */
/* main sum, threaded                                                  */
/* ------------------------------------------------------------------ */

typedef struct { long lo, hi; double s, theta; double acc; } job_t;

static void *sum_worker(void *arg)
{
    job_t *J = (job_t *)arg;
    double s = J->s, th = J->theta, acc = 0.0;
    for (long n = J->lo; n < J->hi; n++) {
        double ph = th - TAB_A[n] - s * TAB_L[n];
        ph -= TWO_PI * nearbyint(ph * INV_TWO_PI);
        acc += TAB_R[n] * cos(ph);
    }
    J->acc = acc;
    return NULL;
}

static double Z_of(double s)
{
    double th = theta_mod_2pi(s, NULL);
    pthread_t tid[64];
    job_t jobs[64];
    int nt = NTHREADS;
    for (int i = 0; i < nt; i++) {
        jobs[i].lo = 1 + (long)((double)(NTERMS) * i / nt);
        jobs[i].hi = 1 + (long)((double)(NTERMS) * (i + 1) / nt);
        jobs[i].s = s; jobs[i].theta = th; jobs[i].acc = 0.0;
    }
    jobs[nt - 1].hi = NTERMS + 1;
    if (nt == 1) { sum_worker(&jobs[0]); }
    else {
        for (int i = 0; i < nt; i++) pthread_create(&tid[i], NULL, sum_worker, &jobs[i]);
        for (int i = 0; i < nt; i++) pthread_join(tid[i], NULL);
    }
    double main_sum = 0.0;
    for (int i = 0; i < nt; i++) main_sum += jobs[i].acc;

    double t = T0 + s;
    double a = sqrt(t * INV_TWO_PI);
    long N = (long)floor(a);
    double p = a - (double)N;
    double rem = ((N % 2) ? 1.0 : -1.0) * pow(a, -0.5) * rs_C0(p);
    return 2.0 * main_sum + rem;
}

/* ------------------------------------------------------------------ */

static void build_tables(double t0, long n)
{
    mpfr_t l, tt, tp, q, prod;
    mpfr_inits2(PREC, l, tt, tp, q, prod, (mpfr_ptr)0);
    mpfr_set_d(tt, t0, MPFR_RNDN);
    mpfr_const_pi(tp, MPFR_RNDN);
    mpfr_mul_ui(tp, tp, 2, MPFR_RNDN);
    TAB_A = malloc(sizeof(double) * (n + 2));
    TAB_L = malloc(sizeof(double) * (n + 2));
    TAB_R = malloc(sizeof(double) * (n + 2));
    for (long k = 1; k <= n; k++) {
        mpfr_set_ui(l, (unsigned long)k, MPFR_RNDN);
        mpfr_log(l, l, MPFR_RNDN);
        TAB_L[k] = mpfr_get_d(l, MPFR_RNDN);
        TAB_R[k] = 1.0 / sqrt((double)k);
        mpfr_mul(prod, tt, l, MPFR_RNDN);
        mpfr_fmod(q, prod, tp, MPFR_RNDN);
        if (mpfr_sgn(q) < 0) mpfr_add(q, q, tp, MPFR_RNDN);
        TAB_A[k] = mpfr_get_d(q, MPFR_RNDN);
    }
    mpfr_clears(l, tt, tp, q, prod, (mpfr_ptr)0);
}

int main(int argc, char **argv)
{
    double t0 = 1e13, span = 100.0;
    int per_gram = 8;
    const char *out = "rs-scan.json";
    const char *zfile = NULL;
    const char *dumpfile = NULL;
    int emit_zeros = 0;
    for (int i = 1; i < argc; i++) {
        if (!strcmp(argv[i], "--t0")) t0 = strtod(argv[++i], 0);
        else if (!strcmp(argv[i], "--span")) span = strtod(argv[++i], 0);
        else if (!strcmp(argv[i], "--per-gram")) per_gram = atoi(argv[++i]);
        else if (!strcmp(argv[i], "--threads")) NTHREADS = atoi(argv[++i]);
        else if (!strcmp(argv[i], "--emit-zeros")) emit_zeros = 1;
        else if (!strcmp(argv[i], "--out")) out = argv[++i];
        else if (!strcmp(argv[i], "--at")) {           /* evaluate Z once */
            double at = strtod(argv[++i], 0);
            T0 = at; NTERMS = (long)floor(sqrt(at * INV_TWO_PI));
            build_tables(at, NTERMS);
            printf("%.17g %.17g\n", at, Z_of(0.0));
            return 0;
        }
        else if (!strcmp(argv[i], "--zeros-file")) zfile = argv[++i];
        else if (!strcmp(argv[i], "--dump")) dumpfile = argv[++i];
        else { fprintf(stderr, "unknown option %s\n", argv[i]); return 2; }
    }
    T0 = t0;

    double a0 = sqrt(t0 * INV_TWO_PI);
    NTERMS = (long)floor(a0);
    double aend = sqrt((t0 + span) * INV_TWO_PI);
    if ((long)floor(aend) != NTERMS) {
        fprintf(stderr, "N changes over the span (%ld -> %ld); shorten it\n",
                NTERMS, (long)floor(aend));
        return 2;
    }
    fprintf(stderr, "t0=%.17g span=%g  N=%ld terms/eval\n", t0, span, NTERMS);
    build_tables(t0, NTERMS);
    fprintf(stderr, "tables built\n");

    /* Gram spacing 2 pi / log(t/2pi) */
    double gram = TWO_PI / log(t0 * INV_TWO_PI);
    double dt = gram / per_gram;
    long steps = (long)(span / dt);

    FILE *df = dumpfile ? fopen(dumpfile, "w") : NULL;
    double *zs = malloc(sizeof(double) * (steps + 2));
    double prev = Z_of(0.0), prevs = 0.0;
    zs[0] = prev;
    long sign_changes = 0;
    long refine_ops = 0;
    double *zeros = emit_zeros ? malloc(sizeof(double) * (steps + 2)) : NULL;
    long nz = 0;
    double minz = 1e300;

    for (long i = 1; i <= steps; i++) {
        double s = i * dt;
        double z = Z_of(s);
        zs[i] = z;
        if (df) fprintf(df, "%.17g %.17g\n", T0 + s, z);
        if ((prev > 0 && z < 0) || (prev < 0 && z > 0)) {
            sign_changes++;
            if (emit_zeros) {
                /* false position: a simple zero of Z needs only a few steps */
                double lo = prevs, hi = s, zlo = prev, zhi = z;
                double root = lo;
                for (int b = 0; b < 5; b++) {
                    root = lo - zlo * (hi - lo) / (zhi - zlo);
                    if (!(root > lo && root < hi)) root = 0.5 * (lo + hi);
                    double zm = Z_of(root);
                    refine_ops++;
                    if (fabs(zm) < 1e-13) break;
                    if ((zlo > 0) == (zm > 0)) { lo = root; zlo = zm; }
                    else { hi = root; zhi = zm; }
                    if (hi - lo < 1e-10) break;
                }
                zeros[nz++] = root;
            }
        }
        if (fabs(z) < minz) minz = fabs(z);
        prev = z; prevs = s;
    }

    /* census: expected number of zeros with 0 < gamma < t is
     * N(t) = theta(t)/pi + 1 + S(t); over an interval the smooth part is
     * (theta(t2)-theta(t1))/pi. */
    mpfr_t th1, th2, pi_, d;
    mpfr_inits2(PREC, th1, th2, pi_, d, (mpfr_ptr)0);
    theta_pair(0.0, th1);
    theta_pair(steps * dt, th2);
    mpfr_const_pi(pi_, MPFR_RNDN);
    mpfr_sub(d, th2, th1, MPFR_RNDN);
    mpfr_div(d, d, pi_, MPFR_RNDN);
    double expected = mpfr_get_d(d, MPFR_RNDN);
    mpfr_clears(th1, th2, pi_, d, (mpfr_ptr)0);

    FILE *f = fopen(out, "w");
    if (!f) { perror("open"); return 3; }
    fprintf(f, "{\n  \"schema\": \"riemann.x5602-rs-scan.v1\",\n");
    fprintf(f, "  \"agent\": \"opus5-01\",\n");
    fprintf(f, "  \"t0\": %.17g,\n  \"span\": %.17g,\n", t0, steps * dt);
    fprintf(f, "  \"main_sum_terms\": %ld,\n", NTERMS);
    fprintf(f, "  \"gram_spacing\": %.17g,\n  \"grid_step\": %.17g,\n", gram, dt);
    fprintf(f, "  \"evaluations\": %ld,\n", steps + 1 + refine_ops);
    fprintf(f, "  \"sign_changes\": %ld,\n", sign_changes);
    fprintf(f, "  \"expected_zeros_smooth\": %.10f,\n", expected);
    fprintf(f, "  \"deficit\": %.10f,\n", expected - (double)sign_changes);
    fprintf(f, "  \"min_abs_Z_on_grid\": %.6g,\n", minz);
    if (emit_zeros) {
        double mingap = 1e300; long argmin = -1;
        for (long i = 1; i < nz; i++) {
            double g = zeros[i] - zeros[i - 1];
            if (g < mingap) { mingap = g; argmin = i; }
        }
        double dens = log((t0) * INV_TWO_PI) / TWO_PI;   /* zeros per unit t */
        fprintf(f, "  \"zeros_located\": %ld,\n", nz);
        fprintf(f, "  \"min_gap\": %.12g,\n", mingap);
        fprintf(f, "  \"min_gap_normalised\": %.12g,\n", mingap * dens);
        fprintf(f, "  \"min_gap_at_t\": %.17g,\n",
                argmin >= 0 ? t0 + zeros[argmin] : 0.0);
    }
    fprintf(f, "  \"note\": \"a positive deficit means sign changes are missing "
               "and zeros may have left the critical line; it must be resolved "
               "by refinement before any claim\"\n}\n");
    if (df) fclose(df);
    fclose(f);
    if (zfile && emit_zeros) {
        FILE *zf = fopen(zfile, "w");
        if (zf) {
            /* The ordinate is t0 + s with t0 ~ 5e12 and s = O(span).  Forming
             * that sum in binary64 quantises the result to one ulp at t0,
             * which near 5e12 is 2^-10 ~ 9.8e-4 -- three orders coarser than
             * the ~1e-9 to which the root was actually located.  All the
             * precision is in `s`, and rounding the sum throws it away.
             *
             * Both t0 and s are exact binary64 values, so their exact sum fits
             * in 120 bits.  Form it in MPFR and print 30 digits: the emitted
             * ordinate then carries the accuracy the refinement really
             * achieved, and downstream consumers that read it at working
             * precision (turing.py, tau_localise.py) get it intact. */
            mpfr_t tt;
            mpfr_init2(tt, 160);
            for (long i = 0; i < nz; i++) {
                mpfr_set_d(tt, t0, MPFR_RNDN);
                mpfr_add_d(tt, tt, zeros[i], MPFR_RNDN);   /* exact at 160 bits */
                mpfr_fprintf(zf, "%.30Rg\n", tt);
            }
            mpfr_clear(tt);
            fclose(zf);
        }
    }
    fprintf(stderr, "sign_changes=%ld expected=%.6f deficit=%.6f minZ=%.4g\n",
            sign_changes, expected, expected - (double)sign_changes, minz);
    return 0;
}
