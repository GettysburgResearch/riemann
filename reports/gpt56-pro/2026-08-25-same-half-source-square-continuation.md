# Corrected same-half-source Wick-square continuation

Date: 2026-08-25  
Execution PR: #751  
Programmes: #743, #736, #737  
Parent frontier: `T-102990 / BCI102990`  
Status: **exact Wick source compression; ordinary reflection form valid modulo inherited closed contractions; final estimates open**

## Self-audit correction

The canonical equal-pair Boolean identity

\[
\mathfrak B_U^{\rm eq}
=
\int_0^1(1-\theta)
\mathfrak G_{U,\theta}\star
\mathfrak G_{U,\theta}\,d\theta
\]

is exact. The first continuation incorrectly identified the Boolean product
`star` with ordinary source multiplication when passing to Mellin
self-convolution.

Ordinary multiplication also includes pairs of half-source atoms sharing a
prime label. A one-label fixture already gives

\[
x_p\star x_p=0,
\qquad
x_p^2=p^{-1}U_{p^2}\ne0.
\]

The binding correction is `R-106150`.

## Exact repaired field

Define the Wick--Mellin convolution by retaining only pairs with disjoint
prime-label supports. Then

\[
\mathcal J_U^{\diamond}
=
\int_0^1(1-\theta)
(F_{U,\theta}\diamond_MF_{U,\theta})\,d\theta
\]

and

\[
\mathcal O_{\Phi_*}[\mathfrak B_U^{\rm eq}]
=(2D-1)\mathcal J_U^{\diamond}.
\]

The live derivative/outer field is

\[
\frac12D(D-1)(5D+3/2)(2D-1)
\mathcal J_U^{\diamond}.
\]

## Ordinary completion and contractions

Let

\[
\mathcal J_U
=
\int_0^1(1-\theta)
(F_{U,\theta}*_MF_{U,\theta})\,d\theta.
\]

Then exactly

\[
\mathcal J_U
=
\mathcal J_U^{\diamond}+\mathcal C_U,
\]

where every term of `mathcal C_U` has a shared prime label. Such a label has
physical exponent `2`, `3`, or `4` according as it is owner/owner,
owner/core, or core/core. These are the repeated-label and
higher-prime-power source fields recorded as closed in the parent
`T-102990` ledger.

Therefore the ordinary reflection-signature model remains valid after the
fixed differential image, but only modulo this explicit closed contraction
field.

## Correct gates

```text
WKSFSC106150:
  negative mass of the exact differential Wick square is subpower;

SFSC106150:
  negative mass of the ordinary differential self-convolution is subpower;

REFEV106150:
  negative differential variation of ordinary reflection-even energy is
  subpower;

REFOD106150:
  positive differential variation of ordinary reflection-odd energy is
  subpower.
```

The exact implications are

```text
SFSC106150 -> WKSFSC106150 -> BCI102990 -> RH;

REFEV106150
AND REFOD106150
 -> SFSC106150
 -> RH.
```

All gates remain open.

## Normal-ordered family meaning

For a character twist, the exact Boolean source has the normal-ordered analytic
square

\[
\widehat{\mathcal J_{U,\chi}^{\diamond}}(s)
=
\int_0^1(1-\theta)
:\!\widehat F_{U,\theta,\chi}(s)^2\!:_B\,d\theta.
\]

There is no complex conjugation. The Boolean normal ordering removes shared
prime labels. Replacing it by an uncentered modulus square recreates the
contraction field and the character-family atomic multiplicity corrected by
`R-106131`.

The complementary family routes remain `CBKM106130` and the
`WCADD106140 / WCKUM106140` conjunction.

## Replay

```text
PASS_X_106150_WICK_EQUAL_PAIR_HALF_SOURCE_SQUARE
exact_checks=47263
proof_object_sha256=d0cec21f67433559415ee8a62af24db4829606b87b10ed5f5933a406d8004390
```

The replay checks the ordinary/Wick distinction and contraction decomposition
in addition to the retained Boolean/Beta and differential multiplier
identities. It proves none of the one-sided gates or RH.
