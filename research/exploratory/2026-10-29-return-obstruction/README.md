# A single-row obstruction to a larger PR94 return improvement

**Status:** Exact arithmetic about a specified scalar relaxation, not an impossibility theorem for L-functions or for other methods. This does not prove a zero-free region. The source formulas have been transcribed from tracker [PR #94 at head e5a82f72d8ff39a3cc1ad044e6acd727e77a3fc4](https://github.com/GTimG/QuasiRiemannTracker/tree/e5a82f72d8ff39a3cc1ad044e6acd727e77a3fc4/submissions/2026-10-29-arvi-density/src/Submissions/arvi_density); the imported analytic results and the connection from these formulas to the source return have not been independently audited here. The current `BoundsN` already restricts `theta>0.873`; the computation below deliberately relaxes that bound as well.

## Exact obstruction

Take the target `theta = 43643617/50000000 = 0.87287234`, exactly `0.001` below PR94's displayed `0.87387234`. Let `ell=11/3-4 theta`, `y=h-2 ell`, `kappa=2 theta-1`, and `d=h+10^(-10)`. At the one required top-edge parameter point

```text
delta = 9/20, p = 1/2, 793/1000 <= h <= 806/1000,
```

we give the PR94 computation two advantages: (i) all five branch formulas are allowed regardless of their actual window and admission guards; (ii) the numerator capacity is set to the upper bound `C=(31/500)d`, ignoring any further restriction from the physical face. We also round the cap branch's `branchZ` upward to its cap; this makes its exponent slightly smaller. Ignore the positive row reserve. With those relaxations, each branch still has `Ebranch-theta>0` throughout the whole displayed `h` interval. Thus that specific five-branch return cannot certify this target within this geometry, even under those favorable relaxations. This does not preclude a different branch, count, slot dictionary, geometry, or theorem.

For a non-old branch, transcribe the source quantities

```text
V = 5/6-delta
J = V*D + delta*(1-p)*A
N = (1-delta)*J + V*delta*U
Ebranch = 1/2 + 13h/75 - y/2 - ell/2 - 9d/100
          + delta/2 + delta*p*(ell-C/2) + (3/4)d*N/J.
```

For an uncapped count face `(B,lambda)`, set `D=3-p-4p/lambda`, `A=2-4p/lambda`, and `U=(1-p)(1-2pB/lambda)`. For a capped face at slot cap `z`, set `D=3-p`, `A=2`, and `U=(1-p)(1-2pz)`. The count parameters are `B=96232839/100000000`, `lambda=3853/2000`, `z=9999/100000` for `capC`; the weak count branch has `B` reduced by `7/4000`. The physical branch has `B=49283557/50000000`, `lambda=4503/2000`, and `z=31/500`. For `old`, use `D_old=3-p-2p/(3kappa)`, `A_old=2(1-p)(1-p/(3kappa))`, `J=V D_old+delta A_old`, and `N=(1-delta)J+delta A_old V/2`. These are exactly the conventions used by the source's `countJ`, `countN`, and `Ebase`, except for the stated optimistic enlargement of the cap.

With all other variables fixed at the displayed values, each branch's gap is affine in `h`; its endpoint values therefore prove strict positivity throughout the entire interval. The script computes rationally and asserts positivity:

```text
branch   gap at h=.793   gap at h=.806
old      .00534695540    .00577672176
C        .00334611962    .00374308540
capC     .00307786456    .00347043271
weakC7   .00340610681    .00380405598
capP     .00446161378    .00487686634
```

Run `python research/exploratory/2026-10-29-return-obstruction/check_obstruction.py`. The code uses Python `Fraction` throughout; decimals above are rounded output, not the verification method. The calculation is restricted to this single `(delta,p)` point, this `h` interval, this target and these five formulas. It establishes a barrier to this certificate scheme under the listed restrictions, not a lower bound on zeros or on the performance of every possible argument.

## How much would have to change at this point?

At `h=.793`, the optimistic `capC` gap is about `.00307786456`. Keeping its formula and optimistically setting `C=.062d`, make the capped count parameter `z` variable. The derivative of the gap is approximately `-.036424`, so the gap disappears only at `z≈.18449091444` rather than the present `z<.09999`. This is only a necessary single-point threshold for this branch. In the existing capped-face admission condition, `m>=.377` and `2m+lambda*z<=B`; even under the favorable additional assumption `B<=1` at its best value `B=1`, `z=.18449` requires `lambda<=1.333399`, compared with the current `1.9265`. A larger cap alone cannot reach this optimistic threshold while keeping those admission constraints. A new moment estimate would also need all the original uniformity, transport and detector inputs.

Alternatively, keep the current count formula and give the numerator capacity the form `C=c*d`. The same single point requires `c>=.09650037335`, compared with the relaxed cap `.062`. At this target the existing physical-face inequality is stronger still: it gives `C<=.03594404` at `h=.793`, whereas the required value is about `.0765248`. Thus enlarging just the formal `31/500` cap cannot close this gap without also improving or replacing the physical-face inequality. These thresholds trade off against each other; neither is claimed necessary if count and numerator are simultaneously improved, or if the geometry and branch formulas change.

More specifically, the physical budget has the form `C <= (2y-(2-B_P)d)/lambda_P`. Retaining the existing `lambda_P=2.2515`, achieving the required `C` would require `B_P>=1.10088878`. Alternatively, with the favorable constraint `B_P<=1`, it would require `lambda_P<=1.20602443`. These again are necessary only for this prescribed branch and point, with all other parameters held as above; they identify a quantitative moment-face target rather than establish its feasibility.
