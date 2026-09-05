# T-106450 — Fifth-derivative endpoint signed-tail frontier for ninety percent

Claim ID: `T-106450`  
Status: **UNCONDITIONAL ENDPOINT/SOURCE REDUCTION; SIGNEDTAIL5-106450 OPEN**  
Created: 2026-08-25  
Depends on: `L-105290`, `L-106431`, `L-106450--L-106451`; the pinned fixed-order input `R_5/N>997/1000-o(1)`  
RH status: **unproved**

The two-rung endpoint `T-106430` has a signed-complement allowance
`851/15000`.  The first higher endpoint preserving an unconditional positive
exterior-square source is order five.  It gives a substantially larger
fixed-constant allowance.

## 1. One five-rung endpoint symbol

Put

\[
\Theta_{j,T}
 ={\Xi^{(j)}-i\lambda_T\Xi^{(j+1)}
   \over
   \Xi^{(j)}+i\lambda_T\Xi^{(j+1)}}
\]

on a regular dyadic window, with the exact confluent convention at common
zeros. Define

\[
\boxed{
U_{5,T}={\Theta_{0,T}\over\Theta_{5,T}}.
}
\tag{T-106450.1}
\]

All intermediate companions cancel. The all-pass winding identity gives

\[
\operatorname{wind}U_{5,T}
 =R_0(T,2T)-R_5(T,2T)+O(1).
\tag{T-106450.2}

The denominator-cancelled numerator is

\[
-2i\lambda_T
\bigl(\Xi'\Xi^{(5)}-\Xi\Xi^{(6)}\bigr),
\]

whose Fourier density is nonnegative by `L-106450`.

## 2. Visible source and signed complement

Choose

\[
L_T=\log T,
\qquad
\lambda_TL_T={1\over200},
\]

and let `P_(5,T)` be the predeclared four-channel positive/negative-frequency
Paley--Wiener source projection for the fifth endpoint.  The finite adapter is
the order-five instance of `L-106413`; the Xi Fourier tail is
superexponentially small.

Put

\[
A_{5,-}=H_{U_{5,T}}^*H_{U_{5,T}},
\qquad
A_{5,+}=H_{\overline{U_{5,T}}}^*H_{\overline{U_{5,T}}},
\]

and define the signed unobserved charge

\[
\boxed{
\Delta_{5,T}
 =\operatorname{tr}(P_{5,T}^\perp A_{5,-}P_{5,T}^\perp)
 -\operatorname{tr}(P_{5,T}^\perp A_{5,+}P_{5,T}^\perp).
}
\tag{T-106450.3}

The signed Hankel split of `L-106431` gives

\[
\boxed{
R_0(T,2T)
\ge R_5(T,2T)
 -\|H_{U_{5,T}}P_{5,T}\|_{\mathcal S_2}^2
 -(\Delta_{5,T})_+
 -o(N(T,2T)).
}
\tag{T-106450.4}

By `L-106451`, the complete visible four-channel packet obeys

\[
\boxed{
\|H_{U_{5,T}}P_{5,T}\|_{\mathcal S_2}^2
 <\left({1\over980}+o(1)\right)N(T,2T),
}
\tag{T-106450.5}

provided the declared finite bank is normalized by its literal endpoint
denominator trace.  Any failure of that cofinal normalization is retained in
`Delta_(5,T)` rather than discarded.

## 3. Exact ninety-percent threshold

The pinned unconditional fixed-order estimate is

\[
{R_5(T,2T)\over N(T,2T)}
 >{997\over1000}-o(1).
\]

After paying the safe visible source budget, the remaining margin above ninety
percent is

\[
\boxed{
{997\over1000}-{9\over10}-{1\over980}
 ={4703\over49000}
 =0.0959795918\ldots .
}
\tag{T-106450.6}

Define

```text
SIGNEDTAIL5-106450:

limsup_(T->infinity)
  (Delta_(5,T))_+ / N(T,2T)
< 4703/49000.
```

Then

\[
\boxed{
\mathrm{SIGNEDTAIL5}_{106450}
\Longrightarrow
\liminf_{T\to\infty}
{N_0(T,2T)\over N(T,2T)}>0.9.
}
\tag{T-106450.7}

This gate permits almost `9.60%` signed unobserved charge.  It is strictly
weaker numerically than the two-rung `SIGNEDTAIL106430` gate, although its
higher-order companion divisor is different.

## 4. Why this does not yet prove ninety percent

The finite source ratio controls the visible positive bank.  It does not force
large unobserved pole and zero model spaces to cancel in the signed trace.
`R-106430` remains binding.  Pointwise positivity of the exterior-square
Fourier density cannot be promoted to the all-pass index without the signed
complement theorem.

The most useful next composition is to compare the order-two and order-five
signed complements through the exact product

\[
U_{5,T}=U_{2,T}\,U_{2\to5,T}
\]

while retaining the Toeplitz--Hankel product cocycle.  A source-owned estimate
for that cocycle could combine the larger order-five reserve with the simpler
order-two endpoint source.

## 5. Boundary

```text
odd endpoint exterior-square source             PROVED UNCONDITIONALLY
fifth-endpoint four-channel ratio < 1/980        PROVED EXACT FINITE SOURCE
five-rung all-pass telescope                     PROVED EXACT
fixed signed-tail allowance 4703/49000           PROVED EXACT
SIGNEDTAIL5-106450                                OPEN / RECORD-BEARING
ninety percent for zeta                          UNPROVED
density one                                      UNPROVED
Riemann Hypothesis                               UNPROVED
```