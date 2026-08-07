# T-26201 — Endpoint-scale frame proposal for RH

Claim ID: `T-26201`  
Title: Square-root control of the parabolic endpoint blockers produces a genuine nonnegative carry packing with full critical mass and implies RH  
Status: **FULL PROPOSAL — ONE EXPLICIT ENDPOINT-BLOCKER THEOREM OPEN**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-08  
Issue family: `#245/#262`  
Frozen base: PR #248 at `5f2b25f89afbb90a3bc4ca6d40148f530303eb54`  
Dependencies: `L-26201`--`L-26203`; PR #244 `L-23705`; repository square-screw/Landau transfer  
RH status: **UNPROVEN**

## 1. Main theorem and exact hinge

For every endpoint `X`, run the endpoint-scale greedy algorithm of `L-26203`.
It produces nonnegative weights `lambda_T`, nonnegative carry rows

\[
 d_X^{\rm sc}=\sum_{T=3}^X\lambda_Ta_T,
\]

and endpoint blocker losses `ell_T`.

The sole new asymptotic theorem requested by this proposal is:

> **Endpoint-Scale Blocker Theorem (`ESBT`).** There exist absolute constants
> `A,C` such that, for every integer `X>=3` and every `3<=T<=X`,
> \[
> \boxed{
>  \ell_T\le C\sqrt T\,\log^A(2X).}
> \tag{ESBT}
> \]

The weaker aggregate theorem

\[
 \boxed{
 \Sigma_X^{\rm sc}
 =\sum_{T=3}^X\Gamma_T(T-1)\ell_T
 =X^{o(1)}
 }
\tag{ESGS}
\]

is logically sufficient.  `ESBT` is preferred because it is local, has a
simple scale exponent, and is directly adapted to the exact diagonal decay
`Gamma_T(T-1) asymp T^(-3/2)`.

## 2. Exact positive construction

`L-26201` proves, unconditionally, that the parabolic endpoint increments

\[
 a_T=d_T-d_{T-1}
\]

are coefficientwise nonnegative average-binomial carry rows.  Their unweighted
sum has the sharp entropy score

\[
 \sum_{T=3}^XH_T
 \ge4\sqrt X-O(\log X).
\]

`L-26203` runs a backward minimum-ratio algorithm on these atoms and proves
exactly

\[
 d_X^{\rm sc}(n)\ge0,
\tag{T-26201.1}
\]

\[
 \sum_nd_X^{\rm sc}(n)\beta_{nq}
 \le q^{-1/2}\log(X/q)
 \qquad(2\le q\le X).
\tag{T-26201.2}
\]

Thus the proposal does not ask a signed Green correction to become positive
after the fact.  Positivity is built into the construction at every step.

## 3. `ESBT` gives polylogarithmic total slack

The exact scale-slack identity is

\[
 \Sigma_X^{\rm sc}
 =\sum_{q=2}^{X-1}\gamma_q\ell_{q+1},
\qquad
 \gamma_q=\Gamma_{q+1}(q).
\tag{T-26201.3}
\]

`L-26203` proves

\[
 \frac1{5q^{3/2}}
 \le\gamma_q
 \le\frac1{2q^{3/2}}.
\tag{T-26201.4}
\]

Assuming `ESBT`,

\[
 \begin{aligned}
 \Sigma_X^{\rm sc}
 &\le
 C\log^A(2X)
 \sum_{q=2}^{X-1}\frac{\sqrt{q+1}}{2q^{3/2}}\\
 &=O(\log^{A+1}(2X)).
 \end{aligned}
\tag{T-26201.5}
\]

No cancellation is used after the blocker estimate.

## 4. Polylogarithmic scale slack gives the full `4 sqrt(X)` mass

The universal feasible-vector theorem of PR #244 gives

\[
 \sum_n n d_X^{\rm sc}(n)
 =8\sqrt X-2\Sigma_X^{\rm sc}+O(\log^2X),
\tag{T-26201.6}
\]

and

\[
 \sum_nd_X^{\rm sc}(n)(\log(n+1)+3)
 =O(\log^2X).
\tag{T-26201.7}
\]

Therefore

\[
 \boxed{
 \sum_nd_X^{\rm sc}(n)G_n
 \ge4\sqrt X-O(\log^{A+1}(2X)).}
\tag{T-26201.8}
\]

Multiplying the column inequalities (T-26201.2) by the nonnegative von
Mangoldt weights and using Legendre/Kummer gives the complete prime-power ramp
bound

\[
 \boxed{
 \sum_{q=p^k\le X}
 \frac{\Lambda(q)}{\sqrt q}\log\frac Xq
 \ge4\sqrt X-O(\log^{A+1}(2X)).}
\tag{T-26201.9}
\]

The ordinary-prime reduction of PR #248 may be inserted, but is not needed for
this implication.

## 5. Prime ramp to RH

At square endpoints `X=N^2`, the repository's exact square-screw identity has
archimedean main term `4N`.  Equation (T-26201.9) gives a polylogarithmic upper
envelope for the adverse screw channel.  The frozen square-mesh interpolation
and Landau pole-exclusion argument then give rightmost-zero exponent zero.
Functional-equation symmetry yields

\[
 \boxed{\mathrm{ESBT}\Longrightarrow\mathrm{RH}.}
\tag{T-26201.10}
\]

The downstream normalization remains source-pinned to the independently
reviewed square-screw consumer; no finite numerical ladder is used.

## 6. Why this hinge is different from the prior ones

### 6.1 Not Carry Saturation

The exact triangular inverse need not be coefficientwise positive.  The scale
greedy may leave slack, and `ESBT` controls only the loss created by its explicit
minimum-ratio choices.

### 6.2 Not the monotone Divisibility Cover

The rejected cover deleted positive defect and paid `log m` per unit.  The scale
frame reweights already positive endpoint atoms and charges the exact diagonal
amount `asymp T^(-3/2)`.

### 6.3 Not the signed Green correction

The canonical Green solution is an exact signed equality object.  Here every
row coefficient is nonnegative from the beginning.  The price is one positive
scale-weight theorem rather than a positivity-preserving deformation of
`G_X^{-1}r`.

### 6.4 Not the original Greedy Slack Theorem

PR #244's blocker diagonal is

\[
 \beta_{qq}\asymp1.
\]

The endpoint-scale blocker diagonal is

\[
 \gamma_q\asymp q^{-3/2}.
\]

Consequently bounded blocker losses are unnecessary: square-root growth is
still harmless.  This is a substantially wider proof target.

## 7. Proposed proof attack on `ESBT`

The exact ingredients now point to a concrete attack.

### Step A — use the continuum flux

`L-26202` proves

\[
 \int_\theta^1E(u)du\le0
\]

for every scale.  Thus every continuum defect is transportable to slack at a
larger scale with nonpositive logarithmic cost.  A finite proof should preserve
this order instead of separating positive and negative parts.

### Step B — exploit contiguous endpoint freezes

An off-diagonal blocker `q_T<T-1` forces

\[
 \lambda_U=0
 \qquad(q_T<U<T).
\]

Hence the complete blocker ledger is a sequence of contiguous scale intervals.
There is no branching graph.  Emit the maximal frozen intervals and charge
one continuum-flux budget to each interval.

### Step C — reciprocal-cell bulk estimate

For a block with lower endpoint above a polylogarithmic scale, compare the exact
finite response `Gamma_T(q)` to the derivative of the reciprocal-cell formula
in `L-26202`.  The required estimate is not an absolute approximation of the
prime ramp; it is the directed inequality that the incoming tail slack pays the
outgoing blocker ratio.

### Step D — terminal scale

For `T<=log^B(2X)`, the trivial diagonal bound is already of the form `ESBT`
after increasing `A`.  Thus only the bulk scale requires a transport theorem.

### Step E — exact mutation

The proof must retain the dyadic/`2/3` fixed-ratio Mertens shell.  A finite
scale ledger which loses that coordinate or takes absolute values before the
continuum-tail recombination is invalid.

## 8. Fail-closed rejection conditions

The proposal is **UNPROVEN** unless all of the following are supplied:

1. a uniform proof of `ESBT` or `ESGS`;
2. every endpoint atom and blocker emitted exactly;
3. directed finite-floor errors on every reciprocal cell;
4. no use of prime-ramp asymptotics to prove the scale slack itself;
5. preservation of the fixed-ratio Möbius mutation;
6. independent audit of the square-screw/Landau orientation.

A counterfamily with

\[
 \ell_T\gg T^{1/2+\delta}
\]

on sufficiently many scales would invalidate `ESBT`; it would not invalidate
the exact positive frame or the aggregate `ESGS` alternative.

## 9. Exact proof boundary

```text
parabolic seed as nonnegative carry rows       PROPOSED COMPLETE
positive endpoint increments                   PROPOSED COMPLETE
endpoint-scale greedy feasibility               PROPOSED COMPLETE
exact blocker and interval-freeze ledgers       PROPOSED COMPLETE
continuum defect tail majorization              PROPOSED COMPLETE
ESBT / ESGS                                     OPEN / RH-BEARING
ESBT -> nonnegative 4 sqrt(X) packing            COMPLETE CONDITIONAL
sharp packing -> prime ramp -> RH                IMPORTED/PROPOSED COMPLETE
Riemann Hypothesis                               UNPROVEN
```
