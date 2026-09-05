# M-105110 — Review contract for oriented-edge cancellation

Claim ID: M-105110

Status: **HOSTILE REVIEW CONTRACT**

Created: 2026-08-23

Depends on: L-105103; L-105105; L-105107; L-105109; L-105110; R-105110

RH status: **unproved**

## Cauchy-kernel ledger

- Fix the edge orientation before checking any sign.
- A normal exterior approach is not itself an oriented-integral divergence.
  For an interior projection, the simple kernel has a bounded arctangent
  jump even though its supremum and absolute integral diverge.
- The real logarithmic term records the ratio of the two tangential endpoint
  distances.  It is uniformly bounded only when the projection stays away
  from both endpoints.
- A pole projecting to a corner gives a one-sided logarithmic divergence.
  Do not silently pair adjacent edges.
- Reversing the edge orientation reverses every displayed integral.

## Application contract

- Continue the **weighted quotient** \(W_jh_j\), not merely \(h_j\),
  meromorphically across the open edge.
- Authenticate every approaching exterior pole and its full local order.
- For the simple-pole theorem, verify the weighted residue formulas and a
  uniform \(\ell^1\) bound on those residues.
- Verify uniform corner-projection separation.
- Subtract the authenticated principal parts and bound the remaining term in
  edge \(L^1\).  Selector norm control alone is not a remainder estimate.
- Multiple or common events need the full confluent principal parts from the
  L-105103 recurrence and are outside the simple-pole theorem.

## Exact fixtures

- For \(F_\delta=e^{z^2/2-\delta z}\), use
  \(w=z-\delta\),
  \(h_1=1/w\), and
  \(h_2=1/w-w/(w^2+1)\).
- The edge \(E_a\) is upward, so both centered integrals tend to
  \(-i\pi\).  A downward orientation flips the sign.
- The parameter \(a\) is fixed when asserting absolute-integral divergence.
  If \(a/\delta\) stays bounded or tends to zero, that conclusion need not
  hold.
- On a left-hand rectangle the pole \(\delta\) is exterior and the interior
  manifest is empty.  The unit weight is a fixed test weight, not the optimum
  for an empty interpolation problem.

## Stable-manifest firewall

- For
  \(F_N=\exp((1-e^{-Nz^2})/(2N))\), check
  \(F_N'/F_N=ze^{-Nz^2}\) before making any event claim.
- The only first-quotient pole globally is the simple target zero; its residue
  and optimal selector norm are one.
- The right-edge integral is purely positive imaginary and exceeds
  \(e^N/(5N)>N^2/30\).
- The full normalized contour charge stays one.  This forces cancellation
  among edges; it does not bound any individual edge.
- Call \((e^{Nz^2}-1)/z\) the additive holomorphic remainder.  It is not
  zero-free, even though the multiplier \(e^{Nz^2}\) is.

## Scope firewall

- The positive theorem is a sufficient finite-edge certificate, not a Xi
  estimate.
- The negative family treats only the first quotient, varies with \(N\), has
  infinite order, and uses shrinking-height rectangles.
- No Xi continuation, exterior manifest, weighted residue sum, corner
  separation, pole-subtracted remainder estimate, cofinal edge passage,
  strict coherence, RCMV104530, or RH conclusion follows.
