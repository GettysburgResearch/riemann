# Validation and limitations

The mathematical note and checker have the same author. No independent
agent, external referee, Lean build, upstream theorem rebuild, actual zero
calculation or repository-wide CI is claimed.

Freshly run in this pass:

- Ordinary and optimized Python reproduce CHECKS.json byte-for-byte.
- 192 rational/Gaussian-rational configurations compare the original nested
  rational factor with the expanded numerator and first mixed cancellation.
- 240 configurations impose the actual algebraic relation dW=1/q and
  E=b q^4 d^6 v, and test the resonant expansion and local lower margins.
- 108 finite polynomial models independently assemble the Laurent finite
  part and recover the compensated logarithmic derivative, at multiplicities
  1 through 12. Their roots are SYNTHETIC, not purported zeta zeros.
- The transverse derivative is explicitly distinguished from the tangential
  derivative; six separately executed `python -O` mutations fail at their
  intended predicates. MUTATIONS.json gives the exact errors.
- The 2,035 count includes repeated guards and identities within those cases;
  it is not 2,035 independent analytic cases.
- An initial combined ZIP-replay command reached its 20-second tool limit.
  Separate ordinary and optimized replays then completed successfully and
  matched CHECKS.json. The final archive is byte-compared below; the verifier
  and reports are unchanged. The manifest authenticates bytes, not validity.

The q values 7,13,25,49 and phases 1,-1,i,-i are algebraic fixtures for the
rational identity. They are not a complete CT ray-character/ideal census;
no residue-field computation or full ramified Gauss-source reconstruction is
claimed. The proof of the infinite product uses the written uniform
majorant, not these finite tests.

The primary CT v2 and de Faveri manuscript bodies could not be retrieved
freshly. Their deep estimates are not inputs to this packet. The explicit
unramified factor was read live in the pinned #971 file. Its identification
with a physical CT contour integral retains that upstream source contract.
Classical Dedekind continuation/functional equation is used explicitly.

Highest-priority review: PROOF (2) and (5)-(6); the correlated error (9)-(10)
and the vertical derivative bound (8); the finite-S factor in (13); and
meromorphic Laurent coefficients at a crossing (rho,0) in (15)-(17).
In particular, restricting a ratio to t=0 must not be mistaken for joint
holomorphy or for a bound on its normal derivative.

Exploration not promoted: numerical optimization of existing numerator and
mollifier moment envelopes did not establish a stronger global bound. One
broad optimization command timed out; smaller runs completed. None of that
floating exploratory output is used as proof or included in CHECKS.json.
