# Same-half-source square continuation

Date: 2026-08-25  
Execution PR: #751  
Programmes: #743, #736, #737  
Parent frontier: `T-102990 / BCI102990`  
Status: **exact source compression; final one-sided estimates open**

## Main result

The canonical equal-pair Boolean balanced source has the exact form

\[
\mathfrak B_U^{\rm eq}
=
\int_0^1(1-\theta)
\mathfrak G_{U,\theta}^{\star2}
\,d\theta,
\]

where `mathfrak G_(U,theta)` is one combined source containing:

```text
one unsquared owner prime;
one Boolean half-core;
the exact depth weight theta^|core|.
```

The Beta coefficient

\[
2\int_0^1(1-\theta)\theta^{k-2}d\theta
=\binom{k}{2}^{-1}
\]

is exactly the canonical equal-pair Duhamel share.

One half-source atom has the unique physical form

\[
n=p a^2,
\]

so the map `(p,a)->n` is injective and its source diagonal is subpower.

## Common-mother compression

Let

\[
F_{U,\theta}=\mathcal O_A[\mathfrak G_{U,\theta}],
\qquad
\mathcal J_U
=
\int_0^1(1-\theta)
(F_{U,\theta}*_M F_{U,\theta})d\theta.
\]

Using

\[
\Phi_*=2(D-1/2)A*_M A,
\]

one obtains

\[
\mathcal O_{\Phi_*}[\mathfrak B_U^{\rm eq}]
=(2D-1)\mathcal J_U.
\]

The live derivative/outer observation is

\[
\frac12D(D-1)(5D+3/2)(2D-1)\mathcal J_U.
\]

The factor is `2D-1`, not `D-1`: a derivative of a convolution equals the
derivative on either factor, not the sum of derivatives on both factors.

## Reflection signature

For the real principal half-field,

\[
(F*_MF)(e^x)
=\|E_xf\|_2^2-\|O_xf\|_2^2.
\]

Thus the final sign is a reflection-even reserve minus a reflection-odd defect
of one field. The exact sufficient conjunction is

```text
REFEV106150:
  negative differential variation of the even energy is subpower;

REFOD106150:
  positive differential variation of the odd energy is subpower.
```

Together they imply `SFSC106150`, then `BCI102990`, then RH. All remain open.

## L-family meaning

Every character twist also has an analytic-square form

\[
\widehat{\mathcal J_{U,\chi}}(s)
=
\int_0^1(1-\theta)
\widehat F_{U,\theta,\chi}(s)^2d\theta.
\]

The square is not a modulus square. A positive second moment must use the
Wick-centered repair of `T-106140`; otherwise the conductor-dimensional atomic
trace reappears.

## Replay

```text
PASS_X_106150_EQUAL_PAIR_HALF_SOURCE_SQUARE
exact_checks=24146
proof_object_sha256=4890064413d40fb6a9a1fe2bb1523b8271e217fca166c6d4883f1acf4f42a3b6
```

RH remains unproved.
