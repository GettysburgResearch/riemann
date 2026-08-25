# L-106133 — The canonical equal-pair Boolean source is a Beta average of one owner–core half-source squared

Claim ID: `L-106133`  
Programme aliases: `LFAM1.EQUAL_PAIR_HALF_SOURCE`, `LFAM2.BOOLEAN_DUHAMEL_SQUARE`, `STRESS.CANONICAL_PAIR_BETA_FACTOR`  
Status: **PROVED EXACT OPERATOR-VALUED BOOLEAN SOURCE IDENTITY**  
Created: 2026-08-25  
Depends on: `L-106132`; parent `L-102746--L-102748`, `L-102952`, `L-102962--L-102963`, `T-102990`  
Programme issues: #743, #736, #737  
RH status: **not assumed**

The canonical equal-pair gauge of `T-102990` and the Boolean half-source square
of `L-106132` fit together exactly. The full balanced source is not merely a
sum over owner pairs: it is a Beta average of one combined owner–core
half-source convolved with itself.

The interpolation variable below is a combinatorial depth parameter. It is not
the complementary-temperature parameter of `L-102898`.

## 1. Operator-valued Boolean algebra

Work on one finite labelled prime set `mathcal L`; the two labelled copies of
`67` remain distinct. On a singleton label put

\[
x_p=p^{-1/2}U_p,
\qquad
y_p=p^{-1}U_{p^2}.
\tag{L-106133.1}
\]

Thus `x_p` is an unsquared owner atom and `y_p` is a completed square-core
atom. For a squarefree support `S`, write

\[
y_S=\prod_{p\in S}y_p.
\]

All products below use disjoint-support Boolean convolution `star`, so one
label can never be used simultaneously as owner and core.

Let

\[
f_U=a_U\star h,
\qquad
h(S)=(-1/2)^{|S|},
\qquad
b_U=f_U\star f_U
\tag{L-106133.2}
\]

as in `L-106132`. Define the operator-valued core half-source

\[
\mathfrak f_U(S)=f_U(S)y_S.
\tag{L-106133.3}
\]

Let `Pi` be the singleton owner source

\[
\Pi(\{p\})=x_p,
\qquad
\Pi(S)=0\quad(|S|\ne1).
\tag{L-106133.4}
\]

For `0<=theta<=1`, define the depth dilation

\[
(T_\theta F)(S)=\theta^{|S|}F(S).
\tag{L-106133.5}
\]

Because cardinalities add on disjoint unions,

\[
\boxed{
T_\theta(F\star G)
=(T_\theta F)\star(T_\theta G).
}
\tag{L-106133.6}

Put

\[
\boxed{
\mathfrak G_{U,\theta}
=\Pi\star T_\theta\mathfrak f_U.
}
\tag{L-106133.7}
\]

Every atom of `mathfrak G_(U,theta)` has the unique physical shape

\[
\boxed{n=p a^2,\qquad(p,a)=1,}
\tag{L-106133.8}
\]

with one unsquared owner and one squarefree half-core. The map `(p,a)->pa^2`
is injective because `p` is the squarefree kernel of `n`.

## 2. Exact canonical equal-pair identity

Let `S` be a labelled support of depth `k>=2`, choose an unordered owner pair
`{p,q}` inside `S`, and put

\[
C=S\setminus\{p,q\}.
\]

In

\[
\mathfrak G_{U,\theta}\star\mathfrak G_{U,\theta},
\]

the owner assignment `(p,q)` occurs in both orders. Summing all disjoint
splittings of the remaining support gives

\[
2x_px_q\,\theta^{k-2}b_U(C)y_C.
\tag{L-106133.9}
\]

The elementary Beta integral is

\[
\int_0^1(1-\theta)\theta^{k-2}\,d\theta
=\frac1{k(k-1)}.
\tag{L-106133.10}
\]

Hence the coefficient owned by `{p,q}` after integration is

\[
\frac{2}{k(k-1)}x_px_qb_U(C)y_C
=
\frac1{\binom{k}{2}}x_px_qb_U(C)y_C.
\tag{L-106133.11}
\]

This is exactly the canonical equal-pair Duhamel share of `L-102746` and
`L-102962`.

Therefore, coefficientwise in the complete labelled source algebra,

\[
\boxed{
\mathfrak B_U^{\rm eq}
=
\int_0^1(1-\theta)
\mathfrak G_{U,\theta}\star
\mathfrak G_{U,\theta}\,d\theta.
}
\tag{L-106133.12}
\]

Here `mathfrak B_U^eq` is the complete Boolean balanced source in the canonical
equal-pair gauge. A finite labelled support sees only rational Beta
coefficients, so the integral is an exact finite algebraic notation.

## 3. Owner exclusion and source functoriality

Restriction away from any finite owner, marked-prime or renewal set commutes
with:

```text
Boolean convolution;
the cutoff mu_U;
a_U;
the half-source h and f_U;
the depth dilation T_theta;
the identity L-106133.12.
```

This follows from `L-102952` and (L-106133.6). Thus the same universal
half-source is used in every legal equal-pair owner fibre; only the allowed
supports and the explicit owner atoms change.

The pair of distinct labelled copies of `67` is permitted algebraically. Its
physical repeated-prime realization remains in the inherited closed diagonal
ledger. No conclusion-bearing term is hidden there.

## 4. Source-space diagonal

If

\[
|f_U(S)|\le C^{|S|}
\]

on one finite horizon, the literal half-source coefficient diagonal satisfies

\[
\sum_{p,a}\frac{|f_U(a)|^2}{pa^2}
\le
\left(\sum_{p\le16Y}\frac1p\right)
\prod_{r\le16Y}\left(1+\frac{C^2}{r^2}\right)
=Y^{o(1)}.
\tag{L-106133.13}
\]

The divisor bound for `f_U` supplies such a fixed `C`. Because (L-106133.8) is
injective, no equal-product multiplicity occurs in this diagonal.

This is a free/source diagonal statement. It does not bound distinct physical
near-collisions after logarithmic observation.

## Meaning

The four-label Boolean incidence source has been compressed to one family of
single-owner half-fields:

```text
canonical equal-pair balanced source
  =
Beta average of
  (one owner + one Boolean half-core)
  convolved with itself.
```

The corresponding common-mother and derivative observations are calculated in
`L-106134`. The identity is exact but is not a positivity statement: a
convolution square is not an autocorrelation square.
