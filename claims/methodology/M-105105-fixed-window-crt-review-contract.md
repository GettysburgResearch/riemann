# M-105105 — Hostile review contract for fixed-window CRT jet selectors

Claim ID: M-105105

Status: **REVIEW METHODOLOGY**

Created: 2026-08-23

RH status: **unproved**

Reject L/T-105105 if any item below fails.

## Event and pole accounting

- The manifest covers the union of all interior zeros of \(F'\) and \(F''\)
  and contains no duplicate or boundary event.
- Actual pole orders are \((r-m)_+\) and \((r+s-2m)_+\), not raw
  denominator orders.
- Common removable points receive no artificial modulus.
- Every \(F''\)-only actual \(Q\)-pole is present exactly once.
- Targets are exactly all real, noncommon, odd-order \(F'\)-zeros in the
  authenticated window manifest; omission fails even if two supplied target
  lists agree with each other.

## Selector congruences

- At a target of order \(r\), \(W_1\) has leading local term
  \(w^{r-1}\) modulo \(w^r\).
- At the same target, \(W_2\) has leading local term
  \(r w^{2r-2}\) modulo \(w^{2r-1}\).
- At every nontarget actual pole, the selector vanishes to the full actual
  pole order.
- Reduced representatives are unique only modulo the full primary modulus.
- Weighted residues are recomputed from exact Taylor series, independently
  of the CRT congruence constructor.

## Polynomial corollary

- The supplied factorization of \(f'\) reconstructs it exactly.
- Each multiplicity factor is monic and square-free; distinct strata are
  pairwise coprime.
- \(D_r=(f'/A_r^r)(A_r')^r\) is inverted only after its unit condition is
  checked modulo \(A_r\).
- The nonlinear stratum \((x^2-1)^3\) authenticates the full power
  \((A_r')^r\); replacing it by \(A_r'\) must fail.
- The second carrier satisfies \(H\equiv R^2\pmod{S_{\rm odd}}\).
- All-root traces are not relabeled as real-window moments; nonreal algebraic
  squares are not replaced by modulus squares.

## Mutation firewalls

- Missing, duplicate, or extraneous event manifests fail closed.
- Missing target nodes fail both against a separately frozen target manifest
  and against the eligible set derived from the event manifest.
- Omitted, mislabeled, nonmonic, nonsquare-free, or overlapping polynomial
  strata fail closed.
- For \(x^4-1\), squaring \(W_1P\) has residue zero; omitting the factor
  \(r=3\) from \(W_2\) gives \(1/48\), not \(1/16\).
- For the simple cubic, the unweighted adjacent-pole charge \(2/9\) differs
  from the selected second moment \(5/18\).
- For \(F=z-z^5/5\), the event \((m,r,s)=(1,0,3)\) at zero has
  \(d_1=0,d_2=1\); its unweighted \(Q\)-residue \(-1/4\) must be killed.
  The same fixture has nonzero real/even selectors and authenticates the
  conjugation/parity claim.
- Normal and optimized Python reproduce the same authenticated artifact.

## Scientific boundary

- Selector existence is conditional on a complete exact finite-window event
  manifest.
- No selector degree, coefficient, or boundary-norm estimate is inferred.
- No rational square-free factor is claimed to isolate an arbitrary real
  embedding or interval.
- No common affine-invariance claim is made across mixed critical orders;
  horizontal rescaling acts with order-dependent powers.
- No Xi event census, cofinal-window estimate, RCMV104530, or RH conclusion
  follows formally.
