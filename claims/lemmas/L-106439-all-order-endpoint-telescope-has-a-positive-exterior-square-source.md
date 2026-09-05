# L-106439 — Every endpoint derivative block has an exterior-square positive source

Claim ID: `L-106439`  
Status: **PROVED EXACT AT FINITE REGULAR SCOPE; ACTUAL XI SOURCE IDENTITY UNCONDITIONAL**  
Created: 2026-08-25  
Depends on: `L-106400--L-106401`; the positive even Xi Fourier kernel  
RH status: **not assumed**

The two-rung endpoint cancellation extends to a direct block from `F` to
`F^(K)` for every `K>=1`.  No intermediate derivative companion occurs.

## 1. Exact endpoint block

Let `F` be real entire, or a real polynomial on finite regular scope.  Put

\[
G=F^{(K)}
\]

and, for `lambda>0`, define

\[
\boxed{
U_{K,\lambda}
 ={(F-i\lambda F')(G+i\lambda G')
   \over
   (F+i\lambda F')(G-i\lambda G')}.
}
\tag{L-106439.1}
\]

On the real axis `|U_(K,lambda)|=1`.  Direct multiplication gives

\[
\boxed{
N_K-D_K
 =2i\lambda
  \bigl(F F^{(K+1)}-F'F^{(K)}\bigr).
}
\tag{L-106439.2}
\]

Both the identity carrier `F F^(K)` and the quadratic companion term
`lambda^2 F'F^(K+1)` cancel exactly.

For a regular real polynomial, the companion half-plane count applied to the
first factor and the inverse `K`th factor gives

\[
\boxed{
\operatorname{wind}U_{K,\lambda}=R_0-R_K,
}
\tag{L-106439.3}
\]

where `R_j` is the number of real zeros of `F^(j)`, with the common endpoint
and degree convention used in `L-106400`.  The winding is independent of the
positive value of `lambda`.

Consequently

\[
\boxed{
R_0\ge R_K-\|H_{U_{K,\lambda}}\|_{\mathcal S_2}^2
}
\tag{L-106439.4}
\]

at finite rational scope, with the declared common-zero/confluent ledger.

## 2. Exterior-square Fourier identity

Assume

\[
F(t)=\int_{\mathbb R}\Phi(u)e^{itu}du,
\qquad
\Phi(u)=\Phi(-u)\ge0.
\]

Define

\[
\mathcal T_K[F]
 =F F^{(K+1)}-F'F^{(K)}.
\]

Writing `v=xi-u`, product convolution followed by symmetrization under
`u<->v` gives

\[
\boxed{
\widehat{\mathcal T_K[F]}(\xi)
 ={i^{K+1}\over2}
 \int_{\mathbb R}
 (v-u)(v^K-u^K)
 \Phi(u)\Phi(v)du.
}
\tag{L-106439.5}
\]

The integrand is an exterior-square frequency separation.  It has a fixed
sign structure for every parity.

### Odd endpoint order

If `K=2m+1`, the function `x->x^K` is increasing on the real line, so

\[
(v-u)(v^K-u^K)\ge0.
\]

Put

\[
\Lambda_K(\xi)
 ={1\over2}\int
 (v-u)(v^K-u^K)
 \Phi(u)\Phi(v)du\ge0.
\]

Then

\[
\boxed{
\widehat{\mathcal T_K[F]}(\xi)
 =(-1)^{m+1}\Lambda_K(\xi).
}
\tag{L-106439.6}
\]

Thus, up to a harmless global sign, the complete actual endpoint numerator
has a nonnegative Fourier density.

### Even endpoint order

If `K=2m`, factor

\[
(v-u)(v^{2m}-u^{2m})
 =(v-u)^2(v+u)
  \sum_{j=0}^{m-1}v^{2(m-1-j)}u^{2j}.
\]

Since `v+u=xi`, define

\[
\Lambda_K(\xi)
 ={1\over2}\int
 (v-u)^2
 \sum_{j=0}^{m-1}v^{2(m-1-j)}u^{2j}
 \Phi(u)\Phi(v)du\ge0.
\]

Then

\[
\boxed{
\widehat{\mathcal T_K[F]}(\xi)
 =i(-1)^m\xi\Lambda_K(\xi).
}
\tag{L-106439.7}
\]

`K=2` is exactly `L-106401`.

## 3. Hankel-source form

For odd `K`, the negative Hardy compression is, up to phase, the Hankel
operator with positive kernel

\[
\Lambda_K(x+s).
\]

For even `K`, it has positive kernel

\[
(x+s)\Lambda_K(x+s).
\]

In either parity, every finite source Gram of the actual endpoint numerator is
positive semidefinite.  No frozen Euler product, mollifier or RH hypothesis is
used.

## 4. Significance

The direct endpoint block avoids all intermediate derivative companions and
all cross-rung coherent assembly.  In particular `K=5` may consume the pinned
unconditional fifth-derivative real-zero input on this branch through one
all-pass quotient whose surviving actual-Xi numerator already has a
nonnegative Fourier density.

The theorem does not bound the all-pass quotient Hankel charge; the
outer-normalized/model-space and signed-tail interfaces of
`L-106432--L-106438` remain binding.
