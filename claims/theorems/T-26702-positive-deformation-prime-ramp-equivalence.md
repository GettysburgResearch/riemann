# T-26702 — Positive deformation and the prime-ramp frontier

Claim ID: `T-26702`  
Title: Positivity-preserving finite carry construction is unconditional; its sharp mass is exactly the RH-equivalent ordinary-prime ramp  
Status: **PROPOSED COMPLETE SYNTHESIS FROM STATED DEPENDENCIES — RH REMAINS UNPROVED**  
Authoring agent: `gpt56-08`  
Created: 2026-08-08  
Dependencies: `L-26703`; PR #248 `L-24517`, `T-24504`  
Scope: exact separation of finite positive geometry from the global arithmetic scalar

## 1. Unconditional positive deformation

For every integer

\[
X\ge104301,
\]

`L-26703` constructs a nonnegative carry-row vector `b_X^+` satisfying every ordinary-prime constraint

\[
v_p(b_X^+)
\le p^{-1/2}\log(X/p)
\qquad(p\le X)
\tag{T-26702.1}
\]

and attaining the exact ordinary-prime objective

\[
\boxed{
J_{\mathbb P,X}(b_X^+)
=P_X
:=\sum_{p\le X}\frac{\log p}{\sqrt p}\log(X/p).
}
\tag{T-26702.2}
\]

The vector is obtained by a finite linear programme in the nonnegative physical-coordinate cone. Its exact dual is the cone of monotone strongly additive functions. Finite dyadic rigidity shows that every dual vector differs from the logarithmic/von-Mangoldt ray only in the already feasible outer region.

Thus a positive finite packing exists at every endpoint without DCRS, Greedy Slack, pointwise Green positivity, a monotone cover, or a signed-flow convergence theorem.

## 2. The sharp mass is still the arithmetic scalar

The parabolic seed has

\[
J_{\mathbb P,X}(b_X^{(0)})
\ge4\sqrt X-O(\log^2X)
\tag{T-26702.3}
\]

by `L-24517`. The exact positive correction in `L-26703` changes its objective by

\[
P_X-J_{\mathbb P,X}(b_X^{(0)}).
\tag{T-26702.4}
\]

Consequently the positive construction has critical mass if and only if the prime ramp itself does:

\[
\boxed{
J_{\mathbb P,X}(b_X^+)
\ge4\sqrt X-X^{o(1)}
\iff
P_X\ge4\sqrt X-X^{o(1)}.
}
\tag{T-26702.5}
\]

No geometric or positivity loss remains between the two sides.

## 3. RH equivalence

The equivalence triangle `T-24504`, together with the `O(log^2X)` removal of higher prime powers in `L-24517`, gives

\[
\boxed{
\mathrm{RH}
\iff
P_X\ge4\sqrt X-O_\varepsilon(X^\varepsilon)
\quad\text{for every }\varepsilon>0.
}
\tag{T-26702.6}
\]

Combining (T-26702.2), (T-26702.5), and (T-26702.6),

\[
\boxed{
\mathrm{RH}
\iff
\text{the unconditional positive deformation }b_X^+
\text{ has entropy/objective }4\sqrt X-X^{o(1)}.
}
\tag{T-26702.7}

The theorem does not prove that asymptotic. It proves that all finite positivity and transport requirements can be met **without adding any new debt beyond the exact RH-equivalent scalar**.

## 4. Consequences for the live proof graph

The following proposed global hinges are now known to be coordinate choices rather than independent finite-existence problems:

```text
DCRS / Greedy Slack;
positive deformation of the canonical Green state;
signed constraint-dipole feasibility;
finite Gamma-carry positive minorants;
endpoint-scale positive packing.
```

They may still provide useful estimates, but a proof cannot close merely by constructing a positive object: `L-26703` already constructs one. The source-specific arithmetic task is to prove that its exact objective `P_X` stays within subpower distance of the parabolic main term.

The dual theorem gives a precise firewall. The normalized logarithmic weights

\[
y_p=\frac{\log p}{\log X}
\]

are the extremal interior dual ray. Any attempted estimate that removes this ray has discarded the RH-bearing mode.

## 5. Recommended direct attacks

Three live coordinates remain genuinely relevant to the scalar:

1. **Dyadic two-contact descent.** PR #269 compresses the inverse-zeta source to two carry contacts and two bottom Green charges. A half-scale recurrence for its odd-column leakage would control the logarithmic ray without estimating the full Green energy.
2. **Annular additive rigidity.** PR #267 controls all transverse monotone-additive modes by annular curvature. It remains to combine that rigidity with a source-specific recurrence for the logarithmic mode.
3. **Signed Green–Skorokhod contact debt.** PR #270 retains the complete clipped dipole before taking positive parts. A half-scale contact-cell recurrence would give the needed scalar bound.

The present theorem shows exactly how these routes must be judged: they must estimate the logarithmic scalar, not merely produce feasible positive geometry.

## 6. Status boundary

```text
finite nonnegative deformation                 PROPOSED COMPLETE
ordinary-prime feasibility                     PROPOSED COMPLETE
zero additional positivity/transport tax       PROPOSED COMPLETE
objective equals the actual prime ramp          EXACT
prime-ramp lower bound                          OPEN / RH-EQUIVALENT
Riemann Hypothesis                              UNPROVED
```

There is no genuine unconditional RH proposal on this branch at present. A future full proposal must add a noncircular estimate of the scalar in (T-26702.6).