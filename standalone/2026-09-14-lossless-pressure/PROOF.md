# Lossless local-pressure transfer by separating close pairs

**Status (14 September 2026): proposed analytic theorem and arithmetic checks; independent review pending. No RH proof.**

The new result is a dimension-uniform transfer from local Fourier-kernel pressure to the clipped Gram defect. Its numerical corollaries use explicitly identified, previously published universal six-gap inequalities. Those large interval searches were **not rerun** in this contribution. The new finite arithmetic was reconstructed with Python's standard library and exact rationals. The mathematical argument, its arithmetic implementation, and the inherited analytic and computational inputs remain subject to independent review.

## 1. Target and contribution

Let

\[
\Phi(t)=\begin{cases}(t-1)^2,&0\le t\le2,\\2t-3,&t\ge2,\end{cases}
\qquad \Delta(G)=\operatorname{tr}\Phi(G).
\]

For a positive Fourier probability kernel \(K\), put
\(G_X=(K(x_i-x_j))_{i,j=1}^m\) and
\(E(X)=2\sum_{i<j}|K(x_i-x_j)|^2\).
The known stability-enhanced multiplicity argument retains \(\Delta(G)\), not \(E(X)\). In general these differ: the three-by-three all-ones Gram has \(E=6\) but \(\Delta=5\).

Existing seven-point pressure arguments bound \(E\) and then lose part of that bound by treating the Gram as a general positive matrix. This contribution instead partitions the actual Fourier Gram into close pairs and a separated remainder. The pairs pay for their removal. A compact-Fourier-support majorant keeps the remainder's spectrum strictly below 2. No clipping loss remains in the resulting pressure inequality.

For the source window and case-J pressure in [G], the proposed corollary is

\[
\boxed{\liminf_{T\to\infty}\frac{N_{\rm sc}(T)}{N(T)}\ge
\frac{104405554524189}{155021134296875}
=0.6734923918453979711624\ldots.} \tag{1}
\]

Here \(N(T)\) counts all nontrivial zeros with multiplicity at positive heights up to \(T\), and \(N_{\rm sc}(T)\) counts the simple critical-line zeros. Equation (1) uses the unconditional fixed-function pair-correlation theorem [L, Lemma 3.1] and the imported complete local inequality [G, Proposition 2.1, case J]. It assumes neither RH nor a conjectural zero-density statement. Its dependence on the unreplayed local certificate is explicit, not removed by our arithmetic checks.

The new ingredients are Sections 2-4 and their direct smoothing-compatible use. The clipped rank inequality, Fourier majorization method, pinching, and arithmetic second moment are not claimed as new individually. The source window and pressure coefficients belong to [G]. Related pair-selection ideas appear in [S]. No exhaustive priority claim is made.

## 2. General separation-or-pair lemma

**Theorem 2.1.** Suppose \(K\) is the Fourier transform of an even probability density, and for some \(h\ge1\), nonnegative coefficients \(a_{ij},b_r\), and \(\epsilon>0\),

\[
\sum_{r=0}^{h-1}b_rg_r+
\sum_{0\le i<j\le h}a_{ij}|K(g_i+\cdots+g_{j-1})|^2
\ge\epsilon \quad(g_r\ge0), \tag{2}
\]

with span capacities

\[
\sum_{j-i=\ell}a_{ij}\le2\quad(1\le\ell\le h),
\qquad B=\sum_rb_r.
\]

Assume also that for some \(d>0\):

1. every finite \(d\)-separated set has \(\|G_X\|_{\rm op}\le2\);
2. \(|K(x)|^2\ge\epsilon\) for \(|x|<d\).

Then for every ordered finite multiset \(X\) of size \(m\),

\[
\boxed{\Delta(G_X)+B\operatorname{span}(X)\ge\epsilon(m-h).} \tag{3}
\]

Define the span of zero or one point to be zero. The theorem includes repeated points and all sizes.

**Proof.** Summing (2) over the consecutive \((h+1)\)-point windows of any \(r\)-point list gives

\[
E(X)+B\operatorname{span}(X)\ge\epsilon(r-h). \tag{4}
\]

A pair of index separation \(\ell\) receives at most its span capacity 2, and a gap at most the sum \(B\) of all its possible positional coefficients. All omitted terms are nonnegative. For \(r\le h\), (4) is automatic.

Scan the points left to right. When the next two points are less than \(d\) apart, remove them as a pair; otherwise retain the first and continue. The retained list is \(d\)-separated: after retaining a point, every later retained point is at least as far away as its original immediate successor. All removed pairs are disjoint. Write \(r\) for the retained count and \(p\) for the pair count, so \(m=r+2p\).

Convex trace pinching gives

\[
\Delta(G_X)\ge\Delta(G_{\rm retained})+
\sum_{\rm pairs}\Delta(G_{\rm pair}). \tag{5}
\]

For completeness, take an orthonormal eigenbasis in each principal block. Scalar Jensen applied to the spectral resolution of the full matrix gives
\(\Phi(\langle u,Gu\rangle)\le\langle u,\Phi(G)u\rangle\); summing proves (5). Operator convexity is not asserted or needed.

All eigenvalues of the retained Gram lie in \([0,2]\), so
\(\Delta(G_{\rm retained})=\operatorname{tr}(G_{\rm retained}-I)^2=E(\mathrm{retained})\).
A pair Gram has eigenvalues \(1\pm|K(x)|\), both in \([0,2]\), and hence defect \(2|K(x)|^2\ge2\epsilon\). Apply (4) to the retained list and use its span no larger than the original span. The result is \(\epsilon(r-h)+2p\epsilon=\epsilon(m-h)\). QED.

The coefficient 2 in the pair payment and the full sum \(B\) in the span payment are mandatory. The theorem does not assert \(\Delta(G)=E(G)\) for the original unpartitioned Gram.

## 3. A uniform geometric certificate for the actual windows

Let \(I=[-1/2,1/2]\), \(a=1/\sqrt2\), and

\[
v_c(t)=\cos(\sqrt2t)+\sum_{j=1}^{24}c_j\cos(2\pi jt),\quad
A=\int_Iv_c(t)\,dt=\frac{\sin a}{a},\quad
f_c=A^{-1}v_c\mathbf1_I,\quad K_c=\widehat f_c.
\]

Use Fourier convention \(\widehat f(x)=\int f(t)e^{-2\pi ixt}dt\). All 24 coefficients, the case-J pair weights, and the pressure coefficients are retained exactly in `inputs.json`, transcribed from [G, Appendix A]. Their absolute sum is

\[
S_*:=\sum|c_j|=\frac{85368367}{1250000000}=0.0682946936.
\]

All results of this section hold for any coefficients with absolute sum at most \(S_*\), including the unperturbed Montgomery-Taylor window. Positivity follows from \(v_c\ge3/4-S_*>0\). Also \(A\ge11/12\).

### 3.1 Complete sinc-square majorant

Put \(d=4/5\), \(C=29/20\). For all real \(t\),

\[
\boxed{v_c(t)\mathbf1_I(t)\le C\operatorname{sinc}^2(\pi d t).} \tag{6}
\]

Here \(\operatorname{sinc}x=\sin x/x\), with its removable value. To prove (6), take \(u=t^2\in[0,1/4]\), \(b=(88/35)^2\), and

\[
R(u)=1-bu/6+b^2u^2/120-b^3u^3/5040.
\]

Since \(\pi<22/7\), sinc is decreasing on the relevant interval, and its alternating Taylor remainder has the stated sign,
\(\operatorname{sinc}(\pi d t)\ge R(u)>0\).
The positivity follows already from \(R(u)\ge1-bu/6>0\), as its last two terms have nonnegative sum here. Also
\(\cos(\sqrt2t)\le1-u+u^2/6\).
It suffices to prove positivity on \([0,1/4]\) of the degree-six polynomial

\[
P(u)=\frac{29}{20}R(u)^2-(1-u+u^2/6)-S_*.
\]

In the degree-six Bernstein basis on that interval, its seven coefficients are respectively greater than

```
0.3817, 0.2960, 0.2204, 0.1539, 0.0957, 0.0451, 0.0013.
```

The exact minimum is

\[
\frac{299693708900577804719593}{214594019143628906250000000}>\frac1{1000}.
\]

These are exact rational comparisons reconstructed by `verify.py`, not a sampled positivity test. The Bernstein basis functions are nonnegative and sum to one. Outside \(I\) the left side of (6) is zero and the right side nonnegative. This proves the complete majorant.

Its Fourier transform is

\[
\widehat{C\operatorname{sinc}^2(\pi d\,\cdot)}(x)
=\frac C d(1-|x|/d)_+.
\]

Therefore, for any finite \(d\)-separated points and complex coefficients \(z_i\),

\[
\begin{aligned}
z^*G_Xz
&=\frac1A\int_Iv_c(t)\left|\sum_i z_i e^{2\pi i x_it}\right|^2dt\\
&\le\frac1A\int_{\mathbb R}C\operatorname{sinc}^2(\pi dt)
\left|\sum_i z_i e^{2\pi i x_it}\right|^2dt\\
&=\frac C{dA}\sum_i|z_i|^2
\le\frac{87}{44}\sum_i|z_i|^2<2\sum_i|z_i|^2. \tag{7}
\end{aligned}
\]

The off-diagonal terms vanish exactly by Fourier support, including separation exactly \(d\). This argument is independent of the number and locations of the points.

### 3.2 Close pairs have ample positive defect

For the unperturbed normalized kernel \(K_0\), Chebyshev's integral inequality for the two decreasing functions \(\cos(\sqrt2t)\) and \(\cos(2\pi xt)\) on \([0,1/2]\) gives

\[
K_0(x)\ge\operatorname{sinc}(\pi x),\qquad0\le x\le4/5.
\]

Chebyshev's covariance inequality does not require the second cosine to stay nonnegative. Monotonicity of sinc and \(\sin u\ge u-u^3/6\), with \(\pi^2<10\), give

\[
\operatorname{sinc}(4\pi/5)=\frac14\frac{\sin(\pi/5)}{\pi/5}
\ge\frac14(1-\pi^2/150)>\frac7{30}.
\]

Since \(|K_c-K_0|\le S_*/A\le12S_*/11\),

\[
\boxed{K_c(x)\ge\frac7{30}-\frac{12S_*}{11}
=\frac{1637934697}{10312500000}>\frac3{20}
\quad(|x|\le4/5).} \tag{8}
\]

Thus a close pair has defect at least \(9/200\), enough to pay for two points whenever \(\epsilon\le9/400\). Both imported pressures used below are far below that budget.

## 4. The imported local inputs and the new all-size consequences

### 4.1 Existing repository input

The main-branch reviewer supplement [R, S01-S02] reconstructs the complete inequality (2) with \(h=6\), \(b_r=1/3000\), \(a_{ij}=2/(7-(j-i))\), \(\epsilon=19/5000\), and the unperturbed window. The source reports a complete independent 713,315-node interval exhaustion. We read the proof and its stated arithmetic contract; we did **not** rerun that search.

Theorem 2.1 gives, for every size,

\[
\Delta(G_X)+\frac1{500}\operatorname{span}(X)
\ge\frac{19}{5000}(m-6). \tag{9}
\]

There is no 269/280-block cap or generic spectral-envelope loss in (9).

### 4.2 Newer externally published input

For the same perturbed window fixed in Section 3, [G, Proposition 2.1, case J] reports the complete inequality (2) with

\[
\epsilon=\frac{15729481}{2000000000}=0.0078647405,
\quad B=\frac{1970462189}{500000000000}=0.003940924378.
\]

Its six positional pressure coefficients are symmetric and sum to \(B\). The 21 nonnegative pair coefficients have each of their six span capacities exactly 2; `verify.py` checks this from the explicit input snapshot. Checking these capacities does **not** replay the universal inequality.

Theorem 2.1 therefore gives

\[
\boxed{\Delta(G_X)+B\operatorname{span}(X)\ge\epsilon(m-6)
\quad\hbox{for every finite ordered }X.} \tag{10}
\]

Only case J is needed: neither the eight auxiliary pressures nor the 159-vertex polyhedral calculation in [G] enters this deduction. The input is a previously published finite certificate, not a new conjecture equivalent to the desired conclusion. Nevertheless it must be validated independently before treating the full numerical corollary as independently checked. Attempts to access the cited Zenodo record and API in this session failed; the author's public full manuscript was read instead.

## 5. Smoothing without a growing-block or growing-test assumption

The endpoint-positive density \(f_c\) is not a smooth compactly supported test function. Choose real even smooth cutoffs \(0\le\chi_\tau\le1\), compactly supported inside \(I\), approaching 1 on its interior. Let

\[
m_\tau=\int\chi_\tau^2 f_c,\quad
f_\tau=\chi_\tau^2 f_c/m_\tau=\eta_\tau^2,
\quad K_\tau=\widehat f_\tau,
\quad e_\tau=\|K_\tau-K_c\|_{L^\infty(\mathbb R)}.
\]

Then \(m_\tau\to1\), \(f_\tau\to f_c\) in \(L^1\cap L^2\), and \(e_\tau\to0\). One may bound \(e_\tau\le2(1-m_\tau)\). The separated Gram norm is at most \(87/(44m_\tau)<2\) once \(m_\tau>87/88\). On close pairs, \(K_\tau\ge3/20-e_\tau\).

For real arguments both kernels have modulus at most 1. Thus each squared kernel changes by at most \(2e_\tau\). The total pair coefficient mass in (2) is 12, so the **complete** local inequality holds for \(K_\tau\), on every nonnegative gap vector, with

\[
\epsilon_\tau=\epsilon-24e_\tau.
\]

For sufficiently small fixed \(\tau\), this is positive and below \((3/20-e_\tau)^2\). Theorem 2.1 applies directly to the smoothed kernel, giving

\[
\Delta(G_{X,\tau})+B\operatorname{span}(X)
\ge\epsilon_\tau(|X|-6) \tag{11}
\]

for all finite sizes. This is a uniform perturbation on **real** kernel values, not on complex zero-side sums. The latter use the fixed-function theorem below. No unbounded-gap term is discarded, no simultaneous \(T\)-dependent smoothing is used, and no growing matrix-size approximation is assumed.

## 6. Arithmetic transfer, including the retained defect

### 6.1 The imported arithmetic theorem

For every fixed real even \(\eta\in C_c^\infty((-1/2,1/2))\) with \(\int\eta^2=1\), let \(f=\eta^2\), \(K=\widehat f\), and

\[
z_\rho=-i(\rho-1/2)\frac{\log T}{2\pi},\qquad
\mathcal S_f(T)=\sum_{0<\gamma,\gamma'\le T}K(z_\rho-z_{\rho'})^2.
\]

The unconditional formula [L, Lemma 3.1 and its Section 3 unweighting] gives

\[
\mathcal S_f(T)=(\mathcal C(f)+o_f(1))N(T),\quad
\mathcal C(f)=\int f^2+\iint |t-u|f(t)f(u)\,dt\,du. \tag{12}
\]

All zeros are included with multiplicity. The square in this formula is an algebraic square, not an absolute square of an individual complex kernel value.

To record the fixed-test boundary explicitly: apply the weighted pair-correlation formula separately to \(Q=f*f\) and \(Q''\). Since \(\widehat{Q''}(z)=-4\pi^2z^2K(z)^2\), their linear combination \(Q-Q''/(4\log^2T)\) cancels the rational weight exactly. Both applications are to fixed functions, and the second contribution is divided by \(\log^2T\). This is the published unweighting argument, not an assumption of uniformity for arbitrary varying tests. The underlying pair-correlation theorem and Riemann-von Mangoldt asymptotic are external analytic inputs, not proved by our checker.

### 6.2 Exact finite linear algebra

Here is a reconstruction of the retained-defect inequality used in [R,G,S]. Work in the real Hilbert space

\[
\mathcal H=\{h\in L^2(I;\mathbb C):h(-t)=\overline{h(t)}\}.
\]

For real \(x\), \(v_x(t)=\eta(t)e^{2\pi ixt}\) is a unit vector. Extend bilinearly to complex \(z\); the bilinear inner product is
\(\mathcal B(v_z,v_w)=K(z-w)\). A nonreal conjugate pair has \(v_z=g+ih\), \(v_{\bar z}=g-ih\), where \(g,h\in\mathcal H\). Its contribution of multiplicity \(q\) is \(2q(g\otimes g-h\otimes h)\), of trace \(2q\) and positive index at most one. A real point of multiplicity \(q\) contributes \(qv_x\otimes v_x\).

Let \(A_0=P+Q\) be the resulting finite-rank real self-adjoint operator, with \(P\) consisting of the \(s=N_{\rm sc}(T)\) simple real atoms. Then

\[
\operatorname{tr}A_0=N(T),\quad
\|A_0\|_{\rm HS}^2=\mathcal S_f(T),\quad
n_+(Q)\le(N(T)-s)/2. \tag{13}
\]

These identities follow by expansion and conjugation pairing, without RH. Restrict to a finite-dimensional span containing all these vectors. Let \(G\) be the \(s\)-column unit Gram of \(P\).

Write \(Q=Q_+-Q_-\). Dropping \(2\operatorname{tr}(PQ_+)\ge0\), using \(Q_+Q_-=0\), and then the trace rearrangement inequality reduces the negative part to scalar inequalities. For \(p,n\ge0\),

\[
(p-n)^2+4n\ge2p+\Phi(p)-1.
\]

This follows by minimizing at \(n=(p-2)_+\). Also each positive eigenvalue of \(Q\) satisfies \(q^2\ge4q-4\). Since \(\Phi(0)-1=0\), the nonzero spectra of \(VV^*\) and \(V^*V\) give

\[
\|A_0\|_{\rm HS}^2
\ge4\operatorname{tr}A_0-3s-4n_+(Q)+\Delta(G)
\ge2N(T)-s+\Delta(G).
\]

Consequently

\[
\boxed{s\ge2N(T)-\mathcal S_f(T)+\Delta(G).} \tag{14}
\]

The classical inertia/trace mechanism and its clipped refinement are credited; this section checks the exact interface rather than introduces a new one.

### 6.3 Complete limit passage

Use (11) for the actual simple real coordinates, which lie in an interval of length \(L_T=T\log T/(2\pi)\). Equations (12)-(14) give, for every sufficiently small **fixed** \(\tau\),

\[
(1-\epsilon_\tau)s
\ge(2-\mathcal C(f_\tau)+o_\tau(1))N(T)-BL_T-6\epsilon_\tau.
\]

First let \(T\to\infty\), using \(L_T/N(T)\to1\). Then let \(\tau\to0\). The quadratic functional \(\mathcal C\) is continuous under the stated \(L^1\cap L^2\) convergence on the common compact support. Thus

\[
\boxed{\liminf\frac{N_{\rm sc}(T)}{N(T)}
\ge\frac{2-\mathcal C(f_c)-B}{1-\epsilon}.} \tag{15}
\]

This is cumulative in height. It contains no unresolved RH-strength sign or vanishing-defect assumption.

## 7. Exact constants and comparison

Orthogonality of the integer cosine modes and \((I+D)\cos(\sqrt2t)=\mathrm{constant}\), where \((Dq)(t)=\int_I|t-u|q(u)du\), give

\[
H_c:=2-\mathcal C(f_c)=\frac32-\frac{\cos a}{A}
-\frac1{A^2}\sum_{j=1}^{24}\frac{c_j^2}{2}
\left(1-\frac1{2\pi^2j^2}\right). \tag{16}
\]

Indeed \((I+D)\cos(2\pi jt)=(1-1/(2\pi^2j^2))\cos(2\pi jt)+\mathrm{constant}\), so all cross terms vanish. This source-specific formula also appears in [G]; it is not new here.

The fresh exact-rational evaluation gives

\[
0.67213647333280977542285707062155122
<H_c<
0.67213647333280977542285707062155123.
\]

The calculation uses Machin's formula with alternating rational arctangent sums and adjacent alternating sums for \(\cos a\) and \(A=\sin a/a\). There is no floating special-function input. In particular
\(H_c>210042647916503/312500000000000\). Inserting this lower bound and case J in (15) gives exactly (1).

The draft [G] displays \(r_*=1757544638415046796829717/2609661779050000000000000\). The improvement over this **specific unreviewed draft**, not an asserted world record, is enclosed by

\[
0.00001636804631048196339706595444482
<(1)\text{'s rational}-r_*<
0.00001636804631048196339706595444483.
\]

In percentage points the gain is about 0.001636804631. No claim is made to have located every current result or independently reviewed the entire source literature.

Using only the older repository pressure (9) instead gives

\[
\frac{H_{\rm MT}-1/500}{1-19/5000}
=0.6730583253156109674105\ldots,
\quad H_{\rm MT}=\frac32-\frac1{\sqrt2}\cot(1/\sqrt2).
\]

This improves the repository's extracted 280-block value \(0.673009652279\ldots\) without changing its local inequality. The newer window gives a further improvement. Neither calculation estimates the distance to proving RH.

## 8. Validation and limitations

Run `python -I verify.py --check results.json` and `python -I test_verify.py`; both also run with `-O`. Exact checks cover all seven Bernstein coefficients, the strict separated-norm budget, the close-pair budget, source span capacities, the window baseline, both comparison constants, and artifact input identity. The tests include an alternative series truncation, failed majorants, altered capacities, complete finite partition implementation checks, the arbitrary-Gram clipping counterexample, and a rejected changed result record.

These checks do not prove Fourier analysis, the written pinching and smoothing lemmas, the arithmetic input, or the inherited six-dimensional pressure statement. In particular a `PASS` must never be described as a fresh replay of [G]'s 9,412,168-box case-J search, nor of [R]'s seven-point search. There is no Lean build or independent review recorded here.

The step beyond the inspected source arguments is a uniform removal of their spectral-relaxation loss. It establishes a proposed quantitative corollary from finite local inputs, rather than replacing RH by an equivalent condition. It is still a proportion theorem: even a density-one result would not exclude finitely or sparsely many off-line zeros. This packet does not solve that separate problem.

## References and reading boundaries

- **[R]** GettysburgResearch/riemann, main `f99d9e3908dde4865377c75d9ca051c1f545bf4f`, `reviews/A/supplement/REPORT.md`, Sections S01-S02; and PR #726 source `e8e6d85221a9a85fb2a5f82a1807802f89b06b7b`, `claims/lemmas/L-105560-defect-retaining-multiplicity-bridge.md`. Actual statements, proofs, capacities, and analytic adapter read; original searches not rerun.
- **[G]** Jonas J. Gebendorfer, *An expanded window and joint position pressures for simple critical-line zeros*, research draft v0.3, 7 September 2026, DOI **10.5281/zenodo.22643957**. Author-uploaded full text read: Proposition 2.1, Appendix A, Sections 2-6. https://www.researchgate.net/publication/414047851_An_expanded_window_and_joint_position_pressures_for_simple_critical-line_zeros . This is an internally checked research draft, not an independently reviewed record. Its 24 coefficients and case-J constants are attributed imports.
- **[L]** Youness Lamzouri, *A new proof that more than 2/3 of the zeros of the Riemann zeta function are simple and on the critical line*, arXiv:2609.02882, Lemma 3.1 and Section 3 fixed-function unweighting. Primary PDF and displayed formulas inspected. https://arxiv.org/abs/2609.02882 . The underlying unconditional pair-correlation theorem is Baluyot-Goldston-Suriajaya-Turnage-Butterbaugh, Acta Arith. 214 (2024), 357-376; we use its statement as imported in [L], not a fresh full audit of that paper.
- **[AF]** Levent Alpoge and Romain Furman, *More than two thirds of the zeros of the Riemann zeta function are simple and on the critical line*, arXiv:2608.13637v2. Sections 1-3, source window, Gram construction, and Poisson identity inspected. https://arxiv.org/html/2608.13637v2 . Their paper credits the argument to Claude.
- **[S]** Yuhang Shi, *A Schur-Jensen gain in the critical-line zero problem*, DOI **10.5281/zenodo.21903013**. Pair-selection precedent and clipped-refinement attribution read through [G] and its author abstract; not independently audited in full.

Prior continuation PR #885 was confirmed at head `26e54e14e8648dbc2cde6bf17058ca508e42dc70`; its uploaded-packet description was read, not its entire analytic argument re-audited. Thirty recently updated PR descriptions and selected main-source searches informed this scope. The seven independent thread reports mentioned in the user's critique were not available as standalone reports and were not falsely claimed as replicated.
