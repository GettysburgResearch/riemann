# L-105405 — The cofinal F1 trace is one compact adelic Gram form

Claim ID: `L-105405`

Status: **PROVED EXACT TRACE REDUCTION; DISTINCT-PRODUCT ESTIMATE OPEN**

Freeze the ratio-eight centered-ray theorem and common source factorization of
PR #719 at head

```text
847e7feeac864bda4e3df38329d1a70c59aa4814.
```

For one completion time `tau`, write the exact carrier-recombined primitive
coordinates in logarithmic scale as

\[
A_\tau(u)
=
\sum_n\frac{\sigma_\tau(n)}{\sqrt n}
 k_A(u-\log n),
\]

\[
B_\tau(u)
=
\sum_n\frac{\sigma_\tau(n)}{\sqrt n}
 k_B(u-\log n).
\tag{L-105405.1}
\]

Here `sigma_tau` is the literal labelled completion-tangent source and the
fixed kernels `k_A,k_B` are the curvature and slope coefficients of the
centered filtered disk. By PR #719 `L-102732`, both kernels are supported on
one ratio-eight shell.

For one logarithmic block `I_T=[T,T+1]`, define

\[
\mathcal K_T(n,m)
=
\int_{I_T}
\left[
\frac1{24}k_A(u-\log n)k_A(u-\log m)
+
2k_B(u-\log n)k_B(u-\log m)
\right]du.
\tag{L-105405.2}
\]

Then finite Fubini and `L-105404` give

\[
\boxed{
\int_{I_T}\mathcal H_{\rm prim}(A_\tau,G_\tau)\,du
=
\sum_{n,m}
\frac{\sigma_\tau(n)\sigma_\tau(m)}{\sqrt{nm}}
\mathcal K_T(n,m).
}
\tag{L-105405.3}
\]

## 1. Positive-semidefinite trace kernel

For every finitely supported scalar sequence `c_n`,

\[
\sum_{n,m}c_nc_m\mathcal K_T(n,m)
=
\int_{I_T}
\left[
\frac1{24}\left|\sum_nc_nk_A(u-\log n)\right|^2
+
2\left|\sum_nc_nk_B(u-\log n)\right|^2
\right]du
\ge0.
\tag{L-105405.4}
\]

Thus `mathcal K_T` is a literal Hodge/Gram trace kernel, not a formal positive
matrix attached after source collapse.

Because the two kernels have ratio-eight support,

\[
\boxed{
\mathcal K_T(n,m)=0
\quad\text{unless}\quad
\frac18<\frac nm<8.
}
\tag{L-105405.5}
\]

## 2. Adelic coordinates

For every surviving pair write uniquely

\[
n=ga,\qquad m=gb,\qquad (a,b)=1.
\]

Then the archimedean coordinate is `log(a/b)` in a fixed compact interval,
while the non-archimedean separation is the coprime pair `(a,b)` and common
core `g`. Equation (L-105405.3) becomes the exact adelic trace

\[
\sum_{g}\sum_{\substack{(a,b)=1\\1/8<a/b<8}}
\frac{\sigma_\tau(ga)\sigma_\tau(gb)}
     {g\sqrt{ab}}
\mathcal K_T(ga,gb).
\tag{L-105405.6}
\]

No generic labelled-to-physical contraction is invoked.

## 3. Closed and open sectors

The frozen PR #719 theorems `L-102702`, `L-102703` and `L-102708` close, at
polylogarithmic/subpower cost:

```text
coefficient diagonal n=m;
same physical product/factor-pair sector;
duplicate-owner representations;
same-owner square cores;
all ratios outside [1/8,8].
```

Consequently the only unclosed part of (L-105405.3) is the signed
`n!=m`, different-owner, distinct-product near-collision term.

Call the assertion that its positive contribution is `e^{o(T)}`, uniformly
and integrably in `tau`,

\[
\boxed{\mathrm{F1ATO105405}.}
\]

Since the `(tau,u)` domain of one block has measure one, Cauchy gives

\[
\left(
\int_0^1\int_{I_T}
\sqrt{\mathcal H_{\rm prim}}\,du\,d\tau
\right)^2
\le
\int_0^1\int_{I_T}
\mathcal H_{\rm prim}\,du\,d\tau.
\tag{L-105405.7}
\]

Therefore

\[
\boxed{
\mathrm{F1ATO105405}
\Longrightarrow
\mathrm{F1PE105403}
\Longrightarrow
\mathrm{TRF102750}
\Longrightarrow
\mathrm{RH}.
}
\tag{L-105405.8}
\]

All finite geometry, carrier quotient, trace construction, diagonal sectors and
far-ratio sectors are now closed. The remaining statement is one literal
arithmetic off-diagonal estimate.
