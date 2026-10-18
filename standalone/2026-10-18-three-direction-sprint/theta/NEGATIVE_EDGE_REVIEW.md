# Independent internal review of the signed-edge completion consumer

Reviewed source: `../NEGATIVE_EDGE_COMPLETION.md`, actual-byte SHA256
`09751e346e6b983729706ad2a65ad63c8d0292b9a95c5ea0cc31145f5e3c8cef`.
Reviewer: parallel theta track. This is a scoped internal reconstruction,
not external referee acceptance or approval of an actual theta completion.

I reconstructed sections1--3 against the stated finite Ising hypotheses.
No blocking error was found at this scope.

For a negative edge with price a, inversion gives
`|J|=(log cosh(2a))/2<=a^2`, because `log cosh t<=t^2/2` for real t.
The double endpoint sum and nonnegative cross terms give
`sum_edges a^2 <= (1/2)sum_i(sum_j a_ij)^2`.
The site budget then gives K<=b^2 sum_i w_i^2/2. Ferromagnetic
zero-field correlations are nonnegative, including the diagonal1,
so Vplus>=sum_i w_i^2. All these inequalities remain valid with
arbitrary graph size and degree.

For each spin configuration the deleted negative interaction lies in
[-K,K]. This gives the two termwise partition bounds and the factor
exp(2K) for a partition ratio, with no missing sign or normalization.
The finite zero-field positive reference law is symmetric and of bounded
support. Conditional on the already established real-zero theorem in
MIXED_SIGN_STRIP.md, its even exponential-type Hadamard product has no
quadratic exponential factor; differentiation gives
Vplus=2sum_(lambda>0)lambda^(-2). Therefore its real MGF is bounded by
exp(Vplus c^2/2). The zero-field high-temperature expansion makes all
spin-product expectations nonnegative; expansion of field factors proves
Zplus(v)<=Zplus(|v|)<=Zplus(cw). Jensen gives Zplus(h)>=Zplus(0).
Combining these statements yields the exact whole-plane upper bound(5).

The normal-family consumer uses bounded Vplus, not merely bounded signed
variance. It works for varying graph sizes: Montel supplies subsequences,
Cauchy's formula transfers every fixed derivative, and all actual theta
derivatives determine the same entire function. Hurwitz then transfers
zero exclusion outside the prescribed band. No finite fit is used to
establish its cofinal premise.

In the symmetric subclass, the graph involution is preserved when J is
replaced by Jplus. Spin flip followed by that involution makes the
reference-field observable centered. FIELD_BUDGET_EQUIVALENCE.md thus
applies with the stated R>b. Partition comparison gives
Mplus,h(R)<=exp(2K) M_J,h(R), producing (8). The separate bound on
sum w_i^2 is essential to close this implication; the source explicitly
retains it and makes no circular claim when K is unbounded.

The mathematical dependency on MIXED_SIGN_STRIP.md's zero-band proof is
preserved. This receipt audits the negative-cost and compactness
consumer, rather than independently re-proving every Asano contraction
in that other file. The source accurately leaves the actual cofinal
theta construction and any improved zeta region open.
