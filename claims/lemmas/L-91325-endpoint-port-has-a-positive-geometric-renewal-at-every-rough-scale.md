# L-91325 — The endpoint port has a positive geometric renewal at each single rough scale

> **SCOPE CORRECTION.** `R-91303` proves that positive one-scale details do not
> tensorize over distinct primes: the mixed `(67,71)` detail is negative at
> `x=4690`. This file proves the one-scale theorem and the same-scale geometric
> renewal only. Distinct-prime composition must retain the coupled matrix or
> three-state port.

Claim ID: `L-91325`  
Status: **PROPOSED COMPLETE EXACT ONE-SCALE RENEWAL THEOREM — MULTIPRIME TENSORIZATION REFUTED**  
Created: 2026-08-12  
Corrected: 2026-08-12 after `R-91303`  
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

At `n=q^2m`, the elementary bound `(1+y)^(-1/2)>=1-y/2` gives

\[
 H(q^2m)
 \ge\frac{(q-1)(q-2)}{2q^2\sqrt m}.
\tag{L-91325.10}

Since `q>=8`,

\[
 \frac{(q-1)(q-2)}{2q^2}
 \ge\frac{21}{64},
\tag{L-91325.11}

while

\[
 R_m\le\frac5{48\sqrt m}.
\tag{L-91325.12}

Therefore

\[
 H(n)-R_m
 \ge\frac1{\sqrt m}
 \left(\frac{21}{64}-\frac5{48}\right)
 =\frac{43}{192\sqrt m}>0.
\tag{L-91325.13}

Combining (L-91325.4), (L-91325.7), and (L-91325.13) proves the theorem. ∎

## 3. Positive single-scale detail atom

For an integer `R>=64`, let `a_R=log R` and define causally

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

No point in `Re z>0` is canceled. The exact same-scale renewal is

\[
 \boxed{
 \varrho(t)=
 \sum_{j=0}^{\lfloor t/a_R\rfloor}
 \eta_R(t-ja_R).
 }
\tag{L-91325.17}

## 4. Probability-law form

The critically normalized endpoint law `V` has density

\[
 f_V(t)=\frac12e^{-t/2}\varrho(t).
\tag{L-91325.18}

Put `r_R=R^-1/2` and define

\[
 \boxed{
 f_{Y_R}(t)=
 \frac{e^{-t/2}\eta_R(t)}{2(1-r_R)}.
 }
\tag{L-91325.19}

Since `widehat(varrho)(1/2)=2`, this has total mass one. Multiplying the renewal
by `e^-t/2/2` gives

\[
 \boxed{
 V\overset d=Y_R+(\log R)J_R,
 }
\tag{L-91325.20}

where `Y_R` and `J_R` are independent and

\[
 \boxed{
 \mathbb P(J_R=j)=(1-r_R)r_R^j,
 \qquad j\ge0.
 }
\tag{L-91325.21}

Thus repeated powers of one fixed rough scale admit a coefficient-one positive
geometric port decomposition.

## 5. Exact single-prime match

For one remaining rough prime `p>=67`, take `R=p`. The geometric ratio is

\[
 r_p=p^{-1/2},
\]

the same coefficient appearing in repeated powers of that prime. Along a branch
containing no other new prime, the native endpoint port decomposes as

```text
current block                         weight 1-p^(-1/2);
first p-delayed block                 weight (1-p^(-1/2))p^(-1/2);
second p-delayed block                weight (1-p^(-1/2))p^(-1);
...                                   ...
```

and the weights sum to one. This is a valid conservative ledger for arbitrary
powers of the **same** prime.

## 6. Distinct-prime firewall

For distinct primes `p,q`, positivity of `eta_p` and `eta_q` does not imply
positivity of

\[
 (I-S_p)(I-S_q)\varrho.
\]

`R-91303` gives the exact counterexample

\[
 \varrho(4690)-\varrho(4690/67)-\varrho(4690/71)<-1.33,
\]

because `4690/(67\cdot71)<1`.

Therefore the one-prime geometric laws cannot be tensorized into independent
scalar port pieces over the distinct-prime tree. Least-prime labels prevent
source duplication, but they do not prove scalar port disjointness.

Distinct-prime composition must retain one of the coupled structures already
available:

```text
matrix endpoint Schur port                  L-91316/L-91320;
positive three-state dilation               L-91323;
positive ordinary-column functor            L-91324.
```

## 7. Correct reset consequence

The theorem removes repeated-prime amplification inside one rough branch. It
also supplies useful positive single-scale blocks for a coupled matrix
colligation. It does **not** finish the all-generation port ledger.

The remaining theorem is:

> construct a conservative matrix/three-state composition over distinct rough
> primes, then apply the ordinary physical projection of `L-91324`, while
> retaining the factor-54 score recurrence.

## 8. Verification

The companion replay checks the exact analytic constants, 90,000
high-precision cell-endpoint mutation controls, renewal telescoping, and exact
geometric normalization.

Retained verdict:

```text
PASS_ROUGH_SCALE_ENDPOINT_PORT_RENEWAL
```

The counterexample companion is

```text
PASS_ROUGH_PORT_NON_TENSORIZATION_COUNTEREXAMPLE.
```

## 9. Proof boundary

```text
varrho(x)>varrho(x/R), R>=64                    EXACT
positive one-scale detail atom                  EXACT
zero-safe one-scale multiplier                  EXACT
same-scale geometric renewal                    EXACT
same-prime conservative power ledger            EXACT
distinct-prime scalar tensorization              REFUTED
coupled multiprime matrix/three-state ledger      OPEN
positive ordinary color erasure                  AVAILABLE
coefficient-one all-generation score recurrence  OPEN / RH-BEARING
Riemann Hypothesis                               UNPROVEN
```
