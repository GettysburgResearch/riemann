# L-9514 — Exact Volterra–virial identity for the analytic totient energy

Claim ID: `L-9514`  
Title: The RH-bearing analytic-totient square mean is the joint remainder between the total and arithmetic cubic mean squares  
Status: `PROPOSED — EXACT IDENTITY; CRITICAL REMAINDER BOUND OPEN`  
Authoring agent: `gpt56-08`  
Created: 2026-08-07  
Dependencies: the Kaczorowski–Wiertelak arithmetic/analytic decomposition; `L-9512`, `T-9506`  
Scope: exact real-variable identity on finite intervals; no RH assumption  
Related counterexample candidates: none

## 1. The three totient errors

Put

\[
c={6\over\pi^2}.
\tag{L-9514.1}
\]

For real `x>=1`, define the analytic part

\[
\boxed{
 A(x)=E^{\rm AN}(x)
 ={1\over2}\left(
 1+\sum_{d=1}^{\infty}
 \mu(d)\left\{{x\over d}\right\}^{2}
 \right),}
\tag{L-9514.2}
\]

the arithmetic slope

\[
\boxed{
 f(x)=-\sum_{d=1}^{\infty}{\mu(d)\over d}
 \left\{{x\over d}\right\},}
\tag{L-9514.3}
\]

and the ordinary summatory-totient error

\[
\boxed{
 E_\varphi(x)=
 \sum_{n\le x}\varphi(n)-{c\over2}x^2.}
\tag{L-9514.4}
\]

The series in (L-9514.2) is absolutely convergent in its tail because, for
`d>x`, its summand is `mu(d)x^2/d^2`. The series in (L-9514.3) is interpreted in
the standard convergent Kaczorowski--Wiertelak normalization; every identity
below may first be proved with a finite divisor cutoff and then passed to the
limit on compact intervals.

The elementary identity

\[
\sum_{n\le x}\varphi(n)
 ={1\over2}\left(
 1+\sum_{d=1}^{\infty}\mu(d)
 \left\lfloor{x\over d}\right\rfloor^2
 \right)
\tag{L-9514.5}
\]

and `floor(y)=y-{y}` give exactly

\[
\boxed{E_\varphi(x)=x f(x)+A(x).}
\tag{L-9514.6}
\]

This is the classical arithmetic/analytic decomposition.

## 2. The analytic part is the Volterra primitive

Away from integer points, termwise differentiation in (L-9514.2) gives

\[
 A'(x)=
 \sum_{d=1}^{\infty}{\mu(d)\over d}
 \left\{{x\over d}\right\}
 =-f(x).
\tag{L-9514.7}
\]

The derivative series is locally legitimate after the usual symmetric/finite
cutoff passage; its derivative in the distributional sense is the locally
finite centered totient measure. The function `A` is continuous, piecewise
quadratic, and (L-9514.7) holds almost everywhere. Consequently

\[
\boxed{E_\varphi(x)=A(x)-xA'(x)}
\tag{L-9514.8}
\]

almost everywhere.

Equivalently, the analytic error is the Volterra primitive of the arithmetic
part:

\[
 A(b)-A(a)=-\int_a^b f(x)dx.
\tag{L-9514.9}
\]

## 3. Exact virial identity

For every `1<=a<b`,

\[
\begin{aligned}
 E_\varphi(x)^2-x^2f(x)^2
 &=(A-xA')^2-x^2(A')^2\\
 &=A^2-2xAA'\\
 &=2A^2-{d\over dx}\left(xA^2\right)
\end{aligned}
\tag{L-9514.10}
\]

almost everywhere. Integration gives the exact identity

\[
\boxed{
\begin{aligned}
2\int_a^b|E^{\rm AN}(x)|^2dx
={}&\int_a^b|E_\varphi(x)|^2dx
 -\int_a^b x^2|f(x)|^2dx\\
&+\left[x|E^{\rm AN}(x)|^2\right]_{a}^{b}.
\end{aligned}}
\tag{L-9514.11}
\]

No asymptotic theorem, zero location, or sign hypothesis enters this formula.
The right side is automatically nonnegative although it is written as the
difference of two quantities of cubic scale plus an endpoint correction.

On one dyadic interval this reads

\[
\boxed{
\begin{aligned}
2\int_X^{2X}|E^{\rm AN}(x)|^2dx
={}&\int_X^{2X}|E_\varphi(x)|^2dx
 -\int_X^{2X}x^2|f(x)|^2dx\\
&+2X|E^{\rm AN}(2X)|^2
 -X|E^{\rm AN}(X)|^2.
\end{aligned}}
\tag{L-9514.12}
\]

## 4. Exact RH-facing reformulation

By `T-9506`, RH is equivalent to

\[
\int_X^{2X}|E^{\rm AN}(x)|^2dx
 \ll_\varepsilon X^{2+\varepsilon}
\tag{L-9514.13}
\]

for every `epsilon>0`. Hence RH is equivalently the joint virial remainder bound

\[
\boxed{
\begin{aligned}
&\int_X^{2X}|E_\varphi(x)|^2dx
 -\int_X^{2X}x^2|f(x)|^2dx\\
&\quad+2X|E^{\rm AN}(2X)|^2
 -X|E^{\rm AN}(X)|^2
 \ll_\varepsilon X^{2+\varepsilon}.
\end{aligned}}
\tag{L-9514.14}
\]

Thus the missing local-to-Bohr estimate is not unrelated to the classical
mean-square theory of the summatory totient error. It is precisely the
**joint remainder after cancellation of the total and arithmetic cubic mean
squares**, with the endpoint flux retained.

## 5. Why separate mean-square asymptotics do not suffice

Suppose separately that

\[
\int_1^X|E_\varphi(x)|^2dx=\beta X^3+R_{\rm tot}(X)
\]

and

\[
\int_1^Xx^2|f(x)|^2dx=\beta X^3+R_{\rm ar}(X).
\]

Equation (L-9514.11) requires a bound for the **correlated difference**

\[
R_{\rm tot}(X)-R_{\rm ar}(X)
 +X|E^{\rm AN}(X)|^2,
\tag{L-9514.15}
\]

not independent absolute bounds for `R_tot` and `R_ar`. Existing cubic-scale
remainders are much larger than `X^(2+epsilon)` and cannot be subtracted by a
triangle inequality.

The cancellation must be preserved at the level of the common arithmetic
packet, exactly as the terminal-prime and double-centered Type-II programmes
require.

## 6. Fourier explanation of the critical one-power loss

For a finite denominator cutoff, the arithmetic sawtooth packet has Fourier
coefficients of shape

\[
 {\mu(d)\over d h}
 \quad\text{at frequency }{h\over d},
\tag{L-9514.16}
\]

whereas one Volterra integration produces the analytic packet with coefficients
of shape

\[
 {\mu(d)\over h^2}.
\tag{L-9514.17}
\]

The divisor denominator `1/d` disappears. This is exactly why the classical
arithmetic-part dispersion estimate does not automatically control the analytic
part: the near-resonant Farey block loses one critical power after the Volterra
primitive is taken.

Equation (L-9514.11) shows the only legitimate way to recover that power from
the total-error theory: estimate the total and arithmetic channels jointly,
including their endpoint flux, before absolute values are taken.

## 7. Relation to the other global routes

The same joint remainder appears in the repository in three alternate
coordinates:

1. the Möbius-weighted near-resonant Farey cluster of `L-23002`;
2. the doubly centered balanced Type-II prime block of `L-15153/L-21504`;
3. the curvature-normalized prime-transport reserve of PR #218.

The present identity is the exact real-variable adapter between the classical
totient decomposition and those signed-correlation routes.

## 8. Proof boundary

Closed exactly:

- the arithmetic/analytic decomposition;
- `A'=-f` almost everywhere;
- the Volterra representation;
- the virial identity;
- the equivalence of the critical analytic square mean with the joint remainder.

Open:

- the estimate (L-9514.14), equivalently the critical near-resonance theorem and
  RH.

This lemma does not claim that the two cubic mean-square remainders cancel at
the required rate; it identifies the precise cancellation that a full proof
must establish.
