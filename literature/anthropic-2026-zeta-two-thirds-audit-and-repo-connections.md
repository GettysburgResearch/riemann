# Anthropic/Claude 2026 Riemann-zeta two-thirds theorem — technical audit and connections to the live repository

Status: **LITERATURE / CROSS-FERTILIZATION NOTE — NOT AN RH CLAIM**  
Authoring agent: `gpt56-pro-09-w`  
Date: 2026-08-10  
Primary sources:

- Anthropic research page: `https://www.anthropic.com/research/riemann-zeta`
- paper: *More than two-thirds of the zeros of the Riemann zeta function are on the critical line*
- condensed informal note supplied with the paper
- 95-page coordination transcript supplied by the user
- formalization repository: `https://github.com/anthropics/zeta-23-lean`

## 1. What Claude actually proved

The work is a genuine unconditional theorem, not an RH proposal:

1. more than two thirds of the nontrivial zeta zeros lie on the critical line;
2. more than one half are simple;
3. more than five sixths are distinct;
4. an optimized compact window improves the headline proportions numerically.

The argument compresses the Weil form to a finite Gabor/Fejér test space. In the zero decomposition:

- each critical-line zero contributes a positive rank-one block;
- each functional-equation pair off the line contributes an indefinite block of signature `(1,1)`.

The prime side computes the trace and Hilbert–Schmidt data unconditionally. The key rank–trace inequality then extracts a lower bound on the rank of the positive on-line part while paying only for the positive/negative inertia of the off-line blocks.

This is scientifically stronger than any unreviewed RH architecture in the repository because it already yields a new unconditional theorem and has a formalization. The repository has broader and in places more ambitious structural reductions, but those do not outrank a verified theorem until their load-bearing steps pass review.

## 2. The methodological breakthrough

The most reusable idea is not the numerical constant `2/3`. It is:

> Do not force an indefinite object to become positive if the consumer only needs a weaker inertia statistic.

Several failed Claude routes attempted:

- direct negative-index counting;
- blockwise positivity;
- higher moments beyond the available bandwidth;
- stronger local diagonalization of off-line pairs.

The successful route retained the signature-`(1,1)` blocks and designed a linear rank–trace inequality which only consumes the spectral information actually available.

This is exactly the correct correction to the live Q4 frontier. PR #350 had promoted full polarized jet-matrix positivity to the synthesis interface. PR #357 already imported Claude's principle and reduced that to one negative eigenvalue / determinant defect. The present continuation goes further: **aggregate before paying the inertia defect**, so the unknown current itself strengthens the positive determinant and disappears from the bound.

## 3. Why Claude's method does not prove RH

The paper is intentionally degree-one/bandwidth-limited.

The unconditional prime-side input controls trace and second moments on a finite test space. Higher-moment attempts run into support restrictions and unavailable arithmetic correlations. The method therefore proves a sharp positive proportion but does not supply a mechanism forcing every off-line pair to disappear.

The coordination transcript is unusually valuable here. It records that many seemingly stronger approaches failed because they:

- required bandwidth beyond the unconditional prime-side range;
- treated near-line off-line pairs as uniformly coercive, although their bad eigenvalue can degenerate;
- silently replaced an indefinite pair block by a positive surrogate;
- inferred global information from a finite-dimensional compression without a matching limit theorem.

These are the same failure modes repeatedly encountered in the repository's prolate, Selberg, carry, and Q4 programmes.

## 4. Exact connection to the Q4 two-state ledger

The corrected Q4 relative curvature is two dimensional. In centered coordinates it has the form

\[
K_e=
\begin{pmatrix}
R_e&-C_e/2\\
-\overline{C_e}/2&|D_e|^2
\end{pmatrix}.
\]

PR #357 proved

\[
\det K_e=R_e|D_e|^2-|C_e|^2/4
\]

and reduced full positivity to one square-versus-reserve defect.

The new observation in `L-90304` is that the physical theorem never needs to pay these defects row by row. For a nonnegative aggregate,

\[
\overline K=\sum_ew_eK_e,
\]

write

\[
A=\sum w_eR_e,\qquad
F=\sum w_e|E_e|^2,\qquad
U=\sum w_e\Theta_e.
\]

Then, whenever `A>F`,

\[
\operatorname{tr}(\overline K)_-
\le
\frac{|U|^2}{4(A-F)}.
\]

The complete RH-sensitive current energy cancels from the right side.

On the physical compact-source block:

\[
A\gg J,\qquad
F\ll J^2e^{-J},\qquad
U\ll J,
\]

so the bad spectral mass is only `O(J)`. This is precisely the polynomial inertia ledger required by the coefficient-one Q4 recurrence.

Claude's conceptual move therefore does more than weaken a matrix PSD condition: after physical aggregation it appears to close the arithmetic defect estimate itself.

## 5. Other connections to repository routes

### 5.1 Prime endpoint / annular filters

Claude's finite Gabor compression suggests treating the factor-64 annular prime endpoint as a finite matrix problem with:

- on-line rank-one contributions;
- explicit off-line pair blocks;
- prime-side trace/Frobenius moments.

This may produce unconditional density information for the annular statistic even if its eventual sign remains RH-equivalent. It is a publishable intermediate target independent of the Q4 route.

### 5.2 Carry / SHARP

The two-low-row zero-safe scalar is one-dimensional and therefore cannot benefit from inertia directly. But the complete Pascal Green state is naturally matrix-valued after keeping several low rows. Claude's lesson suggests searching for a rank–trace inequality on that low-row matrix rather than proving coefficientwise SHARP positivity.

### 5.3 Balanced Type II

The reflected Selberg packet route repeatedly tried to prove every terminal packet positive. Claude's result suggests a weaker target:

- retain the complete signed balanced block;
- bound its negative index or total negative spectral mass;
- use the final scale recurrence only on the positive rank/trace statistic it consumes.

This may avoid the impossible packetwise positivity theorem.

### 5.4 Prolate/CCM

Claude's proof reinforces the repository's existing firewall: a finite compression can prove a positive proportion theorem without approaching full RH unless the limit interface is separately controlled. Any prolate claim must state exactly which inertia statistic survives the cofinal limit.

## 6. Coordination lessons worth importing

The 95-page transcript documents a productive workflow:

1. maintain a theorem ledger and a separate idea ledger;
2. assign independent agents to falsification, not only construction;
3. test every candidate on model worlds:
   - Davenport–Heilbronn-type functional equations;
   - Epstein/automorphic analogues;
   - Beurling systems with planted off-line zeros;
   - finite fake-Weil polynomials;
4. preserve failed paths with exact failure reasons;
5. formalize the finite linear algebra early;
6. ask which invariant the final consumer actually needs before proving a stronger local theorem.

The repository already does much of this informally. The Claude transcript validates the practice and suggests making the model-world mutation suite mandatory for every future RH proposal.

## 7. Formalization import

The Lean repository is useful even beyond the two-thirds theorem. High-value reusable components include:

- finite Hermitian inertia and rank–trace inequalities;
- block matrix decompositions;
- exact trace/Frobenius identities;
- Weil explicit-formula normalization;
- finite Gabor/Fejér test-space bookkeeping.

The new aggregate theorem `L-90304` is elementary enough to formalize immediately and would make a good first OpenAI-side formal artifact.

## 8. Honest competitive assessment

Anthropic has not proved RH. It has produced a serious new unconditional theorem with a formal proof package.

The repository's strongest advantage is breadth: it has exact source transformations, carry identities, two-state Q4 geometry, annular criteria, Brownian formulations, and multiple adversarial firewalls that are not present in Claude's paper.

The repository's weakness is verification debt. Many claims are still `PROPOSED` and several earlier "final" steps were later corrected.

The proper competitive response is therefore not to claim a larger theorem prematurely. It is to use Claude's strongest idea to remove one genuinely open matrix defect, emit a reviewable proof packet, and force the next reviewer to attack a concrete complete composition rather than an unnamed gap. That is the purpose of `L-90304`, `L-90305`, and `T-90302`.
