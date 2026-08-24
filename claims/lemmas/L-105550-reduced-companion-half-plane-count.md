# L-105550 — Reduced companion half-plane count

Claim ID: `L-105550`  
Status: **PROVED EXACT FOR REAL POLYNOMIALS; REGULAR-WINDOW ARGUMENT-PRINCIPLE EXTENSION**  
Created: 2026-08-24  
Depends on: elementary argument principle and Cauchy index  
RH status: **not assumed**

## 1. Polynomial statement

Let `p in R[z]` be nonconstant, let

\[
g=\gcd(p,p'),\qquad P=p/g,\qquad Q=p'/g,
\]

and let `D=deg P`.  Thus `D` is the number of distinct complex roots of `p`,
counted once.  Fix `delta>0` and put

\[
E_\delta(z)=Q(z)+i\delta P(z).
\tag{L-105550.1}
\]

Because `P,Q` are coprime and real, `E_delta` has no real zero.  Let `N_+`
and `N_-` be its upper- and lower-half-plane zero counts, with multiplicity.
Let `R` be the number of distinct real roots of `p`.

Then

\[
\boxed{N_++N_-=D,\qquad N_+-N_-=R.}
\tag{L-105550.2}
\]

Consequently

\[
\boxed{N_+=\frac{D+R}{2},\qquad N_-=\frac{D-R}{2}.}
\tag{L-105550.3}
\]

In particular `N_-` is exactly the number of distinct nonreal conjugate root
pairs of `p`.  The result is independent of `delta>0`.

## 2. Proof

The degree of `E_delta` is `D`, so the first identity follows once real zeros
are excluded.  Traverse the upper-half-plane semicircle counterclockwise.
The leading term `i delta P(z)` changes argument by `D pi`.

On the real axis, the quotient `Q/P=p'/p` after common-factor cancellation has
one simple pole at every distinct real root `r` of `p`, with positive residue
equal to the multiplicity of `r` in `p`.  Thus its Cauchy index is `R`.
The curve

\[
Q(x)+i\delta P(x)=P(x)(Q(x)/P(x)+i\delta)
\]

acquires exactly `pi` of additional continuous argument at each such pole.
Hence the real-axis argument increment is `R pi`.  The argument principle gives

\[
2\pi N_+=\pi(D+R),
\]

which proves (L-105550.2)--(L-105550.3).  The lower count follows by degree.

This proof is the Hermite--Biehler/Cauchy-index identity with every common
factor cancelled before the count.

## 3. Companion Cayley ratio

On the real line define

\[
U_\delta(x)=\frac{Q(x)+i\delta P(x)}{Q(x)-i\delta P(x)}.
\tag{L-105550.4}
\]

It is unimodular and tends to `-1` at both ends.  On the one-point
compactification of the real line,

\[
\boxed{\operatorname{wind}U_\delta=R.}
\tag{L-105550.5}
\]

Thus the real-root count is a topological degree, not a magnitude estimate.

## 4. Regular entire-window form

Let `F` be real entire and let `(a,b)` be a regular interval.  Cancel every
common local factor of `F` and `F'` in the meromorphic quotient.  For a regular
conjugation-invariant rectangle whose boundary avoids the reduced companion
zeros, the same argument principle gives

```text
real distinct zeros in (a,b)
  = companion partial index in the rectangle
    + the literal endpoint Cauchy-index bits.
```

The endpoint term is the `V_a(F,F')-V_b(F,F')` ledger of `L-105500` and belongs
to `{-1,0,1}`.  No simplicity or coprimality assumption is imposed before the
local common factors are reduced.
