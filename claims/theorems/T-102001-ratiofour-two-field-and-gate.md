# T-102001 — Two ratio-four field energies jointly imply RH

Claim ID: `T-102001`
Status: **PROVED CONDITIONAL AND-GATE; BOTH FIELD-ENERGY ESTIMATES OPEN**
Created: 2026-08-21
Depends on: PR #685 `L-100310--L-100312`; `L-102009`
RH status: **unproved**

For each endpoint `X`, put

\[
U_X=\lfloor X^{1/3}\rfloor
\]

and retain the two ratio-four fields of `L-102009`:

\[
F_{X,-}(Y)
=\sum_{d>U_X}\frac{\mu(d)}{\sqrt d}A_-(Y/d),
\]

\[
F_{X,+}(Y)
=\sum_{e>U_X}\frac{a_{U_X}(e)}{\sqrt e}A_+(Y/e).
\]

Define their endpoint-local logarithmic energies

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

The exact factorization `L-102009.13` and Cauchy--Schwarz give, pointwise,

\[
\boxed{
(\mathcal B_{U_X}(X))_-^2
\le \mathcal E_-(X)\mathcal E_+(X).
}
\tag{T-102001.3}
\]

## The two hypotheses

Define the large-Möbius-tail energy condition

\[
\boxed{
\mathrm{LMTE102001}(L):
\quad
\int_{2^L}^{2^{L+1}}
\mathcal E_-(X)\frac{dX}{X}
=2^{o(L)}
}
\tag{T-102001.4}
\]

and the divisor-completed-tail energy condition

\[
\boxed{
\mathrm{DCTE102001}(L):
\quad
\int_{2^L}^{2^{L+1}}
\mathcal E_+(X)\frac{dX}{X}
=2^{o(L)}.
}
\tag{T-102001.5}
\]

If both hold, Cauchy--Schwarz in the endpoint variable yields

\[
\begin{aligned}
\int_{2^L}^{2^{L+1}}
(\mathcal B_{U_X}(X))_-\frac{dX}{X}
&\le
\left(\int_{2^L}^{2^{L+1}}\mathcal E_-(X)\frac{dX}{X}\right)^{1/2}\\
&\quad\times
\left(\int_{2^L}^{2^{L+1}}\mathcal E_+(X)\frac{dX}{X}\right)^{1/2}\\
&=2^{o(L)}.
\end{aligned}
\tag{T-102001.6}
\]

Summing logarithmic blocks gives the balanced Vaughan condition
`BVD100310`. The Type-I term has finite logarithmic mass by
`L-100310--L-100311`, and the fixed Mellin--Landau consumer of `L-100312`
therefore gives

\[
\boxed{
\mathrm{LMTE102001}
\ \wedge\ 
\mathrm{DCTE102001}
\Longrightarrow RH.
}
\tag{T-102001.7}
\]

## Why this is a genuine conjunction

The two statements are not alternate names for `BVD100310`:

```text
LMTE102001:
  the literal large Möbius tail, observed through the compact zero-moment
  dyadic step A_-;

DCTE102001:
  the divisor-completed coefficient a_U=b_U*1, observed through the
  complementary compact kernel A_+.
```

Their multiplicative convolution is exactly the balanced Vaughan packet. The
Cauchy product is taken before either field is physically collapsed into an
unsigned coefficient diagonal.

Neither energy estimate is proved here. In particular, source-blind diagonal
bounds reproduce the known critical power loss. The contribution of this
theorem is the exact construction of two different statements which together,
and through a lossless same-occurrence product, imply the conclusion.

```text
ratio-four kernel factorization          PROVED EXACT
source factorization b_U*a_U             PROVED EXACT
same-occurrence field convolution         PROVED EXACT
pointwise product certificate             PROVED EXACT
LMTE102001                                OPEN / RH-BEARING
DCTE102001                                OPEN / RH-BEARING
Riemann Hypothesis                        UNPROVED
```
