# An exact ordinary-zeta bridge and sparse capture without full moments

**Status:** proposed proved arithmetic identities and sampling/capture theorem. The arithmetic observation hypothesis remains open. No new zero-free constant or RH conclusion is claimed unconditionally.

**Scope:** one fixed test, the literal zero-extended Eisenstein sextic family with trivial coefficient character, an explicit finite restoration of its deleted Euler factors, and the ordinary Riemann zeta target. The theorem below observes only the principal sixth-power orbit. It requires no full moment bound and asserts no zero exclusion for the general Hecke-twist family.

**Main output:** a fixed causal character filter converts the principal Eisenstein Möbius row into the ordinary integer Möbius source exactly. Its sixth-power replication identity survives. After a sufficiently rough but fixed set of excluded base primes is chosen, a positive fraction of small values at each point of a sparse scale grid forces the ordinary source to have the corresponding power bound, up to an arbitrarily small loss. The bounded bases may change completely from one sample to another; the other bases can have arbitrary amplitudes.

## 1. Sources, objects, and the narrowed target

The frozen repository baseline is PR #928, commit `ab98878279cd5614fe79bb94aa916e97c9ee50b4`. The exact local sources read for this construction are:

| Source at that commit | Interface used | SHA-256 |
| --- | --- | --- |
| `standalone/2026-10-10-sextic-critical-core/LOG_FREE_REPLICATED_SPIKES.md` | Exact exclusion recurrence and positive-density rough bases, Sections 1–3 | `b59978c1c5d3b5cb904c7f22d675a67bb71b2af512db9f0577e568a04565a86b` |
| `standalone/2026-10-10-signed-graph-and-joint-descent/sources/pr926/SAMPLED_MOMENT_CRITERION.md` | Fixed nonvanishing Mellin tests and all-derivative bound, Proposition 2.1 and Corollary 2.2 | `18bf2fdad438eb21ae3318eba7d42e9c03803b2dd1abc4d8f6448fb3b04499de` |

The reading of `PROGRAMMES.md`, `OPEN_CUTS.md`, and `research/integrated/CURRENT_RESULTS.md` was used to check the boundaries against the older integer Möbius, compact-wavelet, Mellin–Landau, causal Euler, and capture programmes. None of their open arithmetic premises is assumed here.

Let \(K=\mathbb Q(\sqrt{-3})\), and let \(S\) be the fixed finite bad-prime set of **prime ideals**. Use the inherited primary convention and put

\[
A_u(D;W)=\sum_{(\mathfrak n,S)=1}
\mu_K(\mathfrak n)\chi_{\mathfrak n}(u)
W(N\mathfrak n/D).
\tag{1.1}
\]

Thus the coefficient character \(\nu\) is fixed to be trivial. All nonunit zeros of the sextic symbol are retained. In particular \(\chi_{\mathfrak n}(1)=1\).

Write \(\chi_{-3}\) for the real primitive character modulo three:

\[
\chi_{-3}(m)=0,1,-1\quad\text{according as}\quad m\equiv0,1,2\pmod3.
\]

For a positive integer \(a\), let \(\mathsf S_aF(D)=F(D/a)\). Define the finite signed restoration operator

\[
\mathcal P_S=\prod_{\mathfrak p\in S}(I-\mathsf S_{N\mathfrak p}),
\tag{1.2}
\]

and the restored row family

\[
\boxed{
B_u(D;W)=\mathcal P_S
\left[\sum_{m\ge1}\chi_{-3}(m)A_u(D/m;W)\right].
}
\tag{1.3}
\]

Every sum in (1.3) is finite at each physical \(D\), since the test is supported in a compact subinterval of \((0,\infty)\). A split rational prime can give two distinct prime ideals with the same norm. Their two factors in (1.2) must both be retained; they are not identified as one factor.

The filter is fixed before the growing scale varies. No infinite absolute-summability claim for \(\sum_m|\chi_{-3}(m)|m^{-\alpha}\) is being made when \(\alpha\le1\).

## 2. Exact restoration of the integer Möbius source

### Theorem 2.1. The principal row is exactly ordinary Möbius

For every physical \(D>0\),

\[
\boxed{B_1(D;W)=\sum_{n\ge1}\mu(n)W(n/D).}
\tag{2.1}
\]

This holds as a finite coefficient identity for every fixed test for which the displayed sums are finite.

**Proof.** Initially for \(\Re s>1\), the norm Dirichlet series of the principal raw row is

\[
\sum_{(\mathfrak n,S)=1}\frac{\mu_K(\mathfrak n)}{(N\mathfrak n)^s}
=\frac{1}{\zeta_K(s)P_S(s)},
\qquad
P_S(s)=\prod_{\mathfrak p\in S}(1-(N\mathfrak p)^{-s}).
\tag{2.2}
\]

The scale filter in (1.3) multiplies this by \(P_S(s)L(s,\chi_{-3})\). The elementary Euler-factor identity

\[
\zeta_K(s)=\zeta(s)L(s,\chi_{-3})
\tag{2.3}
\]

therefore leaves \(1/\zeta(s)\). For completeness, at a split prime the product of the two ideal factors is \((1-p^{-s})^{-2}\); at an inert prime it is \((1-p^{-2s})^{-1}\); and at the ramified prime three it is \((1-3^{-s})^{-1}\). These are exactly the corresponding factors of the right side of (2.3). Absolute convergence in \(\Re s>1\) identifies the Dirichlet coefficients. Equivalently these are formal local power-series identities, with only finitely many factors involved in any coefficient. Pairing each coefficient with \(W(n/D)\) proves (2.1). \(\square\)

The finite restoration is essential. Omitting \(\mathcal P_S\) would give the ordinary Möbius source convolved with \(P_S(s)^{-1}\), not (2.1).

For the fixed universal test of Section 4, (2.1) gives

\[
\int_0^\infty B_1(D;W)D^{-s}\frac{dD}{D}
=\frac{\widehat W(s)}{\zeta(s)}
\qquad(\Re s>1).
\tag{2.4}
\]

The numerator is nonzero in \(\Re s>0\). Hence a bound \(B_1(D;W)=O(D^\beta)\), \(\beta>0\), excludes zeta zeros with real part greater than \(\beta\): the left side and its derivatives converge locally uniformly in that half-plane, and analytic continuation of (2.4) cannot have a reciprocal-zeta pole there.

This argument does not assert that the analogous filtered numerator is nonzero for every nonprincipal Hecke row. Such numerators can cancel zeros. Only the exact ordinary-zeta identity (2.4) is used.

## 3. The source-specific replica identity survives the bridge

### Proposition 3.1. Exact positive dilation recurrence on the principal orbit

For every ideal \(w\) prime to \(S\),

\[
\boxed{
B_{w^6}(D;W)
=\sum_{\operatorname{rad}(\mathfrak r)\mid w}
B_1(D/N\mathfrak r;W).
}
\tag{3.1}
\]

The ideal \(\mathfrak r\) need not be squarefree. Every ideal prime power with prime support in \(w\) is included, and equal norm values are counted with their actual ideal multiplicities. The sum is finite at each \(D\).

**Proof.** In (1.1), multiplication of the row by \(w^6\) inserts exactly the mask \((\mathfrak n,w)=1\). The inherited finite inverse-Euler identity, here with coefficient character one, is

\[
A_{w^6}(D;W)
=\sum_{\operatorname{rad}(\mathfrak r)\mid w}
A_1(D/N\mathfrak r;W).
\]

All operators on the right are scale dilations. They commute with the fixed finite restoration and the physical finite sum in (1.3). Reordering these finite sums proves (3.1). \(\square\)

The condition \((w,S)=1\) cannot be dropped from this formula with the displayed unrestricted inverse factors: a prime already absent from the original coefficient source supplies no new exclusion factor.

### Proposition 3.2. Almost all sufficiently rough bases have a small correction

Fix \(\alpha>0\) and \(0<\gamma\le1\). There is a fixed finite prime-ideal set \(Q\supseteq S\) such that, for

\[
\mathcal V_Q(Y)=\{w:(w,Q)=1,\ Y/2<Nw\le Y\},
\quad J_Q(Y)=|\mathcal V_Q(Y)|,
\]

at least \((1-\gamma/4)J_Q(Y)\) of these bases satisfy

\[
K_\alpha(w):=
\sum_{\substack{\mathfrak r\ne1\\\operatorname{rad}(\mathfrak r)\mid w}}
(N\mathfrak r)^{-\alpha}\le\frac12
\tag{3.2}
\]

for all sufficiently large \(Y\). Also \(J_Q(Y)\asymp_QY\).

**Proof.** The elementary ideal count and finite inclusion–exclusion give \(J_Q(Y)\sim\kappa_QY\), \(\kappa_Q>0\). The exact positive mean limit proved in the frozen replica source is

\[
\frac1{J_Q(Y)}\sum_{w\in\mathcal V_Q(Y)}K_\alpha(w)
\longrightarrow
\prod_{\mathfrak p\notin Q}
\left(1+\frac1{N\mathfrak p((N\mathfrak p)^\alpha-1)}\right)-1.
\tag{3.3}
\]

It follows by counting bases divisible by \(\operatorname{rad}(\mathfrak r)\) and dominated convergence. The dominating Euler product converges for every fixed \(\alpha>0\). Enlarge the **fixed** set \(Q\) so the right side is less than \(\gamma/16\). The mean is at most \(\gamma/8\) for large \(Y\). Markov's inequality bounds the fraction with \(K_\alpha>1/2\) by \(\gamma/4\). This proves the claim. No prime ideal theorem, growing-\(Q\) uniformity, or fixed-\(P_{61}\) extrapolation is used. \(\square\)

If \(\beta>\alpha\), the same bases satisfy \(K_\beta\le K_\alpha\). Consequently the set \(Q\) in this proposition can be fixed once for the entire conclusion with exponents \(\beta>\alpha\).

## 4. Quantitative regularity of the restored family

Use the fixed test \(W=W_{\mathscr L}\) of PR #926, where \(\mathscr L:\mathbb N\to[1,\infty)\) is nondecreasing, has bounded consecutive ratios, and

\[
\sum_{j\ge1}\frac1{j\mathscr L(j)}<\infty.
\tag{4.1}
\]

Its Mellin transform is nonzero in \(\Re s>0\), its support is a compact subinterval of \((1,2)\), and its logarithmic profile has the all-order derivative bound from the frozen source. In particular the original universal test \(W_*\) corresponds to \(\mathscr L(j)=j\).

### Lemma 4.1. Direct row-uniform derivative bound after filtering

There are fixed constants \(C,B\ge1\) such that, for every \(X\ge2\), every row \(u\ne0\), every integer \(m\ge1\), and \(0\le t\le\log2\),

\[
\boxed{
\left\|\frac{d^m}{dt^m}B_u(Xe^t;W)\right\|_\infty
\le C X\log(2X)B^{m+1}m!\,\mathscr L(m)^m.
}
\tag{4.2}
\]

**Proof.** Expand the finite operator \(\mathcal P_S\). Each resulting term has a fixed norm shift \(a\) and sign. The remaining pairs \((\mathfrak n,r)\), with \(r\) a positive integer, satisfy \(a r N\mathfrak n\le4X\). Their number is at most

\[
\sum_{r\le4X/a}O_K(X/(ar))
\ll_{K,S}X\log(2X).
\]

The same estimate covers nonempty bounded scales below one by the fixed support constants. Every arithmetic coefficient has modulus at most one before the fixed restoration is summed. Applying the profile derivative estimate to each pair gives (4.2). This is a direct count, not an invocation of an \(\ell^1\) bound for the subcritical character-dilation filter. \(\square\)

### Lemma 4.2. A high value forces many high samples in one common block

Let \(f\in C^m([0,\log2];\mathbb C)\). Take a uniform grid of spacing \(\Delta\), and any block of \(q\) consecutive nodes whose convex hull contains \(t\), where

\[
q=\lceil4m/\gamma\rceil.
\]

If at least \(\gamma q/2\) of these nodes have \(|f|\le T\), then

\[
|f(t)|
\le (C_1/\gamma)^mT
+\frac{(q\Delta)^m}{m!}\|f^{(m)}\|_\infty,
\tag{4.3}
\]

where \(C_1\) is an absolute constant. Thus a value exceeding the right side forces more than \((1-\gamma/2)q\) high nodes in this same block.

**Proof.** Let \(g\ge\gamma q/2\ge2m\) be the number of good nodes. Select every \(\lfloor g/m\rfloor\)-th good node until \(m\) have been chosen. Their separation is at least

\[
\lfloor g/m\rfloor\Delta
\ge\frac{\gamma q\Delta}{4m}.
\]

The Lagrange basis on their convex hull and on the whole block has absolute sum at most

\[
\frac{(8m/\gamma)^{m-1}}{(m-1)!}
\le(C_1/\gamma)^m.
\]

The divided-difference integral remainder has absolute value at most the second term of (4.3); its simplex has volume \(1/m!\). This also proves the bound for complex-valued \(f\), without a real mean-value-point assumption. \(\square\)

The block is chosen from the evaluation point, not from the row. Therefore the same block can be used simultaneously for every row having a high value there.

## 5. Sparse capture from a positive fraction of principal replicas

Fix \(\alpha>0\), \(h>0\), \(0<\gamma\le1\), and the corresponding fixed \(Q\) from Proposition 3.2. For every dyadic \(X=2^j\), choose

\[
D_{X,i}=X\exp(i\Delta_X),\qquad
\Delta_X=\frac{\log2}{N_X},\qquad0\le i\le N_X,
\tag{5.1}
\]

with

\[
\Delta_X\log X\,\mathscr L(\lceil\log X\rceil)\longrightarrow0.
\tag{5.2}
\]

Set \(Y_X=X^{h/6}\), and use one common base set \(\mathcal V_Q(Y_X)\) throughout this interval. Every observed row satisfies \(N(w^6)\le X^h\le D_{X,i}^h\). No moving row-entry endpoint is crossed inside an interpolation argument.

### Theorem 5.1. A fractional observation criterion for ordinary zeta

Suppose there is a fixed constant \(C_0\) such that, at every grid point of every sufficiently large dyadic interval,

\[
\boxed{
\#\left\{w\in\mathcal V_Q(Y_X):
|B_{w^6}(D_{X,i};W)|\le C_0D_{X,i}^{\alpha}\right\}
\ge\gamma J_Q(Y_X).
}
\tag{5.3}
\]

Then for every \(\varepsilon>0\),

\[
\boxed{B_1(D;W)\ll_\varepsilon D^{\alpha+\varepsilon}.}
\tag{5.4}
\]

Consequently \(\zeta(s)\) has no zeros with \(\Re s>\alpha\).

The good bases in (5.3) need not be the same at different nodes. There is no amplitude or moment hypothesis on the remaining bases. The theorem uses neither the imported inverse second moment nor a theta or reflected-Gauss bound.

**Proof.** Fix \(\beta>\alpha\), and suppose \(|B_1(D)|/D^\beta\) is unbounded. The function is continuous, locally bounded, and zero below a positive scale. Choose record scales \(D_j\to\infty\) with

\[
F_j=|B_1(D_j)|/D_j^\beta\longrightarrow\infty,
\qquad |B_1(x)|\le F_jx^\beta\quad(0<x\le D_j).
\tag{5.5}
\]

Let \(X\le D_j\le2X\) be its dyadic interval. By (3.1), every base with \(K_\alpha(w)\le1/2\) has

\[
|B_{w^6}(D_j)-B_1(D_j)|
\le F_jD_j^\beta K_\beta(w)
\le\tfrac12|B_1(D_j)|.
\tag{5.6}
\]

Thus at least \((1-\gamma/4)J_Q(Y_X)\) rows have absolute value at least \(F_jD_j^\beta/2\) at this one common scale.

Write \(L=\log X\) and

\[
r_X=\log\frac1{\Delta_X L\mathscr L(\lceil L\rceil)},
\qquad m_X=\left\lceil\frac{8L}{r_X}\right\rceil.
\tag{5.7}
\]

For large \(X\), \(r_X\to\infty\), \(1\le m_X\le\lceil L\rceil\), and \(m_X=o(L)\). Put \(q_X=\lceil4m_X/\gamma\rceil\). Condition (5.2) implies \(N_X/L\to\infty\), so a block of \(q_X\) consecutive nodes covering \(\log(D_j/X)\) exists, using the first or final block near the endpoints.

Monotonicity of \(\mathscr L\) and \(q_X\le5m_X/\gamma\) give, for large \(X\),

\[
Bq_X\Delta_X\mathscr L(m_X)\le e^{-r_X/2}.
\]

The remainder in Lemma 4.2, with the uniform estimate (4.2), is consequently at most

\[
CX\log(2X)B e^{-m_Xr_X/2}
\ll X^{-2}.
\tag{5.8}
\]

Also \((C_1/\gamma)^{m_X}=X^{o(1)}\). With sample threshold \(T=C_0(2X)^\alpha\), the right side of (4.3) is therefore \(X^{\alpha+o(1)}+O(X^{-2})\), smaller than \(F_jD_j^\beta/2\) for all sufficiently large record scales.

Each of the high rows in (5.6) can thus be good at fewer than \(\gamma q_X/2\) nodes of this same block. The remaining at most \(\gamma J_Q/4\) rows can be good at all nodes. The total number of good row-node incidences is less than

\[
\left(\frac\gamma2+\frac\gamma4\right)q_XJ_Q
<\gamma q_XJ_Q.
\tag{5.9}
\]

But (5.3), summed over the block's nodes, supplies at least \(\gamma q_XJ_Q\) good incidences. This contradiction proves \(B_1(D)=O(D^\beta)\). Since \(\beta>\alpha\) was arbitrary, (5.4) follows. Equation (2.4) gives the stated zeta exclusion. \(\square\)

### Explicit fixed-test grids

For \(W_*\), it is enough to take

\[
N_X=\left\lceil(\log X)^2\omega(X)\right\rceil,
\qquad\omega(X)\longrightarrow\infty.
\tag{5.10}
\]

For the alternative fixed profile
\(\mathscr L(j)=\log(e+j)[\log\log(e^e+j)]^{1+\delta}\), \(\delta>0\), the inherited construction permits

\[
N_X\asymp
\log X\,\log\log X\,
(\log\log\log X)^{1+\delta}\omega(X).
\tag{5.11}
\]

The test is fixed once. The assertion concerns its explicitly chosen grid on every sufficiently large dyadic interval, not an arbitrary subsequence of intervals.

## 6. What burden has actually been removed

The old full-moment criterion controls a positive sum over all \(O(D^h)\) rows and pays for every large value. Theorem 5.1 instead asks for a positive proportion of bounded values within one \(O(D^{h/6})\) principal replica annulus, and only at the fixed grid scales. It does not estimate an exceptional moment, and it does not replace such an estimate by an equivalent weak-norm bound at every amplitude.

As a statement about abstract row arrays, (5.3) places no upper bound on any moment of the unobserved fraction: that fraction can have arbitrarily large entries. What makes the actual theorem possible is the exact source identity (3.1), the rough-base correction bound, and the quantitative scale regularity. Thus the proof is a capture argument for this arithmetic source, not a generic inference from scalar moments or arbitrary arrays.

For a quantitative target such as \(\alpha=17/24\), the remaining arithmetic proposition is now explicit: at each stated grid scale, prove (5.3) for the restored literal family, on any fixed positive fraction \(\gamma\) of the specified rough principal replicas. The theorem does not prove that proposition.

If these propositions were established for every \(\alpha>1/2\), with one fixed test and with the fixed roughness set allowed to depend on \(\alpha,\gamma\), Theorem 5.1 would give RH for ordinary zeta. This does not require a conclusion about every Hecke twist. The target row and the restored detector remain fixed; only the observation set used to prove its bound changes with the stated exponent.

## 7. Compatibility with the older programmes

**Integer Möbius and fixed Mellin consumers.** The identity (2.1) is a coefficient-level bridge, so it does not assume RH in order to identify the source. It is substantially more specific than an analogy between two reciprocal-L transforms. For any kernel \(K\) compactly supported in \((0,\infty)\), putting \(W(y)=y^{-1/2}K(1/y)\) gives the algebraic relation

\[
D^{-1/2}B_1(D;W)=\sum_n\frac{\mu(n)}{\sqrt n}K(D/n).
\tag{7.1}
\]

The factor-67 modified source is obtained by applying \(I-67^{-1/2}\mathsf S_{67}\) to the right side, equivalently by applying \(D^{-1/2}(I-\mathsf S_{67})\) to \(B_1\). These identities do not authorize replacing a particular old kernel by \(W_{\mathscr L}\), or importing its sign, derivative, or noncancellation theorem for a different test.

**Compact wavelets and critical SHARP.** The old ratio-eight wavelet and the unbounded critical SHARP kernel have their own regularity and Mellin multipliers. The sampling theorem here uses its declared smooth universal profile. The already-proved positivity at supercritical SHARP powers supplies no new bound for (5.3), and the fixed-prime bias theorem supplies no unproved growing-prime uniformity. A later use of an old kernel must check that kernel itself, rather than relabeling the present detector.

**Causal Euler corrections.** The present filter is a fixed character-dilation sum plus a finite Euler restoration. It is different from the horizon-dependent Dickman correction of a finite Euler product. It needs no all-half-plane Dickman norm assertion. Conversely, the retained line-one Dickman theorem does not by itself bound this filtered family below one. Any norm transfer through \(\chi_{-3}\) must retain the signed periodic cancellation or a quantitative derivative-space hypothesis; divergent absolute coefficient mass is not discarded.

**Capture and cumulants.** The constructive row-node incidence argument above permits the bounded replica set to adapt between samples, while proving that a hypothetical large ordinary-zeta source value is still detected. This is independent of the older operator cardinal-capture theorem, whose positivity premise remains open. Complete-residue independence also does not supply a connected-cumulant cancellation for the short finite-height row distribution. No such unproved transfer is used.

## 8. Remaining gap and evidence boundary

The exact bridge, derivative count, interpolation lemma, and capture implication are proved above. The missing arithmetic input is (5.3) for the restored row family in the desired range of \(\alpha\). This is narrower than the full Hecke-family moment hierarchy, but remains a substantive cancellation problem about the actual integer Möbius source and its finite Euler replicas.

The accompanying `check_zeta_bridge_capture.py` uses only integers and exact rational arithmetic. Its deterministic report, `zeta_bridge_capture_diagnostic.json`, binds the manuscript and checker bytes and replays the two pinned source hashes when run with the declared `--repo` argument. The run checked 729 disjoint bad-prime/replica-support assignments through coefficient 160, with 116,640 coefficient equalities, all eight local split/inert/ramified deletion patterns, and six negative controls for omitted restoration, duplicate ideal norms, omitted prime powers, forbidden overlap, and source confusion. It also checked 11,089 finite good-node patterns and 55,445 rational interpolation evaluations, with the report stating the exact finite coverage.

These diagnostics check finite coefficient, interpolation, and incidence algebra. They do not establish (5.3), an asymptotic regularity estimate, a scale-uniform analytic bound, zeta zero exclusion, or RH. No such computational claim is made here.
