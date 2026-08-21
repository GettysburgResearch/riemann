# L-9516 — Reflected Selberg identity for the vertical prime energy

Claim ID: `L-9516`  
Title: The product of the two conjugate zeta twists converts Selberg's quadratic identity into the exact Hermitian square required by the Hardy-energy route  
Status: **PROPOSED EXACT ALGEBRAIC LEMMA PENDING INDEPENDENT REVIEW**  
Authoring agent: `gpt56-08`  
Created: 2026-08-07  
Dependencies: elementary Dirichlet-series differentiation; `L-21503`; `L-9512`  
Scope: initially `Re(s)>1`; compact safe windows then give the finite product-scale packet

## 1. A general Selberg coefficient identity

Let
\[
A(s)=\sum_{n\ge1}a(n)n^{-s}
\]
be a Dirichlet series with convolution inverse
\[
B(s)=\sum_{n\ge1}b(n)n^{-s}=A(s)^{-1}
\]
in one absolute-convergence half-plane. Define its generalized von Mangoldt
sequence by
\[
-\frac{A'}A(s)=\sum_{n\ge1}\Lambda_A(n)n^{-s}.
\]
Then
\[
\Lambda_A=-b*(a\log)
\]
and differentiating once gives
\[
\boxed{
 b*(a\log^2)
 =\Lambda_A\log+\Lambda_A*\Lambda_A.
}
\tag{L-9516.1}
\]
Indeed the Dirichlet series of both sides is
\[
\frac{A''(s)}{A(s)}
=-\left(-\frac{A'}A\right)'(s)
 +\left(-\frac{A'}A(s)\right)^2.
\]

## 2. Conjugate zeta twists

For real `t`, let
\[
\chi_t(n)=n^{-it}.
\]
Put
\[
a_+(n)=\chi_t(n),\qquad
b_+(n)=\mu(n)\chi_t(n),\qquad
\Lambda_+(n)=\Lambda(n)\chi_t(n),
\]
and define `a_-`, `b_-`, `Lambda_-` by replacing `t` with `-t`.
Their Dirichlet series are
\[
A_+(s)=\zeta(s+it),\qquad
A_-(s)=\zeta(s-it).
\]

For the product
\[
A_\times=A_+A_-
\]
the coefficient and inverse sequences are
\[
a_\times=a_+*a_-,\qquad
b_\times=b_+*b_-,
\]
while
\[
\Lambda_\times=\Lambda_++\Lambda_-.
\]
Apply (L-9516.1) to `A_times`, `A_+`, and `A_-`. The linear logarithmic terms
cancel, and commutativity of Dirichlet convolution gives the exact coefficient
identity
\[
\boxed{
\begin{aligned}
&b_\times*(a_\times\log^2)
-b_+*(a_+\log^2)
-b_-*(a_-\log^2)\\
&\hspace{25mm}=2\,\Lambda_+*\Lambda_-.
\end{aligned}}
\tag{L-9516.2}
\]

The coefficient on the right is explicitly
\[
2\sum_{ab=n}\Lambda(a)\Lambda(b)
\left(\frac ab\right)^{-it}.
\tag{L-9516.3}
\]
No zero hypothesis or limiting argument enters this identity.

## 3. Exact Hermitian square

For real `sigma>1`, take Dirichlet series in (L-9516.2). Since
\[
-\frac{\zeta'}\zeta(\sigma-it)
=\overline{-\frac{\zeta'}\zeta(\sigma+it)},
\]
we obtain
\[
\boxed{
2\left|\frac{\zeta'}\zeta(\sigma+it)\right|^2
=\mathcal C_\times(\sigma,t)
 -\mathcal C_+(\sigma,t)
 -\mathcal C_-(\sigma,t),
}
\tag{L-9516.4}
\]
where each `C` is the absolutely convergent Dirichlet series of the
corresponding left-side convolution in (L-9516.2).

This is the missing reflected square. The scalar centered Selberg equation
produces `H(z)^2`; the conjugate-product equation produces the Hermitian quantity
`H(z) overline{H(z)}` after the pole model is subtracted or killed by a safe
window.

## 4. Windowed vertical energy

Let `H` be a real compact safe window and write its bilateral Laplace transform
as `Hhat`. For `alpha>1/2`, put
\[
w_{H,\alpha}(t)
=\left|\widehat H(\alpha+it)\right|^2\ge0.
\]
Multiplying (L-9516.4), with `sigma=1/2+alpha`, by this weight and integrating
gives
\[
\boxed{
\begin{aligned}
&2\int_{\mathbb R}w_{H,\alpha}(t)
 \left|\frac{\zeta'}\zeta
 \left(\frac12+\alpha+it\right)\right|^2dt\\
&\quad=
\int_{\mathbb R}w_{H,\alpha}(t)
 [\mathcal C_\times-\mathcal C_+-\mathcal C_-]
 \left(\frac12+\alpha,t\right)dt.
\end{aligned}}
\tag{L-9516.5}
\]

Because `H` is compactly supported, the Fourier transform in `t` of
`w_(H,alpha)` is the compactly supported autocorrelation of
\[
u\mapsto e^{-\alpha u}H(u).
\]
Consequently the right side of (L-9516.5) is an exact finite-ratio arithmetic
packet: only factor pairs whose logarithmic ratio lies in one fixed compact
interval occur.

For the boundary-safe high-order windows `H^[K+1]`, the zeta-pole contribution
is killed to the declared order. The remaining left side is precisely the
positive vertical energy used by the prime Hardy, balanced-semiprime, and
analytic-totient routes, after the fixed normalization adapters are applied.

## 5. Product-scale forcing

The forcing in (L-9516.5) is source bound. Its inverse coefficients are
\[
b_\times(n)
=\sum_{de=n}\mu(d)\mu(e)
 \left(\frac de\right)^{-it}.
\tag{L-9516.6}
\]
Thus integration in `t` produces the same Möbius-weighted Farey/ratio packet
isolated in `L-9515` and `L-23002`, but now as the exact forcing of a positive
Hermitian square rather than as an externally postulated cancellation.

Applying the exact finite Möbius resolvent `L-23201` to both inverse factors
makes every coefficient through a prescribed endpoint finite and typed. This is
the input for the terminal contraction proposal `L-9517`.

## 6. Significance

`L-9516` removes one structural mismatch that survived the real-exponential
Selberg-Hankel construction:

```text
old scalar adjoint:     H(z)^2
required Hardy energy:  |H(z)|^2
reflected product:      H(z) overline(H(z)) exactly.
```

It does not by itself bound the forcing packet. The source-specific high-order
contraction of that packet remains the arithmetic theorem.

## 7. Proof boundary

Closed here:

- the generalized Selberg coefficient identity;
- the conjugate-product subtraction;
- the exact Hermitian square;
- the compact ratio support after window integration;
- the explicit Möbius inverse coefficients.

Open here:

- a critical-scale upper bound for the reflected forcing;
- the terminal rate needed for RH.
