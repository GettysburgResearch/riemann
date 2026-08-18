# T-98000 — Eventual completed-parity Lorenz feasibility collapses to two zero-hinge signs

Claim ID: `T-98000`  
Status: **UNCONDITIONAL REDUCTION; BOTH ZERO-HINGE SIGNS OPEN**  
Created: 2026-08-18  
Frozen base: PR #596 at `40bfd7e70521f4205e95d3960812a6cef6073c05`  
Depends on: `L-98000--L-98003`; PRs #584/#591/#596  
RH status: **unproved**

Let

\[
H_X=T_E(X)-T_O(X)
\]

be the native signed target and

\[
R_X=R_E(X)-R_O(X)
=5c_X(2)+3c_X(3)
\]

the native signed `5:3` scalar. The latter is `GPC67` from PR #589 and the zero
hinge `D_X^+(0)` in PR #591.

Then there exists `X_0` such that for every real `X>=X_0`, completed-parity
scalar Lorenz feasibility at `X` is equivalent to

\[
\boxed{H_X\ge0\quad\text{and}\quad R_X\ge0.}
\tag{T-98000.1}
\]

Consequently, at eventual-uniform scope,

\[
\boxed{
\mathrm{CPSL}_{67}
\Longleftrightarrow
\mathrm{GTC}_{67}\ \wedge\ \mathrm{GPC}_{67}.
}
\tag{T-98000.2}
\]

## Proof

`CPSL67` always implies both inequalities. Target capacity is the negative-dual
ray, and at `lambda=0` the Lorenz slack is exactly `R_X`.

Conversely, take `X` sufficiently large for `L-98002`. Then

\[
T_O(X)>T_{E,+}(X),
\tag{T-98000.3}
\]

where `T_(E,+)` is the target capacity of every even atom with positive scalar.
By `L-98000/L-98001`, those are exactly the even indices `k<X/2`, they precede
every zero-scalar atom in the Lorenz order, and all atom ratios lie in `[0,6)`.

Assume `H_X>=0`. Then `T_E>=T_O`, so after saturating every positive-scalar
even atom, the remaining target demand

\[
T_O-T_{E,+}>0
\]

can be filled entirely from the zero-scalar even shell `X/2<=k<=X`. Therefore
the exact Lorenz envelope at the odd target is

\[
\boxed{\Phi_X(T_O)=R_E.}
\tag{T-98000.4}
\]

The scalar-superordination clause is now precisely `R_O<=R_E`, namely `R_X>=0`.
This proves (T-98000.1).

Equivalently, whenever total target capacity holds, the minimizing dual parameter
is eventually

\[
\boxed{\lambda_*=0.}
\tag{T-98000.5}
\]

Every interior hinge `0<lambda<6` and the high tail `lambda>=6` are automatically
above the zero-hinge value.

## Consequences

1. **The continuous Lorenz frontier is not the final arithmetic obstruction.**
   At sufficiently large endpoints it carries no independent condition beyond
   target capacity and the native scalar sign.
2. **`LBP67` is stronger than necessary away from zero.** Its all-`lambda`
   Euler-minus cone remains a valid sufficient theorem, but eventual `CPSL67`
   does not require proving that stronger cone.
3. **The conclusion-producing scalar route is root-only.** PR #594's
   `RBLPTE67` and PR #590's balanced large-prime Type-II frontier now target the
   actual remaining scalar sign directly.
4. **Target capacity is not bookkeeping.** `L-98003` proves independently that
   `GTC67 -> RH`; its sign also contains zero-free-strip strength.
5. **Either zero hinge would close RH.** The frozen Mellin consumer gives
   `GPC67 -> RH`, while `L-98003` gives `GTC67 -> RH`.

The exact surviving graph is

\[
\mathrm{CPSL}_{67}
\Longleftrightarrow
\mathrm{GTC}_{67}\wedge\mathrm{GPC}_{67}
\Longrightarrow\mathrm{RH},
\]

and separately

\[
\mathrm{GTC}_{67}\Longrightarrow\mathrm{RH},
\qquad
\mathrm{GPC}_{67}\Longrightarrow\mathrm{RH}.
\]

## Exact boundary

```text
scalar/target ratio rho_* ordered in [0,6)       PROVED
Lorenz atom order = increasing source index       PROVED
one-switch Lorenz envelope                        PROVED
positive squarefree zero-scalar shell             PROVED ASYMPTOTIC
marginal lambda*=0 eventually                     PROVED CONDITIONAL ON TARGET CAPACITY
CPSL67 <-> GTC67 and GPC67 eventually             PROVED EXACT REDUCTION
GTC67                                              OPEN / RH-BEARING
GPC67                                              OPEN / RH-BEARING
Riemann Hypothesis                                 UNPROVEN
```

This theorem eliminates a layer of convex geometry. It does not claim either
remaining zero-hinge arithmetic inequality.