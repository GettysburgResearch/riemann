# M-105200 — Hostile review contract for the Xi natural-endpoint and low-order Levinson programme

Claim ID: `M-105200`  
Status: **REVIEW PROTOCOL**  
Created: 2026-08-23  
Updated: 2026-08-23  
RH status: **unproved**

## Review order

1. `R-105201`: verify the exact scope correction to `CRDB105200`;
2. `L-105206`: verify the endpoint quotient and top-boundary telescopes;
3. `L-105207`: verify the exterior-square Fourier Gram signs and conventions;
4. `L-105208`: verify the linewise norm and phase sum identities;
5. `L-105211`: verify the completed-zeta/Levinson factorization;
6. exact `X-105210` replay and retained result;
7. `L-105200--L-105205`: natural-scale high-tail analysis;
8. `L-105209`: complete safe-ray two-tilt saddle;
9. `T-105200/T-105210`: conclusion graph and remaining gates.

## Binding logical audit

The reviewer must independently reconstruct

\[
\mathcal D_r
=O_0+2\sum_{j<r}
\left[R_j(1-\mathfrak C_j)-E_j\right].
\]

Reject any wording which counts `CRDB105200` itself as an independent
low-order estimate.  It is a sufficient zero-count ledger, not a producer.

The boundary telescope must use one fixed `lambda` across the finite ladder.
If different derivative-level parameters are inserted, the exact quotient
cancellation is lost and every transition factor must be restored.

## Exterior-square Gram checks

Reject `L-105207` unless the reviewer verifies:

- the Hilbert-space inner-product convention;
- the factors `(-1)^a` in the exterior vectors;
- the identity
  \[
  <omega_(a,t),omega_(b,s)>=Lambda_(a+b)(s-t);
  \]
- Hermitian symmetry for mixed derivative indices and translations;
- the Fourier formula, including the factor `pi` and the coordinate
  `-u(xi-u)` which makes the Hankel sequence a positive moment sequence;
- that positive definiteness does **not** imply pointwise positivity away from
  the origin.

The central positivity interval must be derived from the spectral second
moment and not treated as a global Laguerre theorem.

## Mean-orientation checks

For `L-105208`, verify directly from the two-sided Xi Fourier kernel that on
`z=x-iy`

```text
E     has multiplier (iu)^k(1+lambda u)e^(yu);
E#    has multiplier (iu)^k(1-lambda u)e^(yu).
```

The exact norm difference must be

\[
4\lambda C_k(y)>0.
\]

The optimal parameter and reflected/forward norm ratio must follow by ordinary
one-variable optimization.  Reject any promotion from line-averaged dominance
to pointwise Hermite--Biehler dominance.

The phase sum rule must retain the amplitude weight `|E|^2`; deleting it is a
false localization.

## Natural-scale high-tail checks

Reject `L-105200` unless the proof supplies:

- one uniform dominant saddle for the positive Xi kernel;
- curvature and third/fourth derivative estimates on the standardized scale;
- exponentially negligible tails after bounded complex exponential tilting;
- relative, not merely additive, control of the one-sided Fourier transform;
- derivative control from a strictly larger complex parameter disk.

Reject `L-105201/L-105202` upon any hidden exchange of fixed derivative order
and growing height, missing buffer, or replacement of an actual critical point
by a model point without `C^2` control.

## Complete safe-ray checks

`L-105209` is the most vulnerable new analytic claim.  Reject it unless all of
the following are proved uniformly for `y>=0`:

1. a unique positive tilted saddle and a variance bound no worse than the
   untilted variance;
2. a non-cancelling lower bound for `P_(r,y)(T)` under `T sigma_r ->0`;
3. exact use of the cancellation
   \[
   \int u^rPhi(u)(1-u/mu_r)du=0;
   \]
4. a three-region proof that the reflected term and its first derivative are
   uniformly negligible;
5. a narrow-sector bound for `G_r/G_(r+1)`, not merely nonvanishing of `E_r`;
6. no use of the fixed-order Stirling/Bell-polynomial estimate with a
   derivative order growing like `T^2 log T`.

The smallest failure invalidating the complete safe-ray theorem is failure of
the uniform reflected-to-positive ratio (L-105209.15).

## Levinson factorization checks

For `L-105211`, verify

\[
xi+lambda xi'
=H(1+lambda h)
\left[zeta+{lambda\over1+lambda h}zeta'\right].
\]

The safe-line nonvanishing of `1+lambda h` must be uniform on the stated
horizontal ray and use a correct digamma/Stirling estimate.  The factorization
must not be described as a bound for the argument of the zeta auxiliary.

## Replay boundary

`X-105200` and `X-105210` authenticate only finite rational/Gaussian-rational
algebra.  They do not machine-prove:

- the Xi Fourier integral or its analytic limit passages;
- `L-105200--L-105202`;
- `L-105205` or `L-105209`;
- fixed-height localization `HLOC105210`;
- the last positive-residue exclusion;
- RH.

The smallest conclusion-facing open statement is `HLOC105210`, together with
the separate last positive-residue exclusion of PR #720.
