# Review, provenance, and limits

## What was actually attempted

The aim was a direct multiplicative proof of the RH-facing signed norm estimate. The candidate inequality was nonnegative correlation at each new prime, so that only the summable diagonal factors remained. The exact three-prime calculation falsifies that candidate on the genuine Mobius vector. The full PNT argument then proves that the unstopped normalized energy does not merely lack a proof of boundedness: it diverges with the logarithmic asymptotic in EP11.

The source-correct repair is to keep a physical horizon and its lost-boundary term. The resulting identity is exact. Its collective signed lower bound remains open. This is not claimed as a completed improvement to a known RH-sensitive arithmetic estimate.

The Euler-product family is distinct from all of the following: a raw integer cutoff, a finite prime cutoff of xi's logarithmic derivative, the full infinite Mobius source, and an exact finite-dimensional compression of a full-source operator. The proof distinguishes them throughout. All three original routes remain open research programmes; this pass adds no new moment or Hardy-matrix positivity certificate.

## Repository sources read or consulted

1. PR #793 metadata and changed-file list at head `c4fedfcebf5226915969610281c650f452844fd8`.
2. `AGENTS.md` at that head; blob `be9b5255e6108096450bfd63d8f04a7e9cec580a`.
3. `pass5-faithful-source/SOURCE_COMPILER.md` at that head, read in full. Its certified arithmetic-jet algorithm is context, not a proof input for EP1--EP6. Its implementation and certificate were not independently rerun in this pass.
4. `pass5-sharp-arithmetic-tail/PROOF.md` from the supplied author archive, also present in the published filename list. Its uniform integer-tail result is preserved, not overwritten; the current proof does not require that theorem as an input.
5. PR #790 current summary, at head `513d8f206bb597747afcb7a7410cdf768519d548`. Only the summary was newly read. Its three-sparse positivity and signed-block theorems are not imported into the present argument.
6. A targeted PR search found #660's free-labelled/physical-energy distinction and related #757 and #403 programmes. Their PR descriptions were contextual overlap checks, not independently reviewed theorem dependencies.

No comprehensive repository archaeology, parent broad-suite replay, or claim of priority over other branches was made.

## External primary sources

- NIST DLMF 27.4, Euler products and Dirichlet series: https://dlmf.nist.gov/27.4 . This supplies standard conventions for the finite/infinite Euler products and Mobius Dirichlet series; the finite identities in the proof are rederived.
- NIST DLMF 27.12, PNT: https://dlmf.nist.gov/27.12 . Only the classical unconditional asymptotics pi(X)~X/log X and theta(X)~X are used. No effective numerical error or zero-free region is asserted.
- NIST DLMF 18.14.8, alpha=0: https://dlmf.nist.gov/18.14.E8 . This is the imported Laguerre modulus bound used in EP19, not a newly proved inequality.
- S. M. Gonek, *Finite Euler products and the Riemann Hypothesis*, arXiv:0704.3448: https://arxiv.org/abs/0704.3448 . The abstract was read for literature context. The paper's conditional approximation theorems are not used as premises.
- S. M. Gonek, C. P. Hughes, J. P. Keating, *A Hybrid Euler-Hadamard product formula for the Riemann zeta function*, arXiv:math/0511182: https://arxiv.org/abs/math/0511182 . Abstract read for context. Neither its explicit formula nor random-matrix model is imported here.

No PDF was analyzed in this pass. The infinite norm asymptotic is proved using the displayed elementary logarithm bound, PNT and integration, not inferred from those abstracts. The literature on Euler products outside their absolute-convergence region is extensive. External novelty would require a specialist comparison; none is claimed.

## Mathematical self-audit

- The logarithm in EP8--EP9 is the sum of local analytic logarithms, not a potentially discontinuous principal log of the final product.
- The PNT-weighted concentration uses p<=X^(1-epsilon) versus larger primes; the order of limits X then epsilon is explicit.
- The norm lower bound uses an interval of positive width, not only one large point. Its logarithmic prefactor is negligible relative to A_X.
- Diagonal convergence uses 2a>1. The logarithmic-growth theorem is stated only for fixed 1/2<a<1; no endpoint or uniform-in-a assertion is smuggled in.
- The three-prime sign holds for all a>0; the rational a=1 example is only a finite check, not the proof for the open interval.
- The physical norm has factor 1/(2pi) and denominator a^2+t^2. Its diagonal is D/(2a), not D.
- The full update uses an isometric right shift. The stopped update includes the exact non-isometric loss B_j.
- The prime set through exp L gives exact full-source coefficients only on the physical horizon [0,L]. The energy-escape theorem explicitly prevents interpreting the raw product's explosion as an RH counterexample.
- EP17's lower bound on the assembled innovation sum is unproved. Individual nonnegativity is false. No triangle inequality supplies the collective bound.
- Large supported integers in EP19 do not imply coverage of all smaller omitted-prime integers. The plus-sign control is separately identified as non-zeta.

## What the executable checks do

`verify.py` reconstructs finite Euler coefficients and compares the Gram double sum with an independently implemented original-variable step integral. It checks full and stopped prime updates, the normalized telescoping ledger, the exact three-prime obstruction, and finite-horizon agreement with a separate trial-division Mobius implementation. All acceptance arithmetic is integer or Fraction arithmetic; primality uses integer square root. Acceptance does not rely on removable Python assert statements.

The ordinary and optimized runs each execute 489 exact checks. Twelve unit/rejection tests run in each mode. Result comparison is type-sensitive and rejects duplicate JSON keys. Saved result files are recomputed, not accepted on their PASS labels. The manifest binds every tracked packet file except itself.

The bounded checks do not prove PNT, Fourier inversion, the infinite norm asymptotic, the large-N prime-cutoff statement, or RH. No actual large prime sum, zeta-zero census, numerical Hardy matrix, Lean build, remote CI result, independent referee verdict, or new Mobius cancellation bound is claimed.

## Publication boundary

This packet was prepared add-only for PR #793. The available GitHub actions in this session provide reads but no file/commit/ref publication action; a direct git remote attempt failed DNS resolution. The supplied patch is therefore a handoff, not a claimed remote commit. The external publication receipt and publisher script are outside the tracked research packet. The patch is replay-tested in an isolated empty Git checkout, not represented as a full source-base checkout.
