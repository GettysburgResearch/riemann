# T-106430 — Signed Paley–Wiener complement frontier for ninety percent

Claim ID: `T-106430`  
Status: **SUPERSEDED BY T-106440; EXACT SIGNED SPLIT RETAINED, VISIBLE \(1/600\) PROMOTION UNPROVED**  
Created: 2026-08-25  
Superseded: 2026-08-25  
Depends on: `L-106400--L-106431`; binding correction `R-106432/L-106432--L-106434`  
RH status: **unproved**

## Retained theorem

`L-106431` proves the exact signed source/complement identity

\[
-\operatorname{wind}U_T
=
\mathcal V_{P_T}(U_T)+\mathcal D_{P_T}(U_T)
\]

and consequently

\[
-\operatorname{wind}U_T
\le
\|H_{U_T}P_T\|_{\mathcal S_2}^2
+
\bigl(\mathcal D_{P_T}(U_T)\bigr)_+.
\]

This part remains valid.

## Binding correction

The former display `T-106430.3`

\[
\|H_{U_T}P_T\|_{\mathcal S_2}^2
<
\left(\frac1{600}+o(1)\right)N(T,2T)
\]

was described as inherited from the four-channel endpoint source theorem.
`R-106432` proves that a source-density or denominator-cancelled numerator
estimate does not imply this actual compressed all-pass energy. `L-106434`
shows the missing factor explicitly:

\[
H_{N_T/D_T}P_T
=
H_{1/D_T}T_{N_T-D_T}P_T.
\]

The denominator inverse and the source-to-scalar-Hardy observation map were
not estimated. Therefore the former unconditional reduction to
`SIGNEDTAIL106430` is not established as written.

## Conditional constant retained

If an independent theorem proves

\[
\limsup
\frac{\|H_{U_T}P_T\|_{\mathcal S_2}^2}{N(T,2T)}
<
\frac1{600},
\]

then the signed complement threshold

\[
\limsup
\frac{\bigl(\mathcal D_{P_T}(U_T)\bigr)_+}{N(T,2T)}
<
\frac{851}{15000}
\]

does imply more than ninety percent. The implication and arithmetic constant
are correct; the visible premise is open.

The binding formulation is `T-106440`, which uses the literal hard-band
spectral energy and its explicit Cauchy--exponential divisor matrix.

```text
signed trace split                         PROVED EXACT
four-channel source-density ratio <1/600  PROVED AT SOURCE SCOPE
actual visible all-pass energy <1/600     OPEN
T-106430 unconditional reduction          SUPERSEDED
T-106440 actual spectral gate              BINDING
ninety percent / density one / RH          UNPROVED
```
