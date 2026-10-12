# Independent signed-sector kernel inertia review

Status: ACCEPTED at the fixed finite source scope of SI1–SI4. The actual
Schwartz selected-critical kernel is indefinite. The full moment remains
positive. No asymptotic moment estimate, factorable negative vector,
zero-free improvement, or RH result is established.

Reviewer: `/root/final_height_review/collision_review`, 2026-10-10,
during the authorized two-hour continuation.

What was actually run: local proof, checker and imported review reads,
with SHA-256 binding. No checker execution, fresh native replay, full
Schwartz matrix reconstruction, or numerical eigensolver by this reviewer.

## Exact reviewed identities and imported finite source

All table paths are relative to continuation `literature/`.

| File | SHA-256 |
| --- | --- |
| `SIGNED_SECTOR_KERNEL_INERTIA.md` | `07d578eb15e54e4b88dc93abc1f6e81b08b1a7e52f07c938b7ddc3122e830df0` |
| `check_signed_sector_inertia.py` | `50773ad76433ef448d6233080411a3c8d452670b1a7ccee679280c23383bc1e2` |
| `signed-sector-inertia-certificate.json` | `fda297ed5fc3435058f55fb6dbcad34114353aa635c11a1aca426bb8111a26a5` |
| `FULL_SIGNED_COMPACT_WITNESS.md` | `1c0a1718080e6f763a3531f9f9a8f8fcd31868c48d241290406fe4cef61644ca` |
| `check_full_signed_compact.py` | `ace0ec9a10deef974d3cae842590bc46c2d048e65dfa5b14b659cbc7c380dc50` |
| `FULL_SIGNED_COMPACT_WITNESS_INDEPENDENT_REVIEW.md` | `5084650971b3af4d5dbb30ed169ecc5f30a4ce463f064edb6bcca3d5ce13d008` |
| `FOURIER_COMPACT_BALANCED_TRACE.md` | `480cb96c363ddddf5d35306b0b25739c110b6f407e8101a43aaddae04605f120` |
| `check_fourier_compact_trace.py` | `dddf8f7c12fe022e54e19d9994da6092fd7a3a7e9da1d1d67b6daf6f5c27c598` |
| `FOURIER_COMPACT_BALANCED_TRACE_INDEPENDENT_REVIEW.md` | `edae9fd20fbe7afcd29d2380628c17e59b1c5ba91e4fffb193135db4d9313680` |

Imported independently replayed receipt pairs are:

* `independent-full-signed-compact-normal.json` and its `-optimized.json`
  partner: both `46e642fa1c4774f1d31166de547731762fa7f89ac3f0a3ce6b0c500f91571d93`.
* `independent-fourier-compact-trace-normal.json` and its `-optimized.json`
  partner: both `fa2e817911ebaee9411f3b617149fa55ad98e9b7abc6e604dd6b3a1d6cc6aae8`.

Their native replay and primitive source authentication are imported from
the named independent reviews, not newly performed here. The literal
PR914 sector source is `CONDUCTOR_SECTORS.md`, SHA-256
`c160bbb1b1d7c6bcc5514d496ad41f15fd17ea3d36206b0d05cfa0d7d6503983`.
Its definitions in Sections 7 and 10 were read in this review sequence.

## Source, coefficients and exact diagonal removal

The family is genuinely finite at D=30 and H=40. A fixed compact smooth
norm profile can have value one at 7/30, 13/30, 19/30 and 31/30 and zero
at every other integer-norm sample at that scale. These prime norms have
two distinct actual prime ideals each; their equal norms never identify
their ideal labels. With the trivial fixed nu, all eight source column
coefficients are -1. Every ordered pair coefficient is therefore +1,
including a repeated prime pair. This is an admissible fixed instance of
the literal inverse family, not an asymptotic prime-only substitution.

For ordered pairs alpha=(p,q), beta=(r,s), the entry uses the literal
four-slot character with its zero extensions, and the exact critical
indicator from PR914. Swapping the two sides conjugates the character
and coefficient and preserves the indicator. The genuine Phi_delta is
real and nonnegative Schwartz, so the entire row sum is absolutely
convergent and the matrix is Hermitian. Its nonunit masks are unchanged.

On a diagonal alpha=beta, each occurring prime in `(p,q,p,q)` appears
twice or four times. There is no singleton, hence g1=1 and the critical
indicator is zero. This proves all 64 diagonal entries vanish exactly.
The removal is prescribed by the existing source sector, not a freely
chosen centering. The same reasoning holds when p=q. The 64-dimensional
ordered basis has repeated pair functions, but this causes no problem
for the stated ambient-dimension spectral bound.

Because every incorporated pair coefficient is one, summing every
matrix entry is exactly the full critical R2 of the frozen finite family.
There is neither an omitted ordering factor nor a new coefficient class.
The full witness enumerates all 4,096 tuples, applies its critical test
before character grouping, and retains all 3,696 critical tuples and
their principal masks.

## Paid genuine Schwartz form and quantitative inertia

The imported directed compact-Fourier form is
`8852.5068916015827910965314252477411701769971627151`
with printed radius `1.51e-47`. The same source mollification with
delta=1e-12 changes the full critical form by less than .35. Its complete
budget counts every critical tuple, at most two mask divisors, primitive
norm at least seven, and the complete odd-denominator dual norm box.
The strict Fourier-support gap excludes new norm samples. Thus this is
a payment for the entire form, not a finite-row approximation to Phi_delta.

The inertia checker implements a rational upper bound for that analytic
budget using `sqrt7>2645/1000`:

    E_full = 3696*2*40*34693*90*1000/(2645*10^12)
           = 72126747/206640625 < 7/20.

Subtracting this bound and the imported directed radius still gives
`1^* M 1 > 8852`. The proof's use of the genuine Schwartz companion is
therefore source-qualified. No individual Schwartz matrix entry is
required numerically for the following exact spectral argument.

For any Hermitian n-by-n matrix with zero trace and
`1^* M 1 > B > 0`, the all-ones vector has norm squared n, so
`lambda_max>B/n`. The other n-1 eigenvalues sum to
`-lambda_max<-B/n`; at least one is below `-B/[n(n-1)]`.
For n=64 and B=8852, this proves precisely

    lambda_min(M) < -8852/(64*63) = -2213/1008.

It also proves indefiniteness without computing an eigenvector or any
matrix entry. Positivity of the full moment is consistent with this
negative spectrum because M is the selected critical kernel, not that
full moment's Gram matrix.

## Leading face and its normalization

Use the 56 ordered pairs with distinct primes and retain an entry only
when its four ideal labels are distinct. This restriction is symmetric
under exchanging the sides and has zero diagonal. Every such tuple has
four singleton primes; its smallest possible singleton norm is
`7*7*13*13=8281>40`, so all these leading tuples remain critical.
The surviving 1,680 ordered entries are exactly the fully coprime
leading face; summing them introduces the same `(2!)^2` ordering
multiplicity already present in the imported balanced-face formula.

The imported compact leading form is
`3916.7665189976260644009926745000130837431873375545`
with printed radius `2.52e-47`. Its complete mollification budget is
below .001, so the genuine Schwartz form is greater than 3916.
The same trace-zero spectral argument with n=56 gives

    lambda_min(L) < -3916/(56*55) = -979/770.

The result concerns this precisely restricted face, not an inference
from its sign to the sign of the remaining critical contribution.

## Checker audit and exact remaining boundaries

The inertia checker directly binds the full and leading source proofs,
source checkers, the full independent review and both two-mode receipt
pairs. It parses the printed real balls with exact fractions, pays the
full Schwartz error rationally and imports the separately paid leading
error. It requires the complete physical tuple count and source scales.
These are imported-source gates, not new primitive computation.

Its separate auxiliary spatial-disk control reconstructs all eight prime
residue fields from quadratic roots and discrete logs and every nonzero
Eisenstein lattice row of norm at most 40. Its coordinate bound follows
from `N(a+bomega)>=3a^2/4` and the corresponding bound for b. Character
tables retain the nonunit zeros. The critical classifier uses singleton
multiplicities and same-side doubles, with the exact integer inequality
`Ng1^2*Ng2>H^2`; it does not classify solely by residual exponent.

The code constructs the full 64-by-64 exact auxiliary matrix and sums
the filtered 56-pair leading entries. It checks Hermitian symmetry and
zero diagonal for the full matrix and records a full-kernel negative
two-by-two minor, determinant -252. The leading symmetry and zero
diagonal also follow from its symmetric four-distinct filter. The
auxiliary forms 1176 and 456 concern the compact spatial disk, not the
compact-Fourier test or its Schwartz companion. The actual-source
inertia is obtained from the imported complete forms and analytic error
payments; the actual Schwartz matrix was not numerically reconstructed.

A PSD-kernel entry inequality would force every entry of a zero-diagonal
matrix to vanish, contradicting either positive form. This rules out
that particular automatic Cauchy adapter for the selected kernels.
It does not rule out a signed trace bound, a higher-correlation estimate,
or a bound restricted to the actual factorable one-column source weights.
An arbitrary negative eigenvector in ordered-pair space has not been
shown realizable by those weights. No full-moment indefiniteness,
asymptotic obstruction, or new source moment theorem follows.
