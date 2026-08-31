# Independent review of the coherent quadratic graded algebra

Scientific freeze: `4fb6ffd9b626af2d9ee22fdd075280ccadb7a675`.

I independently read the five-file packet in `koszul-analytic-parent/`: `COHERENT_QUADRATIC_GRADED_ALGEBRA.md`, its replay note, `coherent_quadratic_replay.py`, the verification record and the 24-test source. The final frozen proof and replay note were read again by exact commit. I checked the source construction, parity operation, full ramified factors, positive count formula, finite duality and explicit tail arguments against the previously reviewed S4 and quadratic-cover packets. No producer or test was independently executed by this reviewer. Root reports focused Ruff, the producer write/check and optimized check after final binding, and 24 tests in each mode passed.

## Mathematical assessment

No remaining blocker was found under the stated hypotheses.

The distinction between the fixed-twist module `R_n tensor chi` and the algebra `R_n tensor chi^n` is substantive. The latter is the diagonal colour subalgebra of the actual two-colour source, with multiplication defined before its series. The proof correctly uses the lax monoidal map for middle extension and does not replace full ramified invariants by tensor products of invariant inputs. Grade zero is the untwisted principal factor; the fixed-twist grade zero is generally `L(chi,T)`, and equals one only for the specified genus-zero chi_u cover.

The finite cohomology assignment is untwisted in even grades and fixed-twist in odd grades. Thus the ordinary ratio is meromorphic for grading modulus below one, with principal poles only in even grades. It is a polynomial-growth Segre cohomology construction, not the exponential-growth Lie parent. The exact finite functional equation, including the grade-zero contribution, has the stated S4 asymptotics `K_N~N^6/72` and `W_N~N^7/84`. The claim excluding a finite rational reciprocal prefactor is restricted to the stated fixed-grading region and does not exclude other infinite completions.

The joint source has two full scalar resonances, `(1,+1)` and `(1,-1)`. Their coefficients are the nonnegative normalized counts `Ztilde/(2|G|)` and `(2Z-Ztilde)/(2|G|)`. The second cannot be omitted. The all-root radial constant follows from these two actual source weights; a closed point of Ztilde supplies a positive term at a degree divisible by any prescribed root order. The constant-twist interpretation at minus grading retains extension-degree parity, including the unchanged single points at ramification. The odd-characteristic nonsquare description is explicitly limited to its Kummer model.

## Replay and repaired precision

The runtime authenticates the preceding `c0b19791` proof and producer before import, then preserves that adapter's recursively authenticated geometric chain. Primitive recounts remain bounded by field order49. The p5 full degree-ten factor is used as frozen source data; p7 panels retain their four-trace restriction and reject full determinant or higher-trace promotion.

The source parity operation is evaluated at `w=z^m` before replacing w by minus w. It is not confused with `(-z)^m`; the tests contain the even-extension falsifier. Full infinity determinants, including nonzero invariant spaces with zero first trace, are preserved. Actual joint-cover and constant-twist point counts are checked against the two scalar weights. The signed grade-zero rational factor is kept separate from the real logarithm after leaving the initial arithmetic Euler disk.

The independently assembled positive-grade determinant logarithm and cohomological power logarithm have separate conservative tails. The final proof repairs an earlier unnecessary norm claim: its trace-power estimate uses purity and eigenvalue absolute values, independently of the arbitrary fixed Hermitian norms. The radial acceptance comparison uses the upper endpoint of the target interval, not its lower endpoint. Type, source-authentication, partial-data, colour and ramification controls are present.

## Scope

This packet supplies an actual source-level operation law and its analytic consequences for a specified function-field graded completion. Finite-cover cohomology, weights and duality are classical inputs; the scalar products belong to the classical multiple-q-factorial genre. There is no number-field or archimedean transfer, universal fixed-grading functional equation, new RH theorem or external priority claim. The separate fixed-twist and coherent-algebra boundary theorems must not be substituted for each other.
