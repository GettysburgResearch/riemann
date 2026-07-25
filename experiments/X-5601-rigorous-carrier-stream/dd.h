/* dd.h -- double-double arithmetic used by the X-5601 rigorous carrier stream.
 *
 * Agent: opus5-01
 * Issue: #55 / #28
 *
 * Every routine here is the standard Dekker/Knuth double-double kernel.  The
 * error constants that the certificate relies on are stated in
 * `claims/lemmas/L-5601-double-double-carrier-enclosure.md`; this file only
 * has to be a faithful implementation of those kernels.
 *
 * The implementation requires an IEEE-754 binary64 FMA (checked at build time
 * through `-mfma`) and round-to-nearest-even, which is the default mode and is
 * never changed by this program.
 */
#ifndef X5601_DD_H
#define X5601_DD_H

#include <math.h>

typedef struct { double hi, lo; } dd;

static inline dd dd_of(double a) { dd r; r.hi = a; r.lo = 0.0; return r; }

/* |a| >= |b| required. Exact. */
static inline dd quick_two_sum(double a, double b) {
    dd r; r.hi = a + b; r.lo = b - (r.hi - a); return r;
}

/* Knuth two-sum. Exact for all finite inputs. */
static inline dd two_sum(double a, double b) {
    dd r; r.hi = a + b;
    double bb = r.hi - a;
    r.lo = (a - (r.hi - bb)) + (b - bb);
    return r;
}

/* Exact product using a single fused multiply-add. */
static inline dd two_prod(double a, double b) {
    dd r; r.hi = a * b; r.lo = fma(a, b, -r.hi); return r;
}

static inline dd dd_neg(dd a) { dd r; r.hi = -a.hi; r.lo = -a.lo; return r; }

static inline dd dd_add(dd a, dd b) {
    dd s = two_sum(a.hi, b.hi);
    dd t = two_sum(a.lo, b.lo);
    s.lo += t.hi;
    s = quick_two_sum(s.hi, s.lo);
    s.lo += t.lo;
    s = quick_two_sum(s.hi, s.lo);
    return s;
}

static inline dd dd_add_d(dd a, double b) {
    dd s = two_sum(a.hi, b);
    s.lo += a.lo;
    return quick_two_sum(s.hi, s.lo);
}

static inline dd dd_sub(dd a, dd b) { return dd_add(a, dd_neg(b)); }

static inline dd dd_mul(dd a, dd b) {
    dd p = two_prod(a.hi, b.hi);
    p.lo += a.hi * b.lo + a.lo * b.hi;
    return quick_two_sum(p.hi, p.lo);
}

static inline dd dd_mul_d(dd a, double b) {
    dd p = two_prod(a.hi, b);
    p.lo += a.lo * b;
    return quick_two_sum(p.hi, p.lo);
}

static inline dd dd_div(dd a, dd b) {
    double q1 = a.hi / b.hi;
    dd r = dd_sub(a, dd_mul_d(b, q1));
    double q2 = r.hi / b.hi;
    r = dd_sub(r, dd_mul_d(b, q2));
    double q3 = r.hi / b.hi;
    dd q = quick_two_sum(q1, q2);
    return dd_add_d(q, q3);
}

/* Exact numerator and denominator (both representable in binary64). */
static inline dd dd_div_dd_exact(double num, double den) {
    double q1 = num / den;
    dd p = two_prod(q1, den);          /* exact q1*den */
    double r = (num - p.hi) - p.lo;    /* exact remainder, no rounding */
    double q2 = r / den;
    return quick_two_sum(q1, q2);
}

static inline double dd_to_d(dd a) { return a.hi + a.lo; }

#endif /* X5601_DD_H */
