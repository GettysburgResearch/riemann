# T-8301 — Background-stable whole-matrix first-cell certification

Claim ID: T-8301  
Title: Endpoint Green pressure plus one operator moat decides a rank-two first-cell event  
Status: PROPOSED  
Authoring agent: `gpt56-05-i`  
Reviewing agents: none  
Created: 2026-07-25  
Last updated: 2026-07-25  
Dependencies: L-8301; an operator-norm bound for the smooth background  
Scope: rigorous promotion or exclusion of a D-0801 first-cell whole-matrix crossing  
Related counterexample candidates: none

## Statement

Let `H` be positive-definite Hermitian with

\[
 H\succeq\mu I,\qquad \mu>0.
\]

Let `C_zeta` and `lambda_+` be as in L-8301. Let `B` be Hermitian with

\[
 \|B\|_2\le\beta.
\]

For `tau>=0`, define

\[
 Q=H-\tau C_\zeta+B.
\]

### Positive certificate

If

\[
 \boxed{\mu(1-\tau\lambda_+)>\beta,}
\]

then

\[
 \boxed{Q\succ0.}
\]

### Negative certificate

If

\[
 \boxed{\mu(\tau\lambda_+-1)>\beta,}
\]

then `Q` has a strictly negative quadratic direction and is not positive
semidefinite.

### Unresolved band

Only

\[
 \left|1-\tau\lambda_+\right|\le\frac\beta\mu
\]

requires a more detailed calculation. The dimensionless robust pressure
`tau lambda_+-1` is compared against one relative moat `beta/mu`.

## First deposition cell

In the D-0801 first cell of `q=p^alpha`, let

\[
 \tau=\tau_q(\varepsilon)
 =\frac{K}{2\pi\alpha\sqrt q}
   \frac{\varepsilon}{1+\varepsilon/\log q}
\]

and decompose the exact path as

\[
 Q(L_0+\varepsilon)
 =H_0-\tau_q(\varepsilon)C_{\zeta_q}+B(\varepsilon),
\]

where `H_0` is the exact left-threshold matrix and `B` contains every other
change: old-prime hat motion, leading-scalar motion, exact archimedean motion,
pole motion, and any separately admitted correction in the chosen
normalization.

Suppose

\[
 H_0\succeq\mu I
\]

and

\[
 \|B(\varepsilon)\|_2\le\beta(\varepsilon).
\]

Then:

1. if
   \[
   \mu(1-\tau_q(\varepsilon)\lambda_{+,q})
   >\beta(\varepsilon)
   \]
   throughout the cell, the exact matrix remains positive there;

2. if at one exact or rigorously enclosed point
   \[
   \mu(\tau_q(\varepsilon)\lambda_{+,q}-1)
   >\beta(\varepsilon),
   \]
   then the exact matrix has a negative direction there.

The second conclusion, combined with independently reviewed D-0801
admissibility and Guinand--Weil normalization, would give a finite RH-disproof
witness.

## Proof

L-8301 identifies `lambda_+` as the maximum generalized Rayleigh quotient:

\[
 x^*C_\zeta x\le\lambda_+x^*Hx
\]

for every `x`. Therefore

\[
 x^*(H-\tau C_\zeta)x
 \ge(1-\tau\lambda_+)x^*Hx.
\]

Under the positive hypothesis, `1-tau lambda_+>0`, so

\[
 x^*(H-\tau C_\zeta)x
 \ge\mu(1-\tau\lambda_+)\|x\|_2^2.
\]

Also

\[
 x^*Bx\ge-\beta\|x\|_2^2.
\]

Adding gives

\[
 x^*Qx
 \ge[\mu(1-\tau\lambda_+)-\beta]\|x\|_2^2>0.
\]

For the negative certificate, choose a generalized eigenvector `x_+` satisfying

\[
 C_\zeta x_+=\lambda_+Hx_+.
\]

Then

\[
 x_+^*(H-\tau C_\zeta)x_+
 =(1-\tau\lambda_+)x_+^*Hx_+.
\]

Now the coefficient is negative. Since `H\succeq mu I`,

\[
 (1-\tau\lambda_+)x_+^*Hx_+
 \le-\mu(\tau\lambda_+-1)\|x_+\|_2^2.
\]

Finally

\[
 x_+^*Bx_+\le\beta\|x_+\|_2^2,
\]

so

\[
 x_+^*Qx_+
 \le[\beta-\mu(\tau\lambda_+-1)]\|x_+\|_2^2<0.
\]

The first-cell statements are substitutions. ∎

## Exact negative-vector extraction

A proof-producing implementation need not trust an interval eigensolver. Let
`y in C^2` be an exact or dyadically rounded eigenvector of `J_zeta G` for the
positive eigenvalue, and put

\[
 x=H^{-1}Uy.
\]

For the exact eigenvector,

\[
 C_\zeta x=\lambda_+Hx.
\]

In computation, two residual-controlled endpoint solves from L-8302 and a
dyadic `y` give an explicit full-space vector. Its exact quadratic interval can
then be checked directly. T-8301 is both a screening theorem and a source of a
compact negative nomination.

## Motivation

L-4204 and L-5501 rank thresholds using the endpoint product of one frozen
vector. That can miss a crossing caused by rotation into another endpoint-rich
direction. L-8301 computes the exact best direction, while T-8301 pays for all
remaining first-cell motion through one operator moat.

This splits the search into three cheap objects:

1. a positive floor `mu` for the left-threshold matrix;
2. a `2 x 2` endpoint Green enclosure;
3. a smooth-background radius `beta`.

Only cells whose robust pressure interval meets zero need a full directed replay.

## Analytic domain audit

The abstract theorem is finite-dimensional. In D-0801 every term assigned to
`B` must be Hermitian in the same normalized basis.

## Dependency audit

- L-8301 supplies the exact generalized eigenvalue.
- L-8302 is one way to certify it.
- A separate claim must bound `B(epsilon)` for the chosen cutoff path.
- The RH implication remains conditional on the repository's D-0801 theorem
  stack.

## Gap audit

1. The same normalization must be used for `H`, `C_zeta`, `B`, `mu`, and
   `beta`.
2. `beta` is an operator-norm bound, not a fixed-vector bound.
3. The left-threshold matrix must be rigorously positive; discovery eigenvalues
   do not supply `mu`.
4. Use the lower pressure endpoint for a negative certificate and the upper
   endpoint for a positive certificate.
5. Equality or overlap with the unresolved band authorizes no sign claim.
6. A negative D-0801 matrix is not an unconditional RH disproof until the
   admissibility and explicit-formula gates are independently established.

## Adversarial tests

- A diagonal background has a smallest eigenvector with zero endpoint mass. The
  positive certificate holds at `tau=2/25`, while the negative certificate
  holds at `tau=3/25`.
- Add `+beta I` in the negative case and `-beta I` in the positive case to test
  the sharp inequality directions.
- Set the moat equal to the boundary and require `UNRESOLVED`.
- Use a complex phase and correlated Green matrix to audit `r`.

## Remaining uncertainty

No mathematical gap is known. The production bottleneck is obtaining complete
lag boxes or another rigorous positive background certificate from which `mu`
and the endpoint solves can be reconstructed.

## Suggested next attack

After the first complete `K=1024` lag-box pass, certify the recovered baseline
matrix positive, compute the two endpoint Green columns, and scan adjacent
thresholds by T-8301. This tests the entire matrix path, not merely the recovered
vector already excluded by PR #65.
