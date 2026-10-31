# Swarm continuation: support windows, Bessel companions, and native cosine synthesis

**Status: proposed research components, with proofs, internal cross-reviews, and reproducible finite certificates. No proof of RH or improvement of an unconditional zero-free boundary is claimed.**

This is an additive continuation of [PR #1026](https://github.com/GettysburgResearch/riemann/pull/1026), frozen at `11b4f6612275955a1fddb5c53f67dc21124783f8`. That parent supplies the exact xi matrices, observation map, theta source, Bessel boundary reduction, and rational interval primitive. Its files and recorded conclusions remain unchanged. The new results have their own identities and reviews below.

The work was divided among an anchor/operator lane, a cofinal Bessel lane, and a deterministic-transform/native-approximation lane. The coordinating lane built a complete complex-disk certificate and checked how the results fit together. Separate agents reviewed the final analytic arguments and replayed the finite checkers. These are internal AI-agent reviews; they are not external human refereeing or formal proof-assistant verification.

## What changed in this pass

| Direction | Established here | Remaining mathematical obligation |
|---|---|---|
| Moving anchors | The old absolute positive-part budget necessarily fails in a cofinal regime. A literal support-window limit, complete-prime transfer, and lower-spectral-bound transfer replace it. | Positivity on an unbounded sequence of support windows. |
| Cofinal Bessel sums | A quantitative complete-source rate, a fixed entire companion, exponentially paired numerator/denominator zeros, and a residue asymptotic. | Control at the target zero neighborhoods, including nonreal poles, multiplicities, and residue signs. |
| Local Bessel gate | Exact all-zero reality within `|z| <= sqrt(2000)` for two specified actual-source higher-order approximants. | A cofinal family satisfying the gate on disks whose radii tend to infinity. |
| Native cosine synthesis | A deterministic whole-strip multiplier, explicit images of the original discrete generators, Sobolev estimates, and a bound on the complete omitted frequency range. | One coefficient construction with vanishing complete norm and compatible global tail control. |

The targeted prior-art checks identify substantial classical foundations. The source-specific results were developed and proved in this pass; worldwide novelty or priority is not established.

## 1. Moving matrices become literal support windows

Let `P_(N,a)` project onto the Laguerre span

\[
V_{N,a}=\operatorname{span}\{\sqrt{2a}e^{-au}L_n(2au):0\le n\le N\}
\subset L^2(0,\infty).
\]

The [window bridge](anchor/LAGUERRE_WINDOW_BRIDGE.md) proves

\[
a_j\to\infty,\quad N_j/a_j\to L<\infty
\quad\Longrightarrow\quad
P_{N_j,a_j}\to \mathbf1_{[0,2L]}
\quad\text{strongly}.
\]

For an infinite ratio, the limit is the identity. The finite ratio therefore has an exact geometric meaning. The proof is elementary: compute the projection between two decaying exponentials, sum a geometric series, use density, and upgrade weak convergence to strong convergence because the limit is itself a projection. This does not give operator-norm convergence.

An exponential-weight estimate then justifies passage of the **entire** prime operator through that limit:

\[
\sum_{m\ge2}\frac{\Lambda(m)}{\sqrt m}P_jT_{\log m}P_j
\longrightarrow
\sum_{2\le m<e^{2L}}\frac{\Lambda(m)}{\sqrt m}
Q_{2L}T_{\log m}Q_{2L},
\]

strongly, with strong convergence of the adjoints and a uniform norm bound. Here `T_t phi(u)=phi(u+t)` and `Q_ell` is the support projection. A convergent Mangoldt majorant controls all omitted prime powers uniformly. This is not a fixed-prime-prefix calculation.

The old positive family `a=100(N+1)` has `L=1/100`. Its limiting support length is `1/50`, below the first prime delay `log 2`. Its entire arithmetic operator consequently tends strongly to zero. Finite matrices still contain all prime terms; the vanishing concerns the proved limiting operator.

The more substantial transfer concerns minimum eigenvalues. Let `Q` be the actual xi quadratic form written in the manuscript, including the gamma, pole, and complete prime terms, and put

\[
\lambda(\ell)=\inf_{\substack{\|\phi\|=1\; ;\;\operatorname{supp}\phi\subset[0,\ell]}}
\mathcal Q(\phi),
\]

with the infimum taken in its logarithmic Fourier form domain. For `0<L<infinity`,

\[
\liminf_j\lambda_{\min}G_{N_j}(a_j)\ge\lambda(2L).
\]

Strong convergence alone would not justify this statement. The proof controls moving minimizing vectors: exponential weights prevent mass escaping in space, and the actual gamma term controls logarithmic Fourier energy. Together these give strong compactness. The prime and pole terms pass to the limit, while the nonnegative gamma form is lower semicontinuous.

A certified positive lower bound on any fixed window therefore gives eventual positivity for **all orders along that fixed ratio**. The manuscript also proves continuity of the window spectral floor and computes the exact norm of each newly visible prime shift. Newly exposed short intervals are not small perturbations in ordinary operator norm, so a naive small-window-extension argument remains invalid.

### Why the previous budget is abandoned

The [budget obstruction](anchor/ANCHOR_BUDGET_OBSTRUCTION.md) proves, for `N>=1`, `a0>=100(N+1)`, and `1<=a1<a0`,

\[
\|X_+\|-\lambda_{\min}G_N(a_0)
>\frac12\log\frac{N+1}{a_1}-\frac{29}{12}.
\]

Here `X_+` is the integrated positive part used by the preceding sufficient transport estimate. In particular that estimate necessarily fails when `(N+1)/a1>=128`. The proof combines a trace lower bound, an alternating Fejer trial vector, and an actual-source endpoint estimate. An exact two-dimensional model also shows that both the absolute budget and a fixed initial relative metric can fail while every endpoint matrix remains positive.

This refutes a sufficient proof mechanism. It does not prove indefiniteness of the actual endpoint matrix.

## 2. A fixed companion explains the Bessel cancellation

The [cofinal companion manuscript](bessel/COFINAL_COMPANION.md) keeps the actual source

\[
w(x)=\Phi\bigl(\tfrac12\operatorname{arsinh}x\bigr),\qquad
c_n=I_n(a)w(n/a),
\]

and its finite positive kernel

\[
\mathcal K_{a,M}(t)=e^{-a\cosh(2t)}
\sum_{|n|\le M}c_{|n|}e^{2nt}.
\]

For every fixed exponential weight and `0<c<2*pi`, it proves

\[
\int_{\mathbb R}|\mathcal K_{a,M}(t)-\Phi(t)|e^{R|t|}dt
\le C_{R,c}\left(a^{-1}+e^{-cM/(2a)}\right).
\]

Thus the explicit schedule `M=ceil(a(3+2 log a))` converges at rate `O_R(1/a)` in each such norm, including the complete theta source and cutoff remainder.

Write the energy transform as `F=A y+B dot y`, with `nu^2=-E`, `y=K_nu(a)`, and radial derivative `dot y=a partial_a y`. Use the real entire growing solution `u=(I_nu+I_(-nu))/2` and define `J=A u+B dot u`. The new result is the explicit entire limit

\[
J_\infty(E)=\frac1\pi\int_0^\pi w(i\sin\theta)\cos(\nu\theta)d\theta
+\frac{\sin(\pi\nu)}\pi\int_0^\infty\Phi(t/2)\sinh(\nu t)dt.
\]

The closed-strip regularity needed at the angular cusp is proved from the actual theta transformation. It yields the endpoint Fourier estimate that controls the otherwise exponentially amplified angular sum. The limiting companion is independent of the approximating degree and anchor.

The Wronskian gives the exact identities

\[
-B/u=F-(y/u)J,\qquad A/\dot u=F-(\dot y/\dot u)J.
\]

Since `y/u ~ pi exp(-2a)`, the normalized numerator and denominator differ from the same source transform by exponentially small amounts. At a simple zero `E_*` of `X(E)=Xi(2 sqrt E)`, when `J_infinity(E_*)` is nonzero,

\[
\frac{\operatorname{Res}_{E=\lambda_a}[-A(E)/B(E)]}
{2\pi a e^{-2a}}
\longrightarrow
\frac{J_\infty(E_*)}{\mathscr X'(E_*)}.
\]

There are accompanying exact-scale limits for the nearby numerator, denominator, and transform zeros. On each fixed compact energy disk along a cofinal sequence, away from fixed neighborhoods of the zeros of X, the correct upper-half-plane sign follows automatically at large a. The unresolved issue on that compact has therefore been localized to those neighborhoods, with an explicit source ratio governing simple real poles.

The theorem does **not** exclude nonreal target zeros or prove the companion ratio positive at every real target zero. A companion zero, multiple target zero, or common factor needs its own treatment. Exact negative-energy controls also rule out a tempting global Pick-function shortcut; the growing-solution background must be retained.

The included 240/360-digit polynomial calculations are exploratory diagnostics. Agreement between those runs is not directed arithmetic and is not a proof of residue signs or a complete pole count.

## 3. The local Bessel gate succeeds for two actual higher-order sources

The [local certificate](local_gate/LOCAL_WINDOW_CERTIFICATE.md) proves that every zero in

\[
|z|\le\sqrt{2000}=20\sqrt5
\]

is real for each complete finite sum

\[
F_{a,M}(z)=c_0K_{iz/2}(a)
+\sum_{n=1}^{M}c_n\bigl(K_{n+iz/2}(a)+K_{n-iz/2}(a)\bigr)
\]

at `(a,M)=(10,50)` and `(20,100)`.

| Source | All denominator poles in `|E|<500` | Graeffe rounds | Boundary polynomial degree | Bernstein cells / depth |
|---|---:|---:|---:|---:|
| `a=10, M=50` | 6, all simple positive real | 3 | 24 | 1 / 0 |
| `a=20, M=100` | 8, all simple positive real | 5 | 49 | 5 / 4 |

The checker reconstructs every coefficient from rational enclosures of the primitive theta and Bessel-I series, including their complete tails. Graeffe squaring plus a strict Rouche inequality counts **all complex denominator zeros** in the disk. Disjoint real sign-change intervals exhaust that count. Full interval enclosures certify strictly positive residues at every pole and exclude numerator cancellation.

Finally a Chebyshev boundary polynomial is converted to Bernstein form. Strict lower bounds on a finite interval partition prove the sign on the **entire** upper semicircle. The maximum principle on the punctured half-disk then supplies the interior sign. The ordinary self-adjoint Bessel Weyl identity excludes nonreal transform zeros, and positivity of the original kernel excludes negative energy.

The proof includes exact rejection controls for an interior complex-pole example and a real-pole example with negative residue. Both have the apparently correct outer boundary sign. This checks that the consumer does not silently omit those essential hypotheses.

The two denominator counts are not counts of zeta zeros or even counts of transform zeros. The theorem concerns reality of all transform zeros in the stated disk. It does not extend the verified height for zeta, and these fixed-ratio examples do not constitute a cofinal family.

## 4. A deterministic cosine transform preserves the native problem

The [cosine/native manuscript](cosine/COSINE_PHASE_AND_NATIVE_SYNTHESIS.md) gives, for `1<alpha<2`, a deterministic transfer from an explicit two-exponential density `q_alpha` to the native arithmetic density `p_alpha`, bypassing the earlier log-gamma-noise construction. The multiplier has order `3/2-alpha`; at `alpha=3/2` it is the unit-modulus phase

\[
m(1/2+it)=2^{it}
\frac{\Gamma(1/4+it/2)}{\Gamma(1/4-it/2)}.
\]

This is implemented by cosine transform and inversion in logarithmic coordinates. Those classical operators are credited explicitly. The new calculation applies them to the literal native discrete generators, retaining their original coefficients and norm.

For `b_n(k)={k/n}` in `ell^2(N,1/[k(k+1)])`, define

\[
S(y)=\sum_{k\ge1}\bigl(\sin(y/k)-y/k\bigr),\qquad
V_n(y)=\frac yn\log n+\frac{S(y)}n-S(y/n).
\]

The logarithmic compensator is forced by the harmonic cutoff. The complete finite approximation error becomes exactly

\[
\mathcal E_N=\frac2\pi\inf_{c_2,\ldots,c_N}
\int_0^\infty
\left|\sin y-\sum_{n=2}^N c_nV_n(y)\right|^2\frac{dy}{y^2}.
\]

This is a transformed presentation of the classical native RH criterion, not a proof that the minima vanish. The manuscript constructs the transported off-line-zero functional, so the obstruction survives the transformation. It also proves the native fractional Sobolev estimates needed across the full alpha strip.

For a native residual bounded by B, its reciprocal-cell embedding `E f` satisfies the complete frequency bound

\[
\int_Y^\infty|\mathcal C E f(y)|^2dy\le\frac{16B^2}{\sqrt Y},
\qquad Y\ge2.
\]

Thus a certified finite-frequency computation can be extended to the full norm once its coefficient/residual budget is controlled. A separate explicit bound encloses the complete defining tail of each S series.

The natural Mobius coefficients synthesize the target uniformly on compact frequency intervals, and the note proves this using the full series. Their native initial residual is exactly `k A_N`, where `A_N=sum_(n<=N) mu(n)/n`. Consequently their complete error is at least

\[
|A_N|^2\bigl(N+1-H_{N+1}\bigr).
\]

The safe compact-convergence and large-frequency tail estimates do not meet on a common asymptotic range. Exact prefix interpolation also forces a growing coefficient budget. These calculations identify a real construction problem rather than promoting compact convergence into full-norm convergence.

## Review and reproduction

The [claim ledger](CLAIMS.md) gives exact quantifiers and failure boundaries. [Validation](VALIDATION.md) distinguishes analytic proof review, exact finite checks, primitive-source certificates, and ordinary diagnostics. The [source ledger](SOURCES_AND_PROVENANCE.md) records inherited identities, primary references, and overlap. `MANIFEST.json` binds every delivered file except itself by SHA-256 and Git blob SHA-1.

Reviews are in [anchor](anchor/REVIEW_ANCHOR.md), [cofinal Bessel](bessel/REVIEW_COFINAL.md), [local gate](local_gate/REVIEW_LOCAL_GATE.md), and [cosine/native](cosine/REVIEW_COSINE.md). The coordinating mathematical review is [here](COORDINATOR_REVIEW.md).

Run from the repository root:

```sh
python -I -S -B standalone/2026-10-31-swarm-continuation/anchor/verify_anchor_followup.py
python -I -S -B standalone/2026-10-31-swarm-continuation/bessel/verify_companion_structure.py
python -I -S -B standalone/2026-10-31-swarm-continuation/cosine/verify_cosine_native.py
python -I -S -B standalone/2026-10-31-swarm-continuation/local_gate/verify_local_gate_controls.py
python -I -S -B standalone/2026-10-31-swarm-continuation/local_gate/certify_bessel_window.py --a 10 --order 50 --radius 500
python -I -S -B standalone/2026-10-31-swarm-continuation/local_gate/certify_bessel_window.py --a 20 --order 100 --radius 500
```

These exact checkers need only the Python standard library and the frozen parent interval file. Diagnostic scripts have separate dependencies and are not acceptance gates. The parent packet must remain present, which is why the prepared continuation targets its branch. The delivery notes record whether GitHub publication has completed.
