# L-32302 — The RH-sensitive opposite-parity source is a dyadic log-derivative dipole

Claim ID: `L-32302`  
Title: The source `W=omega_2*Lambda_omega` is exactly `-omega_2 log`; every complete odd two-adic fiber has zero total mass and one explicit dyadic-difference factor  
Status: **PROPOSED COMPLETE EXACT DIRICHLET-ALGEBRA LEMMA — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-sol`  
Created: 2026-08-08  
Dependencies: PR #268 definitions of `omega_2,a_omega,Lambda_omega,W`  
Scope: exact source simplification; no energy estimate or RH conclusion

## 1. General inverse derivative identity

Let arithmetic sequences `omega,a` satisfy

\[
omega*a=\varepsilon,
\]

and define

\[
\Lambda=\omega*(a\log),
\qquad
W=\omega*\Lambda.
\]

Write their Dirichlet series as

\[
\Omega(s)=\sum_n\omega(n)n^{-s},
\qquad
A(s)=\sum_na(n)n^{-s}.
\]

Then

\[
\Omega(s)A(s)=1,
\]

and the series of `a log` is `-A'(s)`. Hence

\[
\Lambda(s)
=-\Omega(s)A'(s)
=\frac{\Omega'(s)}{\Omega(s)}.
\tag{L-32302.1}
\]

Multiplication by `Omega` gives

\[
\boxed{
W(s)=\Omega'(s).
}
\tag{L-32302.2}
\]

Since

\[
\Omega'(s)
=-\sum_n\omega(n)\log n\,n^{-s},
\]

coefficient comparison gives the exact identity

\[
\boxed{
W(n)=-\omega(n)\log n.
}
\tag{L-32302.3}
\]

Thus the source-change recurrence of PR #268 is the differentiated inverse identity; `W` is not an independent arithmetic sequence.

## 2. Opposite-parity specialization

For

\[
\omega_2
=\mu-\frac32\delta_2*\mu+\frac12\delta_4*\mu,
\]

the local two-adic polynomial on one odd squarefree core `u` is

\[
\boxed{
 p(z)
=(1-z)^2(1-z/2)
=1-\frac52z+2z^2-\frac12z^3.
}
\tag{L-32302.4}

More precisely,

\[
\sum_{\nu=0}^3\omega_2(2^\nu u)z^\nu
=\mu(u)p(z).
\tag{L-32302.5}
\]

When `mu(u)=0`, the whole fiber vanishes and the formulas below remain trivial.

## 3. Complete logarithmic source fiber

By (L-32302.3),

\[
\begin{aligned}
\sum_{\nu=0}^3W(2^\nu u)z^\nu
&=-\mu(u)
\sum_{\nu=0}^3p_\nu
(\log u+\nu\log2)z^\nu\\
&=-\mu(u)
\left[
 \log u\,p(z)
 +(\log2)z p'(z)
\right].
\end{aligned}
\tag{L-32302.6}

Because `p` has a double zero at `z=1`, both `p(1)` and `p'(1)` vanish. Therefore

\[
\boxed{
\sum_{\nu=0}^3W(2^\nu u)=0.
}
\tag{L-32302.7}

The RH-sensitive source is already a zero-mass dyadic fiber before any carry transform, physical window, or norm.

## 4. Explicit dyadic-difference factor

Put

\[
U=\log u,
\qquad
L=\log2.
\]

Direct factorization gives

\[
U p(z)+L z p'(z)
=\frac{1-z}{2}
\left[
 (3L+U)z^2
 -(5L+3U)z
 +2U
\right].
\tag{L-32302.8}
\]

Hence

\[
\boxed{
\sum_{\nu=0}^3W(2^\nu u)z^\nu
=-(1-z)\,\mu(u)R_u(z),
}
\tag{L-32302.9}
\]

where

\[
\boxed{
R_u(z)
=\frac12
\left[
 (3\log2+\log u)z^2
 -(5\log2+3\log u)z
 +2\log u
\right].
}
\tag{L-32302.10}

Thus every complete odd-core source fiber is an exact adjacent dyadic difference of a three-tap logarithmic fiber.

Equivalently there is a unique finite arithmetic sequence `V` on each complete fiber such that

\[
\boxed{
W=(\varepsilon-\delta_2)*V
}
\tag{L-32302.11}
\]

fiberwise. The inverse physical filter

\[
(\varepsilon-\delta_2)^{-1}
=\sum_{j\ge0}\delta_{2^j}
\]

has normalized translation weights `2^{-j/2}` and is therefore `ell^1` in the square-root physical normalization.

Consequently `W` and the dyadic primitive `V` have the same block-energy exponential exponent under any fixed compact physical window, modulo a fixed causal delay collar.

## 5. Relation to the live proof frontier

PR #268 treats the exact identity

\[
a_\omega*W=\Lambda_\omega
\]

as a positive-inverse source change. Equations (L-32302.3)--(L-32302.11) expose an additional source-local structure which is lost by absolute proper-divisor charging:

```text
W is the logarithmic derivative of the inverse source;
every complete odd-core W fiber has zero total mass;
that cancellation is a literal dyadic adjacent difference;
the dyadic inverse is stable at the square-root physical normalization.
```

A future boundary/cap recurrence should therefore transport the complete dipole fiber before using the positive-inverse source change. This is compatible with the repeated lesson from the terminal-boundary refutations: source cancellation must precede absolute norms.

## 6. Proof boundary

Closed exactly, subject to review:

1. `W(s)=Omega'(s)`;
2. `W(n)=-omega(n)log n`;
3. the complete four-tap two-adic fiber;
4. zero total mass on every odd core;
5. the explicit `(1-z)` dyadic-difference factor;
6. stable square-root-normalized causal inversion of that finite dyadic difference.

Open:

1. a quantitative carry/physical estimate exploiting this dipole before source change;
2. the propagated cap-interface/Cycle-Debt theorem;
3. RH.
