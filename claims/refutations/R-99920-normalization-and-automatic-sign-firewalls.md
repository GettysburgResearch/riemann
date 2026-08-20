# R-99920 — Native-normalization and automatic-sign firewalls

Claim ID: `R-99920`  
Status: **PROVED EXACT SEPARATORS**  
Created: 2026-08-20  
Depends on: PR #667 `R-99900`  
RH status: **not assumed**

## 1. The activity is `1/p`, not `1/sqrt(p)`

For the normalized zero-free box,

\[
\frac{(\mathcal S_{67}h)(X)}{\sqrt X}
=\sum_{n\le X}\frac{\beta(n)}n\Phi_{67}(X/n).
\]

Therefore a prime label has native activity `a_p=1/p`.  At the duplicated prime `67`, the middle fibre is

\[
-\frac2{67},
\]

whereas the auxiliary unweighted cancellation from a `1/sqrt(p)` operator would produce `-2`.  These are different source operators.

Every theorem in the T-99920 packet uses `a_p=1/p` and two separately owned `67` labels.

## 2. Full-cube matching does not imply the activated sign

The exact priority flow perfectly matches the complete weighted parity cube, but activation truncation leaves the upward flux of `L-99921`.  That flux cannot be set to zero by formal cube symmetry.

The elementary exact control

\[
\sum_{n\le13}\frac{\mu(n)}n
=-\frac{2323}{30030}<0
\]

shows that a monotone cutoff may still expose a negative parity prefix.  Hence product monotonicity plus complete-cube matching is not a proof of the global box sign.

## 3. Pairwise positivity is not composition

Positive one-prime or two-prime blocks do not imply that arbitrary further Euler factors preserve their positive cone.  The priority-flow theorem avoids this inference: it gives one global coefficient-exact flow for the complete finite cube and then identifies the only activation loss explicitly.

## Boundary

```text
native normalized activity                    1/p, exact
auxiliary half-order normalization             rejected for this use
full-cube Hasse matching                       exact
activation surface automatically zero          false
pairwise positivity implies full composition   not used / rejected
```
