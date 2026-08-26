# L-102893 — A positive square-lattice inverse recovers the native detector from the midpoint square

Claim ID: `L-102893`  
Status: **PROVED EXACT POSITIVE-TRANSFER IMPLICATION**  
Created: 2026-08-24  
Depends on: `L-102892`; PR #715 fixed common-mother consumer  
RH status: **not assumed**

Retain

\[
\eta*\eta=\beta*\beta^\square
\]

from `L-102892`.  Define the nonnegative arithmetic function \(\omega\) by

\[
\boxed{
\sum_{d\ge1}\frac{\omega(d)}{d^z}
=
\frac{\zeta(2z)}{1-67^{-2z}}.
}
\tag{L-102893.1}
\]

Equivalently,

\[
\omega
=
\left(\beta^\square\right)^{-1}
\]

in the labelled convolution algebra after physical collapse.  Its coefficients
are nonnegative: (L-102893.1) is the product of the square-indicator series
\(\zeta(2z)\) and the geometric series in \(67^{-2z}\).

Therefore

\[
\boxed{
\omega*(\eta*\eta)=\beta.
}
\tag{L-102893.2}
\]

## 1. Exact observation identity

Define the fixed outer observations

\[
\mathscr S_\eta(X)
=
\sum_n\frac{(\eta*\eta)(n)}{\sqrt n}R_L(X/n),
\]

\[
H_\beta(X)
=
\sum_n\frac{\beta(n)}{\sqrt n}R_L(X/n).
\]

Finite arithmetic Fubini applied to (L-102893.2) gives

\[
\boxed{
H_\beta(X)
=
\sum_d\frac{\omega(d)}{\sqrt d}
\mathscr S_\eta(X/d).
}
\tag{L-102893.3}
\]

The kernel, source normalization and detector are fixed; no endpoint-dependent
multiplier is introduced.

## 2. Polylogarithmic positive inverse mass

From (L-102893.1),

\[
\sum_{d\le Y}\frac{\omega(d)}{\sqrt d}
\le
\sum_{k\ge0}\frac1{67^k}
\sum_{m\le\sqrt Y/67^k}\frac1m.
\]

Hence

\[
\boxed{
\sum_{d\le Y}\frac{\omega(d)}{\sqrt d}
\ll\log(2Y).
}
\tag{L-102893.4}
\]

All weights in (L-102893.3) are nonnegative.  Therefore

\[
(H_\beta(X))_-
\le
\sum_d\frac{\omega(d)}{\sqrt d}
(\mathscr S_\eta(X/d))_-.
\]

Integrating and changing variables gives

\[
\boxed{
\int_1^Y(H_\beta(X))_-\frac{dX}{X}
\ll
\log(2Y)
\int_1^Y(\mathscr S_\eta(X))_-\frac{dX}{X}.
}
\tag{L-102893.5}
\]

The upper limit on the right may be used because the negative-mass integral is
monotone in its horizon.

## 3. New sufficient criterion

Define

```text
GMBC102893:
  the arithmetic geometric-midpoint square observation S_eta has subpower
  logarithmic negative mass in the fixed outer kernel R_L.
```

Then (L-102893.5) gives

\[
\boxed{
\mathrm{GMBC}_{102893}
\Longrightarrow
\int_1^Y(H_\beta)_-\frac{dX}{X}=Y^{o(1)}.
}
\tag{L-102893.6}

The fixed common-mother/outer-ray Mellin–Landau consumer on PR #719 therefore
gives

\[
\boxed{
\mathrm{GMBC}_{102893}\Longrightarrow\mathrm{RH}.
}
\tag{L-102893.7}

## Scope firewall

Although the half-source observation \(H_\eta\) is eventually positive by
`L-102892`, \(\mathscr S_\eta\) is an arithmetic **source-convolution square**
under the signed fixed kernel \(R_L\).  It is not the pointwise square
\(H_\eta^2\), and its negative mass is not controlled by the tail sign of
\(H_\eta\) alone.

Thus the theorem creates a new positive-inverse route to RH but does not prove
`GMBC102893`.
