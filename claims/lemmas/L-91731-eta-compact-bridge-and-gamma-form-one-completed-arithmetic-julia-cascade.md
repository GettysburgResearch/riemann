# L-91731 — Eta, compact bridge, and gamma form one explicit completed arithmetic Julia cascade

Claim ID: `L-91731`  
Status: **PROVED EXACT POSITIVE ARITHMETIC SOURCE COLLIGATION; MODEL EXHAUSTION OPEN**  
Created: 2026-08-13  
Depends on: `L-91630/L-91631`, `L-91530`, `L-91730`  
RH status: **unproved**

## 1. Paired-eta channel

On

\[
\mathcal E=\bigcup_{m\ge1}[\log(2m-1),\log(2m)]
\]

the hard and safe carrier kernels are

\[
K_\eta^-(t,u)
=
I_\eta(\sigma-\omega+i(t-u)),
\]

\[
K_\eta^+(t,u)
=
I_\eta(\sigma+\omega+i(t-u)).
\]

`L-91630` gives

\[
\boxed{
K_\eta^-=K_\eta^++D_\eta,
\qquad D_\eta\succeq0,
}
\tag{L-91731.1}
\]

through the multiplier pair

\[
m_\eta(y)=e^{-\omega y},
\qquad
d_\eta(y)=\sqrt{1-e^{-2\omega y}}.
\]

## 2. Compact dyadic/gamma bridge

On `0<t<log 2`, the same weighted construction gives

\[
\boxed{
K_{\rm br}^-=K_{\rm br}^++D_{\rm br},
\qquad D_{\rm br}\succeq0.
}
\tag{L-91731.2}
\]

The returned multiplier is `e^(-omega t)`. This is the compact bridge of
`L-91530`; the old free-pole tail is absent before norms are taken.

## 3. Gamma beta channel

The positive beta/Laplace representation

\[
\pi^\omega
\frac{\Gamma((s-\omega)/2)}
     {\Gamma((s+\omega)/2)}
=
\frac{2\pi^\omega}{\Gamma(\omega)}
\int_0^\infty
 e^{-(s-\omega)t}
 (1-e^{-2t})^{\omega-1}dt
\]

gives weighted hard and safe kernels satisfying

\[
\boxed{
K_\Gamma^-=K_\Gamma^++D_\Gamma,
\qquad D_\Gamma\succeq0,
}
\tag{L-91731.3}
\]

again with returned multiplier `e^(-omega t)`.

## 4. Rational channel

The factor

\[
b_\omega(s)^2
=
\left(\frac{s-\omega}{s+\omega}\right)^2
\]

is inner and therefore contributes a lossless returned channel with zero
Julia detail.

## 5. Completed ordered source identity

The complete arithmetic hard kernel is

\[
K_{\rm arith}^-
=
K_\eta^-K_{\rm br}^-K_\Gamma^-.
\]

The safe returned kernel is

\[
K_{\rm arith}^+
=
K_\eta^+K_{\rm br}^+K_\Gamma^+.
\]

By `L-91730`,

\[
\boxed{
\begin{aligned}
K_{\rm arith}^-
={}&K_{\rm arith}^+\\
&+D_\eta K_{\rm br}^-K_\Gamma^-\\
&+K_\eta^+D_{\rm br}K_\Gamma^-\\
&+K_\eta^+K_{\rm br}^+D_\Gamma.
\end{aligned}
}
\tag{L-91731.4}
\]

Every term is a positive full-carrier kernel. Carrier modulations, physical
delay phases, reflection, and bosonic second quantization commute with the
weighted multipliers.

## 6. Analytic transfer factor

`L-91631` identifies the corresponding analytic factors in

\[
\frac{\xi(s-\omega)}{\xi(s+\omega)}
=
\frac{I_\eta(s-\omega)}{I_\eta(s+\omega)}
b_\omega(s)^2
\frac{F_L(s-s_0)}{F_L(s-s_1)}
\pi^\omega
\frac{\Gamma((s-\omega)/2)}
     {\Gamma((s+\omega)/2)}.
\]

Thus all arithmetic factors now have explicit positive or lossless source
channels. No source-side pole or unbounded same-space inverse remains.

## 7. Remaining issue

The exact open theorem is to identify the returned and detail spaces in
(L-91731.4) with the canonical critical and deterministic stable model
outputs, leaving no hyperbolic or auxiliary component.
