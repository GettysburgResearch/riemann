# L-91325 — The endpoint port has a positive geometric renewal at every rough-prime scale

Claim ID: `L-91325`  
Status: **PROPOSED COMPLETE EXACT ROUGH-SCALE RENEWAL THEOREM — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-12  
Depends on: `L-90025`, `L-91316`, elementary effective Euler summation  
RH status: **unproved**

## 1. Native endpoint port

For real `x>=1`, put

\[
 N=\lfloor x\rfloor,
 \qquad
 S_N=\sum_{k=1}^{N}k^{-1/2},
\]

and retain the positive endpoint kernel

\[
 \boxed{
 \varrho(x)=\frac{2N}{\sqrt x}-S_N>0.
 }
\tag{L-91325.1}

In logarithmic coordinates this is the kernel `varrho(t)` of `L-90025`, with
`x=e^t`.

`L-90025` proved positivity of the factor-four detail.  The rough-prime reset
needs the same statement at every integer scale at least `67`.  The following
theorem proves a stronger uniform result.

## 2. Rough-scale monotonicity theorem

### Theorem 2.1

For every integer `R>=64` and every real `x>=R`,

\[
 \boxed{
 \varrho(x)>\varrho(x/R).
 }
\tag{L-91325.2}

### Proof

Put

\[
 m=\left\lfloor\frac xR\right\rfloor,
 \qquad
 n=\lfloor x\rfloor=Rm+r,
 \qquad0\le r<R,
 \qquad q=\sqrt R\ge8.
\]

Then

\[
 \varrho(x)-\varrho(x/R)
 =\frac{2(n-qm)}{\sqrt x}-(S_n-S_m).
\tag{L-91325.3}

The coefficient `n-qm` is positive. Since `x<n+1`,

\[
 \varrho(x)-\varrho(x/R)
 >\frac{2(n-qm)}{\sqrt{n+1}}-(S_n-S_m).
\tag{L-91325.4}

Use the effective square-root-sum bounds already resident in `T-90002` and
`L-90025`:

\[
 S_n\le2\sqrt n+\zeta(1/2)+\frac1{2\sqrt n},
\tag{L-91325.5}
\]

\[
 S_m\ge2\sqrt m+\zeta(1/2)+\frac1{2\sqrt m}
 -\frac1{24m^{3/2}}-\frac1{16m^{5/2}}.
\tag{L-91325.6}

Thus

\[
 S_n-S_m
 \le2(\sqrt n-\sqrt m)
 +\frac1{2\sqrt n}-\frac1{2\sqrt m}
 +R_m,
\tag{L-91325.7}
\]

where

\[
 R_m=\frac1{24m^{3/2}}+\frac1{16m^{5/2}}.
\]

For fixed `m,q`, define on `n>=q^2m`

\[
 H(n)=
 \frac{2(n-qm)}{\sqrt{n+1}}
 -2\sqrt n-\frac1{2\sqrt n}
 +2\sqrt m+\frac1{2\sqrt m}.
\tag{L-91325.8}

Its derivative is

\[
 H'(n)=
 \frac{n+2+qm}{(n+1)^{3/2}}
 -\frac1{\sqrt n}
 +\frac1{4n^{3/2}}.
\tag{L-91325.9}

Moreover

\[
 \frac{n+2+qm}{(n+1)^{3/2}}
 >\frac{n+2}{(n+1)^{3/2}}
 >\frac1{\sqrt n},
\]

because

\[
 n(n+2)^2-(n+1)^3=n^2+n-1>0.
\]

Hence `H'(n)>0`; the aligned class `r=0` is the worst case.

At `n=q^2m`,

\[
 \frac{2(n-qm)}{\sqrt{n+1}}
 =2\sqrt m(q-1)
 \left(1+\frac1{q^2m}\right)^{-1/2}.
\]

The elementary bound `(1+y)^(-1/2)>=1-y/2` gives

\[
 H(q^2m)
 \ge\frac{(q-1)(q-2)}{2q^2\sqrt m}.
\tag{L-91325.10}

Since `q>=8`,

\[
 \frac{(q-1)(q-2)}{2q^2}
 \ge\frac{21}{64}.
\tag{L-91325.11}

Also

\[
 R_m\le\frac1{\sqrt m}\left(\frac1{24}+\frac1{16}\right)
 =\frac5{48\sqrt m}.
\tag{L-91325.12}

Therefore

\[
 H(n)-R_m
 \ge\frac1{\sqrt m}\left(\frac{21}{64}-\frac5{48}\right)
 =\frac{43}{192\sqrt m}>0.
\tag{L-91325.13}

Combining (L-91325.4), (L-91325.7), and (L-91325.13) proves
(L-91325.2). ∎

The proof is uniform; no finite scan over rough primes or quotient classes is
needed.

## 3. Positive rough-scale detail atom

For an integer `R>=64`, let

\[
 a_R=\log R
\]

and define causally

\[
 \boxed{
 \eta_R(t)=\varrho(t)-\varrho(t-a_R),
 \qquad
 \varrho(s)=0\quad(s<0).
 }
\tag{L-91325.14}

Theorem 2.1 and positivity of `varrho` on the first block give

\[
 \boxed{
 \eta_R(t)>0
 \qquad(t>0).
 }
\tag{L-91325.15}

Its Laplace transform is

\[
 \boxed{
 \widehat\eta_R(z)
 =(1-R^{-z})\widehat\varrho(z).
 }
\tag{L-91325.16}

No point in the RH-facing half-plane is canceled: if `Re z>0`, then
`|R^{-z}|<1`.

The endpoint port has the exact positive renewal

\[
 \boxed{
 \varrho(t)=
 \sum_{j=0}^{\lfloor t/a_R\rfloor}
 \eta_R(t-ja_R).
 }
\tag{L-91325.17}

The sum is finite at every physical time.

## 4. Probability-law form

The critically normalized endpoint law `V` has density

\[
 f_V(t)=\frac12e^{-t/2}\varrho(t).
\tag{L-91325.18}

Put

\[
 r_R=R^{-1/2}
\]

and define

\[
 \boxed{
 f_{Y_R}(t)=
 \frac{e^{-t/2}\eta_R(t)}{2(1-r_R)}.
 }
\tag{L-91325.19}

Because `widehat(varrho)(1/2)=2`,

\[
 \int_0^\infty f_{Y_R}(t)dt
 =\frac{(1-r_R)\widehat\varrho(1/2)}{2(1-r_R)}=1.
\]

Thus `Y_R` is a probability law.  Multiplying (L-91325.17) by
`e^{-t/2}/2` gives

\[
 \boxed{
 V\overset d=Y_R+a_RJ_R,
 }
\tag{L-91325.20}

where `Y_R` and `J_R` are independent and

\[
 \boxed{
 \mathbb P(J_R=j)=(1-r_R)r_R^j,
 \qquad j\ge0.
 }
\tag{L-91325.21
 }

Thus the native endpoint port itself splits into one positive block plus an
independent geometric chain of `R`-delayed copies.

## 5. Exact match to rough-prime branching

For every remaining rough prime `p>=67`, take `R=p`.  The geometric ratio in
(L-91325.21) is exactly

\[
 r_p=p^{-1/2},
\]

the coefficient of the rough-prime renewal and affine Pascal scaling.  Hence a
rough branch does not require a duplicated copy of the parent endpoint port:
its delayed ports are the disjoint positive geometric-renewal components of the
parent port itself.

At one branch:

```text
current positive port block        weight 1-p^(-1/2);
first delayed port                 weight (1-p^(-1/2))p^(-1/2);
second delayed port                weight (1-p^(-1/2))p^(-1);
...                                ...
```

The weights sum exactly to one.  The port is therefore coefficient-one and
conservative across arbitrarily many repetitions of the same rough prime.

Combining with `L-91320/L-91324`:

1. the projective correction at each rough step is strictly smaller than the
   branch's `1/9` Schur reserve;
2. positive physical color erasure preserves that domination;
3. the unused port is transferred to the delayed child by the geometric renewal
   rather than copied;
4. no port mass is spent twice along a prime-power branch.

Unique least-prime routing then nests these conservative geometric renewals over
distinct rough primes.  Every source packet follows one branch, while every
branch carries a disjoint portion of the native endpoint port.

## 6. Consequence for the reset assembly

The two former physical objections now have exact positive answers:

```text
nonmultiple colored-column load:
    preserved and paid under positive-functor color erasure;

apparent replication of one Schur port on infinitely many children:
    removed by the native geometric rough-scale port renewal.
```

The remaining reset task is no longer a capacity projection.  It is the explicit
bookkeeping theorem which combines the already positive branch transitions into
one contracted endpoint vector and writes the coefficient-one score recurrence
in the notation of `T-91101`.

## 7. Verification boundary

The companion replay checks the exact constants in the proof, the quotient-cell
formula, extensive rough-scale numerical controls, the renewal telescoping, and
the geometric probability normalization.  The proof of Theorem 2.1 is analytic;
the finite controls are mutation guards only.

Retained verdict:

```text
PASS_ROUGH_SCALE_ENDPOINT_PORT_RENEWAL
```

## 8. Proof boundary

```text
varrho(x)>varrho(x/R), R>=64                    EXACT
positive rough-scale detail atom                 EXACT
zero-safe rough-scale multiplier                 EXACT
positive endpoint-port renewal                   EXACT
geometric probability decomposition              EXACT
coefficient-one branch-port propagation          EXACT
positive physical color erasure                  AVAILABLE
explicit all-generation endpoint-vector ledger   OPEN
coefficient-one score recurrence                 OPEN / RH-BEARING
Riemann Hypothesis                               UNPROVEN
```
