# T-21704 — A direct Brownian Nörlund real-zero proposal for RH

Claim ID: `T-21704`  
Title: Real zeros of explicit finite Brownian gamma approximants would prove the Riemann Hypothesis by Hurwitz  
Status: **FULL GLOBAL PROPOSAL — ONE FINITE REAL-ZERO THEOREM OPEN**  
Authoring agent: `gpt56-sol`  
Created: 2026-08-08  
Dependencies: `L-21705`, `L-21706`; Hurwitz or Rouché theorem  
RH status: **UNPROVED**

## 1. Proposed proof spine

\[
\boxed{
\begin{aligned}
&\text{Brownian bridge range}\\
&\longrightarrow\text{finite independent Gamma(2) spectral sums}\\
&\longrightarrow\text{logarithmic Nörlund occupation average}\\
&\longrightarrow\text{exact functional-equation approximants }\mathcal X_N\\
&\longrightarrow\boxed{\text{BLNRZ: every finite strip zero lies on }1/2}\\
&\longrightarrow\text{local uniform convergence to }4\xi\\
&\longrightarrow\mathrm{RH}.
\end{aligned}}
\tag{T-21704.1}
\]

This route attacks the zeros of `xi` directly. It does not pass through the prime ramp, WSTS, a Mertens bound, the balanced Type-II theorem, or a Weil-form inequality.

## 2. Conditional completion

Assume BLNRZ on an unbounded sequence `N_j`. Suppose `rho` is a zero of `xi` with

\[
0<\operatorname{Re}\rho<1,
\qquad
\operatorname{Re}\rho\ne\frac12.
\]

Choose a closed disk `D` centered at `rho`, contained in the open critical strip and disjoint from the critical line, whose boundary contains no zero of `xi`.

By (L-21706.8),

\[
\mathcal X_{N_j}\longrightarrow4\xi
\]

uniformly on `D`. Rouché's theorem therefore gives, for all sufficiently large `j`, the same positive number of zeros of `mathcal X_(N_j)` and `xi` inside `D`. This contradicts BLNRZ because `D` does not meet the critical line.

Hence every nontrivial zeta zero lies on the critical line:

\[
\boxed{\mathrm{BLNRZ}\Longrightarrow\mathrm{RH}.}
\tag{T-21704.2}
\]

No separate zero-density, prime number theorem, or functional-equation symmetry step is required beyond the construction itself.

## 3. Why this is not another equivalence-only endpoint

BLNRZ asks for an all-`N` theorem about finite phase-type distributions and finite Dirichlet splines. The input data are

```text
rates 1^2,1^2,2^2,2^2,...,N^2,N^2;
positive cutoff probabilities 1/(K H_N);
finite gamma convolution;
finite Hermite divided differences.
```

A proof could in principle use only finite total positivity, Sturm theory, canonical systems, or special-function identities. The limiting zeta function enters only after the finite real-zero theorem is established.

The theorem is still RH-bearing: an invalid proof may hide the limiting zero problem in a uniform total-positivity or Hermite–Biehler assertion. The review protocol is therefore fail closed.

## 4. Adversarial mutations

A proposed proof must survive all of the following.

1. **Raw-cutoff mutation.** Replacing the logarithmic mean by `m_N` must not remain covered; raw symmetrizations exhibit off-line pairs numerically.
2. **Generic-spectrum mutation.** Replacing `n^2` by arbitrary increasing rates must fail; random phase-type spectra exhibit off-line zeros.
3. **Weight mutation.** The proof must expose where `1/K` is used; it may not silently prove all positive averages.
4. **Finite-height mutation.** Argument-principle agreement below a finite height is evidence only.
5. **Limit-first mutation.** No property of `xi` or its zeros may be used to prove the finite theorem.
6. **Jensen-universality mutation.** Eventual low-degree hyperbolicity or local Hermite asymptotics is insufficient.
7. **Hidden Hermite–Biehler mutation.** Any asserted half-plane modulus inequality must include its complete zero-free and mean-type proof.
8. **Eisenstein embedding mutation.** A positive-measure analogy is insufficient; the exact finite transform and normalization must match `mathcal X_N`.

## 5. Current evidence

The exact checker `X-21703` validates the finite gamma, partial-fraction, moment, and Nörlund identities only.

Floating/high-precision reconnaissance currently finds:

```text
raw N=75:  one reflected off-line pair near height 111.46;
raw N=100: one reflected off-line pair near height 111.48;

logarithmic Nörlund:
N<=500, height<=300       contour count = critical-line count;
N=1000, height<=2000      contour count = critical-line count;
N=2000, height<=2000      contour count = critical-line count.
```

These are discovery records, not certificates. The exact theorem remains open.

## 6. Review order

1. `L-21705-finite-brownian-gamma-truncations.md`
2. `X-21703-brownian-norlund/verify.py`
3. `L-21706-logarithmic-norlund-xi-approximants.md`
4. `O-21705-raw-truncation-failure-and-norlund-reconnaissance.md`
5. `M-21702-brownian-norlund-review-protocol.md`
6. this theorem
7. the inherited BPY normalization on PR #217
8. future BLNRZ production proof

## 7. Exact status

```text
finite Brownian/gamma algebra              PROPOSED COMPLETE + EXACT REPLAY
quantitative convergence to xi             PROPOSED COMPLETE
raw finite real-zero shortcut              NUMERICALLY REJECTED / NOT USED
BLNRZ                                      OPEN / RH-BEARING
BLNRZ -> RH                                COMPLETE CONDITIONAL ARGUMENT
Riemann Hypothesis                         UNPROVED
```
