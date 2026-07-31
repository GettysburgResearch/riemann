# L-15121 — The arithmetic/canonical source defect is one polynomial differential residual

Claim ID: `L-15121`  
Status: **PROVED FINITE-DIMENSIONAL LEMMA**  
Authoring agent: `gpt56-04-f`  
Created: 2026-07-31  
Dependencies: `L-15109`, `L-15114`, `L-15120`  
Scope: analytic reduction of the final arithmetic source comparison  
Related counterexample candidates: none

## 1. Setup

Let

\[
 \Omega(s)=\prod_{i=1}^{n}(\lambda_i-s),
 \qquad
 \phi_i(s)=\frac{\Omega(s)}{\lambda_i-s},
 \qquad
 P(s)=\sum_i p_i\phi_i(s),
\]

with distinct real nodes, every `p_i!=0`, and `sum p_i=1`.  Let the arithmetic
special source be `beta_i`, and define

\[
 \boxed{
 R_0(s)=\sum_i p_i\beta_i\phi_i(s).}
 \tag{L-15121.1}
\]

For the target-pinned scalar `c`,

\[
 R_c(s)=R_0(s)-c\{sP(s)+\Omega(s)\}.
 \tag{L-15121.2}
\]

The canonical source is

\[
 g(s)=-\frac{P'(s)}{P(s)}.
\]

## 2. Exact residual polynomial

For `a,c,d in R`, define

\[
 \boxed{
 E_{a,c,d}(s)
 =R_0(s)-c\{sP(s)+\Omega(s)\}
  +aP'(s)-dP(s).}
 \tag{L-15121.3}
\]

At every node,

\[
 \boxed{
 \frac{E_{a,c,d}(\lambda_i)}{P(\lambda_i)}
 =\beta_i-c\lambda_i-a g(\lambda_i)-d.}
 \tag{L-15121.4}
\]

### Proof

The interpolation identities give

\[
 R_0(\lambda_i)=\beta_iP(\lambda_i),
\]

and

\[
 \{sP(s)+\Omega(s)\}_{s=\lambda_i}
 =\lambda_iP(\lambda_i).
\]

Finally `aP'/P=-ag`.  Dividing (L-15121.3) by the nonzero node value proves
(L-15121.4). QED.

The constant `d` is the ordinary source gauge: adding one common constant to a
special source changes no divided difference.

## 3. Exact canonical-ray equality

The following are equivalent:

1. for every node,
   
   \[
   \beta_i-c\lambda_i=a g(\lambda_i)+d;
   \]
2. the target-pinned arithmetic matrix equals the scaled canonical matrix,
   
   \[
   T_p(c)=aQ^{\rm can};
   \]
3. the polynomial identity
   
   \[
   \boxed{E_{a,c,d}(s)\equiv0}
   \tag{L-15121.5}
   \]
   
   holds.

Indeed, (1) makes all off-diagonal special entries agree, and the common target
kernel forces the diagonals.  Conditions (1) and (3) are equivalent because
`E` has degree at most `n-1` and vanishes at the `n` distinct nodes.

Thus exact canonical-ray matching is a three-parameter linear polynomial
identity, not an accidental matrix fit.

## 4. Normalized form

Put

\[
 t=1/a>0,
 \qquad
 q=c/a,
 \qquad
 e=d/a.
\]

Dividing (L-15121.3) by `a` gives

\[
 \boxed{
 \mathcal R_{t,q,e}(s)
 =tR_0(s)-q\{sP(s)+\Omega(s)\}
  +P'(s)-eP(s).}
 \tag{L-15121.6}
\]

At a node,

\[
 \frac{\mathcal R_{t,q,e}(\lambda_i)}{P(\lambda_i)}
 =t\beta_i-q\lambda_i-g(\lambda_i)-e.
 \tag{L-15121.7}
\]

The divided differences of these node values are exactly the normalized
matrix discrepancies in `L-15120`.  The constant `e` disappears from every
divided difference, while it can be chosen to reduce nodewise residuals and
conditioning.

## 5. Coefficient-space proof interface

All four polynomials

\[
 R_0,
 \qquad sP+\Omega,
 \qquad P',
 \qquad P
\]

are linear or elementary transforms of the exact target and arithmetic source.
Therefore a proof can work before root isolation or matrix assembly:

1. build directed coefficient intervals for these four polynomials;
2. solve a small rational Chebyshev or LP problem for `(t,q,e)`;
3. evaluate `mathcal R` at the nodes with directed arithmetic;
4. divide only after proving `0 notin P(lambda_i)`;
5. feed the resulting source discrepancies to `L-15120`.

The exact equality case requires only solving a rational linear system in three
unknowns and checking that every coefficient of `E` vanishes.

## 6. Differential-equation interpretation

A successful near-canonical comparison is equivalent to the first-order
polynomial differential relation

\[
 \boxed{
 P'(s)+(tR_0(s)-q\Omega(s))
 -(qs+e)P(s)\ \text{is small}.}
 \tag{L-15121.8}
\]

In the exact case,

\[
 P'(s)+(tR_0(s)-q\Omega(s))=(qs+e)P(s).
\]

This is the clean analytic target for the Weil/Hermite trace-form program.  It
asks the arithmetic interpolation multiplier `R_0` to reproduce the logarithmic
derivative of the target polynomial after one scale, one boundary slope, and
one gauge constant are removed.

## 7. Relation to residue weights

At a simple target root `r_k`, (L-15121.3) becomes

\[
 E_{a,c,d}(r_k)
 =R_c(r_k)+aP'(r_k).
\]

Hence the arithmetic residue weight

\[
 w_k(c)=-\frac{R_c(r_k)}{P'(r_k)}
\]

satisfies

\[
 \boxed{
 w_k(c)-a
 =\frac{E_{a,c,d}(r_k)}{P'(r_k)}.}
 \tag{L-15121.9}
\]

Thus the residual polynomial measures directly how far every arithmetic weight
is from the positive canonical value `a`.  If directed root isolators prove

\[
 |E(r_k)|<a|P'(r_k)|
\]

for every root, all arithmetic weights are positive and the exact scalar gate
passes.  This root-explicit test can succeed even when the row-sum relaxation of
`L-15120` is too pessimistic.

## 8. Gap audit

1. Small polynomial coefficients do not automatically imply small nodewise
   ratios when `P(lambda_i)` is tiny.
2. The differential residual is a reformulation, not a proof that it is small.
3. The arithmetic source must include the complete prime-power stream.
4. Root-explicit inequality (L-15121.9) requires directed simple-root isolators.
5. Proving a cofinal normalized residual bound remains the RH-bearing arithmetic
   theorem.