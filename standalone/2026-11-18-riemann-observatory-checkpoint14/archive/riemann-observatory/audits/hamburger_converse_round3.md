# Hamburger converse and the arithmetic boundary of positive-kernel models

Date: 2026-11-17. Researcher: li_advocate. Novelty is not claimed.

## Outcome and scope

An ordinary Dirichlet-series representation, the **exact conductor-one zeta functional equation**, finitely many poles, and appropriate growth imply that the function is a scalar multiple of zeta. An Euler product is not an additional hypothesis in this converse. Our Bessel countermodels satisfy the gamma factor, functional equation, permitted poles, and finite-order hypotheses, but fail the ordinary Dirichlet-series hypothesis. Their failure has an explicit positive-real asymptotic witness.

Primary evidence inspected:

* Hamburger, *Über die Riemannsche Funktionalgleichung der ζ-Funktion (Erste Mitteilung)*, Math. Z. 10 (1921), 240–254, DOI 10.1007/BF01211612: original scanned pp240–242, including Satz1 and its two-series extension. Only this portion was read; no whole-paper audit.
* Burnol, arXiv:1106.4749v2, 7 January 2012, published Expositiones Math. 30(3) (2012), 295–308, DOI 10.1016/j.exmath.2012.03.003: complete fourteen-page preprint read. Theorem1, Corollaries1–2, and their pp7–10 proof are the main source. The underlying distribution/Mellin dictionary in Burnol2007, Theorem4.54 and Remark4.29, is explicitly an external dependency, not independently audited here.
* Knopp, *Hamburger’s Theorem on ζ(s) and the Abundance Principle for Dirichlet Series with Functional Equations*, Number Theory (2000), 201–216: selected pp201–205 and 211–216, with displayed statements on pp201,211–212 visually checked. This is the author's own exposition and restatement of his1994 theorem; the 1994 publisher PDF was initially inaccessible; the original pp361–363 were subsequently accessed through GDZ, as documented below.
* Nakamura, arXiv:2008.02570v4, 10 September 2021: complete seven-page preprint read, with p4 visually checked. Published identity: Mathematica Slovaca73(5) (2023), 1145–1152, DOI10.1515/ms-2023-0084. The journal text was not accessed or compared. Direct FE/Dirichlet-series manipulations were checked; cited zero-distribution theorems were not independently audited.

Private source files and rendered evidence are in `sources/hamburger_round3/`. Do not redistribute these source PDFs or full extracted texts as part of the public archive.

## Exact original statement

Hamburger1921 p240, Satz1 assumes a single-valued analytic/meromorphic function f on C with:

1. At most finitely many finite-plane poles, of arbitrary finite orders.
2. Constants r,γ>0 so that f is regular for |s|≥r and |f(s)|≤exp(|s|^γ) there.
3. f(s)=Σ_{n≥1}a_n n^{-s}, absolutely convergent for Re(s)>1.
4. π^{-s/2}Γ(s/2)f(s)=π^{-(1-s)/2}Γ((1-s)/2)f(1-s).

Then f=cζ. No Euler product, positivity, real coefficients, normalization, zero-counting law, or RH is assumed. The equation includes the exact gamma factor, sign +1, and conductor1. Replacing the gamma parity, conductor, or integer frequencies changes the problem.

The p241 two-series extension replaces the right-hand f(1-s) by g(1-s), where g(z)=Σb_n n^{-z} is absolutely convergent in some sufficiently far right half-plane, and concludes f=g=cζ. These statements were read in the original scanned pages, rather than inferred from a later abstract.

## A stronger usable version, with all quantifiers

Set χ(s)=π^{s-1/2}Γ((1-s)/2)/Γ(s/2). Burnol Theorem1, pp2–3, assumes:

* f is an ordinary Dirichlet series convergent for Re(s) sufficiently large;
* f continues meromorphically to C with finitely many poles;
* for every finite vertical strip and every ε>0, f(s)=O(exp(exp(ε|s|))) as |Im(s)|→∞ in that strip;
* g(s)=χ(s)f(1-s) satisfies, for some integer M≥0 and real y>1/2, g(s)=O(|s|^M y^{-Re(s)}) uniformly as Re(s)→+∞.

It concludes f=Σ_{k∈Z}c_k ζ(s−2k), a finite sum. Corollary2 additionally assumes, along the **real** axis, g(σ)=c+O_k(σ^{-k}) for every k∈N, and concludes f=cζ. The real-axis condition in Corollary2 must not be substituted for the uniform half-plane condition in Theorem1.

Consequently, if f obeys the exact self-dual zeta FE, the first three bullets alone force f=a_1ζ. Indeed convergence somewhere implies |a_n|=O(n^A), hence absolute convergence in a further half-plane. Fix σ1 in that half-plane. For σ≥σ1,

    sup_t |f(σ+it)−a_1| ≤ 2^{−(σ−σ1)} Σ_{n≥2}|a_n|n^{−σ1}.

Thus g=f is bounded on a right half-plane (M=0,y=1 works), and has the required superpolynomially fast real limit a_1. Finite order after removal of finitely many poles is much stronger than the stated strip-growth bound. This extension to convergence in *some* half-plane is supported by Burnol's primary theorem; it should not be attributed without qualification to the precise1921 p240 statement, which assumes absolute convergence for σ>1.

## Proof dependency reconstruction

Burnol pp7–10 proceeds as follows:

1. Ordinary-series convergence gives polynomially bounded coefficients, hence the even tempered measure D=Σ_{n≥1}a_n(δ_n+δ_{−n}).
2. The FE-side hypothesis and χ's vertical polynomial bounds give polynomial bounds for f on sufficiently far left and right vertical lines. The sub-double-exponential hypothesis permits a Phragmén–Lindelöf argument after polynomial removal of poles, giving polynomial growth on intermediate strips.
3. Burnol2007's moderate-meromorphic/Mellin dictionary identifies E=Fourier(D) with a quasi-homogeneous part Q plus a distribution E1 vanishing on (−Y0,Y0). The right-real growth/support identity gives Y0≥y>1/2. This is the main external dependency.
4. Integer support gives exp(2πix)D=D, so E is 1-periodic. Overlapping neighborhoods of 0 and1 force the analytic part q of Q to satisfy q(x)=q(1−x), then extend to an entire polynomial.
5. Even Bernoulli polynomials remove finite ζ(s+2j) terms. The remaining periodic distribution is supported at the integers and is a finite sum of even derivatives of the Dirac comb. Fourier transformation gives the positive shifts ζ(s−2j).
6. The transforms of individual shifts have asymptotic g_k(σ)~(−4π²)^{−k}σ^{2k}. Boundedness removes k>0, and convergence faster than every inverse power removes k<0. Only cζ remains.

The local distribution steps and shift asymptotics were reconstructed. This is not a fully independent proof of the external distribution dictionary or all of Burnol's generalized-frequency Theorems2–3. Audit scope: full substantive reading, with scoped technical reconstruction and an explicit external dependency.

## Exact matching to the Bessel model

Use the independently reconstructed model in `proposals/independent_campaigns/bessel_finite_offline_countermodel_round3.md`:

    F_T(s) = K_{(s−1/2)/2}(2π) Q_T(s−1/2) / D_T,
    D_T = K_{1/4}(2π) Q_T(1/2) > 0,
    Q_T(w) = [(w−1/4)^2+T²][(w+1/4)^2+T²],   T≥32.

It is entire of order1, real, F_T(s)=F_T(1−s), F_T(0)=F_T(1)=1. Define

    L_T(s) = F_T(s) / [.5 s(s−1) π^{−s/2} Γ(s/2)]
           = F_T(s) π^{s/2} / [(s−1) Γ(1+s/2)].

The second expression establishes the precise pole structure: only a simple pole at1, with residue2; the apparent pole at0 is removable. Moreover (s−1)L_T is entire of finite order, since F_T and reciprocal gamma are of order1. Its completed function is

    π^{−s/2}Γ(s/2)L_T(s) = 2F_T(s)/[s(s−1)],

which has exactly the zeta FE with conductor1, sign+1, and only simple poles at0 and1. Scaling L_T by1/2 gives residue1 if desired.

For real s→+∞, put ν=s/2−1/4. The gamma-integral representation gives

    K_ν(2π) = .5 π^{−ν} Γ(ν) (1+O(1/ν)),

with explicit relative bounds 1−π²/(ν−1)≤ratio≤1 for ν>1, by 1−x≤e^{−x}≤1 inside the integral. Since Γ(ν)/Γ(s/2)~(s/2)^{−1/4} and Q_T(s−1/2)~s^4,

    L_T(s) ~ [(2π)^{1/4}/D_T] s^{7/4}.

Every ordinary Dirichlet series absolutely convergent in a right half-plane is bounded along the positive real axis and tends to its coefficient at n=1, by the displayed tail bound. Therefore L_T admits no such representation. It also admits no ordinary Dirichlet series merely convergent somewhere, since such convergence implies absolute convergence in a further half-plane.

If an ordinary series could be supplied while preserving these analytic properties, the converse would force L_T=2ζ, hence F_T=2ξ. The already established four off-line zeros therefore cannot coexist with that additional hypothesis. This is a barrier for the generic model class, not a statement about the zeros of actual ζ.

## Exceptions: do not collapse different hypotheses

### A. Knopp's abundance is in another Dirichlet variable

Knopp2000 pp201,211–212 uses

    R(z)=π^{−z}Γ(z)φ(z),    R(z)=R(1/2−z),
    φ(z)=Σ a_n n^{−z}.

To write the conventional zeta gamma factor one sets F(s)=φ(s/2). Then

    π^{−s/2}Γ(s/2)F(s)=R(s/2),
    F(s)=Σ a_n (sqrt(n))^{−s}.

These are generalized frequencies sqrt(n), not the ordinary integer frequencies required by Hamburger/Burnol. Knopp explicitly distinguishes assuming φ(z/2) is an ordinary Dirichlet series, which forces the square-frequency form φ(z)=Σ b_n n^{−2z}; in that class uniqueness returns. His abundance does not refute the correctly normalized ordinary-series converse. The original Knopp1994 pp361–363 were subsequently visually read through GDZ (PAPER-HC006): p361 explicitly has the same gamma/reflection normalization, and p362 Theorem1 retains it. The full technical construction was not read.

Nakamura2008.02570v4 p4 states that Knopp has infinitely many independent solutions satisfying its(H2), (H3), and ordinary-series condition(K). As printed, these use Γ(s/2) with integer frequencies n^{−s}; that appears incompatible with the preceding primary normalization and Burnol's converse. **Classification: unresolved source-level attribution/normalization ambiguity pending independent adjudication.** The concern is a background sentence, not a demonstrated failure of Nakamura's main theorems. The2023 journal version was not inspected.

### B. Nakamura's explicit examples avoid the converse for identifiable reasons

For even primitive χ mod q>1, his f(s,χ)=q^sL(s,χ)+G(χ)L(s,barχ) satisfies the exact zeta FE (Theorem2.1(i), elementary proof p5). Its q^s term introduces frequencies n/q, including1/q<1. Indeed f(σ,χ)~q^σ, so it is not an ordinary Dirichlet series convergent in any right half-plane.

Corollary2.2 instead uses g=f/(q^s+q^{1−s}). Its ordinary-series expansion is valid for σ>1 because

    q^s/(q^s+q^{1−s}) = Σ_{k≥0} (−q)^k (q^{2k})^{−s},   σ>1/2.

It preserves the FE, but only a *Dirichlet polynomial*, not an ordinary polynomial in s, is asserted to clear all poles. That replacement is not Hamburger's finite-pole hypothesis. No claim that every candidate denominator pole survives cancellation was checked here.

### C. An elementary infinite-pole example makes the distinction explicit

For an integer q≥2 set

    M(s) = 1/[(1−q^{2−s})(1−q^{1+s})],    f(s)=M(s)ζ(s).

Then M(1−s)=M(s), so f satisfies the exact zeta FE. For σ>2,

    M(s)=−Σ_{j≥0,k≥1} q^{2j−k} (q^{j+k})^{−s}

is an absolutely convergent ordinary Dirichlet series, and so is f. Nevertheless f has a simple pole at every s=2+2πik/logq: the second denominator is nonzero there, and ζ is nonzero for Re(s)=2 by the absolutely convergent Euler product. There are infinitely many poles. In the standard Nevanlinna meaning M and f are meromorphic of finite order, illustrating why the phrase 'meromorphic finite order' cannot silently replace 'polynomial times f entire of finite order'. No novelty is claimed for this elementary example.

No counterexample with ordinary integer frequencies, finitely many poles, and exact zeta FE but growth beyond Burnol's bound was established here. Knopp's rescaling must not be presented as such an example.

## Concrete next research steps

1. Independently audit the moderate-Mellin dictionary, Burnol2007 Theorem4.54/Remark4.29, to close the external dependency in the weak-growth converse. The local periodicity argument has already been reconstructed.
2. Check Knopp1994 p362 and the2023 Nakamura journal text before upgrading the background attribution ambiguity. Keep any correction restricted to the actual version and sentence inspected.
3. For any proposed positive-kernel RH strategy, explicitly calculate L(s)=F(s)π^{s/2}/[(s−1)Γ(1+s/2)] and first test its real-axis boundedness. If it fails, determine the missing Mellin-distribution integer-support condition rather than imposing an Euler product by analogy.
4. A meaningful stability problem is to specify a topology controlling both the analytic continuation/FE and the discrete integer support of the Mellin distribution. A finite coefficient match, finite Li prefix, or zero-count asymptotic alone supplies no such control. No stability theorem is asserted here.

The research conclusion is a precise scope boundary: the countermodels retain more analytic structure than a mere symmetry analogy, but the exact arithmetic representation is already a uniqueness condition under established growth hypotheses.

## Addendum: all fixed Bessel polynomial perturbations fail the ordinary-series test

The positive-real witness extends beyond the particular quartet. Fix c>0 and any nonzero polynomial P of integer degree d≥0 with leading coefficient p_d. Put

    F(s)=P(s−1/2)K_{(s−1/2)/2}(c),
    L(s)=F(s)π^{s/2}/[(s−1)Γ(1+s/2)].

No positivity or symmetry of P is needed for this negative statement. The same gamma-integral estimate gives, as real σ→+∞,

    L(σ) ~ p_d c^{1/4} (2π/c)^{σ/2} σ^{d−9/4}.

Multiplication by a nonzero normalization constant simply multiplies this nonzero leading constant. If L were a nonzero ordinary Dirichlet series convergent somewhere, let n0 be its first nonzero coefficient index. Absolute convergence in a farther half-plane and dominated convergence give

    n0^σ L(σ) → a_{n0} ≠ 0.

Combining this with the displayed asymptotic first forces n0 sqrt(2π/c)=1, and then forces d−9/4=0. The latter is impossible for integer d. Thus **no nonzero polynomial perturbation of this fixed-scale Bessel family has an ordinary Dirichlet-series standard uncompletion**, for any c>0. In particular, changing c cannot fix the arithmetic representation. This covers polynomial differential modifications of the underlying kernel, including those that preserve positivity. It does not cover nonpolynomial kernel modifications or sums of differently shifted Bessel orders.

For c=2π and d=0 or2 the uncompleted function tends polynomially to0, so mere real-axis boundedness would not detect the failure; the first-nonzero-coefficient asymptotic does. This elementary family obstruction is independently derived here, with no novelty claim and parent review requested.


## Original Knopp1994 statement access update

The original journal scan pp361–363 is now directly inspected, not merely inferred from the2000 restatement. It is saved privately as `sources/hamburger_round3/knopp1994_excerpt.pdf` and the three original IIIF JPEGs. Printedp361 states R(s)=π^(−s)Γ(s)φ(s), R(s)=R(1/2−s); p362 distinguishes ordinary φ(s/2) in3(a) from ordinary φ(s) in the abundance condition3 and Theorem1. This confirms the normalization comparison. The remaining limitations are the uninspected1994 construction/proof, the uninspected2023 journal version, and final independent adjudication of the narrowly scoped background attribution.
