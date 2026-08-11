# R-90412 — The uniform critical Selberg-integral input in `L-90419` is not unconditional

Claim ID: `R-90412`  
Title: `L-90419.2` misstates the scope of the classical Selberg–Saffari–Vaughan theory; the `Xh polylog(X)` bound uniformly through macroscopic `h` is itself critical/RH-strength  
Status: **LOAD-BEARING SCOPE CORRECTION — `L-90419` IS CONDITIONAL, NOT AN UNCONDITIONAL PIG THEOREM**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-11  
Scope: corrects the external analytic input only; the exact bridge/Haar identities, maximal-transfer algebra under a stated hypothesis, mean criterion, and factor-four annularization remain valid

## 1. The overstatement

`L-90419.2` asserted unconditionally, uniformly for every `1<=h<=X`,

\[
 \sum_{x\le X}
 |\psi(x+h)-\psi(x)-h|^2
 \ll Xh\log^2(2X).
\tag{R-90412.1}
\]

The cited classical Selberg/Saffari–Vaughan literature does **not** provide this critical-scale estimate uniformly through `h` comparable with `X` without an RH-strength hypothesis or an additional larger error term/range restriction.

At `h\asymp X`, (R-90412.1) is a square-root-scale mean-square assertion for macroscopic Chebyshev increments. It is precisely the type of global prime-error control the PIG programme is trying to prove, not a soft unconditional input.

Therefore the classification

```text
all nonmean endpoint modes at PIG scale
    PROPOSED COMPLETE UNCONDITIONAL
```

in the first version of the PR front door is withdrawn.

## 2. What remains correct in `L-90419`

The implication proved after the displayed input is algebraically valid:

> If a maximal short-interval estimate
> \[
> \sum_{x\le X}
> \max_{h\le H}
> |D_\circ(x,h)|^2
> \ll XH\log^A X
> \]
> holds uniformly through `H\asymp X`, then every nonconstant Haar mode is at PIG scale and endpoint PIG reduces to the mean.

The following steps survive exactly:

1. nested-interval formula for each triangular window;
2. Cauchy–Schwarz in the nesting index;
3. injectivity of the standard `(u,r)` starts;
4. scale estimate
   \[
   \sum_u|H_{u,\ell}|^2
   \ll N\ell\log^A N;
   \]
5. dyadic summation of the full Haar tree;
6. reduction to the mean under that hypothesis.

Accordingly `L-90419` is retained only as a **conditional transfer theorem** from a critical maximal Selberg integral to the nonmean PIG tree.

## 3. Unconditional frontier restored

The unconditional results on PR #383 remain:

```text
exact Fourier/inverse-Laplacian form;
exact bridge/Haar form;
randomized Euler PIG in expectation;
generic Fourier bulk outside sqrt(N);
generic Haar tree through sqrt(N);
exact high-modulus/character reindexing;
exact radix-four Haar state relation;
mean-to-inclusive-Pascal identity;
direct RH equivalence of the mean;
factor-four zero-safe annularization.
```

The open deterministic endpoint is again

```text
one mean coefficient
+
O(sqrt(N)) low Fourier modes;
```

or equivalently

```text
one mean coefficient
+
fewer than sqrt(N) coarse Haar coefficients.
```

The mean alone is RH-equivalent, but the coarse nonmean tree is not claimed closed unconditionally.

## 4. Lifecycle instructions

- Cite `R-90411` for the normalization correction.
- Cite `R-90412` whenever `L-90419` is used.
- Do not describe the Saffari–Vaughan theorem as supplying (R-90412.1) uniformly to macroscopic intervals unconditionally.
- Do not cite `L-90419` as an unconditional proof of nonmean PIG.
- The direct mean equivalence `T-90420` and the factor-four annular theorem `L-90421` are unaffected.

## 5. Honest boundary

```text
L-90419 algebra under critical maximal input   VALID CONDITIONAL TRANSFER
L-90419 claimed unconditional external input   WITHDRAWN / TOO STRONG
all nonmean PIG modes unconditionally          OPEN AT COARSE SCALES
mean critical-growth estimate                  OPEN / RH-EQUIVALENT
deterministic PIG                              UNPROVED
RH                                             UNPROVED
```
