# L-23803 — Exact Möbius adjoint decoder for carry elimination

Claim ID: `L-23803`  
Title: Möbius inversion converts every carry column into one affine kernel and identifies the reciprocal-zeta channel inside the exact carry inverse  
Status: **PROPOSED EXACT LEMMA PENDING INDEPENDENT REVIEW**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-07  
Issue: #238  
Dependencies: `L-23801`  
Scope: exact finite algebra and proof firewall; no sign theorem

## 1. Möbius transform of one carry row

For integers

\[
2\le m\le n,
\]

define

\[
\Gamma_{n,m}
=\sum_{k\le n/m}\mu(k)\beta_{n,mk}.
\tag{L-23803.1}
\]

Then

\[
\boxed{
\Gamma_{n,m}
=\frac{2m-n-1}{n+1}.}
\tag{L-23803.2}
\]

### Proof

Use the floor-sum representation from `L-23801`:

\[
\beta_{n,q}
=\left\lfloor\frac nq\right\rfloor
 -\frac2{n+1}\sum_{j=0}^{n}
  \left\lfloor\frac jq\right\rfloor.
\]

For the first term, the elementary Möbius identity gives

\[
\sum_{k\le n/m}\mu(k)
 \left\lfloor\frac{n/m}{k}\right\rfloor=1.
\]

For the second term, interchange the finite sums. For each `j>=m`,

\[
\sum_{k\le j/m}\mu(k)
 \left\lfloor\frac{j/m}{k}\right\rfloor=1,
\]

while it is zero for `j<m`. There are `n-m+1` contributing integers. Thus

\[
\Gamma_{n,m}
=1-\frac{2(n-m+1)}{n+1}
=\frac{2m-n-1}{n+1}.
\]

No asymptotic estimate enters.

## 2. Möbius coordinates of the target

For a finite target vector `w(q)`, define

\[
\boxed{u_m
=\sum_{k\le X/m}\mu(k)w(mk).}
\tag{L-23803.3}
\]

Möbius inversion over multiples gives

\[
w(q)=\sum_{k\le X/q}u_{qk}.
\tag{L-23803.4}
\]

If `c` is the exact triangular inverse

\[
w(q)=\sum_{n=q}^{X}c_n\beta_{nq},
\]

then (L-23803.2) gives

\[
\boxed{u_m
=\sum_{n=m}^{X}
 c_n\frac{2m-n-1}{n+1}.}
\tag{L-23803.5}
\]

The carry inverse is therefore a finite second-order adjoint of one Möbius
transform, not a coefficientwise positive kernel.

## 3. Explicit inverse coefficient

Solving (L-23803.5) for `c_j` gives

\[
\boxed{
 c_j
 ={(j+1)[j u_j-(j-2)u_{j+1}]
   +2\sum_{m=j+2}^{X}u_m
  \over j(j-1)}.}
\tag{L-23803.6}
\]

For the carry target

\[
w_X(q)=q^{-1/2}\log(X/q),
\]

one has

\[
\boxed{
 u_m
 =m^{-1/2}
  \sum_{k\le X/m}
  {\mu(k)\over\sqrt k}
  \log\frac{X/m}{k}.}
\tag{L-23803.7}
\]

Thus the apparent finite floor inequality contains a smoothed Möbius Riesz
mean explicitly.

## 4. Mellin firewall

The continuum inverse profile associated with (L-23803.6) has Mellin multiplier
of the form

\[
\boxed{
\Phi(z)
=\frac{(z+\tfrac12)(z+\tfrac32)}
 {z^2(z-\tfrac12)\zeta(z+\tfrac12)},}
\tag{L-23803.8}
\]

up to the declared normalization convention. The reciprocal-zeta factor is not
an artifact of one proof technique: it is the analytic image of the exact
finite Möbius transform (L-23803.3).

Consequently:

- pointwise Carry Saturation is a deep arithmetic statement;
- a proof may not replace the complete quotient layer by total variation;
- the packing/covering theorem of `L-23802` is genuinely weaker because it may
  tolerate a sparse negative part or use different nonnegative certificates.

## 5. Quotient-layer review target

On a quotient layer

\[
\frac{X}{r+1}<m\le\frac Xr,
\]

only the finite prefix

\[
\mu(1),\ldots,\mu(r)
\]

appears in (L-23803.7). This yields a finite exact symbolic problem at every
fixed layer.

The existing outer-layer argument closes the first four nontrivial quotient
layers. The proposed continuation must group complete quotient layers before
absolute values and prove either:

1. the residual-ratio invariant forcing diagonal saturation; or
2. the weaker weighted negative-mass / packing-covering estimate.

The identity (L-23803.2) is the exact algebraic adapter for either attack.

## 6. Proof boundary

Closed exactly:

- the affine Möbius transform of the carry matrix;
- the inverse coefficient formula;
- the explicit smoothed Möbius source;
- the quotient-layer finite-prefix reduction.

Open:

- positivity or small negative mass of the inverse;
- the carry sandwich theorem;
- RH.