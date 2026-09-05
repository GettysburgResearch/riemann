# T-105270 — Carrier-corrected ninety-percent frontier

Claim ID: `T-105270`  
Status: **PROVED CORRECTION AND CONDITIONAL IMPLICATION; NINETY PERCENT OPEN**  
Created: 2026-08-24  
Depends on: R-105270; L-105270--L-105271; L-105500; T-105240  
RH status: unproved

## 1. Disposition of the former edge gate

The exact Toeplitz--Hankel formulas of T-105260 remain valid at their local
source scope, and the carrier-free Hankel polarization still costs less than
\(1/60\).  However, R-105270 proves that the positive degree-zero safe-line
carrier is canceled exactly by the complementary closed contour.

Therefore the natural `EDGEFLUX105260` decomposition contains a mandatory
negative identity block in the pure-carrier fixture.  Its proposed
\(647/19980\) bound is false in that decomposition.  T-105260 is superseded as
a conclusion-producing route.

Likewise, T-105250's all-degree coefficient hierarchy remains correct, but an
actual/model transfer that counts the model's degree-zero term as a positive
closed-contour identity cannot be asymptotically lossless without separately
owning the carrier cancellation.

## 2. What remains genuinely useful

After closed-contour renormalization,

\[
\frac{P_K(x)^2}{1-x}
\longmapsto
Q_K(x)=\sum_{m\ge K+1}q_{K,m}x^m.
\]

The carrier-free tail has superfactorially small physical Hilbert--Schmidt
energy.  L-105271 also proves that its vertical endpoint pieces can be killed
by a source-fixed analytic taper without changing more than `o(d)` horizontal
mass.

Thus the polynomial hierarchy is a powerful **perturbation suppressor**, but
not a source of positive trace.

## 3. Exact repaired implication

Let \(G_T\succ0\) be a physical Gram on a \(d_T=(1-o(1))N_1(T,2T)\)-dimensional
source-owned observation space.  Suppose the actual Xi critical-residue
compression has a decomposition

\[
C_T=B_T+Q_{K,T}+E_T,
\tag{1}
\]

where:

1. `INDEXCARRIER105270`: \(B_T\) is a **conclusion-facing** carrier—owned by
   actual residues, a Cauchy/Hermite--Biehler index, or a non-holomorphic
   boundary jump—and
   \[
   \nu_+(B_T)\ge(19/20+\varepsilon)d_T;
   \]
2. the carrier-free Wick tail satisfies
   \[
   \operatorname{tr}
   \bigl((G_T^{-1/2}Q_{K,T}G_T^{-1/2})_-\bigr)
   =o(d_T)
   \]
   after taking fixed \(K\) sufficiently large;
3. the remaining carrier-free contour error satisfies
   \[
   \operatorname{tr}
   \bigl((G_T^{-1/2}E_TG_T^{-1/2})_-\bigr)
   <(\varepsilon-o(1))d_T.
   \]

Then Ky Fan subadditivity and the exact confluent full-signature theorem give

\[
\boxed{
\liminf_{T\to\infty}
\frac{N_0(T,2T)}{N(T,2T)}>0.9.
}
\tag{2}
\]

The natural concrete candidate for `INDEXCARRIER105270` is the canonical
companion/Cauchy-index field of T-105230/T-105240, not the holomorphic frozen
constant.  Its real-axis Lorentz energy and companion-pole index are already
owned exactly; the source-qualified estimate required to obtain a
\(19/20+\varepsilon\) base remains open.

## 4. Precise status

```text
closed-contour carrier cancellation          PROVED EXACT
T-105260 natural edge budget                 REFUTED
analytic endpoint taper for carrier-free row PROVED
carrier-free Wick tail suppression           PROVED AT MODEL/SOURCE SCOPE
conclusion-facing index carrier               OPEN / RECORD-BEARING
ninety percent for zeta                       UNPROVED
Riemann Hypothesis                            UNPROVED
```

This correction prevents a false unconditional ninety-percent claim while
retaining the valid source algebra and isolating the exact kind of carrier a
successful proof must construct.
