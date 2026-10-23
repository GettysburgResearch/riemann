# Retaining the two-length saving in the weighted full Kubota mean

22 October 2026. Status: proposed source-dependent deduction, with a
complete proof below; independent review pending. Scope: a continued
full sextic Gauss-series mean. This does not bound a primitive signed
remainder or the complete inverse moment, and proves no smaller
zero-free boundary.

## 1. Source and normalization

The input is *Primitive sextic Kubota means and a sharp sixth-power-free
large sieve*, rStation paper 10, version 2, Sections 2, 4 and 5:

<https://rstation.ai/api/v1/papers/riemann_hypothesis_10/versions/2/download>.

The source snapshot has SHA256
`525c899dd4dd5cb0ed15db43f63fb6e25cc140f98358e9d41ddfe897f5a23a7a`.
Its full finite-vector functional equation, fixed bad-prime sections,
sextic and quadratic large sieves, and vertical growth are retained as
imports. The refinement is to keep the two-length bound in its equation
(4.8) through the absorption proof, rather than replace that bound by
the larger quantity used in its Proposition 3.

Work over the Eisenstein integers, with good primary representatives
outside the primes above 6, the source's self-dual additive character,
and literal zero extension. Put

\[
 D_\nu(r,u)=\sum_c\nu(c)g_6(r,c)(Nc)^{-u},\qquad
 Z_\nu(r,u)=\zeta_S(6u-5)D_\nu(r,u).
\]

The first series is initially defined for \(\Re u>3/2\) and is then
continued by the imported finite-vector theory. The fixed ray section
\(\nu\) belongs to the source's finite family. There is no uniformity
claim for a growing bad-prime level or infinity type.

## 2. The refined statement

Let \(A,B\ge1\), \(M=AB\), \(L_0=\sqrt{AB^3}=\sqrt M B\), and set

\[
 \begin{split}
 \mathcal F(A,B)=\min\big\{&M/B+M^{1/2}B
                         +MB^{-1/2}+M^{3/4}B^{1/2},\\
                         &M/B+M^{3/2}/B\big\}.
 \end{split}                                                   \tag{1}
\]

For every fixed \(0<\eta<1/12\) and \(\epsilon>0\), uniformly for
good \(h\), \(t\in\mathbb R\), and the indicated lengths,

\[
 \boxed{
 \frac1B\sum_{\substack{a\asymp A,\ b\asymp B\\
                         ab\ {m squarefree},\ (ab,h)=1}}
 |D_\nu(hab^3,1+\eta+it)|^2
 \ll_{\eta,\epsilon}
 (Nh\,M)^\epsilon (Nh)^{1/2}(1+|t|)^6\mathcal F(A,B).}
                                                               \tag{2}
\]

The same assertion holds for a fixed finite collection of source
components, with the equivalent vector norm. All constants may depend
on the fixed local data.

Two convenient, weaker forms of (1) are

\[
 \mathcal F(A,B)\ll
 \begin{cases}
 MB^{-1/2}+M^{3/4}B^{1/2},&1\le B\le\sqrt M,\\
 M^{3/2}/B,&\sqrt M\le B\le M.
 \end{cases}                                                   \tag{3}
\]

Thus (2) has a fixed power saving over the source's volume bound when
\(B=M^b\) lies in any closed subinterval of \((0,1/2)\) or
\((1/2,1]\). It has no such saving at \(B=1\) or
\(B\asymp\sqrt M\).

## 3. Keeping the finite-series estimate

Use the source notation

\[
 \Psi_6(A,L)=A+L+A^{5/6}L^{1/3}+A^{1/3}L^{5/6},
 \qquad
 \mathcal B_{A,B}(L)=
       \min\{\Psi_6(A,L),(A/B)(B+L)\}.
                                                               \tag{4}
\]

The proof of its Lemma 2, through equation (4.8), gives for the
smoothed full series the bound

\[
 (Nh\,MY)^\epsilon\mathcal B_{A,B}(Y)                 \tag{5}
\]

for its squared mean with the factor \(1/B\). This is before the
coarse substitution \(\mathcal B_{A,B}(L_0)\ll M\).
Every numerator-prime extraction \(c=w e^2f^4n\), the row masks,
the fixed ray components, and the counts of \(e,f,w\) have already
been retained in (5). In particular, (5) is not a claim restricted to
squarefree moduli.

Each alternative in (4) is nondecreasing in \(L\), and each of its
monomials has \(L\)-exponent between zero and one. Consequently, for
\(k\ge1\),

\[
 \mathcal B_{A,B}(kL_0)
       \le k\mathcal B_{A,B}(L_0)=k\mathcal F(A,B).      \tag{6}
\]

The equality is a direct substitution of \(L_0=\sqrt M B\).
For the completed smoothed series, the source's convolution has
weights \((Nd)^{-1-6\eta}\) on this line. Weighted Cauchy has
finite total weight, while every \(d\) shortens \(Y\) by
\((Nd)^6\). Monotonicity in (4), exactly as in the last paragraph
of the source's Lemma 2, therefore preserves (5)--(6). The source's
bound also covers shortened scales below one.

## 4. Absorption preserves the refined quantity

Keep the full finite vector \(\mathbf Z\), and let

\[
 V(t)=\frac1B\sum_{a,b}\|\mathbf Z(hab^3,1+\eta+it)\|^2.
\]

The sum has exactly the restrictions in (2). Put \(u=1+\eta+it\)
and \(\theta=7/6\). Use the source's pole-cancelling kernel

\[
 K_u(w)=\Gamma(w)\left(1+\frac{w}{u-\theta}\right).
\]

The source's exact smoothed identity (5.3), with its continued
remainder \(\mathbf I\), and functional-equation bound (5.4) give

\[
 \frac1B\sum_{a,b}\|\mathbf I_{hab^3}(u;Y)\|^2
 \le C_\eta
 \left(\frac{Nh\,AB^3(1+|t|)^{10}}{Y^2}\right)^{2\eta}
 \int_{\mathbb R}V(-t-y)e^{-c|y|}\,dy.                 \tag{7}
\]

Choose

\[
 Y=k_\eta\sqrt{Nh}\,L_0(1+|t|)^5,
\]

where the fixed \(k_\eta\) will be taken sufficiently large. By
(5)--(6), the smoothed mean is at most

\[
 C_{\eta,\epsilon,k_\eta}
 (Nh\,M)^\epsilon\sqrt{Nh}(1+|t|)^6\mathcal F(A,B).
                                                               \tag{8}
\]

Here \(Y\ll k_\eta\sqrt{Nh}M^{3/2}(1+|t|)^5\), so a
sufficiently small internal subpower in (5) is absorbed in the
displayed arithmetic subpower and sixth height power. The fixed
finite-vector dimension changes only the constant.

The source's growth estimate ensures
\(\mathcal S=\sup_t V(t)/(1+|t|)^6<\infty\) for the fixed
\(h,A,B\). Divide the squared smoothed identity by
\((1+|t|)^6\). Equation (7), the exponential moment
\(\int(1+|y|)^6e^{-c|y|}\,dy<\infty\), and a sufficiently large
\(k_\eta\) give

\[
 \mathcal S\le\tfrac12\mathcal S+
 C_{\eta,\epsilon}(Nh\,M)^\epsilon\sqrt{Nh}
                              \mathcal F(A,B).
\]

Absorption proves the completed-vector version of (2). On
\(\Re u=1+\eta\), the reciprocal of \(\zeta_S(6u-5)\) is
bounded by an absolutely convergent Euler product. Removing it
proves (2) for \(D_\nu\). This argument uses no zero-free
hypothesis.

For (3), when \(B\le\sqrt M\), the terms \(M/B\) and
\(\sqrt M B\) in the first alternative of (1) are respectively
at most \(MB^{-1/2}\) and \(M^{3/4}B^{1/2}\). When
\(B\ge\sqrt M\), use the second alternative. This proves (3).

## 5. What the refinement does not supply

Primitive inversion subsequently sums over \(b\mid n\). Near its
balanced divisor range \(Nb\asymp\sqrt{Nn}\), (2) still has the
source's volume size. Even in ranges where (3) saves a power, applying
it to a specified scalar Gauss pairing does not estimate the full
character moment or the component orthogonal to a Gauss frame.

An exact physical-support argument can separately remove some large
primitive divisors from a smoothed scalar remainder. Combining that
argument with (2) requires retaining its Euler factors and Mellin
profiles. It is not part of theorem (2), and no boundary improvement
is inferred from the refinement alone.
