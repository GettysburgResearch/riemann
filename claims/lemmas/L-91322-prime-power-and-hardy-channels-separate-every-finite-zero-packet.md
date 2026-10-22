# L-91322 — Prime-power inputs and Hardy outputs separate every finite zero packet

Claim ID: `L-91322`  
Status: **EXACT FINITE-PACKET CONTROLLABILITY/OBSERVABILITY THEOREM; COMPLETED METRIC INTERTWINER OPEN**  
Created: 2026-08-12  
Depends on: elementary confluent Vandermonde algebra; the explicit zero-port vectors of PR #396  
RH status: **unproved**

## 1. Prime-power exponential source vectors

Let

\[
 Z=\{z_1,\ldots,z_r\}\subset\mathbb C
 \tag{L-91322.1}
\]

be distinct, and assign multiplicities `m_j>=1`. Put

\[
 M=\sum_{j=1}^r m_j.
 \tag{L-91322.2}
\]

For a prime `p` and integer `k>=1`, define the confluent exponential vector

\[
 \boxed{
 v_{p,k}
 =\left(k^\ell p^{-kz_j}ight)_{
          1\le j\le r,\ 0\le\ell<m_j}
 \in\mathbb C^M.
 }
 \tag{L-91322.3}
\]

These are the natural value/jet couplings of the prime-power source at the
spectral points `z_j`.

## 2. A prime avoiding every collision

For `i!=j`, a collision

\[
 p^{-z_i}=p^{-z_j}
 \tag{L-91322.4}
\]

requires

\[
 \Re(z_i-z_j)=0,
 \qquad
 (\Im z_i-\Im z_j)\log p\in2\pi\mathbb Z.
 \tag{L-91322.5}
\]

For a fixed pair, at most one prime can satisfy (L-91322.5). Indeed, if two
distinct primes `p,q` did, then `log p/log q` would be rational, so
`p^m=q^n` for some positive integers `m,n`, impossible for distinct primes.

There are finitely many pairs. Hence one may choose a prime `p` for which

\[
 \lambda_j:=p^{-z_j}
 \tag{L-91322.6}
\]

are pairwise distinct and nonzero.

## 3. Confluent Vandermonde controllability

For such a prime, the `M x M` matrix with rows `k=1,...,M` and columns
`(j,ell)`,

\[
 V_{k,(j,\ell)}=k^\ell\lambda_j^k,
 \tag{L-91322.7}
\]

is a confluent Vandermonde matrix. Its determinant is nonzero:

\[
 \det V
 =C(\lambda_1,\ldots,\lambda_r)
  \prod_{j=1}^r\lambda_j^{m_j}
  \prod_{i<j}(\lambda_j-\lambda_i)^{m_im_j},
 \tag{L-91322.8}
\]

where the first factor is a nonzero product of factorials and powers of the
`lambda_j` depending only on the multiplicities.

Consequently

\[
 \boxed{
 \operatorname{span}\{v_{p,k}:1\le k\le M\}
 =\mathbb C^M.
 }
 \tag{L-91322.9}
\]

Equivalently, if

\[
 \sum_{j=1}^r\sum_{\ell=0}^{m_j-1}
 c_{j,\ell} k^\ell p^{-kz_j}=0
 \qquad(k=1,2,\ldots),
 \tag{L-91322.10}
\]

then every coefficient vanishes.

Thus one suitably chosen prime, through finitely many of its powers, controls
every finite value/jet packet.

## 4. Source weights do not destroy spanning

The generalized-Jordan source multiplies the `p^k` channel by nonzero factors
of the form

\[
 \frac{1-p^{-2ak}}{k p^{k\sigma}}
 \quad\text{or their positive square roots}
 \tag{L-91322.11}
\]

for `a>0` and safe `sigma`. Multiplication of the rows of `V` by nonzero
scalars does not change rank. Hence the exact positive Jordan/Poisson weights
retain finite-packet controllability.

## 5. Hardy/Cauchy observability

Let `p_1,...,p_r` be distinct points in the right half-plane, again with
multiplicities `m_j`. The zero-port output functions are the Cauchy jets

\[
 \boxed{
 e_{j,\ell}(x)=\frac1{(x-p_j)^{\ell+1}}
 \qquad(0\le\ell<m_j).
 }
 \tag{L-91322.12}
\]

up to nonzero stable inner factors and normalizations.

If

\[
 \sum_{j,\ell}c_{j,\ell}e_{j,\ell}(x)=0
 \tag{L-91322.13}
\]

for every `x` in any real open interval avoiding the poles, the left side is a
rational function vanishing on a uniqueness set. It is identically zero, and
its principal parts at the distinct poles force every `c_(j,ell)=0`.

Therefore the causal/anti-causal carrier family, and a fortiori the complete
Takenaka--Malmquist output family, observes every finite zero packet.

## 6. Finite annular cascade minimality

Suppose the completed source-to-boundary realization has the natural couplings:

```text
prime-power input to a zero jet: k^ell p^(-k z_j);
zero jet to a Hardy carrier:     (x-p_j)^(-ell-1),
```

with the declared nonzero completed gamma/stable factors. Then every finite
annular zero packet is both controllable and observable. It cannot be a hidden
pole--zero cancellation state of a minimal cascade.

Combining with `L-91321`:

\[
 \boxed{
 \text{coarse-scale innerness}
 +\text{the natural completed finite-packet coupling}
 \Longrightarrow
 \text{no finite annular zero packet}.
 }
 \tag{L-91322.14}
\]

## 7. Exact remaining issues

This theorem closes the algebraic rank problem. It does not by itself construct
the completed positive-metric coupling. The remaining obligations are:

1. derive the value/jet source coupling from one common Guinand--Weil/Fock
   boundary map, rather than declare it;
2. prove the map is closable and positive-metric on the infinite source space;
3. control infinite-height tails so finite annular packets exhaust all hidden
   states;
4. preserve the gamma/pole, coupled Brownian/theta, stable, and bridge ports.

These are precisely the analytic-intertwiner obligations of `O-91302`; finite
controllability and observability are no longer open.
