# M-105210 — Hostile review addendum for the actual low-order Levinson descent

Claim ID: `M-105210`  
Status: **REVIEW PROTOCOL**  
Created: 2026-08-23  
RH status: **unproved**

This addendum controls `R-105201`, `L-105206--L-105212`, and `T-105210`.

## Review sequence

1. Reconstruct `R-105201` from the exact reverse-Rolle and winding identities.
2. Check the fixed-`lambda` boundary telescope in `L-105206`.
3. Check the exterior-square signs and Fourier convention in `L-105207`.
4. Check both Plancherel identities and the weighted phase sum in `L-105208`.
5. Review every uniform-in-`y` step of the proposed safe-ray theorem
   `L-105209`.
6. Check the completed-zeta factorization and digamma carrier in `L-105211`.
7. Check the curvature-normalized block Gram and the exact factor `R` in
   `L-105212`.
8. Run both exact low-order replays.
9. Review the two open gates in `T-105210` without treating either as proved.

## Automatic rejection tests

Reject a reconstruction upon any of the following:

- calling `CRDB105200` an independent producer after
  \[
  D_r=O_0+2\sum [R_j(1-C_j)-E_j];
  \]
- allowing `lambda` to vary between adjacent derivative quotients while still
  claiming exact telescoping;
- dropping the factors `(-1)^a` or changing the Hilbert inner-product
  convention in the exterior-square Gram without recomputing the sign;
- concluding pointwise `Lambda_m(t)>=0` from positive definiteness;
- deleting the amplitude weight from
  \[
  \int |E|^2\theta'>0;
  \]
- using fixed-order Stirling asymptotics at derivative order
  `r~T^2 log T`;
- replacing the all-`y` reflected-component estimate in `L-105209` by a fixed
  compact-depth estimate;
- treating the zero-free carrier `H(1+lambda h)` as a bound for the argument of
  `V_lambda`;
- proving only `C=1-o(1)` and declaring the last wrong extremum absent;
- omitting the strict extinction threshold
  \[
  \Lambda_{2a}(0)[R\operatorname{tr}K-1^TK1]<M_2;
  \]
- using the complete Gram distance as though it were automatically comparable
  to its rank-one residue projection;
- promoting either finite replay to an analytic Xi theorem.

## Load-bearing distinctions

The low-order packet contains three different strengths:

```text
unconditional exact:
  boundary telescope;
  exterior-square Fourier Gram;
  mean Hermite-Biehler orientation;
  completed-zeta factorization;
  curvature-normalized residue Gram;

proposed complete / review required:
  natural-scale Gaussian Xi limit;
  high-tail two-flux asymptotics;
  complete safe-ray terminal companion;

open:
  HLOC105210 fixed-height argument localization;
  negative mean at the last defective level;
  ESDE105212 strict subunit residue extinction;
  RH.
```

The smallest failure invalidating the terminal-endpoint theorem is failure of
uniform reflected-component negligibility in `L-105209.15`.

The smallest conclusion-facing residue statement is **not** asymptotic
coherence.  It is the strict subunit inequality `ESDE105212`, together with
the correct negative mean.
