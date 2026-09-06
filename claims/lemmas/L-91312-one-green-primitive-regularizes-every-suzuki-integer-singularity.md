# L-91312 — One Green primitive regularizes every Suzuki integer singularity; only the global Hardy tail remains

Claim ID: `L-91312`  
Status: **EXACT LOCAL REGULARIZATION AND HARDY TRANSFORM; GLOBAL NORM REMAINS INNERNESS-BEARING**  
Created: 2026-08-12  
RH status: **unproved**

## 1. Primitive of the arithmetic kernel

For `omega>0`, define

\[
 A_\omega(x)=\int_1^x h_\omega(y)\,dy,
 \qquad x\ge1,
 \tag{L-91312.1}
\]

and set `A_omega(x)=0` for `0<x<1`.

By `R-91303`, near every integer `N`,

\[
 h_\omega(x)
 =C_{\omega,N}(x-N)^{\omega-1}
 +\text{less singular terms}
 \qquad(x\downarrow N),
 \tag{L-91312.2}
\]

with finite nonzero `C_(omega,N)`. Therefore

\[
 \boxed{
 A_\omega(x)
 =A_\omega(N)
 +\frac{C_{\omega,N}}\omega(x-N)^\omega
 +o(|x-N|^\omega).
 }
 \tag{L-91312.3}
\]

Thus `A_omega` is locally bounded and locally square integrable at every
integer for every `omega>0`. One primitive raises the singular exponent from
`omega-1` to `omega` and removes the hard `omega=1/2` local threshold.

## 2. Logarithmic causal vector

Put

\[
 f_\omega(t)
 =e^{-t/2}A_\omega(e^t)\mathbf1_{t\ge0}.
 \tag{L-91312.4}
\]

For every finite `L`, `f_omega` belongs to `L^2(0,L)`. Consequently the finite
Hankel operator

\[
 (\mathsf J_{\omega,L}u)(s)
 =\int_0^L f_\omega(s+t)u(t)\,dt,
 \qquad 0<s<L,
 \tag{L-91312.5}
\]

is Hilbert--Schmidt whenever it is restricted to the triangle `s+t<=L`; more
generally every compactly supported smooth cutoff of `f_omega(s+t)` is
Hilbert--Schmidt. The local integer singularities no longer obstruct ordinary
Fredholm determinants.

## 3. Exact Hardy transform

Let

\[
 \Theta_\omega(z)
 =\frac{\xi(\frac12-\omega-iz)}
        {\xi(\frac12+\omega-iz)}.
 \tag{L-91312.6}
\]

In the initial upper half-plane of convergence, integration by parts in the
inverse-Mellin definition of `h_omega` gives

\[
 \boxed{
 \widehat f_\omega(z)
 =\int_0^\infty f_\omega(t)e^{izt}\,dt
 =\frac{\Theta_\omega(z)}{\frac12-iz}.
 }
 \tag{L-91312.7}
\]

The factor

\[
 r(z)=\frac1{\frac12-iz}
 \tag{L-91312.8}
\]

is one fixed outer vector in `H^2(C_+)`.

## 4. Exact separation of local and global difficulties

The following are now cleanly separated:

```text
local integer singularities of h_omega:
  removed unconditionally by one primitive;

finite-interval Hilbert--Schmidt realization:
  available unconditionally for every omega>0;

global L2 norm of f_omega:
  finite iff Theta_omega is inner;

factor-four annular energy of PR #402:
  finite iff the same global L2 norm is finite.
```

In particular, a hard-range canonical construction should be built from the
primitive kernel `f_omega`, not by asking a fixed local dilation polynomial to
make `h_omega` Hilbert--Schmidt.

## 5. Corrected integrated-Marchenko target

For each finite `L`, form the compact integrated Hankel operator

\[
 \mathsf J_{\omega,L}
 \tag{L-91312.9}
\]

with a declared endpoint cutoff and the finite lossless `p=2` boundary port.
The corrected route-I theorem is:

> **Integrated Marchenko Optical Identity (`IMOI_omega`).**  
> The finite Fredholm systems of `J_(omega,L)` admit a source-ordered
> conservative realization whose visible transfer is
> `Theta_omega(z)r(z)`, whose one-dimensional outer port is `r`, and whose
> auxiliary defect is exactly the global Jordan/Fock plus theta/Brownian
> reserve. The realization is compatible as `L` increases, and its inductive
> limit is lossless.

Because `r` is outer, losslessness of the product channel forces innerness of
`Theta_omega`. Conversely, under innerness the complete norm is exactly the
outer-vector norm.

The local compactness and the outer-port algebra are exact. Compatibility,
losslessness, and the global source/output Gram identity are the remaining
RH-bearing parts.
