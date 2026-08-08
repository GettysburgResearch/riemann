# Full-problem continuation: the critical digital prefix bank

Date: 2026-08-08  
Branch: `agent/gpt56-pro/262-critical-euler-fiber-bridge`  
Status: **new exact critical-order mechanism; physical bank upper theorem remains open; RH unproved**

## 1. Why the proposal had to change

The latest scope review on PR #236 proves that a single finite digital prefix cannot have polylogarithmic conditioning.  At a genuine critical-line zero, the prefix symbol is already as small as

\[
R^{-1/2}(\log R)^{O(1)}
\]

in amplitude, so the squared inverse scale is \(R^{1+o(1)}\).  Any proposed polylogarithmic inverse would suppress legitimate line modes and is false at the intended source.

This does not kill the factor-five programme. It fixes the correct scale of its observability component.

## 2. Exact new mechanism

The binary-digit coefficient

\[
c_2(n)=1-v_2(n)
\]

and the opposite-parity Möbius coefficient

\[
\omega_2(n)
=
\mu(n)-\frac32\mathbf1_{2\mid n}\mu(n/2)
+rac12\mathbf1_{4\mid n}\mu(n/4)
\]

satisfy

\[
c_2*\omega_2
=
\varepsilon-\frac52\delta_2+\delta_4.
\]

For every integer \(R\ge5\), retaining **all multiplicative prefixes at once** gives

\[
\sum_{d<R}\omega_2(d)d^{-s}C_{<R/d}(s)
=1-\frac52\,2^{-s}+4^{-s}.
\]

In physical coordinates,

\[
\mathcal H
=
\sum_{d<R}\frac{\omega_2(d)}{\sqrt d}
\tau_{\log d}\mathcal A_{R/d},
\]

where

\[
\mathcal H
=I-\frac5{2\sqrt2}\tau_{\log2}
+rac12\tau_{2\log2}.
\]

The multiplier factors as

\[
(1-\sqrt2e^{-i\xi\log2})
(1-2^{-3/2}e^{-i\xi\log2}),
\]

and therefore has the uniform lower bound

\[
\kappa_*=(\sqrt2-1)(1-2^{-3/2})>0.
\]

Since

\[
\sum_{d<R}\frac{|\omega_2(d)|}{\sqrt d}\le5\sqrt R,
\]

the bank obeys the exact critical-order inequality

\[
\|f\|_2^2
\le
\frac{25}{\kappa_*^2}R
\sum_{d<R}\pi_R(d)
\|\mathcal A_{R/d}f\|_2^2.
\]

The same statement holds in \(H^1\).

This closes the **conditioning exponent** exactly at the scale required by critical-line modes. It does not rely on a bounded-rank theorem, a false Hankel cone, or a synthetic matrix.

## 3. Why this is source compatible

The synthesis weights are precisely \(\omega_2\), the source for which PR #269 proves:

- the pointwise dyadic carry wavelet;
- confinement of all potentially negative logarithmic-Kummer rows to \(2m\le n<5m\);
- a uniform carry-feature Schur reserve;
- positive generalized-prime synthesis.

Thus the digital observability bank and the factor-five carry source are not merely analogous. They are the same arithmetic source in analysis and synthesis roles.

## 4. What remains

The exact bank lower bound does not bound its observations. A full proof must assemble the complete two-frequency physical bank and prove that its weighted observation energy is controlled by:

1. the factor-five transition Gram;
2. a source-complete tempered critical-line/endpoint channel;
3. strict lower-scale outputs;

with a net reserve.

The finite-horizon commutator of every prefix is supported only in the explicit upper collar \(J\le t\le J+\log R\). Hence there is no hidden interior localization error.

The remaining production theorem is now narrower than the former generic physical-to-carry map:

```text
exact omega_2-weighted digital prefix bank
+ independent-frequency physical block
+ quotient cells 2,3,4
+ carry reserve
+ explicit collars
-> strict critical-order source recurrence.
```

## 5. Status

```text
single-prefix polylog conditioning             REFUTED by PR #236
critical-order prefix-bank algebra             PROPOSED COMPLETE
critical R observability exponent              PROPOSED COMPLETE
source compatibility with omega_2              EXACT
physical upper estimate for bank observations  OPEN / RH-BEARING
Riemann Hypothesis                             UNPROVED
```

The new exact theorem is `L-26210`; its standard-library replay is `X-26203`.
