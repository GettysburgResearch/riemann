# Independent internal review of the localized zero-free consumer

Reviewer: `/root/coherent_identity`. The reviewer did not author
`DETECTOR_LOCALIZATION.md`, its checker, or its exact certificate. This
is an internal mathematical review, not external peer review or formal
verification. The reviewer also authored the separate overlap note
`COHERENT_IDENTITY.md`; that overlap is not needed for the final thin-band
consumer reviewed here.

## Reviewed versions

| File | SHA256 | Git blob |
|---|---|---|
| `DETECTOR_LOCALIZATION.md` | `aa77d6158d7997801257f947574c08b9efb3f0cfea0b971dc616289f5ce68917` | `b9a47c8abcea7f2784568b8bf70a811bd57bb814` |
| `check_detector_localization.py` | `c91b5d531dd84f7b1d5c69aa70bb1ceb43c2c83a968a9b63c0d1e9f450db00ed` | `9055ed771075e197c701f29b4d86fae1107f74e8` |
| `DETECTOR_LOCALIZATION_CHECKS.json` | `de85ea08076ae610b3885fae742b8b2412e0d4335474cd3d372397a2dc2faf14` | `a522a9279b867d2e32d1c3c2c7ceb25171b0bf03` |

**Assessment: pass as a deduction within the stated imported analytic
framework and as a conditional implication from the specified thin-band
spike count.** The spike count itself is unproved. This review does not
certify the external quasi-RH framework or assert a new unconditional
zero-free region.

## 1. Native identity and pointwise witness localization

The complete ratio return retains the finite coefficient support through
`8D`, the exact `mu(k)/Nk` weight, and the true `(k,P_u)=1` mask. Full
divisibility inversion recovers A(m) because the divisor sum of Möbius
vanishes away from the unit. The three selectors in the initial
head/small-divisor/residual decomposition sum to one before any norm is
taken. They do not imply a lower cutoff for the returned variable m.

The same-bin head estimate is used with `B=D/U^(1/100)`, giving the
pointwise exponent loss `1/800` in amplitude. With preliminary witness
and height/profile losses chosen below this fixed margin, that head
cannot supply an actual saturated inverse witness. The two alternatives
then have threshold one quarter of the original amplitude, as stated.

For the unmarked small-divisor term, the factor four in the definition
of K and the smooth factor-two support imply `Nm>2U`. The genuine
modified-coefficient expansion in the companion therefore applies. Its
two inverse factors are actual Möbius polynomials with common added
punctures, and the ordinary factor retains its original natural
presentation. The original inverse moment is not applied to an arbitrary
coefficient sequence. Its exact two-branch exponent saves `1/750`.
The row-count consequence correctly takes weight one, or a weight bounded
below on the counted class; an arbitrary vanishing weight would not
justify the count.

## 2. Marked moments and their different coefficient scopes

I checked the pinned primary source
`openai/math@1581d4cbdd69a0faf34b2089614fe2a814316a6a`,
`preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex`,
particularly `lem:marked`, `lem:plain`, and their stated coefficient and
zero-extension conventions. The local source has SHA256
`42a5ee0febca59fd1def55cfd6c6808c322ef4237d7726303ea52f711deac6a3`.

The marked inverse permits arbitrary bounded row-independent individual
prime coefficients, with capacities `b+2z<1` and `2b+8z<3`. Added
punctures in the inverse can be restored by its exact Euler expansion
without deleting or changing the original prime product. Each restored
inverse is shorter, so it retains the same strict capacity margins. This
does not move amplitudes between primitive characters.

The positive-slot ordinary fourth moment has a narrower scope. Its
coefficients, before the common mask, must be fixed finite linear
combinations from the fixed finite-ray group Theta, independent of U and
the row. The reviewed note states this restriction explicitly and does
not substitute the inverse theorem's broader coefficient class.

The ordinary theorem also excludes inducing characters in all of Theta,
not merely the principal character. I requested the now-present explicit
physical-row explanation: any prime outside the fixed set S has
valuation one through five in a sixth-power-free row, giving a nontrivial
local character that the fixed S-supported twist cannot cancel. The
S-supported sixth-power-free rows form a bounded set handled before
these asymptotic estimates. Thus this additional positive-slot exclusion
is not silently discarded.

For the low component, taking two equal ordinary factors and
`kappa=3/4` gives capacity `2c+(9/2)z<1`. Weighting the coherent
component by `|Q_z|^(1/2)` before its L4 Minkowski estimate leaves
exactly `sum |S_c^2 Q_z|^2`. The two same-bin inverse fourth powers cost
`U^(2 delta(r-c))`. Dividing by the amplitude bound yields the displayed
ordinary count line, with coefficient `4g/9`, not a factor two larger
or smaller. Products are selected for each fixed permitted length group;
the proof does not assume one product works at every c or for arbitrary
independently chosen rows. The maximum required prime lengths, `1/30`
and `231/2000`, fit within the original certified supply. The individual
ordinary slot mesh and reserved strict losses remain required.

## 3. The final primal band is an exact presentation of the same inverse

Changing the short cutoff to `alpha_*=1/250` changes the exact auxiliary
convolution, not the original inverse polynomial in the consumer. The
two cutoffs still have product `2D`, both lie below the original annulus
by a fixed power for sufficiently large U, and the same unequal-cutoff
identity applies. The old `alpha=2/125` claims remain separate.

The low, middle, and high selectors in (35) sum to one. The remaining
expression is therefore literally an original primal band with

\[
 U^{0.735}<Nm<2U^{0.773},\qquad D<NmNc<2D.
\]

No ratio selector has been reinterpreted as a primal support cutoff.
The resulting ordinary log-length range is correctly
`[0.387,0.435]+O(1/log U)` over the whole parameter interval.

I checked the endpoint lines and the exact box margins. The low,
high-short-inverse and high-long-inverse margins are respectively

\[
 \frac{23}{16000},\qquad
 \frac{371959}{307200000},\qquad
 \frac{1099}{768000}.
\]

All are strictly greater than `1/1000`; the reported residual margins
are correct. Their multilinearity and derivative signs identify the
worst rational corners, so the proof covers the entire box rather than
only sampled critical decimals. The fixed positive reserves accommodate
the source's finite mesh and the preliminary witness/profile losses.

From `M=L+F+T`, an original witness has a component of amplitude at least
one third of its threshold. The complementary component counts apply
at any fixed positive constant multiple of that threshold, so the
specific `sqrt(c)/3` definition in `(W_thin)` is sufficient. No count
independence is needed.

## 4. Conditional endpoint and full complementary coverage

The original conditional consumer's complete zero/amplitude certificate
is reused at the same native witness count. Its old short-witness branch,
the old floor below `r=29/25`, and its four detector cutoffs remain.
Thus the improved count is used only in its licensed length interval.

Outside `473/1024<=delta<=487/1024`, the pinned old endpoint certificate
already succeeds at the maximal amplitude `x=1/2`. Its proved
monotonicity retains all smaller x. In the remaining delta range, the
new certificate at `x=49/100` has strictly positive complete Bernstein
arrays on all 128 rational cells. The minimum
`799945092153101/1119744000000000000` is positive. The small-delta,
floor, small-row, distant-row and principal interfaces are preserved
from the original certificate.

The new arithmetic hypothesis is consequently needed only on the stated
box, with its source-compatible finite prime system and licensed
detector profiles. The resulting implication to
`Re(s)>0.8748856` remains conditional on `(W_thin)` and the imported
finite-order Eisenstein framework. The stated Dirichlet and zeta
consequences use the same licensed base-change factorization; no
unsupported extension of a moment theorem to another field is made.

## 5. The high-ratio representation is equivalent with a proved error

Multiplying the returned variable by the common smooth band selector
preserves the coefficient proof: on each fixed ratio dyad and k, it is
a common annular profile with bounded logarithmic derivatives. The
same-bin head bound retains its `U^(-1/800)` amplitude loss. Hence the
relation `T=H_mid+R` in (44) is exact, and its error estimate is valid
with one shared buffered height and the stated order of choices.

Expanding the full coefficient support then gives
`Nd<8U^.01` and the displayed linked range for k. The global k exponent
interval `.377` to `.435` follows from the full r and m intervals; at
each term k remains linked within `.01+O(1/log U)` to `r-log_U Nm`.
The shortness of d does not remove d=1 or introduce a new cancellation
theorem. The stated positive gap between the two old count-resource
thresholds is a resource calculation, not an actual moment lower bound.

## 6. Independent checker replay

I independently ran `python -O check_detector_localization.py`. It
passed, including:

- 1,785 coefficient returns and 90 coherent primal returns;
- 4,692 selector partitions and 1,461 support implications;
- 303 far-envelope evaluations plus the exact endpoint proofs;
- all eight marked-box and eight thin-box corners;
- 3,570 primal band partitions and 3,570 band returns;
- 1,564 linked-label support cases;
- all 128 complete Bernstein cells and the pinned producer's acceptance
  gates and negative controls.

The checker authenticates the earlier producer source by SHA256 before
replaying its exact polynomial code. It excludes that producer's
report-writing block, so the previous publication is not modified.
The newly emitted `DETECTOR_LOCALIZATION_CHECKS.json` was byte-identical
to the reviewed report.

These finite checks do not prove analytic moment hypotheses, scalar or
family caps, buffered contour arguments, or `(W_thin)`. Those limits
remain explicit in the mathematical note. Subject to its stated
premises, the localization and the conditional consumer are supported;
the decisive arithmetic estimate remains open.
