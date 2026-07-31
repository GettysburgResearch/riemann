# L-14313 — Dimension-free Schur bound from a whole-packet radical tail map

Claim ID: `L-14313`  
Title: Exact radical frames reduce a growing corrected low matrix to one tail-synthesis operator norm  
Status: `PROPOSED`  
Authoring agent: `gpt56-08`  
Created: 2026-07-31  
Dependencies: `L-14308`, `L-14309`; elementary operator duality  
Scope: complete control of support-dependent low packets by exact global Weil-radical extensions  
Related counterexample candidates: none

## Purpose

`L-14312` shows that fixed-column decay cannot control a growing matrix. This
lemma supplies a stronger, dimension-free mechanism tailored to the radical
construction: extend the **entire** low packet by global radical vectors and
control the operator norm of their joint discarded-tail map.

The resulting bound has no factor `dim(S_j)`.

## Abstract setup

Let `Q` be a Hermitian form. For one level, let

- `C` be a finite-dimensional coefficient Hilbert space;
- `U:C->H_loc` be an isometry onto the declared low space `S`;
- `V:C->X_tail` be a linear tail-synthesis map;
- for every `c in C`,
  \[
    r(c)=Uc+Vc
  \]
  belong to the radical of `Q`.

Let `E=S^perp` be the complete complement. Let `M` be a positive metric on
`E`, and suppose

\[
 C_E-\gamma I\succeq hM,
 \qquad h>0,
 \tag{L-14313.1}
\]

in the notation of `L-14308`.

Define the low and cross blocks by

\[
 \langle Bc,d\rangle=Q(Uc,Ud),
 \tag{L-14313.2}
\]

and

\[
 \langle Rc,e\rangle=Q(Uc,e),
 \qquad e\in E.
 \tag{L-14313.3}
\]

Assume there are finite numbers `alpha,beta>=0` such that

\[
 |Q(Vc,Vd)|\le\alpha\|c\|\|d\|,
 \tag{L-14313.4}
\]

and

\[
 \sup_{\langle Me,e\rangle\le1}|Q(Vc,e)|
 \le\beta\|c\|.
 \tag{L-14313.5}
\]

## Main theorem

Then

\[
 \boxed{-\alpha I_C\preceq B\preceq\alpha I_C,}
 \tag{L-14313.6}
\]

\[
 \boxed{R^*M^{-1}R\preceq\beta^2I_C,}
 \tag{L-14313.7}
\]

and therefore

\[
 \boxed{
 B-h^{-1}R^*M^{-1}R
 \succeq
 -\left(\alpha+\frac{\beta^2}{h}\right)I_C.}
 \tag{L-14313.8}
\]

The estimate is independent of `dim(C)`.

### Proof

Since `r(c)` is radical,

\[
 Q(Uc,Ud)=-Q(Vc,Ud).
 \tag{L-14313.9}
\]

Using the radical identity with `r(d)` tested against `Vc` and Hermitian
symmetry gives

\[
 Q(Vc,Ud)=-Q(Vc,Vd).
 \tag{L-14313.10}
\]

Hence

\[
 \boxed{Q(Uc,Ud)=Q(Vc,Vd).}
 \tag{L-14313.11}
\]

Equation (L-14313.4) now proves (L-14313.6).

For `e in E`, radicality gives

\[
 Q(Uc,e)=-Q(Vc,e).
 \tag{L-14313.12}
\]

Thus the `M`-dual norm of `Rc` is at most `beta||c||`. By the Riesz
representation in the `M` geometry,

\[
 \langle R^*M^{-1}Rc,c\rangle
 =\|Rc\|_{M^{-1}}^2
 \le\beta^2\|c\|^2,
\]

which proves (L-14313.7). Combining the two bounds proves
(L-14313.8). QED.

## Continuity corollary

Suppose a tail norm `||.||_X` satisfies

\[
 |Q(x,y)|\le C_{tt}\|x\|_X\|y\|_X
 \qquad(x,y\text{ in the tail class}),
 \tag{L-14313.13}
\]

and

\[
 \sup_{\langle Me,e\rangle\le1}|Q(x,e)|
 \le C_{te}\|x\|_X.
 \tag{L-14313.14}
\]

If

\[
 \boxed{\|V\|_{C\to X}\le\delta,}
 \tag{L-14313.15}
\]

then one may take

\[
 \alpha=C_{tt}\delta^2,
 \qquad
 \beta=C_{te}\delta,
\]

and

\[
 \boxed{
 B-h^{-1}R^*M^{-1}R
 \succeq
 -\delta^2
 \left(C_{tt}+\frac{C_{te}^2}{h}\right)I.}
 \tag{L-14313.16}
\]

Therefore a cofinal sequence is closed whenever

\[
 C_{tt,j}\delta_j^2\longrightarrow0,
 \qquad
 \frac{C_{te,j}^2\delta_j^2}{h_j}\longrightarrow0.
 \tag{L-14313.17}
\]

This is the correct whole-packet version of the scalar ratio in `T-14302`.

## Approximate-frame adapter

Often exact radical local parts span a space `S_rad` that is merely close to
the desired generalized-prolate packet `S_low`. Let `Pi_rad,Pi_low` be their
orthogonal projections and suppose

\[
 \|\Pi_{rad}-\Pi_{low}\|\le\varepsilon<1.
 \tag{L-14313.18}
\]

Then the projection from `S_rad` to `S_low` is invertible with condition number
at most

\[
 \frac{1+\varepsilon}{1-\varepsilon}.
\]

Transporting the exact radical frame to `S_low` amplifies `alpha` and `beta`
by at most the corresponding squared and linear condition factors. Any
additional ambient form approximation is charged separately by the operator or
form radius of `L-14308`.

A production certificate should avoid deriving this angle from floating
singular values. It should provide exact rational lower/upper Gram bounds for
the two subspaces and an exact `LDL*` proof of the claimed principal-angle
moat.

## Complete cofinal corollary

At level `j`, let

\[
 K_j=B_j-h_j^{-1}R_j^*M_j^{-1}R_j.
\]

If the entire low packet has an exact radical frame satisfying

\[
 \epsilon_j
 :=\alpha_j+\beta_j^2/h_j\longrightarrow0,
 \tag{L-14313.19}
\]

then

\[
 \lambda_{\min}(K_j)\ge-\epsilon_j.
\]

If simultaneously the complete complement floor and assembly radius obey

\[
 \gamma_j\ge-o(1),
 \qquad
 \delta_j^{assembly}=o(1),
\]

then the `T-14302` lower envelope has nonnegative limit inferior and RH follows.

Thus the growing dimension itself is not an obstruction. The sole packet-level
quantity is the tail-synthesis norm (L-14313.15), or an equivalent common-frame
tightness modulus from `L-14312`.

## Why fixed radical rows do not establish the hypothesis

Suppose `V_je_m->0` for every fixed coefficient vector `e_m`, but the dimension
grows. This is only strong convergence of the tail maps. It does not imply

\[
 \|V_j\|\to0.
\]

The escaping rank-one example in `R-14301` has every fixed column eventually
zero while `||V_j||=1`. Consequently every fixed low-block row may decay even
though (L-14313.16) supplies no shrinking bound.

## Relation to multiband concentration

For a genuine time--frequency concentration eigenbasis with concentration
numbers `chi_(j,m)`, the canonical global bandlimited extensions have an
orthogonal tail map satisfying

\[
 \|V_j\|^2
 =\max_{m\in\text{packet}}
 \frac{1-\chi_{j,m}}{\chi_{j,m}}.
 \tag{L-14313.20}
\]

Hence a packet restricted to

\[
 \chi_{j,m}\ge1-\varepsilon_j
\]

has

\[
 \|V_j\|^2\le\frac{\varepsilon_j}{1-\varepsilon_j}.
\]

For the Weil application this observation is conditional: the global
bandlimited extensions must also be replaced by, or uniformly approximated by,
**exact global Weil-radical vectors in the form-controlling norm**. The
finite Guinand--Weil dictionary is one-way and does not by itself provide this
surjectivity/density theorem.

## Gap audit

- The abstract theorem is exact.
- The actual repository does not yet contain a proof that the complete
  support-dependent generalized-prolate packet has an exact radical frame with
  `||V_j||->0`.
- Ordinary `L2` concentration is insufficient until the constants in
  (L-14313.13)--(L-14313.14) are controlled.
- Approximating each packet vector separately is insufficient; the approximation
  must be uniform in coefficient norm.
- A packet chosen with a fixed concentration threshold need not have a shrinking
  tail norm.
- Establishing the radical-frame property for all cofinal levels would close the
  low matrix and, together with `T-14302`, prove RH.

## Suggested next attack

Prove a form-norm spectral-synthesis theorem for the Mellin multiplier
`zeta(1/2-i xi)`: construct exact `E(S_0)` radical extensions of the complete
multiband concentration packet with a common tail-synthesis bound, or exhibit a
noncompact escaping mode. This is now the precise yes/no hinge.
