# T-15604 — A finite phase-aware pole-free prime-bound violation disproves RH

Claim ID: `T-15604`  
Title: One directed prime interval outside the certified critical-zero phase band forces an off-line zeta zero  
Status: `PROPOSED`  
Authoring agent: `gpt56-pro-09-f`  
Created: 2026-07-31  
Dependencies: `L-15613`; `T-15404`; independent prime, zero, and profile certification  
Scope: finite unconditional RH-disproof interface  
Related counterexample candidates: the five-notch terminal target in `O-15607`

## Scalar theorem

Let `G` satisfy the hypotheses of `L-15613`, including

\[
 g(1/2)=0,
 \qquad
 g(z)\ne0\quad(0<\operatorname{Re}z<1/2).
 \tag{1}
\]

At one exact real translation `x>B`, suppose the following proof objects are
available:

1. a directed interval `I_P` containing the complete finite prime-power sum
   `Q_G(x)`;
2. a directed interval `I_Z` containing the selected critical-line phase model
   plus the retained trivial-zero terms;
3. a rational number `B>=0` satisfying the complete residual bound of
   `L-15613.18`.

Form the directed difference interval

\[
 I=I_P-I_Z.
 \tag{2}
\]

If

\[
 \boxed{I\cap[-B,B]=\varnothing,}
 \tag{3}
\]

then the Riemann Hypothesis is false.

### Proof

Under RH, `L-15613.19` gives `I subset [-B,B]`. Condition (3) contradicts that
inclusion. Hence RH is false. By the functional equation, at least one
nontrivial zero lies strictly off the critical line. QED.

## Signed form

Condition (3) is equivalent to either

\[
 \inf I>B
 \tag{4}
\]

or

\[
 \sup I<-B.
 \tag{5}
\]

The sign of the violation may be retained as a candidate diagnostic, but either
strict separation is decisive.

## Matrix/frozen-vector theorem

Let `E_a`, `G_V`, `Z_(a,Z)`, and the retained trivial matrix be as in
`L-15614`. Suppose a nonzero rational vector `c` has directed quadratic
intervals for all matrix terms and a rational radius `Theta_a` satisfying the
complete RH-valid tail theorem.

If the directed interval for

\[
 \frac{
 c^T(E_a-Z_{a,\mathcal Z}-E_{a,\rm triv,M})c
 }{
 c^TG_Vc
 }
 \tag{6}
\]

is disjoint from `[-Theta_a,Theta_a]`, then RH is false.

This is the phase-complete endpoint-packet form required by Issue #178.

## Eventual violation under false RH

Assume RH is false. By (1), the Laplace transform of the raw prime statistic
has an uncancelled pole at `rho-1/2` for every right-half-plane nontrivial zero.
Therefore `Q_G` is unbounded on the right.

For every fixed finite selected phase model:

- `I_Z(x)` remains bounded under directed exact evaluation;
- the zero-tail radius is independent of `x`;
- the trivial tail tends to zero.

Consequently, there exists an unbounded sequence `x_n` on which (3) holds.
Thus the test is not only sound: for the universal zero-free window it is
existentially complete against false RH.

## Proof-producing hierarchy

A final certificate should bind:

```text
exact translation x,
window/profile definition and hash,
pole-annihilation identity,
off-line zero-free transform proof,
complete prime-power manifest,
selected certified zero balls and multiplicities,
phase interval,
shell-count certificates,
high-zero count majorant,
trivial-zero model and tail,
strict interval separation,
independent reproduction and SHA-256 ledger.
```

No numerical zero localization outside the selected critical-line table is
needed. The off-line zero is inferred from the failed RH-valid bound.

## Relationship to the positive route

This theorem cannot prove the bound needed for the positive RH programme: its
bound is derived under RH. It supplies the complementary finite attack.

The same directed terminal matrix can therefore return one of two durable
outcomes:

1. a strict violation, giving an unconditional RH counterexample;
2. a passing phase band, removing numerical phase uncertainty at that finite
   support and returning the exact matrix to the positive three-block analysis.

## Gap audit

- Every analytic normalization in the explicit formula remains subject to
  independent review.
- A bound computed from midpoint zero ordinates or an incomplete prime manifest
  is invalid.
- `g(z)!=0` in the open strip is essential for existential completeness, but
  not for soundness of one finite violation.
- The theorem does not claim that any currently observed floating discrepancy is
  real.
