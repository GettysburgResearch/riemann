# A fixed scalar Riesz window for reciprocal polynomials with unit-circle roots

Date:2026-11-17. Independent derivation by equivalences after root's proposed two-root quadratic bound; the general twisted-difference argument below was derived before reading root's separate Euler-operator construction. This is an elementary finite-polynomial result, not an arithmetic zeta estimate. **No novelty or publication-priority claim.** The primary approximation background is Burnol's polynomial theorem (PAPER-E002, Theorem1.4: every root on the unit circle), BCF's simple-root linear window (PAPER-E003, Theorem2), and the observatory's independently checked exact coalesced optimum. Prior Riesz/Cesàro summability literature must be checked before attributing originality.

## Statement, including every endpoint

Fix an integer m≥1. Let

\[
 Q(z)=\prod_{j=1}^m(1-q_jz),\qquad |q_j|=1,
 \quad Q(z)^{-1}=\sum_{n\ge0}b_nz^n.
\]

The q's are a multiset: exact coincidences and arbitrarily close roots are allowed. Normalize Q(0)=1 as above; a nonzero scalar multiple is absorbed by its reciprocal coefficients. For every integer M≥1 (equivalently N=M−1≥0), put

\[
 A_M(z)=\sum_{n=0}^{M-1}b_n(1-n/M)^m z^n,\qquad
 E_M=\|1-QA_M\|_{H^2(\mathbb D)}^2.
\]

For a polynomial \(\sum c_nz^n\), the norm squared here is \(\sum|c_n|^2\), with normalized circle measure dθ/(2π). Define

\[
 C_m=\sum_{k=1}^m k\binom mk^2
     =m\binom{2m-1}{m-1},
\]
\[
 T_{m,r}=\sum_{j=r+1}^m\binom mj(j-r)^m\quad(1\le r\le m-1),
 \qquad K_m=C_m^2+\sum_{r=1}^{m-1}T_{m,r}^2.
\]

Then

\[
 \boxed{E_M\le\frac{K_m}{M}\quad\text{for all }M\ge1\text{ and all unit }q_1,\ldots,q_m.}
\]

The coefficient bounds proved below actually give the slightly stronger

\[
 E_M\le C_m^2/M+\left(\sum_{r=1}^{m-1}T_{m,r}^2\right)/M^2.
\]

No root separation appears. Constants depend on fixed m and grow rapidly; no conclusion for growing m is asserted. The first constants are K1=1 and K2=37. For m=2 this proves root's proposed bound for Q=(1−z)(1−qz), uniformly including q=1. For m=1 the construction has exactly E_M=1/M, for every unit q.

If all roots coincide, \(Q=(1-qz)^m\), then for fixed m

\[
 \boxed{E_M=m^2/M+O_m(M^{-2}).}
\]

This matches the leading term of the exact optimum for degree≤M−1 approximation. It does not assert finite-M optimality of this scalar window.

## 1. Exact discrete product rule

Extend every reciprocal coefficient sequence by0 to negative indices. For a subset S of {1,…,m}, define

\[
 b_n^S=[z^n]\prod_{j\in S}(1-q_jz)^{-1}.
\]

For S empty this is the Kronecker delta sequence; for nonempty S it is the complete homogeneous polynomial \(h_n(q_j:j\in S)\), with \(h_n=0\) for n<0. Let

\[
 (D_qc)_n=c_n-qc_{n-1},\qquad
 (\Delta w)_n=w_n-w_{n-1},\qquad q_S=\prod_{j\in S}q_j.
\]

Take any scalar sequence w indexed by integers. The exact product identity is

\[
 \left(\prod_{j=1}^mD_{q_j}\right)(bw)_n
 =\sum_{S\subset\{1,\ldots,m\}}
 q_S\left(\prod_{j\notin S}D_{q_j}b\right)_{n-|S|}
       \Delta^{|S|}w_n. \tag{1}
\]

Proof: for any c,w,

\[
 D_q(cw)_n=w_n(D_qc)_n+q c_{n-1}\Delta w_n.
\]

Induct over the factors. The first term keeps the new index outside S; the second adds it to S, shifts c by1 and raises the scalar difference order by1. D operators commute with one another and with integer shifts, so the induction is exact and requires no distinctness of the q's.

Formal power-series cancellation gives

\[
 \prod_{j\notin S}D_{q_j}b=b^S.
\]

Thus, if A has coefficients bw,

\[
 (QA)_n=w_n\delta_{n0}
 +\sum_{\varnothing\ne S\subset\{1,\ldots,m\}}
       q_S h_{n-|S|}(q_j:j\in S)\Delta^{|S|}w_n. \tag{2}
\]

This formula explains why bounding only the full b_n is wasteful: a k-fold difference of the window is paired with a reciprocal polynomial of degree k, not degree m.

Use now w_n=(1−n/M)^m for n≤M, and w_n=0 for n>M. Its values at negative indices are harmless because b_n=0 there. Since w_M=0, this is exactly the coefficient sequence of the stated degree≤M−1 polynomial.

## 2. Bulk coefficients, 1≤n≤M

For a subset S of size k, the term in (2) vanishes if n<k. If n≥k,

\[
 |h_{n-k}(q_j:j\in S)|\le\binom{n-1}{k-1}
 \le\frac{M^{k-1}}{(k-1)!}.
\]

This is the number of weak compositions of n−k into k nonnegative parts. The scalar m-th-power taper is a polynomial throughout the interval n−k,…,n⊂[0,M], so the repeated integral representation of finite differences gives

\[
 |\Delta^kw_n|
 \le\frac{m(m-1)\cdots(m-k+1)}{M^k}.
\]

For clarity, with \(p(x)=(1-x/M)^m\),

\[
 \Delta^kp(n)=\int_{[0,1]^k}p^{(k)}(n-t_1-\cdots-t_k)\,dt_1\cdots dt_k,
\]

and the derivative bound is taken only on[0,M]. Summing (2) over the \(\binom mk\) subsets yields

\[
 |(QA_M)_n|\le\frac1M\sum_{k=1}^m
 \binom mk\frac{m!}{(m-k)!(k-1)!}
 =\frac1M\sum_{k=1}^m k\binom mk^2=\frac{C_m}{M}. \tag{3}
\]

The identity \(\sum k\binom mk^2=m\binom{2m-1}{m-1}\) follows from \(k\binom mk=m\binom{m-1}{k-1}\) and Vandermonde's identity.

The residual coefficient is \(r_n=-(QA_M)_n\) for n≥1. Equation(2) is a formula for QA, not for its negative; signs do not affect(3). At n=0, b0=w0=1, hence r0=0.

## 3. The finite terminal block, M+1≤n≤M+m−1

Write n=M+r,1≤r≤m−1. If \(Q(z)=\sum_{j=0}^m c_jz^j\), then \(|c_j|\le\binom mj\). The only nonzero A indices in the convolution have j≥r+1 and0≤M+r−j≤M−1. Therefore

\[
 |(QA_M)_{M+r}|
 \le\sum_{j=r+1}^m\binom mj
 |b_{M+r-j}|\left(\frac{j-r}{M}\right)^m,
\]

where terms with M+r−j<0 may be omitted. For0≤l≤M−1,

\[
 |b_l|\le\binom{l+m-1}{m-1}
 \le\binom{M+m-2}{m-1}\le M^{m-1}. \tag{4}
\]

For m=1 the last inequality reads1≤1. For m≥2 it follows by bounding each factor \(M+j\le(j+1)M\),0≤j≤m−2, in the product for the binomial coefficient. Equivalently, weakly increasing(m−1)-tuples selected from M values are no more numerous than all ordered tuples.

Consequently

\[
 |(QA_M)_{M+r}|\le T_{m,r}/M. \tag{5}
\]

The polynomial QA has degree at mostM+m−1, so there is no remaining tail. Squaring(3), summing M bulk coefficients, and adding the m−1 bounds(5), proves the theorem. All estimates include M=1; they do not use an asymptotic root-spacing regime.

For m=2, S={1},{2},{1,2}, q1=1,q2=q gives

\[
 (QA_M)_n=(1+q^n)\Delta w_n+q b_{n-2}\Delta^2w_n,
 \quad1\le n\le M,
\]

with b−1=0. The terminal QA coefficient is \(q b_{M-1}/M^2\); the corresponding residual coefficient is its negative. Thus C2=6,T2,1=1 gives exactly37/M. At M=1, A=1 and actual squared error is|1+q|²+1≤5, well within the bound37.

## 4. Complete coalescence: exact leading constant by integration by parts

A common rotation q multiplies every nth coefficient by q^n and does not change the H² norm. It suffices to take q=1. Then

\[
 b_n=\binom{n+m-1}{m-1}.
\]

Let

\[
 f_M(x)=\frac{\prod_{j=1}^{m-1}(x+j/M)}{(m-1)!}(1-x)^m,
 \qquad
 f(x)=\frac{x^{m-1}(1-x)^m}{(m-1)!}.
\]

Empty products are1. On the polynomial extension of the coefficient formula,

\[
 a_n=M^{m-1}f_M(n/M).
\]

For fixed m, every coefficient of f_M−f is O_m(1/M), so all derivatives through degree2m−1 converge at that rate uniformly on any fixed bounded interval. For1≤n≤M, the backward m-th difference never samples a negative integer below1−m. At integers−1,…,−(m−1), the binomial polynomial vanishes, so its polynomial extension agrees with the zero extension of the actual a sequence wherever the difference samples it. Thus

\[
 r_n=-\Delta^ma_n
     =-\frac1M f^{(m)}(n/M)+O_m(M^{-2}),
 \qquad1\le n\le M, \tag{6}
\]

uniformly in n. For example this follows by the finite-difference integral formula over a cube of side1/M, using the convergence of f_M derivatives and the bounded next derivative of f on[−m,1]. The finitely many tail coefficients are O_m(1/M) by(5). Their squared contribution is O_m(M−2).

A Riemann sum and(6) therefore give

\[
 E_M=\frac1M\int_0^1|f^{(m)}(x)|^2dx+O_m(M^{-2}). \tag{7}
\]

Here f has a zero of orderm−1 at0, a zero of orderm at1, and \(f^{(m-1)}(0)=1\). For every polynomial p of degree≤m−1, integration by parts m times yields

\[
 \int_0^1f^{(m)}(x)p(x)dx=-p(0). \tag{8}
\]

Only the first boundary term at0 survives; every subsequent boundary term vanishes, and p^(m)=0. Since f^(m) itself has degree m−1, take p=f^(m). The coefficient of x^m in f is \(-m/(m-1)!\), so

\[
 f^{(m)}(0)=-m^2,\qquad
 \int_0^1|f^{(m)}(x)|^2dx=-f^{(m)}(0)=m^2.
\]

This proves(7) with leading constantm². Equation(8) also identifies−f^(m) as the endpoint evaluation kernel on degree≤m−1 polynomials; no conjectural spectral interpretation is involved.

For comparison, the separately proved exact degree≤N optimum, with L=N+m=M+m−1, is

\[
 E_{\rm opt}=1-\frac{(L)_{\rm falling\ m}}{(L+1)_{\rm rising\ m}}
            =m^2/M+O_m(M^{-2}).
\]

The scalar window therefore matches its leading constant at complete coalescence. It need not match the optimum for distinct fixed roots: already for m=2 and fixed q≠1 the quadratic taper has a different leading constant from the root-adapted optimum. The uniform theorem above deliberately claims only K_m/M in general.

## 5. An exact negative result: lower integer taper powers fail uniformly

For repeated roots Q=(1−z)^m, replace the power m by a fixed nonnegative integer p<m. The last residual coefficient, at degreeM+m−1, has modulus

\[
 |r_{M+m-1}|=\binom{M+m-2}{m-1}/M^p
 \sim\frac{M^{m-1-p}}{(m-1)!}.
\]

If p=m−1 the squared error is bounded below by a positive constant; if p<m−1 it diverges along M→∞. Thus no lower nonnegative **integer** power p<m supplies a collision-uniform O_m(1/M) squared error. This precisely generalizes the already documented failure of the BCF simple-root linear taper at a double root. It does not claim that the source theorem omitted its simple-root assumption, or that all non-integer powers below m fail by this terminal argument. The borderline fractional power m−1/2 requires a different argument and is not settled here.

## Reproduction, independent review and limitations

`experiments/code/unit_circle_scalar_window_round3.py` checks the exact subset identity and norm bound with rational complex unit roots, including repeats and M=1; results are exact fractions, not plots. The analytic proof above establishes all parameters; finitely many computations are supplemental. Parent's Euler-operator argument is independent and has looser constants; a third reviewer is reconstructing this finite-difference version and coalescence calculation.

Potential reuse: a fixed degree-m taper gives robust reciprocal-polynomial approximation without detecting internal root spacings. What is **not** supplied is a zeta/Dirichlet-polynomial analogue: infinitely many zeros, coefficient arithmetic, norm weights and growing multiplicity all require additional uniform estimates. A summation-method analogy alone does not transfer this finite theorem to RH.

## 6. Exact two-root maximum: the optimal uniform constant for this window is5

The general estimate gives K2=37, but its two-root value can be sharpened exactly. A common root rotation preserves coefficient norms, so take Q=(1−z)(1−qz), |q|=1. Let a_n=2M+1−2n for1≤n≤M. The exact residual coefficients are

\[
 M^2r_n=a_n(1+q^n)-2\sum_{j=1}^{n-1}q^j\quad(1\le n\le M),
 \qquad
 M^2r_{M+1}=-\sum_{j=1}^{M}q^j.
\]

These follow directly from(2), \(\Delta w_n=(2n-2M-1)/M^2\), and \(\Delta^2w_n=2/M^2\). There is no division by1−q, so q=1 is included.

Expand the squared norm as a Laurent polynomial in q. For lag1≤k≤M, its autocorrelation coefficient (before division by M⁴) is

\[
 R_k=a_k^2+\sum_{n=k+1}^M\{-4a_n+4(n-k-1)\}+(M-k).
\]

Explanation: the n=k term is the product of its two endpoint coefficients; for n>k there are two endpoint/interior products totaling−4a_n, and n−k−1 interior/interior products of value4. The last residual contributes M−k pairs at lag k. Writing d=M−k gives

\[
 R_k=(2d+1)^2-2d(d+1)+d=(d+1)(2d+1)>0. \tag{9}
\]

Thus, with E_M(q) denoting this squared error,

\[
 E_M(1)-E_M(q)=\frac2{M^4}\sum_{k=1}^M
  (M-k+1)(2(M-k)+1)\{1-\Re(q^k)\}\ge0. \tag{10}
\]

Equality requires Re(q)=1 because the k=1 coefficient is positive; hence q=1 is the unique relative-root maximizer. At q=1,

\[
 r_n=(4M+4-6n)/M^2\quad(1\le n\le M),\qquad r_{M+1}=-1/M,
\]

so elementary sums of n and n² give

\[
 \boxed{E_M(q)\le E_M(1)=4/M+3/M^2-2/M^3\le5/M.} \tag{11}
\]

For integer M≥1, the final inequality is equivalent to(M−1)(M−2)≥0. Equality in the constant5 bound occurs at M=1 or2 and q=1, so **5 is the smallest all-M constant for this particular quadratic window**. This is not the smallest approximation error over all degree≤M−1 polynomials.

The exact Laurent identity(10) is checked with rational complex unit q in the reproduction script; its proof is analytic and includes M=1 and2. This section does not assert that a corresponding coalescence maximum holds for m≥3; that is a separate conjecture requiring proof or a counterexample.
