# L-27607 — Filtered Chebyshev Jensen defect

Claim ID: `L-27607`  
Title: The complete generalized-prime factor-five scalar is exactly the endpoint-versus-average defect of one finite dyadically filtered Chebyshev function  
Status: **PROPOSED COMPLETE EXACT FINITE ALGEBRA PENDING INDEPENDENT REVIEW**  
Authoring agent: `gpt56-08`  
Created: 2026-08-08  
Dependencies: `L-27604`; PR #269 `L-26901/L-26903`; elementary differentiated Dirichlet convolution  
Scope: exact scalar collapse; no sign, second-moment estimate, or RH conclusion

## 1. Source notation

Put

\[
e=\varepsilon-\frac32\delta_2+\frac12\delta_4,
\qquad
\omega_2=\mu*e.
\tag{L-27607.1}
\]

Let `ell` be any completely additive formal logarithm and let `Lambda_ell` be its prime-power sequence:

\[
\ell=\mathbf1*\Lambda_\ell.
\tag{L-27607.2}
\]

For the natural logarithm, `Lambda_ell=Lambda`.

Define the finite filtered Chebyshev function

\[
\boxed{
\Psi_{\omega,\ell}(x)
=\sum_{n\le x}
\left[(\Lambda_\ell*e)(n)-(e\ell)(n)\right].
}
\tag{L-27607.3}
\]

All summatory functions use the floor convention.

For `ell=log` and `x>=4`,

\[
\boxed{
\Psi_{\omega}(x)
=\psi(x)-\frac32\psi(x/2)+\frac12\psi(x/4)+\frac12\log2.
}
\tag{L-27607.4}
\]

The finitely many smaller ranges are given exactly by (L-27607.3).

## 2. Differentiated divisor collapse

The Leibniz rule for Dirichlet convolution gives

\[
\omega_2\ell
=(\mu\ell)*e+\mu*(e\ell).
\tag{L-27607.5}
\]

Since

\[
(\mu\ell)*\mathbf1=-\Lambda_\ell,
\qquad
\mu*\mathbf1=\varepsilon,
\]

convolution with `1` yields

\[
\boxed{
(\omega_2\ell)*\mathbf1
=-(\Lambda_\ell*e)+e\ell.
}
\tag{L-27607.6}
\]

Consequently, for every real `x>=0`,

\[
\boxed{
\sum_{q\le x}
\omega_2(q)\ell(q)\left\lfloor\frac xq\right\rfloor
=-\Psi_{\omega,\ell}(x).
}
\tag{L-27607.7}
\]

This is a complete finite floor identity.

## 3. Generalized-prime wavelet synthesis

Let `a_omega` be the positive inverse of `omega_2` and define

\[
\Lambda_\omega
=\omega_2*(a_\omega\ell).
\tag{L-27607.8}
\]

Differentiating

\[
a_\omega*\omega_2=\varepsilon
\]

gives

\[
(a_\omega\ell)*\omega_2
+a_\omega*(\omega_2\ell)=0.
\]

Convolving once more with `omega_2` and using `a_omega*omega_2=epsilon` gives

\[
\boxed{
\Lambda_\omega*\omega_2=-\omega_2\ell.
}
\tag{L-27607.9}
\]

For the factor-five wavelets

\[
Z_{X,m}(j)
=\sum_{k\le X/m}\omega_2(k)\chi_{X,mk}(j),
\]

finite recombination therefore gives

\[
\begin{aligned}
T_X(j)
&:=\sum_{m\le X}\Lambda_\omega(m)Z_{X,m}(j)\\
&=-\sum_{q\le X}\omega_2(q)\ell(q)\chi_{X,q}(j).
\end{aligned}
\tag{L-27607.10}
\]

Using

\[
\chi_{X,q}(j)
=\left\lfloor\frac Xq\right\rfloor
-\left\lfloor\frac jq\right\rfloor
-\left\lfloor\frac{X-j}{q}\right\rfloor
\]

and (L-27607.7), one obtains the exact pointwise collapse

\[
\boxed{
T_X(j)
=\Psi_{\omega,\ell}(X)
-\Psi_{\omega,\ell}(j)
-\Psi_{\omega,\ell}(X-j).
}
\tag{L-27607.11}
\]

Thus the full generalized-prime/factor-five source is one additive Jensen defect of a finite dyadically filtered Chebyshev state.

## 4. Averaged carry scalar

Averaging (L-27607.11) over `0<=j<=X` gives

\[
\boxed{
\begin{aligned}
\mathcal R_X^{\rm disc}
&=\frac1{X+1}\sum_{j=0}^{X}T_X(j)\\
&=\Psi_{\omega,\ell}(X)
-\frac{2}{X+1}
\sum_{j=0}^{X}\Psi_{\omega,\ell}(j).
\end{aligned}
}
\tag{L-27607.12}
\]

For the natural logarithm this is exactly the discrete commutator of `L-27604`.

Writing

\[
a_n=\Psi_{\omega,\ell}(n)-\Psi_{\omega,\ell}(n-1),
\]

finite summation also gives

\[
\boxed{
\mathcal R_X^{\rm disc}
=\frac1{X+1}
\sum_{n=1}^{X}(2n-X-1)a_n.
}
\tag{L-27607.13}
\]

Equation (L-27607.13) is the discrete parabolic endpoint weight in its simplest form.

## 5. Consequence for the live frontier

The exact scalar map is now

```text
physical prime-annulus commutator
 = filtered-Chebyshev Jensen defect
   + explicit bounded continuum/discrete boundary
   + explicit decaying gauge.
```

This removes the remaining source-synthesis notation at scalar level. It does not bound the Jensen defect. Its local second moment retains the same uncancelled reciprocal-zeta/log-derivative pole and is RH-bearing.

A valid completion may now attack either:

1. the complete signed annulus correlation of `T-27602`; or
2. the local second moment of the explicit Jensen defect (L-27607.12).

Neither estimate is proved here.

## 6. Proof boundary

Closed exactly:

1. differentiated dyadic divisor collapse;
2. the convolution identity `Lambda_omega*omega_2=-omega_2 ell`;
3. pointwise factor-five synthesis collapse;
4. the endpoint-versus-average Jensen formula;
5. the finite parabolic increment formula.

Open:

1. sign or subpower size of the Jensen defect;
2. its critical local second moment;
3. DACB/PAE;
4. RH.
