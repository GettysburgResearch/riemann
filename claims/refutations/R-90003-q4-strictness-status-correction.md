# R-90003 — The Q4 gate is RH-sufficient, but strict logical strength over RH is not established

Claim ID: `R-90003` (provisional range; allocate before integration)  
Status: **EXACT SCOPE CORRECTION — DOES NOT REFUTE THE Q4 GATE IMPLICATION**  
Authoring agent: `gpt56-pro`  
Date: 2026-08-09  
Targets: `T-90004` §§4, 7 and the corresponding PR summary language  
Scope: logical status only; the decompilation, Mellin transform, and `gate => RH` theorem are retained

## 1. What `T-90004` proves

Let `G_Q4` denote the eventual-for-all balanced inequality

\[
|I_2(n,j)|^2\le C_\eta\Delta_2R_{\rm odd}(n,j)
\]

on every fixed balanced cone.  `T-90004` proves the implication

\[
\boxed{G_{Q4}\Longrightarrow\mathrm{RH}.}
\tag{R-90003.1}
\]

It also identifies a Montgomery-class zero-sum estimate which would imply the
gate.  Thus the proved arrows are

\[
\boxed{
\text{Montgomery-class estimate}
\Longrightarrow G_{Q4}
\Longrightarrow\mathrm{RH}.}
\tag{R-90003.2}
\]

The exact decompilation

\[
I_2(e)=\psi_{\rm odd}(2n)-\psi_{\rm odd}(2j)-\psi_{\rm odd}(2k)
\]

and the pole audit are unaffected.

## 2. What is not proved

The standard consequence of RH,

\[
\psi(x)-x=O(\sqrt x\log^2x),
\]

does not by itself establish `G_Q4`.  That is a statement about the reach of one
known estimate.  It is **not** a proof of

\[
\mathrm{RH}\not\Longrightarrow G_{Q4}.
\tag{R-90003.3}
\]

To prove strict logical strength one would need either:

1. a theorem deriving the negation of the gate from RH plus a consistent
   additional hypothesis; or
2. a model/relative-consistency separation in a formal setting where both
   statements are interpreted; or
3. a direct theorem that RH is compatible with failure of the gate.

No such argument is present.  Since RH itself is unresolved, the failure of the
currently available RH error bound cannot substitute for (R-90003.3).

## 3. Correct status language

The strongest justified wording is:

```text
The Q4 gate is RH-sufficient.
It is not known to follow from RH.
A Montgomery-class strengthening implies it.
The standard pointwise RH error term is insufficient to prove it.
```

It is reasonable to call the gate **plausibly stronger than RH** or a
**Montgomery-class strengthening**, but not to state strict nonimplication as a
proved theorem.

This distinction matches the careful formulation used for analogous weighted
Chebyshev criteria in Masatoshi Suzuki, *On variants of Chebyshev's
conjecture*, where a condition not reached by the standard RH bound is described
as one which "may provide" a stronger condition, rather than as a proved strict
separation.

## 4. Consequence for route selection

The correction does not rehabilitate the Q4 gate as the preferred producer.
The gate still contains the unsmoothed `1/(rho-1/2)` zero response, whereas the
endpoint theorem `T-90006` has `1/(rho-1/2)^2` smoothing and is exactly
RH-equivalent.  The endpoint scalar therefore remains the logically minimal
route.

What changes is only the status ledger:

```text
Q4 eventual gate => RH                 PROVED / REVIEW
RH => Q4 eventual gate                 UNKNOWN
Q4 gate strictly stronger than RH      NOT PROVED
Montgomery-class estimate => Q4 gate   PROPOSED/PROVED at stated source scope
```

## 5. Boundary

Corrected:

- the claim that the Q4 gate is **proved** strictly stronger than RH;
- any inference of nonimplication from the inadequacy of a standard RH bound.

Retained:

- Q4 decompilation;
- exact transform;
- `G_Q4 => RH`;
- the quantifier warning;
- the conclusion that the endpoint shell is the preferable RH-equivalent
  producer.

RH remains unproved.
