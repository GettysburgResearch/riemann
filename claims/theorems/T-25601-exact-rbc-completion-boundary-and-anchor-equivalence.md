# T-25601 — Exact RBC completion boundary and anchor equivalence

Claim ID: `T-25601`  
Title: The reflected finite-resolvent programme closes every source-map and finite-depth obligation but leaves one full-scale fixed-ratio Möbius anchor whose subexponential energy is the RH-bearing theorem  
Status: **PROPOSED COMPLETE CLASSIFICATION THEOREM PENDING INDEPENDENT REVIEW**  
Authoring agent: `gpt56-pro-22`  
Created: 2026-08-07  
Issue: #256  
Dependencies: PR #241 `L-9518`; PR #250 `L-24901`; `R-25601`, `L-25601`--`L-25604`; `L-23401/T-23401`; `L-23008`  
Scope: complete logical disposition of the RBC completion attempt

## 1. Inputs retained

Fix a compact zero-safe window and one finite-resolvent order `K`.  The
following proposed inputs are retained at their exact scopes.

1. `L-9518` gives the exact two-frequency physical block normal Gram.
2. `L-24901` closes every reflected residual-depth row except the top-top row by
   superorder complete-lattice Euler summation.
3. `L-25601` packages the complete finite depth system in one matrix inverse and
   exports every reflected cross term exactly.
4. `L-25604` gives a positive root-of-unity depth frame.
5. `L-25602/L-25603` identify and localize the unique reciprocal-zeta charge.

No balanced estimate is imported from `L-23203`.

## 2. Exact finite-depth reduction

After the non-top Euler purge, the complete reflected source splits into

\[
\boxed{
\mathcal S_{K,J}
=
\mathcal S_{K,J}^{\rm rf}
+
\mathcal A_{c,J},}
\tag{T-25601.1}
\]

where:

- `S^(rf)` is reciprocal-free at every nontrivial zeta zero and consists of the
  finite depth/color differences, declared complete-lattice rows, source-bound
  endpoints, and strict lower-scale destinations;
- `A_(c,J)` is one representative of the one-dimensional meromorphic quotient,
  which may be taken to be the fixed-ratio Möbius shell
  \[
  Q_c(t)=e^{-t/2}[M(e^t)-M(ce^t)].
  \]

The word “one” in (T-25601.1) means analytic quotient rank one.  The anchor
occupies a full multiplicative shell of scale `e^J`.

## 3. Source-map and charge-injection obligations

The matrix depth lift proves the complete packet/global source map and every
cross term.  The quotient map of `L-25603` injects all nontrivial meromorphic
charge into one scalar anchor.  Thus the following parts of the proposed RBC
certificate can be completed exactly:

```text
complete depth manifest;
independent two-frequency source map;
all depth cross terms;
bounded local depth incidence;
reciprocal-free versus charged quotient split;
rank-one scalar charge projection;
all-ratio shell transfer.
```

This is the strongest correct form of a bounded charge theorem.

It does **not** prove the `C_ref/K` exponent asserted in PR #250, because the
charged anchor has scale `X`, not `V=X^(1/K)`.

## 4. Strict reserve obstruction

The aggregate reflected identity is the squared norm of the synthesized packet
sum.  `R-25601` proves that its synthesis Gram has a nontrivial kernel and that
its natural Schur complement is exactly zero.  Therefore

\[
\boxed{
\text{reflection + exact source map + bounded incidence}
\not\Rightarrow
\text{strict Schur reserve}.}
\tag{T-25601.2}
\]

The cyclic phase lift supplies a positive frame but does not estimate the
anchor-color forcing.  Far-right residual contraction is exponent-critical by
`R-25602`.  Meromorphic reparametrization merely moves the same charge between
the base and residual by `L-25602`.

Hence no remaining algebraic choice in the finite resolvent produces a strict
reserve for free.

## 5. Anchor Shell theorem

For fixed `0<c<1` and fixed `B>0`, put

\[
\boxed{
E_{c,B}(J)=\int_J^{J+B}|Q_c(t)|^2dt.}
\tag{T-25601.3}
\]

Call the following statement `ASH(c,B)`:

\[
\boxed{
E_{c,B}(J)=e^{o(J)}.}
\tag{T-25601.4}
\]

The exact transform of `Q_c` is

\[
\widehat Q_c(z)
={1-c^{z+1/2}\over
(z+1/2)\zeta(z+1/2)},
\tag{T-25601.5}
\]

and its numerator has no zero at a hypothetical zeta zero to the right of the
critical line.  The fixed-ratio shell theorem of PR #234 gives

\[
\boxed{
ASH(c,B)\Longleftrightarrow RH.}
\tag{T-25601.6}
\]

The direction needed by a proof proposal is `ASH => RH`; the reverse direction
is the standard zero-free-half-plane estimate.  `L-23008` makes the choice of
fixed ratio immaterial.

## 6. RBC implies the anchor theorem

Suppose a purported `RBC(K)` family has:

1. the exact fixed-ratio scalar projection required by `D-24901`;
2. a strict reserve with no hidden same-scale copy of the target;
3. strict lower-scale routes and coefficient loss tending to zero in the
   recurrence.

Project the source-bound inequality onto the scalar anchor coordinate.  The
same recurrence and loss apply to `E_(c,B)(J)`.  Iteration gives

\[
E_{c,B}(J)=e^{o(J)}.
\]

Therefore

\[
\boxed{
\text{a valid unbounded RBC family}
\Longrightarrow ASH(c,B)
\Longrightarrow RH.}
\tag{T-25601.7}
\]

This proves that the production reserve cannot be a routine consequence of
packet geometry: it contains an RH-equivalent scalar theorem.

## 7. Corrected completion choices

A genuine completion must now prove one of the following equivalent-strength
source-specific statements.

### A. Reflected anchor reserve

A two-frequency, source-bound inequality

\[
E_{c,B}(J)
\le
\exp(o(J))
\left[1+\max_{u\le(1-\delta)J+C}E_{c,B}(u)\right].
\tag{T-25601.8}
\]

### B. Direct shell energy

Equation (T-25601.4).

### C. Carry/transport projection

A sharp nonnegative carry minorant, signed constraint-dipole transport, or
Gamma-carry factor whose finite entropy ledger gives the prime-ramp bound with
`4 sqrt(X)-X^o(1)`.

These are different proof languages for the same surviving scalar charge.  No
one is established by the finite-resolvent algebra alone.

## 8. Disposition of PR #250

The completion attack changes the status of the two open RBC obligations as
follows.

```text
actual source map and reflected cross terms       CLOSED PROPOSED EXACT
bounded depth incidence                           CLOSED PROPOSED EXACT
analytic charge injection                         CLOSED, RANK ONE
charge exponent C_ref/K                           REJECTED FOR THE ANCHOR
aggregate reflected Schur reserve                 EXACTLY ZERO
independent source-specific anchor reserve         OPEN / RH-BEARING
RBC as a route to RH                               VALID CONDITIONALLY
RH                                                 UNPROVED
```

The PR #250 certificate schema remains useful after replacing “bounded paid
`V`-coordinates” by “reciprocal-free ledger plus one full-scale anchor.”

## 9. Proof boundary

This theorem does not claim RH.  It proves the exact boundary reached by the
attempt to prove the remaining RBC elements and prevents the unresolved anchor
from being hidden under another finite charge or face-count slogan.
