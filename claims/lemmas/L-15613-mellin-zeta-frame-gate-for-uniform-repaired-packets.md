# L-15613 — Mellin–zeta frame gate for uniformly controlled repaired packets

Claim ID: `L-15613`  
Title: A uniformly controlled growing radical packet requires a weighted Mellin frame bound, not source-tail decay alone  
Status: `PROPOSED`  
Authoring agent: `gpt56-08`  
Created: 2026-07-31  
Dependencies: the Connes–Consani `E`-range radical/Mellin factorization; Mellin Plancherel; `L-14313`; `L-15304`; `L-15611`  
Scope: proof-grade growing-rank source packets for the cofinal capacity/saturation route  
Related counterexample candidates: none

## Purpose

The recent stack supplies:

1. exact finite-codimension source repair;
2. source packets whose **unnormalized** exterior tails are small;
3. dimension-free Schur bounds once the normalized whole-packet tail-synthesis
   norm is small.

There remains a normalization gate.  A source packet can have tiny ordinary
source tails while its arithmetic `E`-image has an arbitrarily small Gram
value.  Dividing by that Gram can destroy the tail estimate.  This lemma gives
the exact required frame inequality and identifies its arithmetic content.

## Arithmetic Mellin Gram

For an admissible even source `f`, write

\[
 \Phi_f(t)
 =\int_0^\infty f(x)x^{-1/2-it}\,dx,
 \tag{L-15613.1}
\]

and

\[
 E(f)(u)=u^{1/2}\sum_{n\ge1}f(nu).
 \tag{L-15613.2}
\]

In the declared normalization, Mellin factorization gives

\[
 \mathcal M E(f)(t)
 =\zeta\!\left(\frac12+it\right)\Phi_f(t).
 \tag{L-15613.3}
\]

Hence Mellin Plancherel gives the exact global Gram identity

\[
 \boxed{
 \langle E(f),E(g)\rangle_{L^2(d^*u)}
 =\frac1{2\pi}\int_{\mathbb R}
 |\zeta(1/2+it)|^2
 \Phi_f(t)\overline{\Phi_g(t)}\,dt.}
 \tag{L-15613.4}
\]

Let `C_a` be a finite-dimensional coefficient Hilbert space and let

\[
 \mathcal R_a:C_a\longrightarrow\mathcal S_0^{\rm ev}
 \tag{L-15613.5}
\]

be an exact source-repair map, for example the external graph repair of
`L-15611`.  Define the weighted Mellin frame floor

\[
 \boxed{
 g_a^2
 =\inf_{\|c\|=1}
 \frac1{2\pi}\int_{\mathbb R}
 |\zeta(1/2+it)|^2
 |\Phi_{\mathcal R_ac}(t)|^2dt.}
 \tag{L-15613.6}
\]

This is exactly the smallest global `E`-Gram eigenvalue in the chosen
coefficient norm.

## Localization and normalized tail synthesis

Let `P_a` be multiplication by the indicator, or an admissible smooth cutoff,
of the localized multiplicative interval.  Put

\[
 J_a=P_aE\mathcal R_a,
 \qquad
 T_a=(I-P_a)E\mathcal R_a.
 \tag{L-15613.7}
\]

Assume a tail norm `X_a` dominates the ordinary `L2` tail norm and that

\[
 \|T_a\|_{C_a\to X_a}\le\epsilon_a.
 \tag{L-15613.8}
\]

Then for every `c`,

\[
 \|J_ac\|_2^2
 =\|E\mathcal R_ac\|_2^2-\|T_ac\|_2^2
 \ge(g_a^2-\epsilon_a^2)\|c\|^2.
 \tag{L-15613.9}
\]

Consequently, if

\[
 \epsilon_a<g_a,
 \tag{L-15613.10}
\]

then `J_a` is injective, the localized packet has the full repaired rank, and
the tail map normalized by the localized packet satisfies

\[
 \boxed{
 \left\|T_aJ_a^{-1}\right\|_{
 J_a(C_a)\to X_a}
 \le
 \frac{\epsilon_a}{\sqrt{g_a^2-\epsilon_a^2}}.}
 \tag{L-15613.11}
\]

### Proof

The orthogonal local/tail decomposition proves (L-15613.9).  Its positive lower
bound gives injectivity.  For `u=J_ac`,

\[
 \|c\|
 \le\frac{\|u\|_2}{\sqrt{g_a^2-\epsilon_a^2}},
\]

and (L-15613.8) gives (L-15613.11).  QED.

## Dimension-free corrected-low-block consequence

Suppose the tail/form continuity estimates of `L-14313` hold:

\[
 |Q(x,y)|\le C_{tt,a}\|x\|_{X_a}\|y\|_{X_a},
 \tag{L-15613.12}
\]

\[
 \sup_{\langle M_ae,e\rangle\le1}|Q(x,e)|
 \le C_{te,a}\|x\|_{X_a},
 \tag{L-15613.13}
\]

and the complement moat is `h_a>0`.  Then the corrected low block on
`J_a(C_a)` satisfies

\[
 \boxed{
 B_a-h_a^{-1}R_a^*M_a^{-1}R_a
 \succeq
 -\frac{\epsilon_a^2}{g_a^2-\epsilon_a^2}
 \left(C_{tt,a}+\frac{C_{te,a}^2}{h_a}\right)I.}
 \tag{L-15613.14}
\]

Thus a proof-grade uniformly controlled repaired packet follows from

\[
 \boxed{
 \frac{\epsilon_a^2}{g_a^2}
 \left(C_{tt,a}+\frac{C_{te,a}^2}{h_a}\right)
 \longrightarrow0,}
 \tag{L-15613.15}
\]

with `epsilon_a/g_a -> 0`.

The estimate contains no packet-dimension factor.  All growing-rank difficulty
is concentrated in the weighted frame floor `g_a` and the joint tail operator
norm `epsilon_a`.

## Why ordinary Hermite/prolate concentration is insufficient

A source-space concentration estimate can prove

\[
 \|(I-P_a)f\|\ll1
\]

uniformly over a large source packet.  It does not imply a lower bound for
(L-15613.6), because the arithmetic map inserts multiplication by

\[
 \zeta(1/2+it)
\]

in Mellin space.  This multiplier vanishes at every critical-line zero.
Accordingly, a sequence of source transforms concentrating in shrinking
neighborhoods of certified zeros can have unit source norm but weighted Gram
value tending to zero.

This is the Gram-side version of `L-15304`: exact radical transforms vanish at
actual zeta zeros, so evaluation-visible packet directions cannot be absorbed
by a small-tail radical frame merely from a dimension or ordinary
concentration estimate.

The statement does **not** show that a particular Hermite packet has bad Gram.
It shows that a proof must certify one of:

1. a directed finite lower Gram bound from (L-15613.4);
2. an analytic weighted-frame theorem for the chosen growing packet;
3. an evaluation near-kernel/visible split, with only the near-kernel assigned
   to the radical packet.

## Constraint-aware finite certificate

Choose an exact basis `f_1,...,f_d` of the repaired source packet.  The global
arithmetic Gram is

\[
 G^E_{ij}
 =\frac1{2\pi}\int
 |\zeta(1/2+it)|^2\Phi_{f_i}(t)
 \overline{\Phi_{f_j}(t)}dt.
 \tag{L-15613.16}
\]

A proof packet may supply directed rational matrices

\[
 G^E\succeq g^2H,
 \qquad
 T^*T\preceq\epsilon^2H,
 \tag{L-15613.17}
\]

for one exact coefficient Gram `H`.  Exact rational `LDL*` then proves the
localized lower Gram and the normalized tail bound.  This is invariant under
all changes of packet basis.

## Interaction with the weighted-deficit scalar route

`L-15612` converts the verified low compression of a `d`-dimensional packet
into automatic weighted-deficit capture.  L-15613 supplies the missing
normalization step needed to turn source-tail estimates into that actual low
compression and complete residual packet.

The remaining two independent asymptotic gates are therefore:

1. the weighted Mellin frame/tail ratio (L-15613.15);
2. the arithmetic scalar deficit moat
   \[
   \operatorname{Tr}D_a-d_a(G_a-\alpha_a)
   \le G_a-\Gamma_a.
   \]

Neither follows from packet rank alone.

## Proof boundary

- The Hilbert-space estimates are exact.
- Equation (L-15613.4) inherits the exact Mellin and Fourier conventions of the
  Connes--Consani source theorem and requires independent normalization review.
- The source packet must lie in the exact domain of the arithmetic `E` map.
- A midpoint Gram eigenvalue is not a proof of `g_a>0`.
- Classical mean-value estimates for `|zeta|` do not automatically give a
  smallest-eigenvalue bound for an arbitrary growing packet.
- This lemma does not prove a cofinal weighted frame for the zeta packet or RH.
