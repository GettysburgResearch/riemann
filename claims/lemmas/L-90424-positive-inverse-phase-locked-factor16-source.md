# L-90424 — The phase-locked factor-16 filter has a positive inverse and positive Jordan deformation

Claim ID: `L-90424`  
Title: The unique phase-locked factor-16 scalar is the own current of a zero-bare Dirichlet source with positive inverse coefficients, nonnegative generalized primes, and coefficientwise-positive Jordan ratios, up to one fixed dyadic gauge  
Status: **PROPOSED COMPLETE EXACT DIRICHLET-SOURCE THEOREM — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-11  
Dependencies: `L-90423`; elementary Euler-factor algebra  
Scope: source construction and current typing; no current upper bound, PIG estimate, or RH conclusion

## 1. Source and inverse

Let

\[
Q_*(y)=(1-y)(1-2y)(2-y)(1-4y)
\]

and define

\[
\boxed{
B_*(s)=\frac{Q_*(2^{-s})}{2\zeta(s)},
\qquad
A_*(s)=B_*(s)^{-1}
 =\frac{2\zeta(s)}{Q_*(2^{-s})}.
}
\tag{L-90424.1}
\]

Write `y=2^-s`. At every odd prime the Euler factor of `A_*` is the ordinary zeta factor. At two,

\[
\boxed{
A_{*,2}(y)
 =\frac1{(1-y)^2(1-2y)(1-y/2)(1-4y)}.
}
\tag{L-90424.2}
\]

Every factor on the right has a power series with strictly positive coefficients. Hence

\[
\boxed{a_*(n)>0\qquad(n\ge1),}
\tag{L-90424.3}
\]

where `a_*` is the coefficient sequence of `A_*`.

## 2. Nonnegative generalized primes

Let

\[
\Lambda_*(s)=-\frac{A_*'}{A_*}(s).
\]

For every odd prime power,

\[
\boxed{\Lambda_*(p^k)=\log p.}
\tag{L-90424.4}
\]

At two, logarithmic differentiation of (L-90424.2) gives

\[
\boxed{
\Lambda_*(2^k)
 =(\log2)\left(2+2^k+2^{-k}+4^k\right)>0.
}
\tag{L-90424.5}
\]

Thus the complete generalized von Mangoldt sequence is coefficientwise nonnegative.

## 3. Coefficientwise-positive Jordan path

For `tau>=0`, put

\[
J_{*,\tau}(s)=\frac{A_*(s-\tau)}{A_*(s)}.
\tag{L-90424.6}
\]

Each local geometric factor obeys

\[
\frac{1-cp^{-s}}{1-cp^{\tau-s}}
 =1+
 \frac{c(p^\tau-1)p^{-s}}
      {1-cp^{\tau-s}},
\tag{L-90424.7}
\]

whose formal Dirichlet coefficients are nonnegative. Multiplying the finitely many two-adic factors and the ordinary odd-prime factors gives

\[
\boxed{J_{*,\tau}(n)\ge0\qquad(n\ge1,\tau\ge0).}
\tag{L-90424.8}
\]

Thus every Jordan jet of this source comes from one coefficientwise-positive deformation.

## 4. Exact zero-bare collapse

Let `b_*` denote the coefficient sequence of `B_*`. Since multiplication by `zeta` is divisor-prefix convolution,

\[
\boxed{
\mathbf1*b_*
 =\delta_1-\frac{15}{2}\delta_2
  +\frac{35}{2}\delta_4
  -15\delta_8+4\delta_{16}.
}
\tag{L-90424.9}
\]

The total coefficient is zero. Therefore its ordinary prefix is identically zero above sixteen. In particular the bare carry field of `b_*` vanishes exactly whenever parent and both children are at least sixteen.

This is a genuine zero-bare source, not an asymptotic cancellation.

## 5. Own current and the ordinary factor-16 scalar

Define the own source current

\[
q_*=-b_*\log=b_* *\Lambda_*.
\tag{L-90424.10}
\]

Its divisor-prefix coefficient has Dirichlet series

\[
\begin{aligned}
\zeta(s)B_*'(s)
&=\frac12\left[
 Q_*'(2^{-s})
 +Q_*(2^{-s})
  \left(-\frac{\zeta'}{\zeta}(s)\right)
 \right].
\end{aligned}
\tag{L-90424.11}
\]

Consequently the ordinary-prime coefficient with Dirichlet series

\[
Q_*(2^{-s})\left(-\frac{\zeta'}{\zeta}(s)\right)
\]

is exactly

\[
\boxed{
2(\mathbf1*q_*)-g_*,
}
\tag{L-90424.12}
\]

where the gauge `g_*` is supported only at `2,4,8,16` and has coefficients, after factoring out `log2`,

\[
\boxed{(15,-70,90,-32).}
\tag{L-90424.13}
\]

Thus the phase-locked scalar `S_*` of `L-90423` is the physical/current output of this positive inverse system, up to one fixed finite dyadic gauge. Every fixed-row or fixed-block contribution of that gauge is bounded absolutely.

## 6. Reflected interpretation

Because the bare field vanishes in the deep balanced region, the two source-convolved individual terms in the reflected Selberg subtraction vanish there. The surviving product term is twice the normal Gram of the own current `q_*`.

This identifies the exact source to be used in any future phase-locked reflected attack:

```text
positive inverse A_*;
nonnegative generalized primes Lambda_*;
positive Jordan deformation;
zero bare field;
finite ordinary-current gauge;
critically phase-locked dyadic multiplier.
```

It does not upper-bound that positive product Gram. The latter remains the conclusion-producing arithmetic theorem.

## 7. Proof boundary

Closed exactly here:

1. positive inverse Euler factorization;
2. positive inverse coefficients;
3. explicit nonnegative generalized-prime sequence;
4. coefficientwise-positive Jordan ratios;
5. exact zero-bare source;
6. own-current/ordinary-current identity;
7. fixed finite gauge;
8. source typing for the reflected product block.

Open:

1. an upper bound for the positive current Gram;
2. critical growth of `S_*`;
3. RH.