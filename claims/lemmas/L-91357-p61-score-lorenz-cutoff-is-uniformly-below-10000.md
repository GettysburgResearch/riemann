# L-91357 — The `P_61` score-Lorenz cutoff is uniformly below `10000`

Claim ID: `L-91357`  
Status: **PROVED EXACT FINITE-PREFIX / GLOBAL-CUTOFF THEOREM — DIRECTED REPLAY PROVIDED**  
Created: 2026-08-13  
Depends on: `L-91328`, `L-91345`, `L-91348`  
RH status: **unproved**

## 1. Causal score atoms

Let

\[
 P_{61}=\prod_{q\le61}q,
 \qquad p\ge67,
 \qquad1\le y\le67,
 \qquad x=py,
 \qquad r=p^{-1/2}.
\]

For a squarefree divisor `d|P_61`, put

\[
 K_S(d)=W_S(x,d)-rW_S(y,d),
\tag{L-91357.1}
\]

where

\[
 W_S(X,d)=\left(\frac{5\sqrt X}{d}-\frac3{\sqrt d}\right)
 \mathbf1_{d\le X}.
\tag{L-91357.2}
\]

Let `E_S` and `O_S` be the positive even- and odd-parity score measures.  The
score-Lorenz projection removes a leftmost portion of `E_S` with total mass
`|O_S|`.  Its cutoff is therefore at most a number `C` once

\[
 E_S([1,C])\ge |O_S|.
\tag{L-91357.3}
\]

## 2. Two fixed finite-prefix constants

Set

\[
 C=10000.
\]

Define

\[
 A_C=
 \sum_{\substack{d\mid P_{61}\\\mu(d)=1,\ d\le C}}\frac1d
 -
 \sum_{\substack{d\mid P_{61}\\\mu(d)=-1}}\frac1d,
\tag{L-91357.4}
\]

and

\[
 B_C=
 \sum_{\substack{d\mid P_{61}\\\mu(d)=1,\ d\le C}}\frac1{\sqrt d}
 -
 \sum_{\substack{d\mid P_{61}\\\mu(d)=-1,\ d\le C}}\frac1{\sqrt d}.
\tag{L-91357.5}
\]

The companion standard-library checker uses the exact common denominator of the
`1/d` sums and directed rational square-root enclosures.  It proves

\[
 \boxed{A_C>0}
\tag{L-91357.6}
\]

and the strict gate

\[
 \boxed{
 5\sqrt C\,A_C-3B_C-\frac{335}{\sqrt C}>0.
 }
\tag{L-91357.7}

No floating sign decision is used.

## 3. Parent score reserve at the fixed cutoff

Assume first that `x>=C`, so every even divisor `e<=C` is active.  The parent
score capacity minus all active odd demand is

\[
\begin{aligned}
 H_X^{\rm par}(C)
 ={}&
 \sum_{\substack{e\mid P_{61}\\\mu(e)=1,\ e\le C}}W_S(x,e)
 -
 \sum_{\substack{o\mid P_{61}\\\mu(o)=-1,\ o\le x}}W_S(x,o).
\end{aligned}
\tag{L-91357.8}
\]

For the reciprocal coefficient, replacing the active odd set by all odd divisors
can only decrease the expression.  For the square-root coefficient, every odd
divisor at most `C` is active, and the additional active odd terms are favorable.
Consequently

\[
 \boxed{
 H_X^{\rm par}(C)
 \ge5\sqrt x\,A_C-3B_C.
 }
\tag{L-91357.9
 }

## 4. The child subtraction is uniformly small

Because `y<=67<C`, the cutoff `C` contains every active child source.  The child
bracket is therefore the complete finite `P_61` endpoint-score forcing at `y`.
The positive-Euler-factor upper corridor of `L-91328`, interpolated to the score
parameter `5/3`, gives

\[
 0<F_S^{(61)}(y)<5\sqrt y.
\tag{L-91357.10}
\]

Hence

\[
 rF_S^{(61)}(y)
 <5r\sqrt y
 =\frac{5y}{\sqrt x}
 \le\frac{335}{\sqrt x}.
\tag{L-91357.11}
\]

Combining (L-91357.9)--(L-91357.11),

\[
\boxed{
 E_S([1,C])-|O_S|
 >5\sqrt x\,A_C-3B_C-\frac{335}{\sqrt x}.
}
\tag{L-91357.12
}

The right side is strictly increasing in `x`, because `A_C>0`.  Its minimum on
`x>=C` is the certified positive value in (L-91357.7).  Therefore

\[
 E_S([1,C])>|O_S|
 \qquad(x\ge C).
\tag{L-91357.13}

If `x<C`, every active source is already below `C`, so the cutoff bound is
trivial.

Thus in all cases

\[
\boxed{
 c_{\rm Lorenz}<10000.
}
\tag{L-91357.14
}

## 5. Consequence for literal row typing

`L-91348` reduces row subordination to the score-Lorenz cutoff determinant.  The
present theorem proves that only finitely many even `P_61` divisors below
`10000` can ever be the cutoff, independently of the unbounded rough prime
parameter.

The remaining LRPT determinant family is therefore

```text
cutoff c: even P_61 divisors c<10000;
row j:    2<=j<=66;
child y:  1<=y<=67;
rough p:  p>=67, with only analytic/asymptotic p dependence.
```

This removes the unbounded cutoff index from the first open arrow.  It does not
by itself prove the row determinant signs.

## 6. Verification

The companion replay checks all `2^18` divisor states and certifies
(L-91357.6)--(L-91357.7) by exact `Fraction` arithmetic and directed inverse
square-root bounds.

Retained verdict:

```text
PASS_P61_SCORE_LORENZ_CUTOFF_10000
```

## 7. Proof boundary

```text
finite reciprocal prefix A_C>0                  DIRECTED EXACT
finite square-root prefix enclosure              DIRECTED EXACT
uniform score reserve at C=10000                 EXACT
Lorenz cutoff c<10000                            EXACT
unbounded cutoff index                           ELIMINATED
finite row-prefix determinant family             EXPLICIT
literal row-packet typing                        OPEN / LRPT
Riemann Hypothesis                               UNPROVEN
```
