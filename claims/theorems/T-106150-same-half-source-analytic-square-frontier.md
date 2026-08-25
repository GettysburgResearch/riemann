# T-106150 — Corrected same-half-source Wick square and single reflection-signature frontier

Claim ID: `T-106150`  
Programme aliases: `LFAM1.SAME_HALF_SOURCE_FRONTIER`, `LFAM2.WICK_ANALYTIC_SQUARE_FAMILY`, `STRESS.REFLECTION_MISMATCH_GATE`  
Status: **CORRECTED EXACT WICK SOURCE COMPRESSION AND IMPLICATION MATRIX; ONE-SIDED ESTIMATES OPEN**  
Created: 2026-08-25  
Corrected: 2026-08-25  
Depends on: `L-106133--L-106135`; binding `R-106150`; parent `L-102955--L-102963`, `T-102990`; repaired family frontiers `T-106130`, `T-106140`  
Programme issues: #743, #736, #737  
RH status: **unproved**

The canonical coprime two-sided Boolean incidence current of `T-102990` has
an exact one-half-source normal form. The exact square is a Boolean/Wick square,
not an ordinary source square. Ordinary Mellin self-convolution supplies a
reflection-signature coordinate after its shared-label contractions are moved
to the parent’s already-closed repeated/higher-prime-power ledger.

## 1. Exact Wick derivative current

Let

\[
\mathcal J_U^{\diamond}(X)
=
\int_0^1(1-\theta)
(F_{U,\theta}\diamond_MF_{U,\theta})(X)\,d\theta
\]

be the Wick--Mellin field of `L-106134`, and define

\[
\boxed{
\mathcal D_{\rm out}
=\frac12D(D-1)(5D+3/2)(2D-1).
}
\tag{T-106150.1}
\]

After exact Boolean Type-I removal, canonical equal-pair allocation,
repeated-label and squared-activity removal, common-core extraction, and
restoration of the equal-core and one-sided sectors already closed by
`L-102955`, the live derivative observation is

\[
\boxed{
H_K^{\rm live}
=
\mathcal D_{\rm out}\mathcal J_U^{\diamond}
+H_{\rm closed},
}
\tag{T-106150.2}
\]

with

\[
\int_1^Y|H_{\rm closed}(X)|\frac{dX}{X}=Y^{o(1)}.
\tag{T-106150.3}
\]

Every carrier, endpoint-colour, marked-67, shell and incidence label remains
inside the half-source before the Wick projection.

Define

```text
WKSFSC106150:
  on every dyadic horizon,

      integral (D_out J_U^diamond)_- dX/X = Y^o(1).
```

Then

\[
\boxed{
\mathrm{WKSFSC}_{106150}
\Longrightarrow
\mathrm{BCI}_{102990}
\Longrightarrow
\mathrm{RH}.
}
\tag{T-106150.4}

`WKSFSC106150` remains open.

## 2. Ordinary self-convolution modulo closed contractions

Put

\[
\mathcal J_U(X)
=
\int_0^1(1-\theta)
(F_{U,\theta}*_MF_{U,\theta})(X)\,d\theta.
\tag{T-106150.5}
\]

`R-106150` gives

\[
\mathcal J_U
=
\mathcal J_U^{\diamond}+\mathcal C_U,
\]

where every atom of `mathcal C_U` has a repeated label of exponent at least
`2`. The parent `T-102990` ledger closes the fixed differential observation of
these repeated/higher-prime-power fields. Hence

\[
\boxed{
H_K^{\rm live}
=
\mathcal D_{\rm out}\mathcal J_U
+\widetilde H_{\rm closed},
}
\tag{T-106150.6}
\]

with

\[
\int_1^Y|\widetilde H_{\rm closed}(X)|\frac{dX}{X}=Y^{o(1)}.
\tag{T-106150.7}
\]

Define

```text
SFSC106150:
  integral (D_out J_U)_- dX/X = Y^o(1).
```

Then

\[
\boxed{
\mathrm{SFSC}_{106150}
\Longrightarrow
\mathrm{WKSFSC}_{106150}
\Longrightarrow
\mathrm{BCI}_{102990}
\Longrightarrow
\mathrm{RH}.
}
\tag{T-106150.8}

`SFSC106150` remains open.

## 3. One reflection-mismatch gate

In logarithmic coordinate `x=log X`, define

\[
\begin{aligned}
\mathcal E_U(x)
&=\int_0^1(1-\theta)
\|E_xf_{U,\theta}\|_2^2\,d\theta,\\
\mathcal O_U(x)
&=\int_0^1(1-\theta)
\|O_xf_{U,\theta}\|_2^2\,d\theta,\\
\mathcal N_U
&=\int_0^1(1-\theta)
\|f_{U,\theta}\|_2^2\,d\theta.
\end{aligned}
\tag{T-106150.9}

Here `E_x=(I+R_x)/2`, `O_x=(I-R_x)/2`, and
`R_xf(u)=f(x-u)`. By `L-106135`,

\[
\boxed{
\mathcal E_U+\mathcal O_U=\mathcal N_U,
\qquad
\mathcal J_U=\mathcal E_U-\mathcal O_U.
}
\tag{T-106150.10}
\]

The quantity `mathcal N_U` is independent of `x`. Since
`mathcal D_out` contains the factor `D`,

\[
\boxed{
\mathcal D_{\rm out}\mathcal J_U
=2\mathcal D_{\rm out}\mathcal E_U
=-2\mathcal D_{\rm out}\mathcal O_U.
}
\tag{T-106150.11}
\]

Therefore

\[
\boxed{
(\mathcal D_{\rm out}\mathcal J_U)_-
=2(\mathcal D_{\rm out}\mathcal E_U)_-
=2(\mathcal D_{\rm out}\mathcal O_U)_+.
}
\tag{T-106150.12}
\]

The first two-gate reflection formulation was redundant. Define the single
gate

```text
REFSIG106150:
  integral (D_out O_U)_+ dx = Y^o(1).
```

Equivalently one may use the negative part of `D_out E_U`. Then

\[
\boxed{
\mathrm{REFSIG}_{106150}
\Longleftrightarrow
\mathrm{SFSC}_{106150}
\Longrightarrow
\mathrm{RH}.
}
\tag{T-106150.13}

Moreover,

\[
\boxed{
\mathcal O_U(x)
=\frac14\int_0^1(1-\theta)
\int_{\mathbb R}
|f_{U,\theta}(u)-f_{U,\theta}(x-u)|^2
\,du\,d\theta.
}
\tag{T-106150.14}
\]

Thus the remaining ordinary reflection problem is the positive differential
variation of one explicit reflection-mismatch energy. `REFSIG106150` is open.

## 4. Normal-ordered L-family coordinate

For every multiplicative character `chi`, twist each physical half-source atom
`n=p a^2` by `chi(n)` and write the resulting field as
`F_(U,theta,chi)`. Multiplicativity and `L-106133` give the exact
normal-ordered analytic square

\[
\boxed{
\widehat{\mathcal J_{U,\chi}^{\diamond}}(s)
=
\int_0^1(1-\theta)
:\!\widehat F_{U,\theta,\chi}(s)^2\!:_B
\,d\theta.
}
\tag{T-106150.15}
\]

There is no complex conjugation. The Boolean normal ordering removes pairs
sharing prime labels. Replacing (T-106150.15) by an uncentered positive modulus
square reintroduces both shared-label contractions and the conductor-dimensional
atomic trace corrected by `R-106131`.

The source-faithful family coordinates remain:

```text
CBKM106130:
  connected physical-squareclass Kummer--Möbius current;

WCADD106140 AND WCKUM106140:
  Wick-centered additive and nonprincipal Kummer traces.
```

Over function fields, the correct object is a normal-ordered one-owner
half-core Kummer sheaf, or the connected two-coordinate trace of `T-106130`,
with constant constituents and shared-label contractions removed before a
family absolute value.

## 5. Exact diagonal and residual obstacle

The half-source map

\[
(p,a)\longmapsto pa^2
\]

is injective, and `L-106133` gives a subpower source diagonal. Therefore the
corrected same-field frontier contains no equal-product representation
multiplicity, owner-pair allocation multiplicity, complete-character atomic
trace, or core-only/physical-squareclass ambiguity.

The ordinary completion adds only the explicitly typed closed contraction
ledger. What remains is one signed physical near-collision/reflection-mismatch
component of one half-field.

## Current boundary

```text
canonical equal-pair source = Beta Boolean half-source square  PROVED EXACT
one-owner half-source physical map injective                    PROVED EXACT
half-source source diagonal                                    PROVED SUBPOWER
ordinary = Wick + repeated-label contractions                  PROVED EXACT
contraction observation                                        INHERITED CLOSED
common-mother differential Wick self-convolution               PROVED EXACT
reflection complementarity                                     PROVED EXACT
ordinary reflection model modulo closed contractions           PROVED EXACT

WKSFSC106150                                                    OPEN / RH-BEARING
SFSC106150                                                      OPEN / RH-BEARING
REFSIG106150                                                    OPEN / EQUIVALENT TO SFSC
CBKM106130                                                      OPEN / RH-BEARING
WCADD106140 / WCKUM106140                                      OPEN / RH-BEARING
BCI102990                                                       OPEN / RH-BEARING
Riemann Hypothesis                                             UNPROVEN
```
