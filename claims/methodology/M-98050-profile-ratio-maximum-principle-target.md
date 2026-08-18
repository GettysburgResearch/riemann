# M-98050 — Profile-ratio maximum-principle target for dynamic finite-block transfer

## Objective

For an admissible future state with least prime `p`, define whenever the denominator is positive

\[
Q(Y,p)=\frac{U(Y/p,p^+)}{U(Y,p^+)}.
\]

The exact native recurrence is

\[
U(Y,p)=U(Y,p^+)\left(1-\frac{Q(Y,p)}p\right).
\]

Thus the one-prime Bellman inequality is exactly

\[
\boxed{Q(Y,p)\le p.}
\]

This formulation converts the remaining dynamic finite-block transfer into a ratio bound rather than a positivity cone.

## Continuous model

In the homogeneous Dickman approximation,

\[
Q_{\rm cont}(u)=\frac{\rho(u-1)}{\rho(u)}=-u\frac{\rho'(u)}{\rho(u)}
\ll u\log(u+2).
\]

Hence `Q_cont << p` throughout the hereditary mesoscopic corridor. The root difficulty is whether the discrete Stieltjes-transferred ratio can develop a large upward spike while both numerator and denominator retain the exact common future-prime source.

## Desired theorem: PRMP67

Prove a source-specific maximum principle of the form

\[
Q(Y,p)
\le
\max\{Q(Y_0,p),\,C u\log(u+2)\}
\]

along each activation interval or under the update `Y -> Y/p`, with a finite initial certificate. Any such bound with right side `<p` for every `p>=67` would give dynamic finite-block transfer and hence GPC67.

## What a valid proof must exploit

- numerator and denominator use the same future-prime state `p^+`;
- the same signed Stieltjes measure `dh` enters both;
- their kernels differ only by the multiplicative endpoint shift `Y -> Y/p`;
- source activations are nested;
- no division may be made where the denominator sign is unknown.

## Hostile tests

Before promotion, test exact finite states for:

1. denominator zeros or near-zeros;
2. ratio spikes at activation knots;
3. failure of cellwise monotonicity;
4. p=67 and p=71 first, where the margin is smallest;
5. mutations of one Möbius owner to ensure the claimed maximum principle is genuinely source-specific.

A counterexample to PRMP67 does not refute GPC67; it only refutes this low-dimensional closure mechanism.
