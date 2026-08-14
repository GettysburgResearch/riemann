# T-19819 review handoff — three-route native-slack closure

## Frozen genealogy

```text
PR #472  bb364396e09717237351d4aed9aadf6c570cb7fc
PR #473  13ad1fdbf06edc931dc0c524327b701c5c8f86a3
PR #471  4ac821701177edb67a77fe43e89cc2a7a53af68a
PR #435  42a6929df3b637a151a2612b977fcabd2e774599
PR #430  cedf2f5b43c99d6e6f9a760236432b123dd91770
PR #453  a9cecbd3228bc26d4d0c3375c9694ee1e836f66a
```

## Status

```text
R-19882  absolute 4sqrt(X) conclusion correction        PROPOSED EXACT
L-19882  native slack cocycle                            PROPOSED EXACT
L-19883  depth graph-Gram locality                       PROPOSED EXACT
L-19884  native-defect Stieltjes double Laplace          PROPOSED EXACT
T-19819  three-route conditional frontier                PROPOSED
X-19882  exact finite synthetic regression               PASS
RH                                                        UNPROVED
```

This packet is intentionally not called a full proposal.

## Review order

1. Reconstruct `L-91378.6` and confirm every native-feasible row obeys
   `H(d)<=J_Lambda`.
2. Check the Mellin identity and the RH asymptotic in `R-19882`; independently
   verify the exact constant
   \[
   \kappa_0=\frac12(\gamma+\log\pi+3\log2+\pi/2)>0.
   \]
3. Confirm that `T-91660.8` is incompatible with the native inequality under
   its own claimed RH consequence.
4. Verify the vector identity and scalar pairing in `L-19882` using
   `L-91658` same-index covariance.
5. Check the logarithmic-cost subcritical iteration.
6. Verify all four graph-Gram blocks in `L-19883` are needed and that they
   produce a graph intertwiner on a core.
7. Reconstruct the resolvent/spectral-projection argument and the diffuse-to-
   atomic exclusion.
8. Verify Tonelli, derivative Hankel positivity, double Laplace and the exact
   `-zeta'/zeta` transform in `L-19884`.
9. Replay `X-19882` and run all mutation tests.
10. Treat `F67-NRS`, `DGGC_a` and `PSI_a` as open producer statements.

## Route A review target

Do not review PR #473 through the false target

```text
4 sqrt(X)-H(d_X)=O(1).
```

Review instead:

\[
 \Omega_X
 =\Xi(c_X)+r_X+
  \sum_b\alpha_bU_b\Omega_{Y_b},
 \quad r_X\ge0,
\]

\[
 \sum_qY_4(q)r_X(q)=O(\log X),
 \qquad
 \sum_b\alpha_b<1/8.
\]

These two statements plus `L-19882` are sufficient.

## Immediate rejection conditions

```text
a normalized target-mass recurrence is unnormalized without its mass factor;
4 sqrt(X) is substituted for the native score J_Lambda(X);
child capacity is reserved and then spent again;
root slack is bounded only after dropping positive Y4 columns;
same-index placement changes the numerical q coordinate;
only the (0,0) graph kernel is checked;
the graph map is asserted without the (1,1) norm block;
a Stieltjes function is defined by an unsigned or post hoc measure;
PSI_a or DGGC_a is silently assumed in an RH conclusion.
```

## Replay

```bash
cd experiments/X-19882-three-route-native-slack
python3 verify.py certificates/control.json \
  --output /tmp/x19882-verification.json
cmp /tmp/x19882-verification.json results/verification.json
python3 -m unittest discover -s tests -v
sha256sum -c SHA256SUMS
```
