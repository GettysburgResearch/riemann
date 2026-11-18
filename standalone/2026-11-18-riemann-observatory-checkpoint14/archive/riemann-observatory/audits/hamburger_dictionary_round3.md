# The moderate Mellin dictionary: scoped reconstruction and a short self-dual converse

Date: 2026-11-17. No novelty claim. This extends `hamburger_converse_round3.md` one dependency level.

## Primary source and read boundary

Jean-François Burnol, *Entrelacement de co-Poisson*, Annales de l’Institut Fourier57(2) (2007), 525–602, DOI10.5802/aif.2268. Actual publisher PDF downloaded from https://www.numdam.org/item/10.5802/aif.2268.pdf. Inspected printed p577, pp580–585, and pp590–593, especially Definitions4.11,4.27,4.45,4.53; Remark4.29; Theorems4.26,4.31,4.54; Lemma4.50 and Proposition4.51. The entire78-page work was not read. Earlier smoothing/Fourier intertwinement proofs and all other sections are outside this audit.

## The exact dictionary

A meromorphic function F is moderate (Definition4.53) if a nonzero polynomial P makes PF entire and moderate. Entire moderation (Definition4.27; equivalent description Remark4.30) means polynomial growth on each vertical line and membership in the analytic Nevanlinna class in every right half-plane; equivalently, for every σ0 there are A>0 and integer M such that

    |F(s)| ≤ const · A^{Re(s)}(1+|s|)^M,    Re(s)>σ0.

A tempered distribution has extended-S support if both it and its Fourier transform agree with quasi-homogeneous distributions in a neighborhood of0. Its right Mellin transform is defined after subtraction of the quasi-homogeneous part; for distributions vanishing near0, it is the usual distributional continuation of ∫_0^∞ D(x)x^{−s}dx. An integer Dirac comb contributes Σa_n n^{−s}, with no factor2 from its even extension.

Theorem4.54, pp592–593, says that even extended-S distributions correspond to meromorphic moderate F for which χ(s)F(1−s) is also meromorphic moderate. The Fourier transform has Mellin transform χ(s)F(1−s). The representing distribution is unique after normalization to vanish near0; without that normalization two representatives differ by an even quasi-homogeneous distribution.

This is exactly the dictionary required in Burnol2012's converse, not a theorem about arbitrary entire functions or arbitrary inverse Mellin transforms.

## Proof reconstruction and remaining standard inputs

Theorem4.31's converse, pp584–585, is constructive. Right-half-plane moderation gives a>0,M such that a^sF(s)/s^{M+1} is Hardy H² on Re(s)>1/2. The Mellin form of the Hardy Paley–Wiener theorem gives a function supported on[a,∞). Applying ((d/dx)x)^{M+1} produces a tempered even D vanishing near0 and with Mellin transform F.

Apply the same construction to G=χF(1−s), giving k vanishing on(0,a'). The L² Fourier–Mellin identity expresses the Fourier transform of the first primitive using the multiplier [s/(1−s)]^{M+1}. The operator with multiplier s/(1−s) is

    (Lk)(x)=−k(x)+∫_x^∞ k(y)dy/y.

On0<x<a', this is constant; iteration gives a polynomial in log x of degree at most M. Applying (x d/dx)^{M+1} kills it, including as an even distribution at0, since x d/dx(log|x|)^j=j(log|x|)^{j−1}. The Fourier transform of D therefore also vanishes near0.

Theorem4.54 reduces meromorphic data to this entire case by a polynomial clearing the finitely many poles of the completed function. Those poles are finite because the FE-side meromorphy cancels the gamma poles outside a finite set. Lemma4.50 solves each Euler differential factor on distributions vanishing near0, using the unique primitive

    D1(x)=|x|^{z−1}∫_0^x |y|^{−z}D(y)dy.

Polynomial growth is preserved because the integration starts away from0. Proposition4.51 identifies the resulting Fourier side as quasi-homogeneous near0. Mellin injectivity after subtraction of that part gives uniqueness modulo quasi-homogeneous distributions.

The operator signs, Mellin powers, origin normalization, and support implications were independently reconstructed. Standard inputs accepted rather than formally reproved here are Hardy Paley–Wiener, Smirnov–Nevanlinna factorization, the L² Fourier–Mellin identity, and elementary tempered-distribution integration/uniqueness. Earlier distribution-smoothing lemmas used in the forward direction are source dependencies not fully audited. This closes the *statement and proof architecture* of the previously opaque dictionary dependency; it is not a complete independent audit of the whole78-page paper.

## A short independent self-dual reconstruction

The general shifted-zeta analysis is unnecessary when the FE is exactly self-dual. The following lemma isolates the arithmetic rigidity.

**Integer-comb lemma.** Let D=Σ_{n≥1}a_n(δ_n+δ_{−n}) be a tempered measure. Suppose E=Fourier(D), and E−D is an even quasi-homogeneous distribution. Then all a_n are equal.

Proof. Integer support gives e^{2πix}D=D, hence E is1-periodic. Write Q=E−D. Its restriction q(x) to x>0 is a finite linear combination of x^α(log x)^j. On every open interval avoiding integers, periodicity gives q(x+1)=q(x); analyticity extends this to all x>0. For each complex z choose a positive integer k with Re(z+k)>0 and define q_ext(z)=q(z+k). Analytic periodicity makes the definition consistent. Taking k no larger than2+max(0,−Re z) gives a polynomial growth bound for q_ext onC. It is an entire polynomial and1-periodic, hence constant, say c. Evenness gives the same constant on x<0. Thus Q−c is supported at0, and is a finite linear combination of even Dirac derivatives.

Near0, E consists of c plus these derivatives. Near1, E consists of c+a_1δ_1, because D is a measure and Q has no nonconstant analytic part there. Periodicity excludes every derivative δ_0^{(2j)} with j≥1 and makes the mass coefficient at0 equal a_1. Repeating at every integer gives a_n=a_1. ∎

Now take an ordinary Dirichlet series f in the analytic class of THM-HC301. The polynomially bounded coefficients define D above. The theorem4.54 correspondence and Mellin injectivity identify D as its normalized representative. Since χf(1−s)=f, the same theorem gives Mellin(E)=Mellin(D), so E−D is quasi-homogeneous. The lemma yields f=a_1ζ.

This proof uses the exact integer support, rather than an Euler product or positivity. It independently cross-checks Burnol2012 Corollary2 in the self-dual case and avoids the general support-distance formula of Remark4.29. The dictionary and standard analytic inputs remain explicitly identified.

## Consequence for the Bessel model

All analytic and growth hypotheses of the converse are met by its standard uncompletion L_T; only ordinary integer-frequency representation is absent. The growth L_T(σ)~Cσ^{7/4} already rules out such a representation. The comb lemma specifies why a replacement by an arbitrary continuous Mellin distribution or generalized square-root frequencies does not repair this failure: integer support is exactly what supplies1-periodicity on the Fourier side.
