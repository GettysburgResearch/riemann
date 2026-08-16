# T-20203 — Critical-mesh integer-dilation screw criteria

Claim ID: `T-20203`  
Title: Every fixed integer dilation gives a one-scalar RH criterion on the common square cutoff mesh  
Status: `PROPOSED — COMPLETE ARGUMENT FROM THE IMPORTED SCREW/LAPLACE IDENTITY; PENDING INDEPENDENT REVIEW`  
Authoring agent: `gpt56-pro-09-n`  
Created: 2026-08-07  
Dependencies: `T-20201`; the Nakamura–Suzuki screw/Laplace normalization; Landau's one-sign theorem  
Scope: global scalar criteria, not finite computations  
Related counterexample candidates: none

> This theorem strengthens `T-20201` from the dyadic Haar defect to every fixed
> integer dilation. Its main proof-facing consequence is that the arithmetic
> negative-prime channel can be made arbitrarily thin while the complete prime
> manifest remains the square cutoff `q <= n^2`.

## 1. Integer-dilation defects

Let

\[
 \Psi(t)=-g_\zeta(t)
\]

in the normalization of `T-20201`. For a fixed integer `r>=2`, define

\[
 \boxed{
 \mathcal D_r(t)=r^2\Psi(t)-\Psi(rt).}
 \tag{1}
\]

The dyadic Haar defect is `D_2`.

Assume RH. Pairing the real zero coordinates gives

\[
 \Psi(t)=2\sum_{\gamma>0}m_\gamma
 {1-\cos(\gamma t)\over\gamma^2}.
\]

Therefore

\[
 \mathcal D_r(t)=2\sum_{\gamma>0}m_\gamma
 {r^2(1-\cos\gamma t)-(1-\cos r\gamma t)\over\gamma^2}.
 \tag{2}
\]

For integer `r`,

\[
 |\sin(rx)|\le r|\sin x|,
\]

so every summand in (2) is nonnegative. Hence

\[
 \boxed{RH\Longrightarrow \mathcal D_r(t)\ge0\quad(t\in\mathbb R).}
 \tag{3}
\]

This is again one fixed finite-difference shape at every scale; no growing
packet dimension enters.

## 2. Exact Laplace transform

Write

\[
 F(s)={\xi'(s)\over\xi(s)}.
\]

The screw transform and the substitution `u=rt` give, initially for
`Im z>r/2`,

\[
 \boxed{
 \int_0^\infty \mathcal D_r(t)e^{izt}\,dt
 ={r\over z^2}
 \left[
  F\!\left({1\over2}-{iz\over r}\right)
  -rF\!\left({1\over2}-iz\right)
 \right].}
 \tag{4}
\]

Put

\[
 B_r(z)=F\!\left({1\over2}-{iz\over r}\right)
       -rF\!\left({1\over2}-iz\right).
 \tag{5}
\]

## 3. `r`-adic pole descent

Suppose `B_r` is holomorphic throughout `Im z>0`. Let

\[
 \rho={1\over2}+\delta+i\tau,
 \qquad \delta>0,
\]

be a zero of `xi` of multiplicity `m`, and set

\[
 z_0=i(\rho-1/2).
\]

The second term in (5) has a pole at `z_0`. Cancellation is possible only if

\[
 \boxed{
 \rho_1={1\over2}+{\rho-1/2\over r}}
 \tag{6}
\]

is also a zero. If its multiplicity is `m_1`, the residue of (5) at `z_0` is

\[
 ir(m_1-m).
\]

Thus holomorphy forces `m_1=m`. Iterating gives distinct zeros

\[
 \rho_k={1\over2}+r^{-k}(\rho-1/2)
\]

converging to `1/2`, impossible for the zero set of the nonzero entire function
`xi`. Therefore

\[
 \boxed{B_r\text{ holomorphic on }\operatorname{Im}z>0\Longrightarrow RH.}
 \tag{7}
\]

The functional equation supplies the reflected half-plane after the right-hand
half-plane is cleared.

## 4. Landau transfer

The unconditional derivative estimate for the screw function gives

\[
 |\Psi'(t)|\le C(1+t)e^{t/2}.
\]

Consequently

\[
 |\mathcal D_r'(t)|
 \le C_r(1+t)e^{rt/2}.
 \tag{8}
\]

If, for every `epsilon>0`,

\[
 \mathcal D_r(t)
 \ge-C_\epsilon(1+t)^{B_\epsilon}e^{\epsilon t}
 \tag{9}
\]

eventually, add a sufficiently large positive polynomial multiple of
`e^(epsilon t)` and a compactly supported correction to obtain a nonnegative
function. Landau's one-sign theorem, applied exactly as in `T-20201`, shows that
its Laplace abscissa cannot lie to the right of `epsilon`, because the
meromorphic continuation in (4) has no singularity on the positive real
Laplace axis: both completed-xi arguments there are positive real numbers.

Letting `epsilon` tend to zero makes `B_r` holomorphic in `Im z>0`; (7) gives RH.

Thus

\[
 \boxed{
 \bigl(-\mathcal D_r(t)\bigr)_+=e^{o(t)}
 \quad\Longrightarrow\quad RH.}
 \tag{10}
\]

## 5. The critical square-cutoff mesh

Set

\[
 \boxed{t_n={2\over r}\log n.}
 \tag{11}
\]

Then

\[
 t_{n+1}-t_n
 ={2\over r}\log(1+1/n)\le {2\over rn},
\]

while

\[
 e^{rt/2}\asymp n
\]

on `[t_n,t_(n+1)]`. Equation (8) therefore gives

\[
 \boxed{
 |\mathcal D_r(t)-\mathcal D_r(t_n)|
 \le C_r(1+\log n).}
 \tag{12}
\]

The complete arithmetic support at `rt_n` is always

\[
 e^{rt_n}=n^2.
\]

Combining (3), (10), and (12) yields

\[
 \boxed{
 RH
 \iff
 \mathcal D_r\!\left({2\over r}\log n\right)\ge0
 \text{ for every sufficiently large integer }n.}
 \tag{13}
\]

More weakly,

\[
 \boxed{
 RH
 \iff
 \left(-\mathcal D_r\!\left({2\over r}\log n\right)\right)_+
 =n^{o(1)}.}
 \tag{14}
\]

The implication from right to left uses (12) to recover (9); under RH the
left-to-right implication is pointwise.

## 6. Positive mixtures retain the converse

Let `R` be a finite nonempty set of integers at least two and let `c_r>0`. Put

\[
 \mathcal D_{\mathbf c}(t)=\sum_{r\in R}c_r\mathcal D_r(t),
 \qquad
 C=\sum_{r\in R}c_rr^2.
 \tag{15}
\]

Under RH this is nonnegative. Its transform has bracket

\[
 \sum_{r\in R}c_rr
 F\!\left({1\over2}-{iz\over r}\right)
 -C F\!\left({1\over2}-iz\right).
 \tag{16}
\]

At a parent zero `rho` of multiplicity `m`, holomorphic cancellation requires

\[
 \boxed{
 C m=\sum_{r\in R}c_rr^2m_r,}
 \tag{17}
\]

where `m_r` is the multiplicity of

\[
 {1\over2}+{\rho-1/2\over r}
\]

and is zero when that point is not a zero. Equation (17) says that `m` is a
positive weighted average of the descendant multiplicities. Hence at least one
descendant has multiplicity at least `m`. Repeating this choice produces an
infinite descendant path converging to `1/2`, again impossible.

Therefore every positive finite mixture has the same pole-descent converse.
If `R_max=max R`, its critical sampling mesh is

\[
 t_n={2\over R_{\max}}\log n.
\]

This creates a finite convex design space of RH-equivalent scalar filters while
preserving one square-cutoff prime manifest.

## 7. Dilation cocycle

The defects satisfy the exact identity

\[
 \boxed{
 \mathcal D_{rs}(t)=r^2\mathcal D_s(t)+\mathcal D_r(st).}
 \tag{18}
\]

This is the multiplicative renormalization law behind the family. It permits
composite dilations to be assembled from prime-dilation defects without changing
the global criterion.

## 8. Proof boundary

- The spectral inequality, transform, residue calculation, and cocycle are exact.
- The Landau and sampling steps are the same analytic interface as `T-20201`.
- No eventual sign or subpower bound is proved here.
- The positive-mixture statement is a criterion and design theorem, not an RH proof.
- Independent review must reconstruct the imported screw normalization and the
  one-sign continuation before promotion.