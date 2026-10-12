# Independent physical-length source and enclosure review

Scope: source/formula/parameter review, not a second full residual integration
and not a completed positivity certificate. Reviewed 2026-10-10 during the
authorized two-hour continuation. No prior-wave file was changed.

## Frozen inputs

The continuation `operators/` inputs reviewed here have SHA-256:

* `PHYSICAL_LENGTH_CONTINUUM.md`:
  `c847f1c2072d822456bde8d4fb4490deea10dba59073eadf7a1bbabb6798704a`.
* `physical_length_source.py`:
  `b15da7904f2bdf4f4bc7e68b8dfe2f1de808bb0bac47a905d684c513dba24f1e`.
* `enclose_length_residual.py`:
  `7da9c14f00654150acabd5815d49cd68ba577d3b4fc697d4f928a31a0893ecfb`.
* `enclose_length_weighted.py`:
  `aed3e21e0784f387fb371b871389514c60671bd4f29449b07791d97ab9b77b16`.
* `check_physical_length_source.py`:
  `e02c09d8ead1e300969f09b9b7f426cba77447806b7bd86c46a410223afdaa73`.

The reviewed old gamma Taylor helper remains
`118e828d8bf4cb706fd94c9d179fb8d8de88319df8b20273c4e19284175af0da`.
The wrapper hardbinds it and the old analytical upper/source-convolution
helpers, together with the new source adapter and residual producer.

## Mathematical audit

Accepted at the written, source-qualified scope. The physical interval is
`L=21/20`, `b=3/2`, and the literal source has only the prime-2 cusp because
`L<log 3`. The complete gamma and protected prime tail remain present.

I independently derived the double-integral formula and its sum-zero limit.
The latter is `L(T(alpha)+T(beta))-T'(alpha)-T'(beta)` when
`alpha+beta=0`. The ordinary Gram uses `L f((alpha+beta)L)`.
There is no missing factor of L in the Galerkin construction.

For the moving convolution, differentiating
`K_beta(t)=exp(beta t)[I_-beta(t)+I_beta(L-t)]` gives
`K'_beta=beta K_beta+W(t)-exp(beta L)W(L-t)`.
Integrating this identity gives the implemented physical F, including
both physical endpoints, its mean moment, and the exponential moments.
Integration by parts gives the cosine coefficient
`K(0)-(-1)^n K(L)-(nu+1/(4nu)) D(sin(nu t),exp(beta t))`,
where `nu=n pi/L`. The sign and the plus in `nu+1/(4nu)` are correct.
The sinh moment and its protected Gram subtraction are also correct.

The incomplete-gamma acceleration uses semantic physical frequencies;
`107 pi/L<111 pi` keeps it within the frozen helper's proven range.
Constructor ordering sets L before inherited endpoint/cache construction.
The source slab activation and all `L-t` arguments are correct.

On each checked Cauchy disk, `0<Re t<L` and `|Im t|<=.01`.
The complete gamma series is bounded by its value at zero. The retained
exponential and prime branches give `|W|<8` there. Both base paths and
the at-most-one active prime path are shorter than the stated bounds.
Consequently the deliberately enlarged
`32 exp(4+2 omega/100)` K bound and the additional 120 F bound are valid.
The cosine/sinh projection tests are bounded by 3 on those disks.

The original gamma logarithmic modulus proof is independent of the interval
length. The other literal source terms have derivative below five on the
new real interval, including the continuous prime join. Hence the weaker
new `delta(12+4 log(1/delta))` modulus is valid. Physical omissions have
length at most `L*2^-50`; all six intervals are paid. The added FF/Fp
radii `24 L epsilon` and `36 L epsilon` follow from the anchor and
variation checks. The Cauchy/Gauss error and full three-slab coverage rules
remain the previously reviewed rules, now with physical halfwidths.

The primitive line and seven removed sine constraints give kappa>=1/2
on this interval. The scalar residual cost 9/2 is consistent with this
bound. The full weighted matrix uses the essential physical Parseval
factor `2/L`, positive corrections for modes 8 through 128, and the
entire remaining tail at its inverse weight. No high cosine tail is dropped.

The weighted wrapper rebuilds the exact Galerkin coefficients and U,
checks their entire recorded ball matrices, authenticates the literal
source and runtime parameters, checks every exact panel adjacency, and
requires every shifted LDL pivot to be positive. The stale inherited
phase-8 comment in the running producer does not describe its actual
9/2 arithmetic; the new manuscript states the actual arithmetic explicitly.

## Independent small replay

Fresh activated Python normal and `-O` executions of the source controls
passed byte-identically in `/tmp/physical-length-independent-{normal,optimized}.json`.
They checked 18 complete-transform/derivative controls, 20 complete-gamma
Taylor/native controls, 35 independently derived exponential-kernel F
controls and 42 independent moment controls. The 9-dimensional projection
Gram passed directed LDL. These controls substantiate formula implementation;
the analytic budgets above were read and derived separately.

## Remaining gate

The full 636-panel R integration is the owner's run. Its completed artifact,
coverage, error totals, provenance and final weighted matrix acceptance still
need independent replay before a positivity certificate is accepted. This
review proves neither its completion nor a sign at this length. It makes no
all-window or RH claim.
