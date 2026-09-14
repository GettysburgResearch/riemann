# R-106430 — A small endpoint shift does not imply absolute Paley–Wiener coverage

Claim ID: `R-106430`  
Status: **BINDING SCOPE FIREWALL**  
Created: 2026-08-25  
Depends on: `L-106430`  
RH status: **not assumed**

Consider one reduced anti-analytic Blaschke factor with pole

\[
b=a+iy\in\mathbb C_+.
\]

Its bad model space is one-dimensional.  For the complete hard
Paley--Wiener band \([0,H]\), `L-106430` gives the exact missed trace

\[
\operatorname{tr}(I-C)=e^{-2yH}.
\]

At the live endpoint-bank scale

\[
yH=\frac1{200},
\]

one has

\[
\boxed{
\operatorname{tr}(I-C)=e^{-1/100}>\frac{99}{100}.
}
\]

Any finite source frame contained in that hard band has at least the same
missed trace.  Repeated poles have the larger confluent Laguerre deficit of
`L-106430.3`.

Therefore the implication

```text
small lambda*H
+ small denominator-cancelled four-channel numerator
-> absolute model-space coverage
```

is false in the ambient all-pass class.  The four-channel source estimate
controls the action of the Hankel operator on the declared source.  It does not
show that the source covers the complete bad model space.

This does **not** refute an Xi-specific theorem for the literal matrix
`C_T`.  It proves that such a theorem must use collective endpoint-companion
geometry, and cannot follow from the small shift or positive Fourier density
alone.

The controlling conclusion-facing replacement is the signed complement trace
of `L-106431/T-106430`.  It permits pole and zero model-space deficits to
cancel exactly, as required by the all-pass degree identity.
