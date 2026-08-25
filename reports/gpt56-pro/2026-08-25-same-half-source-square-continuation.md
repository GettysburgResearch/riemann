# Corrected same-half-source Wick and reflection continuation

Date: 2026-08-25  
Execution PR: #751  
Programmes: #743, #736, #737  
Parent frontier: `T-102990 / BCI102990`  
Status: **exact Wick source compression; one reflection-mismatch gate remains open**

## Boolean/Wick correction

The canonical equal-pair identity is exact in disjoint-support Boolean
convolution:

\[
\mathfrak B_U^{\rm eq}
=
\int_0^1(1-\theta)
\mathfrak G_{U,\theta}\star
\mathfrak G_{U,\theta}\,d\theta.
\]

Ordinary source multiplication also contains shared-label contractions. The
binding fixture is

\[
x_p\star x_p=0,
\qquad x_p^2\ne0.
\]

After defining Wick--Mellin convolution by disjoint source supports,

\[
\mathcal O_{\Phi_*}[\mathfrak B_U^{\rm eq}]
=(2D-1)\mathcal J_U^{\diamond}.
\]

The ordinary completion satisfies

\[
\mathcal J_U=\mathcal J_U^{\diamond}+\mathcal C_U,
\]

where `mathcal C_U` contains only repeated/higher-prime-power labels and is
closed by the parent fixed-observation ledger.

## Live derivative gates

With

\[
\mathcal D_{\rm out}
=\frac12D(D-1)(5D+3/2)(2D-1),
\]

one has

```text
H_K^live=D_out J_U^diamond+H_closed
        =D_out J_U+H_tilde_closed.
```

Thus either

```text
WKSFSC106150:
  negative mass of D_out J_U^diamond is subpower;

SFSC106150:
  negative mass of D_out J_U is subpower;
```

implies `BCI102990`, with `SFSC -> WKSFSC`. Both remain open.

## Reflection complementarity

For the ordinary half-field,

\[
\mathcal J_U=\mathcal E_U-\mathcal O_U,
\qquad
\mathcal E_U+\mathcal O_U=\mathcal N_U,
\]

where `mathcal N_U` is independent of the reflection coordinate. Since
`mathcal D_out` contains `D`,

\[
\mathcal D_{\rm out}\mathcal J_U
=2\mathcal D_{\rm out}\mathcal E_U
=-2\mathcal D_{\rm out}\mathcal O_U.
\]

Therefore

\[
(\mathcal D_{\rm out}\mathcal J_U)_-
=2(\mathcal D_{\rm out}\mathcal O_U)_+.
\]

The first even/odd two-gate formulation was redundant. The single exact gate is

```text
REFSIG106150:
  integral (D_out O_U)_+ dx = Y^o(1).
```

It is equivalent to `SFSC106150` and remains open. The mismatch energy is

\[
\mathcal O_U(x)
=\frac14\int(1-\theta)
\int|f_{U,\theta}(u)-f_{U,\theta}(x-u)|^2du\,d\theta.
\]

## Family relation

Character twisting yields a Boolean-normal-ordered analytic square, not an
uncentered modulus square. The complementary family frontiers are
`CBKM106130` and the `WCADD106140 / WCKUM106140` conjunction.

## Replays

```text
PASS_X_106150_WICK_EQUAL_PAIR_HALF_SOURCE_SQUARE
checks=47263
sha256=d0cec21f67433559415ee8a62af24db4829606b87b10ed5f5933a406d8004390

PASS_X_106151_REFLECTION_COMPLEMENTARITY
checks=183600
sha256=d24b5505bd463acc7396590c8ddfe5a1fe811eb3c2d7921a37c9d98490c28183
```

No one-sided estimate or RH result is claimed.
