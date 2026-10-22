# L-91311 — Suzuki's integer singularities are one endpoint singularity under global Jordan convolution

Claim ID: `L-91311`  
Status: **EXACT GLOBAL ARITHMETIC DECONVOLUTION; POSITIVE DILATION OF THE INVERSE REMAINS OPEN**  
Created: 2026-08-12  
RH status: **unproved**

## 1. Generalized-Jordan coefficients

For `omega>0`, put

\[
 c_\omega(n)
 =n^\omega\prod_{p\mid n}(1-p^{-2\omega})
 =\frac{J_{2\omega}(n)}{n^\omega}.
 \tag{L-91311.1}
\]

The coefficients are positive and multiplicative. Their Dirichlet series is

\[
 \boxed{
 C_\omega(s)
 :=\sum_{n\ge1}\frac{c_\omega(n)}{n^s}
 =\frac{\zeta(s-\omega)}{\zeta(s+\omega)}
 }
 \tag{L-91311.2}
\]

in its half-plane of absolute convergence.

At one prime,

\[
 \sum_{k\ge0}c_\omega(p^k)p^{-ks}
 =\frac{1-p^{-(s+\omega)}}{1-p^{-(s-\omega)}}.
 \tag{L-91311.3}
\]

## 2. Explicit Dirichlet inverse

Let `d_omega` be the Dirichlet-convolution inverse of `c_omega`:

\[
 c_\omega*d_\omega=\varepsilon.
 \tag{L-91311.4}
\]

It is multiplicative, `d_omega(1)=1`, and

\[
 \boxed{
 d_\omega(p^k)
 =-(p^{2\omega}-1)p^{-k\omega}
 \qquad(k\ge1).
 }
 \tag{L-91311.5}
\]

Indeed,

\[
 \sum_{k\ge0}d_\omega(p^k)p^{-ks}
 =\frac{1-p^{-(s-\omega)}}{1-p^{-(s+\omega)}}
 =C_\omega(s)^{-1}.
 \tag{L-91311.6}
\]

The inverse coefficients are signed. The positive generalized-Jordan forward
channel therefore cannot be inverted as a positive scalar convolution.

## 3. Arithmetic convolution operator

For an arithmetic sequence `a` and a function `f` on `[1,infinity)`, define

\[
 (\mathcal T_af)(x)
 =\sum_{n\le x}a(n)f(x/n).
 \tag{L-91311.7}
\]

Whenever the finite sums are defined,

\[
 \boxed{
 \mathcal T_a\mathcal T_b
 =\mathcal T_{a*b}.
 }
 \tag{L-91311.8}
\]

This is immediate after writing `n=dm` and regrouping by the product.

## 4. Exact deconvolution of Suzuki's kernel

Suzuki's kernel is

\[
 h_\omega(x)
 =\frac1x\sum_{n\le x}c_\omega(n)
 g_\omega(n/x).
 \tag{L-91311.9}
\]

Put

\[
 f_\omega(y)=g_\omega(1/y),
 \qquad
 H_\omega(x)=xh_\omega(x).
 \tag{L-91311.10}
\]

Then

\[
 \boxed{
 H_\omega=\mathcal T_{c_\omega}f_\omega.
 }
 \tag{L-91311.11}
\]

Applying the exact inverse gives

\[
 \boxed{
 f_\omega=\mathcal T_{d_\omega}H_\omega.
 }
 \tag{L-91311.12}
\]

Equivalently, for every `x>=1`,

\[
 \boxed{
 g_\omega(1/x)
 =x\sum_{n\le x}\frac{d_\omega(n)}n
 h_\omega(x/n).
 }
 \tag{L-91311.13}
\]

All integer singularities of `h_omega` therefore arise by applying one
positive generalized-Jordan arithmetic convolution to the single endpoint
singularity of `g_omega` at `1`.

## 5. Consequences for the canonical route

`R-91303` proves that a fixed single-prime dilation polynomial cannot cancel
the integer singularities in the hard range. Equation (L-91311.13) identifies
the correct global operation:

```text
native Suzuki kernel
  -- signed all-prime Dirichlet inverse -->
one archimedean endpoint kernel.
```

This does not yet prove positivity. The inverse coefficients in (L-91311.5)
are signed, and using them termwise would recreate the arithmetic sign problem.
The viable construction is instead:

1. retain the positive forward Jordan channel in its bosonic Fock dilation;
2. realize the signed inverse as the visible transfer of a conservative
   colligation, with its defect stored in the theta/Gamma/Poisson reserve;
3. regularize the one remaining endpoint singularity by one Green primitive or
   by singular Marchenko theory;
4. recover the canonical system only after the complete optical identity is
   proved.

Thus the all-prime Fock route and the Suzuki canonical route are not merely
parallel. The former supplies the only source-faithful candidate dilation of
the global inverse required by the latter.

## 6. Exact remaining theorem

The canonical side of `AOT_a` can now be stated as a concrete conservative
inverse problem:

> Construct a positive-metric unitary dilation of `T_(d_omega)` on the completed
> Jordan/Fock source whose scalar transfer acts by (L-91311.13), whose auxiliary
> defect is exactly the theta/Gamma/Poisson/`p=2` reserve, and whose endpoint
> output is the Green-regularized `g_omega` channel.

An abstract inverse of `T_(c_omega)` or a signed coefficientwise estimate does
not suffice.
