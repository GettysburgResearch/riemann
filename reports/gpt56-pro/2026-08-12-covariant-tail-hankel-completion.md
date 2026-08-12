# Covariant tail-Hankel completion — 2026-08-12

## Freeze

```text
repository:  gfreund123/riemann
parent PR:   #400
parent head imported through: 779ec2cc11e8a36abd16d2a20886381915933cce
branch:      research/gpt56-pro/91306-covariant-tail-hankel-completion
RH status:   unproved
```

## Executive result

The source-linear prime output of the Poisson/Fock programme is now embedded
explicitly in Suzuki's completed two-sided Hardy tangent, and the parent
branch's completed Fisher phase factorization has been lifted through the
previously open Hardy/model-space projection.

The construction has six exact steps:

1. the ordinary-zeta scattering score is a positive atomic first-chaos measure;
2. its Suzuki Hardy block is exactly the associated tail-Hankel operator;
3. at the fixed safe scale `a=4`, that Hankel operator has a closed Julia
   isometry with three explicit positive auxiliary defects;
4. the gamma/pole factor is the skew connection in a moving-unitary
   factorisation of Suzuki's completed inner multiplier;
5. the completed Fisher phase features form a vector-valued Hardy symbol;
6. orthogonal projection onto the score direction gives Suzuki's scalar shape,
   with an explicit positive orthogonal source-fibre auxiliary.

Thus the requested source-to-Hardy tangent colligation is constructed. The
remaining RH-bearing theorem is no longer an embedding problem: it is the
identity between the explicit Fisher auxiliary and the corrected delayed zeta
screw/Weil defect.

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

## Completed Fisher phase colligation

Let `sigma_a=Y-E_aY`, `V_a=Var_a(Y)`, and let `h_(a,x)` be the centered
normalized phase feature of parent `L-91312`. Define

\[
 \mathbf h_a(x;Y)
 =a\sqrt{V_a}\,\Theta_a(x)h_{a,x}(Y).
\]

The score contraction `c_a(v)=<v,sigma_a/sqrt(V_a)>` satisfies

\[
 c_a(\mathbf h_a(x))=-a\partial_a\Theta_a(x).
\]

Consequently the vector-valued Hankel operator

\[
 \mathscr H_a=(P_-\otimes I)M_{\mathbf h_a}P_+
\]

and the scalar Suzuki tangent Hankel `H_(m_a)` obey

\[
 H_{m_a}=-(I\otimes c_a)\mathscr H_a.
\]

Orthogonal score decomposition yields exactly

\[
 \mathscr H_a^*\mathscr H_a
 =H_{m_a}^*H_{m_a}+\mathscr E_a^*\mathscr E_a.
\]

With Suzuki's normalization,

\[
 2\mathscr H_a^*\mathscr H_a
 =\mathcal J_a^*\mathcal J_a
  +2\mathscr E_a^*\mathscr E_a.
\]

This closes the model-space projection and every carrier/orientation/delay
polarization.

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

Likewise the positive Fisher auxiliary

\[
 2\mathscr E_a^*\mathscr E_a
\]

cannot simply be renamed the zeta screw defect. Their equality must be replayed
in the common delayed Guinand--Weil/Suzuki normalization.

## Final boundary

```text
prime Poisson first-chaos output -> Hardy                CLOSED EXACTLY
explicit positive Julia auxiliary                        CLOSED EXACTLY
causal/anti-causal/delay polarization                     CLOSED EXACTLY
gamma/pole motion as covariant connection                 CLOSED EXACTLY
Fisher phase feature -> model-space shape                 CLOSED EXACTLY
explicit completed positive tangent auxiliary             CLOSED EXACTLY
Fisher auxiliary = delayed zeta screw/Weil defect         OPEN / RH-EQUIVALENT
Riemann Hypothesis                                        UNPROVED
```
