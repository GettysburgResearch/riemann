# R-91402 — SHARP preservation does not make the rough completion a subprobability branch

Claim ID: `R-91402`  
Status: **EXACT SCOPE FIREWALL**  
Created: 2026-08-12  
Depends on: PR #399 `L-91319/L-91320/L-91325` notation  
RH status: **unproved**

## 1. The positive completed rough map

For one rough prime `p`, put

\[
 r=p^{-1/2}.
\]

The positive SHARP-preserving completion used on PR #399 is

\[
 \boxed{
 N_p=(1-r)
 \begin{pmatrix}
 1+2r&0\\
 r&1-2r
 \end{pmatrix}.
 }
 \tag{R-91402.1}
\]

The native block-mass functional is

\[
 w=(1,2),
 \qquad
 w(L,R)^T=L+2R.
\]

The completion preserves this functional relative to the signed arithmetic map `M_p`:

\[
 wN_p=wM_p.
\]

This identity is exact and remains valid.

## 2. The subprobability shortcut is false

Direct multiplication gives

\[
 \boxed{
 wN_p=
 \left(
  (1-r)(1+4r),
  2(1-r)(1-2r)
 \right).
 }
 \tag{R-91402.2}
\]

The first coefficient is

\[
 (1-r)(1+4r)=1+3r-4r^2.
\]

For every

\[
 0<r<\frac34,
\]

and in particular for every rough prime `p>=67`,

\[
 \boxed{(1-r)(1+4r)>1.}
 \tag{R-91402.3}
\]

Taking the positive input state `(L,R)=(1,0)` yields

\[
 wN_p(1,0)^T> w(1,0)^T.
\]

Therefore

\[
 \boxed{wN_p\nleq w}
 \tag{R-91402.4}
\]

componentwise. The completed branch is not a sub-Markov/subprobability map on the whole positive `(L,R)` cone.

## 3. Exact drift cone

For a general positive state,

\[
 \boxed{
 w(N_p-I)\binom LR
 =r\left[(3-4r)L-(6-4r)R\right].
 }
 \tag{R-91402.5}
\]

Thus the native mass is nonincreasing exactly on the cone

\[
 \boxed{
 L\le
 \frac{6-4r}{3-4r}R.
 }
 \tag{R-91402.6}
\]

The threshold is strictly larger than `2` for every `r>0` and tends to `2` as `r->0`. Hence the simple source-specific condition

\[
 L\le2R
\]

is sufficient, but it is not known automatically for the complete rough state. In the diagonal coordinates it is the sign condition

\[
 Y=L-2R\le0.
\]

Treating that sign as automatic would reintroduce the Möbius obstruction.

## 4. Consequence for transport disintegration

The abstract statement

```text
positive state branches + preservation of L+2R
    => positive submeasure partition of one native block
```

is invalid without an additional ledger. One must prove at least one of:

1. the actual rough state remains in the cone (R-91402.6);
2. the positive mass drift in (R-91402.5) is supplied, coefficient one, by the finite `P_61` forcing/outer endpoint block;
3. an augmented state-space colligation carries an explicit nonnegative forcing coordinate whose total mass restores subprobability;
4. the complete full-output cone has a positive dual margin after this drift coordinate is included.

The endpoint Schur inequality can pay a projective **matrix** correction, but matrix positivity alone is not a scalar source-submeasure identity. The scalar drift must remain visible in the target partition.

## 5. Corrected finite-margin target

For the factor-54 route, the robust-grid certificate of `L-91401` must include the additional output coordinate

\[
 \boxed{
 \mathfrak d_p(L,R)
 =r[(3-4r)L-(6-4r)R].
 }
 \tag{R-91402.7}
\]

Its positive part must be absorbed by an explicitly assigned forcing/slack coordinate before the target is disintegrated. Omitting this coordinate can produce a formally positive family of branches whose total native block mass exceeds the parent.

## 6. Scope

This does **not** refute the factor-54 programme, the positive matrix completion, the affine Pascal lift, or a source-specific completed reset. It refutes only the inference that SHARP preservation by itself supplies the subprobability hypothesis needed for scalar target disintegration.

```text
N_p entrywise positive                         EXACT
w N_p = w M_p                                 EXACT
w N_p <= w on full positive cone              FALSE
exact native-mass drift                       EXACT
source-specific drift compensation            OPEN
full-output rational margin including drift   OPEN / FINITE
factor-54 RH reset                             OPEN / RH-BEARING
Riemann Hypothesis                            UNPROVED
```
