# L-91408 — Finite delayed causal prime packets have an exact safe Wick–Green factorization

Claim ID: `L-91408`  
Status: **PROVED EXACT SAME-ORIENTATION CARRIER/DELAY PRIME FACTORIZATION; REFLECTED MIXED BLOCK OPEN**  
Created: 2026-08-12  
Depends on: `L-91026`, `L-91405`  
RH status: **unproved**

## 1. Labelled delayed causal tests

Fix `a>1/2` and retain

\[
 \psi_a(v)
 =\mathbf1_{v\ge0}
  \sum_{r\in\{1,2,4\}}
  (A_{r,a}+B_{r,a}v)e^{-rav}.
\]

For a carrier `x in R` and positive physical delay `delta>=0`, define

\[
 \boxed{
 f_{x,\delta}(v)
 =\mathbf1_{v\ge\delta}
  e^{ix(v-\delta)}
  \psi_a(v-\delta).
 }
\tag{L-91408.1}
\]

This is the physical representative of the frequency-domain test

\[
 e^{-iu\delta}\Psi_a(u-x)
\]

in the Fourier convention of the branch.

Write its three labelled modes as

\[
 f_{x,\delta}(v)=\sum_r f_{r;x,\delta}(v),
\]

\[
 f_{r;x,\delta}(v)
 =\mathbf1_{v\ge\delta}
  e^{ix(v-\delta)}
  (A_{r,a}+B_{r,a}(v-\delta))
  e^{-ra(v-\delta)}.
\tag{L-91408.2}
\]

The labels are retained as part of the source construction; no quotient by a
possible redundant packet representation is taken.

## 2. Safe tilted jump spaces

Let

\[
 d\Pi(u)
 =\sum_{n=p^k}\frac{\Lambda(n)}{\sqrt n}
  \delta_{\log n}(du)
\]

and

\[
 d\Pi_{r,a}(u)=e^{-rau}d\Pi(u).
\]

For each `r`, put

\[
 \mathcal X_{r,a}^{\rm del}
 =L^2\left(
  (0,\infty)_u\times(0,\infty)_v,
  d\Pi_{r,a}(u)dv
 
\right).
\tag{L-91408.3}
\]

All polynomial jump moments are finite because `1/2+ra>1`.

## 3. Delayed production and endpoint maps

For a label `i=(x,delta)`, define

\[
\boxed{
\begin{aligned}
 U_{r,i}(u,v)
 ={}&\mathbf1_{v+u\ge\delta}
 e^{ix(v+u-\delta)}\\
 &\times
 (A_{r,a}+B_{r,a}(v+u-\delta))
 e^{-ra(v-\delta)},
\end{aligned}}
\tag{L-91408.4}
\]

and

\[
 \boxed{
 V_{r,i}(u,v)=f_i(v).
 }
\tag{L-91408.5}

Although the last exponential in (L-91408.4) may grow on the bounded interval
`0<=v<delta`, the indicator and fixed delay make the norm finite.  For large
`v` there is exponential decay, and all `u`-moments are safe.

The key identity is

\[
 \boxed{
 f_i(v+u)
 =\sum_{r\in\{1,2,4\}}
  e^{-rau}U_{r,i}(u,v).
 }
\tag{L-91408.6}

Indeed (L-91408.6) is just the three-mode expansion of the shifted delayed
state, with the complete jump decay extracted into the tilted measure.

## 4. Mixed carrier–delay cross correlations

For two independent labels `i=(x,delta)` and `j=(y,eta)`, define

\[
 k_{ij}(u)
 =\int_0^\infty f_i(v+u)\overline{f_j(v)}dv,
\tag{L-91408.7}
\]

\[
 k_{ij}(-u)
 =\int_0^\infty f_i(v)\overline{f_j(v+u)}dv.
\tag{L-91408.8}
\]

Let

\[
 U_i=(U_{r,i})_r,
 \qquad
 V_i=(V_{r,i})_r
\]

in the direct sum of the three safe spaces.  Using (L-91408.6),

\[
 \boxed{
 \langle U_i,V_j\rangle
 =\int_0^\infty k_{ij}(u)d\Pi(u),
 }
\tag{L-91408.9}
\]

and

\[
 \boxed{
 \langle V_i,U_j\rangle
 =\int_0^\infty k_{ij}(-u)d\Pi(u).
 }
\tag{L-91408.10}

Thus every cross-carrier and cross-delay prime term is retained before taking
a norm.

## 5. Exact delayed prime block

The prime contribution to the Weil Gram of the two delayed tests is

\[
 \boxed{
 \mathfrak P_a^{\rm del}(i,j)
 =-\langle U_i,V_j\rangle
  -\langle V_i,U_j\rangle.
 }
\tag{L-91408.11}

Define

\[
 D_i=U_i-V_i.
\]

Then the fully polarized Wick–Green identity is

\[
 \boxed{
\begin{aligned}
 \mathfrak P_a^{\rm del}(i,j)
 ={}&\langle D_i,D_j\rangle\\
 &-\langle U_i,U_j\rangle\\
 &-\langle V_i,V_j\rangle.
\end{aligned}}
\tag{L-91408.12}

All three kernels are positive Grams in explicit safe first-chaos spaces.  No
raw-delay invariance of `K_(Theta_a)` is used.

## 6. Finite packet form

For a finite labelled packet and coefficients `c_i`, put

\[
 U_c=\sum_i c_iU_i,
 \qquad
 V_c=\sum_i c_iV_i,
 \qquad
 D_c=U_c-V_c.
\]

Then

\[
 \boxed{
 \sum_{i,j}\overline{c_i}
  \mathfrak P_a^{\rm del}(i,j)c_j
 =\|D_c\|^2-\|U_c\|^2-\|V_c\|^2.
 }
\tag{L-91408.13}

This is the exact source-side production-minus-endpoint identity sought for
the delayed causal half of CDFHGI.

## 7. Relation to compressed model-space delay

`L-91401` decomposes a raw Hardy delay into its resident model-space component
and Julia leakage.  The present theorem is the independent prime-source
factorization of the labelled physical delayed tests themselves.

The two constructions can be composed:

```text
labelled physical delayed Cauchy test
 -> safe prime Wick-Green source (this lemma);
 -> resident model-space delay + Julia leakage (L-91401).
```

A complete proof must show that the corresponding endpoint and leakage Grams
match in one completed source normalization.

## 8. What remains

Reflection of (L-91408.1)--(L-91408.13) gives the pure anti-causal block.  The
mixed causal/anti-causal block requires a two-sided state space because the
cross-correlation integral is no longer supported on one common positive
half-line.  The finite bridge must then be inserted into that same two-sided
Green identity.

The remaining steps are therefore explicit:

```text
construct the mixed-orientation safe Green source;
adjoin the bridge state;
combine the gamma/pole/theta boundary kernel with the endpoint Grams;
prove the resulting Schur complement positive.
```

## 9. Exact boundary

```text
finite labelled positive-delay causal packet          EXACT
safe tilted source maps U,V,D                         EXACT
all same-orientation carrier/delay cross terms         EXACT
Wick-Green packet identity                            EXACT
raw model-space delay assumption                      NOT USED
pure reflected anti-causal block                      BY REFLECTION
mixed causal/anti-causal Green block                  OPEN
bridge insertion                                      OPEN
completed boundary Schur complement                   OPEN / RH-BEARING
Riemann Hypothesis                                    UNPROVED
```
