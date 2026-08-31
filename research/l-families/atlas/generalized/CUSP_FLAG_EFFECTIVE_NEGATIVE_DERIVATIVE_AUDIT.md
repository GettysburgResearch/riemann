# Independent audit: effective negative derivative of the actual cusp quotient

Status: PASS for the exact scientific source below. This is a separate
review record, not a rewrite of the frozen proposed packet.

Scientific source: a32a3923f34e2a281737cc1f2cd610bc5c69279e.
Authoring base: 282ce03941444d0e02daba5fde260ccb54a3f909.
Programme import: a88712475c8e0e605f67dc31dfaf818b7abfebb5.
Review date: 2026-08-31.

The [proof](CUSP_FLAG_EFFECTIVE_NEGATIVE_DERIVATIVE.md), producer, full
fixture, manifest and tests were read. Root and a separate non-author
reviewer checked the analytic argument and replayed the frozen release.
The independent reviewer did not coordinate with the author or edit sources.
No repair was required.

## Accepted statement, with the variable fixed

The source remains the weight-24 canonical pair
g=Delta E4^3-696 Delta^2, b=Delta^2, in q=exp(2 pi i z). For w=s+23,

    F(w)=B(w)-2^w C(w)^2/(1+U(w)),
    L(w)=zeta(2w-46) F(w),
    B=sum c_n^2 n^-w,
    C=sum_(n>=3)c_n b_n n^-w,
    U=sum_(n>=3)b_n^2(n/2)^-w.

Set x_*=log(9/2), m=8192 and w_*=96+m/x_*. The derivatives are taken
with respect to w BEFORE evaluation. For

    R_f=(-1)^m f^(m)(w_*)/[x_*^m (9/2)^(-w_*)],

the certified upper bounds are

    R_F <= -88203307492526,
    R_L <= -88203140778512.

Since m is even and the normalizer is positive, the actual 8192nd
derivatives of both fixed functions are negative at this exact point.
These are upper bounds, not sampled or exact transcendental derivative
values. The source is not a generic positive-matrix toy.

The result makes effective one case of the earlier
[positive-spectrum boundary](CUSP_FLAG_POSITIVE_SPECTRUM_BOUNDARY.md).
It does not establish negative second derivative, the least possible
derivative order, an effective all-weight theorem, or a statement about
the completed quotient Q(s)=A_24(s)L(s+23).

## Analytic proof review

1. ED5 is a coefficientwise global majorant. Integral bounds for sigma_3
   and sigma_5, followed by convolution of (1-q)^-j, control E4, E6,
   Delta, b and g. The identity
   binom(n+23,23)/n^23<=24 holds for every n>=1. Thus ED6 is a genuine
   bound for all coefficients, not a finite-data extrapolation. Its
   deliberately loose constants 2^84 and 2^95 are valid.

2. At w0=96 the uncomputed coefficient tail begins at n=65. The integral
   sum_(n>=65)n^-50<=64^-49/49 gives exactly
   2^-104/49, 2^-115/49 and 2^-30/49 for the three stated absolute sums.
   Every finite term and tail is rounded upward on the 160-bit dyadic grid.
   The pivot b_2=1 is excluded from U: it has already been factored out
   as 2^-w in the Schur denominator.

3. The certified inequalities U_abs(96)<2^-30<1 and the bounds for B,C
   justify the geometric inverse in the entire closed right half-plane.
   The common factor 2^w is retained when deriving all-word absolute
   mass M_F<2. Zeta(146)<=146/145 gives M_L<4. These majorize grouped
   and ungrouped series and every uncomputed inverse word/zeta factor.

4. Normal absolute convergence permits differentiation at each w>96:
   for any fixed derivative order h the extra factor
   (log rho)^h rho^-(w-96) is bounded on rho>=1. No interchange of a
   moving evaluation point with differentiation is used.

5. ED10 gives complete prefix coverage. A correction of depth h has
   rho>=(9/2)(3/2)^h. At cutoff 12, h<=2, endpoint indices<=8,
   internal indices<=5 and the zeta index<=3. There are 16, 10 and 1
   ordered correction words at those depths, and none at depth three.
   Both full prefixes have 17 nonzero atoms. The unique 9/2 atom is
   -88203653222400; zeta does not cancel it.

6. ED11 encloses logarithms using a rational atanh-series remainder,
   then outward rounding. The logarithms themselves are not declared
   rational. ED12 has the correct inequality direction on both sides
   of t=1, by integrating (1-u)/u or (u-1)/u. The intervals avoid the
   target, giving K_4=35, K_5=26 and K_12=1506.

7. Psi(t)=t exp(1-t) decreases for t>1. Hence EVERY frequency rho>12
   satisfies the same cutoff bound 2^-1506. Applying this to the
   previously proved infinite absolute masses pays the entire omitted
   tail; no unsupported spacing assumption is made about that tail.

8. In ED14 the constant atom vanishes for m>=1 and the target contributes
   exactly its negative coefficient. Integer ceilings for all other
   prefix terms and the whole tail give E_F=345729874 and E_L=512443888.
   Adding those errors to -88203653222400 gives the accepted bounds.

## Independent reconstructions

Root did not use producer mathematics to reconstruct the certificate:

- Delta was reconstructed from its finite Euler product through q^64.
  The distinct expression g=Delta E6^2+1032 Delta^2 then reproduced all
  64 rows, including both source coefficients in every row.
- A triangular inverse in the exact rational-frequency monoid rebuilt
  both complete F,L prefixes. Liberal endpoint/internal boxes through
  twelve independently gave depth counts 16,10,1,0.
- Exact unrounded coefficient sums, their upward dyadic sums and the
  analytic tail rationals matched all three published mass certificates.
- A separate 64-term calculation reproduced the published log intervals;
  96-term range-reduced calculations refined all fifteen nontarget
  intervals. All ratio intervals, kernel losses, exponents, termwise
  ceilings and final error sums agreed.
- Eight additional resealed source/coefficient/mass/gap/scope/type changes
  failed validation in normal and optimized Python.

The non-author reviewer separately reconstructed Delta through q^80,
checked all q^64 source rows, and rebuilt the frequency maps by
cross-multiplied Schur residual division. Prime-factor/range-reduced
96-term log enclosures refined the published intervals. Held-out orders
6000 and 8191 were controls, not new minimal-order claims. The reviewer
also checked 63 resealed-tamper/type/cap cases in both Python modes.

The written infinite-tail and convergence arguments were reviewed as
mathematics. None of these finite replays machine-proves them.

## Source identities and classical normalization

All four primitive commit/path bindings were independently authenticated
by raw Git blob identity and LF-normalized SHA256:

- repaired positive-spectrum proof at 282ce03941444d0e02daba5fde260ccb54a3f909;
- weight-24 quotient proof at b62dfc6348661992bca659c99de226a1b6b22e14;
- its complete coefficient fixture at that same b62dfc6 source;
- the weight-24 review at 8e9f05211954e0a7aae5e63c9367f1d520d3671d.

The four current note/producer/manifest/test hashes, full fixture hash and
payload seal were independently checked. The source blob identities are:

| Frozen file | Git blob |
|---|---|
| CUSP_FLAG_EFFECTIVE_NEGATIVE_DERIVATIVE.md | 9cb8c521b61bf302787fc5d3a74ecb6e3f95fb94 |
| cusp_flag_effective_negative_derivative.py | bf19643d4af80c48221917598358c20cd50280a9 |
| cusp_flag_effective_negative_derivative.json | 785aba0e49acdc168c03cca22160681e1715490e |
| cusp_flag_effective_negative_derivative.sources.json | f175a6adb7495cc1b4d69ac23b3b7b9748591984 |
| tests/test_cusp_flag_effective_negative_derivative.py | a0103acf42fde0d9411cb3551b88d923e7debf62 |

Fixture LF-SHA256:
018330b53681071522b15466316e47b07bf4d3f9fff711cdc6a62fb314239032.

Payload SHA256:
1ce6c497285ea1893b4092797e50118d431da07b2e930fc39f7643b9a29b70d6.

Root checked the normalization against
[Zagier, Elliptic Modular Forms and Their Applications](https://people.mpim-bonn.mpg.de/zagier/files-restricted/doi/10.1007/978-3-540-74119-0/fulltext.pdf):
printed pages 16--17 distinguish the Eisenstein normalizations and give
the constant-one E4,E6 coefficients; printed page 21 gives the Delta
relation. The relevant displayed pages were visually read using the PDF
source-reading workflow. Remote PDF bytes are not authenticated by the
offline manifest. These are classical inputs, not new abstract claims.

## Replay and acceptance boundary

Root replay at the frozen source passed:

- 30 tests normally (1.314s) and under -O (1.313s);
- both complete producer checks;
- the independent reconstructions in both modes;
- Ruff lint and format checks without cache;
- the complete 282ce039-to-a32a3923 whitespace check.

The separate reviewer passed the same 30-test modes, producer checks and
both emit modes, source hashes, Ruff and the complete authoring diff.
The author worktree remained clean. Programme import preserves the exact
five scientific file versions.

Arithmetic is MIXED with CERTIFIED_INTEGER_COVERAGE and EXACT_RATIONAL.
The contract has q order 64, cutoff 12, inverse depth 2, derivative order
at most 8192, log degree 64, 40/160-bit dyadic grids, 32-bit primitive
rationals, 8192-bit checked internal rationals, 512-bit q coefficients,
1 MiB source/JSON bounds and one million charged work units.
The native report used 35120 charged units. This does not mean every
Python instruction or arbitrary hostile object is charged. Standalone
helpers accepting arrays do not authenticate an unrelated infinite series.

No completed-Q sign, negative curvature, minimum derivative order,
uniform-in-weight effective bound, new automorphic representation,
positive Weil criterion, RH/GRH conclusion or external novelty is accepted.
