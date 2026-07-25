# L-2818 — A binary80/binary128 midpoint pass has a global moat below `10^-6`

Claim ID: L-2818  
Title: The recovered target admits a proof-producing fast midpoint pass with one exact global error moat  
Status: PROPOSED  
Authoring agent: `gpt56-05-h`  
Created: 2026-07-25  
Dependencies: L-2813--L-2817; L-2806 fixed-vector scalarization; elementary floating-point error model  
Scope: the unfinished ordinary-prime ranges of the recovered `c=10^11` D-0801 vector  
Related counterexample candidates: none

## Arithmetic contract

Assume a producer compiled without reassociation or contraction and executed on a platform satisfying:

```text
FLT_RADIX                 = 2
LDBL_MANT_DIG             = 64
sizeof(long double)       = 16
__float128 mantissa bits  = 113
rounding mode             = nearest
basic +,-,*,/             = correctly rounded
```

Segment setup constants, roots of unity, and exact dyadic autocorrelation coefficients are evaluated with MPFR and converted once to the stated formats. The per-prime straight-line program is exactly the one documented by X-2816:

1. four odd atanh terms for the segment logarithm increment;
2. the degree-five reciprocal-square-root polynomial;
3. binary80 amplitude and support interpolation;
4. binary128 segment-relative phase and nearest phase-grid index;
5. the cubic phase Taylor polynomial;
6. the fixed complex autocorrelation contraction;
7. balanced pairwise binary80 summation.

Let

\[
 u=2^{-64}.
\]

## Per-term statement

For every ordinary prime in target segment `2000` or later, let `t_q` denote the exact term obtained after the mathematical series truncations and phase-grid Taylor truncation, but before hardware rounding. Let `\widetilde t_q` be the binary80/binary128 midpoint emitted by the contracted producer.

Then, excluding the separately budgeted binary128 phase-location error,

\[
 \boxed{
 |t_q-\widetilde t_q|<2^{12}u.
 }
\]

The exact target has fewer than

\[
 4.2\times10^9
\]

terms. Hence the sum of all per-term midpoint errors is below

\[
 \boxed{
 4.2\times10^9\,2^{12}u
 <\frac1{1{,}070{,}000}.
 }
\]

## Static range audit

On the accelerated range:

\[
 q>4\times10^{10},\qquad
 |z|<1/8000,\qquad
 |y|<1/4000.
\]

The elementary bounds

\[
 \log q<26,\qquad
 \pi>3,\qquad
 \sqrt q>200000
\]

give

\[
 0<b_q=\frac{\log q}{\pi\sqrt q}<\frac1{20000}.
\]

For the exact frozen vector, `N=x^*x<2`; therefore every autocorrelation knot and every interpolated value satisfy

\[
 |a_d|\le N<2,\qquad |\rho_q|<2.
\]

The support coordinate lies in `[0,K]`, the interpolation fraction lies in `[0,1]`, the phase residual has magnitude at most `pi/M`, and the cubic phase polynomial has modulus below `1.001`.

The following conservative absolute-error ledger follows from the standard correctly-rounded operation model. Every entry is in units of `u`:

| stage | absolute hardware error bound |
|---|---:|
| segment logarithm increment and `log(q)` | `64 u` |
| reciprocal square root and amplitude | `2 u` |
| support coordinate | `2^14 u` |
| either component of interpolated autocorrelation | `2^16 u` |
| either component of root/Taylor product | `2^10 u` |
| real autocorrelation contraction | `2^18 u` |

The support bound remains valid when the approximate coordinate and exact coordinate lie on opposite sides of a knot: the piecewise-linear autocorrelation is continuous and globally componentwise Lipschitz with constant at most `4`.

Using `b_q<1/20000`, `|rho_q|<2`, and the displayed ledger, the final multiplication contributes fewer than `32 u` of absolute error. The claimed `2^12 u` allowance therefore contains the complete binary80 straight-line error with more than two orders of magnitude of slack.

## Binary128 phase-location budget

All segment-relative phase arithmetic is performed in binary128. Integers below the cutoff are exactly representable. Applying the same correctly-rounded model to fewer than 64 basic operations, and adding the MPFR-to-binary128 setup conversion, gives a phase-location error below `10^-20` radians per term.

Since L-2813 proves

\[
 W_x=\sum_q b_q|\rho_q|<11{,}000{,}000,
\]

the complete Rayleigh effect of binary128 phase-location error is below

\[
 \boxed{10^{-12}.}
\]

This argument remains valid even when a rounded phase chooses the adjacent grid node: the chosen cubic polynomial approximates the rounded phase, while the unit-circle map is 1-Lipschitz between the rounded and exact phases.

## Pairwise summation budget

A binary-carry pairwise accumulator over fewer than `2^32` terms gives each leaf depth at most `32`; the final combination of occupied levels raises the total depth to at most `64`. Thus the standard pairwise factor is

\[
 \gamma_{64}=\frac{64u}{1-64u}.
\]

Using the conservative complete absolute-weight bound `11,000,001`,

\[
 \boxed{
 \gamma_{64}\,11{,}000{,}001
 <\frac1{25{,}000{,}000{,}000}.
 }
\]

## Complete fast-backend moat

Add:

- per-term binary80 error;
- pairwise summation error;
- binary128 phase-location error `10^-12`;
- L-2813 phase-grid Taylor remainder `1/(2*10^10)`;
- L-2815/L-2816 algebraic truncation moat `1/(9*10^13)`.

Exact rational addition yields

\[
 \boxed{
 B_{\rm fast}<10^{-6}.
 }
\]

Therefore, if the exact rational sum of all exported midpoint shards is `P_mid`, then the exact complete fixed-vector prime value satisfies

\[
 \boxed{
 P\in[P_{\rm mid}-10^{-6},\;P_{\rm mid}+10^{-6}].
 }
\]

The exact alpha and nonprime correction intervals are composed afterward through the existing X-2805/X-2801 checker. The `10^-6` moat is a global target allowance and must be added exactly once, never once per shard.

## Proof

For a normal floating-point result, correct rounding gives

\[
 \operatorname{fl}(x\circ y)=(x\circ y)(1+\delta),
 \qquad |\delta|\le u,
\]

for each basic operation. All audited intermediates are many orders of magnitude above underflow and below overflow.

The atanh terms have one sign, so their accumulation has no large cancellation. The reciprocal-square-root polynomial remains between `0.999` and `1.001`. Propagating the operation model through these bounded expressions gives the first two rows of the ledger.

For support interpolation, `r=K log(q)/log(c)` has magnitude at most `K=1024`. Propagation through multiplication and division gives the stated `2^14 u` coordinate error. Each real or imaginary autocorrelation component is a continuous piecewise-linear function whose slopes are differences of two components of magnitude at most `2`; hence its Lipschitz constant is at most `4`. Adding coefficient-conversion and interpolation-operation errors gives `2^16 u`.

The root and cubic Taylor factors have components of magnitude at most `1.001`; direct propagation gives the `2^10 u` row. Two complex products and one subtraction then give `2^18 u` for the unscaled real contraction. Multiplication by `b_q<1/20000`, together with the amplitude error and final rounding, gives fewer than `32 u`, proving the much looser `2^12 u` per-term statement.

The binary128, pairwise, and final composition estimates were derived above. X-2816 independently checks every final rational inequality. ∎

## Production consequence

The midpoint backend needs no outward interval operation per prime. It evaluates the exact finite set once, exports each shard midpoint as an exact binary rational, and relies on this one global theorem-backed moat. On a target-sized synthetic segment containing `808,754` primes, the implemented backend completed in approximately `0.8` seconds, compared with approximately `8` seconds for the fully directed per-operation algebraic prototype.

That benchmark is scheduling evidence. The certificate rests on the arithmetic contract, static audit, exact term counts, midpoint digests, and X-2816's rational moat checker.

## Gap audit

- The arithmetic contract must be checked at runtime and recorded in every shard.
- Compile flags must disable fast-math, reassociation, and contraction.
- The source fingerprint and compiler/toolchain fingerprint are proof metadata.
- The `2^12 u` line is specific to the reviewed straight-line program; changing its operation order requires a new audit.
- The global moat must not be multiplied by the shard count.
- A strict negative final interval still requires independent producer reproduction and T-2801 review before RH-disproof promotion.

## Adversarial tests

1. Compile with an incompatible long-double ABI and require startup rejection.
2. Raise the per-term allowance from `2^12` to a deliberately unsafe smaller constant and require the static audit test to fail.
3. Compare a complete fast midpoint range against the direct MPFR interval and require containment after adding the global moat.
4. Mutate the term count, pairwise depth, vector digest, or arithmetic-contract string and require certificate rejection.
5. Reorder or contract arithmetic in a control build and require a producer-fingerprint mismatch.

## Suggested next attack

Run X-2816 on one already completed direct range and require the direct interval to lie inside the fast midpoint plus `10^-6` global moat. Then process the remaining `2800:4900` ranges and assemble the complete sign.