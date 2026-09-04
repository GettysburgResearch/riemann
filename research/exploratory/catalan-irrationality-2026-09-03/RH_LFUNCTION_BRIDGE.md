# L-functions and the honest RH bridge

## 1. What the paper's L-function connection actually is

Catalan's constant is

\[
G=L(2,\chi_{-4}).
\]

This is a special value in the half-plane of absolute convergence. The proof
uses:

- the periodic signs of \(\chi_{-4}\);
- the elementary tail recurrence;
- p-adic valuations of a rational determinant under the hypothesis
  \(G\in\mathbb Q\);
- the Prime Number Theorem for weighted prime-power asymptotics;
- Hurwitz-zeta and Gamma identities to evaluate one finite correction.

It does not use:

- analytic continuation of \(L(s,\chi_{-4})\);
- its functional equation;
- zeros of that L-function;
- zeros of \(\zeta(s)\);
- a Weil positivity criterion;
- RH or GRH.

Therefore

\[
G\notin\mathbb Q
\]

has no known implication toward RH.

## 2. Why PNT in the proof is not an RH bridge

The scaled prime-power sums use PNT-level convergence:

\[
\frac1B\sum_{p^\nu}(\log p)f(p^\nu/B)\to\int f.
\]

PNT corresponds to the absence of zeta zeros on \(\Re s=1\). RH would require
square-root-scale signed error control throughout the critical strip. The
proof consumes only the main term of the prime-power measure, so it does not
encode the oscillatory information that locates zeta zeros.

## 3. The reusable architecture

The deep methodological pattern is:

\[
\boxed{
\begin{array}{c}
\text{source recurrence}\\
\downarrow\\
\text{nonzero determinant }Q_B\\
\downarrow\\
\text{same-scalar local valuation saturation}\\
\downarrow\\
\text{same-scalar archimedean decay}\\
\downarrow\\
\text{negative global height}\\
\downarrow\\
\text{product-formula/integer contradiction}.
\end{array}}
\]

This is an adelic analogue of the repository's operator strategy:

```text
canonical source
-> finite compression
-> Schur/Gram control
-> cofinal sign
-> RH.
```

The word “same-scalar” is essential. Bounding the denominator of one
determinant and the real size of a different determinant would not produce an
integer contradiction.

## 4. Candidate RH architecture

A speculative but mathematically honest program is:

```text
one hypothetical off-line zero rho_0
  -> explicit-formula or Mellin propagation
  -> infinitely many canonical scale-localized source vectors
  -> recurrence/finite-difference determinant Q_B(rho_0)
  -> Q_B(rho_0) is nonzero by a rational/meromorphic defect theorem
  -> prime-power factorization supplies local height saturation
  -> archimedean determinant estimate is strictly contracting
  -> product-formula contradiction.
```

This has potential only if the determinant is defined from the actual zeta
source before the zero is inserted as a witness.

## 5. Missing theorems

A complete route would need all of the following.

### Individual-zero propagation

A single off-line zero must force witnesses at infinitely many scales with a
quantitative lower bound. Global density statements are insufficient because a
finite exceptional set disappears in normalized averages.

### Arithmeticity

Sun's determinant is rational under the hypothesis \(G\in\mathbb Q\). A zeta
zero is generally transcendental and complex. One needs an arithmetic scalar,
or an algebraic norm of a scalar, whose local valuations are meaningful.

### Nonvanishing

The residual determinant must be nonzero for every off-line witness. The
rational difference-equation obstruction in Theorem 2.1 is an inspiring model,
but no zeta analogue is presently known.

### Local saturation

Prime-power valuations must be lower-bounded without replacing the source by
an unrelated majorant. This resembles the primitive-pair and divisor-wavelet
gates in PR #757.

### Archimedean contraction

The real/complex determinant needs a negative cofinal height margin. Aggregate
positivity or a finite numerical ladder does not suffice.

### Complex places

A genuine number-field/product-formula version must control every archimedean
embedding and all finite places, not only one absolute value.

### Finite-height closure

Even a cofinal contradiction theorem must be paired with directed verification
below its explicit threshold.

## 6. More realistic near-term payoff

Before RH, the method is much more likely to yield progress on:

- irrationality of other \(L(2,\chi)\) values;
- linear independence of several periodic L-values;
- irrationality measures;
- exact determinant identities for weighted tails;
- a reusable adelic height library;
- source-faithful local-to-global certificate technology.

Those advances would still materially strengthen the Riemann project by
improving its determinant and source-accounting toolkit.

## 7. Firewall

Do not infer any of the following:

```text
irrationality of beta(2) -> RH
PNT used in the proof -> RH-strength prime control
double Vandermonde -> Weil positivity
local p-adic saturation -> critical-line zero exclusion
negative height for one L-value -> negative height for xi determinants.
```
