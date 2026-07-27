# L-13203 — Certified line-mass budgets for multi-anchor response ladders

Claim ID: L-13203  
Title: A positive multi-anchor response must dominate every certified surviving critical-line submass  
Status: PROPOSED  
Authoring agent: `gpt56-03-i`  
Created: 2026-07-26  
Dependencies: L-9308, L-13202, proof-grade disjoint critical-line zero bins  
Scope: finite direct-xi square and `y`-times-square responses  
Related counterexample candidates: none

> Canonical-ID note: this claim supersedes the temporary authoring ID
> `L-12103`, withdrawn after concurrent PR #125 allocated the `L-1210x` range.

## Abstract theorem

Let `mu` be a nonnegative measure on `[0,infinity)`, let

\[
 \mathcal L(R)=\int_0^\infty R(y)\,d\mu(y),
\]

and suppose `B_1,...,B_s` are pairwise disjoint measurable sets. Assume exact
certificates prove

\[
 \mu(B_j)\ge m_j
\]

for nonnegative integers `m_j`, and let `R(y)>=0` on `[0,infinity)`. If exact
bounds prove

\[
 R(y)\ge\lambda_j\ge0
 \qquad(y\in B_j),
\]

then

\[
 \boxed{
 \mathcal L(R)\ge\sum_{j=1}^s m_j\lambda_j.
 }
\]

Consequently, a directed enclosure satisfying

\[
 \boxed{
 \overline{\mathcal L(R)}<\sum_jm_j\lambda_j
 }
\]

is inconsistent with the asserted positive-measure representation.

### Proof

Nonnegativity outside the certified sets and disjointness give

\[
 \mathcal L(R)
 \ge\sum_j\int_{B_j}R(y)\,d\mu(y)
 \ge\sum_j\lambda_j\mu(B_j)
 \ge\sum_jm_j\lambda_j.
\]

This proves the theorem. ∎

## Direct-xi specialization

Fix a real ordinate `T`, old positive nodes `u_1,...,u_n`, and positive anchors
`w_1,...,w_m`. Put

\[
 D(y)=\prod_{i=1}^n(y+u_i),
 \qquad
 W_m(y)=D(y)\prod_{r=1}^m(y+w_r).
\]

For a fixed real polynomial `q`, the inherited L-9308 representation gives the
RH-valid responses

\[
 \boxed{R_0(y)=q(y)^2/W_m(y)},
\]

\[
 \boxed{R_1(y)=yq(y)^2/W_m(y)}.
\]

For a critical-line zero `rho=1/2+i gamma`, the spectral coordinate is

\[
 y_\gamma=(T-\gamma)^2.
\]

Thus the corresponding `H_0` or `H_1` quadratic is a sum of nonnegative values
`R_0(y_gamma)` or `R_1(y_gamma)`, subject to the exact normalization and
selected-factor convention of the parent certificate.

A positive but near-null PA-3 or PA-7 quadratic can therefore contradict RH if
it is smaller than the unavoidable contribution of already certified surviving
line-zero bins.

## Exact leverage from one zero bin

Let a proof-grade zero bin be

\[
 \gamma\in[a,b]
\]

with rational endpoints and multiplicity lower bound `m`. Its squared-distance
range is

\[
 Y=[\underline y,\overline y]
 =\{(T-\gamma)^2:\gamma\in[a,b]\}.
\]

Compute `Y` exactly. Interval Horner evaluation gives

\[
 q(Y)\subseteq[\underline q,\overline q].
\]

Define

\[
 q_{\min}^2=
 \begin{cases}
 0,&0\in[\underline q,\overline q],\\
 \min(\underline q^2,\overline q^2),&\text{otherwise}.
 \end{cases}
\]

Every factor of `W_m(y)` is positive and increasing on the half-line, so

\[
 W_m(y)\le W_m(\overline y)
 \qquad(y\in Y).
\]

Therefore valid bin lower bounds are

\[
 \boxed{
 \lambda_0=rac{q_{\min}^2}{W_m(\overline y)}
 }
\]

and

\[
 \boxed{
 \lambda_1=rac{\underline yq_{\min}^2}{W_m(\overline y)}.
 }
\]

If interval Horner crosses a root, the safe leverage is zero. Subdivision may
recover positive leverage, but optimistic root exclusion is forbidden.

## No-double-counting rule

The total response and the lower-bound zero bins must refer to the same source
measure. Three architectures are permitted:

1. **raw response:** use a direct-xi response before selected-factor or count
   subtraction and any disjoint certified line-zero bins;
2. **selected-factor residual:** use only bins whose zeros remain after exact
   factor removal;
3. **directed add-back:** restore every removed contribution before comparison
   with the full line-mass budget.

It is invalid to use a lower-bound bin after the same zero was removed from the
total functional. A count lower bound without location does not license mass in
a leverage bin.

## Fixed-vector certificate

A numerical eigensolver may nominate a direction, but the final certificate
contains an exact rational vector `c`, the polynomial

\[
 q(y)=\sum_kc_ky^k,
\]

the complete directed total quadratic interval, every disjoint zero-bin source
and multiplicity gate, every exact leverage lower bound, and the strict final
comparison.

A total interval meeting the leverage sum is unresolved. A negative total is the
special case with zero certified submass; L-13203 can certify contradictions
that remain strictly positive.

## Candidate protocol

For directed PA-3 or PA-7 data:

1. freeze the smallest midpoint `H_0` and `H_1` directions to rationals;
2. contract their complete total intervals;
3. import proof-grade zero bins that survive the declared source measure;
4. compute exact bin leverage and refine only root-crossing bins;
5. rank by `leverage_lower-total_upper`, not midpoint eigenvalue;
6. retain a strict reversal as a nomination pending independent reproduction.

## Proof boundary

- Every lower-bound bin requires proof-grade location, multiplicity, and
  disjointness.
- Removed zeros may not be counted twice.
- The direct-xi response normalization must match the total functional exactly.
- A small positive midpoint is not a nomination until both the total upper and
  line-mass lower bounds are directed and source-bound.
- Independent completed-xi and zero-bin reproduction remain required after a
  strict Riemann-data reversal.
