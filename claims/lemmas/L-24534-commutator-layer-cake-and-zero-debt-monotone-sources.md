# L-24534 — Monotone adjacent-commutator sources telescope into a nonnegative central-tree certificate

Claim ID: `L-24534`  
Title: The complete Hausdorff tail of a divisor source has zero fragmentation debt; only its signed first-difference boundary can require repair  
Status: **PROPOSED COMPLETE — exact finite flow identity**  
Authoring agent: `gpt56-pro-25`  
Created: 2026-08-08  
Issue: #245  
Dependencies: PR #304 exact adjacent-tree commutator identity  
Scope: source-to-flow conversion before triangle inequalities

## 1. Central trees and adjacent commutators

Let `T_m` be the complete central binary fragmentation tree rooted at node `m`,
with `T_1=0`.  Its node divergence is

\[
\partial T_m=e_m-m e_1.
\tag{L-24534.1}
\]

Put

\[
E_{m-1}=T_m-T_{m-1}
\qquad(m\ge2).
\tag{L-24534.2}
\]

Then

\[
\partial E_{m-1}=e_m-e_{m-1}-e_1,
\]

and the exact carry load is

\[
L_q(E_{m-1})=\mathbf1_{q\mid m}.
\tag{L-24534.3}
\]

The individual `E_(m-1)` are signed flows.  Charging each one separately by a
triangle inequality is generally wasteful.

## 2. Discrete source integration by parts

Let `sigma_2,...,sigma_N` be any real finite source sequence and define

\[
\Phi(\sigma)=\sum_{m=2}^{N}\sigma_m E_{m-1}.
\tag{L-24534.4}
\]

Substituting (L-24534.2) and collecting equal trees gives the exact identity

\[
\boxed{
\Phi(\sigma)
 =\sigma_NT_N
  +\sum_{m=2}^{N-1}(\sigma_m-\sigma_{m+1})T_m.
}
\tag{L-24534.5}
\]

There is no boundary term at `T_1` because `T_1=0`.

Equation (L-24534.5) is the source-space analogue of Abel summation.  It must be
performed before any edgewise positive part or norm is taken.

## 3. Zero debt for monotone sources

Assume

\[
\sigma_2\ge\sigma_3\ge\cdots\ge\sigma_N\ge0.
\tag{L-24534.6}
\]

Every coefficient on the right side of (L-24534.5) is then nonnegative.  Since
each `T_m` is itself a nonnegative balanced fragmentation flow,

\[
\boxed{
\Phi(\sigma)\ge0\quad\text{edgewise}.
}
\tag{L-24534.7}
\]

Thus the complete monotone divisor source has **zero negative capacity debt**.
It realizes the load

\[
\boxed{
L_q(\Phi(\sigma))
 =\sum_{\substack{m\le N\\q\mid m}}\sigma_m
}
\tag{L-24534.8}
\]

by a literal nonnegative central-tree certificate.

This conclusion is stronger than the individual commutator estimate

\[
\|E_{m-1}\|_{\omega,1}\ll\sqrt m.
\]

For a monotone tail, the correct debt is zero, not the sum of the individual
upper bounds.

## 4. Hausdorff sources

Suppose

\[
\sigma_m=\int_0^1 t^m\,d\nu(t)
\]

for a finite positive measure `nu`.  Then `sigma_m` is nonnegative and
decreasing.  Applying (L-24534.5) under the integral gives

\[
\boxed{
\Phi(\sigma)
 =\int_0^1
 \left[t^NT_N+
       \sum_{m=2}^{N-1}(1-t)t^mT_m
 \right]d\nu(t),
}
\tag{L-24534.9}
\]

which is manifestly nonnegative.  Therefore every completely monotone common
tail produced by the finite Euler/Peano or eta-boundary analysis is already a
positive fragmentation object once its full source family is retained.

The difficult part is not the common Hausdorff tail.  It is the unmatched
parity/cutoff boundary which remains after that tail is extracted.

## 5. Exact signed remainder ledger

For a general source define

\[
c_m=\sigma_m-\sigma_{m+1}
\qquad(2\le m<N),
\qquad
c_N=\sigma_N.
\tag{L-24534.10}
\]

Then

\[
\Phi(\sigma)=\sum_{m=2}^{N}c_mT_m.
\tag{L-24534.11}
\]

Its negative edge debt is supported only on the negative coefficients
`(c_m)_-`.  In particular, a future proof may estimate a signed boundary by
first removing its greatest decreasing nonnegative minorant and charging only
the residual first-difference oscillation.

This is the correct global-potential formulation of terminal commutator repair:

```text
source values
-> discrete first-difference potential
-> nonnegative complete trees for the monotone part
-> signed debt only for oscillatory boundary variation.
```

It is categorically different from replacing `sigma` by `|sigma|`.

## 6. Application to the PR #304 audit

`R-24530` proves that the entire stopped critical collar is macroscopic in the
termwise atomic norm.  Equation (L-24534.5) shows that this does not force every
large boundary family to be expensive: a monotone common tail can be large and
still have zero debt.

However the unmatched first-odd outer-anchor family in `R-24530` is not a
single decreasing source sequence on the declared physical nodes: it is a
sparse parity boundary with gaps and repeated anchor labels.  A repaired proof
must therefore emit one of the following explicitly:

1. a source reindexing under which the complete family is Hausdorff and the
   carry loads in (L-24534.8) are preserved;
2. a dyadic/eta recombination whose first-difference oscillation is subpower;
3. an actual incoming-tree relative replacement paying the oscillatory part;
4. a sparse scalar estimate such as `L-24531`--`L-24533`.

The monotone-tail identity cannot be cited without that source-binding map.

## 7. Review mutations

A checker should reject:

- `sum |sigma_m| ||E_(m-1)||` used before (L-24534.5);
- omission of the endpoint coefficient `sigma_N T_N`;
- a claim of monotonicity after changing physical source labels;
- a Hausdorff representation which does not preserve divisor loads;
- positive/negative separation before all parity siblings are recombined.

## 8. Proof boundary

Proved exactly:

- the commutator layer-cake identity;
- zero debt for every decreasing nonnegative source;
- zero debt for every positive Hausdorff source;
- localization of signed debt to first-difference oscillation.

Open:

- a subpower bound for the actual critical parity/cutoff oscillation;
- RH.
