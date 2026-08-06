# Prime-annihilator endpoint proof attempt

Agent: `gpt56-pro-global-01`  
Date: 2026-08-07  
Status: **substantial exact reduction and correction pushed; RH not proved or disproved**

## 1. Objective

The requested endpoint was the fixed centered notch identity from `T-21701`:
annihilate every certified critical-line frequency and prove that the remaining
prime signal is zero.

I attacked this as the full theorem rather than adding another finite matrix
gate.  The pass produced one necessary scope correction, one repaired completed
prime theorem, and two sharper positive/probabilistic endpoints.

## 2. First correction: centering creates a two-sided prime formula

The initial compact terminal-prime formula was causal.  Centering the expanding
finite notch supports produces a two-sided rapidly decreasing kernel.  The
reflected stream

\[
 \sum_n{\Lambda(n)\over\sqrt n}G_\infty(x+\log n)
\]

therefore survives.  It cannot be hidden in an endpoint term.

`R-21701` records the correction.  `T-21701` now uses the completed translated
Guinand--Weil functional

\[
 \mathcal P_G(x)=
 \sum_n{\Lambda(n)\over\sqrt n}
 [G(x-\log n)+G(x+\log n)]
\]

and the complete archimedean term.  With this normalization its residual is
exactly the off-line zero packet and

\[
 \mathrm{RH}\iff\mathcal R_\infty\equiv0.
\]

The positive weighted energy

\[
 \int_0^\infty e^{-2\sigma x}|\mathcal R_\infty(x)|^2dx
\]

is a Cauchy Gram and vanishes exactly under RH.

## 3. Strongest scalar collapse: every off-line quartet has one sign

The annihilator product can be factored at the characteristic-function level.
For every critical-line ordinate `gamma`, the uniform and cosine-bell laws have
transforms

\[
 U_\gamma(t)={\sin(\pi t/\gamma)\over\pi t/\gamma},
\]

\[
 C_\gamma(t)=
 {\sin(\pi t/\gamma)
  \over(\pi t/\gamma)(1-t^2/\gamma^2)},
\]

so

\[
 U_L=E_LC_L.
\]

Writing the centered Hadamard product as

\[
 \Xi=E_LE_N
\]

gives

\[
 \Xi C_L=U_LE_N.
\]

Thus

\[
 \mathrm{RH}\iff \mu_\Xi*\mu_C=\mu_U.
\]

The crucial improvement is already visible at second order.  An off-line
quartet represented by

\[
 \rho=1/2+\delta+i\gamma,
 \qquad \delta>0,
\]

contributes

\[
 4m_\rho{\gamma^2-\delta^2\over(\gamma^2+\delta^2)^2}>0.
\]

Consequently

\[
 \boxed{
 D_{\rm off}
 ={\xi''(1/2)\over\xi(1/2)}
 -2\sum_{\xi(1/2+i\gamma)=0}{m_\gamma\over\gamma^2}
 \ge0,}
\]

and

\[
 \boxed{D_{\rm off}=0\iff\mathrm{RH}.}
\]

This is `T-21702`.  It proves that the full annihilator endpoint does not need an
all-function identity: one scalar saturation already rules out every off-line
quartet, with no cancellation possible.

A verified zero height `H` and an ordinary zero-count majorant give an explicit
unconditional upper bound `D_off=O((log H)/H)`.  This is near saturation, but a
finite verified height cannot force exact equality.

## 4. Brownian bridge range representation

Biane--Pitman--Yor identify

\[
 Y=\sqrt{2/\pi}
 \left(\max b-\min b\right)
\]

for a standard Brownian bridge and prove

\[
 \mathbb E[Y^s]=2\xi(s).
\]

Under the half-size-biased law, `Z=log Y` has characteristic function

\[
 {\xi(1/2+it)\over\xi(1/2)}.
\]

Therefore

\[
 \operatorname{Var}(Z)={\xi''(1/2)\over\xi(1/2)}
\]

and the scalar endpoint becomes

\[
 \boxed{
 \mathrm{RH}\iff
 \operatorname{Var}_{1/2}(\log Y)
 =2\sum_{\gamma\ {m on\ line}}{m_\gamma\over\gamma^2}.}
\]

The same random variable is a square root of the explicit gamma convolution

\[
 \Sigma_2={2\over\pi^2}
 \sum_{n\ge1}{\Gamma_{2,n}\over n^2},
\]

which obeys the size-biased perpetuity

\[
 \Sigma_2^*\overset d=\Sigma_2+H\Sigma_2^*,
 \qquad
 \mathbb P(H\in dh)=(h^{-1/2}-1)dh.
\]

`L-21703` records the exact renewal equation and isolates the independent
probability inequality that would finish the proof.

## 5. Proof mechanisms tested

### 5.1 Ordinary averaging

Rejected.  The centered notch convolution has finite total variance; it
converges to a nondegenerate kernel rather than dispersing to zero.

### 5.2 One-sided terminal-prime identity

Rejected after centering.  The reflected prime stream is load bearing.

### 5.3 Generic characteristic-function positivity

Insufficient.  Symmetric positive densities and even log-concave densities may
have nonreal Fourier zeros.  Positivity of Nakamura's completed-Riemann density
does not supply the reverse variance inequality.

### 5.4 Infinite divisibility of `Sigma_2`

Insufficient by itself.  Additive gamma infinite divisibility does not imply
that the Mellin transform of `Sigma_2`, or the Fourier transform of its tilted
logarithm, is a Pólya-frequency transform.

### 5.5 Lee--Yang / total-positivity closure

No valid decomposition was found that writes the tilted Brownian log-range as a
ferromagnetic convolution of elementary Lee--Yang laws.  Establishing such a
decomposition would prove the endpoint, but assuming it merely restates the
missing real-zero theorem.

### 5.6 Finite verified zeros

They give a quantitatively tiny upper bound on `D_off`, not equality.  An
off-line quartet at an arbitrarily high ordinate has arbitrarily small positive
charge.

## 6. Exact remaining theorem

The smallest independent positive statement is now

\[
 \boxed{
 \operatorname{Var}_{1/2}(\log Y)
 \le2\sum_{\gamma\ {m on\ line}}{m_\gamma\over\gamma^2}.}
\]

`T-21702` supplies the reverse inequality and shows that equality is equivalent
to RH.

A stronger sufficient target is the convex-order comparison

\[
 \mathcal L(\log Y\text{ under half tilt})*\mu_C
 \preceq_{\rm cx}\mu_U.
\]

The only currently noncircular inputs capable of proving it are:

1. the Brownian bridge path geometry;
2. the explicit `n^{-2}` gamma convolution;
3. the size-biased perpetuity kernel `h^{-1/2}-1`;
4. an exact differential/renewal comparison preserving convex order.

No proof of this final inequality was obtained in this pass.

## 7. Relation to parallel global attacks

- PR #219 turns the square-screw scalar into a prime-power convex polygon and
  leaves one cofinal transport inequality.
- PRs #216/#222 reduce a prime-only Hardy norm to a signed balanced semiprime
  dispersion estimate.
- PR #218 uses one fixed Haar screw defect and leaves an all-order Stieltjes
  positivity theorem.
- PR #217 now turns the centered annihilator into a positive off-line variance
  defect and an explicit Brownian perpetuity inequality.

These are not four independent mysteries.  They are convex-dual, Hardy-energy,
renormalized-screw, and probabilistic coordinates of the same global signed
spectral charge.

## 8. Honest verdict

The prime-annihilator endpoint was **not proved**.  The original endpoint was
first repaired, then compressed from an infinite functional identity to one
strictly positive scalar defect.  This is a substantial reduction: every
possible off-line quartet now has the same sign, and a single Brownian variance
upper bound would complete RH.

All new theorem statements remain proposed pending independent review.
