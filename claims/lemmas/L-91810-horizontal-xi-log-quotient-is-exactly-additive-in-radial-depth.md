# L-91810 — The horizontal completed-xi logarithmic quotient is exactly additive in radial depth

Claim ID: `L-91810`  
Status: **EXACT MEROMORPHIC RADIAL COCYCLE AND LOCAL ZERO-DEPTH DECOMPOSITION**  
Created: 2026-08-13  
Depends on: `L-91800`, `L-91801`, `L-91804`  
RH status: **unproved**

## 1. Purpose

PR #430 identifies the remaining theorem as interval-locality in the horizontal depth variable. This note removes one layer of that burden: the *analytic transfer itself* already has an exact additive depth cocycle before any Hilbert-space allocation is chosen.

Put

\[
 \Phi_{\sigma,t}(r)=\log \xi(\sigma+r+it)
\]

on any simply connected zero-free radial interval, with one continuous branch of the logarithm. Then

\[
 \partial_r\Phi_{\sigma,t}(r)
 =\frac{\xi'}{\xi}(\sigma+r+it).
\]

## 2. Exact interval increment

For every zero-free interval `I=(u,v)` contained in the domain of the chosen branch,

\[
\boxed{
 \log\frac{\xi(\sigma+v+it)}{\xi(\sigma+u+it)}
 =\int_u^v\frac{\xi'}{\xi}(\sigma+r+it)\,dr.
}
\tag{L-91810.1}
\]

Consequently, for adjacent intervals `I=(u,v)` and `J=(v,w)`,

\[
\boxed{\Delta_{I\cup J}=\Delta_I+\Delta_J.}
\tag{L-91810.2}
\]

The same identity holds after polarization in finitely many carrier variables because integration and finite linear combination commute.

Thus the horizontal completed transfer is not merely globally factorizable: its logarithm is a finitely additive interval functional away from zeros.

## 3. Symmetric horizontal quotient

For the completed horizontal quotient

\[
 \Theta_{\sigma,\omega}(t)
 =\frac{\xi(\sigma-\omega+it)}{\xi(\sigma+\omega+it)},
\]

one has on every zero-free radial path

\[
\boxed{
 -\log\Theta_{\sigma,\omega}(t)
 =\int_{-\omega}^{\omega}
 \frac{\xi'}{\xi}(\sigma+r+it)\,dr.
}
\tag{L-91810.3}
\]

This is the analytic counterpart of the diffuse prime/eta/bridge/gamma radial source resolutions of `L-91800/L-91804`.

## 4. What happens at a zero

Let `rho` be a zero of multiplicity `m`, and let a radial path cross the depth

\[
 d=|\Re\rho-1/2|>0.
\]

Locally,

\[
 \frac{\xi'}{\xi}(s)=\frac{m}{s-\rho}+h(s),
\]

with `h` analytic. Hence the distributional radial derivative of a continuously unwrapped logarithmic phase acquires a jump concentrated at the crossing depth. Equivalently, contour deformation across the pole changes the logarithmic increment by `2 pi i m`.

Therefore the completed logarithmic radial derivative decomposes schematically as

\[
\boxed{
 d\mathcal L
 =\ell_{\rm reg}(r)\,dr
 +2\pi i\sum_{\rho\ {m crossed}}m_\rho\,\epsilon_\rho\,\delta_{d_\rho},
}
\tag{L-91810.4}
\]

where `epsilon_rho` records orientation. The positive hyperbolic depth measure of `L-91801` is the positive-metric version of precisely these point-depth singularities.

The statement here is analytic and does **not** assert positivity of the regular part.

## 5. Locality is now an allocation problem, not a transfer problem

Equations (L-91810.1)--(L-91810.3) show that the visible completed transfer already respects every rational radial interval. The remaining RLSL burden cannot be that the scalar transfer fails to localize. It is narrower:

> construct the positive arithmetic/model Kolmogorov allocation so that it intertwines the interval projections associated with this already-local scalar cocycle.

Thus PR #430's open theorem separates into two statements:

```text
analytic interval cocycle of completed xi transfer       EXACT / this lemma
positive source-to-model interval-module allocation      OPEN / RH-BEARING
```

## 6. Consequence for a prospective proof

Suppose a completed source/model colligation `W` realizes the transfer and, for every half-open rational interval `I`, satisfies

\[
 W P_I=Q_I W.
\]

By `L-91803`, its one-particle map cannot populate a positive-depth atom from the diffuse arithmetic source. By `L-91801`, every crossed off-line zero produces such an atom. Hence all crossed-zero hyperbolic ports vanish.

The new point is that the interval projections are canonically dictated by the logarithmic derivative itself; they need not be invented independently of the transfer.

## 7. Firewall

The additive scalar cocycle alone does **not** imply module locality of an arbitrary global Kolmogorov factorization. A global unitary may mix two disjoint radial intervals while leaving the total scalar transfer unchanged. Therefore (L-91810.2) is not RLSL and does not prove RH.

## 8. Exact boundary

```text
zero-free radial log-xi increment                    EXACT
additivity on adjacent radial intervals              EXACT
symmetric horizontal quotient integral               EXACT
zero crossing produces point-depth log singularity   EXACT LOCAL MEROMORPHIC FACT
scalar interval additivity -> Hilbert module map      FALSE WITHOUT EXTRA INPUT
canonical interval-module allocation                  OPEN / RH-BEARING
Riemann Hypothesis                                    UNPROVED
```
