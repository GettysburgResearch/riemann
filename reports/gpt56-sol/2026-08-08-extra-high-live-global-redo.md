# Extra-high live global redo and full-problem frontier

Date: 2026-08-08  
Agent: `gpt56-sol`

## Purpose

This pass deliberately redoes the two preceding research passes from the live repository rather than inheriting their narrative. It then continues the requested full-problem attack. The result is a corrected global architecture plus new proved algebra; **RH is not claimed proved**.

## 1. Corrections to the previous two passes

The earlier fast narrative substantially overstated how close several mechanisms were.

### 1.1 Rank-one parity contraction is false

The tentative `2x2` parity shortcut is exactly refuted on PR #263:

\[
\det(vv^*-T^*vv^*T)
=-|v_+v_-|^2|a-b|^2.
\]

Unequal channel multipliers force an indefinite direction. The ratio-three transition is also `3^{-s}`, not a power of the dyadic variable `2^{-s}`.

### 1.2 Raw annular `H^1` tail transfer is invalid

The raw opposite-parity annular signal is piecewise exponential with jump atoms and is not automatically in the absolutely-continuous Sobolev domain used by the digital-tail theorem. PR #263 now records that domain mismatch explicitly.

### 1.3 Restricted Mersenne saturation is false at the claimed cofinal scope

PR #314 supplies a hypothesis-matching Farkas obstruction to eventual Restricted Mersenne Saturation. The earlier Mersenne-collar route therefore cannot be promoted to a proof.

### 1.4 Terminal boundary atomization is false

PRs #311/#313/#317 show that ordinary divisor-source atomization of the stopped critical boundary has linear or polynomial cost on macroscopic quotient cells. Any proof which source-inverts that boundary before recombination manufactures a large obstruction.

The same boundary has only logarithmic native paired/central-flow variation on PR #316. The order of operations is load bearing.

### 1.5 Strict contraction of the complete eta source is impossible

PR #323 proves that the normalized eta transfer has multiplier

\[
1-\eta(1/2+i\xi),
\]

and at every critical zeta zero this equals **one** exactly. A source-blind translation-invariant norm containing that oscillatory mode cannot strictly contract the complete eta state.

This is not merely a no-go. It fixes the correct scale threshold.

## 2. The sharp spectral target is coefficient-one scale descent

PR #333 proves the correct normalization. If `rho=beta+i gamma` is a zeta zero, the principal Mellin mode is neutral under eta propagation, while endpoint doubling changes its amplitude by

\[
2^{\rho-1/2},
\qquad
|2^{\rho-1/2}|=2^{\beta-1/2}.
\]

Therefore

```text
critical-line zero       scale factor 1;
off-line zero            scale factor >1.
```

A recurrence

\[
\boxed{
E(J)\le C(1+J)^A+E(J-\delta)
}
\]

with one fixed `delta>0` already gives polynomial energy after `O(J)` iterations and hence the subexponential pole bound required for RH. Strict coefficient `<1` is unnecessary and, on the principal mode, impossible.

The full proof architecture must therefore be triangular:

```text
principal dyadic RH mode       carry losslessly with coefficient one;
transverse analytic channels   contract strictly;
cutoff/cap channels            pay polylogarithmic source-complete debt;
```

## 3. Durable finite coordinate: Cycle Debt

The most robust carry coordinate remains PR #272. For the exact target divergence `r_X`,

\[
\mathfrak N_\eta(X)
=
\min_z\sum_e\omega_e[-d_X^{\rm tree}-C_\eta z]_+
\]

and finite LP duality gives

\[
\mathfrak N_\eta(X)
=
\max_F\left[-\sum_mr_X(m)F(m)\right],
\]

subject to

\[
0\le F(n)-F(j)-F(n-j)\le\omega_{n,j}.
\]

A subpower bound gives the sharp prime ramp and RH. Generic bounded-rank, monotonicity, or source-free cone theorems have all failed against explicit separators/firewalls; the proof must preserve the actual principal source.

## 4. Strongest existing boundary result

PR #316 proves that the complete first activated boundary has

\[
\sum_n\sqrt n\,|b_X(n)-b_X(n+1)|=O(\log X)
\]

and supplies the actual signed central-flow certificate with `O(log X)` negative capacity debt and a strict half-scale residual.

It further proves, for every analytic depth `a` and every power exponent `s>=1/2`, that the fully telescoped **fresh** endpoint profile

\[
h_{a,X,s}(x)
=x^{-s}\log\min\{2^a(x-1)+1,X\}
\]

has polylogarithmic native first-difference debt uniformly in depth.

What remains is propagation/recombination of an already-injected cap state under later stages.

## 5. New theorem `L-32301`: strong transverse contraction

Define

\[
\left\|\sum_{h\ge0}a_hx^{-\sigma-h}\right\|_{\sigma,\star}
=
\sum_{h\ge0}|a_h|(1+h)^4 64^{-h}.
\]

The exact shifted central operator obeys

\[
\boxed{
\|\mathscr C f\|_{\sigma,\star}
\le\frac67\|f\|_{\sigma,\star},
\qquad\sigma\ge1/2.
}
\]

The proof uses the previously proved radius-`1/4` row bound and

\[
(1+\ell)^4 64^{-\ell}\le4^{-\ell}.
\]

For the all-depth endpoint profile, below its cap

\[
h_{a,X,s}(x)
=x^{-s}\left[
\log2^a+\log x
-
\sum_{\ell\ge1}
\frac{(1-2^{-a})^\ell}{\ell}x^{-\ell}
\right],
\]

and the complete faster-power tail has weighted norm below

\[
\log(4/3)<1/3
\]

uniformly in depth. Above the cap the profile is simply `log X x^{-s}`. The two branches are continuous and have exactly one derivative jump.

Thus the all-generation obstruction cannot lie in analytic power tails, faster-power proliferation, polynomial exponent losses, or depth-dependent affine-log coefficients. All of those channels are strictly transverse and contractive.

## 6. New theorem `L-32302`: the RH-sensitive current is already a dyadic dipole

For an inverse pair `omega*a=epsilon`, with

\[
\Lambda=\omega*(a\log),
\qquad
W=\omega*\Lambda,
\]

one has exactly

\[
W(s)=\Omega'(s),
\qquad
\boxed{W(n)=-\omega(n)\log n}.
\]

For the opposite-parity source

\[
\omega_2
=\mu-\frac32\delta_2*\mu+\frac12\delta_4*\mu,
\]

the local polynomial on every odd squarefree core is

\[
p(z)=(1-z)^2(1-z/2).
\]

The complete logarithmic source fiber is

\[
-\mu(u)[\log u\,p(z)+(\log2)zp'(z)].
\]

Because `p(1)=p'(1)=0`, every complete fiber has zero total mass. More strongly,

\[
\log u\,p(z)+(\log2)zp'(z)
=
\frac{1-z}{2}
\left[(3\log2+\log u)z^2-(5\log2+3\log u)z+2\log u\right].
\]

Hence

\[
\boxed{W=(\varepsilon-\delta_2)*V}
\]

fiberwise for an explicit three-tap logarithmic source `V`. The normalized inverse of `(epsilon-delta_2)` has delays `2^{-j/2}` and is `ell^1`, so this dipole extraction does not change the exponential block-energy exponent.

This is an important cross-route lesson: **move the complete RH-sensitive dipole before invoking any positive inverse or proper-divisor expansion**. Absolute source expansion destroys exactly this cancellation.

## 7. Haar/bottom scalar and exact analytic cancellation

PR #333 supplies the critical Haar source

\[
\nu_2=\mu-\sqrt2\,\delta_2*\mu,
\]

whose carry charge is the constant `sqrt(2)-1` on every interior split and negative only on endpoint neighbors. It gives the exact three-bottom-coordinate telescope

\[
\mathcal H_2(X)
=
\log X+
\sum_a[-(1+\sqrt2)r_a(2)+\sqrt2 r_a(3)+\sqrt2 r_a(4)].
\]

The infinite analytic central resolvent then cancels the entire `log X` main term **exactly**:

\[
\log X+
\sum_a\mathcal B(\mathscr C^aw_X^\infty)
=
\frac{\log2}{\zeta(1/2)}.
\]

Therefore all nonconstant arithmetic behavior is the finite cutoff Duhamel correction. This is an excellent one-sided consumer, but bounding that correction is still RH-bearing; the exact telescope does not itself close the proof.

## 8. Leading full-problem architecture after the redo

The strongest current architecture is now:

```text
exact principal dyadic source / Haar scalar
-> extract complete dyadic dipole fibers
-> contract every analytic/faster-power transverse channel (6/7)
-> pay each fresh cap injection with the explicit polylog central-flow certificate
-> propagate only the neutral cap/dipole principal state
-> prove a coefficient-one fixed-scale recurrence
-> polynomial Cycle Debt / shell energy / Haar scalar
-> Mellin/Landau pole exclusion
-> RH.
```

A valid final theorem may be phrased as a Critical-Neutral Cap Recurrence:

\[
D_{\rm cap}(2Y)
\le D_{\rm cap}(Y)+C\log^A(2Y),
\]

or as an exactly equivalent coefficient-one recurrence for the principal dyadic physical energy. It must retain all Pascal-cycle freedom and all same-destination source recombination before a negative part or norm.

## 9. Other live routes after the redo

### Prime-annulus commutator

PR #289 gives an exact fixed top-quarter statistic retaining every zeta pole. Its local energy `PAE` is equivalent to RH. It is a clean scalar firewall, but no independent PAE bound is proved.

### Two-contact source / reflected Selberg

PRs #302/#330 close the source-matched current-scale interior reserve with an absolute scale-independent constant and absorb endpoint energy. The remaining theorem is a source-coupled lower-scale Schur recurrence for the principal inverse-zeta mode. This is very compatible with the coefficient-one neutral architecture above.

### Square-root hinge carry route

PRs #329/#332 reduce the elementary route to square-root hinge positivity. Directed positivity through large finite endpoints is evidence only; the inner hinge remains a Mertens/reciprocal-zeta theorem.

### Brownian route

The variance and convex-order reductions remain genuinely independent, but SAT/stop-loss saturation remains RH-equivalent and unproved.

## 10. Routes no longer treated as near-complete

```text
restricted Mersenne saturation          refuted
terminal atomic boundary closure        refuted
fixed-order Abel positivity             refuted
rank-one parity contraction             refuted
strict complete eta contraction         impossible at zeta modes
conditional-Hankel carry closure        refuted
monotone positive Divisibility Cover    refuted
source-free five-adic automaton         scope-corrected / incomplete
pure prime-tail subpower queue          refuted/proposed refuted
```

## 11. Exact current frontier

A complete proof still requires a supplied theorem, not reviewer labor:

> Preserve the principal dyadic cap/dipole source through each support-halving step and prove a coefficient-one delayed recurrence after every transverse analytic component and fresh cap injection has been discharged by the existing exact certificates.

The new work removes several previously suspected obstructions and fixes the correct spectral normalization, but this principal recurrence has not yet been proved.

## 12. Status

```text
live graph re-audited                         YES
previous parity shortcut                      REFUTED
previous raw-H1 shortcut                      WITHDRAWN
Mersenne restricted saturation                REFUTED
terminal atomic closure                       REFUTED
strict complete eta contraction               IMPOSSIBLE / wrong target
quartic-weighted analytic interior            PROPOSED COMPLETE
RH-sensitive dyadic dipole factorization      PROPOSED COMPLETE
fresh all-depth boundary injections           IMPORTED / PROPOSED COMPLETE
coefficient-one neutral recurrence            OPEN / RH-BEARING
unconditional proof of RH                     NO
```
