# L-34007 — The Brownian gamma weight is the squared tail of Euler's sine product

Claim ID: `L-34007`

Status: **PROPOSED COMPLETE EXACT CANONICAL-PRODUCT LEMMA — INDEPENDENT REVIEW REQUESTED**

Created: 2026-08-09

Dependencies: `L-34003`

Scope: exact canonical-product form of the all-`N` Brownian numerator; no half-plane zero-free theorem and no RH claim

## 1. Recall the gamma-interpolated weight

`L-34003` defines

\[
C_N(x)
=4\frac{\Gamma(N+1)^4}
 {\Gamma(N-x+1)^2\Gamma(N+x+1)^2},
\qquad 0<x<N+1,
\tag{L-34007.1}
\]

and proves

\[
H_N(z)
=-\frac12\sum_{i=1}^N
\left(C_N(x)x^{1-2z}\right)'_{x=i}.
\tag{L-34007.2}
\]

We identify `C_N` with one exact tail of Euler's sine product.

## 2. Finite gamma product

For arbitrary complex `x` away from the displayed poles,

\[
\frac{\Gamma(N+1-x)\Gamma(N+1+x)}
 {\Gamma(1-x)\Gamma(1+x)}
=\prod_{k=1}^N(k-x)(k+x)
=(N!)^2\prod_{k=1}^N\left(1-\frac{x^2}{k^2}\right).
\tag{L-34007.3}
\]

Euler's reflection identity in the form

\[
\Gamma(1-x)\Gamma(1+x)
=\frac{\pi x}{\sin\pi x}
\tag{L-34007.4}
\]

therefore gives

\[
\frac{\Gamma(N+1)^2}
 {\Gamma(N+1-x)\Gamma(N+1+x)}
=
\frac{\sin\pi x}
 {\pi x\prod_{k=1}^N(1-x^2/k^2)}.
\tag{L-34007.5}
\]

Squaring and multiplying by four yields

\[
\boxed{
C_N(x)
=4\left[
\frac{\sin\pi x}
 {\pi x\prod_{k=1}^N(1-x^2/k^2)}
\right]^2.
}
\tag{L-34007.6}

All apparent singularities at the integers `1,...,N` are removable.

## 3. Infinite-product tail

Euler's product

\[
\frac{\sin\pi x}{\pi x}
=\prod_{k=1}^{\infty}
\left(1-\frac{x^2}{k^2}\right)
\tag{L-34007.7}
\]

converges locally uniformly. Cancelling its first `N` factors in (L-34007.6) gives the exact canonical-product identity

\[
\boxed{
C_N(x)
=4\prod_{k=N+1}^{\infty}
\left(1-\frac{x^2}{k^2}\right)^2.
}
\tag{L-34007.8}

Thus the Brownian weight is literally the square of the tail remaining after deleting the first `N` zero pairs from the sine product.

At an integer `1<=i<=N`, (L-34007.8) gives

\[
\boxed{
C_{N,i}
=4\left[
\frac{\binom{2N}{N-i}}
 {\binom{2N}{N}}
\right]^2
=4\frac{(N!)^4}{(N-i)!^2(N+i)!^2},
}
\tag{L-34007.9}
\]

recovering `L-34003`.

## 4. Tail Stieltjes logarithmic derivative

On every compact subset avoiding the tail zeros `N+1,N+2,...`, logarithmic differentiation of (L-34007.8) is legitimate and gives

\[
\boxed{
\frac{C_N'(x)}{C_N(x)}
=-4x\sum_{k=N+1}^{\infty}
\frac1{k^2-x^2}.
}
\tag{L-34007.10}

Hence the shift in `L-34003`, at every `1<=i<=N`, may be written as

\[
\boxed{
\alpha_{N,i}
=-\frac12
+2i^2\sum_{k=N+1}^{\infty}
\frac1{k^2-i^2}.
}
\tag{L-34007.11}
\]

This is exactly equivalent to

\[
\alpha_{N,i}=i(H_{N+i}-H_{N-i})-\frac12,
\]

because partial fractions of the tail sum telescope to the harmonic-number difference.

## 5. Critical-quarter shift

Put

\[
z=\frac14+w.
\]

Equation (L-34003.11) becomes

\[
\boxed{
H_N\left(\frac14+w\right)
=-\frac12\sum_{i=1}^N
\left(C_N(x)x^{1/2-2w}\right)'_{x=i}.
}
\tag{L-34007.12}

The exact RH-facing Brownian problem is therefore a minimum-phase statement for a sampled derivative of a positive squared sine-tail canonical product.

Equivalently, the individual scores are

\[
\boxed{
C_{N,i}i^{-1/2-2w}
\left[
 w-\frac14
 +2i^2\sum_{k>N}\frac1{k^2-i^2}
\right].
}
\tag{L-34007.13}

This coordinate isolates the quarter-line `Re z=1/4` intrinsically: the `-1/4` term is the derivative of the critical square-root weight `x^(1/2)`, while the remaining positive term is the Stieltjes logarithmic derivative of the deleted sine-product tail.

## 6. Structural consequence

The finite Brownian problem is not an arbitrary exponential polynomial.  It is built from one sine-type canonical product with its first `N` zero pairs deleted, sampled exactly at those deleted zeros.

This suggests proof mechanisms unavailable in the generic Dirichlet-average representation:

1. a discrete Herglotz/de Branges form based on the positive tail sum in (L-34007.10);
2. an Euler--Maclaurin or Abel--Plana formula for the sampled derivative in (L-34007.12);
3. a discrete Sturm/canonical-system realization whose Weyl function is the tail Stieltjes sum.

None of these closing mechanisms is asserted here.

## 7. Proof boundary

Closed exactly:

1. the finite gamma-product identity;
2. the sine-product quotient;
3. the squared tail-product representation of `C_N`;
4. the binomial-ratio specialization at the sampled integers;
5. the positive tail-Stieltjes logarithmic derivative;
6. the exact quarter-shifted sampled-derivative formula.

Open:

1. a Herglotz/canonical-system realization of the full sampled sum;
2. cofinal zero-freeness for `Re w>0`;
3. RH.
