# Centered gamma: finitely many nonreal defects, one quantitative repair cost

**Proposed component proofs, pending independent mathematical review. RH is not proved.** This separate continuation uses the exact mean-centered family of PR #855, not its raw or intermediate-time approximants. No integrated status or parent source is changed.

## The new handle on the zero problem

For EVERY fixed finite stage, the centered density has the exact form

$$h_N(t)=(T_N^2-t^2)^{N-1/2}A_N(t),\qquad |t|<T_N,$$

with a positive even analytic amplitude. A complete two-sector endpoint argument proves that every sufficiently large zero of its Fourier transform is **real and simple**. Each stage therefore has only finitely many nonreal zero quartets. The threshold depends on N and is not numerically evaluated.

Move each exceptional quartet radially to the real axis, retaining all multiplicities and leaving the entire infinite real spectrum unchanged. The resulting entire function L_N is real-rooted. Its error is bounded by a scalar cost

$$\Delta_N=\sum_{\rho=a+ib\text{ in the first quadrant}}
       m_\rho\frac{b^2}{|\rho|^4},\qquad
\sup_{|z|\le R}|F_N-L_N|\le4R^2e^{R^2S_*}\Delta_N.$$

A uniform complete zero-tail estimate proves **unconditionally** that this cost converges to the corresponding off-axis defect of the ACTUAL xi function. Consequently Delta_N tending to zero is RH-equivalent. **That vanishing estimate remains open.** Real-rootedness of L_N by construction is not a proof that it approximates xi with vanishing error.

The same exceptional set has a second, algebraic description: the trace-Hankel tower's negative index eventually equals the number of DISTINCT nonreal quartets. Multiplicity weights remain in the form, but repeated roots do not count as independent evaluation coordinates. All sufficiently large roots are handled analytically; no finite zero scan is promoted to that conclusion.

## Why this is a different continuation

The target now tolerates transient complex pairs, collisions, high-frequency escape and splitting near multiple real zeros. It no longer asks for a false universal preservation law or global real-rootedness at every finite stage. A source-only Jensen integral gives the same defect without defining it through a fitted zero table. The finite-index theorem connects the gamma family to the earlier trace-Hankel programme without assuming a self-adjoint metric.

The attempted generic variance-flow finish is tested and fails for an exact real-rooted polynomial: p=(z^2-16)^2 under I-epsilon S develops pairs near 4 +/- i sqrt(137 epsilon). This is a changed polynomial, not xi. A separate NONCERTIFYING two-grid scout suggests a nonreal zero of the centered fourth stage near 30.4480568070 + 0.6599780504 i. Neither scout is used as a premise of the infinite arguments.

## Read and reproduce

Read [PROOF.md](PROOF.md), especially Sections 2--6. [SOURCE_LOCK.json](SOURCE_LOCK.json) fixes the exact predecessors and reading boundaries. [VALIDATION.md](VALIDATION.md) distinguishes source-density enclosures, finite synthetic algebra, the numerical scout and unperformed work.

From this directory:

```sh
python3 -I -S -B check.py --check results.json
python3 -I -S -B -O check.py --check results.json
python3 -I -S -B test_check.py
python3 -I -S -B -O test_check.py
```

The accepting checker uses standard-library integers and Fractions, including full exponential/simplex remainders. It checks 36 complete finite-gamma density enclosures against a separate partial-fraction formula, and exact moment, inertia and variance-operator identities. It does NOT certify an actual Fourier zero, q_N, Delta_N, an all-plane cutoff, or the written infinite theorems. No author-parent module is imported.

Optional, noncertifying, and requiring mpmath:

```sh
python3 -B scout.py --output /tmp/gfd-scout.json
```

The next decisive theorem is an upper bound making the complete Jensen surplus/weighted defect tend to zero along the integer-square gamma cascade. A larger positive finite Hankel block, faster absolute approximation, or independently repairing the zeros does not by itself supply it.
