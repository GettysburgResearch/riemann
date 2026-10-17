# Sharp complete long-twist moments; an audit of the cancellation claim

**PROPOSED unconditional mathematics, not independently reviewed. No new
fixed-twist moment exponent, zero-free boundary, or RH proof.**

This pass replaces the earlier loose norm-fiber count by a multivariable
transport calculation and proves a complete long-Mellin-twist moment bound.
The exact averaging cost stays in the theorem, not in an implicit constant.

## The actual advance

For a fixed number field F, let r count the field factors of F tensor_Q F.
For every fixed k and the original compact-window arithmetic source,

    integral g_T(t-t0) sum_u w(u)|A_t(X,u)|^(2k) dt
      <= C Z X^k log(3X)^(r*k^2-2*k+1) (1+X^k/T).

The source can be native Mobius or any of the coupled, two-channel and
geometric completions. Constants are uniform in m>=2, phases and nonunit
masks, but NOT growing k or discriminants. Every ideal tuple and every
unequal-product-norm contribution is present in this averaged statement.

For the principal native Eisenstein source on X/2<NI<=X, the order is SHARP
for every fixed k and T>=2X^k, uniformly in the twist center:

    mean |A_t|^(2k)  asymp  X^k log(X)^(2*k^2-2*k+1).

Orders 2,4,6 give X log X, X^2 log^5 X, X^3 log^13 X. This is a two-sided
order estimate, not an asymptotic leading constant. The lower proof counts
pairwise-coprime split-prime transport boxes. The upper proof uses a signed
Euler quotient whose absolute critical coefficient mass is finite, then the
(k-1)^2-dimensional transport-box count. The methods are classical.

The complete Gaussian cumulative version is also proved. At fourth order
over Q(omega), its upper bound is

    C Z [log(3D)^6 + (D^2/T)log(3D)^5].

The previous loose norm-fiber exponent at fixed scale was r*k^2. Retaining
the individual column constraints saves 2k-1 logarithms. The k=1 native and
coupled Gaussian bound already occurs in #954 and is explicitly credited.

## A correction to how the earlier result was described

For principal native Mobius coefficients over the Eisenstein field, the
Mobius sign of an ideal tuple is determined by its product rational norm.
Hence EVERY nonzero equal-product-norm tuple contribution is nonnegative.
The earlier positive same-norm covariance asymptotic is valid, but it did
not establish cancellation between opposite signs. Its mathematical scope
was stated narrowly; describing it as progress on the difficult signed
cancellation nevertheless overstated what had been achieved.

This audit does not extend to nonprincipal row phases or coupled powerful
coefficients. Those objects remain distinct.

## What remains, and what was actually checked

The principal fixed-twist unequal-norm remainder is unbounded at the
required power. In fact an allowed unsigned-squarefree profile proves that
the averaging window X^k is necessary at the POWER level for a uniform
coefficient theorem. It is not a counterexample for native Mobius, but it
prevents using this averaged upper bound as automatic pointwise extraction.

Read THEOREMS.md for all hypotheses and complete proofs. The proof uses no
RH/GRH, imported quasi-RH, unknown moment, or assumed signed flux bound.
It is not an independent-prime approximation. Classical ideal counting,
Euler products, Gaussian Fourier integration and matching geometry are
credited in SOURCES.md; no global literature-priority claim is made.

35555 finite predicates reproduce in ordinary and optimized Python,
including 80 formal local splitting cases, 262 transport-cap configurations,
and complete good squarefree Eisenstein ideals through norm 1024. Three
separate corrupted optimized processes fail. NUMERICAL.json is separately
labelled ordinary high-precision finite Fourier quadrature, not a certificate.
No independent referee, Lean build, full-repository validator, upstream theta
build or remote CI is claimed. See VALIDATION.md.

Publication is additive, stacked on #954 at
3241178607671c4dd979cefdad0670fd426194da. Main and inherited proof files are
not modified. The previous ramified-dilation packet is already present on
that base. The earlier norm-fiber download is retained locally unchanged
and its ordinary/optimized checker was replayed; it is not silently claimed
to have become a reviewed or integrated result.
