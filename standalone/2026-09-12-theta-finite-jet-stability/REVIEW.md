# Review request and limits

Review this as a changed-source component theorem, NOT as a proposed RH proof.
The author's attempted completion of the native all-degree sign did not succeed.

## Load-bearing claims

1. Check the Fourier sign of `D^(2m)(D^2-1/4)` for EVEN m. The two occurrences
   of `1/4` are tied to the actual xi endpoint normalization, not a free scale.
2. Check whole-line positivity. It follows from term-polynomial majorants on
   every `Q>=3` and reflection, not from a numerical theta sample. Confirm
   `P0(Q)>=18`, the leading-term threshold, and all negative coefficients.
3. Verify that the changed density has exactly the same normalization and
   moments below order `2m`. Confirm the integrations by parts at both ends.
4. Verify the polynomial factorization, its strict positivity on ALL real v,
   and the new roots. The root at `R+i/4` is explicitly constructed; it is not
   an actual xi zero discovered numerically.
5. Check the exact m=20 bounds and the complete Gaussian envelope. Large
   rational integers are hashed in binary, but the accepting code reconstructs
   their values and inequalities, rather than accepting the hashes as evidence.
6. Inspect the inheritance of the parent's spectral-index argument. The new
   function still has a summable genus-zero reciprocal divisor. Its added
   polynomial has 21 distinct nonreal conjugate root pairs. No first negative
   degree is bounded or computed. Analytic multiplicity and distinct-pair
   count remain different notions.

## Precise missing native theorem

For the unchanged theta cumulants, prove

```
H_d=(q_(i+j+2))_(0<=i,j<=d) >=0 for EVERY d.
```

When H_d is positive definite its next extension requires the sign of
`q_(2d+4)-b^T H_d^-1 b`. A finite Newton recurrence is not a proof of that sign.
This manuscript supplies neither that estimate for every d nor an alternative
source-complete positivity mechanism.

## Important properties NOT preserved by the counterfunctions

The ordinary Euler product, the literal second-order differential theta source,
and confinement of all zeros to the critical strip are not retained. Additional
nonreal roots generally occur outside the strip as well. Accordingly the result
cannot refute a proof that genuinely uses these additional arithmetic facts.
It does not imply a native cumulant matrix is negative or a Lee--Yang model
fails its known zero theorem.

The example DOES preserve every finite input to the previous two 9x9 matrices,
the entire real zero divisor and signs, reflection, endpoints, positivity and a
stronger-than-previous absolute source envelope. Its relevance is to the proposed
finite-data/shape/continuity inference, not to every possible RH proof.

## Execution distinctions

Only the new exact polynomial arithmetic and bounded controls are executed.
The previous 768-bit theta quadrature, earlier spin constructions and all other
agents' numerical campaigns are NOT rerun. Source-file byte authentication is
not mathematical acceptance. The supplied infinite arguments need independent
paper review. No Lean proof, full-repository build or remote CI success is claimed.
