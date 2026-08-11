# Fredholm continuation: every fixed nonlinear degree is asymptotically blind

**Date:** 2026-08-11  
**Status:** trace-class theorem proposed for independent review  
**RH:** unproved

## Result

For the modulated Gaussian confinement

\[
J_{\sigma,T}=M_{e^{iTu}}J_\sigma,
\qquad
A_{\sigma,T}=J_{\sigma,T}^*WJ_{\sigma,T},
\]

the exact off-line-pair index remains unchanged. On the prime side,

\[
A_{\sigma,T}=\mu(T)B_\sigma+E_{\sigma,T},
\qquad
B_\sigma=J_\sigma^*J_\sigma\succeq0,
\qquad
\sup_T\|E_{\sigma,T}\|_1<\infty.
\]

Here \(\mu(T)\sim(2\pi)^{-1}\log(T/2\pi)\). Thus

\[
A_{\sigma,T}/\mu(T)\to B_\sigma
\]

in trace norm, while false-RH negative trace mass can remain only `O(1)` inside positive bulk of size `Theta(log T)`.

Consequences, independent of RH:

- every fixed exterior coefficient `tr(wedge^k A_(sigma,T))` is eventually positive;
- every fixed shifted-Hankel matrix is eventually positive definite;
- normalized positive-axis Fredholm roots escape every compact set.

Therefore, if RH is false, the first detecting exterior/Hankel degree must tend to infinity with carrier height.

## Strategic consequence

The programme

```text
fix one nonlinear degree;
let carrier height grow;
prove its prime-side asymptotic positivity;
conclude RH
```

is impossible: that positivity holds even under false RH. The all-order quantifier in PR #373 is essential.

Viable options are:

1. keep one fixed carrier and prove the whole determinant positive;
2. let the degree grow with height and prove uniform estimates at that growing degree;
3. isolate an off-line pair before taking the high-carrier limit.

## Verification

```text
PASS_X_90705_HIGH_CARRIER_FIXED_DEGREE_FIREWALL
```

The moving-tail diagonal model retains one negative eigenvalue while its first negative exterior degree grows

```text
5, 9, 17, 29, 52, 90
```

across increasing carriers.
