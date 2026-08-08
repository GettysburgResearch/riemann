# R-30401 — Root-only capacity is not expanded central-tree capacity

Claim ID: `R-30401`  
Title: Expanding the canonical central-tree layer cake adds descendant copies of the same central edge, so the root coefficient `c_n-c_(n+1)` is not its total available coefficient  
Status: **EXACT SCOPE CORRECTION**  
Authoring agent: `gpt56-sol`  
Created: 2026-08-08  
Frozen parent: PR #303 at `4367007d658c78a42024a9c94c3c6b078cac2568`  
Dependencies: PR #272 `L-27204`; PR #303 `R-30202`  
Scope: the capacity calculation in the canonical positive central-tree realization; no assertion that all required capacities are available

## 1. Canonical layer cake

Let

\[
c_2\ge c_3\ge\cdots\ge c_N\ge0,
\qquad c_{N+1}=0,
\]

and put

\[
d_m=c_m-c_{m+1}.
\]

For the complete central trees

\[
T_1=0,
\qquad
T_m=[m,\lfloor m/2\rfloor]
 +T_{\lfloor m/2\rfloor}
 +T_{\lceil m/2\rceil},
\]

the positive layer cake is

\[
\mathcal T(c)=\sum_{m=2}^N d_mT_m.
\tag{R-30401.1}
\]

Its carry load is the decreasing divisor source, as recorded on PR #303.

## 2. The omitted descendants

Write

\[
h_n=[n,\lfloor n/2\rfloor].
\]

The summand `d_nT_n` contributes `d_n` to `h_n`, but larger trees can contain
additional copies of the same edge.  Therefore the total coefficient

\[
\kappa_n(c;N):=[h_n]\,\mathcal T(c)
\]

is not generally `d_n`.

The smallest exact witness is

\[
N=4,
\qquad
(c_2,c_3,c_4)=\left(\frac12,\frac13,\frac14\right).
\]

Then

\[
(d_2,d_3,d_4)=\left(\frac16,\frac1{12},\frac14\right),
\]

while

\[
T_2=h_2,
\qquad
T_3=h_3+T_2,
\qquad
T_4=h_4+2T_2.
\]

Consequently

\[
\boxed{
\kappa_2
=\frac16+\frac1{12}+2\cdot\frac14
=\frac34,
}
\tag{R-30401.2}
\]

not `1/6`.

Thus the PR #303 capacity replay, which checks only the root weight
`c_n-c_(n+1)`, does not compute the coefficient of the expanded edge manifest.

## 3. What this does not repair

Descendant capacity is not automatically sufficient.  For example, at

\[
N=6,
\qquad c_m=1/m,
\qquad n=4,
\]

none of `T_5,T_6` contains `h_4`, so

\[
\kappa_4=c_4-c_5=\frac1{20},
\]

whereas the model sibling amount in `R-30202` is `1/5`.

Hence the corrected verdict is:

```text
root coefficient equals c_n-c_(n+1)          VERIFIED;
total expanded edge coefficient equals it    FALSE;
descendants can add substantial capacity      VERIFIED;
descendants always supply the requested edge  FALSE;
source-to-edge capacity problem                STILL OPEN in zero-defect form.
```

The purpose of this correction is not to revive the zero-defect claim.  It
prevents a root-only surrogate from being used as either a proof or a lower
bound for the actual expanded capacity.

## 4. Proof boundary

Closed exactly:

1. the descendant omission in the root-only calculation;
2. the rational witness (R-30401.2);
3. a rational witness showing that descendant capacity need not suffice.

Not closed:

1. a zero-defect central-capacity theorem;
2. Cycle Debt;
3. RH.
