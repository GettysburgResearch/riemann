# L-102009 — The balanced Vaughan packet factors into two explicit ratio-four fields

Claim ID: `L-102009`
Status: **PROVED EXACT SOURCE/KERNEL FACTORIZATION; TWO FIELD ENERGIES OPEN**
Created: 2026-08-21
Depends on: PR #685 `L-100310--L-100311`; `L-102002`
RH status: **not assumed**

Let `h=log 2`. In logarithmic coordinate define the positive two-box
exponential spline

\[
A(e^u)
=\int_{[0,h]^2}e^{t_1/2}
\delta(u-t_0-t_1)\,dt_0dt_1.
\tag{L-102009.1}
\]

It is nonnegative, supported on `[1,4]`, and has Mellin transform

\[
\boxed{
\widehat A(s)
=\frac{(1-2^{-s})(1-\sqrt2\,2^{-s})}
{s(s-1/2)}.
}
\tag{L-102009.2}
\]

Explicitly,

\[
A(y)=
\begin{cases}
2(\sqrt y-1),&1\le y\le2,\\
2\sqrt2-\sqrt{2y},&2\le y\le4,\\
0,&\text{otherwise}.
\end{cases}
\tag{L-102009.3}
\]

Define the two fixed ratio-four kernels

\[
A_-=(D-1/2)A,
\qquad
A_+=(D+3/2)A,
\qquad D=y\frac d{dy}.
\tag{L-102009.4}
\]

Their Mellin multipliers are `(s-1/2) Ahat(s)` and
`(s+3/2) Ahat(s)`. Therefore their Mellin convolution satisfies

\[
\boxed{K_1=A_-*_M A_+,}
\tag{L-102009.5}
\]

because the ratio-16 zero-moment kernel of `L-100310` has

\[
\widehat K_1(s)
=(s-1/2)(s+3/2)\widehat A(s)^2.
\tag{L-102009.6}
\]

The first factor is especially simple:

\[
\boxed{
A_-(y)=
\begin{cases}
1,&1<y<2,\\
-\sqrt2,&2<y<4,\\
0,&\text{otherwise},
\end{cases}}
\tag{L-102009.7}
\]

with endpoint values irrelevant to the finite sums. Thus the half-order zero
is carried entirely by one compact dyadic step field.

## Exact source factorization

Put

\[
b_U(n)=\mu(n)\mathbf1_{n>U}.
\]

Since `mu=mu_U+b_U` and `mu*1=epsilon`, the Vaughan coefficient

\[
a_U=\varepsilon-\mu_U*\mathbf1
\]

satisfies

\[
\boxed{a_U=b_U*\mathbf1.}
\tag{L-102009.8}
\]

The balanced Vaughan source is

\[
a_U*a_U*\mu.
\]

Using `1*1*mu=1`, one obtains

\[
\boxed{a_U*a_U*\mu=b_U*a_U.}
\tag{L-102009.9}
\]

Thus both the source and the kernel split into two factors.

Define the two physical fields

\[
F_{U,-}(Y)
=\sum_{d>U}\frac{\mu(d)}{\sqrt d}A_-(Y/d),
\tag{L-102009.10}
\]

and

\[
F_{U,+}(Z)
=\sum_{e\ge1}\frac{a_U(e)}{\sqrt e}A_+(Z/e).
\tag{L-102009.11}
\]

Because `a_U(e)=0` for `e<=U`, the second sum is also supported on `e>U`.
Associativity of arithmetic convolution and Mellin convolution gives the exact
identity

\[
\boxed{
\mathcal B_U(X)
=\int_0^\infty
F_{U,-}(Y)F_{U,+}(X/Y)\frac{dY}{Y}.
}
\tag{L-102009.12}
\]

No absolute value, completion inverse, or asymptotic interchange is used.
Since both kernels are supported on `[1,4]`, the integrand vanishes unless

\[
U<Y<X/U.
\]

Hence

\[
\boxed{
\mathcal B_U(X)
=\int_U^{X/U}
F_{U,-}(Y)F_{U,+}(X/Y)\frac{dY}{Y}.
}
\tag{L-102009.13}
\]

## A concrete same-occurrence AND certificate

Define

\[
\mathcal E_{U,-}(X)
=\int_U^{X/U}|F_{U,-}(Y)|^2\frac{dY}{Y},
\]

\[
\mathcal E_{U,+}(X)
=\int_U^{X/U}|F_{U,+}(Y)|^2\frac{dY}{Y}.
\]

Changing variables `Y -> X/Y` in the second factor and applying
Cauchy--Schwarz to (L-102009.13) gives

\[
\boxed{
(\mathcal B_U(X))_-^2
\le|\mathcal B_U(X)|^2
\le\mathcal E_{U,-}(X)\mathcal E_{U,+}(X).
}
\tag{L-102009.14}
\]

This is an actual product certificate on the same Vaughan occurrence. It
constructs the abstract AND-gate shape required by `L-102002`:

```text
left field:   literal large Möbius tail b_U with a zero-moment dyadic step;
right field:  divisor-completed tail a_U with the complementary ratio-four kernel;
product:      the exact balanced Vaughan packet.
```

The theorem does not prove subpower bounds for the two energies. Bounding them
by source-blind diagonals would recover the known power-loss firewalls. The new
content is the exact source-and-kernel factorization and the lossless
same-occurrence Cauchy interface.