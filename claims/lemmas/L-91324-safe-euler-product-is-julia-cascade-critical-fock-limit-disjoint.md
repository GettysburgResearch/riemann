# L-91324 — The safe Euler product is an explicit infinite Julia cascade, but the naive critical Fock limit is disjoint

Claim ID: `L-91324`  
Status: **EXACT SAFE CASCADE + CRITICAL REPRESENTATION FIREWALL**  
Created: 2026-08-12  
Depends on: `L-91323`; the prime number theorem for the divergence statement  
RH status: **unproved**

## 1. Finite prime cascade

Order a finite set of primes as \(p_1,\ldots,p_N\). Write

\[
m_j=m_{p_j,a,\sigma},
\qquad
d_j=d_{p_j,a,\sigma}.
\]

Define the scalar channel and emitted details by

\[
M_N=\prod_{j=1}^N m_j,
\tag{L-91324.1}
\]

\[
D_{j,N}
=
\left(\prod_{\ell<j}m_\ell\right)d_j.
\tag{L-91324.2}
\]

Repeated use of `L-91323` gives the exact pointwise optical identity

\[
\boxed{
|M_N(z)|^2
+
\sum_{j=1}^N|D_{j,N}(z)|^2
=1
\qquad(|z_{p_j}|=1).
}
\tag{L-91324.3}
\]

Equivalently, the column

\[
\mathcal J_{N,a,\sigma}
=
(M_N,D_{1,N},\ldots,D_{N,N})^{\mathsf T}
\tag{L-91324.4}
\]

is inner on the prime torus. Reordering the primes gives another lossless
detail basis, related pointwise on the boundary by a unitary coordinate change.

## 2. Infinite safe cascade

If \(\sigma>1\), then

\[
\sum_p(1-c_{p,a,\sigma})<\infty,
\qquad
\sum_p\delta_{p,a,\sigma}^2<\infty.
\tag{L-91324.5}
\]

Therefore the finite scalar products and detail columns converge on compact
subsets and in the natural Hardy/Fock norm. The scalar limit is

\[
\boxed{
M_{a,\sigma}(t)
=
\frac{Q_a(\sigma+it)}{Q_a(\sigma)}.
}
\tag{L-91324.6}
\]

There is an explicit isometric multiplier

\[
\boxed{
\mathcal J_{a,\sigma}:
H^2
\longrightarrow
H^2\oplus
\bigoplus_p H^2
}
\tag{L-91324.7}
\]

whose scalar output is (L-91324.6) and whose \(p\)-th output is the ordered
prime detail.

This is a transfer-level realization of the bosonic/compound-Poisson source
on the safe side.

## 3. Prime-by-prime dyadic rectangle

At every prime, (L-91323.13) factors the \(2a\) section into two \(a\)
sections. Applying this simultaneously over all primes produces an exact
rectangular lattice

```text
prime index        p
radial section     [a,2a] and [2a,4a]
scalar output      Q_(2a)
detail outputs     first-section and returned second-section innovations.
```

All finite rectangles are positive-metric and coefficient one. Associativity
is inherited from ordinary cascade associativity and from the divisor/Fock
pentagon law.

## 4. Exact critical threshold of the naive detail representation

At the moving critical boundary for the horizontal quotient,

\[
\sigma=\frac12-a,
\qquad 0<a<\frac12,
\tag{L-91324.8}
\]

one has

\[
\alpha_p=p^{-1/2-a},
\qquad
\beta_p=p^{-1/2+a},
\]

and

\[
\boxed{
\delta_p^2
=
\frac{
(p^{-1/2+a}-p^{-1/2-a})(1-p^{-1})
}{
(1-p^{-1/2-a})^2
}
\sim p^{-1/2+a}.
}
\tag{L-91324.9}
\]

Hence

\[
\boxed{
\sum_p\delta_p^2=\infty.
}
\tag{L-91324.10}
\]

More generally, for every fixed nonzero boundary frequency \(t\),

\[
\sum_p
\delta_p^2
\frac{|1-e^{-it\log p}|^2}
     {|1-p^{-1/2+a}e^{-it\log p}|^2}
=\infty.
\tag{L-91324.11}
\]

The latter follows from the prime number theorem by comparing with

\[
\int_2^X
\frac{x^{-1/2+a}(1-\cos(t\log x))}{\log x}\,dx,
\]

whose leading nonoscillatory coefficient strictly dominates the oscillatory
coefficient.

## 5. Representation firewall

The safe Euler–Julia cascades do not converge to a positive direct-sum detail
vector on the moving critical boundary. The obstruction is an infinite
particle/detail number, not a bad individual Euler factor.

Therefore a valid completion may not be:

```text
take the safe prime-by-prime Julia product;
let sigma decrease to 1/2-a in the same Fock representation;
append finitely many gamma/theta ports.
```

The critical representation is disjoint from the naive safe vacuum in this
sense. A successful construction must instead use one of:

1. a Green-filtered cyclic wave operator;
2. a source-ordered renormalized representation change;
3. a fixed-safe-scale screw/Hardy form core;
4. a canonical-system/DtN construction that performs the global
   renormalization before the Hilbert norm is taken.

This explains why the finite local positivity of every Euler factor does not
prove RH and why the all-prime analytic intertwiner remains load-bearing.
