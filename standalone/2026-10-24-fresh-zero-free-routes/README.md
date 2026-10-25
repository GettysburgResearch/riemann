# Fresh routes beyond the current zero-free moment envelope

Status: exploratory research with complete component proofs and explicit open analytic estimates. **No new zero-free boundary is established.**

Scope: ordinary zeta, the pinned Eisenstein character family, and the actual theta/Weil source. These are separate routes; their conclusions are not silently combined.

Date: 24 October 2026.

Base: `GettysburgResearch/riemann` main at `f99d9e3908dde4865377c75d9ca051c1f545bf4f`. Exact external and repository dependencies are in [SOURCES.md](SOURCES.md).

## The research change

Recent work has improved structured Gauss sums and projected pieces of the inverse. The complete native inverse estimate remains open. The new packet changes the arithmetic coefficient itself, gives a direct positive-count target for ordinary zeta, and tests whether the proposed spectral approximants can actually converge to their intended source.

| Route | Component established in this packet | Exact unfinished task | Consequence if completed |
|---|---|---|---|
| [Positive marked count](POSITIVE_MARKED_COUNT_TARGET.md) | Exact removal of the pole at one; a single prime-factor mark detects zeros of every multiplicity; a real-integral principal term | For one nonzero smooth profile, prove the complete marked remainder is `O(X^(3/4+epsilon))` for every epsilon | Ordinary zeta is zero-free in `Re s>3/4` |
| [Continue the actual coefficient](arithmetic/DIRECT_NATIVE_APPLICATION.md) | Positive-measure coefficient-transfer theorem; an ordinary squarefree endpoint; exact recovery of the native Mobius inverse at `z=-1` | Prove the fractional coefficient mean on the complete native range, with its original masks, heights, and profiles | Supplies the missing native hypothesis of PR #1014; its other pinned interfaces would then give `Re s>437/500` |
| [Coherent transport across cutoffs](family/COHERENT_LOG_TRANSPORT.md) | Exact prime-power identity at a common character and frequency; precise envelope absorption | A signed estimate for the coupled prime blocks beyond the present marginal M1 range | A new arithmetic input to the detector, rather than another optimization of the old inputs |
| [Source-sensitive resolvents](spectral/THETA_JUMP_FORM_AND_RESOLVENT_DELOCALIZATION.md) | Full theta jump identity; quantitative delocalization and a deep-shift zero obstruction; necessary window for variance matching | Establish the variance-matched legal shift and identify its limit with Xi | A viable source-selection step; no zero-free conclusion follows from normality alone |

The numerical half-planes in the last column are **conditional consequences**, not results of this packet. The source-qualified working benchmark remains `B_flat=0.874886647039964...`. This packet does not independently certify that imported preprint or change the repository's integrated status.

## 1. A direct ordinary-zeta attack with one positive arithmetic weight

For a fixed nonzero `W in C_c^infinity((1,2))`, chosen nonnegative if desired, set

\[
A_\omega(X)=\sum_n\mu^2(n)\omega(n)W(n/X).
\]

The note defines an exact principal term `C_omega(X)` using only the explicitly zero-free disk around the pole at one. It gives both a contour definition and a real-integral formula. No information about high zeros enters that definition.

The complete implication is

\[
\bigl|A_\omega(X)-C_\omega(X)\bigr|
 \ll_{W,\epsilon} X^{3/4+\epsilon}\quad\text{for every }\epsilon>0
\quad\Longrightarrow\quad
\zeta(s)\ne0\quad(\Re s>3/4).
\]

Why a single mark matters: the unmarked squarefree series is `zeta(s)/zeta(2s)`, which is holomorphic at a zeta zero. Marking by `omega(n)` inserts `log zeta(s)`. At a zero of multiplicity `m`, the local term contains `(s-rho)^m log(s-rho)`. It still vanishes at its center, but cannot be continued holomorphically around it. A zero of the smoothing's Mellin transform does not remove the branch.

The arithmetic error estimate is not proved. The first explicit hyperbola attempt reaches the desired `3/4` scale on its small-prime side, but separately estimated large-prime errors have exponent `(1+beta)/2`, approximately `0.9374` at the imported benchmark. Matching that hybrid main term to the exact `C_omega` is another required step. This identifies the signed prime/squarefree remainder as the object to study.

This route lies outside the particular theta direct-majorant mechanism whose `13/15` floor was already recorded in PR #1009. It is not an improvement to that old majorant.

## 2. A direct bridge from ordinary coefficients to the missing inverse

On the original physical rows define

\[
V(z;u)=D^{-1/2}\sum_n\mu^2(n)z^{\omega(n)}
       \psi_u(n)(Nn)^{it}W(Nn/D).
\]

The endpoints are exact: `V(1)` is the ordinary squarefree sum, and `V(-1)` is the native Mobius inverse. The polynomial degree in `z` is at most

\[
(1+o(1))\frac{\log D}{\log\log D}.
\]

Consequently, extrapolation from any fixed positive-measure set of real coefficient parameters to `-1` costs only `D^o(1)`. The proof allows constants to depend arbitrarily on the parameter. A countable cover finds a positive-measure subset with common constants, and an explicit polynomial interpolation inequality completes the transfer. The height and profile orders can also be fixed before consuming the result.

This is stronger than simply assuming uniform estimates on an interval. It also shows exactly why proving more fixed integer divisor orders does not solve the problem: a concrete sublogarithmic-degree counterexample vanishes eventually at every fixed positive integer while remaining large at `-1`.

The source-dependent endpoint adapter at `z=1` is proved using the full ordinary moment explicitly stated in Xu--Sang. What is still missing is the noninteger mean, for example

\[
\sum_{u\ {m sixth\text{-}power\text{-}free}}w(u)|V(z;u)|^2
 \ll (UD)^\epsilon(1+T)^A p_J(W)^2
       \left(U+U^{1/6}D^{4/5}\right),
\]

for a positive-measure set of `z`, throughout the complete native range and its stipulated margins. This goes directly to the actual inverse; it introduces no Gauss-coefficient substitution or new projection complement.

The [fractional detector note](arithmetic/FRACTIONAL_ZERO_DETECTOR.md) also checks the first plausible density-based closure. Even an optimistic extension of the existing density formula leaves an exact `5/48` deficit at `sigma=3/4` against this native target. Separate zero-count and value bounds do not prove it. A useful next estimate must retain their joint or signed structure.

## 3. A spectral direction that survives the first obstruction

The full theta annihilator gives an exact weighted jump identity, including every prime power. The hyperbolic term remains; imposing two pole constraints does not make it disappear.

Broad, mass-one approximate null vectors imply that normalized resolvents chosen with a safe negative spectral margin have `L2` norm tending to zero. Their Fourier transforms are one at zero, so they cannot converge locally uniformly there. For the explicit deep shift `kappa=-exp(4a)`, the rescaled transform converges to `sin(w)/w`; a real zero approaches zero. No zero-free entire multiplier normalized at zero, including a Gaussian factor, can repair that deep-shift failure.

A more precise positive target is the scalar equation `V_a(kappa)=V_X`, matching the second coefficient to Xi. Its real-zero products are automatically a normal family. The note proves a necessary near-bottom spectral window and a conditional existence bracket. Actual existence and identification with Xi remain open.

The companion [nullsource perturbation note](spectral/POSITIVE_NULLSOURCE_PERTURBATIONS.md) shows why positivity, the full annihilator, or minimization of successive finitely many moments cannot alone select theta. Its examples retain the complete source and its tails. These obstructions concern those selectors, not every possible spectral construction.

## 4. What was run and independently checked

The [experiment report](EXPERIMENTS.md) distinguishes exact finite algebra from exploratory character sums. Four reproducible scripts check:

- Coefficient interpolation, coefficient masses, fixed-integer countermodels, and density identities.
- Logarithmic transport, exact rough splitting, and zero-extended character multiplication, including deliberately rejected prime-only formulas.
- Global rational polynomial identities used in the explicit positive theta perturbation.
- Nine finite Eisenstein sextic rectangles, with exact residue arithmetic, complete collision zeros, and exact centered-moment interpolation. The largest has 762 physical rows and 35,284 squarefree columns, at `U=2500`, `D=125000`.

The finite values do not establish a uniform fractional mean or a zero-free region. They exercise the actual arithmetic interpolation interface at the declared finite scopes.

Independent team reviews are recorded separately and bound to file hashes. They found and prompted repairs to the irrational-parameter statement, the legal spectral-shift range, and the marked-count hyperbola scope. These are independent agent checks of the stated component arguments, not external peer review, formal verification, or certification of the imported analytic framework. The publication review records the exact frozen repository commit.

## Reading order and next mathematical work

1. Read [the direct marked-count target](POSITIVE_MARKED_COUNT_TARGET.md) for the most distinct ordinary-zeta formulation. The next calculation is the complete signed remainder after its exact main-term subtraction.
2. Read [the native application](arithmetic/DIRECT_NATIVE_APPLICATION.md), then [the coefficient theorem](arithmetic/COEFFICIENT_CONTINUATION.md), for the shortest connection to the current inverse consumer. Seek control on a positive-measure coefficient set, not another isolated integer order.
3. Use [coherent log transport](family/COHERENT_LOG_TRANSPORT.md) to keep cross-cutoff arithmetic relations before separate positive bounds. Its long-prime term has not been eliminated.
4. Pursue [variance matching](spectral/THETA_JUMP_FORM_AND_RESOLVENT_DELOCALIZATION.md) only with an existence argument and a full source-identification argument. Making an already safe shift more negative is ruled out as a convergence strategy.

The known remaining tasks are analytic, not publication or bookkeeping gates. Completing this packet does not complete any of those tasks.
