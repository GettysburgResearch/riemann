# R-100100 — Binding firewalls for the two-route synthesis

Claim ID: `R-100100`  
Status: **PROVED EXACT SCOPE/MECHANISM FIREWALLS**  
Created: 2026-08-20  
RH status: **unproved**

## 1. Infinite completion erases the detector

Completing every prime to order `k` changes the duplicate-67 source to

\[
\boxed{
B_{\infty,k}(z)=\frac{1-67^{-kz}}{\zeta(kz)}.
}
\]

The original detector `(1-67^(-z))/zeta(z)` has disappeared.  Therefore a
finite completion may not be silently replaced by an infinite completion
before the Mellin-Landau step.

## 2. Endpoint-dependent completion is not one Mellin multiplier

If `Z` or `k` depends on the physical endpoint, then

\[
D(X)=\mathscr A_{Z(X),k(X)}H(X)
\]

has no single multiplier `mathcal A(z)`.  Pole preservation one endpoint at a
time does not prove a global Mellin identity.  Route B therefore uses fixed
completed functions and the sign-change location `N_(Z,k)`.

## 3. The arsinh-one ceiling is methodological

The common lower bound is

\[
H(X)\ge K(X)[1-\sinh\Sigma].
\]

Even as completed-prime mass tends to zero, the remaining prime-ratio interval
contributes `log A+o(1)`.  Thus the present level-pairing proof reaches only

\[
A<\exp(\operatorname{arsinh}1)=1+\sqrt2.
\]

Raising the finite completion order does not by itself establish global
positivity.  Positivity beyond the ceiling is neither proved nor refuted.

## 4. Compact and cubic activation differ

For compact SHARP, shifts `d>X` vanish, so a full completion multiplier may
contain inactive residue contributions.  For the cubic carrier, `Psi(y)>0` for
all `y>0`; all finite completion shifts are physically present.  Route B must
therefore use the cubic carrier if it invokes the full residue multiplier.

## 5. Supercritical carriers do not sign the critical remainder

PR #676 proves all centered remainders before the final prime-harmonic step.
That does not control the final quadratic/cubic critical sign or its critically
weighted downward variation.

```text
infinite completion preserves detector         false
moving completion is one multiplier             false
higher order makes level proof global           false
compact SHARP sees every completion residue      false
cubic carrier sees every completion residue      true
supercritical positivity closes critical sign    false
DCE100100 / QPET100101                           open
Riemann Hypothesis                               unproved
```
