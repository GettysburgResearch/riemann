# Hostile continuation of the native priority-surface route

## Verdict

The final positive surface estimate proposed in PR #669 is false.  The failure
is not numerical and not tied to the chosen priority order.  Prime pairs in
`(2 sqrt(X),3 sqrt(X)]` create an unavoidable positive surface of size
`>>(log X)^(-3)` while their contribution is cancelled in the signed scalar by
the even surface and empty-set survival reserve.

Accordingly, trying to improve the coarea estimate, optimize the ordering, or
sharpen the prime constants cannot prove `UPBF67`.

## Exact repair

The first-owner identity gives

\[
 A_\Phi=s_k\Phi(1)+V_\Phi-U_\Phi.
\]

Applying it to threshold potentials gives

\[
 E(t)=s_k+C_{\rm even}(t)-C_{\rm odd}(t).
\]

After Stieltjes integration the two formulas collapse to

\[
 A_\Phi=\int E(t)d\nu(t).
\]

For the duplicate-67 source, `E(t)=sum_(n<=t) beta(n)/n`.  Thus the apparent
surface simplification is exact only after its signed even/odd cancellation is
restored.  The positive priority flux was a deliberately lossy majorant, and
at critical normalization that loss is power-sized.

## Further attack

A separate attack moved the quadratic carrier rather than its source.  For

\[
 S_c(y)=(4\sqrt y-3+c)1_{y\ge1},
 \qquad -1\le c\le3,
\]

every quadratic native transform is globally nonnegative.  The removal
identity

\[
 S_c(Y)-\sqrt qS_c(Y/q)=(3-c)(\sqrt q-1)
\]

puts the complete labelled source back in the convergent `q^(-3/2)` regime.

At `c=-1`, the carrier is `4(sqrt(y)-1)` and vanishes at activation.  The
normalized quadratic transform is continuous across every source activation,
and its derivative is exactly the critical linear transform.  This eliminates
the atom ledger present in the ordinary quadratic descent.

The remaining weighted downward variation is nevertheless equivalent to RH.
The new carrier is therefore a cleaner target, not a hidden proof.

## Stress tests performed

The continuation also tested and rejected:

- changing the priority order;
- keeping only the positive Hasse min-cut majorant;
- pairing large inactive prime vertices without the even return surface;
- ordinary bounded variation of a positive supercritical transform;
- finite shifted-square inequalities as a substitute for the critical sign;
- source-blind Littlewood--Paley collapse;
- using the quadratic positivity margin without its critical exponential
  weight.

Every failed mechanism loses exactly the signed reciprocal-prefix cancellation
restored by `L-99970`.

## Current boundary

```text
positive priority flux as final gate       false
balanced first-owner surface               exact
activation-free quadratic descent          exact
critical weighted downward variation       RH-equivalent
RH                                          unproved
```
