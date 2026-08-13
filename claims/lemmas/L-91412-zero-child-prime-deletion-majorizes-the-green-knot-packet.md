# L-91412 — The zero-child prime-deletion sector gives an exact exponentially localized lower bound for every Green knot

Claim ID: `L-91412`  
Status: **EXACT COUPLING, MOMENT, AND EXPONENTIAL-TAIL THEOREM**  
Created: 2026-08-13  
Depends on: `L-91410`; PR #396 Green-removal notation  
RH status: **unproved**

## 1. Setup

Fix

\[
0<s<1,
\qquad a=\frac s2,
\qquad c_s=\zeta(1+s)^{-1},
\qquad \kappa=\sqrt{275/14}.
\]

At the knot `t=log n`, let

\[
\mathcal P_n=\{p:p<n\},
\]

and retain the monotone base/Jordan coupling `(X,Y)` of `L-91410`, where `X` is the base logarithmic prime-exponent sum and `Y<=X` is its Jordan-thinned child.

The exact transport gain in that lemma is

\[
\mathcal G_{a,n}
=\kappa a\,\Pr(Y<t\le X)
 +4a^2\,\mathbb E[(X\wedge t)-(Y\wedge t)].
\tag{L-91412.1}
\]

Writing

\[
Z_0(n)=\prod_{p<n}(1-p^{-1}),
\qquad
P_s(n)=\prod_{p<n}(1-p^{-1-s}),
\]

`L-91410` gives

\[
B_a(\log n-)
\ge -c_s+\frac{P_s(n)}{Z_0(n)}\mathcal G_{a,n}.
\tag{L-91412.2}
\]

The present theorem extracts one exact positive sector of this gain and gives a closed exponential tail estimate.

## 2. Conditioning on the zero child

At one prime put

\[
r=p^{-1},\qquad u=p^{-s}.
\]

Under the nested activation coupling of `L-91410`,

\[
\Pr(Y_p=0)=\frac{1-r}{1-ru}.
\]

Consequently

\[
\boxed{
\Pr(Y=0)=\frac{Z_0(n)}{P_s(n)}.
}
\tag{L-91412.3}
\]

Conditioned on `Y=0`, the base exponents remain independent and have the exact law

\[
\boxed{
\Pr(E_p=0)=1-p^{-1-s},
\qquad
\Pr(E_p=k)=(1-p^{-1})p^{-s-k},\quad k\ge1.
}
\tag{L-91412.4}
\]

Indeed, conditional on the child being inactive, the parent is active with probability

\[
\frac{r-r_s}{1-r_s}=ru=p^{-1-s},
\]

and the positive exponent retains its shifted geometric law.

Define the zero-child parent logarithm

\[
\boxed{
X_{s,n}=\sum_{p<n}E_p\log p.
}
\tag{L-91412.5}
\]

Restricting (L-91412.1) to the event `Y=0` and using (L-91412.3) cancels the finite Euler normalization exactly. Therefore

\[
\boxed{
B_a(\log n-)
\ge -c_s+
\mathbb E\left[
 \frac{\kappa s}{2}\mathbf1_{X_{s,n}\ge t}
 +s^2(X_{s,n}\wedge t)
\right].
}
\tag{L-91412.6}
\]

No FKG relaxation, absolute value, or asymptotic replacement occurs in this bound.

## 3. Exact mean

The mean of the zero-child parent is

\[
\boxed{
M_s(n):=\mathbb EX_{s,n}
=\sum_{p<n}\frac{\log p}{p^s(p-1)}.
}
\tag{L-91412.7}
\]

This follows because the activation probability is `p^(-1-s)` and the conditional positive geometric exponent has mean `(1-p^(-1))^(-1)`.

The infinite real-axis source

\[
M_s(\infty)
=\sum_p\frac{\log p}{p^s(p-1)}
=\sum_{j\ge1}-P'(s+j)
\tag{L-91412.8}
\]

converges for every `s>0`. Here `P` is the prime zeta function, and the last identity is used only in its absolutely convergent real domain.

## 4. Capped-linear gain versus the full mean

Put

\[
L_s=\frac{\kappa}{2s}.
\]

For every `x>=0`,

\[
\boxed{
\frac{\kappa s}{2}\mathbf1_{x\ge t}
+s^2(x\wedge t)
\ge
s^2x-s^2(x-t-L_s)_+.
}
\tag{L-91412.9
}

For `x<t` this is equality. For `x>=t`, the left side equals `s^2(t+L_s)`; it dominates `s^2x` until `x=t+L_s` and equals the truncated right side thereafter.

Combining (L-91412.6)--(L-91412.9),

\[
\boxed{
B_a(\log n-)
\ge
-c_s+s^2M_s(n)
-s^2\mathbb E(X_{s,n}-t-L_s)_+.
}
\tag{L-91412.10}
\]

Thus the complete knot obstruction is a real-axis mean margin minus one explicit overshoot stop-loss.

## 5. Uniform moment-generating-function bound

For `0<theta<s` with `theta<=1/2`, the local moment generating function is

\[
\begin{aligned}
 m_p(\theta)
 &:=\mathbb E e^{\theta E_p\log p}\\
 &=1-p^{-1-s}
 +(1-p^{-1})p^{-s}
   \frac{p^{-(1-\theta)}}{1-p^{-(1-\theta)}}.
\end{aligned}
\tag{L-91412.11}
\]

Let `r=p^(-1)` and `q=r^(1+s-theta)`. Then

\[
m_p(\theta)-1
=q\left[
 \frac{1-r}{1-r^{1-\theta}}-r^\theta
ight].
\]

If `theta<=1/2`,

\[
\frac{1-r}{1-r^{1-\theta}}
\le1+r^\theta,
\]

because this is equivalent to `r^theta>=r^(1-theta)`. Hence

\[
0\le m_p(\theta)-1\le q
\]

and therefore

\[
\boxed{
\mathbb E e^{\theta X_{s,n}}
\le
\prod_{p<n}(1-p^{-1-s+\theta})^{-1}
\le\zeta(1+s-\theta).
}
\tag{L-91412.12}
\]

The bound is uniform in the knot and the number of active primes.

## 6. Explicit stop-loss estimate

For every nonnegative random variable `X`, every `T`, and every `theta>0`,

\[
\mathbb E(X-T)_+
\le\frac{e^{-\theta T}}{\theta}\mathbb Ee^{\theta X}.
\tag{L-91412.13}
\]

Choose `theta=s/2`. Since `0<s<1`, the hypotheses of Section 5 hold. Equations (L-91412.12)--(L-91412.13) give

\[
\boxed{
\mathbb E(X_{s,n}-t-L_s)_+
\le
\frac2s\zeta(1+s/2)
\exp\left(-\frac{st}{2}-\frac\kappa4\right).
}
\tag{L-91412.14
}

Substitution into (L-91412.10) proves the explicit knot lower bound

\[
\boxed{
B_a(\log n-)
\ge
-c_s+s^2M_s(n)
-2s\zeta(1+s/2)
 e^{-s\log n/2-\kappa/4}.
}
\tag{L-91412.15
}

## 7. Consequences

Define the finite real-axis margin

\[
\Delta_s(n)=s^2M_s(n)-c_s.
\]

Then every knot satisfying

\[
\boxed{
\Delta_s(n)
\ge
2s\zeta(1+s/2)e^{-s\log n/2-\kappa/4}
}
\tag{L-91412.16
}

is unconditionally safe.

The former compact-middle theorem involved a threshold of order `s^(-2)` from a linear FKG tail. The overshoot term here decays exponentially in `s log n`. Once the positive real-axis margin is quantified, the unresolved knot window has logarithmic length of order

\[
\frac1s\log\frac1{\Delta_s},
\]

not order `s^(-2)`.

The exact surviving one-variable real-axis problem is

\[
\boxed{
s^2\sum_p\frac{\log p}{p^s(p-1)}
>\frac1{\zeta(1+s)}
\qquad(0<s<5/12),
}
\tag{L-91412.17
}

plus an effective finite-prime tail bound. Numerical reconnaissance strongly supports (L-91412.17), but it is not asserted proved here.

## 8. Proof boundary

```text
zero-child conditional exponent law          EXACT
finite Euler normalization cancellation      EXACT
capped-linear majorization                    EXACT
uniform MGF bound by zeta                     EXACT
exponential overshoot localization            EXACT
real-axis mean margin (L-91412.17)            OPEN
all Green-removal knots                        OPEN
completed critical intertwiner                 OPEN / RH-BEARING
Riemann Hypothesis                             UNPROVED
```
