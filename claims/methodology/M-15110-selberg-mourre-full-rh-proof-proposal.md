# M-15110 — Selberg–Mourre route after adversarial repair

Methodology ID: `M-15110`  
Title: Exact global prime-energy front half, refuted universal inverse, and the corrected localized Selberg source theorem  
Status: **FULL-PROBLEM PROGRAM — ORIGINAL UNIVERSAL `SM(J)` REFUTED; SOURCE-SPECIFIC LOCALIZED COERCIVITY OPEN**  
Authoring agent: `gpt56-04-f`  
Created: 2026-08-07  
Updated: 2026-08-07 after adversarial review  
Dependencies: `L-15147`, `L-15148`, `L-15149`, `L-15150`, `T-15119`, `R-15112`; PR #216 frozen at `b76eef1b769584aa9d66d082bfc6634126f986a2`  
Scope: corrected full-problem route and exact independent-review boundary

## 1. Exact front half that survives

For scale four, put

\[
 P(x)={\psi(x)\over x},
 \qquad
 f(x)=P(x)-P(x/4),
 \qquad
 (Uf)(x)={1\over2}f(x/4),
\]

and

\[
 r=(I-U)f.
\]

The RH-sensitive positive energy is

\[
 \boxed{
 \mathcal R_4(Y)=\int_2^Y|r(x)|^2dx.}
\]

At integer endpoints,

\[
 \boxed{
 \mathcal R_4(N)
 =\sum_{m=2}^{N-1}
 {\left[
 \psi(m)-6\psi(\lfloor m/4\rfloor)
 +8\psi(\lfloor m/16\rfloor)
 \right]^2\over m(m+1)}.}
 \tag{M-15110.1}
\]

Subject to the explicit Hardy/Mellin interface in `T-15119/L-15149`,

\[
 \boxed{
 \Theta_\zeta
 =\limsup_{Y\to\infty}
 {\log(1+\mathcal R_4(Y))\over2\log Y},}
 \tag{M-15110.2}
\]

so

\[
 \mathrm{RH}
 \iff
 \mathcal R_4(Y)=Y^{o(1)}.
\]

The scale-subtracted Selberg operator is

\[
 (\mathcal Lg)(x)
 = (\log x)g(x)
 +\sum_{n\le x}{\Lambda(n)\over n}g(x/n)
 -{1\over x}\int_1^xg(t)dt.
 \tag{M-15110.3}
\]

`L-15147` gives

\[
 \mathcal Lf=H_4,
 \qquad
 H_4(x)=O(1),
 \tag{M-15110.4}
\]

and `L-15148` gives

\[
 \mathcal LU=U\mathcal L+(\log4)U
 \tag{M-15110.5}
\]

and

\[
 \boxed{
 \mathcal L(\mathcal L-\log4)r
 =(I-U)\mathcal LH_4
 -(\log4)(I+U)H_4.}
 \tag{M-15110.6}
\]

The right side is explicit and pointwise `O(1+log x)`.

All of this survives the low-reasoning review and the present independent re-derivation.

## 2. Exact Mellin normal form

`L-15149` adds the exact identity

\[
 \boxed{
 \mathcal M(\mathcal Lg)(z)
 =-q(z)^{-1}{d\over dz}
 \left(q(z)\mathcal Mg(z)\right),
 \qquad
 q(z)=(z+1)\zeta(z+1).}
 \tag{M-15110.7}
\]

Thus the Selberg operator is a derivative conjugated by the zeta factor. This explains both the exact dilation commutator and the real coercivity obstruction: a half-plane inverse estimate necessarily controls `1/q`, whose poles are the shifted zeta zeros.

The variable relevant to RH is

\[
 w=z+{1\over2}.
\]

A zero `rho` produces `w=rho-1/2`, and Mellin Plancherel on `Re z=-1/2+sigma` gives the weight `x^(-2sigma)dx`. This is the explicit shift requested by the review.

## 3. Annular representation

On the annuli

\[
 I_j=[4^j,4^{j+1}),
\]

use

\[
 (\mathscr Ug)_j(u)=2^jg(4^ju),
 \qquad1\le u<4.
\]

Then `U` is the unilateral backward shift `S`, multiplication by `log x` is `j log4+log u`, and

\[
 [\mathscr U\mathcal L\mathscr U^{-1},S]
 = (\log4)S.
\]

If `d=mathscr U r`, then

\[
 \boxed{
 \mathcal R_4(4^J)=\sum_{j=0}^{J-1}\|d_j\|_{L^2([1,4])}^2.}
 \tag{M-15110.8}
\]

This is the exact annular square-function target.

## 4. Withdrawal of the original universal `SM(J)`

The previous version proposed, for every causal vector `c`, an estimate of the form

\[
 \|P_J(I-S)c\|^2
 \le C(1+J)^A
 \left[
 1+\max_j4^{-j}
 \|P_j\mathcal A_J(\mathcal A_J-\log4)(I-S)c\|^2
 \right].
 \tag{M-15110.9-WITHDRAWN}
\]

`R-15112` disproves this statement exactly, even for the pure number operator

\[
 \mathcal A_J=N_J,
 \qquad
 [N_J,S]=S.
\]

Choose an interior index `j=floor(J/2)` and a step vector `c` for which

\[
 (I-S)c=t e_j.
\]

Then

\[
 N_J(N_J-I)(I-S)c=j(j-1)t e_j,
\]

so the required inverse constant is at least

\[
 {4^j\over j^2(j-1)^2},
\]

which grows exponentially. The vector is supported far from both boundaries. Therefore neither a fixed-width boundary correction nor the pure number square rescues the advertised block-normalized universal inverse.

Accordingly:

\[
 \boxed{\text{the original universal }SM(J)\text{ is rejected.}}
\]

The earlier statement that one square identity was the sole missing line is withdrawn.

## 5. What the low-reasoning review got right

The review correctly identified three distinct issues:

1. a Selberg square identity is not yet defined coefficient by coefficient;
2. the endpoint/continuous-average ledger has not been proved boundary-local;
3. positivity of the displayed squares does not automatically control the target norm.

It also correctly required the complete `Lambda_2` ledger. `L-15150` gives

\[
 \Lambda_2(p^a)=(2a-1)(\log p)^2,
\]

\[
 \Lambda_2(p^aq^b)=2\log p\log q,
\]

and

\[
 \Lambda_2(n)=0
 \quad\text{for }\omega(n)\ge3.
\]

Hence PR #216 supplies the delicate squarefree-semiprime sector, not the complete factor map. Prime powers and nonsquarefree two-prime channels must also be present.

The review also correctly warned that “finite boundary rank” must mean a uniformly bounded number of annular blocks unless a genuine finite-dimensional source discretization has been fixed.

## 6. Where the low-reasoning review was still too optimistic

The review suggested that the pure number operator supports the missing Poincare estimate. It does support an ordinary unweighted inequality away from the first two blocks, but it **refutes** the block-normalized output estimate needed in the old `SM(J)`.

Its proposed localized Poincare inequality is therefore necessary but not sufficient. Even if

\[
 \|d\|^2
 \le C J^B
 \left[Q_J(d)+\|P_{\rm bdry}d\|^2\right],
\]

one still has to evaluate `Q_J(d)` for the actual source without applying Cauchy–Schwarz against an output whose physical annular `L2` norm is of size `4^(j/2) poly(j)`. That step recreates the exponential block-volume loss.

The missing theorem is not a generic coercivity estimate. It is a **source-specific localized signed identity** that converts the exact Selberg forcing into polynomial scale energy before any absolute-value loss.

## 7. Corrected three-gate completion package

A valid completion now requires all three gates below.

### Gate A — exact finite Selberg square

Construct actual source-coordinate maps `D_(J)` and `V_(J,n)` and prove

\[
 \boxed{
\begin{aligned}
 \operatorname{Re}
 \langle d,
  \mathcal A_J(\mathcal A_J-\log4)d\rangle
 ={}&\|\mathcal D_Jd\|^2\\
 &+{1\over2}
  \sum_n{\Lambda_2(n)\over n}
  \|\mathcal V_{J,n}d\|^2\\
 &+\langle d,\mathcal B_Jd\rangle.
\end{aligned}}
 \tag{M-15110.10}
\]

Every prime-power and two-distinct-prime channel from `L-15150` must be included. This identity remains proposed.

### Gate B — honest endpoint/bulk ledger

Prove which pieces of `B_J` are truly supported in bounded-width boundary blocks. Any continuous averaging term that remains in the interior must be retained as a bulk operator. A valid lower bound is

\[
 \boxed{
 \langle d,\mathcal B_Jd\rangle
 \ge -\mathfrak b_J(d),}
 \tag{M-15110.11}
\]

with an explicit form `mathfrak b_J` whose later source pairing can be bounded polynomially. Merely writing `P_bdry` does not prove localization.

### Gate C — localized source identity

For the **actual arithmetic solution** `d=mathscr U r`, construct scale cutoffs and localized square forms `Q_(J,<=j)` satisfying

\[
 \boxed{
 \sum_{k\le j}\|d_k\|^2
 \le C(1+j)^B
 \left[
  Q_{J,\le j}(d)+\mathfrak b_{J,\le j}(d)+1
 \right],}
 \tag{M-15110.12}
\]

and then prove directly from the signed scale-subtracted Selberg source that

\[
 \boxed{
 Q_{J,\le j}(d)+\mathfrak b_{J,\le j}(d)
 \le C(1+j)^A.}
 \tag{M-15110.13}
\]

The second inequality must be an exact cutoff/commutator or causal-induction calculation. It may not follow from an unweighted global Cauchy–Schwarz estimate and may not take absolute values before the Selberg completion.

Together, (M-15110.12)--(M-15110.13) give

\[
 \mathcal R_4(4^J)\ll(1+J)^{A+B+1},
\]

hence RH through (M-15110.2).

## 8. Current independent-review target

The durable front half may be reviewed separately:

1. `L-15147`: exact scale-subtracted Selberg identity and bounded forcing;
2. `L-15148`: exact dilation commutator, second-order equation, and finite energy;
3. `L-15149`: exact Mellin gauge and variable shift;
4. `T-15119`: Hardy upper-bound details;
5. PR #216 `T-21502/L-21504`: prime-only and squarefree-semiprime reductions.

The completion is now explicitly **GAPS/BLOCKED** at Gates A--C. A future proof may validate the source-specific package, or may show that a growing family of near-null arithmetic modes prevents it.

## 9. Status boundary

Survives as exact/proposed durable mathematics:

- global RH-equivalent Chebyshev and prime energies;
- finite positive arithmetic producers;
- scale-subtracted Selberg equation with bounded forcing;
- exact dilation commutator and second-order elimination;
- Mellin gauge factorization;
- exact complete `Lambda_2` support.

Rejected:

- the universal block-normalized `SM(J)` estimate;
- the claim that the square identity and endpoint bound alone imply the advertised inverse;
- the claim that PR #216 supplies the complete `Lambda_2` factor map.

Open:

- the exact finite square completion;
- honest endpoint/bulk separation;
- localized source-specific Selberg–Poincare control;
- RH.
