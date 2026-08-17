# T-97300 — Completed-parity reconstruction: exact downgrade and surviving RH frontier

Claim ID: `T-97300`  
Status: **PROVED EXACT CONDITIONAL REDUCTION; GLOBAL PRODUCER OPEN**  
Created: 2026-08-17  
Inputs: PRs #559, #561, #567, #568; `L-97300`–`L-97302`; `R-97300`–`R-97301`  
RH status: **unproved**

Define

\[
\mathcal R_X=5c_X(2)+3c_X(3).
\]

The exact fixed-row Mellin formulas give, with `z=s+1/2`,

\[
\int_1^\infty \mathcal R_X X^{-s-1}\,dX
=
\frac6{s^2}
-
\frac{3(1-2^{-z})(2-2^{-z})}{s^2\zeta(z)}.
\tag{T-97300.1}
\]

If `x=2^{-z}`, the finite numerator is

\[
-3(1-x)(2-x).
\tag{T-97300.2}
\]

For `Re z>0`, `|x|<1`, so it is zero-free.

Let `CPSL67` be the all-endpoint assertion that, after the complete finite rough
source is expanded with every cumulative parity retained, the exact scalar
Lorenz inequalities of `L-97302.3` hold.  Equivalently, this is the
source-complete target-plus-scalar producer called `GPHT*` in PR #567 and the
all-depth scalar Hall producer `ASHP67` in PR #568.

If `CPSL67` holds, the common-source vector from `L-97302` gives

\[
\mathcal R_X\ge0
\qquad(X\ge1).
\]

The zero-safe Mellin identity (T-97300.1), the nonnegative-transform theorem of
Landau, and functional-equation symmetry then give

\[
\boxed{
\mathrm{CPSL}_{67}
\Longrightarrow
\mathcal R_X\ge0\ (\forall X)
\Longrightarrow
\mathrm{RH}.
}
\tag{T-97300.3}
\]

## Reconstruction verdict

The formerly described candidate-complete theorem does not survive:

1. completed parity is exact but preserves, rather than removes, `(-1)^|h|`;
2. the odd terminal `(history,p,y)=((67),71,13)` has the wrong exact-target
   direction by a certified margin greater than `17`;
3. `rho(Y)=Q_Y(3)/Q_Y(2)` is indeed monotone, but it lifts a **row-2 exact**
   edge, not a `5:3`-scalar-exact edge;
4. scalar exactness has the exact row tradeoff in `R-97300`, so it cannot be
   promoted to two nonnegative rows;
5. every fixed-depth parity reset is excluded by PR #561 / PR #568, including
   the certified depth-two scalar value below `-62.718`.

The precise downgrade is therefore

```text
candidate-complete unconditional successor       WITHDRAWN
completed-parity owner ledger                     PROVED EXACT
terminal row-ratio monotonicity                    PROVED EXACT
leafwise terminal gluing                          REFUTED
scalar-to-two-row lift                            REFUTED
finite scalar Lorenz/Farkas reduction              PROVED EXACT
CPSL67 / GPHT* / ASHP67                           OPEN / RH-BEARING
Riemann Hypothesis                                UNPROVED
```

PR #556's harmonic quadrature and grouped `P_61` annular reserve may still be
used as inputs to a future global producer.  Its parity-blind root promotion is
not imported.
