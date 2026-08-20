# L-100101 — Arbitrary-order finite Euler completion has an optimal arsinh-one corridor

Claim ID: `L-100101`  
Status: **PROVED UNCONDITIONAL ASYMPTOTIC THEOREM**  
Created: 2026-08-20  
Extends: PR #677 (`k=2`)  
RH status: **not assumed**

Let `(S_af)(X)=f(X/a)`.  For the compact SHARP kernel use zero extension
below one; for the cubic kernel use its actual positive continuation.  For an
integer `k>=2` and finite cutoff `Z`, define

\[
\boxed{
\mathscr A_{Z,k}
=
\left(\sum_{j=0}^{k-1}67^{-j/2}S_{67^j}\right)^2
\prod_{\substack{p\le Z\\p\ne67}}
\left(\sum_{j=0}^{k-1}p^{-j/2}S_{p^j}\right).
}
\tag{L-100101.1}

The square at `67` preserves the two labelled copies in the duplicate-67
source.  The local identity

\[
(1-p^{-z})\sum_{j=0}^{k-1}p^{-jz}=1-p^{-kz}
\tag{L-100101.2}

shows that completed primes have cost `p^k` and activity `p^{-k/2}`, while
primes above `Z` retain cost `p` and activity `p^{-1/2}`.

## 1. Level bound

Both the SHARP and cubic carrier satisfy

\[
q^{-1/2}K(y/q)\le q^{-1}K(y)
\tag{L-100101.3}

for every label cost `q>=2`.  If `M_r(X)` is the unsigned Euler mass at level
`r`, removal double counting gives

\[
M_r(X)\le\frac{\Sigma_{k,Z}(X)^r}{r!}K(X),
\tag{L-100101.4}

where

\[
\Sigma_{k,Z}(X)
\le
\sum_{p\le Z}p^{-k}+67^{-k}
+\sum_{Z<p\le X}p^{-1}
+R_K(X,Z).
\tag{L-100101.5}

For compact SHARP, `R_K=0`.  For the noncompact cubic carrier, primes
`p>max(X,Z)` contribute an absolutely convergent inactive tail, and
`L-100100` gives

\[
0\le R_K(X,Z)
\ll\max(1,\sqrt X)
\sum_{p>\max(X,Z)}p^{-3/2}
\ll\frac1{\log(2\max(X,Z))}.
\tag{L-100101.6}

Pairing levels yields

\[
\boxed{
(\mathscr A_{Z,k}H)(X)
\ge K(X)[1-\sinh\Sigma_{k,Z}(X)].
}
\tag{L-100101.7}

## 2. Optimal fixed-order exponent

Let

\[
P(k)=\sum_{p\ {m prime}}p^{-k}.
\]

Mertens' theorem gives, uniformly for fixed `A>1` and `X<=Z^A`,

\[
\Sigma_{k,Z}(X)
\le P(k)+67^{-k}+\log A+o_{Z\to\infty}(1).
\tag{L-100101.8}

Define

\[
\boxed{
A_k^*=
\exp\!\left(\operatorname{arsinh}1-P(k)-67^{-k}\right).
}
\tag{L-100101.9}

Then, for every `A<A_k^*`,

\[
\boxed{
(\mathscr A_{Z,k}H)(X)>0
\qquad(1\le X\le Z^A)
}
\tag{L-100101.10}

for all sufficiently large `Z`.  The `k=2` case sharpens PR #677's
conservative `10/9` corridor.  Moreover

\[
\boxed{
A_k^*\longrightarrow
\exp(\operatorname{arsinh}1)=1+\sqrt2.
}
\tag{L-100101.11}

## 3. Finite pole preservation

The Mellin multiplier is

\[
\boxed{
\mathcal A_{Z,k}(z)
=
\left(\frac{1-67^{-kz}}{1-67^{-z}}\right)^2
\prod_{\substack{p\le Z\\p\ne67}}
\frac{1-p^{-kz}}{1-p^{-z}}.
}
\tag{L-100101.12}

Every geometric factor is zero-free in `Re z>0`, so every finite completion
retains every hypothetical open-strip reciprocal-zeta pole.

The limiting exponent `1+sqrt(2)` is the sharp ceiling of this
**level-pairing argument**: after completed-prime mass tends to zero, the
unsquared prime interval still contributes `log A`, while positivity requires
`log A<asinh(1)`.  No global sign beyond that ceiling is claimed.
