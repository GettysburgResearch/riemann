# R-106432 — Source-density ratios do not bound visible all-pass Hankel energy

Claim ID: `R-106432`  
Status: **PROVED EXACT FIREWALL; BINDING CORRECTION TO T-106430**  
Created: 2026-08-25  
Depends on: `R-106420`; `L-106410--L-106413`; `L-106431`  
RH status: **not assumed**

## 1. Distinct objects

The small-shift source lemmas compare Fourier densities of the analytic
endpoint numerator difference and a positive analytic denominator source.
They prove exact inequalities of the form

\[
|\widehat{N-D}(\xi)|^2
\le c_*\,|\widehat A(\xi)|^2
\]

on the declared finite source channels, with `c_*<1/600` after summing the
four orientations.

The visible quantity in the signed all-pass index theorem is instead

\[
\|H_{N/D}P\|_{\mathcal S_2}^2,
\]

where `P` is a source projection in the Hardy domain.  Division by `D` is a
non-diagonal meromorphic operation.  A pointwise comparison between the
Fourier densities of `N-D` and `A` does not control the Fourier coefficients
of `(N-D)/D` and therefore does not control this compressed Hankel norm.

## 2. Exact counterfamily

For every integer `m>=1`, put on the unit circle

\[
N_m(z)=1,
\qquad
D_m(z)=z^m,
\qquad
U_m(z)=N_m(z)/D_m(z)=z^{-m}.
\]

Then `N_m-D_m=1-z^m` is analytic, and hence

\[
H_{N_m-D_m}=0.
\]

Nevertheless

\[
\|H_{U_m}\|_{\mathcal S_2}^2=m.
\]

For the hard source projection

\[
P_d:\ H^2\to\operatorname{span}\{1,z,\ldots,z^{d-1}\},
\]

one has exactly

\[
\boxed{
\|H_{U_m}P_d\|_{\mathcal S_2}^2=\min(d,m).
}
\tag{R-106432.1}
\]

Thus the analytic numerator-difference Hankel energy is zero while the
visible all-pass Hankel energy is arbitrarily large.  The same example also
shows that multiplying a source by `D_m` places it in `ker H_{U_m}` rather
than transferring the numerator estimate to the bad model space.

## 3. Consequence for the live ninety-percent gate

The row

```text
four-channel source-density cost < 1/600
  therefore
||H_U P_T||_HS^2 < (1/600+o(1)) N
```

is invalid without a separate quotient/physical-transfer theorem.  Hence the
constant `851/15000` in `T-106430` is not presently available from
`L-106410--L-106413`.

The exact signed source/complement identity `L-106431` remains valid.  Its
correct visible term is computed directly from the Fourier coefficients of
the actual all-pass quotient in `L-106432`.  Any recovery of the former
`1/600` allowance must estimate that literal quantity, including denominator
poles, confluent blocks, finite-window seams and the physical channel map.

Neither ninety percent nor RH follows from the source-density contraction
alone.
