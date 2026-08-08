# Full-problem attack: logarithmic Nörlund averages of finite Brownian gamma laws

## Executive judgment

The carry programme has now isolated exact RH-equivalent arithmetic scalars. Rather than introduce another scalar coordinate, this pass returned to the Brownian representation of `xi` and asked for a direct sequence of finite real-zero approximants.

The first construction—symmetrizing one finite gamma cutoff—fails numerically by genuine-looking reflected off-line pairs. The corrected construction averages **all nested cutoffs with logarithmic occupation weights before symmetrization**.

For

\[
S_K=\sum_{n\le K}\Gamma_{2,n}/n^2,
\qquad
m_K(s)=\mathbb E[(S_K/\pi)^{s/2}],
\]

put

\[
\overline m_N(s)=\frac1{H_N}\sum_{K\le N}\frac{m_K(s)}K,
\qquad
\mathcal X_N(s)=\overline m_N(s)+\overline m_N(1-s).
\]

The exact finite formula, functional equation, and uniform convergence to `4 xi` are closed. The one remaining theorem is finite and global:

\[
\boxed{
\mathcal X_N(s)=0,
\ 0<\Re s<1
\Longrightarrow
\Re s=1/2.}
\]

Call this BLNRZ. An unbounded BLNRZ sequence proves RH immediately by Rouché.

This is a serious direct proposal, not an unconditional proof. The branch is designed to let reviewers either prove the finite special-function theorem or find its first failure.

## 1. Exact probability input

Biane–Pitman–Yor identify the Brownian-bridge range variable with the infinite gamma series

\[
Y_\infty^2=\frac1\pi\sum_{n\ge1}\frac{\Gamma_{2,n}}{n^2}
\]

and prove

\[
\mathbb E Y_\infty^s=2\xi(s).
\]

The finite truncation has rational Laplace transform

\[
L_N(q)=\prod_{n\le N}\left(\frac{n^2}{n^2+q}\right)^2.
\]

Resolving all double poles gives a finite phase-type density and the exact Mellin formula

\[
m_N(s)=\pi^{-s/2}\Gamma(1+s/2)
\sum_{n\le N}C_{N,n}
\left[n(H_{N+n}-H_{N-n})+\frac{s-1}{2}\right]n^{-s}.
\]

The same object is one repeated-knot Hermite divided difference. This places the finite problem at the intersection of phase-type probability, nonuniform B-splines, and finite Dirichlet polynomials.

## 2. Quantitative approximation

The remainder gamma sum has mean at most `2/N`. For `0<=Re s<=1`, the complex power difference identity and the first `Gamma(2)` coordinate give

\[
|m_N(s)-2\xi(s)|\le |s|/N.
\]

The logarithmic mean therefore satisfies

\[
|\mathcal X_N(s)-4\xi(s)|
\le
\frac{\zeta(2)}{H_N}(|s|+|1-s|).
\]

This is a strong proof-facing feature: once finite real-rootedness is proved, the RH transfer is a one-paragraph Rouché argument with no asymptotic prime estimate.

## 3. Why the raw idea was rejected

The unaveraged approximants

\[
X_N^{raw}=m_N(s)+m_N(1-s)
\]

have the correct symmetry and much faster `1/N` convergence, but symmetry plus convergence is not enough. High-precision reconnaissance finds reflected off-line pairs near height `111.46` at `N=75` and near `111.48` at `N=100`. A finite argument-principle scan at `N=75` counts two more strip zeros than line crossings.

This is consistent with the general warning in the literature that natural truncations of xi-related expansions may acquire nonreal zeros. The raw producer is a mandatory adversarial mutation, not a dependency.

## 4. Why the logarithmic mean is structurally different

The weights

\[
\mathbb P(K=k)=1/(kH_N)
\]

are positive occupation weights on the nested spectral cutoffs. They do three things simultaneously:

1. preserve a genuine probability/Mellin interpretation;
2. give every fixed mode asymptotically full logarithmic weight;
3. turn the `1/K` cutoff error into the summable `1/K^2` convergence ledger.

The resulting one-sided factor is

\[
\overline m_N(s)
=\pi^{-s/2}\Gamma(1+s/2)
\sum_{n\le N}(\alpha_{N,n}+\beta_{N,n}s)n^{-s},
\qquad\beta_{N,n}>0.
\]

Numerically, this small change prevents the pair collision seen in the raw truncation throughout a substantially larger range.

## 5. Current reconnaissance

The gamma-stripped argument-principle code compares the complete strip winding count with critical-line crossings.

```text
raw N=75, T=120          38 strip / 36 line
Nörlund N=500, T=300     138 strip / 138 line
Nörlund N=1000, T=2000   1517 strip / 1517 line
Nörlund N=2000, T=2000   1517 strip / 1517 line
```

Scans through `N=500` and height `300`, and selected levels through height `1000`, also matched. The first roots move steadily toward Riemann ordinates.

All such data are explicitly classified as floating reconnaissance. They do not justify the cofinal quantifier.

## 6. The most plausible proof mechanisms

### 6.1 Hermite–Biehler / canonical system

Find an explicit finite companion `E_N` with

\[
\mathcal X_N(1/2+iz)=E_N(z)+E_N^\#(z)
\]

and prove the upper-half-plane modulus inequality. The phase-type chain with repeated rates `n^2` nominates a finite positive Hamiltonian, but the correct boundary determinant has not yet been found.

### 6.2 Integral of squares

Gasper's method proves real zeros for the Pólya Xi-star and K-Bessel functions by writing a modulus difference as an integral of squares. Here the repeated-knot phase-type density and the positive cutoff mixture may permit a finite identity of the same form. Every boundary term must be retained; generic log-concavity is insufficient.

### 6.3 Dirichlet-spline total positivity

Each `m_K` is a Mellin transform of a Dirichlet average and one Hermite divided difference with repeated knots `n^-2`. The target is a theorem saying that the logarithmic occupation mixture lies in a multiplicative sign-regular class whose symmetrized Mellin transform has central-line zeros.

### 6.4 Pólya / Lagarias–Suzuki zero-block inequality

Lagarias and Suzuki prove line-zero theorems for explicit reflected combinations by grouping zeros of a base entire function and comparing shifted factors one block at a time. A finite analogue would factor the one-sided Nörlund Mellin function and prove that its reflected terms have unequal moduli off the central line. The zero strip and exponential/mean type are load bearing.

### 6.5 Phase-type Sturm realization

`S_N` is the absorption time of a sequential Markov chain with each rate `n^2` repeated twice. The logarithmic mean randomizes the starting spectral cutoff. A self-adjoint dilation or canonical-system realization of its symmetrized Mellin transform would prove BLNRZ by ordinary spectral theory.

## 7. Relation to the rest of the repository

This route is genuinely global and structurally independent of WSTS/BTP.

- It consumes the same `xi` object as the Brownian SAT proposal but replaces the RH-equivalent final convex-order inequality by a finite approximant theorem.
- It avoids the prolate ground-line obstruction: no target eigenline is assumed inside a localized Weil matrix.
- It avoids the arithmetic first-cell firewall until the final limiting identification, where it is already built into BPY's exact `xi` moment formula.
- It is compatible with the repository's insistence that finite numerics never replace a cofinal theorem.

If BLNRZ fails at some larger level, the failure itself will be informative: it will identify which finite spectral modes reproduce an off-line quartet and can be compared directly with the raw-truncation collision.

## 8. Exact assurance

The standard-library verifier checks 456 exact rational identities and four mutations:

```text
harmonic collapses   136
Laplace rows          64
normalizations        16
moment rows          112
Dirichlet rows        80
Nörlund rows          48
mutations            4/4
```

Retained digest:

```text
a112d0e37e820d1ebabaa1e2b8b6cad517a0631012c81543b37ec3f2fca88393
```

The verifier does not certify a single zero.

## 9. Final status

```text
Brownian finite gamma model                  PROPOSED COMPLETE
partial fractions / Mellin / spline formula PROPOSED COMPLETE
critical-strip convergence                   PROPOSED COMPLETE
raw-cutoff real-zero theorem                 NUMERICALLY REJECTED / NOT USED
BLNRZ finite real-zero theorem               OPEN / RH-BEARING
BLNRZ -> RH                                  COMPLETE CONDITIONAL
Riemann Hypothesis                           UNPROVED
```

The next pass should attack BLNRZ itself rather than return to another RH-equivalent arithmetic scalar.
