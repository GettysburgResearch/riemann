# L-91308 — The phase-locked `p=2` packet is a lossless local port, not a hard-range Suzuki regularizer

Claim ID: `L-91308`  
Status: **CORRECTED / LOCAL PORT RETAINED; REGULARIZATION CLAIM REFUTED**  
Created: 2026-08-12  
Corrected: 2026-08-12  
RH status: **unproved**

## 1. Surviving local facts

Let

\[
Q_*(y)=(1-y)(1-2y)(2-y)(1-4y).
\]

The associated local Tate factor satisfies

\[
2^{2s}Q_*(2^{-s})
=16(1-2^{-s})(1-2^{-s-1})
   (1-2^{s-1})(1-2^{s-2}),
\]

or equivalently `16 A_2(s)A_2(1-s)`. It has no zero in the open critical
strip. The dyadic radial synthesis symbol

\[
G(z)=2\sqrt2-13z+11\sqrt2z^2-4z^3
\]

has a positive unit-circle lower bound, so the radial orbit is a stable Riesz
system.

These exact statements remain useful. The packet is a finite, zero-safe,
lossless local boundary port and may be Schur-eliminated from a completed
system.

## 2. Refuted claim

`R-91303` computes the leading singular coefficient of the filtered Suzuki
kernel at every odd integer:

\[
\kappa_\omega
=35+(1-2^{-2\omega})(-15\,2^\omega+2\,2^{2\omega}).
\]

For `0<omega<=1/2`,

\[
\kappa_\omega
\ge37-\frac{15}{2}\sqrt2
>\frac{103}{4}>0.
\]

Therefore the filtered kernel still has an
`(x-N)^(omega-1)` singularity at every odd integer. It is not locally `L2` in
the hard range, and the corresponding ordinary Hilbert--Schmidt/trace-class
Fredholm construction does not follow.

## 3. Corrected Suzuki route

The proper global repair is:

1. `L-91311`: deconvolve all integer singularities through the exact all-prime
   generalized-Jordan Dirichlet inverse;
2. `L-91312`: apply one Green primitive, raising the sole endpoint exponent
   from `omega-1` to `omega`;
3. build compatible finite integrated Hankel/Marchenko systems from the
   primitive kernel;
4. prove their global source/output losslessness by `OVOT_omega` or the
   minimal one-node exhaustion `ONAE_omega`;
5. retain the present `p=2` packet only as the finite local boundary port.

The fixed local packet does not replace the all-prime arithmetic operation.

## 4. Exact status

```text
open-strip local zero-safety                 EXACT
stable radial Riesz synthesis                EXACT
finite lossless p=2 boundary port            PROPOSED COMPLETE
hard-range local regularization              FALSE
all-prime deconvolution                       L-91311
one-primitive local regularization            L-91312
global integrated Marchenko losslessness      OPEN / RH-BEARING
Riemann Hypothesis                            UNPROVED
```
