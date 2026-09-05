# PFR-R2 — Analytic hard-window firewall

Status: **AUTHOR-PROVED EXACT NO-GO THEOREM; REVIEW PENDING**
Scope: zero-independent holomorphic exponential-mode filters
RH status: **unproved**

Let a linear filter act on exponential modes by

\[
\mathcal T(e^{\lambda t})=H(\lambda)e^{\lambda t},
\]

where `H` is holomorphic on a connected domain containing the centered
physical strip.  If the filter annihilates every possible mode in a nonempty
open ordinate band, then `H` vanishes on an open subset and hence is
identically zero.  It cannot also retain a nonzero interior band.

Therefore no zero-independent holomorphic multiplier gives an exact hard
height window.  Future Gamma resolvents, Gaussian filters, and convolution
filters with exponential moments must accept leakage.  Exact localization
would require a non-holomorphic/nonlocal operation, additional global
structure, or interpolation using the outside zero set itself.

This is an identity-theorem firewall, not an RH result and not an external
novelty claim.

Full proof: `LOCALIZATION_FIREWALL_108260.md`.
