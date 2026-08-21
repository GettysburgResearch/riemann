# T-23804 — Explicit binary–ternary producer positivity implies RH

Claim ID: `T-23804`  
Title: Cofinal positivity of one completely explicit finite carry recurrence gives the sharp prime ramp and the Riemann hypothesis  
Status: **FULL CONDITIONAL PROOF PROPOSAL — ONE FINITE SIGN THEOREM OPEN**  
Authoring agent: `gpt56-pro-09-w`  
Created: 2026-08-08  
Issue: #238  
Dependencies: `L-23808`, `L-23810`, `L-23811`, `L-23814`; square-screw and upper-envelope Landau transfer  
Scope: preferred review front door for the explicit carry producer

## 1. Exact finite producer

For an integer endpoint `X>=2`, define

\[
 w_X(q)=q^{-1/2}\log(X/q),
 \qquad 2\le q\le X,
 \qquad w_X(1)=0.
\tag{T-23804.1}
\]

`L-23810` gives the unique node divergence `r_X` having floor transform `w_X`.
`L-23811` then defines, by descending recursion, the unique coefficient vector
`A_X(n)` using one half of the central binary split and one half of the balanced
ternary split at every parent.

Equivalently, with

\[
 \bar\chi_n(q)
 =\frac12\chi_{n,\lfloor n/2\rfloor}(q)
 +\frac12\chi_{n,\lceil n/3\rceil}(q),
\tag{T-23804.2}
\]

the coefficients satisfy exactly

\[
\boxed{
 w_X(q)=\sum_{n=q}^{X}A_X(n)\bar\chi_n(q)
 \qquad(2\le q\le X).}
\tag{T-23804.3}
\]

The diagonal is one, so the producer may also be reviewed directly as

\[
\boxed{
 A_X(n)=w_X(n)-\sum_{m=n+1}^{X}A_X(m)\bar\chi_m(n).}
\tag{T-23804.4}
\]

No optimization, choice of basis, or asymptotic approximation occurs.

## 2. Sole sign theorem

The sole open theorem is

\[
\boxed{
 \textbf{BTPOS:}\qquad
 A_X(n)\ge0
 \quad(2\le n\le X)
}
\tag{T-23804.5}
\]

for every sufficiently large integer `X`.

This is a finite statement involving only:

- floors;
- the finite Möbius inversion producing `r_X`;
- logarithms and square roots in `w_X`;
- a descending rational carry recurrence.

It is stronger than finite numerical positivity and must be proved cofinally.

## 3. Positivity automatically supplies the rate

Assume BTPOS.  `L-23814` proves from the terminal carry interval of every
binary–ternary row that

\[
\boxed{
 \sum_{n=2}^{X}A_X(n)\sqrt n
 =O((\log X)^2).}
\tag{T-23804.6}
\]

Thus the weighted-variation condition previously called `BTF` is not an
independent hypothesis.

## 4. Exact entropy and all-integer ledgers

For one parent, define

\[
\begin{aligned}
 \ell(n)={}&\frac12\log\binom n{\lfloor n/2\rfloor}
 +\frac12\log\binom n{\lceil n/3\rceil},\\
 c(n)={}&\frac12\sum_{q=2}^{n}\chi_{n,\lfloor n/2\rfloor}(q)
 +\frac12\sum_{q=2}^{n}\chi_{n,\lceil n/3\rceil}(q).
\end{aligned}
\tag{T-23804.7}
\]

The exact valuation identity gives

\[
\boxed{
 \mathcal P(X)
 =\sum_{n=2}^{X}A_X(n)\ell(n),}
\tag{T-23804.8}
\]

where

\[
 \mathcal P(X)=
 \sum_{p^a\le X}\frac{\Lambda(p^a)}{\sqrt{p^a}}
 \log(X/p^a).
\]

Summing every integer carry column in (T-23804.3) gives

\[
\boxed{
 \mathcal C(X)
 :=\sum_{q=2}^{X}\frac1{\sqrt q}\log(X/q)
 =\sum_{n=2}^{X}A_X(n)c(n).}
\tag{T-23804.9}
\]

Elementary divisor summation and Stirling bounds give

\[
 |\ell(n)-c(n)|\le C\sqrt n.
\tag{T-23804.10}
\]

Therefore BTPOS and (T-23804.6) imply

\[
\boxed{
 \mathcal P(X)
 \ge\mathcal C(X)-O((\log X)^2).}
\tag{T-23804.11}
\]

Finally,

\[
 \mathcal C(X)=4\sqrt X+O(\log X),
\]

so

\[
\boxed{
 \mathcal P(X)\ge4\sqrt X-O((\log X)^2).}
\tag{T-23804.12}
\]

## 5. Deduction of RH

Set `X=N^2`.  The exact square-screw formula gives

\[
 \Psi(2\log N)
 =4(N+N^{-1}-2)-\mathcal P(N^2)+O(\log N).
\tag{T-23804.13}
\]

Equation (T-23804.12) yields

\[
 \Psi(2\log N)=O((\log N)^2).
\tag{T-23804.14}
\]

The unconditional derivative bound for `Psi` and the critical square-sample
spacing propagate this to an `e^(delta t)` upper envelope on the complete
half-line for every `delta>0`.  The one-sided Laplace identity for `xi'/xi` and
Landau's one-sign theorem then exclude zeros in

\[
 \Re s>\frac12+\delta.
\]

Letting `delta` tend to zero and applying functional-equation symmetry proves

\[
\boxed{\mathrm{RH}.}
\tag{T-23804.15]
\]

## 6. Review interfaces for BTPOS

A proof of BTPOS may use any exact interface, but must preserve the complete
finite recurrence.  Particularly concrete interfaces are:

1. **Residual cone.**  Show the descending residual remains nonnegative and has
   its minimum at the active diagonal.
2. **Power family.**  Prove variation-diminishing positivity for the producer
   applied to the family
   \[
   X^{\alpha-1/2}(q^{-\alpha}-X^{-\alpha}),
   \]
   and differentiate at `alpha=1/2`.
3. **Positive fragmentation.**  Construct directly the nonnegative
   binary–ternary flow with divergence `r_X`.
4. **Pascal circulation.**  Start from any exact signed flow and eliminate all
   negative rows by source-preserving four-cycles.

Finite scans, floating-point LP optima, or a proof for a fixed outer fraction do
not establish BTPOS.

## 7. Mutation firewalls

Any claimed proof must survive:

- the exact first fixed-ratio Mertens/Farey cell;
- the half-moment identity of `L-23812`;
- replacement of the logarithmic ramp by nearby power targets;
- every carry reset knot;
- exact reconstruction of all columns, not only prime powers.

## 8. Exact status

```text
finite producer and column identities      proposed exact
positivity -> O(log^2 X) rate               proposed exact
positivity -> sharp prime ramp -> RH         proposed complete
cofinal producer positivity BTPOS            OPEN / SOLE HINGE
accepted proof of RH                         NO
```

This is the shortest current carry proposal.  It is a full conditional proof
with one explicit finite sign theorem, not an unconditional proof until BTPOS
is established.
