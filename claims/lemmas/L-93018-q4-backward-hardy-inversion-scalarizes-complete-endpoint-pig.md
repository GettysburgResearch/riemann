# L-93018 - Backward Hardy inversion scalarizes the complete Q4 endpoint PIG

Claim ID: `L-93018`  
Status: **PROPOSED COMPLETE EXACT/ANALYTIC THEOREM - INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-15  
Depends on: `T-93010` for the compact-Q4 source and endpoint notation; the unconditional prime number theorem only for the final boundary limit  
Scope: a universal discrete transform identity, its growth transfer, and the complete actual Q4 endpoint row; no unconditional square-root bound for the Q4 mean and no RH conclusion by itself

## 1. Prefix and mean transforms

Let \(c(1),c(2),\ldots\) be any complex sequence and define

\[
C(N)=\sum_{m\le N}c(m),
\qquad
C(0)=0.
\tag{L-93018.1}
\]

For \(N\ge1\), define the endpoint mean transform

\[
M(N)
=
\sum_{m\le N}c(m)
\left(\frac{2m}{N}-1\right).
\tag{L-93018.2}
\]

Partial summation gives the exact Hardy form

\[
\boxed{
M(N)
=
C(N)-\frac2N\sum_{j=0}^{N-1}C(j).
}
\tag{L-93018.3}
\]

Indeed,

\[
\sum_{m\le N}m c(m)
=
NC(N)-\sum_{j=0}^{N-1}C(j).
\]

Thus the Q4 zero-safe mean is a triangular Hardy transform of the complete
compact prefix.

## 2. Exact finite backward inversion

Put

\[
S(N)=\sum_{j=0}^{N}C(j).
\tag{L-93018.4}
\]

Equation (L-93018.3) is equivalent to

\[
S(N)=\frac{N+2}{N}S(N-1)+M(N).
\tag{L-93018.5}
\]

After normalization,

\[
\boxed{
\frac{S(N)}{(N+1)(N+2)}
-
\frac{S(N-1)}{N(N+1)}
=
\frac{M(N)}{(N+1)(N+2)}.
}
\tag{L-93018.6}
\]

Summing from \(N\) to \(K\ge N\) gives the exact finite identity

\[
\boxed{
\begin{aligned}
C(N)
={}&
M(N)
-
2(N+1)
\sum_{k=N}^{K}
\frac{M(k)}{(k+1)(k+2)}\\
&+
2(N+1)
\frac{S(K)}{(K+1)(K+2)}.
\end{aligned}
}
\tag{L-93018.7}
\]

The last term is the complete boundary mode. It must not be silently dropped
at a finite truncation.

## 3. Boundary-free infinite inversion

Assume

\[
C(N)=o(N).
\tag{L-93018.8}
\]

Then \(S(N)=o(N^2)\), so the boundary term in (L-93018.7) tends to zero.
Consequently

\[
\boxed{
C(N)
=
M(N)
-
2(N+1)
\sum_{k=N}^{\infty}
\frac{M(k)}{(k+1)(k+2)}.
}
\tag{L-93018.9}
\]

The series converges whenever \(M(k)=O(k^\theta L(k))\) with
\(\theta<1\) and a polylogarithmic \(L\).

For the actual compact-Q4 source

\[
c_\circ(m)
=
\Lambda(m)
-
4\mathbf1_{4\mid m}\Lambda(m/4)
+
3(\log4)\sum_{r\ge1}\mathbf1_{m=4^r},
\tag{L-93018.10}
\]

one has

\[
C_\circ(N)
=
\psi(N)-4\psi(N/4)+O(\log N).
\tag{L-93018.11}
\]

The unconditional prime number theorem gives

\[
C_\circ(N)=o(N).
\tag{L-93018.12}
\]

Therefore (L-93018.9) applies unconditionally as an identity to the actual Q4
prefix. No RH estimate is used to remove the boundary mode.

## 4. Polynomial growth is preserved exactly

Suppose that for some \(0\le\theta<1\),

\[
|M(k)|\le B k^\theta
\qquad(k\ge1).
\tag{L-93018.13}
\]

Using

\[
\sum_{k=N}^{\infty}
\frac{k^\theta}{(k+1)(k+2)}
\le
N^{\theta-2}
+
\frac{N^{\theta-1}}{1-\theta},
\tag{L-93018.14}
\]

equation (L-93018.9) gives the explicit bound

\[
\boxed{
|C(N)|
\le
\left(5+\frac4{1-\theta}\right)
B N^\theta.
}
\tag{L-93018.15}
\]

Thus the backward Hardy inverse does not lose a power of \(N\).

## 5. Square-root polylogarithmic growth is preserved

Fix \(A\ge0\). Suppose

\[
|M(k)|
\le
B\sqrt{k}\,(\log(2k))^A
\qquad(k\ge1).
\tag{L-93018.16}
\]

Define the finite constant

\[
D_A
=
1+
4\sum_{\nu=0}^{\infty}
2^{-\nu/2}(\nu+2)^A.
\tag{L-93018.17}
\]

A dyadic decomposition of the tail in (L-93018.9) gives

\[
\boxed{
|C(N)|
\le
D_A B\sqrt N\,(\log(2N))^A.
}
\tag{L-93018.18}
\]

The constant depends only on \(A\), not on the sequence or the endpoint.

## 6. The complete endpoint row follows from the mean envelope

For the complete endpoint row

\[
R_N(j)
=
C(N)-C(j)-C(N-j-1),
\qquad 0\le j<N,
\tag{L-93018.19}
\]

equation (L-93018.18) gives

\[
|R_N(j)|
\le
3D_A B\sqrt N\,(\log(2N))^A.
\tag{L-93018.20}
\]

Hence its normalized PIG energy

\[
\mathscr P(N)
=
\frac1{N^2}
\sum_{j=0}^{N-1}|R_N(j)|^2
\tag{L-93018.21}
\]

satisfies

\[
\boxed{
\mathscr P(N)
\le
9D_A^2B^2(\log(2N))^{2A}.
}
\tag{L-93018.22}
\]

This is a deterministic implication from the global mean envelope to the full
row energy. No separate estimate for a Fourier mode, prime block, major arc,
minor arc, max kernel, or Goldbach term is required.

## 7. Converse coercivity

The exact variance identity of `T-93010` gives

\[
|M(N)|^2\le N\mathscr P(N).
\tag{L-93018.23}
\]

Therefore

\[
\boxed{
\mathscr P(N)\ll(\log N)^B
\quad\Longrightarrow\quad
M(N)\ll
\sqrt N\,(\log N)^{B/2}.
}
\tag{L-93018.24}
\]

Combining (L-93018.22) and (L-93018.24), for every sequence satisfying
\(C(N)=o(N)\),

\[
\boxed{
\begin{aligned}
&|M(N)|\ll\sqrt N\,(\log N)^A
\ \text{for some fixed }A\\
&\qquad\Longleftrightarrow\\
&\mathscr P(N)\ll(\log N)^B
\ \text{for some fixed }B.
\end{aligned}
}
\tag{L-93018.25}
\]

Thus the complete endpoint PIG and the one-dimensional endpoint mean have
exactly the same square-root/polylogarithmic content.

## 8. General exponent transfer

More generally, under \(C(N)=o(N)\),

\[
M(N)=O(N^\theta L(N)),
\qquad \theta<1,
\tag{L-93018.26}
\]

with a dyadically moderate envelope \(L\), implies

\[
\boxed{
\mathscr P(N)
=
O(N^{2\theta-1}L(N)^2).
}
\tag{L-93018.27}
\]

Conversely,

\[
\mathscr P(N)=O(N^\gamma L(N)^2)
\tag{L-93018.28}
\]

implies

\[
\boxed{
M(N)
=
O(N^{(\gamma+1)/2}L(N)).
}
\tag{L-93018.29}
\]

The exponent conversion is therefore

\[
\boxed{\gamma=2\theta-1.}
\tag{L-93018.30}
\]

This is the same exponent relation obtained from the pole-to-energy statement
in `T-93010`, now derived by an explicit finite transform.

## 9. Consequence for the PR #474 major-arc gate

`L-93015` proves unconditionally that the complete prime diagonal and every
mode outside a square-root major arc cost only \(O(\log N)\). The present
theorem shows that the remaining major-arc correlation is not an independent
global theorem:

\[
\boxed{
\text{a square-root/polylog bound for }M_\circ(N)
\text{ at all endpoints}
\Longrightarrow
\text{the full Q4 PIG bound}.
}
\tag{L-93018.31}
\]

The distinct-prime major-arc normal form remains useful for arithmetic attacks
and inverse theorems, but a complete closure may target the scalar
\(M_\circ(N)\) directly.

## 10. Proof boundary

Established exactly or unconditionally:

1. prefix-to-mean Hardy identity;
2. finite backward inversion with its boundary term;
3. boundary-free inversion under \(C(N)=o(N)\);
4. applicability to the compact-Q4 prefix by the PNT;
5. preservation of polynomial exponents;
6. preservation of square-root/polylogarithmic bounds;
7. deterministic mean-to-full-PIG implication;
8. complete mean/PIG equivalence at the RH scale.

Open:

1. an unconditional square-root/polylogarithmic bound for \(M_\circ(N)\);
2. the equivalent Q4 PIG bound;
3. RH.
