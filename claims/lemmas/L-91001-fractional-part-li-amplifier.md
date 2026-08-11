# L-91001 — Fractional-part Li amplifier and a spectral-radius criterion

Claim ID: `L-91001`  
Title: The Euler fractional-part remainder maps every zeta zero by the reciprocal Li Möbius map, putting critical-line zeros on the unit circle and every right off-line zero strictly outside; weighted power moments have spectral radius one exactly under RH  
Status: **PROPOSED COMPLETE EXACT ANALYTIC THEOREM — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-12  
Dependencies: Euler summation for zeta, the functional equation and zero-counting local finiteness  
Scope: an exact nonlinear RH criterion and positive-kernel interface; no unconditional bound for the resulting moments

## 1. Euler's fractional-part remainder

For `Re s>1`, Euler summation gives

\[
\zeta(s)=\frac{s}{s-1}
-s\int_1^\infty \{x\}x^{-s-1}\,dx.
\tag{L-91001.1}
\]

Define

\[
\boxed{
A(s)=\frac{s}{s-1}-\zeta(s).
}
\tag{L-91001.2}
\]

Because `0<= {x}<1`, the integral

\[
\boxed{
A(s)=s\int_1^\infty\{x\}x^{-s-1}\,dx
=s\int_0^\infty\{e^t\}e^{-st}\,dt
}
\tag{L-91001.3}
\]

converges locally uniformly for `Re s>0`. Thus (L-91001.3) is the analytic continuation of (L-91001.2) throughout the open right half-plane, with the singularity at one removable.

## 2. Exact image of a zeta zero

If `rho` is a nontrivial zero, then

\[
\boxed{
A(\rho)=\frac{\rho}{\rho-1}.
}
\tag{L-91001.4}
\]

Consequently

\[
\boxed{
|A(\rho)|^2-1
=\frac{2\operatorname{Re}\rho-1}{|\rho-1|^2}.
}
\tag{L-91001.5}
\]

Hence

```text
Re rho = 1/2  <=> |A(rho)|=1;
Re rho > 1/2  <=> |A(rho)|>1;
Re rho < 1/2  <=> |A(rho)|<1.
```

The functional-equation reflection is reciprocal:

\[
\boxed{
A(1-\rho)=A(\rho)^{-1}.
}
\tag{L-91001.6}
\]

Moreover the standard Li variable is exactly the inverse amplifier,

\[
\boxed{
1-\frac1\rho=\frac{\rho-1}{\rho}=A(\rho)^{-1}.
}
\tag{L-91001.7}
\]

Thus `A` is not merely analogous to the Li map: it is its functional-equation reciprocal.

## 3. A summable symmetric weight

Fix an integer `M>=2` and put

\[
\boxed{
W_M(s)=\frac1{[(s+4)(5-s)]^M}.
}
\tag{L-91001.8}
\]

This weight is analytic and nonzero on the closed critical strip, satisfies

\[
W_M(1-s)=W_M(s),
\tag{L-91001.9}
\]

and on the critical line is positive real:

\[
W_M\!\left(\frac12+it\right)
=\left(\frac1{(9/2)^2+t^2}\right)^M>0.
\tag{L-91001.10}
\]

Since the zero count is `O(T log T)`,

\[
\sum_\rho m_\rho |W_M(\rho)|<\infty.
\tag{L-91001.11}
\]

Therefore the moments

\[
\boxed{
\mathfrak M_{r,M}
=\sum_\rho m_\rho W_M(\rho)A(\rho)^r,
\qquad r=0,1,2,\ldots,
}
\tag{L-91001.12}
\]

are absolutely convergent. No Hadamard regularisation is required.

## 4. RH gives unit spectral radius

Under RH, every zero satisfies `|A(rho)|=1`, and therefore

\[
|\mathfrak M_{r,M}|
\le\sum_\rho m_\rho|W_M(\rho)|
=:C_M.
\tag{L-91001.13}
\]

In particular,

\[
\limsup_{r\to\infty}|\mathfrak M_{r,M}|^{1/r}\le1.
\tag{L-91001.14}
\]

## 5. A false-RH zero forces exponential moment growth

Assume there is a zero to the right of the critical line. Put

\[
R=\sup_\rho |A(\rho)|.
\tag{L-91001.15}
\]

By (L-91001.5), `R>1`. As `|Im rho|->infinity`, uniformly for `0<Re rho<1`,

\[
|A(\rho)|=1+O(|\operatorname{Im}\rho|^{-2}).
\tag{L-91001.16}
\]

Hence the supremum `R` is attained by a finite nonempty packet of zeros. The map

\[
s\longmapsto\frac{s}{s-1}
\]

is injective, so distinct zeros give distinct amplifier values. Splitting (L-91001.12) into the finite maximal packet and the strictly smaller remainder gives

\[
\mathfrak M_{r,M}
=\sum_{j=1}^J c_j z_j^r+O((R-\eta)^r),
\qquad |z_j|=R,
\quad c_j\ne0,
\tag{L-91001.17}
\]

for some `eta>0`.

The generating function of the leading exponential polynomial is

\[
\sum_{r\ge0}\left(\sum_jc_jz_j^r\right)w^r
=\sum_j\frac{c_j}{1-z_jw}.
\tag{L-91001.18}
\]

Its poles at the distinct points `w=z_j^{-1}` cannot cancel. Therefore its radius of convergence is exactly `R^{-1}` and

\[
\boxed{
\limsup_{r\to\infty}|\mathfrak M_{r,M}|^{1/r}=R>1.
}
\tag{L-91001.19}
\]

## 6. Exact criterion

Combining the two directions,

\[
\boxed{
\mathrm{RH}
\Longleftrightarrow
\limsup_{r\to\infty}|\mathfrak M_{r,M}|^{1/r}\le1
}
\tag{L-91001.20}
\]

for every, or equivalently for one, fixed integer `M>=2`.

This is a nonlinear spectral-radius form of the Li criterion. Its distinguishing feature is the positive fractional-part realization of the amplifier itself.

## 7. Proof boundary

Closed exactly here:

1. the positive fractional-part representation of `A`;
2. the exact reciprocal Li map at every zero;
3. strict unit-circle separation by horizontal zero displacement;
4. absolute weighted moment convergence;
5. exact spectral-radius dichotomy;
6. the RH equivalence (L-91001.20).

Open:

1. a prime/fractional-part proof that the moments have subexponential growth;
2. a reflected contour mechanism controlling the critical boundary;
3. RH.