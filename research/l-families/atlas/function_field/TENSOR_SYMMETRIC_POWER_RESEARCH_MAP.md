# Tensor/symmetric-power L-family research map

## Purpose

This is the compact handoff index for the tensor/symmetric-power exploration
on PR #752.  It separates proved local/compact statements, unbound exploratory
leads, and open arithmetic or global questions.  Follow the linked packet
notes for proofs and the JSON payloads for executable provenance.

RH and GRH remain open.  A local spectral identity is not a curve
correspondence, compatible system, automorphic transfer, or global Euler
product.

## 1. Central comparison

For every `r>=1`, the ladder compares

\[
 \operatorname{Std}(E_A)\otimes\operatorname{Sym}^r(E_B)
 \quad\hbox{with}\quad
 \operatorname{Sym}^{2r+1}(E_C).
\]

The raw local factors have different weights.  The typed comparison uses
the dilation

\[
 P_{\operatorname{Std}(A)\otimes\operatorname{Sym}^r(B)}
       (q^{r/2}T)
 =P_{\operatorname{Sym}^{2r+1}(C)}(T).
\]

For odd `r`, the square-root choice must remain explicit.  Dropping this
dilation changes the mathematical question.

## 2. Dependency chain and canonical records

| layer | exact record | status | canonical payload |
|---|---|---|---|
| rational complete Sym-power aliases | `ELLIPTIC_SYMMETRIC_POWER_FULL_FACTOR_SIGN_ALIASES.md` | all `m>=1`, fixed rational `q!=0` | `f1a7f183ee16c98c8f633e9b5ffa5f1bb76c0521cd596d5be71840a35711d983` |
| odd cyclotomic complete spectra | `ELLIPTIC_SYMMETRIC_POWER_CYCLOTOMIC_SPECTRAL_ALIASES.md` | complete odd-order stabilizer | `b783dc120095c5256cacc2eaa79f3f152883f9b33b4074a18b123489f81bc6ff` |
| even cyclotomic complete spectra | `ELLIPTIC_SYMMETRIC_POWER_EVEN_CYCLOTOMIC_ALIASES.md` | complete parity-coset stabilizer | `075a40fc0e4fc6aa835053e2df95f628076cadea51ad83671edea922d3c76c5e` |
| `r=1` tensor / `SO(4)` family | `ELLIPTIC_PAIR_RANKIN_SO4_FAMILY.md` | exact compact coefficient region, moments, and locked finite pushforwards | `3634ab438de17596fa7a616130a318b85b579178b6d87f017523dae25c53e028` |
| `r=1`, tensor versus Sym3 | `ELLIPTIC_SO4_SYM3_SPECTRAL_INTERSECTION.md` | exact integral odd-prime-power spectral intersection | `c2657dceb8784e5581092cfd07500f7f39680ce4685516f0ce03e02c195b230c` |
| `r=2`, tensor versus Sym5 | `ELLIPTIC_TENSOR_SYM2_SYM5_SPECTRAL_INTERSECTION.md` | complete rational raw intersection | `e2c9c7ac3d1329b7b911a5214d36935d2694436cbe6d9cce551b94f8486b01ba` |
| all-r monomial torus ladder | `ELLIPTIC_TENSOR_SYMMETRIC_POWER_SUBTORUS_RIGIDITY.md` | complete integer monomial classification | `f05eea9c197c95af54e874bea437b7547acf42b5ccad50b29f7031b54d5c695d` |
| `r=3`, tensor versus Sym7 | `ELLIPTIC_TENSOR_SYM3_SYM7_SPECTRAL_INTERSECTION.md` | complete integral odd-prime-power raw intersection | `a1ec101912ba9712c015c2cbbd81022097ad113f2d6d0d9178ad7be4b43cfdbf` |
| all-r compact moments | `ELLIPTIC_TENSOR_SYMMETRIC_POWER_MOMENT_LADDER.md` | exact every-even-moment formula; closed forms through degree eight | `0eba593b98d1cdb10cd79354ef15b9352291be1c28d85e961ed35fcd17aed088` |
| all-r universal-graph Hasse counts | `ELLIPTIC_TENSOR_SYMMETRIC_POWER_HASSE_GRAPH_COUNTS.md` | exact square and nonsquare odd-prime formulas | `1c34b50b7535cdb628b7afa712f8f82576eeacde262f25dcf2bfd472ef577681` |
| high-rank compact boundary law | `ELLIPTIC_SYMMETRIC_POWER_HIGH_RANK_HAAR_LIMIT.md` | exact analytic Haar theorem; no generated payload | human proof note |

The payload hashes are full canonical SHA-256 values, not display prefixes.
Each generated packet authenticates its owned note, producer, test, and locked
predecessors.

## 3. What is proved

### Spectral geometry

The complete integer monomial subtorus classification is

\[
 W_r(a,b)=\{\pm a+b(r-2j):0\le j\le r\}=O_r,
 \qquad
 O_r=\{-(2r+1),-(2r-1),\ldots,2r-1,2r+1\},
\]

if and only if

\[
 (|a|,|b|)=(r+1,1)\quad\hbox{or}\quad(1,2).
\]

These give the two universal Dickson--Chebyshev graph loci.  They are
exhaustive among integer monomial one-parameter subtori, not among arbitrary
nonmonomial or isolated algebraic components.

The full rational converse is proved at `r=2`.  The full integral raw
odd-prime-power converse is proved at `r=3`, after the required dilation.

### Compact detector hierarchy

For `V_n=Sym^n(C^2)` and
`B_k(n)=dim((V_n^(tensor 2k))^SU(2))`,

\[
 B_k(n)=[t^{kn}](1-t)(1+t+\cdots+t^n)^{2k}.
\]

The independent product and principal laws agree through degree four and
first split at degree six by

\[
 {3\over2}r(r+1)(r+2).
\]

For even `r`, generic `USp(2r+2)` is the polarization-matched comparator.
For odd `r>=3`, matched `SO(2r+2)` already separates at degree four by
`2r-1`.  At `r=1`, the product law is exactly standard Haar `SO(4)` in every
degree.

### Arithmetic graph counts

At square `q=p^(2k)`, the two-graph union has

\[
 8p^{\lfloor k/(r+1)\rfloor}+8p^{\lfloor k/2\rfloor}
 -1+\mathbf1_{r\ {\rm odd}}-4\mathbf1_{3\nmid(r+1)}
\]

integral Hasse triples.  At nonsquare odd `q=p^e`, odd `r` is empty; even
`r` has the exact first-graph count displayed in the Hasse packet.  This is a
count of sufficient graph loci, not a full all-r intersection theorem or a
simultaneous three-curve realization.

### High-rank compact law

Haar symmetric-power characters converge weakly to

\[
 W={\sin U\over\sin\Theta},
 \qquad
 \Pr(|W|>x)\sim{16\over9\pi^2}x^{-3}.
\]

Here `U` is uniform on `[0,2pi]` and independent of the Haar `SU(2)` angle
`Theta`.

Principal and product ladder laws converge to `W` and `ZW`, with distinct
tail constants.  Their variance stays one, while finite-rank even moments of
order `2k>=4` grow as rank to `2k-3` because of a separate endpoint boundary
layer.  Weak convergence does not justify passing those moments to the limit.

## 4. Unbound exploratory evidence, not promoted theorem

An ephemeral capped `r=4` scout considered

\[
 P_{\operatorname{Std}(A)\otimes\operatorname{Sym}^4(B)}(q^2T)
 =P_{\operatorname{Sym}^9(C)}(T).
\]

The session reported that the gcd of four post-elimination coefficient
numerators was the two-graph divisor, that a torsion sweep through order 80
left orders `5,9,10,11,18,20,22` on four irrational `Z=z^2` factors, and
that no off-graph point appeared in aggregate totals of 24,346 raw triples and
34,225 rational forced pairs.

No source-locked script, numerator list, exact search domain, or grid bounds
were retained.  Those observations are therefore **not reproducible from the
repository** and must be treated only as conjecture-generating leads.  They do
not exclude an isolated noncyclotomic rational point.  `THEOREM_TARGETS.md`
preserves the reported divisor and residual factors together with this
provenance warning.

## 5. Visibility warnings for future computation

- At square bases and `r=1`, the two graphs have equal size.
- At square bases and every fixed `r>=2`, graph two dominates; the union has
  only `Theta_p(q^(-5/4))` density in the ordered raw Hasse cube.
- At fixed square base and high `r`, the exact count becomes six-periodic.
- At nonsquare odd bases, graph two disappears; graph one survives as a thin
  staircase only for even `r`, and odd `r` is empty.
- Uniform trace-cube sampling is therefore a poor discovery strategy.  Sample
  by square class, rank parity, and graph identity.
- These are raw trace-lattice frequencies, not frequencies of realized curves.

## 6. Best next attacks

1. **Isolated `r=4` points.** Eliminate or construct noncyclotomic rational
   zero-dimensional points without a broad Groebner or trace-cube sweep.
2. **Uniform residual support.** Classify the cyclotomic zero-dimensional
   support for general `r` and find a uniform coefficient prefix defining the
   graph union.
3. **The `p=2` nonsquare boundary.** Classify the genuine Dickson-zero
   exceptions omitted from the odd-prime theorem.
4. **Arithmetic realization across primes.** Determine whether linked
   elliptic or higher-variety families can occupy either graph compatibly at
   many places; separate local Waterhouse realization from global geometry.
5. **Uniform two-limit equidistribution.** At fixed `r`, prove the relevant
   arithmetic compact image and effective equidistribution; only then ask for
   error bounds uniform enough to let `r` grow and test the cubic-tail law.

## 7. Replay and resource contract

The two newest generated packets replay with

    python -B research/l-families/atlas/function_field/elliptic_tensor_symmetric_power_moment_ladder.py --check
    python -B -O research/l-families/atlas/function_field/elliptic_tensor_symmetric_power_moment_ladder.py --check
    python -B research/l-families/atlas/function_field/elliptic_tensor_symmetric_power_hasse_graph_counts.py --check
    python -B -O research/l-families/atlas/function_field/elliptic_tensor_symmetric_power_hasse_graph_counts.py --check

The moment packet accounts for 25,317 units below 30,000 and 20,456
Clebsch--Gordan transitions below 21,000.  The Hasse packet accounts for 3,071
units below 20,000; every public enumerator fails before scanning more than
4,096 candidate `C` values.  The high-rank Haar note is a symbolic proof and
runs no producer.

Core ladder checkpoints on PR #752 are `575aff08`, `912895aa`, `978a740e`,
`7cf8e1b7`, `9af34bde`, `010827a5`, `18dfb6e1`, `054bbc46`, and `7f46c7b4`;
earlier bridge and pilot context is retained in the same PR history.  Program
backlinks are recorded on #737, #738, and #741.
