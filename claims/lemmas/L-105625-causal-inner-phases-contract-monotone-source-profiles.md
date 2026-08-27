# L-105625 — Causal inner phases contract every monotone source profile

Claim ID: `L-105625`  
Status: **PROVED EXACT ABSTRACT HARDY-SPACE THEOREM**  
Created: 2026-08-25  
Depends on: `L-105421--L-105422`; `L-105623--L-105624`  
RH status: **not assumed**

## 1. Causal isometries

Work on

\[
\mathcal H=L^2(0,\infty).
\]

Let `P_T` denote multiplication by `1_(0,T)`. An operator `V` is called a
causal isometry if

\[
V^*V=I
\]

and

\[
\boxed{P_TV=P_TVP_T\qquad(T>0).}
\tag{L-105625.1}
\]

Under the Paley--Wiener transform, multiplication by an inner function in the
upper half-plane is a causal isometry.

Equation (L-105625.1) immediately gives the prefix-energy inequality

\[
\boxed{
\int_0^T|(Vf)(\xi)|^2d\xi
\le
\int_0^T|f(\xi)|^2d\xi.
}
\tag{L-105625.2}
\]

## 2. Every decreasing weight contracts

Let

\[
r:[0,\infty)\to[0,\infty)
\]

be bounded, right-continuous and nonincreasing, and let `R=M_r`.
Write

\[
r(t)=r_\infty+\nu((t,\infty))
\]

for the positive Stieltjes measure `nu=-dr`. Layer-cake integration gives

\[
\begin{aligned}
\langle Rf,f\rangle
={}&r_\infty\|f\|^2
+\int_0^\infty
\left(\int_0^T|f(\xi)|^2d\xi\right)d\nu(T).
\end{aligned}
\tag{L-105625.3}
\]

Using (L-105625.2) inside this positive integral yields

\[
\boxed{
V^*RV\preceq R.
}
\tag{L-105625.4}
\]

Thus a causal inner phase can only move source energy toward later frequencies,
where every decreasing diagonal profile assigns no larger weight.

No smoothness or strict monotonicity of `r` is required.

## 3. Quantitative loss identity

The exact weighted loss is

\[
\boxed{
\begin{aligned}
\langle(R-V^*RV)f,f\rangle
=
\int_0^\infty
\left[
\int_0^T|f|^2
-
\int_0^T|Vf|^2
\right]d\nu(T)
\ge0.
\end{aligned}
}
\tag{L-105625.5}
\]

This identifies the reserve as the cumulative energy delayed across every
source cutoff. It is the causal version of the one-sided numerical-radius gap
of `L-105421--L-105422`.

If `r` is strictly decreasing on a set of positive Stieltjes measure, equality
requires equality in every corresponding prefix contraction. For a nonconstant
inner phase and a nonzero generic source vector, the inequality is strict.

## 4. Fourier commutator consequence

Equation (L-105625.4) may be rewritten as

\[
\boxed{
R^{1/2}V^*VR^{1/2}
-
R^{1/2}V^*RVR^{1/2}
\succeq0,
}
\]

or, more transparently,

\[
\|R^{1/2}Vf\|
\le
\|R^{1/2}f\|.
\tag{L-105625.6}
\]

This supplies the sign which an arbitrary-unitary commutator estimate in
`L-105623` lacks. Once the physical phase is authenticated as inner/causal and
the canonical profile is decreasing, the all-pass collision is favorable in
the one-sided weighted energy.

## 5. Current–Turán application

Assume the source hypotheses of `L-105624`, so

\[
r_h(\xi)
={h e^{-h\xi}\Lambda_2(\xi)\over j_h(\xi)}
\]

is nonincreasing. Let the shifted derivative denominator be zero-free in the
open upper half-plane, so its boundary all-pass quotient defines a causal inner
isometry `V_h`. Then

\[
\boxed{
V_h^*M_{r_h}V_h\preceq M_{r_h}.
}
\tag{L-105625.7}
\]

Thus the all-pass phase cannot amplify the canonical current-normalized Turan
source in the one-sided energy coordinate.

This proves the **infinite-line causal phase part** of `PCC105623` under two
explicit source/interface hypotheses:

```text
LC:  the Fourier source is even and log-concave;
IN:  the physical derivative all-pass is represented by the corresponding
     causal inner multiplier on the exact one-sided source space.
```

## 6. Xi consumption boundary

`L-105626` proves `LC` for the standard base-Xi Fourier kernel without
consuming an external log-concavity claim. `L-105627`, specialized to the base
rung, proves `IN` for the extremal Xi-prime all-pass. Their exact conclusion is
recorded in `L-105628`.

The abstract theorem does not extend that conclusion to arbitrary derivative
rungs whose full-line Fourier sources are no longer the same nonnegative even
kernel. Nor does it identify finite zero-count banks or endpoint charges. RH
remains unproved.
