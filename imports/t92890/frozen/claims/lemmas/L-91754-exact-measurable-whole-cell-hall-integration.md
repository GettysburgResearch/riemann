# L-91754 — Exact measurable Hall integration needs no activation collar or mesh

Claim ID: `L-91754`  
Status: **PROPOSED COMPLETE EXACT-INTEGRATION THEOREM ON FROZEN INPUTS — REVIEW REQUIRED**  
Created: 2026-08-15  
Depends on: `L-91690`, `L-91674`, `L-91110`, `L-91688`, `L-91733`  
Supersedes in the controlling chain: activation-collar approximation and
barycentric Hall refinement  
RH status: **unproved at this claim**

## 1. Whole-cell support

For integer `X`, put

\[
K=\left\lfloor\frac X{67}\right\rfloor+1,
\qquad W=10000,
\]

and retain the endpoint interval

\[
I_X=[K+2,X-W-2].
\]

Both endpoints are integers. Thus every continuumized adjacent endpoint cell
is complete. There is no partial cell at the lower cutoff, at an activation
knot, or at the top omission.

For `s in I_X`, `x=X/s` satisfies `1<x<67`; the factor-67 Hall theorem applies.
The equality endpoint density is

\[
d\mu_X(s)=\frac{2L(X/s)}s\,ds,
\qquad L(X/s)>0.
\]

## 2. Measurable exact Hall kernel

On each finite activation cell, the deterministic left-greedy Hall coefficients
are obtained by finitely many additions, positive divisions, and `min`.
Therefore the Hall map is Borel measurable. Its one-sided values at the finite
knots define a measurable map and affect no integral.

For each fiber, the exact target/score/all-row identity is

\[
P_s=B_s+Z_s,
\qquad B_s,Z_s\ge0.
\]

Attach first-owner rough labels to `Z_s`, apply the exact causal split, but keep
all child terms as labelled internal colours. Fiberwise the current and child
terms sum back to `Z_s` exactly.

Tonelli therefore gives one exact positive parent measure

\[
\Lambda_X^{\rm tot}
 =\int_{I_X}(B_s+Z_s)\,d\mu_X(s),
\]

with every source occurrence owned once.

## 3. One exact positive quantizer

The martingale B-spline quantizer is defined by exact integrals. Apply it once to
`Lambda_X^tot`, retaining labels internally. Its endpoint weights are
nonnegative, and the pointwise barycentric weights sum to one. Hence the total
finite row

\[
d_X^0=\mathcal Q_X\Lambda_X^{\rm tot}
\]

is coefficientwise nonnegative and equals the sum of all labelled Hall bonuses,
causal currents, and causal child colours.

No Hall interpolation, activation collar, child quantizer, or per-colour
finite correction is used.

## 4. Exact retained mismatch seed

Let

\[
\mathcal I_X=\{n\in\mathbb Z:K+2\le n\le X-W-3\}.
\]

Define

\[
E_X^I(n)=
\sum_{\substack{m\in\mathcal I_X\\m\ge n}}
\left[d_X^\star(m)-\int_m^{m+1}d_X^\star(t)dt\right].
\]

Then exactly

\[
E_X^I(n)-E_X^I(n+1)
 =\mathbf1_{\mathcal I_X}(n)
 \left[d_X^\star(n)-\int_n^{n+1}d_X^\star(t)dt\right].
\]

There is no cutoff atom. The all-column identities and estimates of `L-91733`
therefore apply literally.

## 5. Source ownership

Every source occurrence follows exactly one path:

```text
inner source kept as a labelled causal-child colour;
retained outer whole cell or unused bottom/top omission;
Hall match, Hall bonus, or Hall residual;
first rough owner;
causal current or internal causal child;
one martingale endpoint state.
```

At every split the outgoing nonnegative weights sum to the incoming weight.

```text
measurable exact Hall integration        complete
activation collars                       absent
Hall mesh/refinement                      absent
one global positive quantizer             complete
whole-cell mismatch seed                  exact
all child colours internal                exact
native comparison                         next lemma
```
