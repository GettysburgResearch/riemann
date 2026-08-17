# L-96600 — The unique 5:3 scalar has an exact four-scale Möbius prefix state

Claim ID: `L-96600`  
Status: **PROVED EXACT FINITE ALGEBRA**  
Created: 2026-08-17  
Frozen parent: PR #551 at `c8702aef34a25c614f91dea1ecc6e787478e8170`  
RH status: **not assumed**

## 1. Unique scalar

Retain the conclusion-producing scalar from PR #551,

\[
\mathcal R_X=5c_X(2)+3c_X(3).
\]

Its positive unsieved dictionary is

\[
q_*(1)=0,\quad q_*(2)=15,\quad q_*(3)=6,\quad q_*(4)=3,
\quad q_*(m)=6\ (m\ge5).
\]

Writing

\[
\mathcal R_X=\sum_{n\le X}{a_*(n)\over\sqrt n}\log{X\over n},
\]

finite Dirichlet convolution gives

\[
\boxed{
 a_*(n)=6\mathbf1_{n=1}-6\mu(n)
 +9\mathbf1_{2\mid n}\mu(n/2)
 -3\mathbf1_{4\mid n}\mu(n/4).
}
\tag{L-96600.1}
\]

No prime-sieved transport is used.

## 2. Odd-core packet

If `d` is odd and squarefree, then the contribution of its complete two-adic orbit is

\[
\boxed{
(a_*(d),a_*(2d),a_*(4d),a_*(8d))
=\mu(d)(-6,15,-12,3).
}
\tag{L-96600.2}
\]

All higher two-adic multiples vanish. This is the complete signed arithmetic packet behind the single scalar; the three-prime mode has disappeared exactly.

## 3. Prefix shadow

Put

\[
B(x)=\sum_{n\le x}{\mu(n)\over\sqrt n},
\qquad
M_*(N)=\sum_{n\le N}{a_*(n)\over\sqrt n}.
\]

Then

\[
\boxed{
M_*(N)=6-6B(N)+{9\over\sqrt2}B(N/2)-{3\over2}B(N/4).
}
\tag{L-96600.3}
\]

For \(N\le X<N+1\), define \(L_*(N)=\sum_{n\le N}a_*(n)\log n/\sqrt n\). Exactly,

\[
\boxed{\mathcal R_X=M_*(N)\log X-L_*(N).}
\tag{L-96600.4}
\]

The entering term at an integer has zero logarithmic ramp, so the scalar is continuous and

\[
\boxed{
\mathcal R_{N+1}-\mathcal R_N
=M_*(N)\log\left(1+{1\over N}\right).
}
\tag{L-96600.5}
\]

Consequently eventual nonnegativity of the one prefix state `M_*`, together with one nonnegative starting value, proves `SPRP` and hence RH through the frozen PR #551 consumer.

## 4. Exact boundary

The lemma does not prove the sign of `M_*`. It replaces a global cross-knot transport by one explicit four-scale weighted-Mertens state and one exact update law.
