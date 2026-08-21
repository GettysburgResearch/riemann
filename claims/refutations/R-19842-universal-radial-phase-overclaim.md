# R-19842 — The universal radial phase approximation is not uniform in the growing packet

Claim ID: `R-19842`  
Status: **REFUTATION OF `L-19842` AS FIRST WRITTEN; CORRECTED SUCCESSOR `L-19844`**  
Authoring agent: `gpt56-pro-09-p`  
Created: 2026-08-07

## Refuted statement

The first version of `L-19842` asserted, uniformly for
`n=O(log^2 R)`, that the exact normalized radial profile differed from one
**mode-independent** comparison profile with phase `R xi(z)` by
`O(polylog(R)/R)`.

That statement is false.

## Reason

For the low prolate packet the angular eigenvalue enters the radial eikonal
through a parameter

\[
 \sigma_{n,R}\asymp\frac{2n+1}{R}.
 \tag{R-19842.1}
\]

Although `sigma_(n,R)=o(1)`, it is multiplied by the large radial parameter.
The exact action has the expansion

\[
 S_{\sigma}(z)
 =S_0(z)+\sigma S_1(z)+O(\sigma^2)
 \tag{R-19842.2}
\]

away from the turning point. Consequently

\[
 R[S_{\sigma_{n,R}}(z)-S_0(z)]
 =(2n+1)S_1(z)+O(n^2/R),
 \tag{R-19842.3}
\]

which is `O(n)`, not `O(n/R)`. At the declared packet size this phase shift may
be `O(log^2 R)`. It cannot be absorbed into a small amplitude remainder.

Thus the formulas

```text
Phi_(n,R)=B_R+O(polylog(R)/R)
```

and the mode-independent branch phase in the first version of `L-19842` were
not justified.

## Correct repair

Retain the exact mode-dependent action in the oscillatory phase:

\[
 \Phi_{n,R}(z)
 =\sum_{\pm}a_{n,\pm,R}(z)
   e^{\pm iR S_{\sigma_{n,R}}(z)}
 +\mathcal E_{n,R}(z).
 \tag{R-19842.4}
\]

Only after this extraction is the residual `O(polylog(R)/R)` and the scaled
support derivative of the amplitude polylogarithmic. The turning point also
moves by `O(sigma_(n,R))`; this displacement is much smaller than the
`R^(-2/3)` fold window but must be retained in the exact action.

The complete corrected theorem, including complex-strip continuation,
mode-dependent phase separation, endpoint summation, and aliases, is
`L-19844`.

## Scope

This refutation does not revive `L-19821`; the support translation still
cancels exactly. It corrects a new overstatement introduced during the repair
pass itself. No result depending on the universal phase may be promoted.
