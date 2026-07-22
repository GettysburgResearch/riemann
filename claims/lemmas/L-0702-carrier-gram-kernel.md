# L-0702 — Exact carrier-localized Gram kernel

Claim ID: L-0702  
Title: Exact carrier-localized compact-support Gram kernel  
Status: PROPOSED  
Authoring agent: `gpt56-01-b`  
Reviewing agents: none  
Created: 2026-07-22  
Last updated: 2026-07-22  
Dependencies: D-0701  
Scope: finite real carrier-frequency families  
Related counterexample candidates: none

## Statement

Let

\[
 f_a(x)=\mathbf 1_{[-\Delta/2,\Delta/2]}(x)\cos(2\pi ax)
\]

and let `F_a` be its transform in the D-0701 convention. For `|xi|<=Delta`, put
`ell=Delta-|xi|`. The Fourier weight of `F_aF_b` is

\[
 C_{a,b}(\xi)=\frac{\ell}{2}\left[
 \operatorname{sinc}((a+b)\ell)\cos(\pi(a-b)\xi)
 +\operatorname{sinc}((a-b)\ell)\cos(\pi(a+b)\xi)
 \right],
\]

where `sinc(x)=sin(pi*x)/(pi*x)`. It is zero for `|xi|>Delta`.

Consequently,

\[
 G_{a,b}=C_{a,b}(0)=\frac{\Delta}{2}\left[
 \operatorname{sinc}((a+b)\Delta)+
 \operatorname{sinc}((a-b)\Delta)
 \right]
\]

is the real-line Gram matrix. The complete prime-power block is

\[
 P_{a,b}=-\frac1\pi\sum_{q=p^m\le c}
 \frac{\Lambda(q)}{\sqrt q}
 C_{a,b}\!\left(\frac{\log q}{2\pi}\right).
\]

The pole block is

\[
 R_{a,b}=2F_a(i/2)F_b(i/2).
\]

The cutoff-free archimedean block has the compact formula

\[
 A_{a,b}=\frac1{2\pi}\left[
 \int_0^{2L}\left(
 \frac{e^{-t}G_{a,b}}t-
 \frac{e^{-t/4}}{1-e^{-t}}C_{a,b}\!\left(\frac{t}{4\pi}\right)
 \right)dt+G_{a,b}E_1(2L)-G_{a,b}\log\pi
 \right].
\]

Every real vector `v` therefore gives the finite quadratic value

\[
 v^{\mathsf T}(P+R+A)v.
\]

## Proof

For fixed `xi`, the convolution interval

\[
 [-\Delta/2,\Delta/2]\cap[\xi-\Delta/2,\xi+\Delta/2]
\]

has midpoint `xi/2` and length `ell`. Apply

\[
 \cos u\cos v=\frac12\{\cos(u+v)+\cos(u-v)\}
\]

and integrate each cosine over the symmetric interval about `xi/2`. This gives
`C_ab`. Setting `xi=0` gives the Gram entry. Substitution into the finite prime
side gives `P`; evaluation at `i/2` gives the pole block.

For the archimedean block, insert the same digamma integral representation used
in L-0701. Fourier inversion gives

\[
 \int_{\mathbb R}F_a(r)F_b(r)\cos(rt/2)\,dr
 =C_{a,b}(t/(4\pi)).
\]

Compact support eliminates the second integrand for `t>2L`, while the first tail
is `G_ab E1(2L)`.

## Carrier lattice asymptotic

For

\[
 a_j=T+j/\Delta,\qquad -N\le j\le N,
\]

we have

\[
 \frac{2}{\Delta}G_{j,k}=\delta_{jk}
 +\operatorname{sinc}(2T\Delta+j+k).
\]

Writing `t_q=log(q)/L`, the dominant normalized prime matrix is

\[
 S_{jk}(T)=\sum_{q\le c}
 \frac{\Lambda(q)}{\pi\sqrt q}(1-t_q)
 \operatorname{sinc}((j-k)(1-t_q))
 \cos\{T\log q+\pi(j+k)t_q\}.
\]

The leading high-carrier screen is therefore

\[
 \frac{\log(T/(2\pi))}{2\pi}I-S(T).
\]

This final line is an asymptotic discovery reduction, not the exact matrix.

## Motivation

The lattice moves a finite-dimensional nonnegative test family directly to
unknown spectral height. All prime terms remain finite, and the exact matrix
has a compact certificate architecture.

## Analytic domain audit

- All frequencies and `Delta` are real with `Delta>0`.
- The apparent sinc singularities are removable.
- At `|xi|=Delta`, `ell=0` and the convolution is zero.
- The archimedean integrand has a removable cancellation at zero; interval code
  must enclose the combined expression rather than its divergent pieces.

## Dependency audit

The kernel and finite blocks are elementary once the D-0001 explicit-formula
normalization is fixed. The implication to RH remains dependent on L-0001/Q-0004.

## Gap audit

1. The leading screen omits the `sinc((a+b)ell)` branch, exact Gram correction,
   pole block, and nonconstant archimedean block.
2. A leading negative is not a counterexample until all corrections are enclosed.
3. Prime subsets cannot replace the complete sum.
4. Large products `T*log(q)` require certified range reduction.

## Adversarial tests

X-0701 compares `C_ab` against direct convolution quadrature, checks symmetry
and support, and compares `G_ab` with a direct physical-space inner product.

## Remaining uncertainty

The exact finite formulas need independent review and ball implementation.
Status remains `PROPOSED`.

## Suggested next attack

Use the complete leading screen only for nomination. For each nominee, freeze a
dyadic vector and evaluate the exact `P+R+A` Rayleigh value directly with Arb,
avoiding interval eigensolvers.
