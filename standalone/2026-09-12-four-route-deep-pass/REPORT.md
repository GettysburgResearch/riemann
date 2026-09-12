# Four routes toward RH: deep assessment and new component work

Assessment completed 12 September 2026; packaged for publication 13 September 2026. Reviewed against main `f99d9e3908dde4865377c75d9ca051c1f545bf4f` and the research heads through PR #875 as they stood on 12 September. The final assessment check found #875 at `be149104721ae7b65b624c100118edfd7b76b69b`. This proposed follow-up packet accompanies PR #869; it does not claim to assess work posted after that cutoff. The original three-route packet remains unchanged.

**My assessment remains arithmetic first, native gamma second, correlated Ising third, and branching height fourth for completion prospects.** That is a judgment about the remaining mathematical obstacles, not a probability estimate. The strongest constructive advance in this pass is on Ising. The most useful new connection is that the branching orbit admits its own complete weighted-defect criterion with a tail bound uniform in depth, bringing it closer to the gamma route.

All four routes have substantial component mathematics. None of the material reviewed or derived here completes RH. In particular, explicit reformulations, finite moment matching, local zero annihilation, and convergence to the actual xi function do not supply the missing global sign or all-order construction.

## 1. The four routes, in one comparison

| Route | What the current work provides | What would finish the route | What this pass adds |
|---|---|---|---|
| Native arithmetic | Exact identities connecting reciprocal Möbius energy, polynomial trace, and the supremum of zero real parts; a sharp collision diagonal of order `log^4 Y` | A subpower upper bound for the native positive energy/trace, or a sufficient signed covariance estimate | Exact covariance–annular-energy identity; a growing counterfamily ruling out a generic constant-multiple diagonal bound; a classical unconditional `o(N)` trace refinement |
| Native gamma | Actual source identification with theta; convergence of a complete nonnegative zero defect; a fixed-step current handling collisions and multiplicity | Native cumulative production tending to zero, for example a sufficiently strong block contraction | Sharp variance-matched comparison of shape and scale paths; explicit fixed-moment positive-density counterexamples to a Fisher-only sign argument |
| Correlated Ising | Actual entire transforms with only real zeros; several exact finite-order theta matches and infinite growth-calibrated models | Admissible models matching arbitrarily many theta moments, or another proved convergence to the theta law | A certified seed and analytic continuation to connected infinite chains matching through degree eight, preserving all three real-field growth coefficients |
| Branching / height | Actual convergence to xi; eventual centrality at every fixed depth; permanent finite windows and shrinking zero-cluster tracking on expanding windows | Centrality of the limiting clusters, or vanishing of a complete native zero defect | A depth-uniform exponential defect tail and convergence criterion; a sharper leading-factor contribution to the sufficient height cutoff |

Detailed arguments, source citations, and qualifications are in [arithmetic.md](arithmetic.md), [gamma.md](gamma.md), [ising.md](ising.md), and [height.md](height.md). The new Ising construction has a separate [proof](ising-computation/PROOF.md) and [reproduction guide](ising-computation/README.md).

## 2. Arithmetic: a sharper target and a stronger test of proposed bounds

This route has the clearest exact arithmetic constraint. Its source is ordinary Möbius inversion, rather than a broad class of positive approximations. The reviewed generalized Littlewood argument, every-prefix energy lower bound, and trace comparison support the claimed logarithmic exponent identities. Their endpoint cases and complete tails matter; the detailed review checks those rather than inferring validity from PR summaries.

Write

\[
m(x)=\sum_{n\le x}\frac{\mu(n)}n,
\qquad F_X=\sum_{k\le X}m(k)^2.
\]

At a native weak crossing \(Y\), let \(D_Y\) and \(C_Y\) be the complete diagonal and ordered off-diagonal terms of the balanced Newton source in the manuscripts. Set \(B=(Y+1)^2-1\). The new exact identity is

\[
\boxed{C_Y=F_B-F_Y-D_Y+R_Y,\qquad |R_Y|<4.}
\]

The collar remainder is explicit; it is not an omitted asymptotic error. This explains why negative covariance panels alone are weak evidence: they compare annular energy with the diagonal up to this bounded collar correction. They do not establish an independent orthogonality principle.

The latest [#875 arithmetic manuscript](https://github.com/GettysburgResearch/riemann/blob/be149104721ae7b65b624c100118edfd7b76b69b/standalone/2026-09-12-astra-collision-chain-flow/ARITHMETIC.md) proves a matching lower bound for \(D_Y\asymp(\log Y)^4\). Combined with the existing exponent identities, the covariance identity yields

\[
\frac{\log(1+\max(C_Y,0)/D_Y)}{\log Y}\longrightarrow4\Theta-2
\quad (Y\text{ along native crossings}),
\]

where \(\Theta\) is the supremum of real parts of nontrivial zeta zeros. Subpower normalized positive covariance is consequently an RH-equivalent target. A fixed bound \(C_Y\le K D_Y\) would suffice, but is stronger than what has been shown necessary.

A new nonnative family preserves coefficient caps, Liouville signs, exact balance, normalization and its own crossing, yet has bounded diagonal and covariance growing at least as \((\log L)^2\). Thus **those relaxed conditions cannot prove a uniform constant-multiple diagonal bound**. This does not refute the weaker subpower target: logarithmic growth is itself subpower. It identifies which proposed shortcut fails, without overclaiming a general impossibility. The proof uses the complete harmonic kernel and a Mellin limit; it does not extrapolate the small numerical samples, which still have negative covariance.

The literature check also improves the elementary trace baseline: the odd reciprocal Möbius bound in [Tao's primary paper](https://arxiv.org/abs/0908.4323) sharpens the constant, and its decay with a complete source/tail split gives \(S_N=o(N)\) unconditionally. This remains compatible with logarithmic exponent one and gives no fixed exponent saving. The distinction is recorded in the arithmetic note.

**Next attack:** an upper estimate using the literal divisor identity, retaining the mixed terms, at a strength that improves the exponent. Another structural balance argument or a finite negative-covariance table would not resolve the issue identified here.

## 3. Gamma: the current is better founded, but its sign is still the obstacle

The native gamma route has an important advantage over an inverse-model construction: its limiting source is already the actual theta source. The source-to-defect convergence in [#862](https://github.com/GettysburgResearch/riemann/blob/67d5d6a5f588642f4c451fe35d2369b5ddac9346/standalone/2026-09-10-gamma-finite-defect/PROOF.md) survives the audit, including complete zero tails and coalescing multiple roots. It does not require accepting the most delicate claimed higher-order approximation rate elsewhere in the repository.

The new shape interpolation in [#875](https://github.com/GettysburgResearch/riemann/blob/be149104721ae7b65b624c100118edfd7b76b69b/standalone/2026-09-12-astra-collision-chain-flow/GAMMA.md) handles a real endpoint problem: the scale path's endpoint exponent jumps when the added scale vanishes, whereas the shape path has a continuously varying exponent. The review supplies the compact analytic-family details needed for a common exceptional disk at each fixed step, and checks the multiplicity formula. This is meaningful analytic progress. It gives neither a numerical common radius nor a radius uniform in the stage.

The new path comparison matches the mean and variance of the two positive sources. With \(B=(N+1)^2\), scale parameter \(v\), and shape parameter \(u=2v^2\),

\[
\left|\mathbb E\phi(Y_{\rm shape})-\mathbb E\phi(Y_{\rm scale})\right|
\le \frac{2v^2(1-v)}{3B^3}\,\|\phi'''\|_\infty.
\]

The constant is sharp. An explicit positive Peano kernel also proves the corresponding third-order stochastic comparison. This precisely prices the physical difference between the paths. It does not order their Fourier zeros: the reciprocal projection is nonlinear, and the relevant complex tests have no positive third derivative.

An explicit triangular-density perturbation preserves normalization and variance while splitting a double real Fourier zero into a nonreal pair. A related positive physical source preserves its mean as well. These are changed-source controls, not native gamma counterexamples. They rule out deriving the desired sign from positivity, finitely many moment constraints and Fisher information alone.

**Next attack:** one complete native step, including every exceptional cluster and the full exterior allowance. A positive total defect increment would refute stagewise monotonicity; a negative increment would establish an actual dissipation event. Either is more informative than another isolated favorable collision. Completion still requires a cofinal estimate such as

\[
\Delta_{N_{j+1}}\le(1-a_j)\Delta_{N_j}+b_j,
\quad\sum_j a_j=\infty,\quad b_j/a_j\to0.
\]

No result in this packet supplies that estimate.

## 4. Ising: an actual extra moment target has been reached

This pass goes beyond an assessment. Starting from #875's four head groups, a compensated edge calculation selected a coupling between two of the four equal \(b\)-spins. Five parameters then satisfy the head-mass calibration and the four even cumulant constraints through degree eight.

The resulting [proposed component theorem](ising-computation/PROOF.md) gives, for every sufficiently small positive background correlation, a connected infinite ferromagnetic chain with

\[
\mathbb E X^{2r}=\mu_{2r}\quad(r=1,2,3,4),
\]

and

\[
\log\mathbb E e^{hX}
=\frac h2\log h-\frac{1+\log(2\pi)}2h+\frac74\log h+O(1).
\]

Its characteristic function is entire with only real zeros. The finite seed is supported by a directed interval calculation reconstructing the complete theta source and infinite calibration tails. Two integration meshes certify the same radius-\(10^{-12}\) root box. The preconditioned residual is below \(7.63\cdot10^{-22}\), and the whole-box contraction bound is below \(1.252\cdot10^{-7}\).

A new fixed-order Markov cumulant lemma pays the analytic extension to the connected infinite model: each joint cumulant is divisible by every distinct-site gap correlation. This gives normal holomorphic convergence of the required infinite cumulant series. The extension is an analytic existence result; it has no certified explicit positive-correlation radius.

The model's standardized tenth-moment error is strictly positive, approximately \(0.0332115\). It is therefore demonstrably different from theta. This is an improvement from degree six to degree eight **within the infinite family preserving all three growth coefficients**. The earlier finite and leading-growth star models already reach degree fourteen, so it would be misleading to call eight the repository's overall moment record.

The finite Lee–Yang and closure inputs are documented in [Newman–Wu](https://arxiv.org/abs/1901.06596). They prove that suitable Ising approximants would suffice. They do not supply an inverse theorem representing every real-zero probability law by pair-ferromagnetic models. That additional representation problem is one reason I rank this route slightly behind native gamma for completion, despite its concrete success in this pass.

**Next attack:** analyze the cone of compensated next-moment responses under positive edge additions, then establish enough displacement before a weight, coupling or Jacobian reaches a boundary. An unbounded-order extension theorem is the actual goal. Repeated local full-rank calculations alone do not give it.

## 5. Branching and the \(T_n\) question: use the cutoff more carefully

The recent [#873](https://github.com/GettysburgResearch/riemann/pull/873) and [#874](https://github.com/GettysburgResearch/riemann/pull/874) are stronger than a fixed-window statement: they track the actual xi zero clusters on expanding windows, with shrinking radii and multiplicities retained. However, tracking a cluster near an actual xi zero does not establish that the zero is central. The permanent clean bands are unbounded but do not cover the strip.

The supplied \(T_n\) is a **sufficient proof bound**, not an observed last-exception height and not a lower bound on the optimal cutoff. A hypothetical fixed off-line xi zero could persist below those growing bounds without contradicting eventual centrality at each finite depth.

There are two new deductions in [height.md](height.md).

First, factor the source polynomial so its logarithmic derivative is

\[
\frac{d}{ds}\log P_n(2^{-s})=-n\log2+O(1),
\qquad |O(1)|<7\log2.
\]

Together with an exact cancellation in the gamma factor, this replaces the isolated phase floor \(320\,16^n\) by a constant times \(4^n\) in an alternative valid threshold. **All complete BV remainder terms are retained. This is not a bound \(T_n=O(4^n)\).** The exact recurrence comparison shows how much that qualification matters: at depth eight the alternative is only about 4.2% smaller, and the original majorant already has 2,811 decimal digits. At the first several depths the old recipe is better.

Second, the normalized branching Mellin function is uniformly bounded on a wider strip. Mapping that strip to the disk and applying Jensen gives the complete positive defect

\[
B_n=\sum_{\substack{H_n(\rho)=0\\0\le\Re\rho\le1}}
m_\rho(\Re\rho-\tfrac12)^2e^{-\pi|\Im\rho|},
\]

with the depth-independent bound

\[
\boxed{B_n^{>R}\le\log9\,e^{-\pi R/2},\qquad B_n\to B_\xi,
\qquad\mathrm{RH}\iff B_n\to0.}
\]

This pays the entire high-zero complement without enumerating exceptions up to \(T_n\). The exponential weight makes it computationally convenient but insensitive to very high zeros: a tiny value cannot substitute for a vanishing theorem. The existing height-30 certificate yields only a fixed small upper bound, not convergence to zero.

**Next attack:** use the literal branching recurrence to control this complete defect, or improve the signed Mellin remainder beyond its total-variation majorant. The first task connects directly with the gamma current work. The random Laplace cutoff and universal operator spectrum in #872 are different objects from \(T_n\); their source-specific identities need an additional argument before they control xi zero geometry.

## 6. What was checked, and what remains proposed

The four notes distinguish imported manuscript claims, arguments checked here, new deductions, interval-certified finite statements and open targets. Root and route agents cross-reviewed the new mathematical arguments within the same session. This is not external referee acceptance or formal verification.

Fresh computations include two complete-source Ising certificate runs, four independent finite algebra tests, exact arithmetic collar controls, gamma comparison controls, and exact reconstruction of the height-cutoff recurrence. The Ising runs use the same rational/outward-rounding backend at different meshes, not independent numerical implementations. The exploratory Ising root search and floating-point nonnative arithmetic panels are explicitly separated from accepting proofs.

Existing large zero certificates and every remote CI job were not replayed. Their stated dependencies remain visible in the route notes. The new claims are proposed component theorems submitted for review, not accepted or integrated results. Reproduction details and artifact hashes are recorded in [VALIDATION.md](VALIDATION.md) and [MANIFEST.json](MANIFEST.json).

The useful common distinction is now clear: arithmetic and gamma already retain the exact arithmetic source but lack a decisive bound; Ising guarantees the desired zero geometry but lacks exact all-order identification; branching retains the source and controls approximation, but still lacks a mechanism forcing limiting clusters onto the line. The new work narrows those gaps and tests plausible shortcuts. It does not eliminate them.
