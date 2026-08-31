# Independent frozen audit: actual weight-24 zeros and poles

Verdict: **PASS**, with no actionable mathematical or release-contract finding.
This is an independent non-author review of science
`ec5bdd9b02ea68bddfcf34ac40a85d283faf64cf`, whose parent is
`eaa8e8263bb34b8b669f911580c9dd9e55766ba2`. All five scientific files were
read, and no scientific file was edited. The verdict covers the stated fixed
weight-24 theorem, not effective constants, simplicity, a zero census, or RH.
There was no author coordination for acceptance.

## 1. Actual quotient and noncancellation

FI1-FI8 (proof lines 18-134) retain the canonical first-coefficient flag:
`g=Delta E4^3-696 Delta^2`, `b=Delta^2`, and `W=C b`. The exact `T2` matrix
has eigenvalues `540 +/- 12 sqrt(144169)` and distinct eigenspaces. Commuting
Hecke operators therefore preserve those lines; the eigenforms have first
coefficient one. This is not an arbitrary substitute flag.

Writing `Z=zeta`, `S_+,S_-` for the two unitary symmetric squares, and `C` for
the unitary tensor product, I independently recovered

`Q_1=A [Z^2 S_+ S_- - C^2] / [Z(S_+ + S_-)-2C] = A N/H`,

with `A=pi^(-s) Gamma(s) (4pi)^(-s-23) Gamma(s+23)`. In particular:

- The local Hadamard numerator is `1-X^2`; multiplication by `zeta(2s)`
  converts the coefficient product series to the tensor-product Euler factor.
- Both changes of basis contribute the same squared determinant `83041344`,
  which cancels from the actual quotient. There is no omitted gamma, zeta,
  basis, or unitary-shift factor.
- The first argument is conjugate-linear, but these fixed real-q eigenforms
  give the symmetric cross-period used in FI7. No conjugation of the complex
  variable is inserted into the meromorphic identity.
- `A` is holomorphic and nonzero on `Re s>1`, so a zero of `H` with `N`
  nonzero is a genuine pole of the original `Q_1`, and the reversed condition
  gives a genuine zero.

The warning in FI9 is important and correct: if `H_c` vanishes to order `m`
and `J_c` to order `r`, the pole order is `max(m-2r,0)` at an ordinary point.
A denominator zero or a pole of `J_c/H_c` alone does not pay noncancellation.

## 2. Imported automorphic hypotheses were actually checked

FI section 3 (lines 146-190) supplies the hypotheses, rather than applying
Booker--Thorne to unspecified formal Euler products. The two weight-24
representations are level one, unitary, and cuspidal with trivial central
character. A self-twist or a twist relating them must be quadratic. A ramified
quadratic twist has nontrivial scalar inertia and cannot preserve an unramified
local parameter. There is no nontrivial quadratic character of Q unramified at
every finite prime. The remaining trivial twist is excluded by the distinct
Hecke eigenvalues. This excludes the dihedral and twist-equivalent exceptions.

I read and visually inspected the relevant primary passages:

- [Gelbart--Jacquet](https://www.numdam.org/article/ASENS_1978_4_11_4_471_0.pdf),
  p.472 and Theorem 9.3 on p.534: the adjoint lift is cuspidal in this case;
  trivial central character identifies it with the symmetric square here.
- [Ramakrishnan](https://www.maths.tcd.ie/EMIS/journals/Annals/152_1/ramak.pdf),
  Proposition 2.3.1(2) and Theorem M, pp.53-54: the tensor lift is cuspidal for
  this non-dihedral, non-twist pair, with the required finite local factors.
  The [published correction](https://emis.muni.cz/journals/Annals/152_3/correction.pdf)
  concerns the running header, not the theorem.
- [Booker--Thorne](https://msp.org/ant/2014/8-9/ant-v8-n9-p01-s.pdf),
  Theorem 1.2 hypotheses, Proposition 3.1 on p.2034, and the contour argument
  on pp.2040-2041. Its inputs must be pairwise nonisomorphic unitary cuspidal
  representations with finite-place Ramanujan bounds. The degrees here are
  `1,3,3,4`; the two degree-three inputs differ already at prime two by
  `25920 sqrt(144169)/2^23`. The trivial GL1 representation is allowed.
- The complete two-page [Booker--Thorne correction](https://msp.org/ant/2014/8-9/ant-v8-n9-x01-Correction-ZerosOfLFunctions.pdf):
  the repaired uniform error still tends to zero, preserving Proposition 3.1.
  The proof does not reuse the original erroneous `O(sigma-1)` estimate.

The finite Satake parameters of the GL2 inputs have modulus one by Deligne;
their explicit symmetric-square and tensor products supply the required
Ramanujan bounds for the lifts. There is no appeal to an unproved general
GL4 Ramanujan conjecture. The source-normalization reference to Holowinsky--
Soundararajan section 2 was also checked in the preceding independent Hecke
audit. Remote literature is read as an analytic import, not falsely included
in the offline Git-byte authentication contract.

## 3. Common prime phases, contours, and distinct-point density

Proposition 3.1 includes the closed annulus. Thus `y=3/2`, `R=4` legitimately
allow all primes and the following two targets with one common phase system:

| Target `(Z,S_+,S_-,C)` | H | N |
|---|---:|---:|
| `(1,1,4,5/2)` | 0 | -9/4 |
| `(1,1,4,2)` | 1 | 0 |

The targets protect different divisors and use the same four genuine inputs.
The positive real target entries do not invoke positivity of a twisted period;
the common prime twists are complex and no such positivity is assumed.

FI11-FI14 and section 5 (lines 211-310) pay the required uniformity:

1. Both twisted polynomials have nonzero coefficient
   `1297521/131072` at index two, multiplied by the common nonzero phase.
   Neither is identically zero despite its vanishing constant coefficient.
2. The bounds `|h_n|<=4 d_4(n)` and `|n_n|<=2 d_8(n)` hold by Dirichlet
   convolution of the local degree bounds. They give uniform absolute tails
   throughout each closed disk inside `Re s>1`, for all prime twists.
   The stated FI13 follows from partial summation of
   `sum_{n<=x}d_r(n)<=x(1+log x)^(r-1)`; its boundary term has the discarded
   favorable sign.
3. At the pole target, a sufficiently small disk has `N_chi` nonzero on its
   closure and `H_chi` nonzero on its boundary. One finite cutoff and one
   finite prime-phase neighborhood control both functions uniformly. The
   untwisted and twisted tails are both paid. Rouche supplies denominator
   zeros while the full-disk numerator margin excludes cancellation.
   Interchanging the targets supplies genuine zeros. This is stronger than
   invoking a theorem about numerator or denominator zeros alone.
4. Rational independence of prime logarithms gives positive lower Lebesgue
   density of good positive shifts. A divisor in a translated radius-rho
   disk can account for at most `2 rho` measure of shifts. Covering the good
   shift set by those intervals yields separate linear lower bounds for
   distinct zeros and distinct poles. No multiplicity bound or simplicity
   is needed, and shrinking the available height interval loses only a
   bounded endpoint amount.

These are analytic arguments. Neither the finite tests nor the audit helper
purport to compute the phases, eta, T0, or an actual zero or pole.

## 4. Independent exact replay and adversarial checks

The accompanying reviewer helper imports no author module. It reconstructs
`Delta=(E4^3-E6^2)/1728`, independently of the producer's logarithmic Delta
recurrence and the resident tests' Euler-product route. It then reconstructs
all 64 `H,N` coefficients directly by Cauchy--Binet arithmetic pairs:

`H_n=delta^2 sum_{m^2|n} b(n/m^2)^2/(n/m^2)^23`,

`N_n=delta^2 sum_{m^2|n} tau(m)
       sum_{a<c, ac=n/m^2} (g(a)b(c)-g(c)b(a))^2/(ac)^23`.

All 128 rational comparisons agree, including every composite index through
64. Separately, multiplication of four formal two-variable Laurent geometric
series verifies the universal FI6 identity through the held-out degree 12,
not just at numerical eigenvalues or native primes. The 13 weight counts are
`1,4,9,...,169`. The entire held-out T2 action through index 32 also agrees.
All arithmetic is exact integer/rational coverage with no rounding.

The exact command was `python [-O] -m unittest` with these six modules:

- `tests.test_cusp_weight24_fixed_divisor_infinity`
- `tests.test_cusp_flag_hecke_source_concentration`
- `tests.test_cusp_flag_fixed_depth_divisor_ladder`
- `tests.test_cusp_flag_native_denominator_poles`
- `tests.test_cusp_flag_local_simple_endpoint_zero`
- `tests.test_cusp_flag_all_weight_endpoint_separation`

Results: **200 tests passed**, normal **59.334 s**, optimized **58.690 s**.
The producer `--check`, `--emit-fixture`, and `--emit-sources` passed in both
modes; both emitted artifacts match the frozen files after LF normalization.
The independent helper also passes normally and under `-O`.

An additional terminal audit obtained **36 genuine rejections in each mode**:
resealed weight, dimension, order, base, schema, scope, exclusions, budget,
quadratic data, eigen-equation, T2 boundary, digest and complete-structure
mutations; duplicate/bool/null/float/NaN/oversized JSON; invalid budget types
and limits; an oversized integer; and a changed literal frozen-source path.
An initial audit-harness attempt accidentally resealed its own bad-digest
mutation back to the original digest; this was corrected before these counts.
It was not a producer failure. Source rejection is not disabled by `-O`.

All six frozen source bindings, four current artifact hashes, and the payload
seal were independently recomputed from literal Git blobs. The science fixture
LF SHA256 is
`35bb6bab8a8be58e2d2ae4d03274f33ddf6f1b2ccea832f6612bfb4cec345c4c`;
its payload seal is
`3e0c049c57cd68648d37be8cbf25171480f3aaea751858d1b8cf2b0e3deb0015`.
The helper fixture records all five complete science SHA256 values.

Ruff check/format and the complete parent-to-science whitespace check pass.
Only the three review files are deposited. Downloaded primary PDFs and rendered
reading images remain an untracked local `tmp/pdfs` cache, not scientific
sources or review-commit contents. No push, PR change, main-worktree edit, or
modification of a frozen scientific file was made.

## 5. What remains outside this verdict

This is a classical simultaneous-value/contour method applied to the actual
canonical quotient, with explicit cancellation guards. It is not a new
automorphic family or new abstract zero theorem. The result does establish
infinitely many actual poles at this fixed weight; it does not bound all pole
locations, give an unsigned asymptotic, prove simplicity or effective onset,
or assert critical-line concentration. Its imported automorphy and value
theorems remain analytic literature inputs, not machine-certified outputs.
