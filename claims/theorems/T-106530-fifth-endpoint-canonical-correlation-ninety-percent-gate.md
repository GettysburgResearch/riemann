# T-106530 — Fifth-endpoint canonical-correlation gate for more than ninety percent

Claim ID: `T-106530`  
Status: **UNCONDITIONAL EXACT REDUCTION; ONE EXPLICIT Cauchy-GRAM DEFICIT OPEN**  
Created: 2026-08-25  
Depends on: `L-106500`, `L-106501`, `L-106512`; the pinned `R_5/N>997/1000-o(1)` input  
RH status: **unproved**

For the reduced fifth-endpoint quotient

\[
U_T={B_{+,T}\over B_{-,T}},
\]

let

\[
m_{-,T}=\deg B_{-,T}
\]

and let `G_-(T),G_+(T),C(T)` be the confluent normalized Cauchy Grams of the
two upper companion divisors, as in `L-106512`.

## 1. Exact adverse charge

`L-106512` gives

\[
\boxed{
\|H_{U_T}\|_{\mathcal S_2}^2
=m_{-,T}
-\left\|G_-(T)^{-1/2}C(T)G_+(T)^{-1/2}\right\|_{\mathrm F}^2.
}
\tag{T-106530.1)

The second term is the total squared canonical correlation between the
numerator and denominator companion model spaces.  Every favorable inner
direction is removed automatically.

## 2. Exact sufficient condition

Define `CANONCORR106530` by

\[
\boxed{
\limsup_{T\to\infty}{1\over N(T,2T)}
\left[
 m_{-,T}
-\left\|G_-^{-1/2}CG_+^{-1/2}\right\|_{\mathrm F}^2
+\mathcal E_{\rm end,T}
\right]
< {97\over1000},
}
\tag{T-106530.2)

where `E_end,T` is the literal common-zero, confluent, finite-window and
cofinal-exhaustion ledger.

The odd endpoint index identity and

\[
\liminf {R_5(T,2T)\over N(T,2T)}>{997\over1000}
\]

then imply

\[
\boxed{
\mathrm{CANONCORR}_{106530}
\Longrightarrow
\liminf_{T\to\infty}{N_0(T,2T)\over N(T,2T)}>0.9.
}
\tag{T-106530.3)

## 3. Why this is the sharp surviving target

```text
raw source-density contraction             insufficient by R-106432;
complete denominator cancellation           forbidden by R-106417;
radial source filter = input multiplier      forbidden by R-106508;
outer Dirichlet defect                       valid but may pay favorable degree;
canonical-correlation deficit                exact adverse Hankel charge.
```

The matrices in (T-106530.1)--(T-106530.2) have explicit entries

\[
{2\sqrt{yy'}\over y+y'+i(a-a')}
\]

and their confluent derivatives.  No unidentified operator norm or source
dimension remains.

## 4. Boundary

```text
fifth endpoint telescope                       PROVED EXACT
positive fifth Wronskian/current hierarchy      PROVED EXACT
exact model-space Cauchy Grams                  PROVED EXACT
adverse charge = canonical-correlation deficit  PROVED EXACT
fixed allowance 97/1000                        PROVED EXACT
CANONCORR106530                                 OPEN / RECORD-BEARING
ninety percent for zeta                        UNPROVED
Riemann Hypothesis                             UNPROVED
```
