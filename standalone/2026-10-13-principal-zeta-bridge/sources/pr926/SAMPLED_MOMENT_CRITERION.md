# Sparse scale sampling for inverse moments with a nonvanishing Mellin detector

**Status:** new proved sampling inequalities and conditional moment-to-zero implications, 2026-10-10. The arithmetic sampled averages remain unproved. No full fourth moment, new zero-free boundary, or RH conclusion is asserted.

**Main advance:** for the existing universal test, integrated moments can be recovered, without a power loss, from values on a suitably distributed subset of the logarithmic scale interval. The retained subset may have measure tending to zero. A discrete version needs only slightly more than \((\log X)^2\) sample points per dyadic interval. A different, explicitly constructed universal test reduces the necessary sample density further. Every test is fixed before the scale varies.

**Sources and retained scope.**

- PR 912, commit 6afd64e042ce7b59d550c3d76e9e2cca8b2c7379, MELLIN_AND_SPIKES.md, Proposition 1.1: the existing universal test \(W_*\).
- PR 917, commit 6b4723042b3d250024eef45cb1924f88f28e902c, SCALE_AVERAGED_CRITERION.md, Theorem 3.1: causal inversion of the moving average of exact sixth-power masks. Its fixed-row extraction proof is recalled where the row budget below differs.
- PR 919, commit 9b04a887e171b3104a66cf57296ce5b0b2920d78, COFINAL_AVERAGED_REDUCTION.md and SMALL_GCD_CONDUCTOR_REDUCTION.md: the signed pointwise remainder inequalities and their analytic dependencies. Their arithmetic remainder estimates are still open.

The sampling inequalities use only smoothness of the fixed test, elementary ideal counting, and explicit interpolation. They do not use the imported native inverse second moment, a zero-free theorem, a Gauss estimate, or Möbius cancellation. Composing them with the higher-order signed reduction retains that reduction's native second-moment premise. The separate fourth-order signed reduction retains its classical-sieve premises.

**What was actually done:** exact derivative estimates for infinite convolutions; an integrated sampling lemma for arbitrary measurable retained sets; a finite-grid interpolation inequality; quantitative choices of the interpolation degree; and a fixed-row-budget extraction proof. Section 8 additionally proves an unconditional wide-aperture modulation average and identifies why it does not give the missing fixed-test moment.

## 1. The family and the row budget that will be recovered

Let \(K=\mathbb Q(\sqrt{-3})\), let \(S\) be the fixed finite set of excluded primes, and fix a finite-order coefficient character \(\nu\). Use the source's literal zero-extended sextic symbol:

\[
A_u(D;W)=
\sum_{(n,S)=1}\mu_K(n)\nu(n)\chi_n(u)W(Nn/D),
\qquad
\chi_n(u)=(u/n)_6.
\tag{1.1}
\]

Ideal indices and all nonzero element rows are retained. Write

\[
M_p(D,H;W)=\sum_{0<Nu\le H}|A_u(D;W)|^p,
\qquad p\ge1.
\tag{1.2}
\]

Fix \(h>0\) and \(X\ge2\), and put \(L_0=\log2\). The known data will concern the original moving-height moment at selected scales \(D=Xe^t\), \(0\le t\le L_0\). The recovered quantity is

\[
Q^\flat_{p,h}(X;W)=
\int_0^{L_0}M_p(Xe^t,X^h;W)\,dt.
\tag{1.3}
\]

The height in (1.3) is fixed at \(X^h\). Since \(X^h\le(Xe^t)^h\), every row used in the interpolation is included in the original moment throughout the entire interval.

We do not claim to recover \(M_p(D,D^h)\) across its moving row-entry endpoints. The fixed lower height is sufficient for zero extraction because it stays within a fixed factor of \(D^h\) on each dyadic interval; Section 6 proves this explicitly.

## 2. Fixed universal tests with explicit derivative growth

Let \(\mathscr L:\mathbb N\to[1,\infty)\) be nondecreasing and satisfy

\[
\mathscr L(j+1)\le C_0\mathscr L(j),\qquad
\sum_{j\ge1}\frac1{j\mathscr L(j)}<\infty.
\tag{2.1}
\]

Choose \(c>0\) sufficiently small that

\[
a_j=\frac{c}{j\mathscr L(j)},\qquad
A=\sum_ja_j<\frac{\log2}{2}.
\tag{2.2}
\]

Let \(U_j\) be independent uniforms on \([-a_j,a_j]\), and let \(f\) be the density of their absolutely convergent sum. Set

\[
t_0=\frac{\log2}{2},\qquad
W_{\mathscr L}(y)=f(\log y-t_0).
\tag{2.3}
\]

### Proposition 2.1. Detector and derivative estimate

The function \(W_{\mathscr L}\) is nonnegative, nonzero, and belongs to \(C_c^\infty((1,2))\). Its Mellin transform is

\[
\widehat W_{\mathscr L}(s)
=e^{t_0s}\prod_{j\ge1}\frac{\sinh(a_js)}{a_js},
\tag{2.4}
\]

and is nonzero for every \(\Re s>0\). There is \(B\ge1\), depending only on the fixed width sequence, such that for every integer \(m\ge1\),

\[
\|f^{(m)}\|_\infty
\le B^{m+1}m!\,\mathscr L(m)^m.
\tag{2.5}
\]

The existing \(W_*\) is the special case \(\mathscr L(j)=j\), \(c=\log2/8\), with

\[
\|f^{(m)}\|_\infty\le B^{m+1}(m!)^2.
\tag{2.6}
\]

**Proof.** Absolute convergence and compact support follow from \(\sum a_j<\infty\). The characteristic function is

\[
\varphi(\xi)=\prod_j\frac{\sin(a_j\xi)}{a_j\xi}.
\]

For any fixed integer \(N\), retaining the first \(N\) factors bounds it by
\(\prod_{j\le N}\min(1,(a_j|\xi|)^{-1})\). Thus it decays faster than every prescribed inverse power, with a constant depending on that power. Fourier inversion gives a smooth density on the whole line. It is nonnegative and supported in \([-A,A]\), as it represents the original probability distribution. This proves the support and smoothness assertions.

The compactly supported distribution gives (2.4) by bounded convergence. The factors differ from one by \(O(a_j^2|s|^2)\) on compact \(s\)-sets; \(\sum a_j^2<\infty\). Each local factor has its nonzero zeros on the imaginary axis. At a point off that axis, no factor vanishes, and the summable deviations from one make their infinite product nonzero.

For the derivative bound, let \(b_j=(2a_j)^{-1}1_{[-a_j,a_j]}\). Its distributional derivative is a signed measure of total variation \(a_j^{-1}\). Differentiate the first \(m\) convolution factors once each. The remaining probability convolution includes \(b_{m+1}\), whose supremum norm is \((2a_{m+1})^{-1}\). Hence

\[
\|f^{(m)}\|_\infty
\le \frac1{2a_{m+1}}\prod_{j=1}^m a_j^{-1}
=\frac{(m+1)!}{2c^{m+1}}
\prod_{j=1}^{m+1}\mathscr L(j).
\tag{2.7}
\]

This distributional bound is a pointwise bound because \(f^{(m)}\) is continuous. Monotonicity bounds the product by \(\mathscr L(m+1)^{m+1}\). Also

\[
\mathscr L(m+1)^{m+1}
\le C_0^m\mathscr L(m)^m\mathscr L(m+1)
\le \mathscr L(1)C_0^{2m}\mathscr L(m)^m.
\]

Absorb \(m+1\le2^m\) and the fixed constants into \(B^{m+1}\). This proves (2.5). Taking \(\mathscr L(j)=j\) gives (2.6) and exactly the previously defined test. \(\square\)

### Corollary 2.2. Native row derivatives, uniform in the row

For \(0\le t\le L_0\), every nonzero row \(u\), and every \(m\ge1\),

\[
\left\|\frac{d^m}{dt^m}A_u(Xe^t;W_{\mathscr L})\right\|_\infty
\le C_K X B^{m+1}m!\,\mathscr L(m)^m.
\tag{2.8}
\]

The constant \(B\) can be enlarged once without depending on \(X,u,m\).

**Proof.** The logarithmic derivative of one test factor is a signed translate of \(f^{(m)}\). Its support permits only \(Nn\le4X\) on this interval. The number of such ideals is \(O_K(X)\). Every coefficient, including the original nonunit zero, has modulus at most one. Sum (2.5) over the contributing ideals. \(\square\)

In particular, the derivative bound is not an unproved derivative-moment hypothesis. Its growth in \(m\) is explicit, so \(m\) may later grow with \(X\).

## 3. Integrated observations on an arbitrary measurable retained set

### Lemma 3.1. Interpolation from integrated data

Let \(I\) be a compact interval of length \(a>0\), let \(E\subset I\) be measurable with \(|E|\ge\gamma a\), \(0<\gamma\le1\), and let \(f\in C^m(I;\mathbb C)\), \(m\ge1\). For every \(1\le p<\infty\),

\[
\|f\|_{L^p(I)}
\le \left(\frac{C}{\gamma}\right)^m
     \|f\|_{L^p(E)}
+\frac{a^{m+1/p}}{m!}\|f^{(m)}\|_\infty,
\tag{3.1}
\]

where \(C>1\) is an absolute constant.

**Proof.** Chebyshev's inequality leaves a measurable \(E_0\subset E\), of measure at least \(\gamma a/2\), on which

\[
|f(t)|\le
\left(\frac2{\gamma a}\right)^{1/p}\|f\|_{L^p(E)}.
\tag{3.2}
\]

This remains valid if that norm is zero, by removing its null exceptional set.

Choose \(m\) points in \(E_0\) separated by at least \(d=\gamma a/(4m)\). A greedy choice is possible: after fewer than \(m\) selections, their excluded \(d\)-neighborhoods have total length less than \(2md=\gamma a/2\). Order the chosen points \(t_1<\cdots<t_m\). Then \(|t_j-t_i|\ge|j-i|d\).

Let \(P\) be their degree at most \(m-1\) interpolation polynomial. Its Lagrange basis satisfies

\[
\begin{aligned}
\sup_{t\in I}\sum_{j=1}^m|L_j(t)|
&\le
\left(\frac ad\right)^{m-1}
\sum_{j=1}^m\frac1{(j-1)!(m-j)!}\\
&=\frac{(8m/\gamma)^{m-1}}{(m-1)!}
\le\left(\frac{16e}{\gamma}\right)^{m-1}.
\end{aligned}
\tag{3.3}
\]

For \(m=1\) the sum equals one. Combining (3.2) and (3.3), and using \(\gamma^{-1/p}\le\gamma^{-1}\), gives

\[
\|P\|_{L^p(I)}
\le(C/\gamma)^m\|f\|_{L^p(E)}.
\]

The interpolation remainder satisfies

\[
|f(t)-P(t)|
\le\frac{\|f^{(m)}\|_\infty}{m!}
\prod_{j=1}^m|t-t_j|
\le\frac{a^m}{m!}\|f^{(m)}\|_\infty.
\tag{3.4}
\]

For complex \(f\), the same bound follows from the divided-difference integral formula: an \(m\)-th divided difference is the integral of \(f^{(m)}\) over a simplex of volume \(1/m!\), evaluated at convex combinations of its nodes. This formula follows by iterating the fundamental theorem of calculus and is complex-linear. It avoids assuming a real mean-value point for a complex function. The \(L^p\) triangle inequality proves (3.1). \(\square\)

### Lemma 3.2. A partition with distributed retained scales

Partition \([0,L_0]\) into intervals of length at most \(\ell\), and suppose \(G\) occupies at least a fraction \(\gamma\) of every partition interval. Then

\[
\|f\|_{L^p(0,L_0)}
\le(C/\gamma)^m\|f\|_{L^p(G)}
+\frac{L_0^{1/p}\ell^m}{m!}\|f^{(m)}\|_\infty.
\tag{3.5}
\]

**Proof.** Apply Lemma 3.1 on each cell and use the \(\ell^p\) triangle inequality over the cells. Their derivative-error \(p\)-th powers sum to at most
\(\ell^{mp}\|f^{(m)}\|_\infty^p\sum_I|I|/(m!)^p\).
Their lengths sum to \(L_0\). Thus there is no factor equal to the number of cells. \(\square\)

The retained set may be disconnected, chosen adaptively, or have highly irregular boundaries. Its integrated values, rather than a supremum or preselected good points, are the input to the lemma.

## 4. Quantitative moment recovery and its power-loss-free regime

For a retained set \(G_X\subset[0,L_0]\), define

\[
Q^G_{p,h}(X;W)=
\int_{G_X}M_p(Xe^t,(Xe^t)^h;W)\,dt.
\tag{4.1}
\]

### Theorem 4.1. Quantified recovery from distributed observations

Suppose \(G_X\) occupies at least a fraction \(\gamma_X\) of every cell of a partition whose maximum length is \(\ell_X\). For every integer \(m\ge1\),

\[
\begin{aligned}
\bigl(Q^\flat_{p,h}(X;W_{\mathscr L})\bigr)^{1/p}
\le{}&
\left(\frac C{\gamma_X}\right)^m
\bigl(Q^G_{p,h}(X;W_{\mathscr L})\bigr)^{1/p}\\
&+C_{K,p,W}X^{1+h/p}
       [B\ell_X\mathscr L(m)]^m .
\end{aligned}
\tag{4.2}
\]

The constants \(B,C\) are independent of \(X,m\), all rows, and the measurable choice of \(G_X\).

**Proof.** Apply Lemma 3.2 and (2.8) to every function \(t\mapsto A_u(Xe^t)\) with \(Nu\le X^h\). Use the \(\ell^p\) triangle inequality over this fixed row set, whose cardinality is \(O_K(X^h)\). On \(G_X\), its row sum is at most the original moving-height moment because \(X^h\le(Xe^t)^h\). This proves (4.2), after absorbing a fixed factor \(B\) into the outside constant. \(\square\)

### Corollary 4.2. No power loss

Put \(L=\log X\). Suppose

\[
\ell_X\mathscr L(\lceil L\rceil)\longrightarrow0.
\tag{4.3}
\]

A fixed positive retained fraction \(\gamma_X=\gamma>0\) is allowed. More generally set

\[
r_X=\log\frac1{\ell_X\mathscr L(\lceil L\rceil)},\qquad
\Gamma_X=\log(C/\gamma_X),
\]

and suppose

\[
\Gamma_X\left(\frac1{r_X}+\frac1L\right)\longrightarrow0.
\tag{4.4}
\]

For every fixed \(p\ge1\), \(h>0\), \(a\ge0\), if

\[
Q^G_{p,h}(X)\ll_\epsilon X^{h+a+\epsilon}
\quad\text{for every }\epsilon>0,
\tag{4.5}
\]

then

\[
Q^\flat_{p,h}(X)\ll_\epsilon X^{h+a+\epsilon}
\quad\text{for every }\epsilon>0.
\tag{4.6}
\]

**Proof.** Since \(r_X\to\infty\), for all sufficiently large \(X\) choose

\[
m_X=\left\lceil\frac{4L}{r_X}\right\rceil.
\tag{4.7}
\]

This is at least one and is at most \(\lceil L\rceil\) eventually. Monotonicity of \(\mathscr L\), followed by \(r_X\ge2\log B\), gives

\[
B\ell_X\mathscr L(m_X)
\le B e^{-r_X}\le e^{-r_X/2}.
\]

Consequently

\[
X[B\ell_X\mathscr L(m_X)]^{m_X}
\le X e^{-m_Xr_X/2}\le X^{-1}.
\tag{4.8}
\]

The observational factor has logarithm at most

\[
m_X\Gamma_X
\le\left(\frac{4L}{r_X}+1\right)\Gamma_X=o(L).
\tag{4.9}
\]

Thus (4.2) implies

\[
(Q^\flat)^{1/p}
\le X^{o(1)}(Q^G)^{1/p}
+O(X^{h/p-1}).
\tag{4.10}
\]

Raise to the fixed \(p\)-th power and allocate the arbitrarily small exponent in (4.5). The derivative error is \(O(X^{h-p})\), smaller than \(X^{h+a}\) because \(a\ge0\). Initial bounded scales are absorbed into the constant. \(\square\)

The degree \(m_X\) may grow with \(X\), and always satisfies \(m_X=o(\log X)\). The explicit bound (2.8), valid for every \(m\) with one fixed \(B\), is essential. Mere membership of an arbitrary test in \(C_c^\infty\), without quantitative derivative control, would not justify this choice.

### Concrete retained-scale regimes

For the existing \(W_*\), condition (4.3) is simply

\[
\ell_X\log X\longrightarrow0.
\tag{4.11}
\]

One can therefore retain half of every logarithmic cell of length
\(1/(\log X\,\omega(X))\), where \(\omega(X)\to\infty\), and discard the other half.

There is also a vanishing-proportion example. Fix \(\delta,A>0\), choose cells of maximum length

\[
\ell_X=(\log X)^{-1-\delta},
\qquad
\gamma_X=(\log\log X)^{-A}.
\tag{4.12}
\]

Then \(r_X\sim\delta\log\log X\), while
\(\Gamma_X=O(\log\log\log X)\), so (4.4) holds. Retaining exactly a fraction \(\gamma_X\) of every cell gives total retained logarithmic measure tending to zero, while (4.6) still has no power loss.

These conclusions allow omitted scales to be numerous. They require local distribution of the retained scales, rather than merely a bound on their total measure.

## 5. A discrete multiplicative grid

The same mechanism gives a finite-sampling version. Let

\[
0=t_0<t_1<\cdots<t_N=L_0,\qquad
t_j=j\Delta,\quad \Delta=L_0/N,
\]

and define

\[
Q^{\rm grid}_{p,h}(X;W)
=\Delta\sum_{j=0}^N
M_p(Xe^{t_j},(Xe^{t_j})^h;W).
\tag{5.1}
\]

### Lemma 5.1. Grid interpolation in \(L^p\)

For \(f\in C^m([0,L_0])\), \(1\le m\le N+1\),

\[
\|f\|_{L^p(0,L_0)}
\le C^m\left(\Delta\sum_{j=0}^N|f(t_j)|^p\right)^{1/p}
+\frac{L_0^{1/p}(m\Delta)^m}{m!}\|f^{(m)}\|_\infty .
\tag{5.2}
\]

**Proof.** On each elementary grid interval, interpolate using \(m\) consecutive nodes. Use the block starting at its left endpoint when possible, and use the final block near the upper boundary. Every interpolation point is within \(m\Delta\) of the output interval. The same factorial-denominator calculation as (3.3), now with exact node spacing \(\Delta\), bounds the sum of absolute basis values by \(C^m\). The remainder is at most
\((m\Delta)^m\|f^{(m)}\|_\infty/m!\).

Each grid node is used by at most \(2m\) output intervals, including the repeated final block. Apply the \(L^p\) triangle inequality over intervals; the factor \((2m)^{1/p}\) is absorbed into a larger absolute \(C^m\). This proves (5.2). It applies at both endpoints and does not restrict a bandlimited polynomial to a varying row interval. \(\square\)

### Theorem 5.2. Discrete sampling criterion

For the universal test in Section 2,

\[
\begin{aligned}
(Q^\flat_{p,h}(X))^{1/p}
\le{}&C^m(Q^{\rm grid}_{p,h}(X))^{1/p}\\
&+C_{K,p,W}X^{1+h/p}
[B m\Delta_X\mathscr L(m)]^m.
\end{aligned}
\tag{5.3}
\]

In particular, if

\[
\Delta_X\log X\,
\mathscr L(\lceil\log X\rceil)\longrightarrow0,
\tag{5.4}
\]

then

\[
Q^{\rm grid}_{p,h}(X)\ll_\epsilon X^{h+a+\epsilon}
\quad\Longrightarrow\quad
Q^\flat_{p,h}(X)\ll_\epsilon X^{h+a+\epsilon}
\tag{5.5}
\]

for every fixed \(a\ge0\), with the customary quantifier for every \(\epsilon>0\).

**Proof.** Apply Lemma 5.1, (2.8), and the fixed-row \(\ell^p\) triangle inequality as in Theorem 4.1. This proves (5.3).

For the consequence, set

\[
r_X=\log\frac1{\Delta_XL\mathscr L(\lceil L\rceil)},
\qquad
m_X=\lceil4L/r_X\rceil.
\]

Then \(m_X=o(L)\), \(m_X\le\lceil L\rceil\), and \(m_X\le N_X+1\) for all sufficiently large \(X\). The last fact follows from \(\mathscr L\ge1\) and (5.4), which give \(N_X/L\to\infty\). As before,

\[
B m_X\Delta_X\mathscr L(m_X)\le e^{-r_X/2},
\]

after an immaterial fixed enlargement of constants to allow \(\lceil L\rceil/L\). The derivative error is \(O(X^{h/p-1})\), while \(C^{m_X}=X^{o(1)}\). The proof of Corollary 4.2 finishes (5.5). \(\square\)

For \(W_*\), take

\[
N_X=\left\lceil(\log X)^2\omega(X)\right\rceil,
\qquad \omega(X)\longrightarrow\infty.
\tag{5.6}
\]

Thus a weighted moment sum over \(O((\log X)^2\omega(X))\) explicitly specified scales in each dyadic interval is enough. No estimate at every individual real scale, and no derivative-moment estimate, is required. The sampled arithmetic moment bound in (5.5) is still an open input.

## 6. Extraction, signed remainders, and cofinal orders

### Theorem 6.1. Sampled moment-to-zero implication

Fix an integer \(k\ge1\), \(h>0\), \(e\ge0\), and one fixed test \(W_{\mathscr L}\). Suppose that on every sufficiently large dyadic \(X=2^j\), either:

1. the hypotheses of Corollary 4.2 hold and

\[
Q^G_{2k,h}(X;W_{\mathscr L})
\ll_\epsilon X^{h+k+e+\epsilon};
\tag{6.1}
\]

or

2. the grid condition (5.4) holds and

\[
Q^{\rm grid}_{2k,h}(X;W_{\mathscr L})
\ll_\epsilon X^{h+k+e+\epsilon}.
\tag{6.2}
\]

The upper bounds are required for every \(\epsilon>0\). Then every fixed primitive row twist induced by \(\nu(n)\chi_n(r)\) has no zero in

\[
\Re s>\frac12+\frac{5h}{12k}+\frac e{2k}.
\tag{6.3}
\]

**Proof.** Sections 4 or 5 first give the full fixed-height integral

\[
\int_X^{2X}M_{2k}(D,X^h;W_{\mathscr L})\frac{dD}{D}
\ll_\epsilon X^{h+k+e+\epsilon}.
\tag{6.4}
\]

For \(D\in[2^j,2^{j+1})\), put

\[
H_\flat(D)=2^{jh},\qquad
Y_r(D)=(H_\flat(D)/Nr)^{1/6}.
\tag{6.5}
\]

This is a measurable stepwise cutoff. For each fixed nonzero \(r\), it is at least one eventually and

\[
Y_r(D)\ge (2^{-h}/Nr)^{1/6}D^{h/6}.
\tag{6.6}
\]

The exact identity \(T_vA_r(D)=A_{rv^6}(D)\), and Jensen over \(Nv\le Y_r(D)\), give

\[
|M_{Y_r(D)}A_r(D)|^{2k}
\ll_{K,r,h}D^{-h/6}
M_{2k}(D,H_\flat(D)).
\tag{6.7}
\]

Fix
\(\sigma>1/2+5h/(12k)+e/(2k)\).
Multiplying (6.7) by \(D^{-2k\sigma}\), integrating each dyadic interval using (6.4), and taking a sufficiently small positive loss produces the summable series with exponent

\[
k+5h/6+e-2k\sigma+\epsilon<0.
\]

PR 917's causal moving-cutoff theorem applies to (6.6). Its proof permits an arbitrary measurable cutoff with this lower bound, including step functions. It yields

\[
\int_0^\infty|A_r(D;W_{\mathscr L})|^{2k}
D^{-2k\sigma}\frac{dD}{D}<\infty.
\tag{6.8}
\]

The function is locally bounded and vanishes below a positive scale, as required.

Hölder's inequality makes the scale Mellin integral holomorphic for \(\Re s>\sigma\). On its initial half-plane of absolute convergence, it equals

\[
\widehat W_{\mathscr L}(s)\frac{E_r(s)}{L_K(s,\psi_r)}.
\tag{6.9}
\]

Here \(E_r\) is the finite, nonvanishing Euler correction for the fixed inducing character. Proposition 2.1 gives nonvanishing of the test throughout \(\Re s>0\). A zero of \(L_K(s,\psi_r)\) in \(\Re s>\sigma\) would therefore produce a pole incompatible with the holomorphic Mellin integral. Let \(\sigma\) approach the stated strict boundary. \(\square\)

The height in the recovered moment is never silently changed from \(X^h\) to \(D^h\). The comparison enters only through the valid lower bound (6.6) for the replica cutoff.

### Signed arithmetic inputs remain one-sided

Suppose an existing exact reduction gives

\[
M_{2k}(D,D^h)
\le C_\epsilon D^{h+k+d+\epsilon}+2T(D),
\qquad d\ge0,
\tag{6.10}
\]

where \(T\) is the original real signed remainder. Its algebra and all of its source hypotheses are retained.

For distributed retained scales, it suffices to prove

\[
\int_{G_X}T(Xe^t)\,dt
\le C_\epsilon X^{h+k+e+\epsilon}.
\tag{6.11}
\]

For the finite grid, it suffices to prove

\[
\Delta_X\sum_j T(Xe^{t_j})
\le C_\epsilon X^{h+k+e+\epsilon}.
\tag{6.12}
\]

Integrating or summing (6.10) with its nonnegative sampling weights gives (6.1) or (6.2) with excess \(\lambda=\max(d,e)\). The controlled term costs no extra power: the total retained measure is at most \(\log2\), and the total grid weight is \(\log2+\Delta_X=O(1)\). The resulting boundary is

\[
\Re s>\frac12+\frac{5h}{12k}
+\frac{\max(d,e)}{2k}.
\tag{6.13}
\]

No absolute value of \(T\) is inserted. There is no regularity assumption on a changing cutoff inside \(T\); interpolation is applied to the original smooth fixed-row functions, not to the signed remainder itself.

For PR 919's fourth-order small-gcd remainder, \(d=0\) and
\(1<h\le11/10\). Thus the same \(1/2+5h/24+e/4\) consequence follows from either sampled signed premise above, subject to its sampling geometry.

For PR 919's cofinal incidence reduction,

\[
d=(2b-1)q,\qquad 1/2<b\le1,\qquad Q_0=D^q.
\]

Its inherited native moment premise remains necessary. Along an unbounded sequence of fixed orders, \(h_k=o(k)\), \(q_k=o(k)\), and \(e_k=o(k)\) still make the conditional boundary tend to \(1/2\). The interpolation factors are \(X^{o(1)}\) at each fixed order and do not create a new order-dependent power excess.

The target row and character stay fixed while choosing the cofinal order. Constants need not be uniform in the order. Coverage of contragredient characters is still needed for the reflected critical-line conclusion. These are conditional consequences; neither sampled signed estimate has been proved here.

## 7. Quantitative improvement from different fixed tests

The profiles below all meet (2.1). The logarithms are regularized at bounded arguments as displayed, and each test is normalized once so its support lies in \((1,2)\).

| Fixed profile \(\mathscr L(j)\) | Retained-set mesh condition | Discrete-grid mesh condition |
| --- | --- | --- |
| \(j\), the existing \(W_*\) | \(\ell_X\log X\to0\) | \(\Delta_X(\log X)^2\to0\) |
| \([\log(e+j)]^{1+\delta}\), \(\delta>0\) | \(\ell_X(\log\log X)^{1+\delta}\to0\) | \(\Delta_X\log X(\log\log X)^{1+\delta}\to0\) |
| \(\log(e+j)[\log\log(e^e+j)]^{1+\delta}\), \(\delta>0\) | \(\ell_X\log\log X(\log\log\log X)^{1+\delta}\to0\) | \(\Delta_X\log X\log\log X(\log\log\log X)^{1+\delta}\to0\) |

The summability assertions reduce respectively to
\(\sum j^{-2}<\infty\),
\(\sum[j(\log j)^{1+\delta}]^{-1}<\infty\), and
\(\sum[j\log j(\log\log j)^{1+\delta}]^{-1}<\infty\).
The integral test proves each one after a bounded initial segment. The profiles are nondecreasing and have bounded consecutive ratios, so Proposition 2.1 applies directly.

For instance, the third test permits a finite grid with

\[
N_X\asymp
\log X\,\log\log X\,
(\log\log\log X)^{1+\delta}\omega(X),
\qquad \omega(X)\to\infty,
\tag{7.1}
\]

in place of the existing detector's slightly super-\((\log X)^2\) grid.

This is a change of the fixed detector, not an inference that an arithmetic estimate for one test automatically holds for another. When using a new test, the sampled arithmetic premise must be proved for that test. The exact source reductions are compatible with any such fixed smooth test; their constants retain their allowed dependence on it.

The construction does not supply a lower bound on the Mellin transform at large imaginary parts. It needs only nonvanishing. Compact support, quantitative derivative growth, and the Mellin detector are simultaneously retained.

## 8. What test modulation proves, and the aperture cost it leaves

There is an elementary unconditional diagonal moment after sufficiently wide averaging over test modulations. It is useful to state it with its necessary limitation.

Let \(W\) be any fixed smooth compactly supported test and put

\[
W_\tau(y)=y^{i\tau}W(y).
\tag{8.1}
\]

For the universal tests above, every fixed \(W_\tau\) still has a nonvanishing Mellin transform in \(\Re s>0\), since
\(\widehat W_\tau(s)=\widehat W(s+i\tau)\).

### Proposition 8.1. Wide-aperture modulation moment

For fixed \(k\ge1\), \(D\ge2\), \(H,T\ge1\), and every \(\epsilon>0\),

\[
\frac1{2T}\int_{-T}^T
M_{2k}(D,H;W_\tau)\,d\tau
\ll_{k,W,K,\epsilon}
H D^{k+\epsilon}\left(1+\frac{D^k}{T}\right).
\tag{8.2}
\]

For each fixed \(D,H\), the Cesaro limit as \(T\to\infty\) is therefore \(O(H D^{k+\epsilon})\).

**Proof.** Expand the ordinary \(k\)-th power and group the ideal tuples by their product norm:

\[
A_u(D;W_\tau)^k
=D^{-ik\tau}\sum_{N\le C_{k,W}D^k}
C_{u,D}(N)N^{i\tau}.
\tag{8.3}
\]

The number of ordered \(k\)-tuples of ideals with product norm \(N\) is at most \(d_{2k}(N)\), because the ideal-count coefficient at a rational integer \(n\) is at most \(d_2(n)\). For each fixed \(k\), the elementary divisor estimate bounds \(d_{2k}(N)\) by \(O_{k,\eta}(N^\eta)\) for every \(\eta>0\). To see this last bound, the prime-power coefficient is \(\binom{e+2k-1}{2k-1}\), a fixed polynomial in \(e\). At all sufficiently large rational primes it is at most \(p^{\eta e}\) for every \(e\ge1\); each of the finitely many smaller primes has the same bound with its own fixed multiplicative constant. Multiply these local bounds. Cauchy--Schwarz within each norm group consequently gives

\[
\sum_N|C_{u,D}(N)|^2\ll_{k,W,\epsilon}D^{k+\epsilon},
\tag{8.4}
\]

uniformly in the row. Indeed the total squared coefficient mass before grouping is at most
\((\sum_{Nn\ll_WD}|W(Nn/D)|^2)^k=O_W(D^k)\).

For an arbitrary polynomial \(P(\tau)=\sum_{N\le L}c_NN^{i\tau}\), direct integration gives diagonal contribution \(\sum|c_N|^2\). If \(N\ne M\),

\[
\left|\frac1{2T}\int_{-T}^T(N/M)^{i\tau}\,d\tau\right|
\le\frac1{T|\log(N/M)|}
\le\frac L{T|N-M|}.
\]

Summing by \(r=|N-M|\), and using
\(\sum_N|c_Nc_{N+r}|\le\sum_N|c_N|^2\), gives

\[
\frac1{2T}\int_{-T}^T|P(\tau)|^2\,d\tau
\le\left(1+\frac{2L(1+\log L)}T\right)
\sum_N|c_N|^2.
\tag{8.5}
\]

Insert \(L\ll_{k,W}D^k\), absorb the logarithm into the prescribed positive loss, apply (8.4), and sum the \(O_K(H)\) rows. This proves (8.2). The finite polynomial expansion also shows directly that its Cesaro limit retains exactly the equal-product-norm groups. \(\square\)

This estimate does not give a fixed-test moment near the target. At \(T=D^a\), the normalized average has excess \(\max(0,k-a)\). Using (8.2) and positivity to bound a fixed finite interval of modulation parameters restores the factor \(T\) from the unnormalized integral. The available excess then becomes

\[
a+\max(0,k-a)=\max(a,k)\ge k.
\tag{8.6}
\]

That is insufficient for the desired cofinal sublinear excess. A normalized mean whose aperture tends to infinity can assign vanishing mass to every fixed modulation interval. One cannot select a single fixed \(\tau\) with the required bounds at all scales from (8.2).

There is likewise no free off-diagonal cancellation from averaging the original nonnegative test over \(D\). Its expanded moment has the kernel

\[
\int_X^{2X}
\prod_{i=1}^kW(Nn_i/D)
\prod_{j=1}^kW(Nm_j/D)\frac{dD}{D}\ge0.
\tag{8.7}
\]

Choose an interval \([a,b]\subset(1,2)\) on which \(W\ge c>0\). For a sufficiently small fixed \(\eta>0\), all tuple norms in
\([a(1+\eta)X,bX]\) have kernel at least
\(c^{2k}\log(1+\eta)\), by restricting \(D\) to \([X,(1+\eta)X]\).
Thus a full fixed-proportion shell of balanced tuples receives no power attenuation from this smoothing kernel alone. Its arithmetic coefficient cancellation remains necessary.

## 9. What has and has not been gained

The new unconditional statements are the explicit all-derivative bound, integrated interpolation from arbitrary locally distributed observations, and the resulting quantitative recovery of a full lower-height moment. They permit rigorously sparser arithmetic hypotheses while preserving the same zero-extraction exponent. The new fixed detectors improve the scale mesh without losing Mellin nonvanishing.

The measurable-set and grid arguments keep one common row set throughout each interpolation interval. Their conclusion is a fixed lower-height integral; the stepwise replica cutoff then supplies the valid extraction. No moving-row endpoint or unproved derivative moment is hidden in that passage.

The remaining arithmetic task can now be posed on retained apertures or on an explicit finite scale grid. Proving that sampled signed average still requires cancellation in the actual Möbius/sextic family. The wide-modulation theorem identifies a real averaged upper bound, but its aperture cost is linear in the moment order at the level needed for fixed-test extraction. It does not close that gap.
