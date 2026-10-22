# R-91440 — SHARP-source mass fractions do not control endpoint-score loss

Claim ID: `R-91440`  
Status: **EXACT ALGEBRAIC REFUTATION OF ONE SCORE-RECURRENCE STEP**  
Created: 2026-08-12  
Corrects: the mass-fraction inference in `T-91424.4--8` on PR #407  
Depends on: `L-91339/L-91340`  
RH status: **unproved**

## 1. Two distinct positive ledgers

The positive target and endpoint-score atoms are

\[
 W_\Psi(x,n)=\frac{4\sqrt x}{n}-\frac3{\sqrt n},
 \qquad
 W_S(x,n)=\frac{5\sqrt x}{n}-\frac3{\sqrt n}.
\tag{R-91440.1}
\]

They are not proportional. Their ratio is

\[
 q_x(n)=\frac{W_\Psi(x,n)}{W_S(x,n)}
       =\frac{4t-3}{5t-3},
 \qquad t=\sqrt{x/n},
\tag{R-91440.2}
\]

and ranges from `1/2` at the endpoint to `4/5` at deep scale.

Consequently a fraction of native SHARP target mass is not, in general, the same fraction of endpoint score or signed score loss.

## 2. Exact two-atom control

Take `x=4`. Then

\[
 W_\Psi(4,4)=\frac12,
 \qquad W_S(4,4)=1,
\tag{R-91440.3}
\]

while

\[
 W_\Psi(4,1)=5,
 \qquad W_S(4,1)=7.
\tag{R-91440.4}
\]

Put

\[
 \nu=\delta_4+\frac1{10}\delta_1,
 \qquad
 \nu_A=\delta_4,
 \qquad
 \nu_B=\frac1{10}\delta_1.
\tag{R-91440.5}
\]

The two pieces carry equal SHARP mass:

\[
 \mathfrak T_4(\nu_A)
 =\mathfrak T_4(\nu_B)
 =\frac12,
 \qquad
 \frac{\mathfrak T_4(\nu_A)}{\mathfrak T_4(\nu)}
 =\frac12.
\tag{R-91440.6}
\]

But their score masses are

\[
 \mathfrak S_4(\nu_A)=1,
 \qquad
 \mathfrak S_4(\nu_B)=\frac7{10},
\]

so

\[
 \boxed{
 \frac{\mathfrak S_4(\nu_A)}{\mathfrak S_4(\nu)}
 =\frac{10}{17}
 >\frac12.
 }
\tag{R-91440.7}
\]

This difference is exact.

## 3. Failure of the generic homogeneity inference

Consider the positive homogeneous loss functional corresponding to the zero packing,

\[
 \mathfrak D(\lambda)=\mathfrak S_4(\lambda).
\]

Then

\[
 \mathfrak D(\nu_A)=1,
\]

whereas weighting the parent loss by the SHARP-mass fraction gives

\[
 \frac12\mathfrak D(\nu)
 =\frac12\cdot\frac{17}{10}
 =\frac{17}{20}<1.
\tag{R-91440.8}
\]

Thus the implication

```text
child is a positive restriction of the native SHARP source
+ score loss is homogeneous
=> child loss <= (SHARP-mass fraction) * parent/full loss
```

is false without an additional shape theorem.

## 4. Consequence for the candidate full proposal

`T-91424` defines

\[
 \theta_{\mathbf p,q}
 =\frac{\|\mu_{\mathbf pq}\|}{\|\mu_{\mathbf p}\|}
\]

from the total mass of the native SHARP source measure and then uses this same number as the coefficient of inherited endpoint-score loss. Equations (R-91440.3)--(R-91440.8) show that this is not a consequence of positivity and homogeneity.

The exact correction is to use the **score mass**

\[
 s(\nu)=\mathfrak S_x(\nu)
\]

for the branching weights, while retaining the target as a separate positive submeasure. `L-91339/L-91340` provide the two-ledger structure needed for that correction.

Even after changing weights, one must still prove one of the following:

1. a source-linear packing functor valid uniformly for every normalized positive kernel measure; or
2. exact self-similarity of every normalized child shape.

Neither follows from a scalar mass identity.

## 5. Scope

This refutation does not disprove the factor-54 route, least-prime source disintegration, or target one-use. It rejects only the displayed score-recurrence coefficient in the candidate proof as presently justified.

```text
positive SHARP source partition                    MAY SURVIVE
SHARP-mass subprobability                          MAY SURVIVE
SHARP mass = score-loss coefficient                FALSE
score-normalized branching                         CORRECTED TARGET
shape-uniform child packing functor                 OPEN
PR #407 full-proof conclusion                       BLOCKED AS WRITTEN
Riemann Hypothesis                                  UNPROVED
```
