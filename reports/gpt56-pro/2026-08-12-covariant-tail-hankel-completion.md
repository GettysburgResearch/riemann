# Covariant tail-Hankel completion — 2026-08-12

## Freeze

```text
repository:  gfreund123/riemann
parent PR:   #400
parent head: 020b886b0ed54c71d2129ddff421c46d7c8871d4
branch:      research/gpt56-pro/91306-covariant-tail-hankel-completion
RH status:   unproved
```

## Executive result

The literal source-linear prime output of the Poisson/Fock programme is now
embedded explicitly in a two-sided Hardy tangent.

The construction has four exact steps:

1. the ordinary-zeta scattering score is a positive atomic first-chaos measure;
2. its Suzuki Hardy block is exactly the associated tail-Hankel operator;
3. at the fixed safe scale `a=4`, that Hankel operator has a closed Julia
   isometry with three explicit positive auxiliary defects;
4. the gamma/pole factor is the skew connection in a moving-unitary
   factorisation of Suzuki's completed inner multiplier.

This closes the prime tangent channel, including polarization, reflection and
delay. It does not prove the completed Fisher-curvature domination of
`T-91008`, whose prime–gamma cross term remains RH-bearing.

## Actual prime score

For `c=a+1/2`,

\[
 Z_a(x)=\zeta(c+ix)/\zeta(c-ix),
\]

and

\[
 a\partial_a\log Z_a(x)
 =\int(e^{ixu}-e^{-ixu})d\beta_a(u),
\]

where

\[
 d\beta_a(u)=a\sum_{n=p^k}\Lambda(n)n^{-c}\delta_{\log n}(du).
\]

This measure is distinct from the normalized Jordan curvature of `L-91037`.

## Tail-Hankel Hardy block

The positive-frequency block of multiplication by the prime score is

\[
 (H_{\beta_a}g)(t)=\int_{u>t}g(u-t)d\beta_a(u).
\]

With `W(t)=beta_a((t,infinity))`, conditional expectation on the triangle
`0<t<u` gives the exact identity

\[
\begin{aligned}
 \|g\|_2^2={}&\|H_{\beta_a}g\|_2^2
 +\|\sqrt{1-W}\,g\|_2^2\\
 &+\iint_{u>t}|g(u-t)-H_{\beta_a}g(t)/W(t)|^2d\beta_a(u)dt\\
 &+\|\sqrt{W^{-1}-1}\,H_{\beta_a}g\|_2^2.
\end{aligned}
\]

At `a=4`, elementary comparison proves

\[
 \beta_4((0,\infty))<85/196<1.
\]

## Covariant gamma completion

Write on the real boundary

\[
 \Theta_a=\Gamma_a Z_a.
\]

Multiplication by `Z_a` is a source isometry into `L2`; multiplication by
`Gamma_a` is unitary. Its logarithmic derivative is a skew connection. The
identity

\[
 (I-Q)\dot M=C(I-R)(\dot V+C^*\dot C\,V)
\]

places the prime Hankel output and explicit gamma/pole motion in the same
completed Suzuki normal tangent without dropping their interference.

## Exact firewall

The Jordan-curvature coefficient is

\[
 [1-(1+2au)e^{-2au}]e^{-(a+1/2)u}/(ka^2),
\]

whereas the Suzuki score coefficient is

\[
 au\,e^{-(a+1/2)u}/k.
\]

Their ratio depends on `u`. Jordan positivity therefore cannot be spent as the
Suzuki score without an explicit transport theorem.

## Final boundary

```text
prime Poisson first-chaos output -> Hardy                CLOSED EXACTLY
explicit positive Julia auxiliary                        CLOSED EXACTLY
causal/anti-causal/delay polarization                     CLOSED EXACTLY
gamma/pole motion as covariant connection                 CLOSED EXACTLY
full completed Fisher curvature >= total Suzuki shape     OPEN / RH-EQUIVALENT
Riemann Hypothesis                                        UNPROVED
```
