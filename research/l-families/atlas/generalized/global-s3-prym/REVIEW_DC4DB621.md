# Independent review: Frobenius descent and the second elliptic quotient

Reviewed scientific commit: `dc4db621017ddaa8aeca1acfb211374dc0f04501`.

This review covers the six new files under `research/l-families/atlas/generalized/global-s3-prym`: `FROBENIUS_DESCENT_AND_SECOND_ELLIPTIC_QUOTIENT.md`, `descent_replay.py`, `descent_source.json`, `test_descent_replay.py`, `descent_artifact.json`, and `descent_provenance.json`. The frozen provenance binds the proof SHA-256 `95615d6ad5ab9e5d8a83d2598a67135e4eba3e8239115833f2a00f52bec8f0ff` and artifact SHA-256 `ba3d477e58339b5f4f3274c69ccded106db633598d3bb0096a4b3701e886cd63`.

The reviewer independently read the proof, producer and all 11 test definitions, and checked the frozen inventory and provenance. The reviewer ran no computation. The main agent reports focused Ruff, producer write and both check modes, and all 11 tests in normal and optimized Python passing at this freeze.

## Mathematical assessment

No blocking error found. With the declared geometric-Frobenius convention, character spaces are permuted by multiplication by `q`; a character orbit of length `r` contributes the return-map factor `det(1-T^r F^r|H_j)`. This is a cyclic-block determinant identity, not a product of factors in the un-substituted variable. The note correctly warns that a single Frobenius orbit need not be a full cyclotomic Galois orbit, so its coefficients need not be rational in general.

For the order-three pair when `q=-1 mod 3`, the orbit has dimension six, its polynomial is even, and its alternating duality has top coefficient `q^3`. Writing the factor as `Q(T^2)` yields the reciprocal cubic relation forcing the root `Q(-1/q)=0`, hence the factor `1+q T^2`. The residual degree-four shape and its weight bound follow with the stated imported curve-weight theorem. The order-three infinity orbit has local denominator `1-T^2`; its odd/even trace distinction is essential and retained.

The forced factor has an actual source explanation. For `C_3: w^6=f_3(x)`, the map `z=w^2` gives the smooth genus-one cubic `E': z^3=f_3(x)` with rational point `(1:1:0)` at infinity. When `q=2 mod 3`, the cube map is bijective on the base field and only one point at infinity is rational, so `#E'(F_q)=q+1` and its numerator is `1+q T^2`. The source-defined full `mu_6` character decomposition separates this quotient from `E` and leaves the stated primitive-character residual summand. No elliptic isomorphism or Weil-restriction classification is inferred from divisibility alone.

The complete infinity accounting is consistent with the normalized projective curves: the number of cube-root infinity points is one in odd extension degree and three in even degree. Finite branch stalks and the descended conductor ledger match the earlier frozen source. The proof distinguishes geometric character labels from arithmetic Frobenius action throughout.

## Producer and falsification assessment

The new field class allows precisely the declared `F_5` extension degrees through six, with cap 15625, without silently increasing the cap of the frozen field implementation. Its arithmetic and irreducibility construction were inspected; the tests independently check the degree-five and degree-six moduli and overlap with the old small fields. No field-state expansion beyond the declared finite cap is requested.

The even-extension character calculation chooses an explicit nontrivial cube root in each field model. This would not by itself establish norm-compatible character labels across unrelated models. The proof and producer instead use the special Frobenius interchange of the two order-three spaces: their return traces are equal and conjugate, hence rational. The code checks that property for every sum and independently compares twice the character trace with the complete curve-count difference. The orientation independence is therefore justified for this special descent, not generalized without proof.

Three even extensions reconstruct the cubic return factor; its `T^2` substitution predicts all six base extension traces. Complete counts separately reconstruct the elliptic factors and the genus-four curve factor, with reciprocity explicitly identified where used. Tests include swapped-root orientation, odd/even infinity, the cyclic-block substitution, the forced-factor sign, reciprocal completion, invalid strata and source-authentication controls. The test inventory does not imply that all genus-four coefficients were obtained from eight independently counted extensions.

## Scope

This packet realizes a classical cohomological factor through actual covers and supplies exact bounded replay. It does not claim external novelty, transport to the integer Riemann source, a new RH proof, or an unconstructed global infinite-rank determinant. Imported trace, quotient, duality and weight theorems remain mathematical dependencies. This is an independent read and audit, not an independent test execution or formal verification.
