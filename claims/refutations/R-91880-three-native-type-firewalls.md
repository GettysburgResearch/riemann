# R-91880 — Three mandatory type firewalls for the explicit native two-sorted compiler

Claim ID: `R-91880`  
Status: **PROVED EXACT TYPE-SEPARATION / SUCCESSOR FIREWALL**  
Created: 2026-08-16  
Frozen predecessor: PR #506 at `3d44cf10f8b5f36fd06a57a745550a25142e3658`  
Comparisons: PR #507 at `dfaa70cd2eefcabbf6717e3da060792904c7f357`; PR #509 at `e01daee9cdfea35d2a7d2591f1df6c8080084119`; PR #503 at `db77e5792966edf080604fd4b69fb00f07739681`  
RH status: **unproved**

## 1. Forced `q=2` Hall-score obstruction

At the admissible root fibre `x=2`, the target Hall edge is forced:

\[
o=2\longrightarrow e=1.
\]

For `z=\sqrt{x/k}` put

\[
T(z)=4z-3,\qquad S(z)=5z-3,\qquad
g(z)=\frac{S(z)}{T(z)}.
\]

Then

\[
g'(z)=-\frac{3}{(4z-3)^2}<0
\]

and therefore

\[
\boxed{
g(\sqrt2)-g(1)
=
\frac{3(1-\sqrt2)}{4\sqrt2-3}<0.
}
\tag{R-91880.1}
\]

Thus a nonzero Hall edge cannot simultaneously be target-null, exact in declared score, and positive in the complete target/score/component-row packet cone.

The surviving output is two-sorted:

```text
positive target-bearing residual source;
target-null nonnegative physical row bonus;
separate nonnegative score surplus.
```

The row bonus is current-only and has no declared-score packet coordinate.

## 2. Native source tree is not the row-first rough lift

The native paired source is split before signed observation. The row-first `P_61` rough lift is the already-observed native packet plus a positive rough response reservoir. These operations do not commute after source labels are erased.

Consequently the compiler input marginal must be tied to either:

1. the exact paired native source tree; or
2. the exact native finite/Volterra hybrid marginal.

It may not substitute

\[
\sum_{m\ \mathrm{rough}}m^{-1/2}U_mN_{X/m}
\]

for the native parent. The strict `q=2` rough-lift separator of PR #507 remains a mandatory regression.

## 3. The Volterra infinitesimal packet is not a canonical causal packet

The exact native Volterra identity supplies positive infinitesimal packets `p_s`. It does not imply positivity of

\[
p_{py}-p^{-1/2}p_y.
\]

The frozen exact witness

```text
p=67, y=15, s=1005, row j=14
```

gives a strictly negative component. Hence the bulk Volterra packet is terminalized directly by the endpoint quantizer. Rough ownership and causal children are applied only to the anchored finite native source tree, where the canonical causal generator theorem is valid.

## 4. Normative boundary

```text
target-null complete Hall packet                 FALSE
row-only Hall bonus                              EXACT
residual-source score superordination            EXACT
native parent = row-first rough lift             FALSE
causal reset on Volterra infinitesimal packet    FALSE
causal reset on canonical anchored packet        RETAINED
signed finite comparison as positive source      FORBIDDEN
Riemann Hypothesis                               UNPROVED
```
