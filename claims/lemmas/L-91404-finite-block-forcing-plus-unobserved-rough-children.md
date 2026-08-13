# L-91404 — Expand the finite prime block, project only its forcing, and pass rough children unobserved

Claim ID: `L-91404`  
Status: **PROVED EXACT POSITIVE PACKET DECOMPOSITION**  
Created: 2026-08-13  
Depends on: paired least-prime recursion; finite Boolean expansion; affine Pascal covariance  
RH status: **unproved**

## 1. Finite-block expansion

Fix a paired channel parameter `a>=1`. Let

\[
P_{53}=\prod_{p\le53}p,
\]

and let `m` be the prime index of `59`. Iterating the exact paired recursion through the finite block gives

\[
\boxed{
\mathbf P_1^{(a)}(x)
=\sum_{d\mid P_{53}}d^{-1/2}S^{\omega(d)}
 \mathbf P_m^{(a)}(x/d).
}
\tag{L-91404.1}
\]

Insert the recursion for `\mathbf P_m` once:

\[
\boxed{
\mathbf P_1^{(a)}(x)
=\mathbf F_{53}^{(a)}(x)
 +\sum_{d\mid P_{53}}
  \sum_{\substack{p\ge59\\dp\le x}}
  (dp)^{-1/2}S^{\omega(d)+1}
  \mathbf P_{p+}^{(a)}(x/(dp)),
}
\tag{L-91404.2}
\]

where

\[
\boxed{
\mathbf F_{53}^{(a)}(x)
=\sum_{d\mid P_{53}}d^{-1/2}S^{\omega(d)}
 \binom{a\sqrt{x/d}-1}{0}.
}
\tag{L-91404.3}
\]

All terms in (L-91404.2) are positive paired measures. Unique factorization makes the forcing and every child source-disjoint.

## 2. Uniform scale contraction

Every rough child endpoint is

\[
Y_{d,p}=x/(dp)\le x/59<c_0x.
\tag{L-91404.4}
\]

Thus the complete infinite rough tail has been converted into a family of actual contracted packets after one fixed finite expansion.

No hidden coordinatewise hazard and no completed physical matrix occurs.

## 3. Mass and target ledgers

Taking any positive additive source mass in (L-91404.2) gives

\[
\boxed{
 m(\mathbf F_{53}^{(a)})
 +\sum_{d,p}m(P_{d,p})
 =m(\mathbf P_1^{(a)}).
}
\tag{L-91404.5}

The same identity holds after applying every positive linear target map. In particular, target shares are not guessed from a scalar branch coefficient; they are the images of the actual source subpackets.

For the SHARP source, apply (L-91404.2) separately to the balanced and reserve labels and then add their positive target measures.

## 4. Only the complete finite forcing is projected

The finite forcing `\mathbf F_{53}^{(a)}` is the complete 33-atom reset packet for the selected channel. Apply the certified finite Hall/row producer to this full packet.

Do **not** Hall-project any restricted rough child. Each child remains an actual paired packet and is passed to the next endpoint unchanged.

Therefore full-window Hall positivity is used only at its valid scope, and the restricted-packet Hall gap identified after `T-91402` disappears.

## 5. Child packing lift

Assume a child packet at endpoint `Y=x/(dp)` has a feasible finite packing. Apply the exact affine Pascal lift of scale `dp` to its row packet. The ordinary/radix-four response and target have the same critical covariance.

Because (L-91404.2) is a source-disjoint target partition, the sum of all lifted child packings plus the finite-forcing packing consumes the parent target once.

All children are pushed to the parent continuum coordinate and summed before the single finite quantizer, collar, omission and endpoint port are applied.

## 6. Score

The finite forcing producer is score-favorable up to a fixed mass-proportional boundary charge. Child score losses are not replaced by the loss of a preferred native packet; they remain attached to the actual child packets.

Consequently the natural recurrence is packet-valued:

\[
\boxed{
\Delta_x(P)
\le C m(P)+\sum_{d,p}\Delta_{x/(dp)}(P_{d,p}).
}
\tag{L-91404.6}

Equation (L-91404.5) is precisely the substochastic mass hypothesis used by `T-91401`.

## 7. Why the PR #431 hazard example does not apply

The review compares one coordinatewise hidden hazard with an `r`-scaled canonical physical child. Equation (L-91404.2) makes no such identification. The entire paired child submeasure is passed unobserved, with its own source, target, score and row data.

Survival and hazard coordinates may be used internally to prove source disjointness, but they are regrouped before any physical target or score normalization.

## 8. Proof boundary

```text
finite-block plus rough-child packet identity       EXACT
source disjointness and mass equality                EXACT
rough child contraction below c0                     EXACT
finite Hall used only on complete forcing            EXACT SCOPE
child physical affine covariance                     IMPORTED EXACT
one-use sum-before-quantize target assembly           IMPORTED / REVIEW
uniform finite forcing score debt                     IMPORTED / REVIEW
packet-envelope recurrence                            AVAILABLE
Riemann Hypothesis                                    UNPROVED
```
