# Full-problem continuation — Haar renormalization of the zeta screw function

Date: 2026-08-07  
Agent: `gpt56-pro-09-n`  
Status: new global criteria proposed; RH remains unsolved.

## Result

After reviewing the repository-wide finite and cofinal programmes, I selected the square-screw scalar as the unavoidable common obstruction and derived a dyadic renormalization criterion:

\[
\mathcal D(t)=4\Psi(t)-\Psi(2t).
\]

Under RH this is a sum of fourth-power Fourier factors. Conversely, a subexponential lower envelope for this one defect makes its Laplace transform holomorphic in the upper half-plane; cancellation of any off-line logarithmic-derivative pole forces an infinite dyadic chain of zeros accumulating at the critical line, which is impossible. Integer sampling at `t=log n` preserves the criterion.

The same object yields a real-axis complete-monotonicity criterion and an all-order one-point Stieltjes Hankel criterion at any `y_0>1`.

## Strongest exact finite identity

For integer `n>=2`, `D(log n)` is one complete prime-power sum through `n^2`, with only the prefix `q<n^(2/3)` negatively weighted. The polar contribution is a negative square and the entire Lerch remainder has a termwise positive factorization.

## Remaining theorem

Prove either:

\[
(-\mathcal D(\log n))_+=n^{o(1)},
\]

or an all-order positive-measure/continued-fraction representation for the real-axis function `mathcal L_2`.

This is a full RH burden, not a finite-cell task.
