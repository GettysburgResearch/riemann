# T-29201 — Positive parity-lifted Mersenne fragmentation proposal for RH

Claim ID: `T-29201`  
Title: A source-complete factor-two parity lift would construct the exact Mersenne-supported carry flow and prove RH  
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
following data.

### 3.1 Lower support flow

A complete `SF-MCF(Y)` flow `d_Y`, including every split and every carry-column
replay.

### 3.2 Ordinary parity-sibling allocation

For every non-Mersenne lower edge `e=[n,j]`, nonnegative numbers

\[
x_e,y_e,
\qquad x_e+y_e\le\alpha d_Y(e),
\tag{T-29201.8}
\]

allocate the three siblings of `L-29202`.  Every even column is then solved
exactly, and the odd columns are solved if and only if the explicit odd-node
network satisfies

\[
B_{\rm odd}(x,y)=z_X.
\tag{T-29201.9}
\]

The complete target charge `z_X` is the odd-multiple Möbius transform
(L-29202.9), not an estimated surrogate.

### 3.3 Mersenne boundary reconstruction

The lifted image of every lower Mersenne extreme edge is recombined with all of
its lower descendants and replaced by a nonnegative flow using only the upper
support menu (T-29201.2)--(T-29201.3).  The replacement must preserve every
carry column exactly.

Its input mass is logarithmic by (T-29201.4), but small mass is not a substitute
for exact reconstruction.

### 3.4 Endpoint and bottom rows

The certificate includes:

```text
column q=2 and the bottom edge [2,1];
the top parent Y whose odd siblings leave the endpoint;
the increment from 2Y to 2Y+1 when required;
every orientation and symmetric duplicate convention.
```

No endpoint row may be hidden in an `O(1)` term.

### 3.5 Final upper flow

After ordinary sibling allocation, Mersenne reconstruction, and endpoint
correction, the emitted flow is a complete `SF-MCF(X)` object.

The theorem `PPMFL` asserts that compatible certificates exist recursively from
one fixed finite base through every dyadic doubling and every intervening unit
endpoint.

## 4. Exact finite acceptance test

The ordinary parity network is accepted only by one of two proof objects:

1. a primal list of all `x_e,y_e` satisfying nonnegativity, shared capacities,
   and exact node divergence; or
2. a proof that every potential satisfies the cut inequality
   \[
   \sum_mz_X(m)\phi(m)
   \le
   \alpha\sum_ed_Y(e)
   \max(0,\Delta_{e,1}\phi,\Delta_{e,2}\phi).
   \]

The Mersenne and endpoint states require their own exact Pascal/tree manifests.
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
\tag{T-29201.10}
\]

Every arrow after `PPMFL` is exact or already isolated in the frozen inputs.

## 6. Why this is not another renamed scalar

The open object is not a bound on Mertens, WSTS, a prime-ramp discrepancy, or a
physical block norm.  It is a finite positive allocation theorem with:

- explicitly listed variables;
- fixed local sibling identities;
- exact capacity constraints;
- an exact odd-divisor node charge;
- a standard max-flow/min-cut alternative;
- a logarithmic, explicitly declared boundary state.

A failed cut produces a concrete finite countercertificate.  A successful
construction produces the complete carry flow consumed by the proof.

The arithmetic difficulty has not disappeared, but it is no longer hidden in
an unnamed cancellation estimate.

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
the unavailable top odd sibling at n=Y.
```

## 8. Exact status

```text
eta source and Mersenne sign localization       inherited proposed exact
Mersenne collar rate                            proved automatically here
parity-sibling/divisor-network algebra          proposed complete exact
ordinary odd-network feasibility                OPEN / SOURCE-SPECIFIC
Mersenne boundary reconstruction                OPEN / SOURCE-SPECIFIC
endpoint-compatible recursive PPMFL             OPEN / LOAD BEARING
PPMFL -> SF-MCF -> RH                            COMPLETE CONDITIONAL CHAIN
Riemann Hypothesis                              UNPROVED
```
