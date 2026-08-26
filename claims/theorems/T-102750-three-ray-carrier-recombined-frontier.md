# T-102750 — The filtered Lorentz current is one three-ray carrier-recombined fluctuation

Claim ID: `T-102750`  
Status: **MAJOR UNCONDITIONAL COORDINATE REDUCTION; RH UNPROVED**  
Created: 2026-08-22  
Base: PR #719  
RH status: **unproved**

`L-102728` provides three nonnegative, source-faithful filtered rays

\[
P_-=JP_2Q_{\tau,-3/2},
\qquad
P_0=JP_2Q_{\tau,-1},
\qquad
P_+=JP_2Q_{\tau,-1/2}.
\]

They reconstruct the filtered activation and critical-wavelet coordinates
exactly:

\[
P_2a_\tau=2(P_-+P_+-2P_0),
\]

\[
G_\tau=P_2a_\tau+\frac12(P_+-P_-).
\]

Hence

\[
\boxed{
5P_2a_\tau-G_\tau
=\frac{17}{2}P_-+\frac{15}{2}P_+-16P_0.
}
\tag{T-102750.1}
\]

## Exact common-carrier cancellation

All active shifted quadratics have the same leading term `16y`.  After `P_2`
and `J`, the three rays therefore have one identical affine carrier

\[
\mathcal C_\tau(X)
=
2(2-\sqrt2)
\left(
\sum_n\frac{\Sigma_\tau(n)}{n^{3/2}}
\right)(X-1).
\]

Put

\[
\widetilde P_\bullet=P_\bullet-\mathcal C_\tau.
\]

Because

\[
\frac{17}{2}+\frac{15}{2}-16=0,
\]

(T-102750.1) is equivalently

\[
\boxed{
5P_2a_\tau-G_\tau
=\frac{17}{2}\widetilde P_-
 +\frac{15}{2}\widetilde P_+
 -16\widetilde P_0.
}
\tag{T-102750.2}
\]

Thus the deterministic linear prime carrier cancels before any absolute value.
The filter problem is no longer an unknown matrix-cone transport: it is one
explicit centered three-ray fluctuation.

## Exact remaining theorem

Define

```text
TRF102750:
  after exact source-region and owner recombination, the centered barycentric
  fluctuation in (T-102750.2) has subpower logarithmic negative mass.
```

Then

\[
\mathrm{TRF}_{102750}
\Longrightarrow
\mathrm{FLC}_{102730}
\Longrightarrow
\mathrm{AR\!-\!DEFECT}_{102600}
\Longrightarrow
\mathrm{RH}.
\]

`TRF102750` is source-compatible with the polarized half-divisor current and
the centered completion envelope.  It remains open.  Estimating any uncentered
ray separately is power-lossy and does not prove it.

```text
three positive filtered rays                PROVED
filtered coordinate reconstruction          PROVED EXACT
common affine carrier                       IDENTIFIED EXACTLY
carrier cancellation in Lorentz current     PROVED EXACT
TRF102750                                    OPEN / RH-BEARING
Riemann Hypothesis                           UNPROVED
```
