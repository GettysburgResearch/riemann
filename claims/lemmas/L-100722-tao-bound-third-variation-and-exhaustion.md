# L-100722 — Uniform rough-prefix control, third variation, and finite-cutoff exhaustion

Claim ID: `L-100722`  
Status: **PROVED USING TAO'S ELEMENTARY SEMIGROUP BOUND**  
Created: 2026-08-21  
Depends on: `L-100720--L-100721`  
RH status: **not assumed**

For an arbitrary set of primes `P`, Tao's elementary semigroup theorem gives

\[
\boxed{
\left|
 \sum_{\substack{d\le x\\p\mid d\Rightarrow p\in\mathcal P}}
 {\mu(d)\over d}
\right|\le1.
}
\tag{L-100722.1}
\]

Reference: T. Tao, *A remark on partial sums involving the Möbius function*,
Bull. Aust. Math. Soc. **81** (2010), 343--349, Theorem 1.1; arXiv:0908.4323.
The finite-divisor form used here is one of the equivalent formulations stated
in that theorem.

## 1. Uniform derivative bound

Apply (L-100722.1) to every term of the compensated prefix in `L-100721`:

\[
\boxed{
|\mathcal B_{p,q;\mathcal P}(x)|
\le(1+p^{-1/2})(1+q^{-1/2}).
}
\tag{L-100722.2}
\]

Consequently the positive coarea kernel has total mass `1/2`, and

\[
\boxed{
|H'_{p,q;\mathcal P}(t)|
\le192(1+p^{-1/2})(1+q^{-1/2}).
}
\tag{L-100722.3}
\]

This estimate is uniform in:

```text
number of interior primes;
length of the endpoint interval;
activation pattern;
physical scale t.
```

It is the first coefficient-exact bound on the complete long-interval cubic
derivative which does not pay the number of interior Euler histories.

## 2. Exact third derivative

Let `c(t)=(1-t)_+^3`. Since

\[
c'''(t)=-6\mathbf1_{0<t<1}
\]

with no delta mass at `t=1`, expansion of `L-100720.5` gives

\[
\boxed{
\begin{aligned}
\widetilde H'''_{p,q;\mathcal P}(t)
=-384\sum_{d\mid D_{\mathcal P}}{\mu(d)\over d^2}
\Big[&\mathbf1_{t<\sqrt d}
-p^{-3/2}\mathbf1_{t<\sqrt{pd}}\\
&-q^{-3/2}\mathbf1_{t<\sqrt{qd}}
+(pq)^{-3/2}\mathbf1_{t<\sqrt{pqd}}
\Big].
\end{aligned}}
\tag{L-100722.4}
\]

Taking total variation yields the factorized bound

\[
\boxed{
\|\widetilde H'''_{p,q;\mathcal P}\|_{L^1(dt)}
\le384(1+p^{-1})(1+q^{-1})
 \prod_{\ell\in\mathcal P}(1+\ell^{-3/2}).
}
\tag{L-100722.5}
\]

Since the prime `3/2` sum converges, the right side is bounded by one absolute
constant for all rough intervals `p,q>=67`.

The first absolute moment is

\[
\boxed{
\int_0^\infty t|\widetilde H'''_{p,q;\mathcal P}(t)|dt
\le192(1+p^{-1/2})(1+q^{-1/2})
 \prod_{\ell\in\mathcal P}(1+\ell^{-1}).
}
\tag{L-100722.6}
\]

For a prime interval `(p,q)`, Mertens' theorem gives the transparent cost

\[
\prod_{p<\ell<q}(1+\ell^{-1})\ll {\log q\over\log p}.
\tag{L-100722.7}
\]

Thus the only growing absolute moment is logarithmic in the endpoint interval;
the unweighted history count has disappeared.

## 3. Joint min--max averaging

Let

\[
\pi_{ij}=r_ir_jL_iR_j
\]

be the exact joint min--max coefficients of `L-100616`.  Since

\[
\sum_{i<j}\pi_{ij}\le1,
\]

(L-100722.5) immediately gives

\[
\boxed{
\sum_{i<j}\pi_{ij}
 \|\widetilde H'''_{ij}\|_{L^1(dt)}
\le C_{\rm cub}
}
\tag{L-100722.8}
\]

for one absolute constant `C_cub`, uniformly in the finite prime cutoff.

## 4. Cutoff exhaustion

If the interior prime set increases, the difference of the third-derivative
measures is bounded by the tail of

\[
\prod_{\ell}(1+\ell^{-3/2}).
\]

Hence the third derivatives converge in total variation.  Equations
`L-100720.6--7` fix the integration constants, so the exact cubic packets and
their first two derivatives converge locally uniformly.

Therefore the finite-cutoff limit preserves:

```text
the literal heat/cubic packet;
the endpoint owners;
the exact compensated-prefix derivative;
the joint min--max source coefficients.
```

No weakly chosen cross-state Gram or post-hoc contraction is used.
