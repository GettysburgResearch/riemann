# T-106150 — Same-half-source analytic-square and reflection-signature frontier

Claim ID: `T-106150`  
Programme aliases: `LFAM1.SAME_HALF_SOURCE_FRONTIER`, `LFAM2.ANALYTIC_SQUARE_FAMILY`, `STRESS.REFLECTION_EVEN_ODD_CONJUNCTION`  
Status: **EXACT SOURCE COMPRESSION AND IMPLICATION MATRIX; ONE-SIDED ESTIMATES OPEN**  
Created: 2026-08-25  
Depends on: `L-106133--L-106134`; parent `L-102955--L-102963`, `T-102990`; repaired family frontier `T-106140`  
Programme issues: #743, #736, #737  
RH status: **unproved**

The canonical coprime two-sided Boolean incidence current of `T-102990` has
an exact one-field source normal form. This removes the separate owner-pair and
core-factor coordinates from the algebraic frontier; the remaining sign is an
analytic self-convolution/reflection-signature problem for one owner–core
half-field.

## 1. Exact derivative current

Let

\[
\mathcal J_U(X)
=\int_0^1(1-\theta)
(F_{U,\theta}*_M F_{U,\theta})(X)\,d\theta
\]

be the same-half-source field of `L-106134`. Define the fixed differential
operator

\[
\boxed{
\mathcal D_{\rm out}
=\frac12D(D-1)(5D+3/2)(2D-1).
}
\tag{T-106150.1}
\]

After exact Boolean Type-I removal, canonical equal-pair allocation, repeated
label and squared-activity removal, common-core extraction, and restoration of
the equal-core and one-sided sectors already closed by `L-102955`, the live
derivative observation has the form

\[
\boxed{
H_K^{\rm live}
=\mathcal D_{\rm out}\mathcal J_U
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
inside the half-field before the self-convolution. Equation (T-106150.2) is a
source identity, not a source-blind replacement of the physical Gram.

## 2. Direct same-field gate

Define

```text
SFSC106150:
  on every dyadic horizon, after the complete source recombination in
  L-106133--L-106134,

      integral (D_out J_U)_- dX/X = Y^o(1).
```

Then (T-106150.2)--(T-106150.3), parent `T-102990`, and the frozen derivative
Mellin consumer give

\[
\boxed{
\mathrm{SFSC}_{106150}
\Longrightarrow
\mathrm{BCI}_{102990}
\Longrightarrow
\mathrm{RH}.
}
\tag{T-106150.4}
\]

`SFSC106150` remains open and RH-bearing. It is not claimed to be easier merely
because it has one field; its advantage is that every algebraic source factor
is now explicit and repeated only once.

## 3. Reflection-even and reflection-odd conjunction

In logarithmic coordinate `x=log X`, define

\[
\begin{aligned}
\mathcal E_U(x)
&=\int_0^1(1-\theta)
\|E_xf_{U,\theta}\|_2^2\,d\theta,\\
\mathcal O_U(x)
&=\int_0^1(1-\theta)
\|O_xf_{U,\theta}\|_2^2\,d\theta,
\end{aligned}
\tag{T-106150.5}
\]

where `E_x=(I+R_x)/2` and `O_x=(I-R_x)/2`. By `L-106134.14`,

\[
\boxed{
\mathcal J_U(e^x)
=\mathcal E_U(x)-\mathcal O_U(x),
\qquad
\mathcal E_U,\mathcal O_U\ge0.
}
\tag{T-106150.6}
\]

Let the same symbol `D_out` denote the corresponding constant-coefficient
operator in `x`. The elementary inequality

\[
(A-B)_-\le A_-+B_+
\]

gives

\[
\boxed{
(\mathcal D_{\rm out}\mathcal J_U)_-
\le
(\mathcal D_{\rm out}\mathcal E_U)_-
+
(\mathcal D_{\rm out}\mathcal O_U)_+.
}
\tag{T-106150.7}
\]

Define two separate source-specific statements:

```text
REFEV106150:
  integral (D_out E_U)_- dx = Y^o(1);

REFOD106150:
  integral (D_out O_U)_+ dx = Y^o(1).
```

Neither statement alone controls the principal current. Together,

\[
\boxed{
\mathrm{REFEV}_{106150}
\wedge
\mathrm{REFOD}_{106150}
\Longrightarrow
\mathrm{SFSC}_{106150}
\Longrightarrow
\mathrm{RH}.
}
\tag{T-106150.8}

This is a genuine implication-matrix conjunction: the even reflection reserve
and odd reflection defect are different nonnegative source measurements of one
half-field.

## 4. L-family coordinate of the half-source

For every multiplicative character `chi`, twist each physical atom
`n=p a^2` in `mathfrak G_(U,theta)` by `chi(n)` and call the resulting field
`F_(U,theta,chi)`. Multiplicativity and `L-106133.12` give the exact analytic
square

\[
\boxed{
\widehat{\mathcal J_{U,\chi}}(s)
=\int_0^1(1-\theta)
\widehat F_{U,\theta,\chi}(s)^2\,d\theta.
}
\tag{T-106150.9}
\]

Thus the family programme may study a new family of **one-owner half-source
L-defects**, rather than begin with four independent owner/core variables.
The principal member is the native Boolean current. Nonprincipal members
retain the full physical character

\[
\chi(p a^2)=\chi(p)\chi(a)^2.
\]

The square in (T-106150.9) has no conjugation. Replacing it by a positive
second moment reintroduces the atomic conductor dimension corrected in
`R-106131`. The Wick-centered additive/Kummer conjunction `T-106140` is the
source-faithful way to use positive character information without that error.

Over function fields, the corresponding object is one Kummer-twisted
owner–half-core sheaf followed by an analytic square and the fixed differential
kernel. A geometric proof must still retain the cutoff-difference row of
`L-106132` and classify constant constituents before applying Deligne bounds.

## 5. Exact diagonal and residual obstacle

The half-source map

\[
(p,a)\longmapsto pa^2
\]

is injective, and `L-106133.13` proves a subpower source diagonal. Therefore the
same-field frontier contains no:

```text
equal-product representation multiplicity;
owner-pair allocation multiplicity;
complete-character atomic trace;
core-only versus physical-squareclass ambiguity.
```

What remains is the signed physical near-collision/reflection-odd component of
one half-field. It is the same arithmetic obstruction seen in the reviewed
half-divisor `HCNC` route, now attached coefficient-exactly to the canonical
Boolean/Hodge source.

## Current boundary

```text
canonical equal-pair source = Beta half-source square     PROVED EXACT
one-owner half-source physical map injective              PROVED EXACT
half-source source diagonal                               PROVED SUBPOWER
common-mother differential self-convolution               PROVED EXACT
derivative outer same-field formula                       PROVED EXACT
reflection even/odd signature                             PROVED EXACT

SFSC106150                                                 OPEN / RH-BEARING
REFEV106150                                                OPEN
REFOD106150                                                OPEN
WCADD106140 / WCKUM106140                                 OPEN / RH-BEARING
BCI102990                                                  OPEN / RH-BEARING
Riemann Hypothesis                                        UNPROVEN
```
