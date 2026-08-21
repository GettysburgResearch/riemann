# L-102103 — A safe common filter removes the half-order carrier from both quadratic–wavelet bridge channels

Claim ID: `L-102103`  
Status: **PROVED EXACT FILTER/KERNEL THEOREM**  
Created: 2026-08-21  
Depends on: PR #697 `L-101101`  
RH status: **not assumed**

Use PR #697's exact bridge `G_beta=C+A+Q`, where

\[
A=-{1\over3}JP_2A_\beta,
\qquad
Q=-{1\over3}JP_2(D-1)E_2,
\qquad
P_2=(I-\sqrt2S_2)(I-S_2)^2.
\]

Define

\[
\boxed{N=J(I-S_2)(I-\sqrt2S_2).}
\tag{L-102103.1}
\]

Applying `N` to all channels preserves the exact bridge:

\[
\boxed{G_\beta^\dagger=C^\dagger+A^\dagger+Q^\dagger.}
\tag{L-102103.2}
\]

The multiplier of `N` is

\[
\boxed{m(s)={(1-2^{-s})(1-\sqrt2\,2^{-s})\over s}.}
\tag{L-102103.3}
\]

The point `s=0` is removable. All new zeros lie on `Re(s)=0` or `Re(s)=1/2`, so no reciprocal-zeta pole at `s=rho-1/2`, `1/2<Re(rho)<1`, is cancelled.

Every source-atom kernel of `A` and `Q` is supported on ratio eight. The two finite differences enlarge support to ratio 32. Because `I-S_2` has zero total logarithmic integral, the final `J` remains compact:

\[
\boxed{\operatorname{supp}K_A^\dagger,\operatorname{supp}K_Q^\dagger\subset[1,32].}
\tag{L-102103.4}
\]

Since `m(1/2)=0`, both kernels have the true continuous moment

\[
\boxed{\int_1^{32}K_i^\dagger(y)y^{-3/2}\,dy=0,\qquad i\in\{A,Q\}.}
\tag{L-102103.5}
\]

The kernels are continuous and piecewise smooth; for `k_i(x)=x^(-1/2)K_i^dagger(1/x)`, the distributional derivative has finite total variation `V_i`. The composite trapezoid/Bernoulli remainder gives

\[
\boxed{
\left|\sum_{m\ge1}{1\over\sqrt m}K_i^\dagger(Y/m)\right|
\le {V_i\over12}Y^{-3/2}.
}
\tag{L-102103.6}
\]

This is a simultaneous Type-I power saving on the same two bridge channels. The zero moment is not reused on their balanced remainder.
