# L-91880 — The exact native hybrid decomposes into a positive source sort, a row-only Hall sort, and one signed observation ledger

Claim ID: `L-91880`  
Status: **CANDIDATE-COMPLETE EXACT ARITHMETIC FIBRE ON FROZEN INPUTS — REVIEW REQUIRED**  
Created: 2026-08-16  
Depends on: `R-91880`; frozen native hybrid identity from PR #509; root Hall theorem and target-normalized row monotonicity from PR #506; exact finite stopping line  
RH status: **unproved**

## 1. Exact native hybrid

For integer `X`, let

\[
K=\left\lfloor \frac X{67}\right\rfloor+1,
\qquad
W=10000,
\]

and let `I_X` be the complete retained integer-cell set

\[
I_X=\{n\in\mathbb Z:K+2\le n\le X-W-3\}.
\]

The exact native finite row has the hybrid identity

\[
\boxed{
c_X=c_{X,A}+\overline c_{X,I}+\mathcal R E_X^I.
}
\tag{L-91880.1}
\]

Here:

```text
c_(X,A)       exact finite native row on complementary anchored cells;
bar c_(X,I)   exact native Volterra row on the same retained complete cells;
R E_X^I       signed retained-cell finite/continuum comparison.
```

The first two terms come from native Möbius occurrences. The third is observation data and is not positive source.

## 2. Bulk native Möbius marginal

On a retained endpoint fibre `s`, put `x=X/s<67` and

\[
\ell_x(k)=k^{-1/2}\left(2\sqrt{x/k}-1\right)>0.
\]

Let `p_s` be the common positive infinitesimal component packet. The paired bulk source marginals are

\[
d\Sigma_{X,I}^{\pm}(s,k)
=
\frac2s\,
\mathbf 1_{\mu(k)=\pm1}\,
\ell_{X/s}(k)\,ds.
\tag{L-91880.2}
\]

Every colour multiplies the same `p_s`. Put

\[
P_+(s)=\sum_{\mu(e)=1}\ell_x(e),
\qquad
P_-(s)=\sum_{\mu(o)=-1}\ell_x(o).
\]

The factor-67 density theorem gives

\[
P_+(s)-P_-(s)=L(x)>\frac{159}{500}.
\]

Define the exact rank-one coupling

\[
\pi_s(o,e)
=
\frac{\ell_x(o)\ell_x(e)}{P_+(s)}
\tag{L-91880.3}
\]

and residual

\[
r_s(e)
=
\ell_x(e)\frac{P_+(s)-P_-(s)}{P_+(s)}.
\tag{L-91880.4}
\]

Then

\[
(\pi_s)_-=\Sigma^-_{X,I,s},
\qquad
(\pi_s)_++r_s=\Sigma^+_{X,I,s}.
\tag{L-91880.5}
\]

Because every colour has the same physical feature `p_s`, matched incidences cancel in every component, ordinary, detail, literal-score, and intrinsic-boundary observation. The residual output is exactly

\[
\boxed{
\sum_e r_s(e)p_s=L(x)p_s\ge0.
}
\tag{L-91880.6}
\]

No rough ownership or causal reset is applied to this bulk packet.

## 3. Anchored finite Hall fibre

The anchored source is the literal finite native paired source, expanded through the exact `P_61` stopping line. On each root Hall fibre the deterministic target coupling gives a positive residual source `c` and a row-only bonus `B` with

\[
T(c)=T(E)-T(O),
\tag{L-91880.7}
\]

\[
S(c)\ge S(E)-S(O),
\tag{L-91880.8}
\]

\[
R(c)+B=R(E)-R(O),
\qquad B\ge0.
\tag{L-91880.9}
\]

The score surplus

\[
\sigma=S(c)-[S(E)-S(O)]\ge0
\tag{L-91880.10}
\]

is recorded separately. The exact obstruction in `R-91880` forbids assigning a declared-score packet coordinate to `B`.

Thus the anchored output is the direct-sum typed object

\[
\boxed{(c;B;\sigma).}
\tag{L-91880.11}
\]

Only `c` enters the native source tree. `B` is a current finite physical row.

## 4. Two source sectors and one row sort

The exact fibre has three ledgers:

```text
positive source ledger:
    anchored Hall residual source;
    retained bulk rank-one residual source;
    literal bottom/top omissions;
    one common discard;

row-only ledger:
    anchored Hall edge bonuses;
    exact finite anchored rows;

signed observation ledger:
    retained-cell finite/continuum comparison;
    intrinsic bulk collar;
    terminal comparison.
```

The q=2 Hall-score obstruction is therefore respected by construction. Equations (L-91880.1), (L-91880.6), and (L-91880.7)--(L-91880.10) give the exact native target, score inequality, and component-row observation before finite realization.

## 5. Boundary

```text
native anchored marginal                 exact finite Möbius source
native retained bulk marginal            exact Volterra Möbius source
bulk Hall cancellation                    exact rank-one incidence
bulk causal split                         absent / forbidden
anchored Hall residual source             positive and target-exact
anchored Hall row bonus                   nonnegative / row-only
declared-score surplus                    separate nonnegative scalar
signed finite comparison                  separate observation ledger
Riemann Hypothesis                        unproved
```
