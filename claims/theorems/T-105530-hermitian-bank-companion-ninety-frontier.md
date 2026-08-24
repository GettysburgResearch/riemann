# T-105530 — Hermitian bank plus companion-flux ninety-percent frontier

Claim ID: `T-105530`  
Status: **EXACT MODEL/FINITE-FLUX THEOREM + CONDITIONAL 90% IMPLICATION**  
Created: 2026-08-24  
Depends on: `L-105500`, `L-105522`, `L-105530`, `L-105531`  
RH status: **unproved**

## 1. What is closed

`L-105530` removes the local Hermitian source mismatch which invalidates a
single scalar Wick square.  The two-channel bank is positive for every strict
scalar contraction, cancels all Hermitian source terms through total degree
two, and differs from the identity by an explicit cubic error.

For `|z|<=1/4`, its nonzero horizontal eigenvalue is at least

\[
\kappa_0=\frac{9139}{9216}.
\tag{T-105530.1}
\]

`L-105531` converts the scalar companion Lorentz identity into a complete
matrix identity with PSD real-line bulk and one signed vertical/companion
flux.

## 2. Exact remaining conjunction

Let `d_T=(1-o(1))N_1(T,2T)` and let `G_T` be the base Gram of a source-owned
observation family.

`BANKREAL105530` is the statement that the actual folded Xi horizontal
compression is the two-channel bank of `L-105530` plus a Gram-normalized
remainder whose negative trace is `o(d_T)`, with the finite-window strip
partial indices retained rather than set to zero.

`MATRIXLERC105531` is the statement that the remaining matrix field of
`L-105531`—including nonreal/confluent pole jets, vertical sides, companion
poles, and collar exhaustion—satisfies

\[
\boxed{
\operatorname{tr}\left(
  (G_T^{-1/2}E_TG_T^{-1/2})_-
\right)
<
\left(\frac{9139}{184320}-o(1)\right)d_T.
}
\tag{T-105530.2}
\]

The constant is `kappa_0/20`.

Then `L-105522` gives

\[
\nu_+(C_T)>\left(\frac{19}{20}-o(1)\right)d_T,
\]

and the full confluent Cauchy-index identity of `L-105500` yields

\[
\boxed{
\liminf_{T\to\infty}
\frac{N_0(T,2T)}{N(T,2T)}>0.9.
}
\tag{T-105530.3}
\]

## 3. Relation to STRIPNEG105520

The new conjunction is a typed producer for the former omnibus gate:

```text
BANKREAL105530 AND MATRIXLERC105531
  -> STRIPNEG105520
  -> N0/N > 0.9.
```

It separates four issues which must not be conflated:

1. local two-boundary Hermitian source cancellation — now proved by the bank;
2. analytic strip/partial-index realization — `BANKREAL105530`;
3. cancellation of every purely holomorphic calibration — the firewall
   `R-105531`;
4. signed companion and endpoint flux — `MATRIXLERC105531`.

## 4. Boundary

```text
one-scalar Hermitian degree-two cancellation       REFUTED EXACT
minimal two-channel cancellation                   PROVED EXACT
horizontal bank positivity/cubic error             PROVED EXACT
matrix companion Lorentz identity                  PROVED EXACT FINITE-COLLAR
BANKREAL105530                                      OPEN / RECORD-BEARING
MATRIXLERC105531                                    OPEN / RECORD-BEARING
ninety percent for zeta                            UNPROVED
public record beaten                               NO
Riemann Hypothesis                                 UNPROVED
```
