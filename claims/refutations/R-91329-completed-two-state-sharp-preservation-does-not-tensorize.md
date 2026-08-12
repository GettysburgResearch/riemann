# R-91329 — The completed two-state SHARP identity does not tensorize, but this does not rule out an interleaved reset policy

Claim ID: `R-91329`  
Status: **EXACT REFUTATION / SCOPE CORRECTION**  
Created: 2026-08-12  
Corrects: the arbitrary-cascade sentence in `L-91325-monotone-transport-disintegration-forgets-rough-colors.md` at `4981bcd2ae05e5a4e41e2877cbf9b4e020081a69`  
Review source: PR #405, head `97d40e6574ba54d827fd361c70d550eeb60c9faf`  
RH status: **unproved**

## 1. One rough factor

For `0<r<1`, put

\[
 M(r)=(1-r)
 \begin{pmatrix}
  1+2r&-2r\\
  r&1-r
 \end{pmatrix},
 \qquad
 N(r)=(1-r)
 \begin{pmatrix}
  1+2r&0\\
  r&1-2r
 \end{pmatrix},
\]

and let

\[
 w=(1,2).
\]

Direct multiplication gives the valid one-step identity

\[
 \boxed{wN(r)=wM(r).}
\tag{R-91329.1}
\]

Thus the positive completion preserves the SHARP output for one operation on an arbitrary current state.

## 2. Exact two-factor failure

For a second parameter `s`,

\[
 N(r)-M(r)
 =r(1-r)
 \begin{pmatrix}
  0&2\\
  0&-1
 \end{pmatrix}.
\]

Using `wN(s)=wM(s)`, one obtains

\[
\begin{aligned}
 wN(s)N(r)-wM(s)M(r)
 &=wM(s)[N(r)-M(r)]\\
 &=\boxed{
  \bigl(0,12rs(1-r)(1-s)\bigr)
 }.
\end{aligned}
\tag{R-91329.2}
\]

The difference is nonzero for every pair of finite rough primes. In particular, with

\[
 r=67^{-1/2},\qquad s=71^{-1/2},
\]

and input `(0,1)^T`, the excess is strictly positive.

Therefore the statement

```text
w N_(p_k) ... N_(p_1) = w M_(p_k) ... M_(p_1)
```

is false already at depth two.

## 3. Lifecycle consequence

The following assertion in the submitted `L-91325` proof is false:

> the one-prime identity survives arbitrary completed rough cascades.

Accordingly, the derivation of an exact native source partition from that product identity is invalid. The abstract measure-theoretic disintegration theorem remains correct conditional on a separately proved positive source partition.

The full composition at `4981bcd...` is therefore false as submitted. This is a refutation of that proof composition, not of RH.

## 4. Exact scope of the counterexample

Equation (R-91329.2) compares two *uninterrupted products*:

\[
 N(s)N(r)
 \quad\text{and}\quad
 M(s)M(r).
\]

It does **not** refute a genuinely interleaved reset construction in which, after each rough operation, one applies a typed positive reset map, records its outer and slack measures, and passes a newly constructed positive residual state to the next generation.

For such a controlled recursion, the relevant identity at step `j` is only

\[
 wN(r_j)u_j=wM(r_j)u_j
\]

for the *current controlled state* `u_j`. No theorem requires that the final controlled state reproduce the uncorrected raw product on the initial state.

This distinction does not rescue the submitted proof: PR #399 does not yet contain the required one-step typed source/target/score partition. It does show that the exact counterexample cannot by itself rule out every interleaved two-state reset policy.

## 5. Correct frontier

```text
one-factor SHARP preservation                        EXACT
uninterrupted completed-cascade preservation         FALSE
submitted native source partition                    UNPROVEN / blocked
abstract target disintegration given a partition     EXACT
interleaved reset induction                          ABSTRACTLY AVAILABLE
one-step typed positive reset partition              OPEN / RH-BEARING
Riemann Hypothesis                                   UNPROVEN
```
