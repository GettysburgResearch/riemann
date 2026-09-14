# Signed Paley–Wiener tail frontier — binding correction

The exact signed Hankel source/complement identity deposited in the original
report remains valid. Its claimed `<1/600` visible all-pass payment does not
follow from the cited four-channel source-density theorem.

The binding correction is now:

```text
R-106432  source density is not compressed all-pass energy
L-106432  exact hard-band spectral split
L-106433  Cauchy--exponential pole/zero tail matrix
L-106434  quotient transfer retains H_(1/D)
L-106435  monotone-profile safe commutator modulus
T-106440  actual spectral-tail ninety-percent frontier
```

For the literal hard band,

\[
\|H_UP_H\|_{S_2}^2
=
\int_0^\infty\min(H,r)|\widehat U(-r)|^2\,dr
\]

and

\[
\Delta_H
=
\int_H^\infty(r-H)
\left(|\widehat U(-r)|^2-|\widehat U(r)|^2\right)dr.
\]

The exact sufficient condition is

\[
\limsup
\frac{\|H_{U_T}P_{H_T}\|_{S_2}^2+(\Delta_{H_T})_+}{N(T,2T)}
<
\frac{73}{1250}.
\]

The former `851/15000` signed-tail allowance is recovered only after an
independent proof that the actual visible term is `<1/600 N`.

```text
source-density ratio <1/600             PROVED EXACT
source ratio -> actual visible energy    OPEN / REFUTED SOURCE-BLINDLY
actual spectral split                    PROVED EXACT
QUOTIENTVIS106440                        OPEN
SIGNEDTAIL106440                         OPEN
ninety percent / density one / RH        UNPROVED
```
