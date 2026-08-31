# Independent review: effective proper theta-source zero pair

Verdict: **PASS** at exact science
`6e47a4b2604668eb88b977c9182f5a04a214638a`, immediate parent
`b1808243579b7eec8542a24a6a729cbed623ad07`.
Review date: 2026-08-31. This reviewer neither authored the effective
argument nor contributed its pre-freeze critique. The reviewed science
is unchanged; this is one separate review-only Markdown addition.

## 1. Frozen identity and source scope

The complete 176-line [effective proof](PROPER_THETA_SOURCE_EFFECTIVE_WEIGHT96.md)
has Git blob `7258cdecaaa9379824e99bbfcaa47170ac0849ba` and normalized-LF
SHA256 `a1ce66344ca96dbc828f405adeeb7d0deea73db62a0d7481fcdb1b2ede7a312e`.
Its entire parent-to-science diff is that one added proof file.

The exact imported science/review pairs are:

| Parent | Science | Independent review |
|---|---|---|
| TQ source central criterion | `0d1f90323c8d61abefee077b7bcaa4c024596a55` | `31e5ca265cc3be43cff30962041d93a2be4d8ee2` |
| HC coefficient Poincare kernel | `14fa39a02267c043ac27cd68ef7157ef77afe83b` | `3575c8274a887bc5de29aa41749cac37f49b73cd` |

The HC successor review is a metadata comparison. Its original mathematical
review at `591d6ade9bcfe218e1519bbab91cce3d2c2ed305`, on science
`eaa8e8263bb34b8b669f911580c9dd9e55766ba2`, was also read completely.
HC Section 7's unfolding and complete Bessel bound were personally checked.
TQ and its MP source completion were already fully read in the immediately
preceding independent TQ review; their precise imported role here is the
exact criterion TQ1--TQ7, NOT the later non-effective norm asymptotic.

The five parent proof/review files below were reauthenticated against their
frozen Git bytes, with exactly matching resident LF-normalized content:

| File | Normalized-LF SHA256 |
|---|---|
| [TQ proof](PROPER_THETA_SOURCE_REAL_ZERO_COROLLARY.md) | `22cbe2797ac06ae37468e4da93d17b261d99675f50255fd6a2c67bf53ca1f70f` |
| [TQ review](PROPER_THETA_SOURCE_REAL_ZERO_COROLLARY_REVIEW.md) | `c4ae9eef856daf5c4df27d76ebfbc2b17c849ab6e3de03fb50efef96c6862b3b` |
| [HC proof](CUSP_FLAG_HECKE_SOURCE_CONCENTRATION.md) | `9ab8e18f6994c3ea6e3bd662cb4b0365e8dc6b5a18a05d1c8b10857f78e90032` |
| [HC successor review](CUSP_FLAG_HECKE_SOURCE_CONCENTRATION_AUDIT_14FA39A0.md) | `e7fc36d9daf9005ec3780d6369e24464188f42adf4ad898839e9f637b240f871` |
| [HC mathematical review](CUSP_FLAG_HECKE_SOURCE_CONCENTRATION_AUDIT_EAA8E826.md) | `d9d5fcb9342cc17baa7d37a9cb235ec119e04bd5ffc1927a18e71be1f2b38198` |

All five corresponding commits are ancestors of the effective science.
These are analytic imports and provenance checks, not a claim that finite
code proves the Poincare expansion or theta continuation.

## 2. Exact vacuum normalization and properness

Use the sign-identified Gamma_infinity quotient in HC and even k>2.
Unfolding the ordinary holomorphic Poincare series in the Petersson
form with conjugate-linear FIRST argument gives

    G(P,f) = integral_0^infinity integral_0^1
               conjugate(q) f(x+iy) y^(k-2) dx dy
           = a_f(1) integral_0^infinity y^(k-2) exp(-4pi y) dy
           = A_1 a_f(1).

The width is one, and there is no extra factor two from the sign quotient.
For P itself this gives G(P,P)=A_1 p; consequently p is real. The positive
explicit lower bound proved below ensures P is nonzero and p>0.
Cauchy--Schwarz then gives G(f,f)>=A_1/p for EVERY a_f(1)=1.
The actual modular form P/p attains equality. Thus G_Q=A_1/p exactly.

This identifies the minimizing lift for G ONLY. It does not identify the
minimizer of H(t), assert it is independent of t, or interchange a source
quotient with Mellin integration. The uniform all-lift bound from TQ remains
the reason that the central criterion applies to the proper source quotient.
At every even k>=96 the level-one cusp dimension is at least two; p>0
also proves surjectivity of [q]. Thus ker([q]) is nonzero and the quotient
is genuinely proper, including the exceptional residue class 2 modulo 12.

## 3. The complete Bessel/Kloosterman estimate

HC's classical Fourier formula has off-diagonal factor 2pi*i^k and
argument 4pi/c at depth one. Its absolute bound is independent of the
parity sign. The defining series, also checked at
[DLMF 10.2.2](https://dlmf.nist.gov/10.2.E2), gives for real x>0 and
integer nu>=0

    |J_nu(x)| <= (x/2)^nu/nu! * exp(x^2/(4(nu+1))).

Indeed (nu+m)!>=nu!*(nu+1)^m bounds EVERY term of the absolute series.
There is no truncation or numerical Bessel evaluation. For nu=k-1>=3,
the trivial Kloosterman bound |S(1,1;c)|<=c and
sum_(c>=1)c^(-nu)<=1+1/(nu-1)<=2 bound the ENTIRE c series. Replacing
its exponential factor by the c=1 upper bound gives exactly

    |p-1| <= 4pi*(2pi)^nu/nu! * exp(4pi^2/k).

This is an explicit inequality valid already for k>=4, not an eventual
asymptotic imported beyond its domain. For k>=96, pi<22/7 gives
4pi^2/k<121/294<1, 2pi<7 and 4pi<13. Since e<3, even the constant39
would suffice; the proof's looser42 is valid. Hence
|p-1|<42*7^nu/nu!. Its successive ratio is 7/(nu+1), at most7/96<1.
The exact base case E4 therefore proves p>999/1000 for every nu>=95.

## 4. Uniform Gamma lower bound and independent arithmetic

With nu=k-1 the power in J is y^(nu-1/2). Its omitted integral on (0,1)
is strictly less than 1/(nu+1/2), because exp(-4pi y)<1 there.
After division by A_1 this is precisely the subtraction in E6.
The lower surrogate (nu-1)!/13^nu is below A_1 and its successive ratio
is nu/13>=95/13>1. E7 therefore gives A_1>1000 for every nu>=95,
and the subtracted amount is less than1/1000 throughout this range.

Integral Cauchy--Schwarz applied to the square roots of
t^(x-1/2)e^(-t) and t^(x+1/2)e^(-t) gives

    Gamma(x+1)^2 <= Gamma(x+1/2)Gamma(x+3/2),
    Gamma(x+1/2)/Gamma(x) >= x/sqrt(x+1/2),    x>0.

All integrals converge in the stated range. Moreover
(x^2/(x+1/2))'=x(x+1)/(x+1/2)^2>0. E9 at95, together with
4pi<88/7, therefore supplies the same lower bound137/50 for EVERY nu>=95.
No Stirling approximation or unknown onset is used.

Independent standard-library integer/Fraction calculations, importing no
author producer, passed normally and under Python -O. Factorials were
reconstructed both by factorial and by the product of all integers.
The two large-integer comparisons were strictly positive:

    95! - 42000*7^95 > 0,
    94! - 1000*13^95 > 0.

Their differences have respectively149 and147 decimal digits. Other
independently reconstructed exact quantities are:

| Check | Exact positive reserve or value |
|---|---|
| E9 left side minus (137/50)^2 | `25353/2626250` |
| (999/1000)(2739/1000) | `2736261/1000000` |
| Previous value minus273/100 | `6261/1000000` |
| Complete exponential-series upper bound | `11743/4320` |
| 273/100 minus that upper bound | `253/21600` |

The exponential tail begins at n=6, and every subsequent term ratio is
at most1/7. Thus 163/60+7/4320 bounds the FULL tail-corrected series.
There is no floating estimate of e hidden in the last comparison.
All eleven transient arithmetic guards passed in both modes; these are
checks of the proof's finite constants, not new G-suite tests.

## 5. Effective conclusion and remaining boundaries

The inequalities give J/A_1>2739/1000 and p>999/1000. Since
G_Q=A_1/p, the exact source parameter obeys

    R=J/G_Q=pJ/A_1>2736261/1000000>273/100>e.

TQ's all-lift cusp bound and MP completion then give
L_(k,1)(1/2)/G_Q>=2R(log R-1)>0 for EVERY even k>=96.
The positive residue at one implies negative divergence from the left.
Real analyticity, absence of interior poles and reflection therefore
force distinct sign-changing real zeros in (0,1/2) and (1/2,1), with
odd multiplicity for at least one reflected pair. Multiplication by
s(s-1) cannot remove either zero. This is the source-level construction,
not a period-Schur quotient or a quotient of sampled central values.

PASS is an effective sufficient threshold for coefficient depth one.
It proves neither optimality nor weight24, simplicity, uniqueness,
individual location, a 12j/k law, a uniform higher-depth threshold,
an Euler product or an RH/GRH counterexample. No central values or
zeros were numerically sampled in this review.

No scientific file, test module, producer, programme front or remote ref
was changed. The existing37-module G replay count is unchanged, and that
suite was not rerun for this analytic-only review. The one-file science
diff and the exact parent bindings were checked separately from the
mathematical argument. No actionable repair is required at this identity.
