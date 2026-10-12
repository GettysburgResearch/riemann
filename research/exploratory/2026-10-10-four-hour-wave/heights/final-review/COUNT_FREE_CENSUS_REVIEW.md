# Independent review of the count-free complete Xi census

Status: ACCEPT at the exact source-qualified finite scope below, after full
mathematical and source/code review and independent native guard replay.
Scope: actual `Xi(z)=xi(1/2+iz)`, the complete classical strip and even
Hadamard product, imported authenticated original Hardy-Z endpoint signs,
and directed Gamma/zeta arithmetic. Complete simple real censuses through
2048 and 2240, and their finite horizontal full-depth companion columns.
This does not prove RH or extend the census to 8192 without a count input.

The reviewed proof is
`xi/outer-ray/COUNT_FREE_CENSUS_RECOVERY.md`, SHA-256
`8b05e1b47a7cc423083fed2817813a5f20586cafc9015626815adc095498b9ce`.
The reviewed checker is `xi/outer-ray/check_count_free_census.py`, SHA-256
`d559d6554b91307ef169e5cb1f501ae12791ea636c0e9fa32f89203622d3cf3e`.
Its accepted `count_free_census.json` has SHA-256
`ce21c175914c1e1d3ad049a8b67e6528ae2f72baed309b4719c1ca8de48a7832`.
This is an exact-file review in a shared exploratory checkout. The root
agent alone supplies the eventual frozen Git commit identity.

## Mathematical findings, CF1–CF10

1. **Complete positive theta source and zero-free disk, CF1–CF5.**
   THEOREM.md uses the correct actual source normalization. Its theta
   kernel has summands
   `(4*pi^2*n^4*exp(9u/2)-6*pi*n^2*exp(5u/2))*exp(-pi*n^2*exp(2u))`,
   and the formula is `Xi(z)=2*integral_0^infinity Phi(u)cos(zu)du`.
   Each summand is positive for `u>=0`; its double-exponential decay
   justifies every exponential moment and the required dominated power
   series. Independent integration by parts with
   `G(u)=exp(u/2)*sum exp(-pi*n^2*exp(2u))` and `G'(0)=-1/4`
   gives `2 integral (G''-G/4)cos=1/2-2(z^2+1/4)integral Gcos`,
   the completed-xi Mellin identity. This also authenticates the factor
   two in the inherited source formula.

   The absolute cosine series inequality is valid for every complex
   argument: `|cos(zu)-1|<=cosh(|z|u)-1`. Therefore CF2 holds on the
   whole closed disk, with no real-axis-only substitution. At `B=11/2`,
   `Xi(-iB)=xi(6)=2*pi^3/63`, because
   `6*5/2*Gamma(3)*zeta(6)/pi^3=2*pi^3/63`.
   The native strict seed and exact rational comparison give
   `xi(6)<2*Xi(0)`. The triangle inequality proves zero exclusion on
   the entire closed disk. With the complete strip `|Im rho|<=1/2`,
   every source root has `|Re rho|>sqrt(30)>5`.

2. **One selected occurrence per bracket, CF6.** The 8049 intervals are
   strictly disjoint and positive. Each authenticated actual Hardy-Z
   sign crossing supplies at least one real Xi zero. No initial root
   uniqueness, simplicity, or finite completeness is used. Choosing
   one occurrence and its even reflection removes exactly one opposite
   pair from the complete even product. If its analytic multiplicity
   exceeds one, the extra occurrences remain in the residual. The
   paired genus-zero product has no nonconstant exponential because
   the entire function in `z^2` has order below one. Thus
   `-3*[z^6]log(F/F(0))` is the complete inverse-sixth sum, and its
   subtraction by the selected real roots gives exactly CF6. Absolute
   convergence follows already from the inverse-square product sum.

3. **Global positive angular projection, CF7–CF8.** Every remaining
   right-half-plane root satisfies `|arg rho|<atan(1/10)`. The angle
   after multiplication by six is below `3/5<pi/2`; no cosine branch
   crosses zero. The exact projection is
   `c=851499/1030301>0`. Every individual root contributes
   `Re(rho^-6)>=c*|rho|^-6`, and all remaining analytic multiplicities
   are nonnegative integers. The residual is real because the retained
   source and the selected real roots preserve conjugation. This
   positivity applies to the complete unselected source, including
   any unknown low root and every extra selected multiplicity. It
   does not rely on the older census assertion through 8192.

4. **Complete and simple census, CF9.** If one remaining root had
   `0<Re rho<=H`, its absolute sixth inverse power would be at least
   `(H^2+1/4)^-3`. That root alone violates the strict upper guard;
   every other residual contribution is nonnegative. Conjugate
   nonreal roots would give two contributions, but the weaker single
   occurrence guard suffices. Extra occurrences of a selected root
   below or at H are excluded in exactly the same way. The exact
   retained interval geometry has no boundary intersection at 2048
   or 2240, so all selected roots are unambiguously above or below
   each boundary. The argument includes a hypothetical zero exactly
   on the height boundary. Evenness supplies the negative census.

5. **Column composition, CF10.** I read the complete inherited proofs
   in CENSUS_LOCALIZATION.md and CENSUS_FULL_COLUMN_SECTOR.md, rather
   than taking their actual-8192 corollaries as hypotheses. Localization
   uses complete paired polynomial approximants, conjugate-pair
   logarithmic derivative positivity, Gauss–Lucas, Hurwitz and the
   positive source moment anchor. Its real simplicity induction keeps
   the smaller ranges under differentiation. The full column then
   uses the complete derivative product, the exact complex Laguerre
   expression `2(Im q)^2-Re q'`, and all three positive coefficients
   in `Re(i E conjugate(E'))`. These proofs need only a complete
   simple real census at their supplied R, so the newly recovered
   census supplies R=2048 or R=2240 directly. The historical-count
   corollaries at R=8192 are unused. At `A=1/2`, the precise allowed
   integer range is `0<=r<=2H-3`, with
   `|T|<H-(r+2)/2`, every `lambda>0`, and every `y>=0`.

## Native computation and imported sign facts

The new checker constructs `s=1/2+i*z` in directed `acb_series` arithmetic,
evaluates the actual Gamma/zeta completed expression through degree six,
and forms `(xi/xi[0]).log()`. Its constant seed is strictly nonzero; the
actual analytic parity/reality identifies the even real coefficient.
Every finite inverse-sixth term is evaluated over the full exact dyadic
interval, with outward ball rounding. No root midpoint replaces that
interval. Dependence between Taylor coefficients or selected roots cannot
invalidate the enclosure: ordinary ball overestimation contains every
allowed combination. The exact rational upper endpoint is the guard input.

The original sign derivation is separate from zero counting in
check_native_slab.py: its Hardy expression is
`exp(i*(Im logGamma(1/4+i*t/2)-t*log(pi)/2))*zeta(1/2+i*t)`.
On the real axis, actual Xi equals this Hardy Z times the nonzero real
factor `-(t^2+1/4)*pi^(-1/4)*|Gamma(1/4+i*t/2)|/2`; opposite endpoint
signs therefore supply actual real Xi zeros. The endpoint loop itself
uses no complete count. The old checker also calls `zeta_nzeros` and
makes additional uniqueness/completeness conclusions, but those claims
are unnecessary for its independently calculated strict signs.

The prefix checker similarly evaluates all 222 strictly refined endpoint
signs by the direct Hardy expression. It also contains a complete-count
call and tail-moment conclusions, which are unused here. Strict nesting
alone does not imply an unproved unique root; the new proof chooses its
occurrence inside the refined sign interval directly. This review separately
replayed all 222 refined endpoint signs without any zero-count call.

The 16098 original endpoint evaluations are imported at their earlier
native replay scope and were not duplicated in this review. All original
and refined interval geometry was independently checked. Direct source
hash maps from both imported receipts and the new receipt were verified,
including their producer/checker bindings. The current native extension
and FLINT/GMP/MPFR binaries agree with the new receipt's hashes. Hash
agreement authenticates source identity, not the analytic validity of an
infinite product or an imported mathematical theorem.

## Exact replay and outcome

I independently ran the owner checker in normal and optimized Python,
with fresh output paths under `/tmp`. Both passed and were byte-identical
to the accepted owner receipt, with SHA-256
`ce21c175914c1e1d3ad049a8b67e6528ae2f72baed309b4719c1ca8de48a7832`.
The independent audit in [audit_count_free.py](audit_count_free.py) also
checks all transitive receipt direct-source hashes, exact angular projection,
strict residual guards and interval census sizes, and directly replays all
222 refined signs without counting. Its normal and optimized receipts
record those independent finite checks; both modes share the same native
arithmetic backend.

| Height H | Complete simple positive roots | Exact guard ratio, rounded for reading | Maximum r |
| --- | ---: | ---: | ---: |
| 2048 | 1561 | 0.5736846361 | 4093 |
| 2240 | 1739 | 0.9821585521 | 4477 |

Only the exact rational guard ratios in the owner and independent receipts
are acceptance predicates. The rounded values in this table are descriptive.

Smallest remaining gap at the accepted finite scope: none found, conditional
on the named classical positive-theta/product/strip results and imported
original strict endpoint-sign facts with their directed native contract.
This review does not rerun the original 8049 sign pairs or historical
Gram/Rosser counting verification, supply a different arithmetic backend,
prove global real zeros, or approve integration of this exploratory packet.
