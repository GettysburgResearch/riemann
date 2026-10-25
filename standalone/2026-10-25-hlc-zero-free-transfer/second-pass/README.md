# Second pass: an actual native gain and quantitative HLC cancellation

Date: 25 October 2026. Status: proposed source-dependent analytic results, exact finite identities, and an exact consumer calculation. No RH proof or smaller global zero-free half-plane is claimed.

This pass goes beyond the first packet's conditional reformulations. It proves a power saving for the actual native Möbius inverse on a specified long-length interval, develops a quantitative strengthening of the supplied HLC argument, and proves additional estimates for the exact coefficients that arise in attempts to join the two routes. All external analytic premises remain explicit and source-qualified.

The original first-pass files are preserved byte for byte. This directory is a new proposed object, with its own mathematical freeze and review reports.

## 1. Main result for the actual Möbius inverse

For the original sixth-power-free Eisenstein physical rows of size U, let

\[
 I(U,D)=\sum_u w(u)\left|D^{-1/2}
       \sum_n\mu_E(n)\psi_u(n)W(Nn/D)\right|^2.
\]

The common profiles, fixed finite ray twists, orientations, natural zeros, licensed punctures and norm heights are retained. The [new native theorem](CAPPED_NATIVE_MOMENT.md) proves, under the pinned all-family 7/8 cap and buffered row-count theorem,

\[
 I(U,U^r)\ll_\varepsilon U^{e_{\rm new}(r)+\varepsilon},\qquad
 e_{\rm new}(r)=
 \begin{cases}
 (1+5r)/6,&1\le r\le10/7,\\
 2/7+3r/4,&10/7\le r\le3/2,
 \end{cases}
\]

with the finite profile and polynomial height costs stated in the theorem.
In particular,

\[
 I(U,U^{3/2})\ll_\varepsilon U^{79/56+\varepsilon},
 \qquad 17/12-79/56=1/168.
\]

The saving is on the actual Möbius coefficient and the complete physical row sum. No Gauss-weighted substitute is inserted.

The key correction is source scope: the pinned OpenAI theorem states a 7/8 cap for **every finite-order Hecke L-function over the Eisenstein field**, not only ordinary zeta. Buffered zero-location bins therefore stop at that cap. On each bin, Borel–Caratheodory and three-circles applied to an Euler-normalized holomorphic logarithm give a subpower reciprocal bound inside its zero-free rectangle. A finite Mellin shift then estimates the original inverse directly.

This does not certify the complete external OpenAI argument. Its family cap and the Xu–Sang buffered row counts are named premises, not conclusions of this packet.

## 2. Quantitative cancellation from the supplied paper

The [uniform HLC extension](UNIFORM_HLC_AUDIT.md) gives a proposed source-dependent proof of

\[
 \sum_{n\le x}\Lambda(n)\mu(n+2)
       \ll x(\log x)^{-1/1000},
 \qquad
 \sum_{p\le x}\mu(p+2)
       \ll x(\log x)^{-1-1/1000}.
\]

The source itself states qualitative cancellation. This extension uses a growing number of well-separated prime bands and explicitly audits the previously fixed-parameter constants. It is accompanied by a separate internal mathematical review. No numerical value for the implied constant or starting threshold is certified, and the entire external 52-page proof is not independently reconstructed.

The new [optimal unmarking theorem](TWO_SIGN_HLC.md) is independent of that analytic premise. For independent normalized band marks with second moments R_i, put q_i=1/R_i. The orthogonal projection of 1 onto products involving at least k bands is

\[
 P_{N,k}=\sum_{|S|\ge k}(-1)^{|S|-k}
          \binom{|S|-1}{k-1}q_S U_S,
\]

and its exact squared error is

\[
 \|1-P_{N,k}\|_2^2=\Pr\!\left(\sum_{i=1}^N B_i<k\right),
 \qquad B_i\sim\operatorname{Bernoulli}(q_i).
\]

For equal fixed R_i, fixed k, this decays exponentially in N, up to a fixed polynomial. It improves the first pass's block-averaging error. The transfer formula retains both the projection coefficient mass and the prime-to-CRT moment discrepancy.

The uniform audit chooses N=floor(loglog(x)/100), with geometrically spaced logarithmic prime scales. It checks the arithmetic root modulus, memory operators, dirty edges, global distinctness, Type I estimates, major arcs and the mixed moments needed for the final projection. The local edge constants are traced to exponential-in-K factors; a fixed-K big-O statement is not silently treated as uniform. A source-anticipated Liouville counterpart is recorded separately in its appendix without a novelty claim.

## 3. Additional positive component estimates

| Result | What is proved | What remains separate |
| --- | --- | --- |
| [Moving cubic twist](MOVING_TWIST_MOMENT.md) | For the exact coefficient mu gamma_2 and radical norm Q, the all-row mean is bounded by A+B Q^(1/3)+A^(1/4)B^(1/2)Q^(1/2), plus the explicit resonant term. At A=B and Q<=B^(3/2), the nonresonant cost is B Q^(1/3), improving the direct B sqrt(Q) extension. | The raw Möbius coefficient lacks the extra Gauss factor; its signed return is not bounded by this theorem. |
| [Exact Gauss inverse and sharper ordinary mean](NATIVE_GAIN.md) | A twisted finite Heath–Brown identity exposes the required mu gamma_2 coefficient with its real moving twist; a cubic/sextic frequency decomposition improves an ordinary component from K^(3/4) to K^(2/3). | The outer factor sum and Fourier frequency signs must still be estimated coherently. |
| [Growing-prime coefficient changes](FRACTIONAL_NATIVE.md) | Full bounded parameter changes at primes up to (log D)^2(loglog D)^(2-delta), and exact polynomial marks on the HLC subpower prime scales, preserve the source row-volume estimate at subpower cost. | The complete fixed-rho damping remainder and the full large-prime sign pattern require further control. |

For the factorial marks, the row-norm cost is explicitly

\[
 k!e_k\!\left((\sqrt{Np}-1)^{-1}:p\in P\right)
 \le\left(\sum_{p\in P}(\sqrt{Np}-1)^{-1}\right)^k.
\]

This reaches the source's finite damping polynomials, including degrees of order sqrt(log D) on its exp((log D)^a) bands with a<1/5. It does not replace a remainder estimate by a finite experiment.

## 4. Why the global boundary is still unchanged

The [complete scalar consumer calculation](DETECTOR_CONSUMER.md) checks where the new inverse saving can enter. The existing selected-prime and long-inverse detector bounds cross at a length t_*<=10/7. The new inverse estimate agrees with the old one up to 10/7; afterwards its long-witness count is still nondecreasing. Thus the optimized count in that consumer is unchanged.

At r=3/2, the new exponent 79/56 remains larger than PR1014's sufficient target 41/30 by 37/840. The logarithmic HLC saving also does not give the fixed power saving for the full shift average required by the first-pass bridge.

The source-qualified working benchmark therefore remains B_flat=0.874886647039964.... The saving must reach the detector's crossing range, or the short-witness estimate must improve, before this consumer gives a smaller half-plane. The new results are usable components, not a completed solution.

## 5. Verification and review

Three exact local checkers passed independent root execution. Their coverage is recorded in [CHECKS.json](CHECKS.json): complete small CRT spaces and optimality identities; rational Euler/convolution identities with repeated-prime corrections; and exact synthetic cyclotomic twisted-convolution/row identities. Adversarial controls reject omitted or altered terms. These computations test finite algebra, not all-scale cancellation.

The mathematical arguments have separate agent review reports with exact hashes. Review scope and intellectual overlap are disclosed. This is internal review, not external peer review or formal verification. The publication receipt binds the mathematical freeze and verifies the remote Git blobs. No CI success is inferred from local checks.

## 6. Exact source record

- First-pass PR1022 head, preserved: `00d36f61ae7898846579840e6a68f9a06bd8295c`.
- Main read at start: `f99d9e3908dde4865377c75d9ca051c1f545bf4f`.
- PR1021 refreshed head: `0f07049ff1e8cc7765f6de01b4e176ad627bba4b`, including its 25-October selector/marked-estimates packet.
- PR1020 head: `c690f96fe6876f945398b3e2779810c563a64743`.
- PR1014 native consumer: `845225c2e7713b69766b95c5e6964d44bb62f6bb`.
- OpenAI arithmetic source: `openai/math@1581d4cbdd69a0faf34b2089614fe2a814316a6a`, `preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex`, blob `268c4e3206d460c617d3d2129742a72b831b3def`.
- Xu–Sang: [arXiv:2610.17675v2](https://arxiv.org/html/2610.17675v2), exact version, especially Lemma 6.2 and Proposition 6.3.
- Lü–Wang–Wu: [arXiv:2610.20242v1](https://arxiv.org/html/2610.20242v1). The original supplied PDF has SHA256 `32ef255566d4f3611d2d89c3a5f3db94c792883cc713d77a7f9d33b163f55e88`; its license and full original source record remain in the first-pass SOURCES.md.

