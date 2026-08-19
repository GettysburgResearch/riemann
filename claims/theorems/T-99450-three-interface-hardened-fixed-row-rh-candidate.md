# T-99450 — Three-interface-hardened target-aligned fixed-row RH candidate

Claim ID: `T-99450`  
Status: **PROPOSED COMPLETE UNCONDITIONAL PROOF CANDIDATE — HOSTILE REVIEW REQUIRED**  
Created: 2026-08-20  
Base: PR #648 at `49be6640ae2714d1f907a6117c4a6d2aaa9f2f11`  
RH status: **not established by publication**

## 1. The three vulnerable interfaces

A hostile audit of PRs #646–#648 identifies three places where a locally valid
statement could fail under composition.

### Vulnerability A — child ownership

A smaller SHARP endpoint is not the raw support restriction of its parent.
`R-99450` gives the exact \(5:1\) density mismatch at
\((Y,Z,t)=(16,4,4)\).

**Repair:** `L-99450` uses the exact Radon–Nikodym derivative

\[
R_{Z\mid Y}(t)
=
\mathbf1_{t\le Z}\frac{T(Z/t)}{T(Y/t)}
\]

inside the random-key widths. Every child and the current are then literal
disjoint restrictions of one parent source.

### Vulnerability B — compact Hall was inherited but not independently replayed

Every downstream row theorem depends on the scalar compact target Hall gate.

**Repair:** `L-99451` reconstructs all 66 all-real prefix inequalities with
outward exact rational intervals. The smallest certified lower bound is at
\(t=13\):

\[
H_{13}>0.359317660598493127\ldots>\frac7{20}.
\]

The compact target flow is therefore independently certified.

### Vulnerability C — signed calibration was at risk of generationwise accumulation

A merely bounded local correction would acquire a geometric or leaf-count
loss if inserted independently at each descendant.

**Repair:** `L-99450` and `L-99452` identify the local correction as the exact
coboundary \(A-A\mathsf T\). It telescopes to the single root potential \(A\).
The canonical continuum frame is doubly clamped, so all activation atoms and
both Volterra homogeneous modes vanish; the retained-cell term decays and the
finite anchored ledger is uniformly bounded.

## 2. Hardened composition

Use the positive target-aligned row atom of PR #646:

\[
Q_Y(j)
=
\int_1^Y T(Y/t)\eta_j(t)\frac{dt}{t},
\qquad
\eta_j(t)>0.
\]

At each compact target fibre, `L-99451` supplies one target Hall flow. Since
every row is the same scalar target times \(\eta_j(t)\), the matched row cancels
exactly and only a positive residual remains.

Use the RN widths of `L-99450` for every rough child. The resulting child
operator \(\mathsf T\) is source-faithful, endpoint-decreasing, and nilpotent.
The positive frame satisfies

\[
P=J+P\mathsf T,
\qquad J\ge0.
\]

For the exact frame \(E=P+A\),

\[
E=J+E\mathsf T+(A-A\mathsf T).
\]

Resolving the finite DAG gives

\[
\boxed{
c_X(j)=D_X(j)+A_X(j),
\qquad
D_X(j)=J(I-\mathsf T)^{-1}\ge0,
\qquad
A_X(j)=O_j(1).
}
\tag{T-99450.1}
\]

No descendant calibration survives.

## 3. Analytic conclusion

`L-99453` gives

\[
\int_1^\infty c_X(j)X^{-s-1}\,dX
=
\frac{C_j}{s^2}
+
\frac{P_j(s+\frac12)}
{s^2\zeta(s+\frac12)}
\]

and the quantitative noncancellation

\[
P_j(\rho)
=
-\frac{\rho(\rho+1)}{1-\rho}j^{-\rho-1}
+o_\rho(j^{-\Re\rho-1}).
\]

The bounded root calibration has Mellin transform holomorphic in
\(\Re s>0\). Hence every off-line reciprocal-zeta pole survives in the
Mellin transform of \(D_X(j)\ge0\). Landau's real-abscissa theorem excludes
that pole. Functional-equation symmetry gives the proposed RH conclusion.

## 4. Interfaces removed from the conclusion chain

```text
raw endpoint cutoff child map               REFUTED / REPAIRED
coordinatewise row coupling                 REMOVED
normalized row-profile Hall campaign        NOT NEEDED
generationwise calibration sum              REFUTED / REPAIRED
positive knot atoms and positive anchors    NOT NEEDED
literal score and all-column capacity       NOT USED
safe-point thinning                         NOT USED
prime-square moat                           NOT USED
```

## 5. Remaining review boundary

The packet independently reconstructs compact target Hall, the row lift, the
RN child source, the calibration telescope, and the analytic pole transfer.

The remaining acceptance obligation is to reconstruct the complete native root
registry on the frozen endpoint-frame data:

```text
exact native frame E;
positive retained frame P;
finite anchored and omission ledger A=E-P;
one typed source label for every term.
```

This registry is explicit on the parent branches but is not rederived from all
historical raw artifacts in the lightweight replay. Failure of that exact
identity rejects the candidate.

```text
three vulnerable interfaces                REPAIRED
candidate composition on frozen registry   COMPLETE
independent acceptance of root registry    REQUIRED
accepted proof of RH                       NO
Riemann Hypothesis                         UNPROVEN PENDING REVIEW
```
