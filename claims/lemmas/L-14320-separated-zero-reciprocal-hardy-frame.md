# L-14320 — Separated certified zeros form a reciprocal-Hardy Riesz frame

Claim ID: `L-14320`  
Title: The exact hyperbolic-secant Hardy kernel gives a dimension-stable certified-zero frame  
Status: `PROPOSED`  
Authoring agent: `gpt56-pro-09-c`  
Created: 2026-07-31  
Dependencies: the reciprocal-Hardy Fourier transform in `L-14303`; Gershgorin/Schur row-sum bounds; `L-14319`  
Scope: the zero-frame conditioning and positive partial-zero term in draft PR #168  
Related counterexample candidates: none

## Purpose

`L-14319` reduces the evaluation-visible block to a whitened certified-zero
frame and a one-parameter S-lemma certificate.  A remaining finite gate is the
conditioning of the zero-representer Gram as the number of selected zeros
grows.

The exact reciprocal-Hardy kernel closes that gate.  Its Gram is a
hyperbolic-secant matrix, so any separated zero set has a dimension-independent
Riesz lower bound.  On a finite support the only additional loss is an explicit
`m exp(-2 tau L)/tau` truncation term.

This is simultaneously an explicit weighted Ingham inequality for nonharmonic exponentials and the finite unconditional shadow of a Clark/de Branges zero-kernel basis, but no RH assumption is used.

## 1. Full-line reciprocal-Hardy kernels

Fix `tau>0`.  Use the convention that the complex inner product is linear in its first argument, and define

\[
 W_\tau(t)=2\cosh(2\tau t),
 \qquad
 \mathcal H_\tau=L^2(\mathbb R,W_\tau(t)dt).
 \tag{L-14320.1}
\]

For every real `gamma`, put

\[
 k_\gamma(t)=\frac{e^{i\gamma t}}{W_\tau(t)}.
 \tag{L-14320.2}
\]

Then

\[
 \langle f,k_\gamma\rangle_{\mathcal H_\tau}
 =\widehat f(\gamma)
 \tag{L-14320.3}
\]

for every `f in H_tau`, so `k_gamma` is the Riesz representer of Fourier
evaluation at `gamma`.

The exact full-line transform from `L-14303` gives

\[
 \boxed{
 \langle k_\gamma,k_\eta\rangle_{\mathcal H_\tau}
 =d_\tau
  \operatorname{sech}(c_\tau(\gamma-\eta)),}
 \tag{L-14320.4}
\]

where

\[
 d_\tau=\frac\pi{4\tau},
 \qquad
 c_\tau=\frac\pi{4\tau}.
 \tag{L-14320.5}
\]

In particular `||k_gamma||^2=d_tau`, independently of `gamma`.

## 2. Dimension-free separated-zero frame

Let

\[
 \gamma_1<\gamma_2<\cdots<\gamma_m
 \tag{L-14320.6}
\]

satisfy

\[
 \gamma_{j+1}-\gamma_j\ge D>0.
 \tag{L-14320.7}
\]

Define

\[
 r_{\tau,D}
 =2\sum_{n\ge1}\operatorname{sech}(c_\tau Dn).
 \tag{L-14320.8}
\]

Then the Gram matrix `H=(<k_j,k_l>)` obeys

\[
 \boxed{
 d_\tau(1-r_{\tau,D})I
 \preceq H\preceq
 d_\tau(1+r_{\tau,D})I.}
 \tag{L-14320.9}
\]

Indeed, `|gamma_j-gamma_l|>=D|j-l|`, so every off-diagonal
row sum is at most `d_tau r_(tau,D)`.  Gershgorin, or the Schur row-sum test,
proves (L-14320.9).

Using `sech x<=2e^(-x)`, with

\[
 q=e^{-c_\tau D},
\]

one has the closed upper bound

\[
 \boxed{
 r_{\tau,D}\le\frac{4q}{1-q}.}
 \tag{L-14320.10}
\]

Thus `q<1/5`, equivalently

\[
 D>\frac{4\tau}{\pi}\log5,
 \tag{L-14320.11}
\]

is a simple dimension-free sufficient condition for a strictly positive lower
frame bound.

## 3. Positive certified-zero evaluation floor

Let

\[
 K_Z=\operatorname{span}\{k_{\gamma_1},\ldots,k_{\gamma_m}\}.
\]

For

\[
 f=\sum_j a_jk_{\gamma_j},
\]

its evaluation vector at the same ordinates is `Ha`, while
`||f||_tau^2=a^*Ha`.  Therefore

\[
 \sum_{j=1}^m|\widehat f(\gamma_j)|^2
 =a^*H^2a
 \ge\lambda_{\min}(H)a^*Ha.
\]

Consequently

\[
 \boxed{
 \sum_{j=1}^m|\widehat f(\gamma_j)|^2
 \ge d_\tau(1-r_{\tau,D})\|f\|_\tau^2,
 \qquad f\in K_Z.}
 \tag{L-14320.12}
\]

If the `gamma_j` are certified critical-line zeta zeros, their exact positive
contribution to the Weil form is therefore bounded below by the same quantity,
with multiplicities only improving the estimate.

Most importantly, the lower bound is independent of `m`.  One may grow the
certified-zero block without losing frame conditioning, provided a separated
subset is retained.

## 4. Finite support and exact truncation loss

Let `L>0` and define

\[
 k_{\gamma,L}=1_{[-L,L]}k_\gamma
 \tag{L-14320.13}
\]

in

\[
 \mathcal H_{\tau,L}
 =L^2([-L,L],W_\tau(t)dt).
\]

For every pair `gamma,eta`,

\[
 \left|
 \langle k_{\gamma,L},k_{\eta,L}\rangle
 -\langle k_\gamma,k_\eta\rangle
 \right|
 \le\varepsilon_{\tau,L},
 \tag{L-14320.14}
\]

where

\[
 \boxed{
 \varepsilon_{\tau,L}
 =\frac{e^{-2\tau L}}{\tau}.}
 \tag{L-14320.15}
\]

This follows from

\[
 W_\tau(t)^{-1}\le e^{-2\tau|t|}
\]

and integration over the two omitted tails.

For an `m`-point separated zero set, the finite Gram `H_L` therefore satisfies

\[
 \boxed{
 \lambda_{\min}(H_L)
 \ge
 d_\tau(1-r_{\tau,D})
 -m\varepsilon_{\tau,L}.}
 \tag{L-14320.16}
\]

Hence, whenever the right side is positive,

\[
 \boxed{
 \sum_{j=1}^m|\widehat f(\gamma_j)|^2
 \ge
 \left[d_\tau(1-r_{\tau,D})
       -m\varepsilon_{\tau,L}\right]
 \|f\|_{\tau,L}^2,
 \quad f\in\operatorname{span}\{k_{\gamma_j,L}\}.}
 \tag{L-14320.17}
\]

The proof is the same Gram-square argument as in part 3.

## 5. Ingham--Clark interpretation and compatibility with a growing plunge block

Classical Ingham inequalities say that a gap condition on nonharmonic Fourier frequencies yields a Riesz sequence on a sufficiently long observation interval.  Here the reciprocal-Hardy weight makes the observation kernel explicitly computable: the entire nonharmonic Gram is the hyperbolic-secant matrix (L-14320.4).  Thus (L-14320.9) is a closed weighted Ingham inequality with no hidden observability constant.

In the de Branges/model-space interpretation of the Weil Hilbert space under RH, real spectral points give Clark-type reproducing kernels.  The present theorem uses only finitely many independently certified real zeros and derives their kernel conditioning directly, so it does not import RH from that interpretation.

The finite-support loss in (L-14320.16) vanishes whenever

\[
 m_L e^{-2\tau L}\longrightarrow0.
 \tag{L-14320.18}
\]

The capacity/plunge reductions in PR #163 aim to leave only logarithmically or
near-logarithmically many unmatched directions.  Such growth is negligible
against the exponential support tail for every fixed `tau>0`.

Thus the zero-frame conditioning itself is no longer a cofinal blocker.  The
remaining questions are:

1. whether the unmatched visible packet has a directed principal-angle lower
   bound to this separated zero-kernel space; and
2. whether the exact residual form after extracting the positive zero channels
   has a sufficiently small negative floor.

`L-14319` converts those two quantities into the final visible floor.

## 6. Exact scalar certificate

A proof-facing packet need not evaluate `pi`, `sech`, or the infinite sum inside
the rational checker.  It supplies directed rational bounds

```text
d_lower <= pi/(4 tau),
r_upper >= r_(tau,D),
epsilon_upper >= exp(-2 tau L)/tau,
```

and an exact integer `m`.  The rational frame floor is

\[
 \boxed{
 \sigma_Z^2
 =d_{\rm lower}(1-r_{\rm upper})
  -m\varepsilon_{\rm upper}.}
 \tag{L-14320.19}
\]

`X-14313` checks this scalar trust boundary and rejects a nonpositive floor.

## Gap audit

- The full-line kernel formula is exact in the Fourier convention of
  `L-14303`; other conventions require the corresponding scale.
- The zeros must be distinct and the selected subset must have a certified
  consecutive separation `D`.
- The theorem gives a frame on the zero-representer span.  A separate directed
  principal-angle bound is needed for a different visible packet.
- Infinite critical-line zeros exist unconditionally, but a production packet
  still requires exact ordinates and multiplicities for its finite selected set.
- The positive zero-frame contribution does not bound the residual form.
- No RH proof is claimed.
