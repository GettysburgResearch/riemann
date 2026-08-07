# R-15112 — Terminal-annulus obstruction to the proposed Selberg–Mourre estimate

Claim ID: `R-15112`  
Title: The finite-section estimate `SM(J)` fails on terminal-annulus vectors, and the PR #216 semiprime Gram has the wrong operator orientation for the proposed Selberg square  
Status: **PROPOSED REFUTATION PENDING INDEPENDENT REVIEW**  
Reviewing agent: `gpt56-pro-18`  
Created: 2026-08-07  
Frozen target: PR #158 at `62989402e20ec4f2fe88937c26d1c6c5c21f9832`  
Targets: `M-15110.12`, `M-15110.17`, `M-15110.18`, and the claim that PR #216 `L-21504` supplies the required positive factor map  
Scope: rejects the advertised finite-section coercivity statement as written; it does not affect `T-15119`, `L-15147`, or the exact algebra in `L-15148`

## 1. Setup

Write

\[
 (\mathcal P f)(x)=\sum_{n\le x}{\Lambda(n)\over n}f(x/n),
 \qquad
 (\mathcal H f)(x)={1\over x}\int_1^x f(t)\,dt,
 \qquad
 M f=(\log x)f,
\]

so

\[
 \mathcal L=M+\mathcal P-\mathcal H.
\]

Let `ell=log 4`, let `P_J` restrict to `[1,4^J)`, and let

\[
 \mathcal A_J=P_J\mathcal LP_J.
\]

The proposed estimate `SM(J)` asserts, for every vector in its declared finite arithmetic graph domain,

\[
 \|P_J(I-S)c\|^2
 \le C(1+J)^A
 \left[
 1+\max_{0\le j<J}4^{-j}
 \|P_j\mathcal A_J(\mathcal A_J-\ell)(I-S)c\|^2
 \right].
 \tag{R-15112.1}
\]

Here `P_j` is the single output annulus, as specified in `M-15110`.

## 2. A terminal-annulus test on which all prime terms vanish

Fix `J` and put

\[
 X=4^{J-1}.
\]

Choose a nonzero smooth function `d` supported in

\[
 3X<x<(4-\varepsilon)X
 \tag{R-15112.2}
\]

for one fixed `0<epsilon<1`. This lies strictly inside the terminal annulus `[X,4X)`.

For every `x<4X` and every integer `n>=2`,

\[
 {x\over n}\le 2X<3X.
\]

Hence

\[
 \mathcal P d=0
 \qquad\text{throughout }[1,4X).
 \tag{R-15112.3}
\]

The function `(M-\mathcal H-ell)d` is also supported in `[3X,4X)`: below `3X` both `d` and its causal integral vanish. Therefore the prime term vanishes again after the first application, and exactly

\[
 \boxed{
 \mathcal A_J(\mathcal A_J-\ell)d
 =(M-\mathcal H)(M-\mathcal H-\ell)d.}
 \tag{R-15112.4}
\]

No prime estimate, PNT input, or approximation enters this identity.

On the terminal annulus,

\[
 \|M\|\le J\ell.
\]

Hardy's inequality gives `||mathcal H||_(2->2)<=2`; a direct Cauchy–Schwarz estimate on `[3X,4X)` also gives a fixed absolute bound. Consequently

\[
 \boxed{
 \|\mathcal A_J(\mathcal A_J-\ell)d\|
 \le C_0J^2\|d\|}
 \tag{R-15112.5}
\]

for an absolute `C_0`. The output is supported in the same terminal annulus.

Choose a finite annular vector `c` whose only nonzero block is `c_(J-1)=d`. Then

\[
 P_J(I-S)c=d;
 \tag{R-15112.6}
\]

the compensating shifted block lies outside the finite section. Thus (R-15112.1), applied to `tc` for a scalar `t`, would give

\[
 t^2\|d\|^2
 \le C(1+J)^A
 \left[
 1+C_0^2J^4\,4^{-(J-1)}t^2\|d\|^2
 \right].
\]

Letting `t->infinity` and dividing by `t^2||d||^2` forces

\[
 1\le C_1(1+J)^{A+4}4^{-J}.
 \tag{R-15112.7}
\]

This is false for all sufficiently large `J`.

Therefore

\[
 \boxed{\text{`SM(J)` is false under its literal universal graph-domain quantifier.}}
 \tag{R-15112.8}
\]

If “source-bound causal vector” is intended to exclude terminally localized vectors, the admissible space must be defined. Such a restriction would turn `SM(J)` from a finite operator coercivity theorem into a source-specific estimate, and its claimed derivation from a general square completion would have to be rewritten.

## 3. The range of `I-S` does not cancel the z=0 prime pole

Under the Mellin convention of `L-15148`, normalized dilation has multiplier

\[
 U_4:\quad 4^{-z-1/2}.
\]

Hence `I-S`, equivalently `I-U_4`, contributes

\[
 1-4^{-z-1/2},
\]

which is nonzero at `z=0`. It removes the `L2` stationary line `Re z=-1/2`, not the zeta-pole position `z=0`.

The actual arithmetic source has an additional factor

\[
 1-4^{-z}
\]

coming from

\[
 f_4=P-P(\cdot/4).
\]

Thus the actual second difference is doubly filtered:

\[
 r_4=(I-U_4)(I-2U_4)P.
\]

The sentence in `M-15110.5.2` that membership in `Ran(I-S)` removes the `z=0` prime-layer singularity is false. The cancellation belongs to the special source `f_4`, not to the whole range of `I-S`.

This correction does not repair (R-15112.8): on a finite section, a terminally supported vector also lies in the projected doubly filtered range because its shifted companions leave the section.

## 4. Product-dilation versus factor-ratio orientation

Define normalized causal dilations

\[
 (U_nf)(x)=n^{-1/2}f(x/n)
\]

and the prime operator

\[
 \mathcal P=\sum_{n\ge2}{\Lambda(n)\over\sqrt n}U_n.
\]

Since

\[
 [M,U_n]=(\log n)U_n,
 \qquad
 U_mU_n=U_{mn},
\]

one has the exact operator identity

\[
 \boxed{
 [M,\mathcal P]+\mathcal P^2
 =\sum_{n\ge2}{\Lambda(n)\log n+(\Lambda*\Lambda)(n)\over\sqrt n}U_n
 =\sum_{n\ge2}{\Lambda_2(n)\over\sqrt n}U_n.}
 \tag{R-15112.9}
\]

Thus the Selberg channel in

\[
 \mathcal L(\mathcal L-\ell)
\]

is a **product-dilation** channel. For `n=pq`, its quadratic contribution is proportional to

\[
 \operatorname{Re}\langle d,U_{pq}d\rangle,
 \tag{R-15112.10}
\]

which correlates scales separated by the product `pq`.

PR #216 `L-21504`, by contrast, comes from a prime Gram or `mathcal P^*mathcal P` orientation. Its semiprime term is proportional to

\[
 \langle U_pd,U_qd\rangle,
 \tag{R-15112.11}
\]

and retains the factor ratio `p/q`. This is the balanced squarefree-semiprime channel.

Equations (R-15112.10) and (R-15112.11) are different operator geometries. No direct insertion of the PR #216 balanced Gram into (R-15112.9) is available. A new intertwining identity would be required.

In particular, positivity of the scalar coefficient `Lambda_2(n)` does not make

\[
 \operatorname{Re}\langle d,U_nd\rangle
\]

nonnegative. The exact factor maps and all compensating diagonal terms must be constructed before a positive-square claim can be made.

## 5. Corrected exact algebraic frontier

Let

\[
 \mathcal H=\int_1^\infty a^{-3/2}U_a\,da,
 \qquad
 \mathcal L=(M-\mathcal H)+\mathcal P.
\]

The identities

\[
 [M,\mathcal H]=\mathcal H^2,
 \qquad
 [\mathcal H,\mathcal P]=0
\]

give the exact decomposition

\[
 \boxed{
 \begin{aligned}
 \mathcal L(\mathcal L-\ell)
 ={}&(M-\mathcal H)(M-\mathcal H-\ell)\\
 &+2\mathcal P(M-\mathcal H)-\ell\mathcal P
 +\sum_{n\ge2}{\Lambda_2(n)\over\sqrt n}U_n.
 \end{aligned}}
 \tag{R-15112.12}
\]

This is the correct starting point for any future Selberg completion. It leaves three nontrivial tasks:

1. complete the **product-dilation** form, including the mixed term `2mathcal P(M-mathcal H)-ellmathcal P`;
2. retain and control the terminal finite-section trace instead of treating it as a harmless constant;
3. derive a source-specific causal recursion or strict renewal contraction.

The already recorded sufficient target

\[
 \mathcal B_4(J)
 \le C(1+J)^A
 +\varepsilon_J\max_{k<J}\mathcal B_4(k),
 \qquad \varepsilon_J<1\text{ eventually},
\]

remains viable. It is not implied by `SM(J)` or by the PR #216 semiprime Gram.

## 6. Status boundary

The refutation does not affect the following exact components:

- the Hardy/Mellin energy criterion `T-15119`;
- the scale-subtracted Selberg–Volterra equation `L-15147`;
- the dilation commutator and second-order equation `L-15148`;
- the finite positive arithmetic formula for `mathcal R_4(N)`;
- the PR #216 prime-only and squarefree-semiprime identities in their own Gram orientation.

It rejects:

- `SM(J)` as stated;
- the claim that `Ran(I-S)` alone removes the `z=0` pole;
- the claim that PR #216 directly supplies the positive factor map in `M-15110.17`;
- the assertion that only the displayed square identity and endpoint lower bound remain before RH.
