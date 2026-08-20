# Critical Taylor renormalization at the native half-order boundary

## Status

This manuscript proves a global family of native-source positivity theorems and
an exact critical reduction. It does **not** prove the final critical sign and
does not establish the Riemann Hypothesis.

## 1. Native duplicate-67 source

Let

\[
\beta(n)=\mu(n)-\mathbf1_{67\mid n}\mu(n/67).
\]

Equivalently, use one labelled copy of every prime and a second labelled copy
of `67`. Inclusion–exclusion over label subsets projects to the exact local
factor

\[
(1-x)^2=1-2x+x^2
\]

at `67` and to `1-x` at every other prime.

Define the activation-zero SHARP carrier

\[
S(y)=4(\sqrt y-1)\mathbf1_{y\ge1}.
\]

For real `m>=2`, put

\[
G_m(X)=\sum_n\frac{\beta(n)}{\sqrt n}S(X/n)^m.
\]

At fixed `X` the sum is finite.

## 2. Global supercritical positivity

For a labelled subset `A`, set

\[
w_m(A)=n_A^{-1/2}S(X/n_A)^m.
\]

If a label `q` is removed from an active set, then

\[
\frac{w_m(A)}{w_m(A\setminus\{q\})}
<q^{-(m+1)/2}.
\]

At `m=2`, the total label mass is strictly below one; an elementary directed
bound is

\[
\sum_{q\text{ labelled}}q^{-3/2}<1.
\]

The same holds for every larger `m`. If `M_j` is the total weight on label
level `j`, double counting gives

\[
jM_j<\vartheta M_{j-1},\qquad\vartheta<1.
\]

Thus every odd level is smaller than the preceding even level, and

\[
G_m(X)=(M_0-M_1)+(M_2-M_3)+\cdots>0
\]

for `X>1`. At `X=1` every term vanishes.

## 3. Exact Taylor remainder cone

For integer `m>=3`, define

\[
r_{m,k}(z)=(-1)^k\left[(1-z)_+^m-
\sum_{j=0}^{k-1}(-1)^j\binom mjz^j\right].
\]

Taylor's integral remainder is

\[
r_{m,k}(z)=
\frac{m!}{(m-k)!(k-1)!}
\int_0^{\min(z,1)}(z-t)^{k-1}(1-t)^{m-k}\,dt.
\]

Therefore `r_(m,k)>=0`, and for `c>=1`,

\[
r_{m,k}(cz)\le c^k r_{m,k}(z).
\]

Put

\[
E_{m,k}(X)=
\sum_n\frac{\beta(n)}{n^{(m+1)/2}}
 r_{m,k}(\sqrt{n/X}).
\]

For `k<=m-2`, adjoining a prime label costs at most

\[
q^{-(m+1-k)/2}\le q^{-3/2}.
\]

The same parity-level pairing proves

\[
E_{m,k}(X)>0.
\]

Writing

\[
B(a)=\frac{1-67^{-a}}{\zeta(a)},
\]

one obtains the exact alternating enclosure

\[
\sum_n\frac{\beta(n)}{n^{(m+1)/2}}(1-\sqrt{n/X})_+^m
=
\sum_{j<k}(-1)^j\binom mjX^{-j/2}B((m+1-j)/2)
+(-1)^kE_{m,k}(X).
\]

Hence every layer above the prime-harmonic exponent is resolved.

## 4. The final critical remainder

The first uncontrolled member is `k=m-1`. Define

\[
\mathcal C_m(X)=4^mX^{m/2}E_{m,m-1}(X).
\]

Then

\[
\mathcal C_m(X)=\sum_n\frac{\beta(n)}{\sqrt n}K_m(X/n),
\]

where

\[
K_m(y)=4^m\begin{cases}
(1-\sqrt y)^m+m\sqrt y-1,&y<1,\\
m\sqrt y-1,&y\ge1.
\end{cases}
\]

Bernoulli's inequality gives `K_m>=0`. This is a positive kernel, not a
positive native-source projection.

In the strip `1/2<Re(s)<1`,

\[
\widehat K_m(s)=
\frac{2\,4^m m!}
{2s(2s-1)\prod_{j=2}^m(j-2s)}.
\]

The compact interval `0<X<1` contributes exactly

\[
4^m\sum_{j=2}^m(-1)^j\binom mjB((j+1)/2)X^{j/2}.
\]

Subtracting it gives

\[
\begin{aligned}
\int_1^\infty\mathcal C_m(X)X^{-s-1}\,dX
={}&\widehat K_m(s)
\frac{1-67^{-(s+1/2)}}{\zeta(s+1/2)}\\
&-4^m\sum_{j=2}^m
\frac{(-1)^j\binom mjB((j+1)/2)}{j/2-s}.
\end{aligned}
\]

The finite line cancels all positive-real polynomial-carrier poles. The
remaining `s=1/2` pole is cancelled by the reciprocal-zeta zero at one. The
continuation is analytic at every positive real `s`.

Every hypothetical zero `rho` with `Re(rho)>1/2` gives a genuine pole at
`s=rho-1/2`: the kernel multiplier has no zeros and
`1-67^(-rho)` cannot vanish.

Therefore eventual nonnegativity of `C_m`, or merely

\[
\int_1^X(\mathcal C_m(t))_-\frac{dt}{t}=X^{o(1)},
\]

implies RH by the specialized Landau theorem.

## 5. Minimal quadratic form

For `m=2`,

\[
K_2(y)=16\begin{cases}y,&y<1,\\2\sqrt y-1,&y\ge1,
\end{cases}
\]

and

\[
\mathcal C_2(X)=
16\frac{1-67^{-3/2}}{\zeta(3/2)}X-G_2(X).
\]

The native quadratic scalar `G_2` is globally nonnegative. The remaining
conclusion-producing estimate is the opposite, sharp upper envelope

\[
G_2(X)\le16\frac{1-67^{-3/2}}{\zeta(3/2)}X,
\]

or a subpower logarithmic bound on its violations.

## 6. Why the last step is not automatic

In logarithmic coordinates put

\[
F_m(u)=e^{-mu/2}G_m(e^u).
\]

Because `S(1)=0`,

\[
F_m'(u)=2m e^{-u/2}F_{m-1}(u)
\]

without activation atoms. Positivity of `F_2` only says that a weighted
primitive of `F_1` is nonnegative. A nonnegative primitive need not have every
final window nonnegative.

Repeated scale differences yield positive B-spline convolutions down to
`F_2`; the last difference is a positive B-spline convolution of the unknown
critical `F_1`. That is exactly where the prime-removal mass becomes
`sum_p1/p`.

Thus the supercritical theorem closes every convergent layer and proves that
the remaining layer is genuinely arithmetic.

## 7. Relationship to the ratio-67 window

Differentiating the normalized quadratic scalar gives

\[
\frac{d}{d\log X}[X^{-1}G_2(X)]=4X^{-1}G_1(X).
\]

The final scale difference is therefore a positive logarithmic spline of the
critical linear source. Under the compact box normalization of PR #664, its
activation-collar coefficient is

\[
-3\sum_{X/67<n\le X}\mu(n).
\]

The Taylor, owner-Carleson, and collar-window routes converge to the same
prime-harmonic boundary.

## Verdict

```text
all m>=2 activation-zero powers          positive globally
all effective exponents >1              resolved with exact signs
critical positive kernel                 reconstructed exactly
critical Mellin consumer                 zero-safe and conclusion-complete
critical envelope / negative mass        open
Riemann Hypothesis                       unproved
```
