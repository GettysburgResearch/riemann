# T-23401 — One fixed-ratio Mertens-shell energy is equivalent to RH

Claim ID: `T-23401`  
Title: A single compact balanced Möbius shell, at any fixed multiplicative ratio, detects the rightmost zeta zero through its block `L2` exponent  
Status: **PROPOSED — COMPLETE MELLIN/HARDY TRANSFER; SHELL-ENERGY BOUND OPEN**  
Authoring agent: `gpt56-pro-09-p`  
Created: 2026-08-07  
Dependencies: `L-23401`; classical Mertens criterion; standard Laplace/Hardy abscissa theorem  
Scope: full Riemann Hypothesis

## 1. Statement

Fix once and for all

\[
0<c<1
\]

and put

\[
I_c(x)=M(x)-M(cx).
\]

Fix also one block length `B>0`, and define the normalized block energy from `L-23401` by

\[
E_{c,B}(J)=
\int_J^{J+B}
\left|e^{-t/2}I_c(e^t)\right|^2dt.
\]

The following are equivalent.

1. The Riemann Hypothesis.
2. For every `epsilon>0`,
   \[
   \boxed{
   \int_1^X|I_c(x)|^2dx
   =O_\varepsilon(X^{2+\varepsilon}).}
   \tag{T-23401.1}
   \]
3. For every `epsilon>0`,
   \[
   \boxed{
   E_{c,B}(J)=O_{\varepsilon,c,B}(e^{\varepsilon J}).}
   \tag{T-23401.2}
   \]

In addition, if

\[
\Theta_\zeta
=\sup_{\zeta(\rho)=0}
 \left(\Re\rho-\frac12\right),
\]

then the block-energy exponent satisfies

\[
\boxed{
\Theta_\zeta
={1\over2}
\limsup_{J\to\infty}
{\log(1+E_{c,B}(J))\over J}.}
\tag{T-23401.3}
\]

Thus the entire RH problem is already present in one explicit positive balanced Gram kernel.

## 2. RH implies the moment bounds

Under RH, the classical Mertens criterion gives, for every `delta>0`,

\[
M(x)=O_\delta(x^{1/2+\delta}).
\]

Therefore

\[
I_c(x)=O_{\delta,c}(x^{1/2+\delta}),
\]

and with `delta=epsilon/4`,

\[
\int_1^X|I_c(x)|^2dx
\ll_{\varepsilon,c}
\int_1^Xx^{1+\varepsilon/2}dx
\ll X^{2+\varepsilon}.
\]

This proves (1) implies (2).

## 3. The second moment implies RH

For `Re(s)>1`, `L-23401` gives

\[
\boxed{
F_c(s):=
\int_1^\infty I_c(x)x^{-s-1}dx
={1-c^s\over s\zeta(s)}.}
\tag{T-23401.4}
\]

Assume (T-23401.1). Fix a compact subset of `Re(s)>1/2`, and let its minimum real part be `sigma>1/2`. Choose `epsilon>0` satisfying

\[
\epsilon<2\sigma-1.
\]

On a dyadic block `[Y,2Y]`, Cauchy--Schwarz gives

\[
\begin{aligned}
\int_Y^{2Y}|I_c(x)|x^{-\sigma-1}dx
&\le
\left(\int_Y^{2Y}|I_c(x)|^2dx\right)^{1/2}
\left(\int_Y^{2Y}x^{-2\sigma-2}dx\right)^{1/2}\\
&\ll
Y^{1+\varepsilon/2}Y^{-\sigma-1/2}\\
&=Y^{-(\sigma-1/2-\varepsilon/2)}.
\end{aligned}
\tag{T-23401.5}
\]

The exponent is negative, so the Mellin integral converges normally on every compact subset of

\[
\Re(s)>\frac12.
\]

Hence the right side of (T-23401.4) is holomorphic there.

If `rho` were a nontrivial zeta zero with `Re(rho)>1/2`, then

\[
1-c^\rho\ne0
\]

by `L-23401.9`, and `rho` is not zero. Thus the right side of (T-23401.4) would have a genuine pole at `rho`, a contradiction. Functional-equation symmetry proves RH.

Therefore (2) implies (1).

## 4. Physical and logarithmic block energies

The substitution `x=e^t` gives the exact identity

\[
\boxed{
E_{c,B}(J)
=\int_{e^J}^{e^{J+B}}
 {|I_c(x)|^2\over x^2}dx.}
\tag{T-23401.6}

On this block,

\[
e^{-2(J+B)}
\int_{e^J}^{e^{J+B}}|I_c(x)|^2dx
\le E_{c,B}(J)
\le e^{-2J}
\int_{e^J}^{e^{J+B}}|I_c(x)|^2dx.
\tag{T-23401.7}

Consequently the local physical bound

\[
\int_X^{e^B X}|I_c(x)|^2dx
\ll_\varepsilon X^{2+\varepsilon}
\]

is equivalent, after an arbitrarily small adjustment of `epsilon`, to (T-23401.2). Geometric block summation is equivalent to the cumulative estimate (T-23401.1).

This proves (2) equivalent to (3).

## 5. Exact growth exponent

Put

\[
Q_c(t)=e^{-t/2}I_c(e^t).
\]

The abscissa of weighted `L2` convergence

\[
\sigma_2
=\inf\left\{\sigma>0:
 e^{-\sigma t}Q_c(t)\in L^2(0,\infty)
\right\}
\]

is determined by the nonnegative block sequence:

\[
\sigma_2
={1\over2}
\limsup_{J\to\infty}
{\log(1+E_{c,B}(J))\over J}.
\tag{T-23401.8}

By `L-23401.7`, the Laplace transform is

\[
{1-c^{z+1/2}\over
 (z+1/2)\zeta(z+1/2)}.
\]

The numerator has no zero at any pole with `Re(z)>0`. The standard Hardy-space abscissa/pole theorem therefore gives

\[
\sigma_2=\Theta_\zeta,
\]

which proves (T-23401.3).

No phase-recurrence theorem, simplicity of zeros, or pointwise leading asymptotic is used.

## 6. The first-cell specialization

At

\[
c={2\over3},
\]

`L-23003` gives

\[
I_{2/3}(D)
=M(D)-M(2D/3)
\]

as the first reduced-Farey cell, up to one fixed nonzero complex scalar. The present theorem strengthens the audit interface:

\[
\boxed{
\mathrm{RH}
\iff
\int_1^X
|M(x)-M(2x/3)|^2dx
\ll_\varepsilon X^{2+\varepsilon}.}
\tag{T-23401.9}

Equivalently, RH is the subexponential block-energy bound for the explicit kernel `K_(2/3,B,J)` of `L-23401`.

## 7. Relationship to the Type-II programmes

The fixed-logarithm decoder `L-15159` on PR #158 shows that every high-order Heath--Brown packet contains an exact translated Möbius safe signal. Choosing the shell window `H_c` makes that signal exactly `Q_c`.

Therefore any proposed `CP(K)`, `BTP(K)`, or signed common-cell theorem must imply (T-23401.2) through an explicit source map. Conversely, proving (T-23401.2) directly already proves RH and makes the larger packet hierarchy unnecessary for logical sufficiency.

This is the minimal source-specific balanced Type-II target.

## 8. Proof boundary

Closed in this theorem, subject to independent review:

- the RH equivalence;
- the physical/logarithmic energy conversion;
- the exact rightmost-zero exponent;
- the first-cell specialization.

Still open:

- the bound (T-23401.1) or (T-23401.2);
- a source-specific balanced Möbius estimate proving it;
- RH.
