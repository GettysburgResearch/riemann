# PFR-R2 — Analytic hard-window firewall

Status: **AUTHOR-PROVED EXACT NO-GO THEOREM / REVIEW PENDING**

Scope: zero-independent holomorphic exponential-mode filters. RH remains unproved.

## 7. PFR-R2 — analytic mode filters cannot make a zero-free hard height window

The remaining localization target has a basic obstruction which should be
recorded before further construction.

Let `Omega` be a connected open set containing the centered physical strip,
and suppose a zero-independent linear filter acts diagonally on exponential
modes by

\[
\mathcal T(e^{\lambda t})=H(\lambda)e^{\lambda t},
\tag{7.1}
\]

where `H` is holomorphic on `Omega`.  This includes translation-invariant
convolutions with sufficient exponential moments, future Gamma resolvents,
and Gaussian or finite resolvent combinations.

If `H` annihilates every possible mode in any nonempty open ordinate band,
then `H` vanishes on a nonempty open subset of `Omega`.  The identity theorem
forces

\[
H\equiv0.
\tag{7.2}
\]

It therefore cannot simultaneously retain a nonzero interior band.  In
particular:

\[
\boxed{
\text{no zero-independent holomorphic mode multiplier gives an exact hard
ordinate window while retaining other modes.}
}
\tag{7.3}
\]

This does not rule out localization.  It proves that an exact source-defined
window must do at least one of the following:

1. accept and quantify leakage;
2. use a non-holomorphic spectral operation and pay the corresponding
   nonlocality on the prime side;
3. exploit additional global structure beyond a scalar diagonal multiplier;
4. interpolate the actual outside zeros, which is inadmissible if their
   locations are inserted into the definition.

Thus `PFR-C2` is now a leakage/structure problem, not a search for a magical
analytic hard cutoff.  This is an elementary identity-theorem firewall;
external novelty is neither expected nor claimed.

---
