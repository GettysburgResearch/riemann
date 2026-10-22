# L-29817 — Divisor-sum source banks decode exactly to adjacent commutators

Claim ID: `L-29817`  
Title: For a finite coefficient source entering through multiples/divisor incidence, the exact Möbius decoder returns the source coefficients themselves, and the adjacent-tree flow realizes the complete carry target with an explicit square-root variation bound  
Status: **PROPOSED COMPLETE EXACT FINITE LEMMA**  
Authoring agent: `gpt56-02-r`  
Created: 2026-08-08  
Dependencies: `L-29816`  
Scope: exact source-to-carry congruence for divisor-sum banks; all-generation source variation remains separate

## 1. Divisor-sum target

Let `c_2,...,c_X` be arbitrary real coefficients and define the carry-column
target

\[
 \boxed{
 h(q)=\sum_{k\le X/q}c_{kq}
 =\sum_{\substack{n\le X\\q\mid n}}c_n,
 \qquad 2\le q\le X.}
\tag{L-29817.1}
\]

This is the natural target produced by a node/cumulative source bank before the
floor divergence is differentiated.

## 2. Möbius inversion is the identity on the source bank

Apply the multiples-Möbius decoder of `L-29816`:

\[
 u_m=\sum_{k\le X/m}\mu(k)h(mk).
\tag{L-29817.2}
\]

Substitute (L-29817.1) and interchange finite sums. The coefficient of `c_n`
with `m|n` is

\[
 \sum_{k\mid n/m}\mu(k).
\]

It is one when `n=m` and zero otherwise. Therefore

\[
 \boxed{u_m=c_m.}
\tag{L-29817.3}
\]

No coprimality condition occurs.

## 3. Exact carry flow

Equation (L-29816.4) becomes

\[
 \boxed{
 \mathscr A(c)
 =\sum_{m=2}^{X}c_mE_{m-1}.}
\tag{L-29817.4}
\]

Its node divergence has cumulative source `c_m`, and its carry loads are
exactly (L-29817.1):

\[
 \boxed{
 \operatorname{load}_q\mathscr A(c)=h(q).}
\tag{L-29817.5}
\]

Thus an emitted coefficient vector may be carried into PR #272's actual split
space without a formal tensor product or scaled sibling identity.

## 4. Capacity bound

By `L-29816.9`,

\[
 \|E_{m-1}\|_{\omega,1}
 \le4(2+\sqrt2)\sqrt m.
\]

Hence

\[
 \boxed{
 \mathcal N_\omega(\mathscr A(c))
 \le4(2+\sqrt2)
 \sum_{m=2}^{X}\sqrt m\,|c_m|.}
\tag{L-29817.6}
\]

The exact proof-facing norm of a source coefficient bank is therefore

\[
 \boxed{
 \|c\|_{\sqrt\cdot,1}
 =\sum_{m=2}^{X}\sqrt m\,|c_m|.}
\tag{L-29817.7}
\]

This bound charges every noncoprime residue chain through the actual adjacent
commutators.

## 5. Adjacent divisor dipoles

As a useful control, take

\[
 c=\delta_a-\delta_b.
\]

Then

\[
 h(q)=\mathbf1_{q\mid a}-\mathbf1_{q\mid b}
\]

and

\[
 \boxed{
 \mathscr A(c)=E_{a-1}-E_{b-1}.}
\tag{L-29817.8}
\]

This gives a square-root-cost realization of a long divisor dipole without the
false scaled sibling tensorization and without an additive chain of length
`|a-b|`.

## 6. Euler source banks

For a node-labeled Euler jet, take

\[
 c_{N+r}=(-1)^r{M\choose r}a_{N+r},
 \qquad0\le r\le M.
\tag{L-29817.9}
\]

Equation (L-29817.4) is the exact carry-flow binding.  The mode separation and
Hausdorff matching of `L-29812` may be used to reorganize its weighted
variation, but no claim that a positive formal source atom is itself a
nonnegative carry flow is required.

A full boundary proof must bound the sum of (L-29817.7) over every finite jet,
exact remainder, common arithmetic destination, and half-scale generation.

## 7. Proof boundary

Proved here:

- exact inversion of every divisor-sum source bank;
- exact adjacent-commutator carry flow;
- explicit square-root weighted variation bound;
- exact long divisor-dipole control.

Open:

- all-generation square-root variation of the emitted source banks;
- DCD;
- RH.
