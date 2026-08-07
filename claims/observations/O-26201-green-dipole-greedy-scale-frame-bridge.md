# O-26201 — Green correction, dipole transport, greedy slack, and the endpoint scale frame

Observation ID: `O-26201`  
Title: The four elementary carry fronts share one constraint residual but differ in where positivity is enforced  
Status: **PROPOSED EXACT SYNTHESIS AND RESEARCH HANDOFF**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-08  
Frozen base: PR #248 at `5f2b25f89afbb90a3bc4ca6d40148f530303eb54`  
Scope: cross-route identifications and attack priorities; no RH conclusion

## 1. One residual, four coordinate systems

Let

\[
 r_X(q)=v_q(b_X^{(0)})-w_X(q)
\]

be the parabolic seed residual.  The live repository treats this same object in
four different ways.

### A. Canonical Green equality correction

PR #248 defines the endpoint-projected Gram `G_X`.  The vector

\[
 T_*=G_X^{-1}r_X
\]

is the canonical signed correction:

\[
 v(b_{T_*})=w_X.
\]

Its energy is

\[
 r_X^TG_X^{-1}r_X,
\]

and its logarithmic component is the exact prime-ramp mode.  Constraint
solvability is complete; positivity of the corrected physical row is not.

### B. Constraint-dipole transport

PR #254 retains the positive and negative parts of `r_X` and seeks a signed
adjacent or incidence flow transporting defect into slack at subpower cost.
The new theorem `L-26202` adds that the **continuum** defect is already ordered:
every upper tail contains at least as much slack as defect.  The remaining issue
is finite arithmetic transport, not the existence of a continuum matching.

### C. Row greedy / DCRS

PR #244's row greedy directly enforces

\[
 d\ge0,
 \qquad B_X^Td\le w_X.
\]

Its sharp mass is equivalent to polylogarithmic total column slack.  PR #252's
DCRS debt is the same theorem up to lower-order logarithmic terms.

### D. Endpoint scale frame

`L-26201` decomposes the parabolic seed as

\[
 d_X^{(0)}=\sum_{T=3}^Xa_T,
 \qquad a_T\ge0.
\]

The endpoint-scale greedy changes only the nonnegative coefficients of these
atoms.  It therefore preserves row positivity automatically and leaves one
scale-slack scalar.

These are not four independent arithmetic obstructions.  They are four choices
for where to impose positivity:

```text
Green route:          solve equality first, recover positivity later;
dipole route:         transport signed residual while protecting the row;
row greedy:           impose positivity row by row;
scale frame:          impose positivity atom by atom in endpoint scale.
```

## 2. The overlooked positive object

Before this pass, the parabolic seed was primarily described as a signed
convexified `b` coordinate with sharp objective.  `L-26201` proves more:

\[
 \boxed{d_X^{(0)}\ge0.}
\]

Moreover,

\[
 \boxed{d_T^{(0)}-d_{T-1}^{(0)}\ge0.}
\]

Thus the seed supplies a nested positive family.  This turns the proposed
positivity-preserving deformation into a one-dimensional positive reweighting
problem:

\[
 d=\sum_T\lambda_Ta_T,
 \qquad \lambda_T\ge0.
\]

No signed Green vector needs to be projected back into the row cone.

## 3. Why endpoint scale is quantitatively favorable

For the original row greedy, final slack is charged by

\[
 \beta_{qq}\ell_q\asymp\ell_q.
\]

For the endpoint-scale greedy, final slack is charged by

\[
 \Gamma_{q+1}(q)\ell_{q+1}\asymp q^{-3/2}\ell_{q+1}.
\]

Therefore the local sufficient theorem widens from a summable aggregate of
order-one charges to the pointwise estimate

\[
 \ell_T\ll\sqrt T\,\operatorname{polylog}X.
\]

The latter allows substantial growth in each blocker.  It does not ask for
bounded weights, bounded contacts, or exact saturation.

## 4. Simpler blocker geometry

The original row blocker at `q` freezes a residue complement and leaves only
rows congruent to `-1 mod q`.  The endpoint-scale blocker at `q<T-1` freezes
exactly

\[
 q<U<T.
\]

Hence every production proof object is a list of contiguous intervals.  This is
well matched to the reciprocal-cell continuum theorem:

```text
continuum upper-tail slack
-> one finite frozen scale interval
-> diagonal endpoint loss.
```

A future proof should aggregate maximal frozen intervals rather than estimate
each skipped endpoint independently.

## 5. A direct bridge to Greedy Slack

For the scale-greedy packing, PR #244's universal conservation law gives

\[
 M_X^{\rm sc}
 =8\sqrt X-2\Sigma_X^{\rm sc}+O(\log^2X).
\]

Thus `ESGS` proves the same sharp positive-minorant conclusion as Greedy Slack
or DCRS, without proving either algorithm's individual coefficients comparable.
The common invariant is total column slack, not the identity of the greedy
producer.

This suggests a repository canonicalization:

```text
abstract sharp-packing criterion:
    there exists one explicit feasible d_X>=0 with total slack X^o(1);

producers:
    row greedy,
    endpoint-scale greedy,
    finite Gamma/carry minorant,
    positive phase frame.
```

No producer should be advertised as logically necessary.

## 6. Continuum tail order and finite attack

`L-26202` proves

\[
 \int_\theta^1E(u)du\le0.
\]

This gives a nonnegative continuum flux `C=-H` with `E=C'`.  The correct finite
analogue is not an unsigned estimate for `|E|`; it is a directed inequality on
each maximal frozen endpoint interval.

A promising finite ledger is:

1. group endpoint atoms by the reciprocal quotient cells crossed by their
   blocker interval;
2. compare the complete finite response with the exact cell primitive
   `H_N(theta)`;
3. retain the incoming tail slack before taking a positive part;
4. charge only the two interval boundaries and the small terminal scale;
5. use `Gamma_(q+1)(q) asymp q^(-3/2)` to sum the boundary debt.

This would prove `ESBT` without proving pointwise positivity of the global
Möbius carry inverse.

## 7. What has and has not been achieved

Established in the present branch:

```text
parabolic seed is a genuine positive carry combination;
endpoint increments are positive atoms;
continuum defect has monotone tail transport;
endpoint-scale greedy is finite, positive, and feasible;
scale slack has an exact diagonal identity;
contiguous blocker intervals replace residue forests;
square-root blocker control is sufficient for RH.
```

Still open:

```text
finite reciprocal-cell transport with subpower boundary debt;
ESBT / ESGS;
sharp cofinal nonnegative packing;
RH.
```

The preferred next attack is therefore not another generic Green norm and not a
return to nonnegative defect covering.  It is the source-bound finite transfer
of the exact continuum tail flux into the endpoint-scale blocker intervals.
