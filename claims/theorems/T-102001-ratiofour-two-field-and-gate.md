# T-102001 — Ratio-four factorization and the symmetric one-field energy gate

Claim ID: `T-102001`
Status: **PROVED CONDITIONAL COMPOSITIONS; ONE LOCAL FIELD ENERGY OPEN**
Created: 2026-08-21
Audited: 2026-08-21
Depends on: PR #685 `L-100310--L-100312`; `L-102009--L-102010`
RH status: **unproved**

For each endpoint `X`, put

\[
U_X=\lfloor X^{1/3}\rfloor.
\]

## The exact two-field factorization

Retain the two ratio-four fields of `L-102009`:

\[
F_{X,-}(Y)
=\sum_{d>U_X}\frac{\mu(d)}{\sqrt d}A_-(Y/d),
\]

\[
F_{X,+}(Y)
=\sum_{e>U_X}\frac{a_{U_X}(e)}{\sqrt e}A_+(Y/e).
\]

Define

\[
\mathcal E_-(X)
=\int_{U_X}^{X/U_X}|F_{X,-}(Y)|^2\frac{dY}{Y},
\tag{T-102001.1}
\]

\[
\mathcal E_+(X)
=\int_{U_X}^{X/U_X}|F_{X,+}(Y)|^2\frac{dY}{Y}.
\tag{T-102001.2}
\]

The exact factorization `L-102009.13` and Cauchy--Schwarz give

\[
\boxed{
(\mathcal B_{U_X}(X))_-^2
\le \mathcal E_-(X)\mathcal E_+(X).
}
\tag{T-102001.3}
\]

Consequently the two block-energy conditions

\[
\int_{2^L}^{2^{L+1}}\mathcal E_-(X)\frac{dX}{X}=2^{o(L)},
\tag{LMTE102001}
\]

and

\[
\int_{2^L}^{2^{L+1}}\mathcal E_+(X)\frac{dX}{X}=2^{o(L)}
\tag{DCTE102001}
\]

jointly imply `BVD100310`, and hence RH through `L-100310--L-100312`.

## Symmetric half-divisor reduction

`L-102010` goes further. Let the nonnegative multiplicative function `eta`
satisfy

\[
\eta*\eta=\mathbf1
\]

and put

\[
h_U=(\mu\mathbf1_{>U})*\eta.
\]

Then the balanced Vaughan source is the exact square

\[
a_U*a_U*\mu=h_U*h_U.
\]

For the corresponding ratio-four minus field

\[
H_{U,-}(Y)=
\sum_n\frac{h_U(n)}{\sqrt n}A_-(Y/n),
\]

define

\[
\mathcal H_U(X)
=\int_U^{4X/U}|H_{U,-}(Y)|^2\frac{dY}{Y}.
\tag{T-102001.4}
\]

The exact Hardy relation between `A_+` and `A_-` has sharp `L2` norm three,
and `L-102010` proves

\[
\boxed{
|\mathcal B_U(X)|\le3\mathcal H_U(X).
}
\tag{T-102001.5}
\]

Therefore the single block condition

\[
\boxed{
\mathrm{HHFE102010}(L):
\quad
\int_{2^L}^{2^{L+1}}
\mathcal H_{U_X}(X)\frac{dX}{X}=2^{o(L)}
}
\tag{T-102001.6}
\]

implies `BVD100310`, then RH.

\[
\boxed{\mathrm{HHFE102010}\Longrightarrow RH.}
\tag{T-102001.7}
\]

## Exact meaning

The initial implication-matrix goal asked for two different statements which
work only together. `L-102009` constructs that conjunction exactly:

```text
large Möbius tail through A_-
  x
positive divisor-completed tail through A_+
  -> balanced Vaughan packet.
```

The positive half-divisor square root then reveals that these two sides are
not independent conjectures: they are two Hardy-related observations of one
source `h_U`. The strongest current frontier is therefore one explicit local
field energy, not two undefined collar certificates.

No unconditional estimate for `HHFE102010` is proved here. Source-blind
diagonal bounds still lose a power, and the field retains the signed
half-order arithmetic required by the reciprocal-zeta detector.

```text
ratio-four kernel factorization             PROVED EXACT
balanced source factorization b_U*a_U       PROVED EXACT
same-occurrence two-field Cauchy gate        PROVED EXACT
positive half-divisor square root            PROVED EXACT
sharp Hardy reduction to one field          PROVED EXACT
HHFE102010                                   OPEN / RH-BEARING
Riemann Hypothesis                           UNPROVED
```
