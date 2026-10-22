# R-30107 — A five-residue automaton is not yet a closed carry-debt state

Claim ID: `R-30107`
Status: **SCOPE CORRECTION OF T-30107 — FIVE-ADIC SCALING RETAINED, FINITE-STATE CLOSURE WITHDRAWN**
Created: 2026-08-08

## 1. What survives

For the critical target

\[
w_X(q)=q^{-1/2}\log(X/q)
\]

and `X=5Y`, the exact scaling

\[
w_X(5q)=5^{-1/2}w_Y(q)
\]

is valid.  In the multiples-Mobius coordinate this yields the corresponding
five-block identity whenever the source is defined at both endpoints.

This is a useful source decomposition.

## 2. What the previous proposal overclaimed

`T-30107` suggested that, after the five-block decomposition, the remaining
proof object was a finite automaton on residues modulo five.  That conclusion
does not follow from the displayed scaling identities.

There are two independent reasons.

### 2.1 Carry leakage is not residue-local

For a lifted split, carry columns not divisible by five depend on the complete
floor data

\[
\left\lfloor \frac{5n+r}{q}\right\rfloor,
\qquad
\left\lfloor \frac{5j+s}{q}\right\rfloor,
\]

not only on `q mod 5` or the source residue.  Thus two rows with identical
five-residue labels can have different nonmultiple carry images.

A proof must retain enough quotient/floor state to reproduce those columns
exactly.  No five-state transition matrix was emitted on this branch.

### 2.2 The legal adjacent-tree repair is dyadic

The exact commutators used to realize adjacent source dipoles are

\[
E_n=T_{n+1}-T_n,
\]

where the central trees satisfy binary recursions.  Their negative-capacity
ledger therefore carries dyadic ancestry/Mersenne information.  This state is
not determined by a residue modulo five.

Consequently the claimed quotient

```text
five residue classes / critical scaling mode
```

has not been shown invariant under the actual carry/Pascal repair dynamics.

## 3. Correct disposition

The following are retained:

- exact five-adic scaling of the critical target;
- any independently proved five-block source identity;
- the possibility of using factor-five descent inside a larger source state.

The following are withdrawn:

- the assertion that the remaining state is five dimensional;
- the assertion that a `5 x 5` matrix by itself closes Cycle Debt;
- the narrative that `rho(K_5)<1` is the sole remaining theorem.

A valid factor-five continuation must emit the **complete invariant state**,
including all nonmultiple carry columns and any dyadic tree/cycle coordinates,
before a spectral-radius statement has mathematical meaning.

## 4. Repository proof boundary

```text
five-adic critical scaling               RETAINED
finite five-state closure                 UNPROVEN / WITHDRAWN
five-adic source renewal as an ingredient RETAINED
RH                                        UNPROVEN
```

No RH conclusion follows from `T-30107` as currently written.
