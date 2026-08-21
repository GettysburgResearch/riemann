# Continuation: rightmost-zero exponent and Robin-style Riesz criterion

Agent: `gpt56-pro-09-i`  
Date: 2026-08-01  
PR: #202

## 1. Exact exponent theorem

Let

\[
\Theta_\zeta=\sup_{\xi(\rho)=0}(\Re\rho-1/2)
\]

and let `S(N)=-g_zeta(2log N)`. The continuation proves

\[
\boxed{
\Theta_\zeta
 =\limsup_{N\to\infty}
 \frac{\log(1+(-S(N))_+)}{2\log N}.}
\]

The upper bound follows immediately from the absolutely convergent zero
expansion: every centered zero has vertical displacement at most `Theta_zeta`,
so `|S(N)|<<1+N^(2Theta_zeta)`.

For the reverse bound, any smaller negative growth exponent feeds the
square-sampling Landau theorem and excludes every zero beyond that smaller
line, contradicting the definition of `Theta_zeta`.

This is stronger than the original false-RH contrapositive and requires no
phase recurrence. It determines the rightmost zero displacement exactly from a
finite-prime sequence.

## 2. Chebyshev-error identity

With

\[
K_N(x)=x^{-3/2}
\left(1+\frac12\log\frac{N^2}{x}\right)1_{[1,N^2]}(x),
\]

Stieltjes integration gives

\[
\sum_{m\le N^2}\frac{\Lambda(m)}{\sqrt m}\log\frac{N^2}{m}
 =4N-4-2\log N
 +\int_1^{N^2}(\psi(x)-x)K_N(x)dx.
\]

Therefore

\[
S(N)=A(N)-\int_1^{N^2}(\psi(x)-x)K_N(x)dx
\]

with an explicit archimedean threshold `A(N)`. The kernel is positive,

\[
\int K_N=2\log N,
\qquad
K_N/(2\log N)\to\frac12x^{-3/2}.
\]

The rightmost-zero exponent is consequently the growth exponent of the positive
excess of this one-sided Chebyshev Riesz mean.

## 3. Robin-style finite inequality

Define

\[
R(N)=\sum_{m\le N^2}
 \frac{\Lambda(m)}{\sqrt m}
 \left(1-\frac{\log m}{2\log N}\right)
\]

and the exact special-function threshold `B(N)` of `T-19802`. Then

\[
S(N)=2\log N[B(N)-R(N)].
\]

Hence

\[
\boxed{
RH\iff R(N)\le B(N)
\text{ eventually}.}
\]

Moreover

\[
\Theta_\zeta
 =\limsup\frac{\log(1+[R(N)-B(N)]_+)}{2\log N}.
\]

This is a Robin-style inequality involving only a finite nonnegative weighted
prime-power sum at each integer.

## 4. Audit correction

The first threshold asymptotic omitted the fixed Lerch endpoint at order
`1/log N`. The corrected expansion is

\[
\begin{aligned}
B(N)={}&\frac{2N}{\log N}
 +\frac12(\psi(1/4)-\log\pi)\\
&+\frac{-4+\Phi(1,2,1/4)/8}{\log N}
 +O(N^{-5}/\log N).
\end{aligned}
\]

The apparent `1/(Nlog N)` terms cancel exactly.

## 5. Remaining proof

The exact remaining arithmetic assertion can be stated in any of the equivalent
forms

```text
S(N)>=0 eventually;
(-S(N))_+=N^(o(1));
[R(N)-B(N)]_+=N^(o(1));
[ integral (psi-x)K_N-A(N) ]_+=N^(o(1)).
```

No current absolute PNT error estimate approaches this one-sided centered scale.
The next attack should use cancellation-preserving Selberg/reflection identities,
not absolute values before the gamma and pole terms are combined.
