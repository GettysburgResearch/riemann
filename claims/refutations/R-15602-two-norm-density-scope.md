# R-15602 — L2 density does not imply simultaneous weighted-deficit capture and small form tail

Claim ID: `R-15602`  
Title: Nonresonant periodized E-range density cannot be promoted to the required two-topology approximation without excluding off-line cardinal defects  
Status: `REFUTATION / SCOPE CORRECTION`  
Authoring agent: `gpt56-02-o`  
Created: 2026-07-31  
Dependencies: `L-15613`; the Connes--Consani zeta-cycle density theorem; continuity of the Weil form  
Scope: the proposed final implication in Issue #156

## Refuted inference

The following inference is not valid:

```text
periodized E-range dense in localized L2
=>
the same finite target packet can be approximated
by exact global E-radicals with vanishing exterior Hardy/form tail.
```

The first statement concerns one localized `L2` topology.  The second concerns
the graph topology of the global Weil form and is strictly stronger.

## Exact obstruction

Assume for the purpose of the scope test that an off-line centered zero
`omega` exists.  Let

\[
 v_\omega=k_\omega-k_{\overline\omega}.
 \tag{R-15602.1}
\]

By `L-15613`,

\[
 \boxed{Q_W(v_\omega,v_\omega)=-2m_\omega<0.}
 \tag{R-15602.2}
\]

The cardinal vector has a finite Hardy/form norm and exponentially decaying
tails at every fixed weight below the critical strip boundary.

Suppose a generic density-to-tail theorem supplied exact global `E`-range
radicals `r_n` such that

\[
 r_n\longrightarrow v_\omega
 \tag{R-15602.3}
\]

in the form topology.  Since every `r_n` is a global radical,

\[
 Q_W(r_n,r_n)=0.
 \tag{R-15602.4}
\]

Continuity of the form would give

\[
 Q_W(v_\omega,v_\omega)=0,
 \tag{R-15602.5}
\]

contradicting (R-15602.2).

Equivalently, if `r_n=k_n+t_n`, localized convergence
`k_n->v_omega` together with a vanishing exterior form tail `t_n->0` would imply
(R-15602.3) and the same contradiction.

## Relationship to zeta-cycle density

At nonresonant logarithmic lengths, the periodized Connes--Consani `E`-range is
dense in the circle `L2` space.  The off-line cardinal restriction may
therefore be approximated in that localized topology.  The preceding argument
shows that the norms of the required global lifts must escape in the exterior
form component.

Thus the zeta-cycle density theorem solves finite algebraic `L2` capacity but
does not solve the two-norm packet problem.

## Correct replacement

The valid simultaneous packet may contain:

1. exact `E`-range radicals;
2. critical-line cardinal vectors after positive zero deflation;
3. no unaccounted off-line cardinal direction.

`L-15614` proves that item 2 is harmless.  Item 3 is precisely the unresolved
RH content.

## Consequence

Any theorem proving the requested simultaneous approximation for every
weighted-deficit target packet, without an explicit defect hypothesis, would
already exclude every off-line zero through (R-15602.2).  It is therefore not a
routine strengthening of `L2` density; it is at least as strong as the
Riemann Hypothesis.

This refutation does not assert that an off-line zero exists.  It identifies
the exact obstruction that a complete proof must eliminate.
