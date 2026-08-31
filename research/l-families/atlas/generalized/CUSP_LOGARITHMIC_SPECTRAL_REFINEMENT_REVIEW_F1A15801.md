# Independent review: logarithmic native cusp spectrum

Verdict: **PASS** for Theorem L at exact scientific commit
`f1a158015a400a1ba9fc36fe16639cfb5c2f7c1a`.

Review date: 2026-09-01. The reviewed theorem is the 206-line file
`fivehour-pass4/CUSP_LOGARITHMIC_SPECTRAL_REFINEMENT.md`, Git blob
`dffb7f1ab6c071c486751dc6bd77c26691356ae2`, normalized-LF SHA256
`3e9c6911431dda28b639941c9cdbd46cd68461abe66ae363c6412c9327fc674a`.
Its imported Theorem K is frozen at
`2c309f1196776575942f7f5434dff857d3a922f9`. The review branch starts from
release head `a25f4524dded2fd6d687780530d59fc91bbfc8f3`, where the theorem file is
unchanged. No scientific source was edited and no push was made.

## Mathematical audit

For every even-weight sequence with `1 <= J=o(k)`, put `nu=k-1` and
`a=4*pi*J`. The claimed bounds

    m_(k,J)+o(1) <= lambda_J(k) <= m_(k,J)+R_1+o(1)

are valid with absolute sequential remainders.

1. On `y>=1`, the radial symbol is increasing. Conditional Gamma densities
   of common shape `nu` have decreasing likelihood ratio as their rate
   increases, so every coefficient `n>=J` has radial average at most the
   rate-`4*pi*J` average. The conditioning error is genuinely absolute:
   if `p=P(Z<1)`, then

       p <= a^nu/Gamma(nu+1),
       |E[Z|Z>=1]-nu/a| <= p*(1+nu/a)/(1-p),

   while the displayed logarithmic lower-tail integral controls the log
   moment. Since `a/nu -> 0`, these errors beat every power even after the
   factor `nu/a`; `psi(nu)=log(nu)+O(1/nu)` then gives (L9) with `o(1)`.

2. The upper coefficient flag has codimension at most `J-1`. Its complete
   cusp Parseval quotient is a positive weighted average of the preceding
   conditional Gamma averages, and `|r_0|<=R_1` there. Below height one,
   `E_0` has a fixed finite supremum. Since
   `m_(k,J)=nu/(24J)-log(nu/(4*pi*J))/2+c_0 -> infinity`, the full Rayleigh
   quotient is the convex combination of two pieces each eventually at
   most `m_(k,J)+R_1+o(1)`. Decreasing-order Courant--Fischer therefore
   gives the stated upper bound at index `J`.

3. The absolute refinement of the height lower bound is sound, not merely
   relative. The bounds inherited from Theorem K imply

       (nu/J)*(1-Q(k,4*pi*J))
         <= (nu/J)*exp(4*pi*J)*2^(-k) -> 0,

   and the explicit logarithmic bound for `delta_(k,J)` remains
   superpolynomial after multiplication by `nu/J`. Hence
   `L_(k,J)=nu/(4*pi*J)+o(1)`. Jensen applies in the complete Petersson
   probability measure; its scalar function is increasing once the mean
   exceeds `3/pi`, which follows from this lower bound. This proves the
   radial estimate (L14) with an absolute `o(1)`.

4. For `H=sqrt(nu/(4*pi*J))`, eventually `H>=1`, so Parseval above `H`
   is on the full cusp rectangle. Keeping the first `J` nonnegative terms
   gives exactly

       P_f(y>=H) >= (1-delta_(k,J))*Q(nu,4*pi*J*H)

   on every unit vector of the `J`-dimensional Poincare span. Here the
   Gamma threshold/shape ratio is `sqrt(4*pi*J/nu)->0`; for example
   `1-Q(nu,x)<=exp(x)*2^(-nu)` makes the missing mass `o(1)` uniformly
   along every admitted sequence. The pointwise Fourier bound is
   `O(exp(-2*pi*H))` on the retained mass and the fixed global bound is
   paid on its `o(1)` complement. Thus (L16) is uniform on the whole unit
   sphere. The max--min form of Courant--Fischer on this dimension-`J`
   span gives the lower bound for the same decreasing eigenvalue `lambda_J`.

The review therefore finds no hidden compact-mass loss, Gamma-shape shift,
flag codimension error, or min--max off-by-one. The result leaves a real
interval of width `R_1`; it does not prove an `o(1)` two-sided remainder,
period-root motion, simplicity, or any RH/GRH assertion.

## Separate finite-certificate replay

The hardened finite certificate at exact head
`a25f4524dded2fd6d687780530d59fc91bbfc8f3` also passed a separate replay
under CPython 3.12.10, python-flint 0.9.0 and FLINT 3.6.0. All 12 tests pass
normally and under `-O`; both 256- and 512-bit fixtures reconstruct exactly
in both modes. Each replay contains 43 operator cells and 75 period cells,
with 57 lower and all 75 upper period certificates. The strict parser rejects
duplicate keys, floats/nonfinite numbers, oversized integers and type changes;
the all-Gamma finite-sum controls and directed cross-precision overlap test
pass. These finite checks instantiate the frozen analytic inequalities and
do not constitute a numerical proof of Theorem L or an infinite assertion.
