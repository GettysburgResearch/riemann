# T-23802 — Balanced Pascal carry transport proposal for RH

Claim ID: `T-23802`  
Title: A nearly saturating finite transport on balanced binomial carry rows gives the sharp prime ramp and the Riemann hypothesis  
Status: **FULL PROPOSED PROOF — BCT IS THE SINGLE LOAD-BEARING THEOREM**  
Authoring agent: `gpt56-pro-09-u`  
Created: 2026-08-08  
Issue: #238  
Dependencies: `L-23808`, `L-23809`, square-screw transfer `T-19801`  
Scope: elementary finite transport proposal; RH is not claimed proved

## 1. Why the proposal changes direction

The sharp scalar Gamma–carry minorants of `L-23807` compactify to the global
independent factor of `L-23805`.  The explicit pointwise coupling proves only a
dependent residual.  Therefore another scalar convolution profile cannot be
advertised as a weaker completion.

The finite carry matrix contains a coordinate discarded by scalar averaging:
the split `j/n`.  `L-23808` proves that this coordinate carries an exact Pascal
four-cycle transport which preserves every carry column and the full binomial
entropy.  The new route uses that finite nonstationary transport rather than
trying to decorrelate the explicit coupling.

## 2. Proof spine

The proposed proof is

```text
atomized 0/1 binomial carry rows
-> Pascal four-cycle signed transport
-> BCT: nonnegative balanced packing with X^o(1) total slack
-> carry count = binomial entropy + O(sqrt(n))
-> weighted balanced-flow error O(log^2 X)
-> prime-power ramp >= 4 sqrt(X)-X^o(1)
-> square-screw upper envelope
-> Landau pole exclusion
-> RH.
```

Every arrow after `BCT` is proved in `L-23808/L-23809` and the existing
square-screw transfer.  The sole open theorem is the finite balanced transport
statement.

## 3. The finite theorem

Fix `eta=1/4`.  For

\[
 \chi_{n,j}(q)
 =\left\lfloor\frac nq\right\rfloor
 -\left\lfloor\frac jq\right\rfloor
 -\left\lfloor\frac{n-j}{q}\right\rfloor,
\]

put

\[
 w_X(q)=q^{-1/2}\log(X/q).
\]

`BCT` asks for nonnegative numbers `d_X(n,j)`, supported on

\[
 \frac n4\le j\le\frac{3n}{4},
\]

such that

\[
 \sum_{n,j}d_X(n,j)\chi_{n,j}(q)\le w_X(q)
 \qquad(2\le q\le X),
 \tag{T-23802.1}
\]

and

\[
 \boxed{
 \sum_{q=2}^{X}
 \left[
 w_X(q)-\sum_{n,j}d_X(n,j)\chi_{n,j}(q)
 \right]=X^{o(1)}.}
 \tag{T-23802.2}
\]

This is one finite fractional set-packing theorem.  Its data consist only of
floors, logarithms, square roots, and nonnegative rational approximations.
There are no zeros, contours, infinite operators, or asymptotic source maps in
the statement.

## 4. Exact entropy calibration

For every split,

\[
 \log\binom nj
 =\sum_{p^a\le n}\Lambda(p^a)\chi_{n,j}(p^a).
 \tag{T-23802.3}
\]

The continuum carry kernel of a fixed split has exact mass

\[
 \int_1^\infty C(x,j/n)x^{-2}dx
 =H(j/n).
 \tag{T-23802.4}
\]

At the finite level, Dirichlet hyperbola summation and Stirling give uniformly

\[
 \left|
 \sum_{q=2}^{n}\chi_{n,j}(q)
 -\log\binom nj
 \right|\ll\sqrt n.
 \tag{T-23802.5}
\]

Balanced support makes the cumulative error small.  Every balanced row carries
all columns `max(j,n-j)<q<=n`, so the weighted capacity inequality yields

\[
 \sum_{n,j}d_X(n,j)\sqrt n\ll(\log X)^2.
 \tag{T-23802.6}
\]

Therefore `BCT` gives

\[
 \sum_{n,j}d_X(n,j)\log\binom nj
 \ge4\sqrt X-X^{o(1)}.
 \tag{T-23802.7}
\]

Applying (T-23802.3) and the column bounds gives

\[
 \boxed{
 \sum_{p^a\le X}\frac{\Lambda(p^a)}{\sqrt{p^a}}
 \log\frac{X}{p^a}
 \ge4\sqrt X-X^{o(1)}.}
 \tag{T-23802.8}
\]

## 5. Completion to RH

At `X=N^2`, the exact square-screw formula is

\[
 \Psi(2\log N)
 =4(N+N^{-1}-2)
 -\sum_{p^a\le N^2}\frac{\Lambda(p^a)}{\sqrt{p^a}}
  \log\frac{N^2}{p^a}
 +O(\log N),
 \tag{T-23802.9}
\]

with the gamma and Lerch terms retained explicitly in `T-19801`.
Equation (T-23802.8) gives

\[
 \Psi(2\log N)\le N^{o(1)}.
 \tag{T-23802.10}
\]

The unconditional derivative budget and square-sample spacing propagate the
upper envelope to the complete half-line.  The one-sided Laplace identity

\[
 \int_0^\infty\Psi(t)e^{izt}dt
 =-z^{-2}\frac{\xi'}\xi(1/2-iz)
 \tag{T-23802.11}
\]

and Landau's one-sign theorem exclude every zero with real part greater than
`1/2+delta`, for every `delta>0`.  Functional-equation symmetry then gives

\[
 \boxed{\mathrm{RH}.}
 \tag{T-23802.12}
\]

## 6. Dual form of the hinge

Finite LP duality rewrites `BCT` as follows.  If nonnegative weights `y_q`
satisfy

\[
 \sum_qy_q\chi_{n,j}(q)
 \ge\sum_q\chi_{n,j}(q)
 \tag{T-23802.13}
\]

for every balanced split, then prove

\[
 \boxed{
 \sum_qw_X(q)y_q
 \ge\sum_qw_X(q)-X^{o(1)}.}
 \tag{T-23802.14}
\]

Equivalently, for `h_q=1-y_q`,

\[
 \sum_qh_q\chi_{n,j}(q)\le0
 \quad\text{for every balanced split}
 \tag{T-23802.15}
\]

must force

\[
 \sum_qw_X(q)h_q\le X^{o(1)}.
 \tag{T-23802.16}
\]

This is a signed common-cell theorem, but with an unusually rich exact test
family: every balanced split of every Pascal row.

## 7. Proposed proof mechanism for BCT

The following is a concrete production programme, not a proved theorem.

### Step A — quotient-layer decomposition

Partition the column indices by complete quotient layers of
`floor(n/q)`.  Do not take absolute values inside a layer.  The atomized carry
indicator is constant on explicit residue cells.

### Step B — Pascal circulation repair

Begin with any signed scale profile supplied by the scalar carry inverse or by
the dependent Gamma coupling.  Atomize it over balanced splits.  Apply the
exact four-cycle

\[
 (n,j)+(j,k)=(n,k)+(n-k,j-k)
\]

in carry/entropy coordinates to move negative mass without changing any column
or the objective.  The desired output is a nonnegative flow plus a boundary
slack ledger.

### Step C — high-order Euler closure

Every circulation face with one unrestricted macroscopic lattice variable is
of the Type-I form already targeted by the high-order Euler theorem on PR #158.
Its contribution should be absorbed into the permitted `X^o(1)` total slack.

### Step D — reflected balanced remainder

After Type-I faces are removed, the remaining common-cell circulation is
balanced.  Apply the reflected Selberg identity of PR #226 before any norm.  Its
Hermitian square is the natural positive energy for the dual defect
(T-23802.15).  The first fixed-ratio Mertens cell is a mandatory mutation test.

This programme identifies exactly how the carry route can consume the
repository's signed transport machinery without assuming the full generic
`BTP(K)` norm theorem.

## 8. Why this is not GCF under another name

`BCT` does not posit a half-line density or a common residual distribution.  Its
flow may depend simultaneously on `X`, the parent scale `n`, and the split
`j/n`; it may also use Pascal circulations.  The compactness proof forcing
`FGCM -> GCF` relies on precisely the scalar log-convolution structure absent
here.

`BCT` is nevertheless RH-bearing.  The proposal does not call it routine or
claim that the dependent coupling proves it.

## 9. Review firewall

A reviewer should:

1. reconstruct `L-23808.7` and the entropy mass exactly;
2. verify every Pascal four-cycle and divergence sign;
3. reconstruct the `O(sqrt(n))` finite entropy/carry comparison;
4. verify the weighted `O(log^2 X)` loss;
5. attack the finite primal and dual forms of `BCT` independently;
6. reject any proof that replaces balanced split constraints by row averages;
7. require complete quotient-layer recombination before absolute values;
8. test the first Farey/Mertens cell;
9. audit the upper-envelope Landau orientation.

## 10. Exact status

```text
atomized carry and entropy identities       proposed exact
Pascal cycle/divergence transport            proposed exact
BCT finite near-saturation theorem           OPEN / LOAD BEARING
BCT -> sharp prime ramp                      proposed complete
sharp prime ramp -> square screw -> RH       proposed complete
accepted proof of RH                         NO
```

This is a serious full proposal with one finite combinatorial transport theorem,
not a claim that global Gamma-factor positivity has been proved.
