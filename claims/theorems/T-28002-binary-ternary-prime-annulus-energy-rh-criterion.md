# T-28002 — Binary–ternary prime-annulus energy criterion

Claim ID: `T-28002`  
Title: RH is equivalent to subexponential local energy of one explicit top-six prime-annulus commutator, whose discrete source is a finite factor-eighteen carry transition  
Status: **FULL CONDITIONAL PROPOSAL — PRIME-ANNULUS ENERGY UNPROVEN**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-08  
Dependencies: `L-28006`; PR #241 independent-frequency block; the standard Laplace pole-exclusion theorem

## 1. Explicit finite statistic

For `X>6`, define

\[
\boxed{
\begin{aligned}
P_{2,3}(X)=\frac1{\sqrt X}\Bigg[&
\sum_{X/2<q\le X}
\Lambda_{2,3}^{\rm ann}(q)
\left(\frac{2q}{X}-1\right)\\
&-\sum_{X/3<q\le X/2}
\Lambda_{2,3}^{\rm ann}(q)\frac{2q}{X}\\
&+\sum_{X/6<q\le X/3}
\Lambda_{2,3}^{\rm ann}(q)
\left(\frac13-\frac{4q}{X}\right)
\Bigg].
\end{aligned}}
\tag{T-28002.1}
\]

Every sum is finite and supported on the top-six annulus.  Proper prime powers
may be retained or removed with an explicit `O(log X/sqrt X)` correction.

By `L-28006`,

\[
P_{2,3}(e^t)
=\mathcal C_{2,3}^{\rm ann}(t)
\qquad(t>\log6).
\tag{T-28002.2}
\]

## 2. Pole tomography

The Laplace transform is

\[
\boxed{
\widehat P_{2,3}(z)
=-E_{2,3}(s)R(s)\frac{\zeta'}{\zeta}(s)
-E_{2,3}(s)R'(s),
\qquad s=z+\frac12.}
\tag{T-28002.3}
\]

Every nontrivial zeta zero `rho` of multiplicity `m_rho` gives the nonzero
residue

\[
-m_\rho E_{2,3}(\rho)R(\rho).
\]

No safe multiplier zero hides an off-line zero.

Consequently the following are equivalent:

1. RH.
2. For every `epsilon>0`,
   \[
   P_{2,3}(X)=O_\epsilon(X^\epsilon).
   \tag{T-28002.4}
   \]
3. The unit-block energy
   \[
   \boxed{
   \mathcal E_{2,3}(J)
   =\int_J^{J+1}|P_{2,3}(e^t)|^2dt}
   \tag{T-28002.5}
   \]
   satisfies
   \[
   \mathcal E_{2,3}(J)=e^{o(J)}.
   \tag{T-28002.6}
   \]

The forward direction uses the classical RH bound for `zeta'/zeta` away from
its critical-line poles after the compact source multiplier is retained.  The
reverse direction is the local Hardy/Laplace pole argument: one pole with
positive real part forces a positive exponential block-energy exponent.

## 3. Exact physical-to-carry scalar map

For integer `X`, `L-28006` gives

\[
\boxed{
P_{2,3}(X)
=\mathcal R_X^{\rm disc}
+\frac{2}{X(X+1)}
\left[
B(X)-2B(X/2)-B(X/3)+2B(X/6)-\log3
\right],}
\tag{T-28002.7}
\]

where the discrete scalar is

\[
\boxed{
\mathcal R_X^{\rm disc}
=\frac1{X+1}
\sum_{j=0}^{X}
\sum_{m\le X}
\Lambda_{2,3}^{\rm ann}(m)
Z^{\rm ann}_{X,m}(j).}
\tag{T-28002.8}
\]

The bracket in (T-28002.7) is bounded and tends to `4/9` after its prefactor.
Thus no unknown continuum/discrete error remains.  The physical pole-sensitive
statistic and the factor-eighteen carry scalar have the same subpower and local
energy criteria.

## 4. Proposed completion — BT-PAE

The single open theorem is:

> **Binary–Ternary Prime-Annulus Energy (`BT-PAE`).**  The complete
> independent-frequency source ledger for (T-28002.8) proves
> \[
> \boxed{
> \mathcal E_{2,3}(J)=e^{o(J)}.}
> \tag{T-28002.9}
> \]

A production certificate must contain:

1. every source row `m<=X<18m-2` and every rounding boundary;
2. the positive inverse and generalized-prime synthesis;
3. the exact first and second commutators;
4. PR #241's two independent frequencies and every cross term;
5. a strict source-image Schur reserve;
6. the bounded continuum/discrete boundary;
7. every lower-scale or previous-block destination;
8. the dyadic bottom-charge and `2/3` Mertens mutations.

The intended recurrence is

\[
\kappa_0\mathcal E_{2,3}(J)
\le C(1+J)^A
+\sum_{r=1}^{R}\theta_r
\mathcal E_{2,3}(J-r\delta),
\qquad
\sum_r\theta_r<\kappa_0.
\tag{T-28002.10}
\]

This is a fixed finite-transition theorem.  No packet-order limit, generic BTP,
or bounded-rank assertion occurs.

## 5. Relationship to the compact critical source

`L-28004/L-28005` provide a complementary physical front end:

```text
compact reciprocal-zeta Riesz window
+ four-channel closed-strip frame
+ coefficientwise positive summed forcing
+ finite Bézout reconstruction.
```

The commutator statistic (T-28002.1) is the scalar boundary coordinate of that
physical programme.  A valid four-channel block recurrence must imply BT-PAE;
conversely BT-PAE supplies an exact scalar mutation for the four-channel proof
object.

## 6. Conditional completion

By the equivalence in section 2,

\[
\boxed{
\mathrm{BT\!\!-\!PAE}
\Longrightarrow
\mathrm{RH}.}
\tag{T-28002.11}
\]

No further arithmetic theorem is required after the local energy estimate.

## 7. Automatic rejection conditions

Reject a claimed proof if it:

1. estimates the continuum statistic without the exact boundary (T-28002.7);
2. drops either the binary or ternary Euler sibling;
3. uses one frequency instead of PR #241's physical block;
4. replaces the complete generalized-prime synthesis by a scalar Kummer row;
5. discards a transition cross term before the source sum;
6. imports carry-space reserve as physical reserve without a map;
7. invokes a fixed Abel-order positivity theorem;
8. loses the dyadic bottom or first-cell Mertens mutation;
9. promotes finite computation to (T-28002.9).

## 8. Exact status

```text
pole-preserving source and annulus formula       proposed complete
continuum/discrete scalar map                    proposed complete
factor-eighteen carry representation             proposed complete
prime-annulus criterion <=> RH                   proposed complete
BT-PAE local energy                              UNPROVEN / RH-BEARING
Riemann Hypothesis                               UNPROVEN
```
