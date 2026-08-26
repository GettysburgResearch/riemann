# T-106600 — Adaptive-scale shallow fifth-endpoint gate for more than ninety percent

Claim ID: `T-106600`  
Status: **UNCONDITIONAL INDEX/HEIGHT REDUCTION; ONE ADAPTIVE SHALLOW CORRELATION OPEN**  
Created: 2026-08-26  
Corrected: 2026-08-26  
Depends on: `L-106500`, corrected `L-106514`, `L-106591`,
`L-106600--L-106603`; pinned \(R_5/N>997/1000-o(1)\) input  
RH status: **unproved**

Let \(F=\Xi\).  On each cofinal regular window choose a source-predeclared
admissible scale \(a_T\) which is holomorphic near the contour, real and
strictly positive on the real interval, and uniformly small enough for the
Rouché exhaustion of `L-106603`.  Form

\[
U_{5,a_T}
=
\frac{(F-ia_TF')(F^{(5)}+ia_TF^{(6)})}
     {(F+ia_TF')(F^{(5)}-ia_TF^{(6)})}
\]

and reduce common factors.  Write its inner quotient as
\(B_{+,T}/B_{-,T}\).

The correction in `L-106514/L-106601` changes only the interpretation of the
phase statistic: it is a sufficient majorant, not the exact canonical charge.
The index, height split, and canonical-correlation gate below are unchanged.

## 1. Index and height are both retained

By `L-106600`,

\[
\boxed{
\operatorname{wind}U_{5,a_T}=R_0-R_5.
}
\tag{T-106600.1}
\]

By `L-106603`,

\[
\boxed{
\sum_{B_{-,T}(x+iy)=0}y
\le
\left(\frac3{4000}+o(1)\right)N(T,2T).
}
\tag{T-106600.2}
\]

Thus adaptive scaling preserves both the conclusion-facing index and the
closed macroscopic height ledger.

## 2. Correct adaptive phase majorant

Let

\[
\mathcal L_5=F'F^{(5)}-FF^{(6)}.
\]

If \(\beta_{5,a_T}'\) is the positive boundary phase density of the reduced
denominator inner factor, then corrected `L-106601` gives

\[
\boxed{
\|H_{U_{5,a_T}}\|_{\mathcal S_2}^2
\le
\frac1{\pi}\int_{\mathbb R}
\beta_{5,a_T}'(t)
\frac{a_T(t)^2\mathcal L_5(t)^2}
{(F^2+a_T^2F'^2)
 ((F^{(5)})^2+a_T^2F^{(6)2})}
\,dt.
}
\tag{T-106600.3}
\]

The Fourier transform of \(\mathcal L_5\) is the explicit nonnegative current
chaos of `L-106500`.  The displayed integral is a stronger sufficient scalar
target; it is not asserted equal to the charge.

## 3. One adaptive microscopic gate

Factor the denominator inner function at height \(\eta=1/100\):

\[
B_{-,T}=B_{-,T}^{\le1/100}B_{-,T}^{>1/100}.
\]

The deep part costs at most \(3N/40+o(N)\).  Define the exact shallow
canonical-correlation charge

\[
\mathfrak C_{\rm ash}(T)
=
\left\|
P_{K_{B_{-,T}^{\le1/100}}}T_{B_{+,T}}
\right\|_{\mathcal S_2}^2.
\]

Define `ADAPTIVESH106600` by the existence of admissible \(a_T\) such that

\[
\boxed{
\limsup_{T\to\infty}
\frac{\mathfrak C_{\rm ash}(T)+\mathcal E_{\rm reg,T}}
     {N(T,2T)}
<
\frac{11}{500}.
}
\tag{T-106600.4}
\]

Then

\[
\|H_{U_{5,a_T}}\|_{\mathcal S_2}^2
<
\left(\frac3{40}+\frac{11}{500}+o(1)\right)N
=
\left(\frac{97}{1000}+o(1)\right)N.
\]

The pinned fifth-derivative input gives

\[
\boxed{
\mathrm{ADAPTIVESH}_{106600}
\Longrightarrow
\liminf_{T\to\infty}
\frac{N_0(T,2T)}{N(T,2T)}>0.9.
}
\tag{T-106600.5}
\]

Positive constants are admissible special cases.  Therefore
`SHALLOWCORR106591` implies `ADAPTIVESH106600`; the new gate is logically no
stronger and potentially strictly weaker.

## 4. Candidate gauge and binding firewalls

`L-106602` shows that the reciprocal carrier frequency annihilates an exact
monochromatic endpoint block.  This motivates the eventual positive analytic
Riemann--Siegel phase-speed reciprocal as one concrete Xi scale, subject to
the regular-window smallness requirement.

No favorable estimate for that scale is claimed.  `R-106600` proves that
pointwise boundary alignment can coexist with a fixed unit Hankel charge
because the denominator phase measure concentrates.  `R-106640` additionally
proves that the denominator phase statistic can strictly exceed the exact
canonical charge even in a one-pole model.

```text
positive-scale endpoint homotopy                  PROVED EXACT
adaptive-scale endpoint index                     PROVED EXACT
variable-scale cofinal height <=3/4000 N           PROVED
all deep charge above height 1/100                 PAID
monochromatic reduced charge                       ZERO EXACTLY
pointwise-angle shortcut                           REFUTED EXACT
phase statistic = exact canonical charge           REFUTED
phase statistic >= exact canonical charge          PROVED
ADAPTIVESH106600 <11/500                           OPEN / 90%-BEARING
ninety percent / density one / RH                  UNPROVED
```
