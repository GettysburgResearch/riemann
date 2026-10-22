# L-93022 - The compact-Q4 source has a positive scale-four generalized-prime factorization

Claim ID: `L-93022`  
Status: **PROPOSED COMPLETE EXACT SOURCE FACTORIZATION - INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-16  
Depends on: `L-93019`; `T-93010`; elementary Euler products and finite Dirichlet convolution  
Scope: exact source coefficients, positive generalized primes, and source-owned endpoint fibres; no aggregate PIG estimate and no RH conclusion

## 1. The scale-four reciprocal source

Retain

\[
 B_4(s)=\frac{1-4^{1-s}}{1-4^{-s}},
 \qquad
 A_4(s)=\frac{B_4(s)}{\zeta(s)}.
 \tag{L-93022.1}
\]

Define its reciprocal

\[
 G_4(s)=\frac1{A_4(s)}
 =
 \zeta(s)\frac{1-4^{-s}}{1-4^{1-s}}.
 \tag{L-93022.2}
\]

Write

\[
 G_4(s)=\sum_{n\ge1}\frac{g_4(n)}{n^s}.
\]

Since

\[
 \frac1{1-4^{1-s}}
 =
 \sum_{r\ge0}4^r(4^r)^{-s},
\]

multiplication by \(1-4^{-s}\) telescopes along the four-adic
valuation. If \(v_2(n)\) is the exponent of two in \(n\), then

\[
 \boxed{
 g_4(n)=4^{\lfloor v_2(n)/2\rfloor}>0.
 }
 \tag{L-93022.3}
\]

Thus \(G_4\) is a literal positive Dirichlet series, and the explicit signed
coefficients \(a_4(n)\) of `L-93019` satisfy

\[
 \boxed{a_4*g_4=\varepsilon.}
 \tag{L-93022.4}
\]

This is an exact convolution inverse, not a formal asymptotic inverse.

## 2. Nonnegative generalized primes

Define the generalized von Mangoldt sequence of \(G_4\) by

\[
 -\frac{G_4'(s)}{G_4(s)}
 =
 \frac{A_4'(s)}{A_4(s)}
 =
 \sum_{n\ge1}\frac{\Lambda_4(n)}{n^s}.
 \tag{L-93022.5}
\]

At every odd prime power,

\[
 \boxed{\Lambda_4(p^k)=\log p.}
 \tag{L-93022.6}
\]

At powers of two,

\[
 \boxed{
 \Lambda_4(2^r)
 =
 \begin{cases}
 \log2,&r\text{ odd},\\
 (2^{r+1}-1)\log2,&r\text{ even}.
 \end{cases}
 }
 \tag{L-93022.7}
\]

All other coefficients vanish. In particular,

\[
 \boxed{\Lambda_4(n)\ge0.}
 \tag{L-93022.8}
\]

One direct derivation of (L-93022.7) uses \(y=2^{-s}\):

\[
 G_{4,2}(s)=\frac{1+y}{1-4y^2},
\]

so

\[
 -\frac d{ds}\log G_{4,2}(s)
 =
 (\log2)\left[
 \frac{y}{1+y}
 +
 \frac{8y^2}{1-4y^2}
 \right].
 \tag{L-93022.9}
\]

The odd coefficients come from the first series; at exponent \(2k\), the two
series give \(-1+2^{2k+1}\).

## 3. A positive two-scale source

Put

\[
 \boxed{
 \Lambda_+
 =
 (\varepsilon+2\delta_2)*\Lambda_4.
 }
 \tag{L-93022.10}
\]

Every coefficient is nonnegative. The scale-four filter factors exactly:

\[
 \varepsilon-4\delta_4
 =
 (\varepsilon-2\delta_2)*
 (\varepsilon+2\delta_2).
 \tag{L-93022.11}
\]

The compact-Q4 source of `T-93010` is

\[
 c_\circ
 =
 (\varepsilon-4\delta_4)*\Lambda_4.
 \tag{L-93022.12}
\]

Combining (L-93022.10)--(L-93022.12) gives the decisive positive
factorization

\[
 \boxed{
 c_\circ
 =
 (\varepsilon-2\delta_2)*\Lambda_+,
 \qquad
 \Lambda_+(n)\ge0.
 }
 \tag{L-93022.13}
\]

Equivalently,

\[
 \boxed{
 c_\circ(n)
 =
 \Lambda_+(n)
 -
 2\mathbf1_{2\mid n}\Lambda_+(n/2).
 }
 \tag{L-93022.14}
\]

This identity includes the complete four-adic gauge. No extra endpoint or
power-of-two correction remains outside the positive source.

For reference, away from the two-adic tower the positive source is especially
small:

```text
Lambda_+(p^k)      = log p       for odd prime powers;
Lambda_+(2 p^k)    = 2 log p     for odd prime powers p^k;
Lambda_+(2^e p^k)  = 0           for odd p and e>=2.
```

The power-of-two coefficients are also explicit and positive.

## 4. Prefix factorization

Let

\[
 \Psi_+(x)=\sum_{m\le x}\Lambda_+(m).
 \tag{L-93022.15}
\]

Then the complete compact-Q4 prefix is exactly

\[
 \boxed{
 C_\circ(x)
 =
 \Psi_+(x)-2\Psi_+(x/2).
 }
 \tag{L-93022.16}
\]

The floor in the second term is understood automatically in the finite sum.
This is a positive-source dyadic Haar difference.

The unconditional prime number theorem used in `L-93018` remains the correct
Hardy boundary input:

\[
 C_\circ(x)=o(x).
 \tag{L-93022.17}
\]

The positive factorization does not permit the boundary term in the backward
Hardy inverse to be discarded without (L-93022.17).

## 5. Source-owned endpoint fibres

For a source atom \(m\), define

\[
 h_m(x)
 =
 \mathbf1_{m\le x}
 -
 2\mathbf1_{2m\le x}.
 \tag{L-93022.18}
\]

For an endpoint \(N\) and row coordinate \(0\le j<N\), put

\[
 Z_{m,N}(j)
 =
 h_m(N)-h_m(j)-h_m(N-j-1).
 \tag{L-93022.19}
\]

Equations (L-93022.13)--(L-93022.16) give the complete row identity

\[
 \boxed{
 R_N(j)
 =
 \sum_{m\le N}\Lambda_+(m)Z_{m,N}(j).
 }
 \tag{L-93022.20}
\]

Every coefficient in (L-93022.20) is nonnegative. Every source occurrence
has one label \(m\), one scale-two Haar fibre, and one physical placement.
There is no prime-block duplication, signed source marginal, or hidden
four-adic atom.

Thus the scale-four logarithmic-derivative dictionary has been upgraded from
a formal signed coefficient identity to a **genuinely positive,
source-owned physical transfer**.

## 6. Zero safety and Mellin interface

From `L-93019`,

\[
 \sum_n\frac{c_\circ(n)}{n^s}
 =
 (1-4^{1-s})\frac{A_4'(s)}{A_4(s)}.
 \tag{L-93022.21}
\]

The finite factor \(B_4\) has zeros only on \(\Re s=1\) and poles only on
\(\Re s=0\). Hence it cannot cancel a nontrivial open-strip zero of
\(\zeta\). The positive source factorization therefore retains the exact
Mellin consumer of `T-93010/T-93011`.

What positivity does **not** do is bound the principal component of
(L-93022.20). That firewall is proved in `R-93022`.

## 7. Proof boundary

Established exactly:

1. positive coefficients \(g_4(n)\);
2. the convolution inverse \(a_4*g_4=\varepsilon\);
3. the nonnegative generalized-prime sequence \(\Lambda_4\);
4. the nonnegative two-scale source \(\Lambda_+\);
5. the coefficientwise factorization
   \(c_\circ=(\varepsilon-2\delta_2)*\Lambda_+\);
6. the exact prefix identity;
7. the source-owned endpoint-fibre decomposition;
8. compatibility with the existing Hardy and Mellin interfaces.

Open:

1. an aggregate critical-scale estimate for the fibres;
2. a square-root/polylogarithmic bound for \(M_\circ(N)\);
3. a capacity-faithful transfer of the remaining principal channel;
4. RH.
