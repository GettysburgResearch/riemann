# Exact counterexample to completed-cascade SHARP preservation in PR #399

**Review artifact:** `REV-PR399-01`  
**Created:** 2026-08-12  
**Reviewed source head:** `4981bcd2ae05e5a4e41e2877cbf9b4e020081a69`  
**Live descendant checked:** `59b1d1773b0f1d98712d58b66f41202e5f221717`  
**Classification:** exact symbolic counterexample; no numerical approximation

## Targeted claim

`claims/lemmas/L-91325-monotone-transport-disintegration-forgets-rough-colors.md` uses the one-factor identity

\[
(1,2)N_p=(1,2)M_p
\]

and then states:

> The same identity survives arbitrary completed rough cascades.

That sentence is load bearing. It is used to identify the completed colored states with an exact positive partition of the native source-block measure

\[
\mathfrak B(u)=((1,2)u)\,\mu_Y,
\]

and then to disintegrate one physical target among the rough colors.

## The matrices

Put

\[
r=p^{-1/2},\qquad 0<r<1.
\]

The arithmetic rough Euler matrix of `L-91319` is

\[
M(r)=(1-r)
\begin{pmatrix}
1+2r&-2r\\
r&1-r
\end{pmatrix},
\]

and its entrywise-positive completion is

\[
N(r)=(1-r)
\begin{pmatrix}
1+2r&0\\
r&1-2r
\end{pmatrix}.
\]

Let

\[
w=(1,2).
\]

For one factor,

\[
wN(r)=wM(r)
=(1-r)(1+4r,\,2-4r).
\]

Thus the one-step statement in `L-91319` is correct.

## Two factors

Take two rough primes with parameters

\[
r=p^{-1/2},\qquad s=q^{-1/2}.
\]

Since

\[
N(r)-M(r)
=r(1-r)
\begin{pmatrix}
0&2\\
0&-1
\end{pmatrix},
\]

we obtain

\[
\begin{aligned}
wN(s)N(r)-wM(s)M(r)
&=wM(s)\,[N(r)-M(r)]\\
&=\boxed{\bigl(0,\,12rs(1-r)(1-s)\bigr)}.
\end{aligned}
\]

The second component is strictly positive for every pair of finite rough primes.
Consequently, for the positive input state `u=(0,1)^T`,

\[
\boxed{
 wN(s)N(r)u-wM(s)M(r)u
 =12rs(1-r)(1-s)>0.
}
\]

A hypothesis-matching concrete pair is `p=67`, `q=71`:

\[
\boxed{
 wN_{71}N_{67}\binom01
 -wM_{71}M_{67}\binom01
 =\frac{12}{\sqrt{67\cdot71}}
  \left(1-\frac1{\sqrt{67}}\right)
  \left(1-\frac1{\sqrt{71}}\right)>0.
}
\]

No floating-point sign decision is involved.

## Why the one-step identity does not tensorize

The equality `wN(r)=wM(r)` only says that `w` annihilates the correction when the correction is the **leftmost operation seen by** `w`. After another rough factor, the relevant row is `wM(s)`, not `w`, and

\[
wM(s)[N(r)-M(r)]\ne0.
\]

Therefore one-step preservation of a left functional does not imply preservation under products unless that functional is a common left eigenvector in the stronger intertwining sense required by the full semigroup.

## Exact consequences

The following PR #399 assertions are contradicted at the submitted hypotheses:

1. the sentence that `(1,2)N_p=(1,2)M_p` survives arbitrary completed rough cascades;
2. exact preservation of the native source-block measure by products of the completed matrices;
3. the derivation of the global positive source partition in `L-91325.14` from those products;
4. the coefficient-one score/source recurrence insofar as it uses that purported mass preservation.

The abstract Markov-kernel disintegration theorem remains correct **conditional on an independently proved positive source partition**. It cannot manufacture such a partition after this failure.

## Relation to the live descendant

The ten-commit descendant ending at `59b1d1773b0f1d98712d58b66f41202e5f221717` introduces:

- `L-91326`, a common quadratic Hilbert defect telescope; and
- `L-91327`, a positive four-state parity dilation with a linear total-variation telescope.

Those are genuine replacements for the failed completed-matrix cascade. Both files explicitly leave the linear endpoint realization / recursive parity projection and bounded all-generation score ledger open. They therefore do not restore the submitted complete proof.

## Verdict

```text
one-factor SHARP preservation                         VERIFIED
arbitrary completed-cascade SHARP preservation       FALSE
completed states -> exact native source partition    UNPROVEN / blocked
abstract target disintegration given a partition     VERIFIED
PR #399 full composition at 4981bcd...                FALSE AS SUBMITTED
live four-state continuation at 59b1d177...           UNPROVEN / GAP
Riemann Hypothesis                                    UNPROVEN
```
