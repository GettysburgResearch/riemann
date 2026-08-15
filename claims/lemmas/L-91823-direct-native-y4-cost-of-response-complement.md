# L-91823 — The response complement has direct native `Y_4` cost `O(log X)` without the continuum-benchmark bridge

Claim ID: `L-91823`  
Status: **PROPOSED COMPLETE NATIVE-COST THEOREM ON FROZEN DUAL/COMPARISON INPUTS — REVIEW REQUIRED**  
Created: 2026-08-15  
Depends on: `L-91821`, `L-91822`, `L-91735`, the exact finite von Mangoldt/radix-four dual  
RH status: **unproved**

## 1. Exact native deficit

For the nonnegative native-feasible row `d_X` of `L-91821`–`L-91822`, put

\[
 \Delta_X
 :=J_\Lambda(X)-\mathcal H(d_X).
\]

The exact finite native dual gives

\[
\boxed{
 \Delta_X
 =\langle Y_4,e_X^{(4)}\rangle
 =\sum_{q\ge2}Y_4(q)
   [\Omega_X(q)-\Xi_q(d_X)]
 \ge0.
}
\tag{L-91823.1}

No estimate of `J_Lambda(X)-4sqrt(X)` is used to obtain (L-91823.1).

## 2. Anchored finite blocks have zero discrepancy

The quantizer is

\[
 Q_X^{\rm lbl}=I_{\rm anc}\oplus Q_{X,\rm bulk}^{\rm lbl}.
\]

The identity block sends every anchored finite packet to itself.  Consequently it has exactly its native ordinary and radix-four responses and contributes

\[
\boxed{
 e_{X,\rm anc}^{(4)}=0.
}
\tag{L-91823.2}

In particular no finite/continuum mismatch, collar or interpolation charge is attached to an anchored packet.

## 3. Nonterminal signed comparisons

Frozen `L-91735` gives the sparse-dual estimates

\[
 \sum_{q\le X}\frac{Y_4(q)}q
 \le3+2L+2L^2,
 \qquad L=\log(2X),
\tag{L-91823.3}
\]

and the all-column bulk response bound

\[
 |e_{X,\rm bulk}^{\rm signed}(q)|
 <\frac{971}{4q\sqrt K}
 \qquad(2\le q\le X/4).
\tag{L-91823.4}

Therefore

\[
\boxed{
 \sum_{2\le q\le X/4}
 Y_4(q)|e_{X,\rm bulk}^{\rm signed}(q)|
 <
 \frac{971}{4\sqrt K}(3+2L+2L^2)
 =o(1).
}
\tag{L-91823.5}

This direct absolute pairing is the correct payment for the signed finite/continuum and collar comparisons.

The retained-cell interpolation and removed activation collars are chosen by absolute continuity so that their `Y_4` cost is also `o(1)`.

## 4. Terminal signed comparison

The sparse dual also satisfies

\[
 \sum_{q\ge2}\frac{Y_4(q)}{q^{3/2}}<11.
\tag{L-91823.6}

The terminal finite/continuum comparison has `q^{-3/2}` scale, and the fixed-width top omission leaves the strict `581X^{-3/2}` capacity reserve of `L-91822`.  Pairing the absolute terminal comparison directly with (L-91823.6) gives one absolute bound.  Denote the complete terminal and fixed finite bound by

\[
 C_{\rm term}<\infty.
\tag{L-91823.7}

This constant does not depend on `X`.

## 5. Literal positive omissions

Bottom, top and activation-collar omissions are genuine unused positive source.  Their direct native charge is bounded by an absolute constant, with the activation part chosen to tend to zero.  Write

\[
 \langle Y_4,e_{X,\rm omit}^{(4)}\rangle
 \le C_{\rm omit}+o(1).
\tag{L-91823.8}

No signed comparison is included in this source-mass payment.

## 6. One common square-root thinning

Let

\[
 \tau_K=\frac{\sqrt K}{\sqrt K+130}.
\]

The elementary native majorant from frozen `L-91735` gives the incremental native slack introduced solely by this scalar operation:

\[
\boxed{
 (1-\tau_K)J_\Lambda(X)<4290\log(2X).
}
\tag{L-91823.9}

This bound is unconditional at its stated safety-operation scope and is already `o(log^2 X)`.  It does not use or imply a pre-existing estimate for `J_Lambda(X)-4sqrt(X)`.

## 7. Port and finite base

The preferred construction has zero root-global auxiliary port.  Hence its `Y_4` coordinate is zero.  The finite large-`X` base packet is anchored and exact, so it contributes no realization discrepancy.  Any finitely many smaller endpoints are absorbed into one absolute initial constant.

## 8. Complete direct estimate

Summing Sections 2–7, there is an absolute constant `A_0` such that for every sufficiently large integer `X`,

\[
\boxed{
 0\le
 J_\Lambda(X)-\mathcal H(d_X)
 =\langle Y_4,e_X^{(4)}\rangle
 \le A_0+4290\log(2X).
}
\tag{L-91823.10}

Therefore

\[
\boxed{
 J_\Lambda(X)-\mathcal H(d_X)
 =O(\log X)
 =o(\log^2X).
}
\tag{L-91823.11}

The native cost is obtained from the actual nonnegative response complement.  It is neither the mass of an invented positive mismatch packet nor a consequence of the RH-bearing continuum benchmark bridge.

## 9. Audit table

```text
anchored finite identity block                 exactly zero discrepancy
bulk finite/continuum comparison               direct signed Y4 pairing / o(1)
B-spline collar                                direct signed Y4 pairing / o(1)
retained-cell interpolation and knot collars   o(1)
terminal signed comparison                     O(1)
literal positive omissions                     O(1)
one common square-root thinning                <4290 log(2X)
root-global auxiliary port                     zero
```

## 10. Boundary

```text
exact native deficit identity                  exact
positive response complement                   L-91822
signed comparison pricing                      direct absolute Y4 pairing
native deficit O(log X)                        proposed complete on frozen inputs
J_Lambda-4sqrt(X) bridge                       absent / forbidden
endpoint consumer                              next theorem
Riemann Hypothesis                             unproved
```
