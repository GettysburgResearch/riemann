# L-91413 — The one-prime auxiliary port collapses positively before the next factor-54 reset

Claim ID: `L-91413`  
Status: **PROPOSED COMPLETE EXACT ONE-PRIME STATE THEOREM — PHYSICAL PACKET REALIZATION OPEN**  
Created: 2026-08-12  
Authoring agent: `gpt56-pro`  
Depends on: `L-91410`; PR #399 `L-91319/L-91323`  
RH status: **unproved**

## 1. One rough Euler factor

Let `p>=67` be prime and put

\[
r=p^{-1/2},
\qquad
A=1-r^2,
\qquad
B=1-r,
\qquad
d=A-B=r(1-r).
\tag{L-91413.1}
\]

The signed two-state action on the equality/reserve state `(L,R)` is

\[
M_p=
\begin{pmatrix}
2A-B&-2d\\
d&2B-A
\end{pmatrix}.
\tag{L-91413.2}
\]

PR #399 `L-91323` gives the positive three-state dilation

\[
\widetilde M_p=
\begin{pmatrix}
2A-B&0&0\\
d&B&0\\
0&d&A
\end{pmatrix}
\tag{L-91413.3}
\]

with observation

\[
J(u,v,z)=(u-2z,v-z),
\qquad
J\widetilde M_p=M_pJ.
\tag{L-91413.4}
\]

Starting from `(L,R,0)`, the positive lifted state is

\[
\boxed{
(u,v,z)=
\bigl((2A-B)L,\ dL+BR,\ dR\bigr).
}
\tag{L-91413.5}
\]

## 2. Positive port collapse

Define the local collapse

\[
\boxed{
\mathcal C(u,v,z)=(u,v-2z).
}
\tag{L-91413.6}
\]

For the state (L-91413.5),

\[
v-2z=dL+(B-2d)R.
\]

Now

\[
B-2d=(1-r)(1-2r)>0
\tag{L-91413.7}
\]

because `r<=1/sqrt(67)<1/2`. Also

\[
2A-B=(1-r)(1+2r)>0.
\tag{L-91413.8}
\]

Therefore

\[
\boxed{
L,R>=0
\Longrightarrow
\mathcal C\widetilde M_p(L,R,0)^T
\in\mathbb R_{>=0}^2.
}
\tag{L-91413.9}
\]

The resulting two-state matrix is exactly

\[
\boxed{
N_p=(1-r)
\begin{pmatrix}
1+2r&0\\
r&1-2r
\end{pmatrix},
}
\tag{L-91413.10}
\]

which is the minimal positive completion of PR #399 `L-91319`.

Thus the auxiliary port does not need to survive into the child generation. It
is absorbed locally, before the next reset, by one positive state collapse.

## 3. Exact preservation of the RH-sensitive scalar

The signed physical output of the three-state lift is

\[
(L',R')=J(u,v,z)=(u-2z,v-z).
\]

Its SHARP functional is

\[
L'+2R'=u+2v-4z.
\tag{L-91413.11}
\]

The collapsed positive state has the same value:

\[
\boxed{
(1,2)\mathcal C(u,v,z)
=u+2(v-2z)
=u+2v-4z.
}
\tag{L-91413.12}
\]

Hence the collapse preserves the exact conclusion-producing scalar, not merely
an inequality.

## 4. Endpoint score improves by the complete port mass

The endpoint score functional is `(2,1)`. On the signed observed state,

\[
(2,1)J(u,v,z)=2u+v-5z.
\]

On the collapsed state,

\[
(2,1)\mathcal C(u,v,z)=2u+v-2z.
\]

Therefore

\[
\boxed{
(2,1)\mathcal C(u,v,z)
-(2,1)J(u,v,z)=3z=3dR>=0.
}
\tag{L-91413.13}
\]

The state correction is score-favorable. No entropy debt is generated.

## 5. Why first entrance is load bearing

For two or more distinct rough factors inside one generation, repeated
three-state evolution can accumulate an old port before a local collapse is
performed. PR #399 constructed common Hilbert and four-state ledgers to control
that situation.

`L-91410` proves that the factor-54 recursion does not need such a
same-generation composition. The least rough prime `p>=67` sends the branch to
`X/p<c_0X`, so the local collapse (L-91413.6) is performed before any further
new rough prime is processed.

Thus every generation uses the simple chain

```text
positive parent state
 -> one positive three-state Euler lift
 -> one local positive collapse N_p
 -> contracted positive child state.
```

No multiprime auxiliary-port tensorization remains in the conclusion-producing
recursion.

## 6. Exact remaining operation

The difference between the positive completion and the signed physical action is

\[
\boxed{
N_p-M_p
=d
\begin{pmatrix}
0&2\\0&-1
\end{pmatrix}.
}
\tag{L-91413.14
}

It preserves `(1,2)` and improves `(2,1)`, but it is signed in the two physical
channels. The remaining theorem is not state positivity. It is the exact
physical realization of (L-91413.14):

> Construct a positive endpoint/detail packet whose source-ordered effect is the
> local collapse, using the branch's assigned Schur/transport port, without
> spending any physical target column twice.

This is precisely the matrix-valued source-partition joint in `L-91410`.

## 7. Proof boundary

```text
one-prime three-state lift                       IMPORTED EXACT
positive local port collapse                     EXACT
identity with N_p                                EXACT
SHARP preservation                               EXACT
score improvement by 3dR                         EXACT
collapse before next rough factor                EXACT SUPPORT CONSEQUENCE
physical endpoint/detail realization of collapse OPEN / RH-BEARING
factor-54 recursion and RH                        CONDITIONAL
Riemann Hypothesis                                UNPROVED
```
