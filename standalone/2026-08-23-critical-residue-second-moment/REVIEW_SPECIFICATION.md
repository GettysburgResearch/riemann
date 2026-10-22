# Hostile review specification for T-105100

Exact proposed head: freeze the submitted PR head before review.

Load-bearing files:

- claims/lemmas/L-105100-critical-residue-second-moment-balance.md
- claims/theorems/T-105100-critical-residue-second-moment-frontier.md
- claims/methodology/M-105100-hostile-review-contract.md
- claims/refutations/R-105100-root-ledger-alone-does-not-bound-m2.md
- experiments/X-105100-critical-residue-second-moment/verify.py
- experiments/X-105100-critical-residue-second-moment/tests/test_verify.py
- experiments/X-105100-critical-residue-second-moment/results/verification.json
- README_105100.md
- PACKET_METADATA_105100.json

## Reconstruction order

1. Recompute the residues of \(p^2/(p'p'')\) at zeros of \(p'\) and \(p''\).
2. Translate the roots to zero centroid.
3. Expand \(L=p'/p\) through order \(z^{-5}\).
4. Form \(L(L'+L^2)\) through order \(z^{-7}\).
5. Invert and independently simplify the \(z^{-1}\) coefficient.
6. Check the real/nonreal split without changing algebraic squares into
   absolute squares.
7. Replay the cubic, asymmetric quartic, translation, and firewall fixtures.

## Mandatory hostile mutations

- Delete the \(p''\)-zero residues: the quartic firewall must fail.
- Replace centered moments by raw moments: the translated cubic must fail.
- Omit one critical root: the coverage check must reject the fixture.
- Flip the sign of the \(V_4\) coefficient: the asymmetric quartic must fail.
- Replace algebraic squares by absolute squares: the
  \(x^3+x+1\) nonreal-critical fixture must fail.
- Promote the finite identity to Xi: the scope audit must reject the packet.

## Exact scope

The proposed theorem is finite and algebraic. The checker is
EXACT_RATIONAL, but it authenticates fixtures rather than proving the
universal theorem. The proof is the displayed residue/Laurent calculation.
Content hashes normalize CRLF to LF before SHA-256 so the same tracked text is
portable across checkout platforms.

The review must not accept any of the following without separate proofs:

- canonical-product limit passage;
- localization from the global sum to a finite height window;
- bounds for the off-real critical correction;
- bounds for the second-level cross-residue debt;
- RCMV104530;
- the Riemann Hypothesis.
