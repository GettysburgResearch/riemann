# T-17001 — Cofinal Schur-defect criterion is equivalent to RH

Claim ID: `T-17001`  
Title: Once the complete complement is positive, a vanishing finite Schur defect is exactly the remaining Riemann-hypothesis content  
Status: `PROPOSED`  
Authoring agent: `gpt56-02-n`  
Created: 2026-07-31  
Dependencies: `L-14201`; `T-14302`; `L-14318`; `L-17001`; Suzuki's localized Weil positivity equivalence  
Scope: every unbounded support sequence with a complete positive complement  
Related counterexample candidates: none

## Setup

Let `A_a` be the exact closed localized Weil operator at support `a`, and let

\[
 \mu(a)=\inf\operatorname{spec}(A_a).
 \tag{T-17001.1}
\]

Use the established support monotonicity

\[
 a<b\quad\Longrightarrow\quad\mu(b)\le\mu(a).
 \tag{T-17001.2}
\]

Let `a_j->infinity`. At every level choose a finite proof-grade packet `U_j`
and its orthogonal complement `E_j`, with block form

\[
 A_{a_j}=\begin{pmatrix}B_j&C_j^*\\C_j&D_j\end{pmatrix},
 \qquad
 D_j\succeq\gamma_j I,
 \qquad \gamma_j>0.
 \tag{T-17001.3}
\]

Define the exact finite Schur defect

\[
 S_j=B_j-C_j^*D_j^{-1}C_j.
 \tag{T-17001.4}
\]

The positive complement can always be constructed at a fixed support from the
top spectrum of the weighted symbol-deficit operator, as in `L-14318` and
`L-17001`.

## Equivalence theorem

The following are equivalent.

1. The Riemann Hypothesis is true.
2. For every such unbounded complete-complement sequence,
   \[
   S_j\succeq0\quad\text{for every }j.
   \tag{T-17001.5}
   \]
3. For one such unbounded sequence there exist `epsilon_j>=0` with
   \[
   \lambda_{\min}(S_j)\ge-\varepsilon_j,
   \qquad
   \varepsilon_j\longrightarrow0.
   \tag{T-17001.6}
   \]
4. The block-Schur lower bounds satisfy
   \[
   F_j\ge-\varepsilon_j,
   \qquad
   \varepsilon_j\longrightarrow0
   \tag{T-17001.7}
   \]
   along one unbounded sequence.

## Proof

### RH implies every Schur defect is nonnegative

Under RH, the localized Weil criterion gives

\[
 A_a\succeq0
 \qquad\text{for every }a>0.
 \tag{T-17001.8}
\]

For any `u in U_j`, choose `e=-D_j^{-1}C_ju`. Then the exact square completion
of `L-17001` gives

\[
 \langle A_{a_j}(u,e),(u,e)\rangle
 =\langle S_ju,u\rangle.
 \tag{T-17001.9}
\]

The left side is nonnegative, so `S_j>=0`. This proves `1=>2`, and `2=>3` is
immediate with `epsilon_j=0`.

### A vanishing Schur defect implies RH

Assume (T-17001.6). By `L-17001`,

\[
 A_{a_j}\succeq-\varepsilon_j I,
 \tag{T-17001.10}
\]

so

\[
 \mu(a_j)\ge-\varepsilon_j.
 \tag{T-17001.11}
\]

Fix any finite support `a`. For all sufficiently large `j`, `a_j>=a`, and
support monotonicity gives

\[
 \mu(a)\ge\mu(a_j)\ge-\varepsilon_j.
 \tag{T-17001.12}
\]

Letting `j->infinity` proves `mu(a)>=0`. Since `a` was arbitrary, localized
Weil positivity holds at every support, and the Weil criterion gives RH. Thus
`3=>1`.

The equivalence with (T-17001.7) is the cofinal lower-envelope theorem
`T-14302`, or follows directly from the same monotonicity argument.

### Robust contrapositive

If RH is false, choose a finite support `a_*` with

\[
 \mu(a_*)=-c<0.
 \tag{T-17001.13}
\]

For all large `j`, monotonicity gives `mu(a_j)<=-c`. The negative-moat transfer
of `L-17001` then gives

\[
 \boxed{\lambda_{\min}(S_j)\le-c}
 \tag{T-17001.14}
\]

cofinally. Therefore the failure is not an unresolved `o(1)` issue: false RH
creates a fixed negative moat in every exact fully corrected low packet once
the complete complement is positive.

QED.

## Resolution of the two requested limits

The complement statement

\[
 \liminf_j\Gamma_j\ge0
 \tag{T-17001.15}
\]

is constructible without RH: at each level include every weighted-deficit mode
above the chosen threshold. The packet is finite because the deficit operator
is trace class.

The second statement

\[
 \liminf_j\lambda_{\min}(S_j)\ge0
 \tag{T-17001.16}
\]

is not an independent tail lemma. By the theorem, it is equivalent to RH after
the complete complement gate. This is the exact logical boundary that any
claimed direct proof must cross.

`L-17002` supplies a noncircular sufficient route to (T-17001.16): prove a
positive corrected visible floor and show that the squared radical-visible
cross map is little-o of that floor. PR #168 supplies a certified-zero S-lemma
and stable separated-zero frames for nominating that visible floor. What remains
zeta-specific is a cofinal lower bound for the residual form after the positive
certified-zero channels are extracted.

## Zero-orbit meaning

Under the polarized zero formula, `L-17003` decomposes the finite zero quotient
into positive critical-line blocks and hyperbolic off-line blocks. Equation
(T-17001.14) is therefore the operator-level shadow of one of those hyperbolic
orbits. Radical tails and symbol complements can move the representation of the
negative direction, but cannot remove its inertia.

## Gap audit

- This theorem proves an equivalence and a robust contrapositive, not RH.
- The packet must have a complete strictly positive complement; a finite sampled
  symbol packet is insufficient.
- The support monotonicity and localized positivity equivalence must be audited
  in the exact Suzuki normalization.
- A numerical Schur eigenvalue tending upward is not a cofinal proof.
- The theorem prevents circular arguments that silently assume the visible
  finite block nonnegative after all analytic tails have been controlled.
