# L-93885 — The prime-square occupancy moat is unconditional

Claim ID: `L-93885`  
Status: **PROPOSED COMPLETE UNCONDITIONAL ASYMPTOTIC THEOREM**  
Depends on: the elementary occupancy identity; the prime number theorem  
RH status: **unproved at this claim**

## 1. Complete and prime-only endpoints

Let

\[
F_\Lambda(X)=\sum_{q\le X}\Lambda(q)r_X(q),
\qquad
A(X)=\sum_{p\le X}(\log p)r_X(p),
\]

and

\[
H(X)=F_\Lambda(X)-A(X).
\]

For `x=e^t`, let

\[
\mathcal Q_{\rm pp}(t)
=
x^{-1/2}
\sum_{\substack{p^a\le x\\a\ge2}}
(\log p)\Delta_{p^a}(x)\ge0,
\]

where `0<=Delta_q(x)<=1` is the exact occupancy age.

## 2. Higher powers vanish

Chebyshev's elementary bound gives

\[
x^{-1/2}
\sum_{\substack{p^a\le x\\a\ge3}}\log p
\ll
x^{-1/6}+x^{-1/4}\log x=o(1).
\tag{L-93885.1}
\]

Only squares survive.

## 3. Square profile

Put `y=sqrt(x)`. Except when `[x-1,x]` contains an integer multiple of `p^2`,

\[
\Delta_{p^2}(x)=\{x/p^2\}.
\]

There are at most two exceptional integers, and

\[
\sum_{p^2\mid n}\log p\le\frac12\log n.
\]

Thus the normalized exceptional contribution is `o(1)`.

Define

\[
f(u)=\{u^{-2}\},\qquad0<u\le1.
\]

It is bounded and Riemann integrable. The weighted PNT gives

\[
\frac1y\sum_{p\le y}(\log p)f(p/y)
\longrightarrow
\int_0^1f(u)\,du.
\]

Therefore

\[
\boxed{
\mathcal Q_{\rm pp}(t)
\longrightarrow
C_{\rm pp}:=\int_0^1\{u^{-2}\}\,du.
}
\tag{L-93885.2}
\]

## 4. Evaluation and sign

With `v=u^{-2}`,

\[
C_{\rm pp}
=
\frac12\int_1^\infty\{v\}v^{-3/2}\,dv.
\]

The elementary continuation identity

\[
\zeta(s)=\frac{s}{s-1}
-s\int_1^\infty\{v\}v^{-s-1}\,dv
\qquad(0<s<1)
\]

gives

\[
\boxed{
C_{\rm pp}=-1-\zeta(1/2)>0.
}
\tag{L-93885.3}
\]

The directed enclosure

\[
-1.460355<\zeta(1/2)<-1.460354
\]

makes the strict sign explicit.

## 5. Green integration

For any finite nonnegative prime-power source, the exact one-sign-change Green
identity is

\[
-F(e^t)
=
\int_0^t\left(1-\frac{t-u}{2}\right)\mathcal Q(u)\,du.
\]

Subtracting the prime-only identity from the complete one gives

\[
-H(e^t)
=
\int_0^t\left(1-\frac{t-u}{2}\right)
\mathcal Q_{\rm pp}(u)\,du.
\]

Since `\mathcal Q_pp(u)->C_pp`, Cesàro integration gives

\[
\boxed{
H(X)
=
\frac{C_{\rm pp}}4\log^2X
+o(\log^2X).
}
\tag{L-93885.4}
\]

Hence

\[
\boxed{
A(X)
=
F_\Lambda(X)
-
\frac{C_{\rm pp}}4\log^2X
+o(\log^2X).
}
\tag{L-93885.5}
\]

No zero-free region or RH assumption enters.

## 6. Consequence of the native producer

If `F_Lambda(X)<=61000` for all sufficiently large integer `X`, then

\[
A(X)<0
\]

at all sufficiently large integers.

The source differential identity and `\psi(x)<4(\log2)x` give

\[
|A'(X)|\ll X^{-1/2}
\]

between activations; the endpoint atom activates continuously. Thus

\[
A(X)-A(\lfloor X\rfloor)=O(X^{-1/2}),
\]

and eventual negativity holds for every real `X`.

## 7. Boundary

```text
positive prime-power occupancy source        EXACT
higher powers vanish                         ELEMENTARY
square PNT limit                             UNCONDITIONAL
constant                                     -1-zeta(1/2)>0
quadratic moat                               UNCONDITIONAL
eventual prime endpoint negativity           FROM BOUNDED F_LAMBDA
Landau/Mellin exclusion                      L-93886
```
