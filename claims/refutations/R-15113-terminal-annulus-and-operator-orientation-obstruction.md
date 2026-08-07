# R-15113 — Terminal-annulus and operator-orientation obstruction

Claim ID: `R-15113`  
Title: The actual finite Selberg operator refutes the old `SM(J)` estimate, and its `Lambda_2` channel is product-dilational rather than the PR #216 factor-ratio Gram  
Status: **PROPOSED EXACT REFUTATION PENDING INDEPENDENT REVIEW**  
Reviewing agent: `gpt56-pro-18`  
Created: 2026-08-07  
Frozen target: PR #158 at `62989402e20ec4f2fe88937c26d1c6c5c21f9832`  
Dependencies: the exact operator definitions in `L-15147/L-15148`; `R-15112` for the independent pure-number-model obstruction  
Scope: refutes the withdrawn universal inverse for the actual arithmetic operator and corrects the proposed use of PR #216; it does not affect the exact Hardy-energy, Selberg, or commutator front half

## 1. The actual compressed Selberg operator

Write

\[
 (\mathcal P f)(x)=\sum_{n\le x}{\Lambda(n)\over n}f(x/n),
 \qquad
 (\mathcal H f)(x)={1\over x}\int_1^x f(t)\,dt,
 \qquad
 M f=(\log x)f(x),
\]

so

\[
 \mathcal L=M+\mathcal P-\mathcal H.
\]

Let `ell=log 4`, put

\[
 X=4^{J-1},
\]

and let `mathcal A_J` be the compression of `mathcal L` to `[1,4X)`, equivalently to annular blocks `0,...,J-1`.

The original `SM(J)` asserted, for every vector in its declared finite graph domain,

\[
 \|P_J(I-S)c\|^2
 \le C(1+J)^A
 \left[
 1+\max_{0\le j<J}4^{-j}
 \|P_j\mathcal A_J(\mathcal A_J-\ell)(I-S)c\|^2
 \right].
 \tag{R-15113.1}
\]

Here `P_j` denotes the single annular output block.

## 2. A terminal-annulus vector sees no prime term

Fix `0<epsilon<1` and choose a nonzero smooth function `d` supported in

\[
 3X<x<(4-\varepsilon)X.
 \tag{R-15113.2}
\]

For every `x<4X` and every integer `n>=2`,

\[
 {x\over n}\le2X<3X.
\]

Therefore

\[
 \boxed{\mathcal P d=0\quad\text{on }[1,4X).}
 \tag{R-15113.3}
\]

The function

\[
 g=(M-\mathcal H-\ell)d
\]

also vanishes below `3X`: there both `d` and its causal integral are zero. Hence the prime operator vanishes again,

\[
 \mathcal Pg=0\quad\text{on }[1,4X),
\]

and the complete compressed second-order operator reduces **exactly** to

\[
 \boxed{
 \mathcal A_J(\mathcal A_J-\ell)d
 =(M-\mathcal H)(M-\mathcal H-\ell)d.}
 \tag{R-15113.4}
\]

No estimate for primes or zeta zeros is involved.

On `[1,4X)`, multiplication by `log x` has norm at most `J ell`. Hardy's inequality gives

\[
 \|\mathcal H\|_{L^2\to L^2}\le2.
\]

Consequently

\[
 \boxed{
 \|\mathcal A_J(\mathcal A_J-\ell)d\|
 \le C_0J^2\|d\|}
 \tag{R-15113.5}
\]

for an absolute constant `C_0`. The output remains entirely in the terminal annulus.

Choose an annular vector `c` whose only nonzero block is the terminal block and whose projected difference satisfies

\[
 P_J(I-S)c=d.
\]

The compensating shifted block lies beyond the finite section. Apply (R-15113.1) to `tc` and let `t->infinity`. After division by `t^2||d||^2`, one obtains

\[
 1\le C_1(1+J)^{A+4}4^{-J},
 \tag{R-15113.6}
\]

which is false for all sufficiently large `J`.

Thus

\[
 \boxed{
 \text{the old universal block-normalized `SM(J)` is false for the actual Selberg operator.}}
 \tag{R-15113.7}
\]

This strengthens `R-15112`: the obstruction is not merely a failure of the pure number model to justify the proposed proof architecture.

## 3. The range of `I-S` does not cancel the zeta-pole channel

Under the Mellin convention of `L-15148`, normalized dilation has multiplier

\[
 U_4:\quad4^{-z-1/2}.
\]

Therefore `I-U_4`, equivalently the annular `I-S`, contributes

\[
 1-4^{-z-1/2},
\]

which is nonzero at `z=0`. Membership in `Ran(I-S)` does **not** cancel the zeta-pole position.

The cancellation at `z=0` comes from the separate arithmetic scale difference

\[
 f_4=P-P(\cdot/4),
\]

whose Mellin multiplier contains `1-4^{-z}`. The actual second difference is

\[
 r_4=(I-U_4)(I-2U_4)P.
\]

Accordingly, the old statement that `Ran(I-S)` alone removes the `z=0` prime-layer singularity is rejected. The corrected `M-15110` no longer makes that claim.

## 4. Exact product-dilation Selberg channel

For every integer `n>=2`, define the normalized causal dilation

\[
 (U_nf)(x)=n^{-1/2}f(x/n).
\]

Then

\[
 \mathcal P=\sum_{n\ge2}{\Lambda(n)\over\sqrt n}U_n,
 \qquad
 U_mU_n=U_{mn},
 \qquad
 [M,U_n]=(\log n)U_n.
\]

It follows exactly that

\[
 \boxed{
 [M,\mathcal P]+\mathcal P^2
 =\sum_{n\ge2}{\Lambda(n)\log n+(\Lambda*\Lambda)(n)\over\sqrt n}U_n
 =\sum_{n\ge2}{\Lambda_2(n)\over\sqrt n}U_n.}
 \tag{R-15113.8}
\]

For `n=pq`, this is a **product-dilation** channel. Its quadratic form contains

\[
 \operatorname{Re}\langle d,U_{pq}d\rangle,
 \tag{R-15113.9}
\]

which correlates a vector with a copy shifted by the product `pq`.

PR #216 `L-21504`, in contrast, expands an ordinary-prime Gram. Its semiprime term is of the form

\[
 \langle U_pd,U_qd\rangle,
 \tag{R-15113.10}
\]

and therefore retains the factor ratio `p/q`. This is an adjoint/Gram orientation, not the `mathcal P^2` orientation in (R-15113.8).

Hence the statement that PR #216 directly supplies the positive factor map required by the old `M-15110.17` is rejected. PR #216 remains correct and useful in its own prime-energy geometry; a new intertwiner would be needed to import it into the second-order Selberg operator.

Coefficient positivity is insufficient: although `Lambda_2(n)>=0`, the form

\[
 \operatorname{Re}\langle d,U_nd\rangle
\]

can have either sign.

## 5. Correct full operator expansion

The continuous averaging operator has the dilation representation

\[
 \mathcal H=\int_1^\infty a^{-3/2}U_a\,da.
\]

The exact identities

\[
 [M,\mathcal H]=\mathcal H^2,
 \qquad
 [\mathcal H,\mathcal P]=0
\]

hold on compactly supported smooth functions. Put

\[
 \mathcal A=M-\mathcal H,
 \qquad
 \mathcal L=\mathcal A+\mathcal P.
\]

Then

\[
 \boxed{
 \begin{aligned}
 \mathcal L(\mathcal L-\ell)
 ={}&\mathcal A(\mathcal A-\ell)\\
 &+2\mathcal P\mathcal A-\ell\mathcal P
 +\sum_{n\ge2}{\Lambda_2(n)\over\sqrt n}U_n.
 \end{aligned}}
 \tag{R-15113.11}
\]

Any future Selberg completion must retain the mixed term

\[
 2\mathcal P\mathcal A-\ell\mathcal P
\]

and must complete the product-dilation form, not substitute the factor-ratio Gram.

## 6. Corrected proof frontier

The exact front half still supports a serious source-specific programme. A valid completion now needs:

1. an exact coefficient-level completion starting from (R-15113.11);
2. honest terminal and continuous-bulk accounting;
3. a localized identity for the **actual arithmetic source** that avoids the exponential annular-volume loss;
4. a strict causal recursion or renewal contraction for the terminal/current-scale energy.

The sufficient block target already recorded in `L-15146/M-15108`,

\[
 \mathcal B_4(J)
 \le C(1+J)^A
 +\varepsilon_J\max_{k<J}\mathcal B_4(k),
 \qquad \varepsilon_J<1\text{ eventually},
\]

remains viable. It is not implied by the old `SM(J)` or by the PR #216 semiprime Gram.

## 7. Status boundary

Unaffected and separately reviewable:

- `T-15119` Hardy/Mellin energy criterion;
- `L-15147` exact scale-subtracted Selberg equation;
- `L-15148` commutator, elimination, finite energy, and annular identity;
- `L-15149` Mellin gauge;
- `L-15150` complete `Lambda_2` support;
- PR #216 prime-only and squarefree-semiprime identities in their own orientation.

Rejected:

- the withdrawn universal `SM(J)` for the actual operator;
- cancellation of `z=0` from `Ran(I-S)` alone;
- direct identification of PR #216's ratio Gram with the product-dilation `Lambda_2` channel;
- the assertion that only one square identity and an endpoint estimate remained before RH.
