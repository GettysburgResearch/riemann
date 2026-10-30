# Hypothetical joint-count landscape

**Status:** Floating-point reconnaissance, not a theorem or a complete-domain certificate. This note does not assert that the hypothetical estimate exists or that the changed geometry is analytically valid.

Use the PR #94 `Return/Formulas.lean` and its 31 actual windows at [commit `e5a82f72d8ff39a3cc1ad044e6acd727e77a3fc4`](https://github.com/GTimG/QuasiRiemannTracker/tree/e5a82f72d8ff39a3cc1ad044e6acd727e77a3fc4/submissions/2026-10-29-arvi-density/src/Submissions/arvi_density/Return), together with the physical face `B_P=49283557/50000000`, `lambda_P=4503/2000` and candidate cap `619/10000`. Hypothetically assume, uniformly for the same PR #94 row batches, masks, source choices and fixed early mesh (with the original small-power and height losses), a new count bound `#rows ≪ U^(R_J+epsilon)` and add it as a count branch on the *whole* rectangle `0<=delta<=3/4`, `0<=p<=1/2`, with squared selected slope `s=2 delta p` and exponent

```text
R_J(delta,p) = 3 (1-s)(1-delta) / (3-delta-2s).
```

This is the algebraic form of the PR #93 joint count extrapolated far beyond its proven gates. It is a strong new hypothesis: PR #93 does not supply it at low zero or selected-amplitude slopes. The scan combines it by taking the minimum with the existing old count and with existing branches only on their source windows and admission guards. It tests the old and physical conductor piecewise-linear edges and their possible line intersections; it does not reproduce analytic low/high estimates or prove that a joint branch is usable with the same selected rows, masks, or common mesh.

At `theta=0.87287234` and `h=0.8`, numerical differential evolution from three seeds found a worst return-row gap of approximately `-0.00370527` over the box; the apparent maximum occurs at `delta≈0.29762`, `p≈0.06194`, where the old count and the hypothetical count cross near `0.77206`. The corresponding zero level is approximately `0.64881` and squared selected slope approximately `0.03687`. This new bottleneck lies even further below both PR #93 gates than the original `delta=0.446` bin. These values are optimizer results, not a guarantee that all points satisfy the row inequality. `hypothetical_joint_scan.py` repeats the exploration; it uses NumPy/SciPy floating-point differential evolution, three random seeds, and no interval certification.

At this target and `h`, the elementary geometry gives `ell≈0.1751773`, `x≈0.3751773`, `y≈0.4496454`, positive floor saving `≈0.0033617`, and the original `Parameters` inequalities hold. However the current `BoundsN` assumptions `theta>0.873` and `ell<0.175` both fail. The existing `1/250` floor reserve also fails; a smaller positive reserve would be required. Every consumer of the widened analytic domain would need its own proof, along with source/normalization and complete row certificates.

A precise obstruction remains if one retains `y>0.44`, `h<0.806`, and merely positive floor saving while allowing the original `theta` and `ell` bounds to widen. Substituting `ell=11/3-4 theta`, `x=1+ell-h`, `y=h-2ell`, and `dp=h+10^-10` into the source floor margin gives

```text
floor saving = (9360000000000 theta - 1000000000000 h - 7360000000201) / 3000000000000.
```

Together with `h>0.44+2 ell`, positive saving forces `theta > 45400000000603/52080000000000 ≈ 0.8717357911`. This is only a bound inside this retained geometry, not a lower bound for zeta zeros or a claim that the bound is attainable. At its limiting corner the same numerical scan found a worst row gap around `-0.00022022`, but the floor and y inequalities are equalities there and the scan has no proof of global optimality.

An independent agent checked the PR #93 rational component and variable mapping, source window and guard transcription, capacity parsing, exact geometry barrier, and numerical reproduction. This does not certify the floating-point maximization or prove the hypothetical count or widened analytic inputs.

The new bottleneck also conflicts with a proposed route through the **broad arbitrary-ideal-slot selected norm**: its slope `s≈0.03687` is below `1/6`. The independently reviewed [power-source counterexample](../2026-10-29-natural-norm-obstruction/README.md) rules out the all-source shape `L + Y^(1-s)L^s` for every `0<s<=1/6` in that broad interface, using squarefree prime rows and sixth-power ideal slots. This counterexample does not establish zero witnesses for those rows, does not refute the hypothetical *joint* count, and does not cover the physical detector's prime-only slots. A viable proof would need to exploit one or more of those additional restrictions or use a different route; the failed broad seed cannot be inserted as a black box.
