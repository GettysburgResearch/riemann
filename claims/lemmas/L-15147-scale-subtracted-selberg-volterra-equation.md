# L-15147 — Scale-subtracted Selberg–Volterra equation

Claim ID: `L-15147`  
Title: The Chebyshev dilation increment satisfies one exact linear Volterra equation with bounded Selberg forcing  
Status: **PROPOSED PENDING INDEPENDENT REVIEW**  
Authoring agent: `gpt56-04-f`  
Created: 2026-08-07  
Dependencies: Selberg's exact coefficient identity; elementary partial summation; the standard elementary estimate for Selberg's forcing  
Scope: exact arithmetic equation for the RH-equivalent energy variable

## 1. Selberg's exact summatory identity

Define

\[
 C(n)=(\mu*\log^2)(n)
 =\sum_{d\mid n}\mu(d)\log^2(n/d)
\]

and

\[
 R(x)=\sum_{n\le x}C(n).
 \tag{L-15147.1}
\]

Selberg's coefficient identity is

\[
 \Lambda(n)\log n+(\Lambda*\Lambda)(n)=C(n).
 \tag{L-15147.2}
\]

Summing through a real endpoint `x>=1` gives

\[
 \sum_{n\le x}\Lambda(n)\log n
 +\sum_{mn\le x}\Lambda(m)\Lambda(n)
 =R(x).
 \tag{L-15147.3}
\]

Partial summation and the definition of `psi` turn this into

\[
 \boxed{
 \psi(x)\log x
 -\int_1^x{\psi(t)\over t}dt
 +\sum_{n\le x}\Lambda(n)\psi(x/n)
 =R(x).}
 \tag{L-15147.4}
\]

All identities use the same right-continuous endpoint convention. Changing a
finite set of jump values does not affect the integral consequences below.

## 2. Exact scale subtraction

Fix `a>1` and put

\[
 A_a(x)=\psi(x)-a\psi(x/a).
 \tag{L-15147.5}
\]

Subtract `a` times (L-15147.4) at `x/a` from (L-15147.4) at `x`.
The boundary term is

\[
 \psi(x)\log x-a\psi(x/a)\log(x/a)
 =A_a(x)\log x+a(\log a)\psi(x/a).
 \tag{L-15147.6}
\]

Because `psi(t/a)=0` below the lower endpoint,

\[
 \int_1^x{\psi(t)\over t}dt
 -a\int_1^{x/a}{\psi(t)\over t}dt
 =\int_1^x{A_a(t)\over t}dt.
 \tag{L-15147.7}
\]

The quadratic convolution difference also closes exactly. For `n<=x/a`, the
two summands combine into `A_a(x/n)`. For `x/a<n<=x`, the missing second term
is zero and the same formula remains valid. Hence

\[
 \sum_{n\le x}\Lambda(n)\psi(x/n)
 -a\sum_{n\le x/a}\Lambda(n)\psi(x/(an))
 =\sum_{n\le x}\Lambda(n)A_a(x/n).
 \tag{L-15147.8}
\]

Therefore

\[
 \boxed{
 \begin{aligned}
 &A_a(x)\log x
 +a(\log a)\psi(x/a)
 -\int_1^x{A_a(t)\over t}dt\\
 &\qquad
 +\sum_{n\le x}\Lambda(n)A_a(x/n)
 =R(x)-aR(x/a).
 \end{aligned}}
 \tag{L-15147.9}
\]

This is the exact scale-subtracted Selberg identity. The quadratic prime
convolution has not been bounded or discarded; it has become a causal
multiplicative convolution acting on the same scale increment.

## 3. Normalized linear Volterra form

Put

\[
 P(x)={\psi(x)\over x},
 \qquad
 F_a(x)={A_a(x)\over x}=P(x)-P(x/a).
 \tag{L-15147.10}
\]

Dividing (L-15147.9) by `x` gives

\[
 \boxed{
 \begin{aligned}
 F_a(x)\log x
 &+\sum_{n\le x}{\Lambda(n)\over n}F_a(x/n)
 -{1\over x}\int_1^xF_a(t)dt\\
 &=H_a(x),
 \end{aligned}}
 \tag{L-15147.11}
\]

where the explicit forcing is

\[
 \boxed{
 H_a(x)
 ={R(x)-aR(x/a)\over x}
 - (\log a)P(x/a).}
 \tag{L-15147.12}
\]

Thus the RH-equivalent unknown `F_a` satisfies one **linear** Volterra equation
with the actual von Mangoldt coefficients as its causal kernel.

In additive logarithmic coordinates `x=e^y`, the convolution term is

\[
 \sum_{\log n\le y}{\Lambda(n)\over n}
 f_a(y-\log n),
 \qquad f_a(y)=F_a(e^y).
 \tag{L-15147.13}
\]

Its Laplace symbol is

\[
 -{\zeta'\over\zeta}(1+z),
\]

so the equation retains the complete arithmetic spectrum.

## 4. The forcing is unconditionally bounded

The standard elementary Selberg estimate gives

\[
 R(x)=2x\log x+O(x).
 \tag{L-15147.14}
\]

Consequently

\[
 {R(x)-aR(x/a)\over x}
 =2\log a+O_a(1).
 \tag{L-15147.15}
\]

Chebyshev's elementary bound `psi(x)=O(x)` gives `P(x)=O(1)`. Therefore

\[
 \boxed{
 H_a(x)=O_a(1)}
 \tag{L-15147.16}
\]

unconditionally.

The global difficulty is not forcing growth. It is the possible failure of a
coercive energy estimate for the Volterra operator on the left of
(L-15147.11). That failure is precisely where an off-critical zero may enter.

## 5. Energy target in the equation's own variable

`T-15119` identifies RH with

\[
 \boxed{
 \int_2^Y|F_a(x)|^2dx=Y^{o(1)}.}
 \tag{L-15147.17}
\]

Equation (L-15147.11) shows that a proof need not estimate an unrelated
prime-pair kernel. It may instead prove a weighted coercivity or renewal bound
for the explicit operator

\[
 \boxed{
 (\mathcal L_af)(x)
 =f(x)\log x
 +\sum_{n\le x}{\Lambda(n)\over n}f(x/n)
 -{1\over x}\int_1^xf(t)dt.}
 \tag{L-15147.18}
\]

The actual arithmetic function satisfies

\[
 \mathcal L_aF_a=H_a,
 \qquad \|H_a\|_\infty<\infty.
 \tag{L-15147.19}
\]

A sufficient full-resolution theorem is an a priori estimate of the form

\[
 \boxed{
 \int_2^Y|f(x)|^2dx
 \le Y^{o(1)}
 \left(
 1+\int_2^Y|\mathcal L_af(x)|^2w_Y(x)dx
 \right)}
 \tag{L-15147.20}
\]

for the relevant causal solution class and one explicit subexponential weight
`w_Y`. Applied to (L-15147.19), it proves RH.

A block-recursive version is the target of `M-15108`.

## 6. Why this is stronger than a formal Selberg restatement

The scale subtraction performs three load-bearing operations simultaneously:

1. it cancels the prime main term exactly;
2. it turns the quadratic convolution into an operator on the same dilation
   increment whose energy is RH-equivalent;
3. it leaves a bounded explicit forcing.

Therefore the final theorem is now a coercivity question for one written-down
linear arithmetic Volterra operator, rather than an unspecified cancellation in
a double prime sum.

This does not make coercivity automatic. Taking absolute values in
(L-15147.11) destroys the observed off-diagonal cancellation and recovers only
phase-blind PNT-scale estimates.

## 7. Production interface

For an integer scale `a` and integer endpoints, a finite checker can emit:

```text
psi prefix table
R prefix table
A_a and F_a table
partial-summation integral
von-Mangoldt Volterra convolution
forcing H_a
exact residual of (L-15147.11)
block L2 energy
```

All entries are rational combinations of logarithms of primes. A directed
implementation may bind each logarithm once and share it across every ledger.

## 8. Proof boundary

Closed:

- the exact summatory Selberg identity;
- its exact dilation subtraction;
- the normalized linear Volterra equation;
- unconditional boundedness of the forcing.

Open:

- a coercive or contractive estimate strong enough to imply
  (L-15147.17).

No such estimate and no proof of RH is claimed.