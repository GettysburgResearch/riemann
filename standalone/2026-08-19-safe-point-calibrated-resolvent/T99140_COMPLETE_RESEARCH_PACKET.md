# T99140 — Safe-point-calibrated nilpotent resolvent hardening

Status: **proposed application hardening; RH unproved**  
Base: PR #628 at `1c21389c7442f81b6bd99649e08177eebc667abc`  
Parent candidate: PR #620 at `493e12fcba3f9b98dda7c3595bff73b256e00ca4`

## 1. The self-consistency obstruction

Put

\[
P_\Lambda(X)=\sum_{n\le X}\frac{\Lambda(n)}{\sqrt n}\log\frac Xn.
\]

Every feasible physical row satisfies

\[
\mathcal H(d_X)\le P_\Lambda(X).
\tag{1}
\]

The PR #620 endpoint chain uses

\[
F_\Lambda(X)=J_\Lambda(X)-P_\Lambda(X)
\le J_\Lambda(X)-\mathcal H(d_X)
\]

and the prime-square/Mellin–Landau consumer.

Mellin inversion gives

\[
P_\Lambda(X)=\frac1{2\pi i}\int_{c-i\infty}^{c+i\infty}
-\frac{\zeta'}{\zeta}\!\left(s+\frac12\right)\frac{X^s}{s^2}\,ds,
\qquad c>\frac12.
\tag{2}
\]

Assume RH. Moving the contour past the pole at `s=1/2`, the safe point `s=0`, the critical-line zeros, and the trivial zeros gives

\[
\boxed{P_\Lambda(X)=4\sqrt X-\kappa\log X+O(1),}
\tag{3}
\]

where

\[
\kappa=\frac{\zeta'}{\zeta}\!\left(\frac12\right)
=\frac12\left(\log\pi+\gamma+\frac\pi2+3\log2\right)
=2.686091709612832\ldots>0.
\tag{4}
\]

The zero contribution is bounded under RH because

\[
\sum_\gamma\frac{m_\gamma}{1+\gamma^2}<\infty.
\]

Equation (4) follows by differentiating the completed functional equation at `1/2` and using

\[
\psi(1/4)=-\gamma-\frac\pi2-3\log2.
\]

Suppose a candidate proves, for all sufficiently large `X`,

\[
\mathcal H(d_X)\ge4\sqrt X-C
\tag{5}
\]

with one absolute constant, proves feasibility, and proves the PR #620 endpoint implication. The endpoint implication yields RH. Equations (1) and (3) then contradict (5).

Therefore the following four assertions cannot all be true:

```text
ideal literal score exactly 4 sqrt(X);
only O(1) loss before feasibility;
ordinary/native feasibility;
the stated endpoint implication to RH.
```

The abstract nilpotent row resolvent of PR #628 is not refuted. The obstruction says that a valid conclusion-producing realization must expose a logarithmic calibration loss before the final native score is measured.

## 2. The exact dyadic logarithmic calibration

Let `X>=2` be an integer and put

\[
K=\left\lfloor\frac X{67}\right\rfloor+1,
\qquad n_X=\lfloor\sqrt K\rfloor,
\qquad L_X=1+\lceil\log_2X\rceil.
\]

Define the rational common thinning

\[
\boxed{\tau_X=\frac{n_X}{n_X+24L_X}.}
\tag{6}
\]

Assume the resolved ideal row is nonnegative and, after the one positive top omission, its nonterminal detail responses satisfy the PR #620 comparison

\[
\Xi_X(q)\le\left(1+\frac{23}{\sqrt K}\right)\Omega_X(q).
\tag{7}
\]

Since `n_X<=sqrt(K)`,

\[
\begin{aligned}
\tau_X\left(1+\frac{23}{\sqrt K}\right)
&\le\frac{n_X}{n_X+24L_X}\left(1+\frac{23}{n_X}\right)\\
&=\frac{n_X+23}{n_X+24L_X}<1.
\end{aligned}
\tag{8}
\]

Thus one common thinning gives strict nonterminal detail feasibility. The terminal positive omission has still more reserve than in the original constant-thinning construction, and the positive radix-four inverse gives ordinary feasibility on the same row.

No directed logarithm or irrational rounding is needed: `n_X`, `L_X`, and `tau_X` are exact integer/rational data.

For every integer `K>=1`,

\[
\lfloor\sqrt K\rfloor\ge\frac12\sqrt K.
\]

Since `K>X/67`,

\[
\begin{aligned}
4\sqrt X(1-\tau_X)
&=4\sqrt X\frac{24L_X}{n_X+24L_X}\\
&\le96L_X\frac{\sqrt X}{n_X}\\
&<192\sqrt{67}\,L_X.
\end{aligned}
\tag{9}
\]

If the one positive omission has literal score at most `C_top`, then

\[
\boxed{
\mathcal H(d_X)
\ge4\sqrt X-192\sqrt{67}\,L_X-C_{\rm top}.
}
\tag{10}
\]

Because `L_X<=2+log_2 X`, the loss is `O(log X)`.

This larger-than-minimal thinning simultaneously:

1. dominates the inherited `23/sqrt(K)` column overfill;
2. removes the impossible constant-deficit claim;
3. matches the unavoidable safe-point logarithmic scale;
4. retains exactly the `o(log^2 X)` endpoint strength.

## 3. Composition with the nilpotent two-sort resolvent

Assume the local PR #620 inputs survive hostile reconstruction:

1. compact two-sort Hall in every physical component row;
2. the residual-only causal row identity;
3. the positive endpoint-frame measure;
4. the finite/continuum discrepancy estimate;
5. the nonterminal and terminal all-column bounds;
6. the prime-square and Mellin–Landau endpoint consumer.

PR #628 resolves the complete labelled source tree before any physical functional is applied:

\[
D_X^{\rm ideal}=J_X(I-T_X)^{-1}s_X=E_X^{\rm eq}.
\]

Hence, on the frozen equality-frame input,

\[
D_X^{\rm ideal}\ge0,
\qquad
\mathcal H(D_X^{\rm ideal})=4\sqrt X.
\]

Remove the one positive top packet and apply (6). The final row is nonnegative, every detail and ordinary column is feasible, and

\[
\mathcal H(d_X)\ge4\sqrt X-O(\log X).
\tag{11}
\]

The elementary parabolic comparison of PR #620 gives

\[
J_\Lambda(X)<4\sqrt X+4\log X.
\]

Therefore

\[
J_\Lambda(X)-\mathcal H(d_X)=O(\log X)=o(\log^2X).
\]

Feasibility gives `H(d_X)<=P_Lambda(X)`, so

\[
F_\Lambda(X)=J_\Lambda(X)-P_\Lambda(X)
\le J_\Lambda(X)-\mathcal H(d_X)
=o(\log^2X).
\]

The frozen prime-square moat and Mellin–Landau consumer then give the proposed RH conclusion.

## 4. Exact boundary

```text
nilpotent row resolution                    proved exact in PR #628
constant-deficit complete composition        refuted
safe-point logarithmic calibration           proved exact
calibrated endpoint composition              complete on frozen local inputs
local Hall/direct-integral/discrepancy inputs pending independent review
Riemann Hypothesis                           unproved
```

The smallest falsifier remains one physical coordinate for which the local identity `E != J+ET`, or one column violating the PR #620 discrepancy bound. The finite algebra in this packet does not establish RH.