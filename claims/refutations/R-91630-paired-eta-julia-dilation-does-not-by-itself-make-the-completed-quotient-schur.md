# R-91630 — The paired-eta Julia dilation does not by itself make the completed quotient Schur

Claim ID: `R-91630`  
Status: **EXACT SOURCE-VERSUS-TRANSFER FIREWALL**  
Created: 2026-08-12  
Depends on: `L-91630/L-91631`  
RH status: **unproved**

## 1. What has been closed

`L-91630` proves the exact positive kernel identity

\[
 K_{\sigma-\omega}^{\eta}
 =K_{\sigma+\omega}^{\eta}
  +K_{\sigma,\omega}^{\eta,\rm detail}.
\]

The hard paired-eta source is therefore one safe returned source plus one
positive detail.  The previously noted same-space inverse is unnecessary.

## 2. Why this is not yet the completed transfer theorem

The completed analytic quotient contains

\[
 \frac{I_\eta(s-\omega)}{I_\eta(s+\omega)}.
\]

A positive kernel decomposition of numerator and denominator source Grams does
not imply that this scalar quotient is Schur.  Indeed, on the positive real
axis,

\[
 I_\eta(\sigma-\omega)>I_\eta(\sigma+\omega),
\]

so the quotient is larger than one.

The correct interpretation is a source norm ledger:

```text
hard source norm
 = safe returned norm
 + eta-detail norm.
```

It is not a contractive multiplier assertion for the ratio.

## 3. Products of positive source kernels do not identify model outputs

`L-91631` gives positive carrier sources for the eta detail and gamma factor,
a lossless rational factor, and a compact bridge.  Tensoring these sources
produces a positive arithmetic Gram.

But a positive arithmetic Gram can still decompose as

\[
 K^{\rm arith}
 =K^{\rm crit}+K^{\rm st}+K^{\rm hyp}+K^{\rm aux}
\]

with nonzero positive `K_hyp` and `K_aux`.  Positivity of the source alone does
not exhaust it by the first two model outputs.

## 4. Corrected obstruction

The paired-eta tail is no longer an unbounded source problem.  The only
remaining conclusion-producing joint is the canonical source-to-model
identification and exhaustion:

```text
explicit positive eta/bridge/gamma source
    -> critical output
     + stable output
     + hyperbolic output
     + auxiliary output;

source norm = critical norm + stable norm.
```

An arbitrary isometry between equal-dimensional or equal-norm spaces is not
sufficient.  The analytic factors of `L-91631` must be retained with
coefficient one.

## 5. Exact boundary

```text
same-space eta inverse unbounded                 TRUE BUT NONBLOCKING
weighted sector-changing eta unitary             EXACT
eta source Julia detail                          EXACT POSITIVE
completed eta quotient Schur                     NOT IMPLIED
positive arithmetic source -> model exhaustion   OPEN / RH-BEARING
Riemann Hypothesis                               UNPROVED
```
