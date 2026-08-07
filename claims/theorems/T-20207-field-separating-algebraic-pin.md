# T-20207 — A tiny field-separating algebraic pin is enough

Claim ID: `T-20207`  
Title: Exact quadratic-field pinning prevents every pole cancellation without transcendental coefficients  
Status: **PROPOSED — COMPLETE ALGEBIC RESIDUE ARGUMENT PENDING INDEPENDENT REVIEW**  
Authoring agent: `gpt56-pro-09-n`  
Created: 2026-08-07  
Dependencies: `T-20206`; elementary algebraic number theory; conductor inclusion for abelian subfields of cyclotomic fields  
Scope: the endpoint Fejer family and, more generally, any finite algebraic filter

## 1. Coefficient field

For the endpoint degree-`N` filter of `L-20211`, every coefficient belongs to the
cyclotomic field

\[
\boxed{
 K_N=\mathbb Q(\zeta_{4(N+1)}).}
\]

Indeed the coefficients are obtained from finitely many sines and cosines at
rational multiples of `pi` by rational arithmetic.

Choose a rational prime `p` satisfying

\[
 p\equiv1\pmod4,
 \qquad
 p\nmid4(N+1).
\]

Then the quadratic field `Q(sqrt p)` has conductor `p`. If `sqrt p` belonged to
`K_N`, this quadratic field would be an abelian subfield of
`Q(zeta_(4(N+1)))`, forcing its conductor to divide `4(N+1)`, a contradiction.
Hence

\[
\boxed{
 \sqrt p\notin K_N.}
\]

For any integer `B>=1`, put

\[
\boxed{
 \eta_{N,p,B}=2^{-B}\sqrt p>0.}
\]

The pin can be made arbitrarily small by increasing `B`, while remaining an
exact quadratic algebraic number outside the coefficient field.

## 2. Pinned positive filter

Define

\[
 \widetilde P_{N,p,B}(x)
 =P_N(x)+\eta_{N,p,B}(1-\cos x).
\]

It is nonnegative. At a hypothetical off-line zero of multiplicity `m`, the
common-pole residue of the filtered logarithmic derivative is

\[
\boxed{
 \mathcal R=m\eta_{N,p,B}+A,}
\]

where `A in K_N`: it is a finite integer-multiplicity combination of the base
filter coefficients.

If `mathcal R=0`, then

\[
 \eta_{N,p,B}=-A/m\in K_N,
\]

contradicting `sqrt p notin K_N`. Thus every off-line zero remains an
uncancelled pole.

The Landau and critical-mesh argument of `T-20206` therefore applies verbatim:
for every fixed `N,p,B`, eventual nonnegativity or a subpower negative part of
the pinned samples implies RH.

## 3. Exact debt

The prime ramp is

\[
 \widetilde L_{N,p,B}(s)
 =L_N(s)+2^{-B}\sqrt p\,(1-s)_+.
\]

At the half-knot,

\[
\boxed{
 {\widetilde L_{N,p,B}(1/2)
  \over
  \widetilde L_{N,p,B}(0)}
 ={
  (N+1)\sin^2(\pi/[2(N+1)])+2^{-B-1}\sqrt p
  \over
  N+1+2^{-B}\sqrt p}.}
\]

Choose, for example, `B>=3N`. Then the pin cost is exponentially smaller than
the sharp `O(N^-2)` Fejer debt.

At the critical mesh, the pin still touches only

\[
 q\le n^{2/N}.
\]

## 4. General field-separation lemma

Let `K` be any number field and let

\[
 P_0(x)=\sum_{k=1}^{N}\lambda_k^{(0)}(1-\cos kx)\ge0
\]

have every coefficient in `K cap R`. If `eta>0` is any algebraic number outside
`K`, then

\[
 P_0+\eta(1-\cos x)
\]

has the same residue-noncancellation property. At a parent pole its residue is
`m eta+A` with `A in K` and `m>=1`, hence cannot vanish.

Thus transcendence is unnecessary: **field separation** is the exact mechanism.

## 5. Proof-production advantage

The quadratic pin can be represented exactly as a pair

\[
 a+b\sqrt p,
 \qquad a,b\in K_N,
\]

and all finite contractions can use directed real embeddings plus exact symbolic
binding. No decimal approximation is part of the pole proof.

## 6. Status boundary

This theorem strengthens only the exposure layer. It does not prove the
cofinal arithmetic sign. The cyclotomic-field inclusion and conductor argument
must be independently reviewed before promotion.
