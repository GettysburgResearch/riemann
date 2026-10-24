# Independent frozen review: full Möbius cubic moment

Date: 24 October 2026. Reviewer: `cubic_moment_review`, independent of the
authors of the reviewed notes. This is an agent mathematical review, not
external peer review or formal verification.

## Frozen source and verdict

The reviewed mathematical source is
[`GettysburgResearch/riemann@f11e86684905c6417683a9f45ac75c223da6a162`](https://github.com/GettysburgResearch/riemann/tree/f11e86684905c6417683a9f45ac75c223da6a162/standalone/2026-10-23-structured-moment-gains/third-pass),
under `standalone/2026-10-23-structured-moment-gains/third-pass/`.

**Verdict: no blocking gap found in the full-moment deduction, the Möbius
exceptional-mean adapter, or its quantitative refinement at their stated
scope.** The full theorem is supported conditional on its explicit
`ZF_beta` hypothesis and pinned analytic inputs. The exceptional ordinary
character mean uses the pinned analytic inputs but no zero-free premise.

I fetched the following six files directly at the frozen commit, computed
their SHA256 and Git blob hashes from the returned bytes, and verified
byte equality with the assembled local files whose mathematics I reviewed.

| File | SHA256 |
|---|---|
| `FULL_MOBIUS_CUBIC_MOMENT.md` | `2de89fd74098dd0b6c952c2f771c1c291553920d23f34d161aef3ee76877b66c` |
| `MOBIUS_EXCEPTIONAL_CUBIC_MEAN.md` | `72e750857893d789f3478a31ed9c2ff2ad49cc2fc5b72d87621f94789bbe434d` |
| `QUANTIFIED_MOBIUS_EXCEPTIONAL_MEAN.md` | `55943b6fc23c49e8ce0137758da6d579c9bd41193772994fe76ee8d58b2b6297` |
| `SOURCES.json` | `bdc5978ef3462998a83f96fc95d0eff3ce49a4ea2a1bb8d6e83737a505d312da` |
| `check_cubic_arithmetic.py` | `8e2412ea3a2a62d49ba663a060c8a484c3840d05d70b969620644e1a9b566262` |
| `cubic_arithmetic_report.json` | `e857bb6e832f76cc587ab719a407b649e95ae3c56daf3db1d514b69b78a592f0` |

The supported full estimate is

\[
 \mathcal M_\theta(A,B)
 \ll X^\epsilon[AB+\mathcal QX^{-\eta_{\rm full}}],
 \qquad X=AB,\quad H=B^2/A,\quad
 \mathcal Q=ABH^{1/3},\quad A\ge B\ge2,
\]

or, with normalized columns,
\(\ll X^\epsilon[A+X^{2/3-\eta_{\rm full}}]\).
The initial punctures, finite ray character, angular order and smooth
test data are fixed. The sum includes all rows and all Poisson frequencies.
The exponent \(\eta_{\rm full}>0\) is existential. The separate explicit
values \(\delta=10^{-9}\), \(\eta=10^{-6}\) concern only the exceptional
ordinary cubic character mean.

## Imported assumptions and authenticated primary source

The full theorem assumes a common zero-free half-plane
\(\Re s>\beta\), \(1/2<\beta<1\), for primitive finite twists of the fixed
angular type, with the stated standard Hecke continuation, functional
equation and conductor-uniform polynomial growth. Complex conjugation
supplies the opposite angular orbit. PR1012 is an optional proposed
supplier of this hypothesis; this review does not certify its proof.

The analytic imports are the ordinary and cubic large sieves, their stated
extensions, the literal uncorrected Poisson formula, full smooth Hecke
duality, the off-diagonal Gram estimate and the exceptional large-value
argument in `openai/math@1581d4cbdd69a0faf34b2089614fe2a814316a6a`.
Their exact paths and roles are recorded in the frozen
[`SOURCES.json`](https://github.com/GettysburgResearch/riemann/blob/f11e86684905c6417683a9f45ac75c223da6a162/standalone/2026-10-23-structured-moment-gains/third-pass/SOURCES.json).

I independently fetched and authenticated all four load-bearing TeX files:

| Source | Exact remote SHA256 |
|---|---|
| `dispersion.tex` | `9a04b892feb99a79ec4e825bcd5096d3adb994c53d539c41d2da35f0a77f317c` |
| `dual.tex` | `1209fd17cee79f4a21b71d66d3d8b60b210216fa783ec555959d2ebff2fba483` |
| `background-type1.tex` | `1c7be908c862dc440772964cfdd59e095e7b0f079cec11d99f5c7a9644198dd1` |
| `angular.tex` | `f14a7c1c4f0b19b70d6705c8a2adcb658bfbc77814edb61cd57edb2465f38510` |

Each original local TeX copy equals the corresponding remote bytes plus
one final newline. The frozen notes correctly identify the exact remote
hashes; no mathematical source discrepancy was found. I reconstructed
the imported argument to the scope needed here, without claiming to
re-prove the underlying Heath-Brown theorem or the entire source paper.

## Mathematical checks

1. **Uniform reciprocal estimate.** A zero-free disk chain bounds the
   analytic logarithm by \(O_\delta(\log(qT))\). Three-lines applied to
   that logarithm with a Gaussian, between an interior line and an Euler
   line, gives \(O((\log(qT))^c)\), \(c<1\), and hence the required
   arbitrary \((qT)^\epsilon\) reciprocal bound. The principal pole
   removal and deleted Euler factors are valid. This uses the common
   orbit hypothesis, not uncontrolled constants for separate members.

2. **Exact arithmetic and masks.** The Poisson formula is the source's
   uncorrected formula with \(d=1\). The \(m\mid f\) inversion, the
   \(l\)-mask and
   \(\mu(fln)=\mu(fl)\mu(n)\mathbf1_{(n,fl)=1}\) retain the original
   zeros. The displayed expression is extended before the formal
   coprimality inversion; no primitive Poisson identity is asserted for
   artificial pairs. The exceptional unit pair is explicitly subtracted
   at cost \(O(BX^\epsilon)\). The original diagonal remains present.

3. **Complete short-\(H\) branch.** Retaining Schwartz decay gives an
   \(O(H')\) nonzero-frequency sum even when \(H'<1\). The exact scale
   calculation is
   \[
   \frac{AF}{MB}\frac{HM}{F^2}
       \left(\frac B{FL}\right)^{2\beta}
   =B^{2\beta+1}F^{-1-2\beta}L^{-2\beta}.
   \]
   Both ideal sums converge, with divisor losses for \(m\mid f\).
   Thus this branch is bounded by \(X^\epsilon AB\) when
   \(H\le B^{2-2\beta}\), including principal twists.

4. **Large-frequency assembly.** The complementary range has
   \(B>X^{1/(1+2\beta)}>X^{1/3}>X^{8/25}\), so the imported scale
   restrictions hold. Large common factors use only divisor bounds and
   positive sieve forms. The remaining sieve inequalities leave exactly
   the stated two exceptional configurations. The benchmark weights
   \(k^{1/3}M^{-2/3}F^{-5/3}L^{-2}\) are summable.

5. **No lost conductor at the exceptional handoff.** The frozen full
   proof includes the added calculation after equation (18). With
   \(Y=B'\), \(c=8/25-2\delta\), and endpoint radius \(\rho\), it gives
   \[
   Nv\le Y^{4\delta/c},\qquad
   Ne\ll Y^{\rho+(7\delta+2\delta')/(3c)}.
   \]
   I checked these bounds from
   \(J\le X^{2\delta'}LY\) and \(PQ_0^2\ge Y^{1-3\rho}\).
   They retain \(f,l,j\) and permit a fixed-neighborhood choice of the
   adapter parameters, with room for the fixed initial puncture.

6. **Möbius adapter and quantitative margins.** The finite convolution
   identity is exact and distributes through multiplicative twists and
   zero masks. It leaves three factors; only the full smooth factor can
   have exponent tending to one. The functional equation's root number
   and conductor phase stay outside the dual polynomial. The remaining
   copied-factor and Gram arguments use common divisor-bounded
   coefficients, including fixed angular/ray twists. In the quantitative
   proof I checked the dominant-factor exponents \(349/150\) and
   \(341/150\); the choice of at most 28 copies; the Gram gaps exceeding
   \(0.03\) against \(66\kappa=0.0066\); and the second-endpoint
   contradiction \(v\le47/60+3\kappa<5/6-\kappa\).

## Computation actually reproduced

After inspecting the source, I ran, from the third-pass directory:

```text
python3 -I -S -B check_cubic_arithmetic.py
python3 -I -S -B -O check_cubic_arithmetic.py
```

Their stdout is byte-identical to each other and to the frozen report.
The report counts 943 arithmetic checks: 408 Gauss checks at
\(p=13,37,61,73\), and 535 checks in the finite four-prime ideal monoid
with norms \(7,7,13,19\) at six cutoffs. Six further identity-ideal sanity
assertions are executed outside that counter. The arithmetic is exact
integer cyclotomic/monoid arithmetic.

This verifies the stated finite identities and rejection of the
square-index substitution. It does not certify the full Poisson formula,
an analytic character mean, a zero-free region or an infinite theorem.

## Remaining boundaries

No first blocking gap was identified within the reviewed deduction.
Application of the full theorem still requires its zero-free hypothesis
to be established or adopted with its source qualifications; adopting
the proposed PR1012 input does not independently certify that input.
A smaller global boundary additionally requires a separate consumer for
the physical sextic inverse complement, with its actual characters,
completion factors and parameter range; the physical short-row problem
can have \(B>A\). This packet does not supply that consumer.

The review does not certify PR1012's boundary proof, the complete source
first-moment theorem, the other comparison sources in the manifest, or
a new global zero-free boundary. It does not extend the result to
arbitrary moving initial punctures, unbounded angular order or an
arbitrary-coefficient operator norm. RH remains unproved.

## Supplementary frozen reviews and integration record

This section is recorded by the integrating agent. The preceding review
is the independent `cubic_moment_review` submission, whose original
SHA256 is `5adc8a7bdaa7fc63442d60f4a77854844addc35bd9708edc46bb5c067836ea61`.
All supplementary verdicts below bind to the same mathematical commit
`f11e86684905c6417683a9f45ac75c223da6a162`.

### Repository comparison and a second full-moment check

Reviewer `new_work_bridge` fetched and authenticated the frozen README,
orientation audit, full-moment proof and source manifest. It found no
new mathematical or factual blocker. It independently checked the
fixed-neighborhood bounds for `Nv` and `Ne`, the full moment's stated
scope, and the PR1019 comparison. It verified all eight manifest entries
against the previously fetched source bytes in SHA256 and Git blob hash.

The review explicitly retained the distinction between PR1019's
projected inverse vector and its uncontrolled complementary projection.
It also checked the physical quartic `k^3` mean's annular cost and the
proposed status of PR1012's all-unitary input. The reviewer authored the
orientation note; its check of that note is an author check. The separate
independent orientation review below supplies that part of the review.

The two additional mathematical-commit files, beyond the six in the
first table, have these authenticated hashes:

| File | SHA256 |
|---|---|
| `README.md` | `c2a377db47db76a092c9eda7fd5a008e822d269c50f79841e381686d077238dc` |
| `CUBIC_FOURTH_POWER_ORIENTATION.md` | `e27fb4fa560e473bb954b178cf3a8c3cea42aa3c37403f8b8a94d91f6e484bd6` |

### Independent physical-orientation review

Reviewer `sparse_quartic` independently fetched the frozen orientation
audit and arithmetic checker, recomputed both Git blob identities and
SHA256 hashes, and found no blocking issue in their stated scope. Its
original review report has SHA256
`73f6aab35dd366c454f9b6c656cd1c759269127cdfe8f3c67dad9b3a380d973d`.

It reconstructed the first-Poisson sign and the exact fourth-power
sextic realization, including the fixed `chi_c(-1)` factor. It checked
lift summation at prime powers, the local state transitions `0 <-> 2`
and `1 <-> 1`, and the displayed primitive inversions. The conductor
test follows conditionally from its expressly assumed geometric
functional equation: the comparison exponent is exactly `-1`, and
under the stated unitarity hypotheses the reflected state-two branch
retains `q^(4-4u)`. This is not a proof of that geometric interface or
an exclusion of every alternative global representation.

The reviewer also replayed the exact checker, obtaining the 943 counted
arithmetic predicates and square-substitution rejection counts
`8,24,40,48`. It explicitly excluded the analytic functional equation,
the complete prime-power local argument and infinite theorems from the
computer check's scope.

This reviewer authored the quantitative exceptional-mean appendix and
does not independently review its own appendix here. The first review
above supplies the independent review of that appendix.

### Commit discipline

The mathematical commit adds eight files under `third-pass/` and does
not change either earlier pass. This review-only followup adds only
`third-pass/REVIEW.md`; it leaves every reviewed mathematical byte
unchanged. The PR remains a proposed source-dependent research packet.
No review establishes the missing sextic inverse consumer or changes
the source-qualified numerical zero-free boundary.
