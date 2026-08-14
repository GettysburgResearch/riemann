# T-91659 — The native-root clause compiler returns an exact discrepancy and separator

Claim ID: `T-91659`  
Status: **PROVED FAIL-CLOSED COMPILATION; NRCT NOT ESTABLISHED**  
Created: 2026-08-14  
Review cutoff: `2026-08-14T16:57:25Z`  
Current main at cutoff: `9c7538559d7f56c2914b39aed5a1fb3fbf7ce131`  
Primary frontier: PR `#469` at `3cf685181bd367b92cdcfeef9249e0b9b542a09e`  
Cross-branch inputs: PR `#464` at `2eb70463f3d0ae791a9f140694d2ace7032ae864`, PR `#467` at `d5e03a3a63bd05b43abf4b5e37905f86e9ec59d6`, PR `#454` at `a0409d54250bc211d62718a1aedb6fa020d7f091`  
Depends on: `R-91102`, `L-91671`, `L-91673`, `L-91674`, `L-91682`, `L-91684`, `L-91685`, `T-91314`, `R-91686`, `L-91686`, `L-91687`  
RH status: **unproved**

## 1. Purpose

Compile the fixed-window root score-Hall route of PR `#464` into every clause of the Native-Root Capacity Theorem `T-91314`, in the exact native normalization of `L-91377`--`L-91379`. If the compilation fails, expose an exact discrepancy and continue through the finite primal/Farkas and direct radix-four routes.

The compilation is fail-closed: no formal positive-linear identity is promoted to a finite physical root packet without source ownership, one-use capacities, ports, and literal `Y_4` slack.

## 2. What PR `#464` does compile

On its certified fixed root window, `L-91673` supplies one common Hall transport for score, target, and every component row. At the deterministic fiber level it proves:

\[
\text{signed score}=\text{positive residual score},
\]

\[
\text{signed target}=\text{positive residual target}+\text{positive slack},
\]

\[
\text{signed row}=\text{positive row bonus}+\text{positive residual row}.
\]

`L-91674` proves formal positive-linear commutation with endpoint integration, common-parent summation, ordinary response, radix-four response formed after the ordinary maps at `q` and `4q`, same-index child placement, and one global quantizer.

The causal reset in `T-91657` supplies

\[
Y_b\le X/67,
\qquad
\alpha_b\ge0,
\qquad
\sum_b\alpha_b<\frac18.
\tag{T-91659.1}
\]

Thus the following portions of `T-91314` compile on the frozen hypotheses:

```text
fixed-window score/target/row Hall algebra         PASS;
formal ordinary/detail commutation                 PASS;
same-index child scaling                           PASS;
child endpoint contraction                         PASS;
total recursive coefficient below 1/8              PASS.
```

## 3. Exact clauses that do not compile

### 3.1 Finite source-owned endpoint realization

The formal endpoint theorem begins with a positive endpoint fiber already represented in one typed vector space. It does not construct the exact finite equality seed from the continuum Volterra packet.

`R-91102` gives the exact discrepancy at `X=3,m=2`:

\[
\boxed{
D_{\rm fc}
=4\sqrt2-4\sqrt3
+
\frac{5\sqrt2}{2}\log\frac32
>\frac1{10}.
}
\tag{T-91659.2}
\]

Therefore the continuum endpoint integral cannot be identified with the finite equality row without an explicit mismatch/current realization generator.

### 3.2 Ordinary and radix-four one-use capacities

The equalities asserted in `L-91673.4--.5` are valid after an actual finite identity

\[
c_X=B_X+R_X\widehat Z_X
\]

has been constructed. The live packet does not export that finite source-owned identity with every mismatch, collar, omission, taper, and base correction included.

Independently, `R-91686` proves that the raw PR `#469` leaf basis is not a substitute. At `(X,p,q)=(136,67,2)`, current plus child overdraws both native ordinary and detail capacity by

\[
\delta=\frac1{\sqrt{134}}\log\frac{68}{67}>\frac1{810}.
\]

For every prime `p>=71`, an infinite family with `X=2(p+1)` has raw-current ordinary overdraw greater than `5/834` before the terminal child is added.

### 3.3 Boundary and common-port ownership

PR `#464` names boundary coordinates abstractly and proves formal linear commutation. It does not export the live one-use port vector or an atomwise partition assigning every finite correction to exactly one owner. The port clause of `T-91314` therefore remains uncompiled.

### 3.4 Exact current debt normalization

`L-91375` proves

\[
\Delta(P_{\rm cur})\le2m(P_{\rm cur})
\]

after entry into the positive typed causal cone. PR `#464` instead states an absolute finite equality correction `C_fin` for its root frame. It does not identify that statement with the literal target-mass inequality `T-91314.4` for the fully corrected native current packet.

### 3.5 Provenance

Deterministic Hall fibers retain labels formally, but the missing finite realization means that the actual arithmetic source occurrences consumed by the mismatch, collar, omission, shared port, current row, and recursive children are not exported as one atomwise partition of the form required by `L-91671`.

### 3.6 Immutable `Y_4` slack

No current-plus-child certificate supplies an explicit vector

\[
s(q)=\Omega_X(q)-\Xi_{d_X^{\rm cur}}(q)-R_X^{(4)}(q)\ge0
\]

with a frozen bound on

\[
\sum_qY_4(q)s(q).
\]

The positive `Y_4(2)` separator in `R-91686` shows that this omission is load-bearing, not cosmetic.

## 4. Clause-compiler verdict

The exact compiler output is

```text
T-91314 source/scale clause                  PARTIAL PASS;
T-91314 recursive mass <1/8                  PASS;
T-91314 ordinary one-use capacity            NOT COMPILED;
T-91314 detail one-use capacity              NOT COMPILED;
T-91314 boundary/common port                 NOT COMPILED;
T-91314 current debt <=2 target              NOT COMPILED AT ROOT;
T-91314 atomwise provenance                  NOT COMPILED;
T-91314 immutable Y4-weighted slack          NOT COMPILED;
PASS_NATIVE_ROOT_CAPACITY_THEOREM             FALSE.
```

This is an exact discrepancy, not a claim that NRCT itself is false.

## 5. The finite stopped-leaf LP is now deterministic

The alternative PR `#467` route asks for variables

\[
0\le u_e\le a_e,
\quad
T(U)=T(O),
\quad
S(U)\le S(O),
\quad
R_j(U)\ge R_j(O).
\tag{T-91659.3}
\]

`L-91686` proves that the leftmost target-Lorenz fill is exactly the common score-minimizing and all-row-maximizing basis of the full box LP. Therefore:

```text
leftmost basis passes every row and score constraint  => LP feasible;
leftmost score or row margin fails                    => exact threshold Farkas separator.
```

No search over arbitrary non-leftmost bases is needed. The remaining work is directed certification over the finite activation/cutoff cells.

## 6. Exact direct radix-four closure program

For a fixed source-owned recursive packet with detail response `R^(4)`, `L-91687` reduces current construction to

\[
 d(s)=B^{-1}\mathcal R_4
 [\Omega_X-R^{(4)}-s]\ge0,
\]

\[
0\le s\le\Omega_X-R^{(4)},
\]

with objective

\[
\min\sum_qY_4(q)s(q).
\tag{T-91659.4}
\]

The ordinary capacity follows automatically from the positive radix-four inverse. Columns with `Y_4(q)=0` are exact score-free repair directions. Their top two row effects are explicit in `L-91687.14--.15`.

## 7. Minimal missing certificate: SONTR

The surviving closure theorem is the following.

> **Source-Owned Native Thinning and Realization (`SONTR`).** For every sufficiently large native root packet, export one finite source-labelled allocation and one detail-slack vector `s` such that:
>
> 1. every source occurrence is assigned once among current, recursive child, stop, finite correction, and residual;
> 2. recursive endpoints and coefficients obey (T-91659.1);
> 3. the reconstructed current row
>    \[
>    d=B^{-1}\mathcal R_4[\Omega_X-R^{(4)}-s]
>    \]
>    is coefficientwise nonnegative;
> 4. target, score, every component row, ordinary/detail capacity, every boundary reserve, and the one shared port are satisfied in the same native normalization;
> 5. the current target-mass debt obeys `T-91314.4`;
> 6. the unused slack obeys
>    \[
>    \sum_qY_4(q)s(q)=O(1)
>    \]
>    or at least `o(log^2 X)`.

A rational atomwise allocation plus directed algebraic interval certificate is a complete proof object. Any infeasible activation cell must return the threshold or general Farkas separator and identify the minimal missing target-null current-thinning generator.

## 8. Consequence and exact boundary

If `SONTR` is proved, it supplies NRCT and the resident subcritical/end-point consumers give the proposed RH implication. This theorem does not prove `SONTR`, NRCT, or RH.

```text
PR #464 fixed-window Hall algebra               COMPILED
PR #464 subcritical child budget                COMPILED
finite equality realization                     EXACT DISCREPANCY
PR #469 raw current+child capacity              EXACTLY SEPARATED
stopped-leaf arbitrary LP bases                 ELIMINATED
leftmost activation-cell margin campaign        OPEN / FINITE-DIRECTED
direct radix-four source-owned thinning         OPEN / SONTR
Native-Root Capacity Theorem                    OPEN
Riemann Hypothesis                              UNPROVEN
```
