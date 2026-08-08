# L-32405 — Critical Haar filter hierarchy

Claim ID: `L-32405`  
Title: Odd critical dyadic Haar powers retain every off-line zeta pole while giving constant positive carry charge on every sufficiently large balanced split  
Status: **PROPOSED COMPLETE EXACT FINITE/ANALYTIC LEMMA PENDING INDEPENDENT REVIEW**  
Authoring agent: `gpt56-pro-09-s`  
Created: 2026-08-08  
Dependencies: `L-32403`; elementary Dirichlet convolution and binomial algebra  
Scope: a fixed-source hierarchy and exact carry geometry; no cofinal sign/energy theorem and no RH claim

## 1. Higher critical Haar sources

Let

\[
D=\varepsilon-\sqrt2\,\delta_2.
\]

For every integer `k>=1`, define

\[
\boxed{\nu_{2,k}=D^{*k}*\mu.}
\tag{L-32405.1}

Its Dirichlet series is

\[
\boxed{
\sum_{n\ge1}{\nu_{2,k}(n)\over n^s}
={\left(1-2^{1/2-s}\right)^k\over\zeta(s)}.
}
\tag{L-32405.2}

Every zero `rho` of zeta with `Re rho>1/2` remains an uncancelled pole because

\[
|2^{1/2-\rho}|<1.
\]

## 2. Exact kth dyadic Riesz difference

Retain

\[
\mathcal R_\mu(X)
=\sum_{n\le X}{\mu(n)\over\sqrt n}\log{X\over n}.
\]

Expanding `D^{*k}` and using the critical normalization

\[
{(\sqrt2)^r\over\sqrt{2^r}}=1
\]

gives

\[
\boxed{
\mathcal H_{2,k}(X)
:=\sum_{n\le X}{\nu_{2,k}(n)\over\sqrt n}\log{X\over n}
=\sum_{r=0}^{k}(-1)^r\binom kr\,
 \mathcal R_\mu(X/2^r).
}
\tag{L-32405.3}

Thus `nu_(2,k)` is the exact kth dyadic Haar difference of the critical Möbius Riesz mean.

Its Mellin transform is

\[
\boxed{
\int_1^\infty \mathcal H_{2,k}(X)X^{-z-1}\,dX
={\left(1-2^{-z}\right)^k\over z^2\zeta(z+1/2)}
}
\tag{L-32405.4}

initially in the absolute-convergence half-plane.

For `k>=3`, the numerator removes the entire zero-frequency `z^-2` drift with at least one zero left over at `z=0`. Off-line poles remain untouched.

## 3. Complete divisor prefix

Since `1*mu=epsilon`,

\[
\boxed{
\mathbf1*\nu_{2,k}=D^{*k}
=\sum_{r=0}^{k}\binom kr(-\sqrt2)^r\delta_{2^r}.
}
\tag{L-32405.5}

Hence the divisor prefix is the finite step function

\[
\boxed{
P_k(x)=
\sum_{\substack{0\le r\le k\\2^r\le x}}
\binom kr(-\sqrt2)^r.
}
\tag{L-32405.6}

For every `x>=2^k`,

\[
\boxed{P_k(x)=(1-\sqrt2)^k.}
\tag{L-32405.7}

## 4. Constant interior carry charge

For an integer split `n=j+(n-j)`, define

\[
Y_k(n,j)=P_k(n)-P_k(j)-P_k(n-j).
\tag{L-32405.8}

If

\[
n,j,n-j\ge2^k,
\]

then all three prefixes have reached the stable value, and therefore

\[
\boxed{
Y_k(n,j)=-(1-\sqrt2)^k.
}
\tag{L-32405.9}

For odd `k`, this is the strictly positive constant

\[
\boxed{
Y_k(n,j)=(\sqrt2-1)^k>0.
}
\tag{L-32405.10}

In particular, on the `1/4`-balanced cone, every parent

\[
\boxed{n\ge2^{k+2}}
\tag{L-32405.11}

has every allowed child at least `2^k`, so every balanced split has the same positive source charge `(sqrt(2)-1)^k` for odd `k`.

Thus the first critical Haar source `k=1` is the first member of a hierarchy whose odd levels make the complete sufficiently-large balanced interior uniformly positive.

## 5. Positive inverse and generalized-prime data

The reciprocal source has Dirichlet series

\[
A_k(s)
={\zeta(s)\over(1-\sqrt2\,2^{-s})^k}.
\tag{L-32405.12}

The geometric-binomial expansion

\[
(1-u)^{-k}=\sum_{r\ge0}\binom{k+r-1}{r}u^r
\]

shows that every Dirichlet coefficient of `A_k` is positive. More explicitly, if

\[
n=2^v m,\qquad m\text{ odd},
\]

then

\[
\boxed{
a_k(n)=\sum_{r=0}^{v}
 \binom{k+r-1}{r}(\sqrt2)^r>0.}
\tag{L-32405.13}

The generalized von Mangoldt sequence is obtained from

\[
-\frac{A_k'}{A_k}(s)
=-\frac{\zeta'}\zeta(s)
+k\log2\,
 {\sqrt2\,2^{-s}\over1-\sqrt2\,2^{-s}}.
\]

Therefore

\[
\boxed{
\Lambda_k(n)
=\Lambda(n)
+k\log2\sum_{r\ge1}(\sqrt2)^r\mathbf1_{n=2^r}
\ge0.}
\tag{L-32405.14}

So every member of the hierarchy retains the same useful positive-inverse and nonnegative-generalized-prime structure seen in the earlier opposite-parity programmes.

## 6. Strategic use of the cubic source

The first odd source beyond `k=1` is `k=3`.

It simultaneously has:

```text
no zero-frequency Mellin pole;
every off-line zeta pole retained;
positive Dirichlet inverse;
nonnegative generalized-prime coefficients;
constant positive carry charge on every 1/4-balanced parent n>=32.
```

This creates an alternative full-problem interface: instead of controlling the complete critical boundary state, one may try to construct a source-complete reflected/carry theorem for the fixed cubic source and treat the finitely many parents below `32` exactly.

No such physical source theorem is asserted here. `R-29002` remains a mandatory firewall: positive generalized-prime coefficients do not by themselves imply a pointwise generalized Kummer square.

## 7. Proof boundary

Established exactly, subject to review:

1. the full critical Haar source hierarchy;
2. exact kth dyadic Riesz differences;
3. the Mellin transform and off-line-pole retention;
4. the finite divisor prefix;
5. constant positive balanced-interior charge for odd `k`;
6. positive inverse coefficients;
7. nonnegative generalized-prime coefficients.

Not established:

1. a source-complete Hermitian/carry coercivity theorem for any `k>=3`;
2. a sign or subpower estimate for `H_(2,k)`;
3. RH.
