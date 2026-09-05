# R-106432 — A source-density contraction is not a compressed all-pass Hankel estimate

Claim ID: `R-106432`  
Status: **PROVED EXACT FIREWALL; BINDS T-106430.3**  
Created: 2026-08-25  
Depends on: `R-106420`; sibling PR #729 `L-105621/T-105620`  
RH status: **not assumed**

## 1. Exact finite counterfamily

On the unit circle fix integers \(m,d\ge1\) and put

\[
N_m(z)=1,\qquad D_m(z)=z^m,\qquad U_m(z)=\frac{N_m(z)}{D_m(z)}=z^{-m}.
\]

Let \(P_d\) be the Hardy projection onto

\[
\mathcal S_d=\operatorname{span}\{1,z,\ldots,z^{d-1}\}.
\]

The denominator-cancelled difference \(N_m-D_m=1-z^m\) is analytic, so

\[
\boxed{\|H_{N_m-D_m}P_d\|_{\mathcal S_2}^2=0.}
\tag{R-106432.1}
\]

By contrast, the actual all-pass Hankel matrix has a one on each anti-diagonal
entry \(j+k+1=m\). Hence

\[
\boxed{\|H_{U_m}P_d\|_{\mathcal S_2}^2=\min(m,d).}
\tag{R-106432.2}
\]

The discrepancy is arbitrarily large. Therefore no source-blind constant
\(C\) can justify

\[
\|H_UP\|_{\mathcal S_2}^2
\le C\,\|H_{N-D}P\|_{\mathcal S_2}^2
\]

for reduced all-pass quotients \(U=N/D\).

## 2. Consequence for the live endpoint packet

`L-106410--L-106413` prove exact inequalities between positive
**source densities** before the physical quotient map. Their replay verifies
those density inequalities and rational constants. They do not evaluate the
Fourier coefficients of \(U=N/D\), nor the compressed operator \(H_UP_T\).

Thus the displayed assertion

\[
\|H_{U_T}P_T\|_{\mathcal S_2}^2
<\left(\frac1{600}+o(1)\right)N(T,2T)
\]

in `T-106430.3` is not inherited from the four-channel source theorem.

This agrees with sibling PR #729: `L-105621/T-105620` explicitly close the
diagonal current--Turán source contraction while retaining the variable
all-pass/physical map as the open phase-collision interface.

## 3. What survives

The following remain valid.

```text
four-channel density ratio < 1/600       PROVED AT SOURCE SCOPE
signed source/complement trace split      PROVED EXACT
confluent Paley--Wiener deficit formula   PROVED EXACT
```

To recover the numerical `851/15000` signed-tail threshold, one must separately
prove an actual quotient/observation theorem giving the \(1/600\) bound for
\(\|H_{U_T}P_T\|_{\mathcal S_2}^2\). That theorem is not supplied by analytic
denominator cancellation.
