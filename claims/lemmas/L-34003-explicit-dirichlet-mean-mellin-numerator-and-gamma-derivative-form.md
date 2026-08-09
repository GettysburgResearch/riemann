# L-34003 — Explicit Dirichlet-mean Mellin numerator and gamma-derivative form

Claim ID: `L-34003`

Status: **PROPOSED COMPLETE EXACT FINITE LEMMA — INDEPENDENT REVIEW REQUESTED**

Created: 2026-08-09

Dependencies: `L-34001-raw-brownian-factor-is-dirichlet-average-mellin-transform.md`; elementary confluent divided differences

Scope: exact finite formula for the zero-bearing Mellin factor; no all-`N` zero-free theorem and no RH claim

## 1. Dirichlet mean

Let

\[
Q_N=\sum_{i=1}^N a_iW_i,
\qquad a_i=i^{-2},
\qquad (W_1,\ldots,W_N)\sim \operatorname{Dirichlet}(2,\ldots,2).
\]

Put

\[
M_N(z)=\mathbb E[Q_N^z].
\]

The standard Dirichlet-average / Hermite--Genocchi identity gives

\[
\boxed{
M_N(z)
=\frac{\Gamma(2N)\Gamma(z+1)}{\Gamma(z+2N)}
[a_1,a_1,\ldots,a_N,a_N]\,x^{z+2N-1},
}
\tag{L-34003.1}
\]

initially for `Re z>-1` and thereafter by analytic continuation away from the elementary gamma poles.  At `z=0`, the divided difference of `x^(2N-1)` is one, so the normalization is exact.

## 2. Repeated-knot expansion

For distinct positive `a_i`, the confluent divided difference in (L-34003.1) is the sum of residues of

\[
\frac{x^{z+2N-1}}{\prod_{j=1}^N(x-a_j)^2}.
\]

At the double pole `a_i`, differentiating the regular factor gives

\[
\begin{aligned}
&[a_1,a_1,\ldots,a_N,a_N]x^{z+2N-1}\\
&=\sum_{i=1}^N
\frac{a_i^{z+2N-2}}
{\prod_{j\ne i}(a_i-a_j)^2}
\left[
 z+2N-1
 -2a_i\sum_{j\ne i}\frac1{a_i-a_j}
\right].
\end{aligned}
\tag{L-34003.2}
\]

No approximation enters this identity.

## 3. Specialize to `a_i=i^(-2)`

For `1<=i<=N`, define

\[
\boxed{
 C_{N,i}
 =4\frac{(N!)^4}{(N-i)!^2(N+i)!^2}>0,
}
\tag{L-34003.3}
\]

and

\[
\boxed{
 \alpha_{N,i}
 =i\bigl(H_{N+i}-H_{N-i}\bigr)-\frac12,
}
\tag{L-34003.4}
\]

where `H_0=0` and `H_m=sum_(k<=m)1/k`.

Elementary product simplification in (L-34003.2) yields a positive constant `K_N`, independent of `z`, such that

\[
\boxed{
[a_1,a_1,\ldots,a_N,a_N]x^{z+2N-1}
=K_N\sum_{i=1}^N
 C_{N,i}i^{-2z}(z+\alpha_{N,i}).
}
\tag{L-34003.5}
\]

Consequently the complete non-elementary zero set of `M_N` is the zero set of the explicit exponential polynomial

\[
\boxed{
 H_N(z)
 :=\sum_{i=1}^N C_{N,i}i^{-2z}(z+\alpha_{N,i}).
}
\tag{L-34003.6}
\]

The omitted prefactor is a product/quotient of gamma functions and a positive real constant, and therefore introduces no zeros.

For `N=2`, (L-34003.6), after multiplication by a positive constant, is exactly

\[
(48z+16)+(3z+11)4^{-z},
\]

recovering `L-34002`.

## 4. One gamma-interpolated weight

Define for real `0<x<N+1`

\[
\boxed{
 C_N(x)
 =4\frac{\Gamma(N+1)^4}
 {\Gamma(N-x+1)^2\Gamma(N+x+1)^2}.
}
\tag{L-34003.7}
\]

Then `C_N(i)=C_(N,i)`.  Differentiating its logarithm gives

\[
\frac{C_N'(x)}{C_N(x)}
=2\psi(N-x+1)-2\psi(N+x+1).
\tag{L-34003.8}
\]

At an integer `i`, the digamma identity `psi(m+1)=H_m-gamma` therefore gives

\[
\alpha_{N,i}
=-\frac12-rac{i}{2}\frac{C_N'(i)}{C_N(i)}.
\tag{L-34003.9}
\]

Substituting into one summand of (L-34003.6) yields the exact derivative form

\[
\boxed{
 C_{N,i}i^{-2z}(z+\alpha_{N,i})
 =-\frac12
 \frac{d}{dx}\left[C_N(x)x^{1-2z}\right]_{x=i}.
}
\tag{L-34003.10}
\]

Thus

\[
\boxed{
H_N(z)
=-\frac12\sum_{i=1}^N
 \left(C_N(x)x^{1-2z}\right)'_{x=i}.
}
\tag{L-34003.11}
\]

The all-`N` Brownian zero problem is therefore an exact sampled-derivative / quadrature problem for one explicit positive gamma weight.

## 5. Structural facts about the weight

The coefficient ratio is

\[
\boxed{
\frac{C_{N,i+1}}{C_{N,i}}
=\left(\frac{N-i}{N+i+1}\right)^2.
}
\tag{L-34003.12}
\]

Hence `C_(N,i)` is strictly decreasing in `i`.  The continuous log derivative in (L-34003.8) is also strictly negative for `x>0`, so `C_N(x)` is decreasing on `(0,N+1)`.

The first few `alpha_(N,i)` may be negative for large `N`, while later ones are positive.  Therefore a proof of half-plane stability cannot simply claim termwise positive real parts in (L-34003.6); the derivative representation (L-34003.11) is the preferred cancellation-preserving coordinate.

## 6. Exact new review target

PR #343 reduces RH to the cofinal theorem

\[
M_N(z)\ne0\qquad(\Re z>1/4).
\]

By this lemma, it is enough to prove

\[
\boxed{
H_N(z)\ne0\qquad(\Re z>1/4)
}
\tag{L-34003.13}
\]

cofinally in `N`, or even the numerically suggested stronger right-half-plane statement.

The derivative formula suggests three concrete mechanisms which are now sharply testable:

1. an Euler--Maclaurin sign/sector theorem for the sampled derivative sum;
2. a variation-diminishing theorem for the gamma weight `C_N`;
3. a direct Hermite--Biehler/canonical-system representation of (L-34003.11).

None of these mechanisms is asserted here.

## 7. Proof boundary

Closed exactly here:

1. the confluent divided-difference formula;
2. the repeated-knot residue expansion;
3. the explicit positive coefficients `C_(N,i)` and shifts `alpha_(N,i)`;
4. reduction of the Mellin zero set to `H_N`;
5. the gamma-interpolated derivative identity;
6. the elementary coefficient ratio/monotonicity.

Open:

1. the cofinal half-plane zero-free theorem for `H_N`;
2. raw Brownian stability;
3. RH.
