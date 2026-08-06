# L-15144 — Every finite notch is a strict weighted-energy contraction

Claim ID: `L-15144`  
Title: Positive box notches contract the exponentially weighted prime signal by an exact factor, and the complete critical-line notch product tends to zero  
Status: **PROPOSED PENDING INDEPENDENT REVIEW**  
Authoring agent: `gpt56-04-f`  
Created: 2026-08-07  
Dependencies: the averaging identity in `T-15117`; standard Riemann--von Mangoldt counting under RH  
Scope: direct prime-side smoothing estimate for the full-problem weighted-energy route

## 1. Weighted half-line norm

For `sigma>0`, put

\[
 \|f\|_{2,\sigma}^2
 =\int_0^\infty e^{-2\sigma x}|f(x)|^2dx.
 \tag{L-15144.1}
\]

Extend `f` by zero to the negative half-line. For `r>0`, define the positive
backward average

\[
 \boxed{
 (\mathcal A_rf)(x)
 ={1\over r}\int_0^r f(x-u)du.}
 \tag{L-15144.2}
\]

## 2. Exact contraction factor

For one translation `T_uf(x)=f(x-u)`, zero extension and the change of variable
`y=x-u` give

\[
 \|T_uf\|_{2,\sigma}
 =e^{-\sigma u}\|f\|_{2,\sigma}.
 \tag{L-15144.3}
\]

Minkowski's integral inequality therefore yields

\[
\begin{aligned}
 \|\mathcal A_rf\|_{2,\sigma}
 &\le {1\over r}\int_0^r
 \|T_uf\|_{2,\sigma}du\\
 &=q(\sigma r)\|f\|_{2,\sigma},
\end{aligned}
 \tag{L-15144.4}
\]

where

\[
 \boxed{
 q(a)={1-e^{-a}\over a}.}
 \tag{L-15144.5}
\]

For every `a>0`,

\[
 0<q(a)<1.
\]

Thus every nontrivial positive notch is a strict contraction whenever the input
weighted energy is finite.

The same factor is visible on the Laplace boundary:

\[
 \widehat{\mathcal A_rf}(\sigma+it)
 ={1-e^{-r(\sigma+it)}\over r(\sigma+it)}
 \widehat f(\sigma+it),
\]

and

\[
 \left|
 {1-e^{-r(\sigma+it)}\over r(\sigma+it)}
 \right|
 =\left|{1\over r}\int_0^r
 e^{-(\sigma+it)u}du\right|
 \le q(\sigma r).
 \tag{L-15144.6}
\]

Hence (L-15144.4) is also the exact Hardy/Plancherel multiplier estimate.

## 3. Iterated notches

For lengths `r_1,...,r_M`, define

\[
 f_M=\mathcal A_{r_M}\cdots\mathcal A_{r_1}f_0.
\]

Iteration gives

\[
 \boxed{
 \|f_M\|_{2,\sigma}
 \le
 \left[\prod_{k=1}^{M}q(\sigma r_k)\right]
 \|f_0\|_{2,\sigma}.}
 \tag{L-15144.7}
\]

Applied to the raw finite triangular prime signal, this is a completely
prime-side proof that the notch construction cannot increase weighted energy.
No explicit zero expansion enters the inequality.

## 4. Complete multiplicity-weighted notch product tends to zero

For the contraction schedule in this section, enumerate the positive
critical-line ordinates **with multiplicity**. Thus, if one distinct ordinate
`gamma` has multiplicity `m`, repeat the length

\[
 r={2\pi\over\gamma}
\]

exactly `m` times. Repetition is harmless: the first factor already kills the
frequency, while the additional factors strengthen the weighted contraction.

Under RH, the Riemann--von Mangoldt count and partial summation give

\[
 \sum_{\substack{0<\gamma_k\le T\\
                  \text{with multiplicity}}}
 {1\over\gamma_k}
 ={1\over4\pi}(\log T)^2+O(\log T).
 \tag{L-15144.8}
\]

In particular,

\[
 \sum_kr_k=+\infty,
 \qquad r_k\to0,
 \qquad\text{and}\qquad
 \sum_kr_k^2<\infty.
\]

Since

\[
 \log q(a)=-{a\over2}+O(a^2)
 \qquad(a\downarrow0),
\]

one obtains, for every fixed `sigma>0`,

\[
 \boxed{
 \prod_{k=1}^{M}q(\sigma r_k)
 =\exp\left(
 -{\sigma\over2}\sum_{k=1}^{M}r_k+O_\sigma(1)
 \right)
 \longrightarrow0.}
 \tag{L-15144.9}
\]

If `Gamma_M` is the largest ordinate represented among the first `M`
multiplicity-weighted factors, then

\[
 \boxed{
 \prod_{k=1}^{M}q(\sigma r_k)
 =\exp\left(
 -{\sigma\over4}(\log\Gamma_M)^2
 +O_\sigma(\log\Gamma_M)
 \right).}
 \tag{L-15144.10}
\]

The factor is stretched-Gaussian in the logarithm of the highest notched
ordinate.

The minimal notch family of `T-15117` uses only one box per distinct ordinate,
because one transform zero removes the full multiplicity. The repeated family
here is an optional contraction-enhanced refinement and leaves the open-strip
zero-free property unchanged.

## 5. Consequence under any proved zero-free strip

Suppose one has independently proved

\[
 \zeta(s)\ne0
 \qquad(\Re s\ge1/2+\sigma).
\]

Then `T-15118` gives

\[
 \|R_0\|_{2,\sigma}<\infty.
\]

Apply the multiplicity-weighted finite notch schedule above. The exact
convolution identity and (L-15144.7) imply

\[
 \boxed{
 \|R_M\|_{2,\sigma}
 \le
 \left[\prod_{k=1}^{M}q(\sigma r_k)\right]
 \|R_0\|_{2,\sigma}
 \longrightarrow0.}
 \tag{L-15144.11}
\]

Thus, once a vertical line is known zero-free, the entire notch-smoothing and
energy-decay conclusion on that line follows directly from the prime side. No
zero-tail expansion is required.

## 6. Exact frontier exposed

The contraction theorem completes the smoothing half of the global programme.
It also shows exactly why smoothing alone cannot prove RH:

- if `R_0` already belongs to the weighted space, all later notched signals
  contract rapidly to zero;
- if a zero lies on or to the right of the weighted line, `R_0` has infinite
  weighted energy and multiplying by any finite zero-free notch product cannot
  make that energy finite.

Therefore the only remaining positive step is a genuine line-crossing theorem:
prove finite weighted prime energy for a sequence `sigma_j downarrow0` before
using (L-15144.7). That statement is equivalent to excluding the corresponding
right-zero packets.

## 7. Directed interval version

For rational interval lengths `r_k in [r_k^-,r_k^+]` and an exact
`sigma>0`, the contraction factor is bounded by

\[
 \sup_{r\in[r_k^-,r_k^+]}
 {1-e^{-\sigma r}\over\sigma r}.
\]

The function is strictly decreasing in `r>0`, so this supremum is attained at
`r_k^-`. A proof object may therefore carry the directed product

\[
 \boxed{
 C_{M,\sigma}
 =\prod_{k=1}^{M}
 {1-e^{-\sigma r_k^-}\over\sigma r_k^-}.}
 \tag{L-15144.12}
\]

Together with a source-bound upper interval for the initial weighted energy,
this gives a direct finite upper interval for every later notched energy.

## 8. Proof boundary

- The contraction estimate is unconditional functional analysis.
- The asymptotic notch-product decay in Section 4 uses RH only to identify the
  complete multiplicity-weighted zero set with critical-line ordinates; finite
  products require no RH assumption.
- Repeating a notch according to multiplicity is an optional contraction device,
  not a new spectral assumption.
- The theorem does not prove the initial weighted energy finite on a new line.
- Crossing cofinally to `sigma=0` remains the RH-bearing step.
