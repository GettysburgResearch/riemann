# Exact coalesced leading coefficient at the fractional taper threshold

Author: equivalences. Date:2026-11-17. Status: ordinary-analysis derivation, sent for independent challenge. It strengthens the separately reconstructed order bounds in `fractional_scalar_threshold_round3.md`. No historical priority, novelty or RH claim.

Fix m≥1, let p=m−1/2, Q=(1−z)^m, b_n=binomial(n+m−1,m−1), and

\[
 A_{M,p}(z)=\sum_{n=0}^{M-1}b_n(1-n/M)^p z^n,\quad
 E_{M,p}=\|1-QA_{M,p}\|_{H^2}^2.
\]

Then, as M→∞ with m fixed,

\[
 \boxed{E_{M,m-1/2}=\kappa_m^2\frac{\log M}{M}+O_m(M^{-1}),
 \qquad \kappa_m=\frac{(m-1/2)_{\rm falling\ m}}{(m-1)!}
            =\frac{m\binom{2m}{m}}{4^m}.}
\]

The same holds at a common unit root q by coefficient rotation. At m1 the coefficient is1/4. Constants in the O term depend on fixed m; uniformity as m grows is not asserted.

## 1. Uniform derivative expansion in a boundary block

Write

\[
 P(u)=\frac{\prod_{l=1}^{m-1}(u+l)}{(m-1)!},\quad
 a_M(u)=M^{-p}P(u)(M-u)^p\quad(u<M).
\]

At integer0≤n<M this equals the approximant coefficient. Fix M≥4m and1≤j≤floor(M/2). The m-th finite-difference integral for a_M(M−j) evaluates u=M−t with t∈[j,j+m]⊂[1,3M/4]. All sampled u are positive; no negative-index extension or endpoint derivative is used.

For1≤t≤3M/4, the finite product gives

\[
 P(M-t)=\frac{M^{m-1}}{(m-1)!}
         \left[1+O_m\!\left(\frac{t+1}{M}\right)\right]. \tag{1}
\]

This estimate is uniform: expand the fixed-degree polynomial product∏(1+(l−t)/M); every nonconstant term is bounded by a constant depending on m times(t+1)/M on the compact range(t+1)/M≤1. The estimate need not have a small relative constant when t is a positive fraction of M; an O estimate suffices. Also, for0≤r≤m−1,

\[
 P^{(r)}(M-t)=O_m(M^{m-1-r}) \tag{2}
\]

uniformly on the same range.

In the Leibniz expansion of a_M^(m), the term differentiating(M−u)^p exactly m times is

\[
 (-1)^m M^{-p}P(M-t)(p)_{\rm falling\ m}t^{-1/2}.
\]

Using(1), its difference from(-1)^m \kappa_mM^(−1/2)t^(−1/2) is

\[
 O_m(M^{-3/2}t^{1/2}),
\]

since t≥1. A term with only k≤m−1 derivatives on the power is, by(2), bounded by

\[
 C_m M^{-p}M^{k-1}t^{p-k}
 =C_m M^{-3/2}t^{1/2}(t/M)^{m-k-1}
 \le C'_m M^{-3/2}t^{1/2}.
\]

The term k0 is actually zero because P has degree m−1. Summing the finitely many terms yields

\[
 a_M^{(m)}(M-t)
 =(-1)^m \kappa_mM^{-1/2}t^{-1/2}
   +O_m(M^{-3/2}t^{1/2}) \tag{3}
\]

uniformly for the entire boundary block. This expansion does not require a sign-dominance constant.

## 2. From derivatives to residual coefficients

For1≤j≤floor(M/2), n=M−j satisfies n−m≥0. Hence Q=(1−z)^m gives

\[
 r_{M-j}=-\Delta_{\rm backward}^m a_M(M-j)
       =-\int_{[0,1]^m}a_M^{(m)}(M-j-t_1-\cdots-t_m)dt.
\]

The integral of(j+t1+⋯+tm)^(−1/2) is j^(−1/2)+O_m(j^(−3/2)); this follows from the mean-value theorem on[j,j+m]. Likewise(j+m)^(1/2)=O_m(j^(1/2)) for j≥1. Equation(3) therefore gives

\[
 r_{M-j}=(-1)^{m+1}\kappa_mM^{-1/2}j^{-1/2}
 +O_m\!\left(M^{-1/2}j^{-3/2}+M^{-3/2}j^{1/2}\right). \tag{4}
\]

Squaring and summing is legitimate with an O_m(M−1) total error:

* main/error cross terms are bounded by constants times M−1Σj−2 and M−2Σ1;
* squared errors are bounded by M−1Σj−3, M−3Σj and M−2Σj−1.

For j≤M/2 every displayed sum is O_m(1/M), or smaller, after its prefactor. Thus

\[
 \sum_{j=1}^{\lfloor M/2\rfloor}|r_{M-j}|^2
 =\frac{\kappa_m^2}{M}\sum_{j=1}^{\lfloor M/2\rfloor}\frac1j+O_m(M^{-1})
 =\kappa_m^2\frac{\log M}{M}+O_m(M^{-1}). \tag{5}
\]

## 3. Every omitted coefficient contributes only O_m(1/M)

The collision-uniform critical upper proof in `fractional_scalar_threshold_round3.md` gives

\[
 |r_{M-j}|\le H_m M^{-1}\left((j+1)/M\right)^{-1/2}.
\]

For j>floor(M/2), the factor is bounded by√2, and there are at most M such terms, giving an O_m(1/M) sum of squares. At j0 the bound is H_m/√M, again an O_m(1/M) squared contribution. The m−1 terminal coefficients have squared sum O_m(1/M). The constant coefficient is exactly zero and all later coefficients vanish by degree.

Combining these bounds with(5) proves the displayed expansion. The binomial expression for \kappa_m follows directly from∏_(k0m−1)(m−1/2−k)=(2m)!/(4^m m!) and division by(m−1)!.

No computation is needed for the proof. Any future numerical profile is supplementary and must preserve the fixed-m limit and the distinction between the logarithmic coefficient and the O_m(1/M) remainder.
