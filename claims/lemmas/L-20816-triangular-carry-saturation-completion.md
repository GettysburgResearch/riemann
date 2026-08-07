# L-20816 — Triangular carry saturation and elementary completion

Claim ID: `L-20816`  
Title: Nonnegativity of one explicit triangular carry solve gives the square-cutoff prime ramp with only a logarithmic-squared loss  
Status: `PROPOSED — ELEMENTARY COMPLETION PROVED; TRIANGULAR COEFFICIENT POSITIVITY OPEN`  
Authoring agent: `gpt56-03-x`  
Created: 2026-08-07  
Dependencies: `L-20815`; `L-20814`; `T-20804`  
Scope: exact final arithmetic hinge for the prime-positive diagonal route

## 1. The unique triangular saturation solve

Fix an integer `X>=2` and put

\[
 w_X(q)=q^{-1/2}\log(X/q),
 \qquad2\le q\le X.
 \tag{L-20816.1}
\]

Because `beta_(nn)=(n-1)/(n+1)>0`, there is one unique real vector

\[
 c_X(2),\ldots,c_X(X)
 \tag{L-20816.2}
\]

satisfying

\[
 \boxed{
 w_X(q)=\sum_{n=q}^Xc_X(n)\beta_{nq}
 \qquad(2\le q\le X).}
 \tag{L-20816.3}
\]

It is emitted by the backward recursion

\[
 \boxed{
 c_X(n)={n+1\over n-1}
 \left[
  w_X(n)-\sum_{m=n+1}^Xc_X(m)\beta_{mn}
 \right],
 \quad n=X,X-1,\ldots,2.}
 \tag{L-20816.4}
\]

In particular `c_X(X)=0` because `w_X(X)=0`.

The load-bearing statement is

\[
 \boxed{c_X(n)\ge0\quad(2\le n\le X).}
 \tag{CS(X)}
\]

It is called the **carry-saturation positivity statement**.

If `CS(X)` holds, `L-20815` gives the exact positive factorization

\[
 \boxed{
 \mathcal R(X)
 =\sum_{n=2}^Xc_X(n)G_n,}
 \tag{L-20816.5}
\]

where

\[
 \mathcal R(X)=
 \sum_{q=p^k\le X}{\Lambda(q)\over\sqrt q}\log(X/q).
 \tag{L-20816.6}
\]

The rest of this lemma proves that `CS(X)` alone supplies the strength required
for RH. No further prime estimate is assumed.

## 2. An elementary dual row inequality

Put

\[
 S_n=\sum_{q=2}^n\beta_{nq},
 \qquad
 V_n=\sum_{q=2}^n{\beta_{nq}\over\sqrt q}.
 \tag{L-20816.7}
\]

Then

\[
 \boxed{
 \sum_{q=2}^n\beta_{nq}
 \left(1-{64\over\sqrt q}\right)
 \le{n\over2}
 \qquad(n\ge2).}
 \tag{L-20816.8}
\]

### Proof

Let `K` be the continuum carry kernel of `L-20815`. Since
`beta_(nq)<=K(n/q)`, split the sum at `q=sqrt(n)`. The first part contributes at
most `sqrt(n)`. On `q>sqrt(n)`, the function `K(n/q)` is affine and monotone on
at most `sqrt(n)` quotient cells, is bounded between zero and one, and its upper
Riemann sum exceeds its integral by at most two per cell. Therefore

\[
 S_n\le
 n\int_1^\infty K(x)x^{-2}dx+3\sqrt n
 ={n\over2}+3\sqrt n.
 \tag{L-20816.9}
\]

For `n>4096`, take

\[
 {3(n+1)\over4}\le q\le n.
\]

Here `floor(n/q)=1` and

\[
 \beta_{nq}={2q-n-1\over n+1}\ge{1\over2}.
\]

There are at least `n/5` such integers, so

\[
 V_n\ge{\sqrt n\over10}.
 \tag{L-20816.10}
\]

Equations (L-20816.9)--(L-20816.10) prove (L-20816.8) for `n>4096`.
For `n<=4096`, every factor `1-64/sqrt(q)` is nonpositive, so the left side is
nonpositive. QED.

## 3. The leading carry mass is `4 sqrt(X)` up to `log^2(X)`

Assume `CS(X)` and define

\[
 L_X={1\over2}\sum_{n=2}^Xn c_X(n).
 \tag{L-20816.11}
\]

Multiply every saturated constraint (L-20816.3) by
`1-64/sqrt(q)`, sum in `q`, interchange the finite sums, and use
(L-20816.8). Since every `c_X(n)>=0`,

\[
\begin{aligned}
 L_X
 &\ge\sum_{q=2}^X
 \left(1-{64\over\sqrt q}\right)
 {1\over\sqrt q}\log(X/q)\\
 &=\sum_{q=2}^Xq^{-1/2}\log(X/q)
 -64\sum_{q=2}^Xq^{-1}\log(X/q).
\end{aligned}
 \tag{L-20816.12}
\]

Elementary integral comparison gives

\[
 \sum_{q=2}^Xq^{-1/2}\log(X/q)
 \ge4\sqrt X-O(\log X)
 \tag{L-20816.13}
\]

and

\[
 \sum_{q=2}^Xq^{-1}\log(X/q)
 \le{1\over2}\log^2X+O(\log X).
 \tag{L-20816.14}
\]

Consequently

\[
 \boxed{
 L_X\ge4\sqrt X-32\log^2X-O(\log X).}
 \tag{L-20816.15}
\]

The exact constant `64` is not important. Its role is to turn the order
`sqrt(n)` lattice discrepancy of the carry rows into a harmless `log^2(X)`
loss in the dual objective.

## 4. Logarithmic coefficient budget

Define

\[
 U_n=\sum_{q=2}^n{\beta_{nq}\over q}.
 \tag{L-20816.16}
\]

There is an absolute constant `c_0>0`; for definiteness one may take
`c_0=1/100` after increasing a fixed initial threshold, such that

\[
 \boxed{U_n\ge c_0\log(n+1)}
 \tag{L-20816.17}
\]

for all sufficiently large `n`.

A direct proof partitions `q` by `a=floor(n/q)`. For
`1<=a<=sqrt(n)/8`, retain the upper half of the interval
`n/(a+1)<q<=n/a`. On a subinterval of length at least a constant multiple of
`n/[a(a+1)]`, formula (L-20815.7) gives `beta_(nq)>=1/3`, while
`1/q>=a/n`. The contribution is at least a constant multiple of `1/(a+1)`;
summing in `a` proves (L-20816.17).

Multiply (L-20816.3) by `1/q` and sum. Under `CS(X)`,

\[
 \sum_{n=2}^Xc_X(n)U_n
 =\sum_{q=2}^Xq^{-3/2}\log(X/q)
 =O(\log X).
 \tag{L-20816.18}
\]

The finitely many `n` below the threshold are controlled individually by the
diagonal constraint

\[
 c_X(n){n-1\over n+1}\le w_X(n)=O_n(\log X).
\]

Therefore

\[
 \boxed{
 \sum_{n=2}^Xc_X(n)\log(n+1)=O(\log X),
 \qquad
 \sum_{n=2}^Xc_X(n)=O(\log X).}
 \tag{L-20816.19}
\]

## 5. Prime-ramp lower bound

Use the entropy estimate of `L-20815`:

\[
 G_n\ge{n\over2}-\log(n+1)-3.
\]

Equations (L-20816.5), (L-20816.15), and (L-20816.19) give

\[
\begin{aligned}
 \mathcal R(X)
 &=\sum_{n=2}^Xc_X(n)G_n\\
 &\ge L_X
 -\sum_{n=2}^Xc_X(n)\log(n+1)
 -3\sum_{n=2}^Xc_X(n).
\end{aligned}
\]

Hence

\[
 \boxed{
 \mathcal R(X)
 \ge4\sqrt X-O(\log^2X).}
 \tag{L-20816.20}
\]

This is already much stronger than a phase-blind prime-number-theorem error. It
is exactly the one-sided square-cutoff precision consumed by `L-20814`.

## 6. Completion of the zeta-screw estimate

For `X>=2`, the explicit archimedean term of `T-20802/L-20809` is

\[
 A(\log X)
 =4\sqrt X+B\log X+{C\over4}-8-R_0(\sqrt X),
 \tag{L-20816.21}
\]

where `R_0>=0`. Since

\[
 \Psi(\log X)=A(\log X)-\mathcal R(X),
\]

(L-20816.20) gives

\[
 \boxed{
 \Psi(\log X)\le O(\log^2X).}
 \tag{L-20816.22}
\]

At `X=N^2`,

\[
 \bigl(\Psi(2\log N)\bigr)_+
 =O(\log^2N)=N^{o(1)}.
 \tag{L-20816.23}
\]

The upper-envelope square-sampling theorem `L-20814` therefore proves RH.

## 7. Exact logical conclusion

The preceding argument proves the implication

\[
 \boxed{
 \left[\forall X\ge2\ \forall n\le X:\ c_X(n)\ge0\right]
 \quad\Longrightarrow\quad RH.}
 \tag{L-20816.24}
\]

All steps after coefficient positivity are explicit elementary inequalities and
the already isolated screw/Landau transfer.

## 8. Proof boundary

Closed:

- uniqueness and exact emission of the triangular coefficients;
- the dual carry-row inequality;
- the `4 sqrt(X)-O(log^2 X)` leading-mass estimate;
- the logarithmic coefficient budget;
- the complete deduction from carry saturation to RH.

Open:

- a proof that every coefficient emitted by (L-20816.4) is nonnegative.

This is now the sole arithmetic hinge of the carry-entropy full-proof proposal.
It is not replaced by finite numerical evidence.