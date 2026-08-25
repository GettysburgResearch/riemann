# T-106440 — Spectral-asymmetry × in-band-hole frontier for ninety percent

Claim ID: `T-106440`  
Status: **SUPERSEDED BY T-106450; OUTER/HOLE DECOMPOSITION RETAINED, VISIBLE \(1/600\) PREMISE OPEN**  
Created: 2026-08-25  
Superseded: 2026-08-25  
Depends on: `L-106400--L-106441`; binding correction `R-106432/L-106432--L-106434`  
RH status: **unproved**

## Retained exact result

For \(P_T\le P_{H_T}\), put \(R_T=P_{H_T}-P_T\). The signed complement of
`L-106431` splits exactly as

\[
\boxed{
\mathcal D_{P_T}(U_T)
=
\Delta_T^{\rm out}+\Delta_T^{\rm hole},
}
\]

where

\[
\Delta_T^{\rm out}
=
\|H_{U_T}P_{H_T}^\perp\|_{\mathcal S_2}^2
-
\|H_{\overline U_T}P_{H_T}^\perp\|_{\mathcal S_2}^2
\]

and

\[
\Delta_T^{\rm hole}
=
\|H_{U_T}R_T\|_{\mathcal S_2}^2
-
\|H_{\overline U_T}R_T\|_{\mathcal S_2}^2.
\]

The coarea, strip-localization, inner-sign and companion-homotopy firewalls
remain exact.

## Binding correction

The former conclusion paid the visible term by \(N/600\), citing the
four-channel source theorem. That theorem proves a diagonal source-density
ratio; it does not prove the actual scalar-Hardy compressed energy

\[
\|H_{U_T}P_T\|_{\mathcal S_2}^2.
\]

`R-106432` disproves this promotion source-blindly, and `L-106434` identifies
the missing denominator inverse. Consequently `OUTASYM106440(a)` and
`INHOLE106440(b)` imply ninety percent with \(a+b<851/15000\) only after an
independent actual-visible estimate \(<N/600\).

The binding theorem `T-106450` keeps the actual visible payment explicit:

\[
q+a+b<\frac{73}{1250}.
\]

```text
outer/HOLE signed split                    PROVED EXACT
visible source-density ratio <1/600        PROVED AT SOURCE SCOPE
actual visible H_U energy <1/600           OPEN
T-106440 unconditional 90% gate            SUPERSEDED
T-106450 actual-visible signed gate         BINDING
ninety percent / density one / RH           UNPROVED
```
