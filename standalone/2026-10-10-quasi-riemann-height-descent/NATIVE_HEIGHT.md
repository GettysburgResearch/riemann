# Native height localization: coherent Newton compression and a complete joint inverse/plain moment

Date: 10 October 2026.
Status: proposed component mathematics with proofs; no improved zero-free half-plane is claimed.
Scope: finite arithmetic identities; a uniform-in-height coarse compression; a complete joint Dirichlet-polynomial mean-square bound; a source-explicit local zero detector.
Inputs: the classical divisor inverse identity, Euler summation, and the previously reviewed finite Dirichlet-polynomial mean-value inequality stated below.
Not used: the imported \(7/8\) theorem, an assumed Chowla bound, independent random phases, a numerical zero census, or a favorable covariance sign.
What was run: the companion exact checker tests the finite arithmetic identities, a Gaussian-rational completely multiplicative twist, the block antiderivative, and the uniform compression bound. It does not verify an infinite analytic theorem numerically.
Smallest missing gain: a center-dependent upper bound for the explicit local off-diagonal functional in Section 6. The averaged estimate proved here does not supply it.

## 1. Sources and purpose

The starting native identities and cubic mesh are [NRC32 at 0f82df3bf1d0bc669a1bbca09f8404b77c6fecde](https://github.com/GettysburgResearch/riemann/blob/0f82df3bf1d0bc669a1bbca09f8404b77c6fecde/standalone/2026-09-21-native-covariance-compression/PROOF.md). The contrast with a source-only phase twist is [CAP36 at aa725eebf89201fcbefbf7f5e209a22ec318ba5a](https://github.com/GettysburgResearch/riemann/blob/aa725eebf89201fcbefbf7f5e209a22ec318ba5a/standalone/2026-09-25-completion-anchored-phase/PROOF.md), and the averaged/principal-member distinction is [ADP37 at the same head](https://github.com/GettysburgResearch/riemann/blob/aa725eebf89201fcbefbf7f5e209a22ec318ba5a/standalone/2026-09-25-anchored-dephasing/PROOF.md).

The external methodological motivation is the common-kernel signed preimage sum in the [October 5 second-transfer lemma](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/The-Quasi-Riemann-Hypothesis-October-5-2026/build/paper2.tex), label lem:second-transfer. No Eisenstein-field coefficient or automorphic estimate is transplanted without an adapter.

The positive results here are:

1. Twisting every convolution factor coherently gives an exact native height family, with **zero algebraic phase defect** and an explicit changed kernel.
2. The complete cubic-mesh detail error stays below \(5/6\) for **all real heights**, with no factor growing in height.
3. The complete mixed inverse/plain product has an unconditional mean-square bound
   \[
   \int_{T}^{T+H}|G_Y(\sigma+it)B_Y(\sigma+it)-1|^2dt
   \ll_\sigma (1+\log Y)^3
   \left(HY^{1-2\sigma}+Y^{4-4\sigma}\right).
   \]
4. At a hypothetical zero, a fully priced Euler approximation forces a large value of this same product defect. A local Sobolev estimate turns it into an explicit positive local-energy threshold. Its diagonal tends to zero; the remaining off-diagonal is written exactly.

These are an extension of the native toolkit and a concrete height-sensitive target. They are not a new global zero-density record or a proof that any previously forbidden half-plane is larger.

## 2. Coherent height twisting removes the algebraic defect

### 2.1 The exact convolution automorphism

For real \(t\), set
\[
\chi_t(n)=n^{-it},\qquad
(\mathcal T_t a)(n)=\chi_t(n)a(n).
\]
For arbitrary arithmetic functions \(a,b\), finite divisor expansion gives
\[
\mathcal T_t(a*b)=(\mathcal T_ta)*(\mathcal T_tb).
\]
Indeed \(\chi_t(d)\chi_t(n/d)=\chi_t(n)\) in every summand. In particular,
\[
\mathcal T_t\mathbf1=\chi_t,\qquad
\mu_t:=\mathcal T_t\mu,\qquad
\chi_t*\mu_t=\delta.
\]

For an integer \(Y\ge1\), let \(g_Y=\mu\mathbf1_{n\le Y}\), \(g_{Y,t}=\mathcal T_tg_Y\), and
\[
e_{Y,t}=\delta-\chi_t*g_{Y,t}.
\]
Then \(e_{Y,t}(n)=0\) for \(n\le Y\). Applying the automorphism to the classical Newton identity yields
\[
\mu_t-\bigl(2g_{Y,t}-\chi_t*g_{Y,t}*g_{Y,t}\bigr)
=\mu_t*e_{Y,t}*e_{Y,t}.
\]
Every nonzero index of \(e_{Y,t}\) is at least \(b=Y+1\), so the right side vanishes for every \(n<b^2\).

**Conclusion.** The coherently twisted Newton update reconstructs \(\mu(n)n^{-it}\) exactly on the complete native square step, for every real \(t\). This statement is finite coefficient algebra; no zero-free assumption or limit in \(t\) enters.

This does not remove CAP36's defect while keeping CAP36's original observable. CAP36 leaves a different part of the convolution untwisted. Here the \(\mathbf1\) factor changes to \(\chi_t\); its observation kernel therefore changes as well.

### 2.2 The changed harmonic kernel is explicit

Write
\[
m_t(k)=\sum_{n\le k}\frac{\mu(n)}{n^{1+it}},\quad
z_Y=g_Y*g_Y,\quad
H_t(r)=\sum_{j=1}^{r}j^{-1-it},\quad H_t(0)=0.
\]
For \(Y<k<(Y+1)^2\), summing the exact coefficient identity gives
\[
m_t(k)=2m_t(Y)-
\sum_{d\le Y^2}\frac{z_Y(d)}{d^{1+it}}
H_t(\lfloor k/d\rfloor).
\]
The height occurs in both \(d^{-it}\) and \(H_t\). Replacing \(H_t\) by the ordinary harmonic numbers would not be an identity.

For integers \(a,d\ge1\), put \(r=\lfloor(a-1)/d\rfloor\) and
\[
A_{d,t}(a)=aH_t(r)-d\sum_{j=1}^{r}j^{-it}.
\]
Counting the number \(a-jd\) of appearances of each term gives
\[
A_{d,t}(a)=\sum_{k=0}^{a-1}H_t(\lfloor k/d\rfloor).
\]
Consequently the exact mean on a block \(I=[a,a+h)\) is
\[
\overline m_{t,I}
=2m_t(Y)-\frac1h
\sum_{d\le Y^2}\frac{z_Y(d)}{d^{1+it}}
\bigl(A_{d,t}(a+h)-A_{d,t}(a)\bigr).
\]
All ordered factorizations contributing to \(z_Y(d)\) are retained.

### 2.3 The full detail error is independent of height

Partition the integer cells \(b,\ldots,b^2-1\) by the NRC32 cubic mesh:
\[
a_0=b,\qquad
h=\min\{b^2-a,\lfloor(a^2/b)^{1/3}\rfloor\},\qquad
a\leftarrow a+h.
\]
The mesh has fewer than \(10b\) blocks and satisfies
\[
Z_Y:=\sum_{I=[a,a+h)}
\frac{h(h^2-1)}{12a^2}<\frac56.
\]

For any complex sequence \(v_k\), the exact variance identity is
\[
\sum_{k\in I}|v_k-\overline v_I|^2
=\frac1h\sum_{0\le i<j<h}|v_{a+j}-v_{a+i}|^2.
\]
For \(v_k=m_t(k)\),
\[
|m_t(k)-m_t(k-1)|=|\mu(k)|/k\le1/k,
\]
uniformly in real \(t\). Therefore
\[
|m_t(a+j)-m_t(a+i)|\le(j-i)/a,
\]
and the block detail energy is at most \(h(h^2-1)/(12a^2)\).

For **every** complex number \(c\), orthogonal projection gives
\[
\sum_{k=b}^{b^2-1}|m_t(k)-c|^2
=\sum_Ih|\overline m_{t,I}-c|^2+D_{Y,t},
\qquad
0\le D_{Y,t}\le Z_Y<5/6.
\]
The error is independent of \(c\), and all inequalities hold simultaneously for every real \(t\).

For completeness, the mesh count follows exactly as in NRC32: a nonfinal block has
\(h\ge\tfrac12(a^2/b)^{1/3}\) and \(h\le a\), so
\[
\int_a^{a+h}x^{-2/3}dx\ge2^{-5/3}b^{-1/3}.
\]
Summing through \(b^2\) gives fewer than \(10b\) blocks. Since \(h^3\le a^2/b\), each error contribution is at most \(1/(12b)\), proving \(Z_Y<5/6\).

This is a complete uniform-height compression theorem, not a numerical trend. The remaining coarse means have the new exact kernel above.

### 2.4 The height-dependent constant cannot be omitted

For \(t\ne0\), the standard limiting reciprocal sum is \(1/\zeta(1+it)\), generally nonzero; at \(t=0\) its value is zero. Thus the raw quantity \(\sum_{k\le X}|m_t(k)|^2\) can have a linear main term even when the centered fluctuations are small.

The finite theorem deliberately permits any \(c\), including an independently justified center or the least-squares center on the chosen interval. Choosing an interval-dependent center changes the observable and needs its own Mellin adapter before being used for a zero-free conclusion. The compression theorem alone makes no such inference. It does show that neither phase transport nor fine resolution has to carry an artificial polynomial cost in \(t\).

## 3. A complete joint inverse/plain moment with exact head cancellation

### 3.1 Form the product before estimating it

Define finite Dirichlet polynomials
\[
G_Y(s)=\sum_{a\le Y}\mu(a)a^{-s},\qquad
B_Y(s)=\sum_{b\le Y}b^{-s},\qquad
R_Y(s)=G_Y(s)B_Y(s)-1.
\]
Their product coefficients are
\[
e_Y(n)=\sum_{\substack{ab=n\\a,b\le Y}}\mu(a)-\mathbf1_{n=1}.
\]
Hence
\[
R_Y(s)=\sum_{Y<n\le Y^2}e_Y(n)n^{-s}.
\]

The vanishing for \(n\le Y\) is exact: every divisor pair of such an \(n\) lies inside the rectangle, so its coefficient is \(\sum_{a\mid n}\mu(a)=\mathbf1_{n=1}\). This is a common-product-kernel signed allocation. It is lost if one estimates \(G_Y\) and \(B_Y\) separately.

There is also an exact boundary form, for \(Y<n\le Y^2\):
\[
e_Y(n)=-
\sum_{\substack{a\mid n\\a>Y}}\mu(a)
-\sum_{\substack{a\mid n\\a<n/Y}}\mu(a).
\]
The two excluded sets are disjoint in this range. In particular,
\[
e_Y(n)=-1-\mu(n)\qquad(Y<n\le2Y,\ n\le Y^2).
\]
This last identity shows that the first boundary block is not a family of independent signs.

The elementary coefficient bounds are
\[
|e_Y(n)|\le d(n),\qquad d(n)^2\le d_4(n).
\]
The second follows prime by prime from
\[
(a+1)^2\le\binom{a+3}{3}\quad(a\ge0).
\]
Moreover
\[
\sum_{n\le Z}d_4(n)\le ZH_{\lfloor Z\rfloor}^3,
\]
by summing over the first three factors and counting the fourth.

### 3.2 Mean-value input and its scope

Use the previously reviewed analytic inequality
\[
\int_I\left|\sum_{n\le N}a_nn^{-it}\right|^2dt
\le(|I|+14N)\sum_{n\le N}|a_n|^2
\tag{MV}
\]
for any interval \(I\), any complex coefficients, and finite support. Its symmetric-interval version is in the frozen [Q4 statement](https://github.com/GettysburgResearch/riemann/blob/f99d9e3908dde4865377c75d9ca051c1f545bf4f/research/integrated/CURRENT_RESULTS.md#q4); the full repaired proof is in [the associated analytic repairs](https://github.com/GettysburgResearch/riemann/blob/f99d9e3908dde4865377c75d9ca051c1f545bf4f/reviews/D-pass3/PROOFS_AND_REPAIRS.md). Translating an interval only multiplies each coefficient by a unit phase.

This is a classical Dirichlet-polynomial mean-value input. It is unconditional and does not assume the desired arithmetic cancellation. An elementary termwise off-diagonal estimate gives the same theorem below with one additional logarithmic factor, so the conclusion does not depend on an unproved critical arithmetic estimate.

### 3.3 Quantitative theorem

Let \(Y\ge2\), \(1/2<\sigma<1\), \(H>0\), and \(T\in\mathbb R\). Define
\[
L_Y=H_{\lfloor2Y^2\rfloor},\quad
a_\sigma=(1-2^{1/2-\sigma})^{-1},\quad
b_\sigma=(1-2^{\sigma-1})^{-1}.
\]
Then
\[
\boxed{
\begin{aligned}
\int_T^{T+H}|R_Y(\sigma+it)|^2dt
\le L_Y^3\bigl[
4a_\sigma^2H Y^{1-2\sigma}
+112b_\sigma^2Y^{4-4\sigma}
\bigr].
\end{aligned}}
\tag{JM}
\]
The bound is uniform in the interval center \(T\).

**Proof.** Split the product indices into blocks
\((N_j,2N_j]\cap(Y,Y^2]\), \(N_j=2^jY\). On one block,
\[
\sum |e_Y(n)|^2n^{-2\sigma}
\le2N_j^{1-2\sigma}L_Y^3.
\]
Apply (MV) with support at most \(2N_j\). The \(L^2(I)\) norm of that block is at most
\[
L_Y^{3/2}
\left(\sqrt{2H}\,N_j^{1/2-\sigma}
+\sqrt{56}\,N_j^{1-\sigma}\right).
\]
Minkowski retains all cross-block covariance. The decreasing geometric series in the first term is at most \(a_\sigma Y^{1/2-\sigma}\). The increasing geometric series in the second is at most \(b_\sigma Y^{2-2\sigma}\). Square the resulting two-term bound and use \((u+v)^2\le2u^2+2v^2\). This gives (JM). QED.

If \(R_Y^{(r)}\) denotes the \(r\)-th derivative with respect to \(t\), then the same proof gives
\[
\int_T^{T+H}|R_Y^{(r)}(\sigma+it)|^2dt
\le(2\log Y)^{2r}\,B_\sigma(Y,H),
\tag{JM-r}
\]
where \(B_\sigma(Y,H)\) is the right side of (JM). This follows by bounding every coefficient factor \((\log n)^r\) by \((2\log Y)^r\); the dyadic proof and source support are unchanged.

At \(\sigma=7/8\),
\[
B_{7/8}(Y,H)\ll(1+\log Y)^3
\left(HY^{-3/4}+Y^{1/2}\right).
\]
This bounds the full joint defect, including its off-diagonal, rather than a product of separate fourth-moment bounds.

### 3.4 A precise averaged gain and its limitation

Dividing by \(H\), the average joint defect tends to zero if \(Y\to\infty\) and \(Y^{4-4\sigma}(1+\log Y)^3=o(H)\). For example at \(7/8\), any choice \(Y=H^q\) with fixed \(0<q<2\) gives a vanishing mean-square defect, up to the harmless lower-order term.

This is uniform in the center, but does not improve merely because the center tends to infinity. A small average still permits narrow bad peaks. Section 5 makes the zero-peak cost explicit.

## 4. Connect the finite product to an actual zeta zero, retaining the pole term

### 4.1 A uniform Euler remainder suitable for height localization

Let \(s=\sigma+it\), \(0<\sigma<1\), and let the integer \(Y\) satisfy
\(Y\ge2(|t|+1)\). Then
\[
\zeta(s)=B_Y(s)+\frac{Y^{1-s}}{s-1}+r_Y(s),
\qquad |r_Y(s)|\le2Y^{-\sigma}.
\tag{E}
\]
The pole term is part of the identity, not an error deleted on the critical strip.

**Proof.** Euler summation first gives, by analytic continuation from \(\sigma>1\),
\[
\zeta(s)=B_Y(s)+\frac{Y^{1-s}}{s-1}
-s\int_Y^\infty\{x\}x^{-s-1}dx.
\]
Write \(\{x\}=1/2+\psi(x)\). The constant contributes
\(-Y^{-s}/2\). The periodic sawtooth has Abel-regularized Fourier series
\[
\psi(x)=-\lim_{r\uparrow1}\sum_{k\ge1}
\frac{r^k\sin(2\pi kx)}{\pi k}.
\]
The regularizations are uniformly bounded by \(1/2\), as Poisson averages of the sawtooth, so dominated convergence applies to the absolutely integrable factor \(x^{-\sigma-1}\).

For either phase
\(\phi_\pm(x)=\pm2\pi kx-t\log x\), the derivative is monotone, has constant sign, and satisfies
\[
|\phi_\pm'(x)|\ge2\pi k-\tfrac12>5k
\quad(x\ge Y).
\]
One integration by parts, retaining the derivative of \(1/\phi_\pm'\), yields
\[
\left|\int_Y^\infty x^{-\sigma-1}e^{i\phi_\pm(x)}dx\right|
\le\frac{3}{5k}Y^{-\sigma-1}.
\]
The boundary and amplitude derivative contribute at most \(2Y^{-\sigma-1}/(5k)\), and the monotone reciprocal-phase derivative contributes at most another \(Y^{-\sigma-1}/(5k)\).

The integrated Fourier series is therefore absolutely summable with weights \(k^{-2}\). Using \(\sum k^{-2}<2\), \(\pi>3\), and \(|s|/Y\le1/2\),
\[
\left|s\int_Y^\infty\psi(x)x^{-s-1}dx\right|
\le\frac25\frac{|s|}{Y}Y^{-\sigma}
\le\frac15Y^{-\sigma}.
\]
Together with the half-endpoint term this is less than \(Y^{-\sigma}\), so the stated constant 2 is conservative. QED.

### 4.2 A zero forces a large product defect

For \(0<\sigma<1\),
\[
|G_Y(\sigma+it)|\le Y^{1-\sigma}H_Y.
\]
At a hypothetical zero \(\rho=\beta+iT\), \(T\ne0\), satisfying the hypotheses of (E),
\[
R_Y(\rho)+1=G_Y(\rho)B_Y(\rho),
\]
and consequently
\[
|R_Y(\rho)+1|
\le H_Y\left[
\frac{Y^{2-2\beta}}{|T|}
+2Y^{1-2\beta}\right].
\tag{Z}
\]
We used \(|\rho-1|\ge|T|\), retaining rather than dropping the pole contribution.

For a fixed \(\sigma_0>1/2\), let \(Y\) be comparable with \(T\) and large enough for (E), for example \(Y=\lceil4(T+2)\rceil\). The right side of (Z) is
\[
O_{\sigma_0}\!\left((1+\log T)T^{1-2\sigma_0}\right)
\]
uniformly for \(\beta\in[\sigma_0,1)\). It eventually falls below \(1/2\), so every such zero forces
\[
|R_Y(\rho)|\ge1/2.
\]
This conclusion is independent of the imported \(7/8\) theorem.

For a whole dyadic height interval \(T\le\Im\rho\le2T\), one may instead use the common integer \(Y=\lceil8(T+2)\rceil\); the same uniform conclusion holds for sufficiently large \(T\).

## 5. A local energy threshold, and why the proved mean bound gives density rather than exclusion

Put
\[
\Omega=2\log Y,\qquad h=\Omega^{-1},
\]
and for a fixed vertical line define
\[
\mathcal E_Y(\sigma;T)
=\int_{T-h}^{T+h}
\left(|R_Y(\sigma+it)|^2
+\Omega^{-2}|\partial_tR_Y(\sigma+it)|^2\right)dt.
\]

For any continuously differentiable \(f\) on this interval, there is a point \(u\) with \(|f(u)|^2\) at most its average. The fundamental theorem of calculus then gives
\[
|f(T)|^2\le\frac{\Omega}{2}\int|f|^2
+2\left(\int|f|^2\int|f'|^2\right)^{1/2}
\le\frac{3\Omega}{2}
\int\left(|f|^2+\Omega^{-2}|f'|^2\right).
\]
Therefore a zero meeting \(|R_Y(\rho)|\ge1/2\) must satisfy
\[
\boxed{\quad
\mathcal E_Y(\beta;T)\ge\frac1{6\Omega}.
\quad}
\tag{P}
\]

This is a local peak lower bound for a specifically defined energy. It does not rely on a conjectural derivative estimate.

The moment estimates prove, on any interval of length \(H\),
\[
\int\left(|R_Y|^2+\Omega^{-2}|\partial_tR_Y|^2\right)
\le2B_\sigma(Y,H).
\]
For \(Y\asymp T\) and \(H\asymp T\), this is
\[
O_\sigma\bigl((1+\log T)^3T^{4-4\sigma}\bigr).
\]
At \(7/8\) it is of order \(T^{1/2}\) times logarithms. This is much larger than the local threshold \(1/(6\Omega)\asymp1/\log T\). Hence the proved estimate allows isolated zero-sized peaks.

For example, on a fixed vertical line, if \(J\) zero-sized points in the interval have pairwise separated ordinates by at least \(2h\), their peak intervals are disjoint and (P) gives
\[
J\le12\Omega B_\sigma(Y,H+2h).
\]
More generally this is a bound for separated large values, whether or not the points are zeros.

One can allow varying real parts \(\beta\in[\sigma_0,1]\) at the price of one further logarithmic factor. Apply the same average-point argument in the \(\sigma\) variable:
\[
\sup_{\sigma_0\le\sigma\le1}|R_Y(\sigma+it)|^2
\le\frac1{1-\sigma_0}\int_{\sigma_0}^1|R_Y|^2d\sigma
+2\int_{\sigma_0}^1|R_Y\,\partial_\sigma R_Y|d\sigma.
\]
The dyadic proof of (JM-r), with coefficient weights bounded using \(\sigma_0\), is uniform for these \(\sigma\). Since \(\partial_\sigma\) and \(\partial_t\) multiply coefficients by logarithms of the same magnitude,
\[
\int_I\sup_{\sigma_0\le\sigma\le1}
\left(|R_Y|^2+\Omega^{-2}|\partial_tR_Y|^2\right)dt
\le2(1+2(1-\sigma_0)\Omega)B_{\sigma_0}(Y,|I|).
\]
Thus the number of pairwise \(2h\)-separated zero-sized ordinates anywhere in that strip is at most
\[
12\Omega(1+2(1-\sigma_0)\Omega)
B_{\sigma_0}(Y,H+2h).
\]
This is an elementary density/localization consequence. Counting all multiplicities or arbitrarily clustered zeros would require an additional standard zero-counting input; no new record is asserted.

## 6. The exact remaining off-diagonal functional

Let \(a_n=e_Y(n)n^{-\sigma}\) for \(Y<n\le Y^2\), and let
\(\delta_{mn}=\log(n/m)\). Exact integration gives
\[
\mathcal E_Y(\sigma;T)=\mathcal D_Y(\sigma)+\mathcal O_Y(\sigma;T),
\]
where
\[
\mathcal D_Y(\sigma)=2h\sum_n a_n^2
\left(1+\frac{(\log n)^2}{\Omega^2}\right)
\]
and
\[
\boxed{
\mathcal O_Y(\sigma;T)=
4\sum_{Y<m<n\le Y^2}a_ma_n
\left(1+\frac{\log m\log n}{\Omega^2}\right)
\cos(T\delta_{mn})
\frac{\sin(h\delta_{mn})}{\delta_{mn}}.
}
\tag{O}
\]
Every product collision has already been combined into \(e_Y(n)\). The derivative cross term has the displayed positive logarithm product; there is no missing factor of two.

The diagonal is small for any fixed \(\sigma>1/2\). Summing the same decreasing dyadic coefficient bounds gives
\[
\sum_n a_n^2
\le\frac{2L_Y^3Y^{1-2\sigma}}{1-2^{1-2\sigma}},
\]
and therefore
\[
\mathcal D_Y(\sigma)\le
\frac{8hL_Y^3Y^{1-2\sigma}}{1-2^{1-2\sigma}}
=o_\sigma(\Omega^{-1}).
\]
Uniformity holds for \(\sigma\ge\sigma_0>1/2\).

For all sufficiently large \(Y\), the diagonal is at most \(1/(12\Omega)\). Hence, under the zero-detection size condition (Z), a sufficient one-sided estimate to exclude a zero at height \(T\) throughout a real-part interval is
\[
\mathcal O_Y(\sigma;T)<1/(12\Omega)
\]
for every \(\sigma\) in that interval, with the same \(Y\) and all endpoint hypotheses retained. With strict inequalities, the sum would be below the zero threshold (P).

This is the **actual native mixed inverse/plain off-diagonal** whose additional height cancellation is needed. The factors \(\cos(T\log(n/m))\) expose where height enters. The center-uniform estimate (JM) replaces this structure by a worst-case separation bound and supplies no decay as \(T\to\infty\).

The off-diagonal is not claimed small here. It is quadratic in the Möbius coefficients after opening \(e_Y(m)e_Y(n)\), with all cofactor restrictions included. This is more specific than an unspecified joint-moment hypothesis and avoids the four inverse-prefix factors of a squared Newton output. Whether its arithmetic structure permits a useful new support contraction remains open.

### 6.1 The diagonal and the zero adapter do reach a shrinking boundary

Here is a uniform component consequence tailored to the proposed height-dependent boundary. Fix \(c>2\), take \(Y\asymp T\) as above, and set
\[
\delta_Y=c\frac{\log\log Y}{\log Y},\qquad
\sigma_0(Y)=\frac12+\delta_Y.
\]
For sufficiently large \(Y\), \(0<\delta_Y\le1/2\). The elementary inequality \(1-e^{-u}\ge u/2\), \(0\le u\le1\), gives
\[
1-2^{-2\delta_Y}\ge\delta_Y\log2.
\]
Also \(L_Y\le4\log Y\) for \(Y\ge3\). Uniformly for
\(\sigma\ge\sigma_0(Y)\), the diagonal estimate therefore implies
\[
\boxed{\quad
\Omega\mathcal D_Y(\sigma)
\le\frac{512}{c\log2}
\frac{(\log Y)^{4-2c}}{\log\log Y}\longrightarrow0.
\quad}
\]
The zero-detection error in (Z) is, on the same range,
\[
O_c\bigl((\log Y)^{1-2c}\bigr)\longrightarrow0.
\]
Thus neither the reciprocal pole term, the truncation remainder nor the diagonal prevents using this detector as close as
\(1/2+c\log\log T/\log T\). These two estimates are actual proved components, uniform in the stated shrinking strip.

The missing off-diagonal estimate remains decisive. The present mean-value majorant has dominant power \(T^{2-4\delta_Y}\), which is of order \(T^2\) times inverse powers of \(\log T\), before its other logarithmic factors. It is far larger than the required local threshold \(1/\log T\). We have therefore **not** proved a zero-free boundary of this shape. The calculation identifies exactly which components already tolerate the requested narrowing and which do not.

## 7. What this changes, and what it does not

The old source-only phase comparison had a genuine cap defect and height-dependent transport factors. The coherent family now has an exact twisted Newton identity and an all-height bounded detail error. The cost is a changed, explicitly written harmonic kernel and a necessary treatment of the reciprocal constant.

Separately, a joint inverse/plain quantity can be estimated **after** exact native divisor cancellation. This gives a full mixed mean-square theorem rather than a request to prove one. Its local connection to an actual zeta zero is now explicit, including the pole term, the profile scale, the derivative energy and a numerical threshold.

Neither result lowers \(7/8\). The genuinely unresolved step is to exploit the height oscillation and arithmetic cofactor allocation inside (O), or to prove a stronger family estimate whose principal extraction pays less. A valid improvement must beat the local threshold at every target height, not merely make the density of potentially bad heights small.

## 8. Validation and attribution

The algebraic checker uses exact integers, Fractions and Gaussian-rational unitary completely multiplicative characters. It verifies:

- the original and coherently twisted Newton coefficients through each declared strict square endpoint;
- exact product-defect support and the boundary/collar identities;
- the explicit twisted block antiderivative;
- the full complex variance identity and the cubic-mesh \(5/6\) budget for the declared finite cases.

Those finite checks do not prove the universal analytic statements. The proofs above do; (MV) is the explicitly cited existing analytic input. The phases used by the checker are algebraic structural controls, not numerical evaluations of \(n^{-it}\) at a physical height.

The executed ordinary and optimized checker runs each completed 29,785 explicit predicates. Native reconstruction and complete compression panels use \(Y=1,2,3,5,7,15,31\), with largest strict endpoint 1023. Product-defect controls cover every integer \(1\le Y\le31\). No inherited campaign or physical-height zeta evaluation is represented as having been replayed.

The convolution automorphism, Möbius inversion, Euler summation, periodic Fourier expansion, Dirichlet-polynomial mean values and Sobolev estimates are classical tools. No external novelty claim is made. The contribution of this note is the exact coherent native-height assembly, its unchanged compression cost, and the complete joint-defect/zero-peak/off-diagonal interface with all source and scale costs retained.
