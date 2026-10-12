# Independent review of the opposite-derivative theta return

Reviewer: `/root/height_mechanisms`, 2026-10-10 UTC.
Result: **ACCEPT O1–O5 at the stated imported theta-automorphy scope**, for
the complete specified standard-cusp all-negative component. No complete
moment or other-cusp assertion is approved by this receipt.

Reviewed document: `../literature/OPPOSITE_THETA_DERIVATIVE.md`, SHA-256
`08fe836931d000685f1304f6041d6c83f5e81ff4d632d64474ad79c9df8d2a4b`.
Primary literal source: `/workspace/.riemann-research/sources/qrh11-12.tex`,
SHA-256 `d9a8f15aa770cf883d0eabd2b775fad694ce20b44cba7928f5c0c9a6d8750d4d`.
The source's automorphy and Patterson coefficients are imported, not rebuilt.

The following interfaces were checked directly against the source labels
`eq:intro-theta-coefficients`, `eq:general-twisted-theta-definition`,
`eq:theta-factorized-shifts`, `eq:ray-fourier`,
`eq:theta-cusp-coordinates`, `eq:ray-local-transform`, `eq:ray-mellin`,
`eq:theta-mellin-functional-equation`, and `eq:theta-weight`.

1. With `lambda=i sqrt3`, the phase of `lambda^(-3)` is `i`.
   The opposite derivative contributes `i alpha(ell)`, so the normalized
   completed coefficient has exactly `-C(s)`, with the same two gamma
   factors and all finite periodic multiplier zeros. The angular character
   is supplied by differentiation rather than inserted into a periodic
   multiplier.
2. At the inverted cusp, the opposite derivative is
   `-(bar(c) v)^(-2) partial_bar_z`. Changing height to `1/(Nc v)` gives
   `-alpha(c)^2 Nc^(1-2s)`. The reflected derivative has `bar(alpha(ell))`;
   dividing by the negative original normalization gives the physical scalar
   `+(i/81)alpha(c)^2`. The finite local Fourier/Gauss calculation occurs
   before this derivative, so its factors and nonunit zeros remain identical.
3. All `j=3` primes of the moving squarefree `k` are active. The source's
   reduced denominator proof uses active denominators, not `j=1`
   specifically: these groups still have `c=c0*k`, with finitely many
   fixed `c0` after the fixed-ray split. Their transformed character is
   `B_(p,3)=chi_p`, retaining its zero; it is not quadratic.
4. The full Mellin symbol satisfies `g(t)g(-t)=1` and both dilation factors
   cancel. Thus `H(HV)=V` exactly. The intermediate profile is rapidly
   decreasing at infinity and `O(x^(5/6-epsilon))` at zero. Its Mellin line
   `s-1/2=-2/3` lies strictly above the first numerator gamma pole `-5/6`.
   The continued opposite coefficient series is entire, and the source's
   polynomial vertical-growth argument has the same coefficient magnitudes
   and gamma factors. These justify the second reflection and inversion.
5. On the selected standard face, the fixed additive bad-ray phase expands
   into finite multiplicative ray characters of `n b^3`. The supplementary
   factor in `n` is cubic. Hence `psi=rho*vartheta*chi_k^3`, with
   `vartheta^3=1`, matches both the `n` and cube coefficients exactly.
   The all-negative Ramanujan allocation does not require `(g,nb)=1`;
   inserting that mask would destroy this completed match.
6. Substituting `X=Ng^2 Nk^2/(cB)` and the second denominator `c0*k` gives
   exactly `Nell' Ng^2/(cB Nc0^2)`. The moving `k` norm cancels before
   taking an absolute value. Every nonzero dual index in `lambda^(-4)O`
   has norm at least `1/81`, so the support bound `Ng^2>C_V B` makes the
   full reflected sum identically zero, uniformly in the fixed finite
   cusp/ray family.

The acceptance depends on retaining the whole completed `n,b` sum and the
actual transformed compact profile. It does not apply to an independently
truncated theta dyad or an arbitrary bounded coefficient envelope. Other
Ramanujan allocations have additional masks and moving twists, and are not
covered by this exact completed-series match. This review leaves their
analytic estimates and the full generalized moment open.

Final source rebinding, 2026-10-10 UTC: the reviewed manuscript is now frozen
at SHA-256 `90760815d367aa645efb2fc1e4af3f24164329989881b319c24a842be3ae0e56`.
The changes are status and the explicit qualifier that the number of terms
may depend on `k`, while the `c0`/cusp geometry belongs to a fixed finite
family and each term separately vanishes. This qualifier was checked and
agrees with the source denominator calculation. The substantive O1–O8
argument is unchanged, and the independent acceptance above remains in
force at this final hash.
