# T-93011 - The complete Q4 endpoint route is exactly one zero-safe mean scalar

Claim ID: `T-93011`  
Status: **PROPOSED COMPLETE RH-EQUIVALENT SCALAR CRITERION - INDEPENDENT REVIEW REQUIRED; RH UNPROVED**  
Created: 2026-08-15  
Depends on: `T-93010`, `L-93018`, `R-93020`  
Scope: the complete actual compact-Q4 source; no unconditional square-root/polylogarithmic mean estimate

## 1. The scalar

Retain the complete compact-Q4 coefficients

\[
c_\circ(m)
=
\Lambda(m)
-
4\mathbf1_{4\mid m}\Lambda(m/4)
+
3(\log4)\sum_{r\ge1}\mathbf1_{m=4^r}
\tag{T-93011.1}
\]

and define

\[
\boxed{
M_\circ(N)
=
\sum_{m\le N}c_\circ(m)
\left(\frac{2m}{N}-1\right).
}
\tag{T-93011.2}
\]

This is the mean of the complete endpoint carry field in `T-93010`.

## 2. Scalar mean implies the complete positive energy

Assume that for some fixed \(A\),

\[
\boxed{
|M_\circ(N)|
\ll
\sqrt N\,(\log(2N))^A
\qquad(N\ge2).
}
\tag{T-93011.3}
\]

The PNT gives \(C_\circ(N)=o(N)\), so the exact backward Hardy inversion of
`L-93018` applies. It yields

\[
C_\circ(N)
\ll
\sqrt N\,(\log(2N))^A.
\tag{T-93011.4}
\]

Therefore every complete endpoint-row coordinate satisfies

\[
R_N(j)
=
C_\circ(N)-C_\circ(j)-C_\circ(N-j-1)
\ll
\sqrt N\,(\log(2N))^A.
\tag{T-93011.5}
\]

Consequently

\[
\boxed{
\mathscr P_\circ(N)
=
\frac1{N^2}\sum_{j=0}^{N-1}|R_N(j)|^2
\ll
(\log(2N))^{2A}.
}
\tag{T-93011.6}
\]

No separate distinct-prime major-arc theorem is needed for this implication.

## 3. Complete positive energy implies the scalar mean

The exact variance identity of `T-93010` gives

\[
|M_\circ(N)|^2
\le
N\mathscr P_\circ(N).
\tag{T-93011.7}
\]

Hence a polylogarithmic complete PIG bound implies a square-root/polylogarithmic
bound for \(M_\circ\).

Combining Sections 2 and 3,

\[
\boxed{
\begin{aligned}
&|M_\circ(N)|
\ll
\sqrt N\,(\log N)^A
\quad\text{for some fixed }A\\
&\qquad\Longleftrightarrow\\
&\mathscr P_\circ(N)
\ll
(\log N)^B
\quad\text{for some fixed }B.
\end{aligned}
}
\tag{T-93011.8}
\]

## 4. Mellin zero safety

`T-93010` proves, for \(\Re z>1\),

\[
\begin{aligned}
\int_1^\infty M_\circ(X)X^{-z-1}\,dX
={}&
\frac{z-1}{z(z+1)}
\Bigg[
(1-4^{1-z})
\left(-\frac{\zeta'}{\zeta}(z)\right)\\
&\qquad+
3(\log4)\frac{4^{-z}}{1-4^{-z}}
\Bigg].
\end{aligned}
\tag{T-93011.9}
\]

Every nontrivial zeta zero survives as a nonremovable pole. If
(T-93011.3) holds, integer-to-real interpolation makes the Mellin integral
holomorphic in \(\Re z>1/2\), so no zero can lie there. Functional-equation
symmetry then gives RH.

Conversely, RH gives

\[
C_\circ(N)\ll\sqrt N\log^2(2N)
\]

and hence (T-93011.3).

Therefore

\[
\boxed{
\mathrm{RH}
\Longleftrightarrow
|M_\circ(N)|
\ll
\sqrt N\,(\log N)^A
\text{ for some fixed }A
\Longleftrightarrow
\mathscr P_\circ(N)
\ll
(\log N)^B
\text{ for some fixed }B.
}
\tag{T-93011.10}
\]

## 5. Quantitative depth transfer

If a hypothetical zero has real part \(\beta>1/2\), then for every
\(0<\varepsilon<\beta-1/2\),

\[
M_\circ(N)\ne O(N^{\beta-\varepsilon}).
\tag{T-93011.11}
\]

By `L-93018`, the corresponding complete endpoint energy cannot satisfy

\[
\mathscr P_\circ(N)
=
O(N^{2\beta-1-2\varepsilon}).
\tag{T-93011.12}
\]

Thus the scalar and energy criteria retain exactly the same off-line-zero
growth exponent.

## 6. Revised Q4 frontier

The distinct-prime Gram, improved prime diagonal, and square-root major-arc
normal forms in `L-93242/L-93015` remain useful for arithmetic estimates and
inverse theorems. They are no longer a logically independent completion gate.

A full Q4 closure may target only

\[
\boxed{
M_\circ(N)
=
O\left(\sqrt N\,\log^A N\right).
}
\tag{T-93011.13}
\]

The backward Hardy inverse then reconstructs every prefix and the complete
positive endpoint energy.

This scalar estimate is still RH-bearing and is not proved here.

## 7. Proof boundary

Established, subject to independent review:

1. scalar mean bound implies complete PIG;
2. complete PIG implies scalar mean bound;
3. both are equivalent to RH through the zero-safe Mellin transform;
4. both carry the same polynomial obstruction exponent.

Open:

1. the unconditional bound (T-93011.13);
2. RH.
