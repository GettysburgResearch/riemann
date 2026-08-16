# L-96300 — MPFR-directed arithmetic encloses the complete Target-Lorenz tail

Claim ID: `L-96300`
Status: **PROVED DIRECTED FINITE/ASYMPTOTIC CERTIFICATE — HOSTILE REPLAY REQUESTED**
Created: 2026-08-16
Tail domain: `py>=166000`, `p>=67`, `1<=y<67`, `2<=j<=66`
Experiment: `X-96300-projective-full-row`
RH status: **unproved**

## 1. Repair of the old interval contract

The old Boost `rounded_transc_std<long double>` sweep treated standard-library
`sqrt` and `log` point values as singleton intervals.  Nonsquare inputs show
that such intervals cannot contain the exact transcendental values.

The repaired verifier uses MPFR 4.2.2 at 256 bits with `MPFR_RNDD` and
`MPFR_RNDU` for the base values

```text
sqrt(n), log(n), 1<=n<=67;
sqrt(166000), log(166000).
```

Every event value has the form `d*m`, where `d|P_61` and
`m in {1,j,j+1}`.  Its square root and logarithm are obtained only by outward
basic interval operations from the base enclosures:

\[
 \sqrt{dm}=\sqrt d\sqrt m,
 \qquad
 \log(dm)=\log d+\log m.
\]

No `libm` transcendental call occurs in the event sweep.

## 2. Complete event campaign

The exact event order is stored as unsigned 128-bit integer products.  The
campaign covers

```text
262,144 P61 divisors;
65 rows;
51,118,080 exact event records;
43,843,584 grouped activation events;
the final unbounded interval.
```

The complete causal determinant has the directed lower bound

\[
 \boxed{\Theta_j(p,y)>26.7858198871370094575061.}
\]

The global minimum certificate is at

```text
py=166000,
row j=66,
upper enclosure at that point <26.7866532123451376208589.
```

The parent determinant and its derivative satisfy

\[
 \boxed{\Theta_j^{\rm parent}>79.2368736388876425819072,}
\]

\[
 \boxed{{d\over dt}\Theta_j^{\rm parent}(t^2)
 >0.239715873017393372044407.}
\]

The final unbounded interval is certified by positive directed lower bounds for
the persistence polynomial and its derivative.  Row 66 is separated from the
nearest competing certificate row 65 by more than

\[
 1.45496583533057111461972.
\]

## 3. Proof object

The eight disjoint row chunks all return zero and aggregate to

```text
PASS_COMPLETE_MPFR_DIRECTED_TARGET_LORENZ_TAIL_51M
ba6b137b64819a9d01e706ffffdf100b091e49034895e6eeb280b56f514c99c5
```

The aggregate verifier checks all row ranges, event counts, positive margins,
minimum location and canonical digest.

```text
old singleton transcendental contract   rejected
MPFR base inclusion                      directed
all subsequent arithmetic                outward
all 65 rows / 51,118,080 records         certified
analytic tail persistence                 certified
RH                                       not concluded here
```
