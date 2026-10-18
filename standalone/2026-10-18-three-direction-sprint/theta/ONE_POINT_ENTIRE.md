# One exponential moment outside the zero band controls the whole plane

**Status: PROPOSED complete analytic lemma, not an RH proof.** This sharpens
the sufficient threshold `R>sqrt(2)b` in PROOF.md to **every `R>b`** for
symmetric bounded-support laws. It also distinguishes the result from the
one-budget strip transfer in repository PR #1002: that transfer permits
arbitrary entire characteristic functions and assumes `R>1/2` in the
actual Xi variable; the bounded-support/zero-band structure here gives
whole-plane normality from a budget at any point strictly above the
desired band. Finite Ising observables satisfy the bounded-support premise.

No cofinal theta construction is supplied by this lemma. It reduces one
explicit requirement on such a construction.

## 1. The theorem

Let `X` be a symmetric real random variable of bounded support, with
`f(z)=E exp(izX)`. Suppose all its zeros obey `|Im lambda|<=b`, and

\[
 0\le b<R,\qquad f(iR)\le M<\infty.
 \tag{1}
\]

There is an explicit finite constant `C(b,R,M)`, independent of the
support size or any finite-model complexity, such that

\[
 \boxed{|f(z)|\le e^{C(b,R,M)|z|^2}\quad(z\in\mathbb C).} \tag{2}
\]

Thus any family with the same`b,R,M` is normal on the entire plane.
One necessarily has`M>=1`; if`M=1`, the law is the point mass at0 and
`f=1`. For`b=0`, one may take `C=(M^2-1)/(2R^2)`.

For`b>0,M>1`, put

\[
 k=\frac\pi{4R},\qquad
 r_*^2=\frac{\cosh(4kb)-\cos(2kb)}
               {\cosh(4kb)+\cos(2kb)}<1,
 \qquad N_* =\frac{\log M}{-\log r_*},
\]

\[
 m_* =\min\left(1,\frac{(R-b)^4}{16b^4}\right),\quad
 P_*=M^2m_*^{-N_*},\quad
 C=\frac{N_*M^2+P_*-1}{R^2}. \tag{3}
\]

These constants are deliberately conservative. Their finiteness, rather
than numerical optimality, is the point.

## 2. Uniformly few zeros can produce negative factors

Symmetry and the exponential-moment budget imply

\[
 |f(x+iu)|\le E e^{-uX}=f(iu)\le f(iR)\le M
 \quad(|u|\le R). \tag{4}
\]

The conformal map `w=tanh(kz)` sends the horizontal strip`|Im z|<R`
onto the unit disk and sends0 to0. Apply Jensen's formula to the bounded
analytic function `f(arctanh(w)/k)`, whose value at0 is1. Counting all
zeros in the strip with multiplicity gives

\[
 \sum_{\lambda}\log\frac1{|\tanh(k\lambda)|}\le\log M. \tag{5}
\]

For a zero with `|lambda|<=2b`, use `|Re lambda|<=2b` and
`|Im lambda|<=b`. The elementary identity

\[
 |\tanh(k(x+iu))|^2
  =\frac{\cosh(2kx)-\cos(2ku)}
         {\cosh(2kx)+\cos(2ku)}
\]

shows that its image has modulus at most`r_*<1`: the denominator is
positive because `2kb<pi/2`. Hence the number of such zeros, with
multiplicity, is at most`N_*`.

There is also a uniform zero gap. Bound (4) holds on the disk`|z|<=R`.
Jensen's formula on that disk, using just one zero, gives

\[
 |\lambda|\ge R/M. \tag{6}
\]

For zeros outside the disk this is automatic. For those inside, it is
the inequality`log(R/|lambda|)<=log M`.

## 3. Control of the complete paired product

Bounded support makes`f` entire of exponential type. There are no purely
imaginary zeros, because `f(iy)=E cosh(yX)>0`. Pair opposite zeros, taking
one representative from each pair, including multiplicity. Hadamard
factorization and evenness give

\[
 f(z)=\prod_\lambda(1-z^2/\lambda^2),
 \qquad\sum_\lambda|\lambda|^{-2}<\infty. \tag{7}
\]

The genus-one linear exponentials cancel within opposite pairs; evenness
removes a remaining linear exponential; exponential type excludes a
quadratic exponential. The constant is fixed by`f(0)=1`.

For each selected representative let

\[
 q_\lambda=|1+R^2/\lambda^2|^2
 =1+\frac{R^2(2|\lambda|^2+R^2-4(\Im\lambda)^2)}{|\lambda|^4}.
\]

For `|lambda|>2b`,

\[
 q_\lambda-1\ge R^2/|\lambda|^2\ge0. \tag{8}
\]

For `|lambda|<=2b`, the distances to`+-iR` are at least`R-b`, so

\[
 q_\lambda
 =\frac{|\lambda-iR|^2|\lambda+iR|^2}{|\lambda|^4}
 \ge m_*>0. \tag{9}
\]

There are at most`N_*` selected inner representatives; counting both
members in (5) only makes that bound more conservative. Equation (7)
and (1) give `product q_lambda=f(iR)^2<=M^2`. Therefore the product of
the outer factors is at most`P_*`. As all outer factors are at least1,

\[
 \sum_{|\lambda|>2b}(q_\lambda-1)
 \le\prod_{|\lambda|>2b}q_\lambda-1\le P_*-1.
\]

Combining this with (6)--(8) proves

\[
 \sum_\lambda|\lambda|^{-2}
 \le \frac{N_*M^2+P_*-1}{R^2}=C.
\]

Finally `|1-z^2/lambda^2|<=exp(|z|^2/|lambda|^2)` in (7) proves (2).
For`b=0`, every factor instead satisfies
`q_lambda-1>=2R^2/|lambda|^2`, giving the stated simpler constant.

## 4. Sharp threshold and cofinal consumer

The strict condition`R>b` cannot be dropped. For`b>0`, the three-point
factor with `a_w=cosh(bw)` has all zeros on`Im z=+-b`, while

\[
 f_w(ib)=\frac{2\cosh(bw)}{1+\cosh(bw)}<2.
\]

For every`S>b`, `f_w(iS)` tends to infinity as`w` tends to infinity.
All fixed positive moments tend to0. PR #1002 gives the stronger
variance-exactly-one version by multiplying this factor by
`cos(sqrt(1-v_w)z)`, where `v_w=w^2/(1+cosh(bw))`; its budget at`ib`
remains at most`2cosh(b)`. Thus even a fixed variance does not repair the
boundary case.

Consequently, symmetric finite Ising observables with a common zero
band`b` and one common actual-law budget`E exp(RX)<=M` for **any `R>b`**
have automatic entire compactness. If their moments converge cofinally
to the actual theta moments, the identity theorem identifies the entire
limit with`Xi/Xi(0)`, and Hurwitz transfers the zero band. For example,
at actual Xi band`b=1/3`, a budget at any fixed`R>1/3` would suffice.
This does not establish the required models or their budget.

The new field-based class in PR #1001 has the required finite zero band
when`|h_i|<=b w_i`. Its zero-field-reference variance bound is one
sufficient way to obtain this actual-law budget, but the theorem above
does not assume that reference variance remains bounded.

## 5. Overlap and credit

PR #1001 at`f6beb3774ae7ff5eca4cb046786eae10e4f88abc`,
`standalone/2026-10-18-zeta-specific-family-and-strip/strip/PROOF.md`, proves
the correlated real-field band, its zero-field-variance growth consumer,
and the stronger cofinal obstruction to independent elementary cosine
products for every`a>=0`. Its rare-jump counterexample overlaps the one
used here. PR #1002 at`1319373815ee408146705b25a426fba6b22ed755`,
`standalone/2026-10-18-five-route-zero-preserving-attack/STRIP_COMPACTNESS.md`,
proves the one-budget transfer on a finite horizontal strip, the exact
variance counterexample, and the bounded-component variance estimate.
The addition here is the paired-product/Jensen upgrade to whole-plane
normality at the sharp strict threshold`R>b` for bounded-support laws.
