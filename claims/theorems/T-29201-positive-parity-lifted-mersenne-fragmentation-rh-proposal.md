# T-29201 — Positive parity-cycle Mersenne fragmentation proposal for RH

Claim ID: `T-29201`  
Title: A source-complete factor-two parity lift with zero-even Pascal completion would construct the exact Mersenne-supported carry flow and prove RH  
Status: **SERIOUS FULL CONDITIONAL PROPOSAL — `PPMFL` IS OPEN**  
Authoring agent: `gpt56-sol`  
Created: 2026-08-08  
Dependencies: `L-29201`, `L-29202`; PR #285 `L-28001/L-28002`; PR #272 Pascal-cycle normal form; standard one-sided Mellin--Landau theorem  
RH status: **unproved**

## 1. Refreshed strategic boundary

The post-review graph has removed several apparent shortcuts:

```text
monotone Divisibility Cover          false at square-root cost;
prime-only tail transport            false by deterministic density drift;
fixed third/fourth/fifth Abel signs  false at finite endpoints;
smooth all-stage central positivity  false because of boundary knots;
WSTS                                 now explicitly equivalent to RH.
```

At the same time, the surviving exact work has concentrated the source:

```text
central eta resolvent       -> one odd-Mobius source;
eta carry image             -> positive binary window;
negative carry geometry     -> Mersenne rows only;
Pascal cycles               -> complete finite repair coordinates;
factor-two source split     -> even lift plus odd adjacent commutator.
```

This proposal attacks the last item constructively rather than estimating an
RH-equivalent scalar.

## 2. Support-feasible MCF

Let `L(n)` be the largest power of two not exceeding `n`.  Define `SF-MCF(X)`
by the existence of a nonnegative flow `d_X(n,j)` satisfying

\[
\sum_{n=q}^{X}\sum_{j=1}^{n-1}
 d_X(n,j)\chi_{n,q}(j)
=q^{-1/2}\log(X/q)
\qquad(2\le q\le X),
\tag{T-29201.1}
\]

with support

\[
n-L(n)<j<L(n)
\quad(n\ne2^r-1),
\tag{T-29201.2}
\]

and

\[
j\in\{1,n-1\}
\quad(n=2^r-1).
\tag{T-29201.3}
\]

`L-29201` proves that no separate asymptotic collar theorem is needed:

\[
\sum_{2^r-1\le X}P_{d_X}(2^r-1)
\le(1+\sqrt2)\log X.
\tag{T-29201.4}
\]

The exact eta-source pairing on PR #285 therefore gives

\[
\mathcal R_\eta(X)
\ge-(1+\sqrt2)\log X.
\tag{T-29201.5}
\]

Its Mellin transform is

\[
\frac{\eta(z+1/2)^{-1}-1}{z^2}.
\tag{T-29201.6}
\]

The one-sided Landau argument of `T-28001` yields

\[
\boxed{
SF\text{-}MCF(X)\text{ for all sufficiently large }X
\Longrightarrow RH.
}
\tag{T-29201.7}
\]

Thus the only issue is exact finite support feasibility.

## 3. Positive Parity Mersenne Flow Lift (`PPMFL`)

Put `X=2Y` and `alpha=2^(-1/2)`.  A `PPMFL(Y)` certificate consists of the
following source-complete data.

### 3.1 Lower support flow

A complete `SF-MCF(Y)` flow `d_Y`, including every split and every carry-column
replay.

### 3.2 Ordinary parity-sibling baseline

For every non-Mersenne lower edge `e=[n,j]`, nonnegative numbers

\[
x_e,y_e,
\qquad x_e+y_e\le\alpha d_Y(e),
\tag{T-29201.8}
\]

allocate the three siblings of `L-29202`.  Every even column is then solved
exactly.  The sibling differences contribute the explicit odd-node incidence

\[
B_{\rm odd}(x,y).
\tag{T-29201.9}
\]

The complete target charge `z_X` is the odd-multiple Möbius transform in
`L-29202.9`, not an estimated surrogate.

The edge-local network equation

\[
B_{\rm odd}(x,y)=z_X
\tag{T-29201.10}
\]

is a particularly strong sufficient certificate, but it is **not assumed to be
necessary**.  A valid proof may need carry-preserving circulation among several
upper parents before nonnegativity becomes visible.

### 3.3 Complete zero-even-column Pascal completion

Let `E_X^{\rm MCF}` be the upper support menu and let

\[
K_X^{\rm even}
=\left\{c\in\mathbb R^{E_X^{\rm MCF}}:
 \sum_{e\in E_X^{\rm MCF}}c_e\chi_e(2q)=0
 \text{ for every }q\right\}.
\tag{T-29201.11}
\]

The certificate may add a signed correction

\[
c_X\in K_X^{\rm even}
\tag{T-29201.12}
\]

provided the **final** split coefficients are nonnegative.  It must emit a
complete parity-compatible Pascal/fundamental-cycle decomposition of `c_X`.
No unnamed nullspace vector is permitted.

The complete ordinary odd-column equation is therefore

\[
\boxed{
B_{\rm odd}(x,y)+L_{\rm odd}(c_X)=z_X.
}
\tag{T-29201.13}
\]

This is the correct factor-two construction target.  The local sibling network
is its sparse first layer; the zero-even cycle space supplies every legal
carry-preserving redistribution that the local lift misses.

### 3.4 Mersenne boundary reconstruction

The lifted image of every lower Mersenne extreme edge is recombined with all of
its descendants and with the zero-even cycle correction, then replaced by a
nonnegative flow using only the upper support menu (T-29201.2)--(T-29201.3).
The replacement must preserve every carry column exactly.

Its input mass is logarithmic by (T-29201.4), but small mass is not a substitute
for exact reconstruction.

### 3.5 Endpoint and bottom rows

The certificate includes:

```text
column q=2 and the bottom edge [2,1];
the top parent Y whose odd siblings leave the endpoint;
the increment from 2Y to 2Y+1 when required;
every orientation and symmetric duplicate convention.
```

No endpoint row may be hidden in an `O(1)` term.

### 3.6 Final upper flow

After sibling allocation, zero-even Pascal completion, Mersenne reconstruction,
and endpoint correction, the emitted flow is a complete `SF-MCF(X)` object.

The theorem `PPMFL` asserts that compatible certificates exist recursively from
one fixed finite base through every dyadic doubling and every intervening unit
endpoint.

## 4. Exact finite acceptance tests

The ordinary parity stage is accepted by either:

1. a primal list of `x_e,y_e` and parity-cycle coefficients satisfying shared
   capacities, exact even-zero conditions, exact odd charge, and final
   nonnegativity; or
2. an exact dual proof for the combined sibling-plus-zero-even-cycle polytope.

For the sibling-only subproblem the dual reduces to

\[
\sum_mz_X(m)\phi(m)
\le
\alpha\sum_ed_Y(e)
\max(0,\Delta_{e,1}\phi,\Delta_{e,2}\phi).
\tag{T-29201.14}
\]

A complete PPMFL proof must additionally certify that every dual direction
annihilating the sibling arcs is paid by an emitted parity-compatible Pascal
cycle or belongs to the declared Mersenne/endpoint state.

Floating feasibility, a generic operator norm, and a finite positive ladder are
not production proofs.

## 5. Conditional completion

Assume `PPMFL`.  Starting from its finite base, induction constructs
`SF-MCF(X)` for every sufficiently large endpoint.  Equation (T-29201.4) gives
the collar bound without a separate estimate.  The eta pairing gives
(T-29201.5), and the Mellin--Landau consumer gives RH.

Hence

\[
\boxed{
PPMFL\Longrightarrow SF\text{-}MCF
\Longrightarrow \mathcal R_\eta(X)\ge-O(\log X)
\Longrightarrow RH.
}
\tag{T-29201.15}
\]

Every arrow after `PPMFL` is exact or already isolated in the frozen inputs.

## 6. Why this is not another renamed scalar

The open object is not a bound on Mertens, WSTS, a prime-ramp discrepancy, or a
physical block norm.  It is a finite positive construction theorem with:

- explicitly listed sibling variables;
- fixed floor identities;
- exact shared capacities;
- an exact odd-divisor node charge;
- a complete zero-even Pascal-cycle coordinate;
- a finite primal/dual alternative;
- a logarithmic, explicitly declared boundary state.

A failed dual produces a concrete finite countercertificate.  A successful
construction produces the complete carry flow consumed by the proof.

## 7. Mandatory mutations

A claimed proof must survive:

```text
PR #254 square-root monotone-cover obstruction;
PR #274 prime-density drift;
R-28101 fixed Abel counterexamples;
R-28102 compact-boundary monotonicity failure;
PR #239 same-sign high-rank Mobius cube;
PR #229 exact 2/3 first-cell Mertens decoder;
all lower Mersenne extreme edges;
the unavailable top odd sibling at n=Y;
a synthetic target where the sibling-only network is insufficient.
```

## 8. Exact status

```text
eta source and Mersenne sign localization       inherited proposed exact
Mersenne collar rate                            proved automatically here
parity-sibling/divisor-network algebra          proposed complete exact
complete zero-even Pascal coordinate            inherited finite basis / source binding open
combined parity-cycle feasibility               OPEN / SOURCE-SPECIFIC
Mersenne boundary reconstruction                OPEN / SOURCE-SPECIFIC
endpoint-compatible recursive PPMFL             OPEN / LOAD BEARING
PPMFL -> SF-MCF -> RH                            COMPLETE CONDITIONAL CHAIN
Riemann Hypothesis                              UNPROVED
```
