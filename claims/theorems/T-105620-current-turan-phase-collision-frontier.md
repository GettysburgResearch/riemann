# T-105620 — Current–Turán hierarchy collapses the remaining source gate to physical phase collision

Claim ID: `T-105620`  
Status: **MAJOR EXACT SOURCE CLOSURE; PHYSICAL ALL-PASS TRANSFER OPEN**  
Created: 2026-08-25  
Depends on: `T-105600--T-105610`; `L-105620--L-105621`; `R-105620`; sibling PR #731  
RH status: **unproved**

## 1. The actual denominator and numerator are one hierarchy

For

\[
F=\Xi,
\qquad
\mathcal T_\Xi=\Xi'^2-\Xi\Xi'',
\qquad
J_h(a)=\Im\bigl(\Xi(a+ih)\overline{\Xi'(a+ih)}\bigr),
\]

`L-105620` proves

\[
\boxed{
\widehat J_h
=
\sum_{k=0}^\infty
{h^{2k+1}\over(2k+1)!}\Lambda_{2k+2},
\qquad
\Lambda_{2k+2}\ge0,
}
\tag{T-105620.1}
\]

with

\[
\Lambda_2=\widehat{\mathcal T_\Xi}.
\]

Hence

\[
\boxed{
\widehat J_h
\ge h\Lambda_2+{h^3\over6}\Lambda_4.
}
\tag{T-105620.2}
\]

The actual Xi denominator current is the complete positive exterior-square
chaos reservoir and the actual Turan numerator is its first chaos. No frozen
or surrogate denominator Gram remains at the diagonal source level.

## 2. Exact two-boundary source contraction

On the positive-frequency upper channel and the negative-frequency reflected
channel,

\[
\boxed{
 h e^{-h|\xi|}\Lambda_2(\xi)
\le\widehat J_h(\xi).
}
\tag{T-105620.3}
\]

Consequently every nonnegative weighted source energy contracts. In
particular, the topology-sensitive half-derivative energies satisfy

\[
\boxed{
 h^2\int_0^\infty
\xi e^{-2h\xi}\Lambda_2(\xi)^2\,d\xi
\le
\int_0^\infty\xi\widehat J_h(\xi)^2\,d\xi,
}
\tag{T-105620.4}
\]

with the reflected copy obeying the same inequality.

The following source-side rows are therefore closed exactly:

```text
actual Turan Fourier tail;
reflected actual-source tail;
source-level denominator whitening;
source-level H^(1/2) magnitude comparison;
all diagonal truncations of those rows.
```

## 3. The remaining noncommuting object

The physical differential microscope is

\[
2\mathcal C_\Xi(a,h)
=
{h\over|\Xi'|^2}
\Re\left(
\mathcal T_\Xi
{\overline{\Xi'}\over\Xi'}
\right)
-
{J_h\over|\Xi'|^2}.
\tag{T-105620.5}
\]

The variable all-pass phase

\[
\boxed{
U_h(a)={\overline{\Xi'(a+ih)}\over\Xi'(a+ih)}
}
\tag{T-105620.6}
\]

and the physical two-trace map are not diagonal in the Fourier source
coordinate. They do not commute with the canonical contraction multiplier

\[
r_h(\xi)
={h e^{-h\xi}\Lambda_2(\xi)\over\widehat J_h(\xi)}
\in[0,1].
\]

Thus the sole source-to-conclusion obstruction is now the collision of the
actual positive hierarchy with the variable all-pass phase and finite-window
endpoint geometry.

Define the reduced gate:

```text
APCX105620 — actual phase-collision transfer

Retain the canonical one-sided contraction r_h<=1 through

  multiplication by conjugate(Xi')/Xi',
  the two-boundary Toeplitz--Hankel physical map,
  denominator zero/pole and confluent seams,
  taper/finite-window endpoints,
  and cofinal regularization,

with the positive Hardy-energy compensation retained rather than discarded.
```

A pointwise realization gives `MCTPHYS105610` and RH. An integrated realization
gives a balanced shell-energy theorem.

## 4. Correction to the raw shell route

`R-105620` gives an exact real-rooted counterfamily for which every positive
height shell is empty but

\[
\sum_k\mathcal E_-(\mathcal U_k)
\]

is arbitrarily large. The raw condition `HSHE105602<2` remains a valid
sufficient theorem, but it is not a natural real-rootedness invariant and is
not the preferred standalone gate.

The exact winding identity is

\[
-\deg\mathcal U_k
=
\mathcal E_-(\mathcal U_k)
-
\mathcal E_+(\mathcal U_k).
\]

A viable integrated proof must retain a source-owned lower bound for the
positive energy or preserve the cancellation before taking negative parts.
That positive compensation is precisely what the one-sided Hardy and phase-
variance programmes supply.

The corrected integrated gate is therefore:

```text
BSHE105620 — balanced shell-energy transfer

After the actual current/Turan source contraction, prove that the all-pass
physical map preserves enough positive Hardy energy that the net negative
winding plus the single telescoped endpoint correction is below two.
```

## 5. Relation to the moving reciprocal carrier

`L-105610--L-105612` independently remove carrier freezing and prove a strict
moving-carrier one-sided reserve on far safe lines. Combining those results
with (T-105620.1)--(T-105620.4) leaves neither a frozen reciprocal source nor a
frozen Turan source:

```text
actual moving reciprocal denominator       exact positive Laplace family;
actual Xi denominator current               exact positive chaos hierarchy;
actual Xi Turan numerator                   first positive chaos;
only signed map                             physical all-pass collision.
```

## 6. Exact present implication matrix

```text
moving-carrier positive Laplace resolution             PROVED EXACT
far-safe-line moving-carrier reserve                    PROVED / REVIEW
current = all-order exterior-square hierarchy           PROVED EXACT
actual Turan = first current chaos                       PROVED EXACT
one-sided/reflected weighted source contraction         PROVED EXACT
raw negative shell energy as natural gate               REFUTED
APCX105620 physical phase-collision transfer             OPEN / RH-BEARING
BSHE105620 balanced shell transfer                       OPEN / RH-BEARING
fixed-width moving-saddle endpoint                       PROPOSED / REVIEW
Riemann Hypothesis                                       UNPROVEN
```

## 7. Scope

The theorem closes a source-normalization problem, not RH. Fourier multiplier
order is not preserved by an arbitrary variable all-pass multiplication. The
countermodel of `R-105610` remains binding. `APCX105620/BSHE105620` are the
honest surviving physical statements.
