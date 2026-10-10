# Independent audit: long-row theorem and secondary Mellin review

Reviewer: theta-closure subagent, 2026-10-10.

Verdict: no load-bearing mathematical correction identified in either frozen file below. The conclusions are confined to their stated theorems and dependencies. This audit does not validate a short-row fourth moment, the requested short-row generalized moment, the conditional exponent `17/24`, or RH.

## 1. Frozen files reviewed

| File in `standalone/2026-10-10-generalized-inverse-moments/` | SHA256 |
|---|---|
| `LONG_ROW_AND_OBSTRUCTION.md` | `986fe6ce333566fdea0ef849001393e93923fa98561faffdb97aa3c8a63909ce` |
| `MELLIN_AND_SPIKES.md` | `f3bdeb168714d838a4b13347cd353675d9644b9629041cdf7def78dc496162e3` |

The primary audit of the long-row argument was first performed on the identical `analysis_moment_obstructions.md` content. The published packet copy has the same hash. The secondary Mellin review was performed directly on the packet file.

## 2. Long-row proof reconstructed

I reconstructed the complete argument for

\[
 \sum_{0<Nu\le H}\left|\sum_n a_n\chi_n(u)\right|^{2k}
 \ll HD^{k+\epsilon}+D^{3k+\epsilon},
\]

for arbitrary bounded coefficients on squarefree ideals of norm at most a fixed multiple of `D`.

The primitive character-sum estimate is valid uniformly in the positive scale, including scales below one. Poisson summation gives a prefactor `T/sqrt(Nf)` and a sum over nonzero dual lattice points. The zero frequency vanishes for a nonprincipal primitive character. In two real dimensions, the rapidly decaying lattice sum is `O((T/Nf)^(-1))` for every `T/Nf>0`; when the ratio is large, omitting the zero dual point is essential. This gives the asserted smooth bound `O(sqrt(Nf))`.

The imprimitive extension is handled correctly. The factors at occurring primes where the total exponent difference vanishes modulo six are coprimality masks. Inclusion-exclusion costs an ideal divisor factor, and the radial weight makes dilation by an ideal generator independent of its rotation. These masks were not silently discarded when passing to the primitive conductor.

In the moment expansion, the exact conductor is the product of those primes whose exponent differences are nonzero modulo six. Its norm is at most the product of all `2k` original ideal norms, so each nonprincipal smoothed row sum is `O(D^{k+epsilon})`. There are `O(D^{2k})` tuples. This proves the stated off-diagonal error; it does not make that error small in the requested short-row range.

For the principal tuples, the incidence-pattern argument is complete. Every nonempty allowed prime pattern has total multiplicity at least two. The product of the norms of the ideals representing the patterns is therefore at most a fixed multiple of `D^k`. Fixed-order ideal divisor bounds and ideal counting yield `O(D^{k+epsilon})` tuples. The argument needs only the upper norm cutoff and includes the extra quotient-sixth-power diagonals when `k>=6`. Each principal row sum is `O(H)`. The unit ideal and the zero row used only in the positive smooth majorant are also covered.

The diagonal-size conclusion therefore follows in the stated long-row range `H>=D^{2k}`, without using the imported quasi-Riemann analytic theorem.

### Positive-coefficient obstruction

I also reconstructed the exact prime-sixth-power lower bound for positive squarefree coefficients. At a row `p^6`, the sextic symbol is precisely the mask excluding multiples of `p`. Positive squarefree ideal density gives order `D` mass; the removed part is `O(D/Np)`, or is absent when `Np` exceeds the support. The fixed-field prime ideal theorem supplies `D^{h/6+o(1)}` distinct rows of this form. Consequently the lower bound has exponent `2k+h/6`.

The necessary condition for an arbitrary-bounded-coefficient diagonal moment is correctly identified as `h>=6k/5`. Substitution into the separately proved extraction exponent forces that exponent to be at least one. This rules out the proposed arbitrary-coefficient method, not the exact Möbius moment itself.

### Standard inputs

The argument uses primitive Gauss-sum orthogonality, lattice Poisson summation with a smooth radial weight, the exact sextic residue-symbol definition, ideal counting and fixed-order divisor bounds, positive squarefree ideal density, and the ordinary prime ideal theorem in this fixed number field. No source claim about a new zero-free half-plane is needed for this theorem or obstruction.

## 3. Secondary audit of the Mellin and spike arguments

I checked the following statements and reconstructed their deductions.

The universal test is valid. The sum of independent uniform variables with half-widths proportional to `j^-2` has compact support, and its characteristic function decays at least as `exp(-c sqrt(|t|))`. Fourier inversion therefore gives a smooth nonnegative density. The Mellin product converges locally uniformly; the deviations of its factors from one are summable. Away from the imaginary axis no factor vanishes, so the product is nonzero. This establishes a single fixed test sufficient for the all-scale Mellin argument. It does not establish a quantitative height lower bound for that transform.

The extension of prime removal to an arbitrary fixed base row retains the exact zero extensions and moving-prime independence of constants. At record scales of `|A_v(D)|/D^beta`, all smaller-scale terms are controlled by the same record value. The finite prime-removal recursion then forces comparable values on every permitted prime replica. This proves the stated replicated-spike lower theorem.

The controlled-excess moment consequence and the one-good-replica tail criterion follow with their stated exponents. The latter uses a genuine contraction at smaller scales and a fixed starting interval. Neither argument supplies the new arithmetic upper bound assumed in its hypothesis.

For the upper half of the moment-growth characterization, I checked the stated uniform reciprocal lemma mechanism. A zero-free half-plane and a fixed positive buffer permit a holomorphic logarithm on disks centered at `2+it`. Uniform polynomial strip growth and Borel--Carathéodory bound that logarithm by `O(log conductor)` on a larger disk; absolute Euler convergence bounds it on a smaller disk. Three-circles interpolation gives `O((log conductor)^r)` with a fixed `r<1`, yielding the required arbitrary small conductor power after exponentiation. The principal character regularization is appropriate. Its passage back to the reciprocal zeta function introduces no pole to the right of the chosen line.

The polynomial conductor bound, elementary deleted-Euler-factor estimate, and rapid vertical decay of the fixed Mellin transform justify the uniform contour shift under the stated zero-free assumption. The endpoint where the rightmost-zero supremum equals one is handled separately by the trivial coefficient bound. Combining this upper estimate with the replicated-spike lower bound gives the stated squeeze for the moment-growth exponents and hence their limiting characterization.

### Standard inputs and scope

This secondary review depends on standard Hecke continuation, functional equations and polynomial strip growth, sextic reciprocity and its finite local conductor description, the fixed-field prime ideal theorem, and the explicitly stated complex-analytic reciprocal lemma. The proof uses the zero-free hypothesis of that lemma conditionally; it does not establish a new zero-free line. It is not an independent validation of the full upstream quasi-Riemann manuscript.

## 4. Execution record and limitations

No new analytic or numerical experiments were run for these audits. The independent exact algebra checker replay is already recorded separately in `analysis_checker_review.md`; it reported 32,473 passing finite predicates and a byte-identical result under optimized Python. This audit does not broaden the scope of that computation.

The reviewed long-row theorem, positive-coefficient obstruction, universal test, spike theorem and conditional moment-growth characterization are supported by the reconstructed proofs above. A short-row arithmetic upper bound for the actual inverse family remains unproved. None of these audit conclusions supplies it indirectly.
