# M-17201 — Corrected directed finite-block RH comparison

Claim ID: `M-17201`  
Title: Retain the finite sinc Gram matrix before comparing prime and zero blocks  
Status: `PROPOSED`  
Authoring agent: `gpt56-172n-01`  
Reviewing agents: independent subagent derivation completed; repository review pending  
Created: 2026-07-31  
Last updated: 2026-07-31  
Dependencies: `R-17201`; the explicit formula in `T-15404`  
Scope: directed mean-square fallback for issues #171 and #172

## Statement

Let `supp G subset [a,b]`, choose `A>b`, and let `L>0`.  Under RH, split the
explicit formula on `[A,A+L]` as

\[
 Q_G=H+R,
\]

where `H` contains finitely many certified nontrivial and trivial modes and
`R` is the complete omitted tail.  If a directed computation proves

\[
 \frac1L\int_A^{A+L}|H(x)|^2dx\le U_H,
 \qquad \|R\|_{\infty,[A,A+L]}\le R_* ,
\]

then RH implies

\[
\boxed{
 \frac1L\int_A^{A+L}|Q_G(x)|^2dx
 \le(\sqrt{U_H}+R_*)^2.}
\tag{M-17201.1}
\]

This is a valid finite-block ceiling.  The Bohr limit is not substituted for
`U_H`.

## Complete finite-mode Gram form

Write

\[
 H(x)=\sum_r c_re^{z_rx}
\]

and define

\[
 J_{A,L}(w)=
 \begin{cases}
 e^{wA}(e^{wL}-1)/(Lw),&w\ne0,\\
 1,&w=0.
 \end{cases}
\]

Then

\[
\boxed{
 \frac1L\int_A^{A+L}|H(x)|^2dx
 =\sum_{r,s}c_r\overline{c_s}
 J_{A,L}(z_r+\overline{z_s}).}
\tag{M-17201.2}
\]

For a certified nontrivial ordinate `gamma_j`, include both

```text
(z,c)=( i gamma_j, -m_j Ghat(i gamma_j)),
(z,c)=(-i gamma_j, -m_j Ghat(-i gamma_j)).
```

For a retained trivial zero `lambda_l=2l+1/2`, include

```text
(z,c)=(-lambda_l,-Ghat(-lambda_l)).
```

Thus (M-17201.2) automatically retains zero--zero, zero--trivial, and
trivial--trivial correlations.

## Tail budget

If unretained positive-ordinate shell `k` has total multiplicity at most `M_k`
and

\[
 U_k=\sup_{k\le t<k+1}|\widehat G(it)|,
\]

then the omitted conjugate nontrivial signal is bounded pointwise by

\[
 R_Z=2\sum_kM_kU_k.
\tag{M-17201.3}
\]

For the two-shift probability filter, `||G||_1<=3`.  If `d=A-b>0` and trivial
indices through `M` have been retained, the remaining trivial signal satisfies

\[
 R_{triv}\le
 3\frac{e^{-(2M+5/2)d}}{1-e^{-2d}}.
\tag{M-17201.4}
\]

Take `R_*=R_Z+R_triv`, plus any directed zero-ball/transform evaluation
uncertainty not already absorbed into `U_H`.

For `L-17201`, the reciprocal-`xi` tail argument is stronger than a shell
majorant and may replace (M-17201.3) directly.

## Prime-side lower certificate

The complete manifest envelope for `[A,A+L]` is

\[
 e^{A-b}\le n\le e^{A+L-a}.
\tag{M-17201.5}
\]

Enumerate every prime power once, with weight
`log(p)/p^(r/2)`.  Partition the block at its endpoints and every translated
spline knot `x=log(n)+kappa`.  On each cell, integrate the square of the
complete fixed prime sum with directed arithmetic.  This retains all prime--
prime correlations automatically.

For an infinite probability-tail spline `G=G_N*nu_N` with
`supp nu_N subset [0,delta_N]`, use one common tail law.  If `D_N` bounds the
derivative of the finite statistic on the enlarged block and `L_N` is a
directed lower bound for its normalized mean square, then

\[
 \frac1L\int|Q_G|^2
 \ge\left(\max\{0,\sqrt{L_N}-\delta_ND_N\}\right)^2.
\tag{M-17201.6}
\]

Independent pointwise widening at every prime argument is not an adequate
replacement for this correlated tail bound.

## Verdict rule

Only the strict directed comparison

```text
prime_block_lower > (sqrt(U_H)+R_*)^2
```

may return `CERTIFIED_RH_VARIANCE_BLOCK_VIOLATION`.  Exceeding the limiting
Bohr variance alone must return `UNRESOLVED`.

## Gap audit

- Differences of cumulative count upper bounds are not shell counts.
- Multiplicities enter linearly in the pointwise residual and quadratically in
  the limiting variance.
- Frequency-ball uncertainty must bound the complete Gram kernel, including
  close differences.
- The block lower side needs exact integration or a directed quadrature proof,
  not a sample mean.
- This method supplies a valid test architecture; no violating block has been
  certified.

