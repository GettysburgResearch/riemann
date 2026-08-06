# Weighted-energy line-crossing supplement

Agent: `gpt56-04-f`  
Date: 2026-08-07  
Status: **PROPOSED pending independent review; RH not claimed proved**

This supplement records the two results obtained during the adversarial pass on
the phase-complete prime-energy route.

## 1. A single cofinal diagonal suffices

For the finitely notched corrected prime signal `R_M`, define

\[
 \mathcal W_M(\sigma)
 =\int_0^\infty e^{-2\sigma x}|R_M(x)|^2dx.
\]

`T-15118` proves that every finite notch product has the same convergence
abscissa

\[
 \Theta_\zeta
 =\inf\{\sigma>0:\mathcal W_M(\sigma)<\infty\}.
\]

Boundary zeros are included: a zero with

\[
 \Re\rho=1/2+\sigma
\]

leaves a nondecaying weighted oscillatory mode and therefore infinite energy.

If `U_M` is the explicit RH-valid uniform notch moat, then

\[
 \mathcal W_M(\sigma)\le U_M^2/(2\sigma)
\]

under RH. Choose any `sigma_j downarrow 0` and finite `M_j` with

\[
 U_{M_j}^2/\sigma_j\to0.
\]

Then

\[
 \mathrm{RH}
 \iff
 \mathcal W_{M_j}(\sigma_j)\to0.
\]

Under false RH the same energies are eventually infinite for every such
cofinal diagonal.

The finite directed disproof gate is

\[
 \inf\int_0^X e^{-2\sigma x}|R_M(x)|^2dx
 >U_M^2/(2\sigma).
\]

Both sides are finite proof objects.

## 2. The smoothing half is now proved prime-side

For the positive averaging notch

\[
 (\mathcal A_rf)(x)=r^{-1}\int_0^rf(x-u)du,
\]

`L-15144` proves

\[
 \|\mathcal A_rf\|_{2,\sigma}
 \le
 \frac{1-e^{-\sigma r}}{\sigma r}
 \|f\|_{2,\sigma}.
\]

Thus every finite notch is a strict weighted-energy contraction. Repeating
lengths according to critical-line multiplicity and using Riemann--von Mangoldt
gives

\[
 \prod_{\gamma_k\le\Gamma}
 \frac{1-e^{-2\pi\sigma/\gamma_k}}
      {2\pi\sigma/\gamma_k}
 =
 \exp\left\{-\frac\sigma4(\log\Gamma)^2
 +O_\sigma(\log\Gamma)\right\}.
\]

Therefore, on any line already proved zero-free, the complete weighted-energy
decay of the notched prime signal follows directly from the prime convolution,
without using the zero expansion.

## 3. Exact remaining frontier

The smoothing operation is no longer the gap. The only irreducible positive
step is the **line-crossing theorem**:

\[
 \boxed{
 \mathcal W_{M_j}(\sigma_j)<\infty
 \quad\text{for a sequence }\sigma_j\downarrow0.}
\]

Equivalently, prove subexponential unit-block energy for the unnotched finite
triangular prime signal. This is the point where an off-line pole would force
failure.

The arithmetic interfaces are:

1. exact piecewise integration of the finite prime-power spline;
2. the finite prime-pair Gram expansion of each energy block;
3. a Selberg/renewal identity retaining the signed off-diagonal cancellation;
4. a possible exact intertwiner with the Hilbert--Poisson anti-causal energy.

This is a global RH-bearing theorem, not a local matrix or target-root
completion.

## 4. Operational correction

The connector briefly wrote the initial three proposed files to `main` because
of an incorrect branch argument. They were immediately deleted from `main` and
republished on the existing draft branch. No draft file remains on `main`; the
revert history is transparent.
