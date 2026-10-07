# Building beyond the imported result

Status: proposed research programme, not a proof of any new zero-free line.
Starting point: the imported family-003 theorem, conditional on its verification, plus the exact source-qualified results in [REPO_COMPARISON.md](REPO_COMPARISON.md).

## 1. What should change in our priorities

The external work gives a concrete model of all-scale signed cancellation using a family that survives Fourier and automorphic transformations. Its most valuable part for this programme is that closure mechanism. The claimed $7/8$ line also gives a quantitative seed, but simply inserting the seed into our existing full MHB32 estimate does not improve it.

The first objective is therefore a new theorem about the **same native coarse covariance**, or a replacement family whose target extraction is fully proved. Another formulation of an RH-equivalent positivity problem would not meet this objective.

A sensible order is:

1. Verify the imported formal endpoints at the pinned source.
2. Reconstruct the shorter proof's actual completed family and its two-Poisson transfer.
3. Test whether its signed-support mechanism has an analogue for NRC32's exact coarse kernel.
4. Use the imported $3/4$ energy envelope and narrower CAP36 completion only where the new transfer explicitly needs them.
5. Attempt a strict exponent improvement with the full complement paid.
6. Consider a repeated contraction only after proving closure under every recursive child.

## 2. The decisive native target is already explicit

NRC32 decomposes the complete next square interval into fewer than $10(Y+1)$ blocks. It has an exact energy identity
\[
F_{(Y+1)^2-1}-F_Y=S_Y+D_Y,\qquad 0\le D_Y<5/6.
\]
The quantity $S_Y$ is the squared norm of the coarse **actual block means**, with the constant $2m(Y)$ and all repeated product representations included. Its full arithmetic formula is in the comparison note.

This is an unusually useful interface for a new method. The fine residual has a bounded total cost. An upper estimate for the complete coarse object would consequently control the whole square step.

The strongest desired theorem would be
\[
S_Y\le C(\log(2Y))^A(1+F_Y)^{2-\delta},\qquad \delta>0.
\]
That remains open. It would already bootstrap a crude polynomial seed to subpower energy. Consequently the existence of a better seed alone cannot be advertised as a proof of this missing theorem.

## 3. Import the signed-support mechanism, with a precise acceptance test

The October 5 second-transfer lemma performs three logically separate tasks:

- It writes all arithmetic preimages of a transformed source explicitly.
- It proves that those preimages carry one common coupled kernel.
- It sums their signed local weights, obtaining a divisor-support restriction and a smaller child family.

For our source, begin with the literal kernel
\[
Q_I=2m(Y)-\sum_{r,s\le Y}\mu(r)\mu(s)K_I(r,s).
\]
Expand $|Q_I|^2$ with its constant and mixed terms. Group by the complete arithmetic data of each transformed term, not merely by a product modulus. A candidate transfer must state which variables represent the original pair, the second pair from the square, the cell, and each common divisor.

The first acceptance test is algebraic: do all representations of the proposed transformed state have exactly the same physical kernel and cutoffs? If not, compute their signed kernel difference and charge its norm. Treating kernels with similar-looking scales as equal would erase precisely the difficult covariance.

The second test is arithmetic: does summing the signed local allocations force an additional support condition, or just reproduce the original source? Record the local polynomial at each prime, including repeated factors and zero masks. Our existing positive prime-pivot obstruction shows why a bound for isolated channels is not adequate.

The third test is quantitative: does the surviving support reduce the row length, product complexity, or native energy after all divisor multiplicities and kernel seminorms are included? Require a strict saving in an explicit exponent inequality. The imported local indicator identity is a model for this procedure, not an identity already established for $K_I$.

A useful first result can be restricted to one native block family, provided the rest of the interval has an independently paid cost small enough to preserve the total gain. A saving on a component whose complement dominates is not a new zero-free result.

## 4. Why the new strip may help with a transfer that was previously too expensive

Conditionally, the imported theorem gives
\[
m(Y)\ll_\epsilon Y^{-1/8+\epsilon},\qquad
F_Y\ll_\epsilon Y^{3/4+\epsilon}.
\]
CAP36 then permits a reciprocal-balanced completion of width
\[
J\ll_\epsilon Y^{7/8+\epsilon},
\]
with the bounded anchored-phase error derived in CONDITIONAL_BRIDGES.md:
\[
\|A_\tau-U_\tau\|^2
 \ll_{\epsilon,H}\tau^2Y^{5/4+\epsilon}
 \quad(|\tau|\le1,\ e^{i\tau\log Y}=1).
\]
At output scale $X\asymp Y^2$, its power is $X^{5/8+\epsilon}$, below the imported full-energy envelope $X^{3/4+\epsilon}$.

This pays one possible change-of-source cost more cheaply. It does not produce a small norm for either source. To use it, prove a native estimate for the source-compressed $A_\tau$, or a valid principal-phase extraction for $U_\tau$ over a phase range where the transfer cost stays small.

The present ADP37 guarantee needs a much longer phase range, reaching order $Y^2$. Its generic same-kernel counterexample also forbids automatic subpower extraction from a phase average. A future argument must explain both the phase scale and why the actual Möbius source has an extra property excluded by that counterexample.

## 5. A complete exponent budget before claiming a new strip

A more flexible target allows a residual scale cost:
\[
1+F_{Y^2}\ll_\epsilon
 Y^{a+\epsilon}(1+F_Y)^p,\qquad 1\le p<2.
\]
The same calculation applies to $(Y+1)^2-1$ at the exponent level, provided the exact endpoint recurrence is retained in the proof.

If $F_Y\ll_\epsilon Y^{\kappa+\epsilon}$, the output exponent is
\[
\kappa_{\rm new}=\frac{a+p\kappa}{2}.
\]
For the imported seed $\kappa=3/4$, a genuine improvement requires
\[
a<\frac34(2-p).
\]
For example, if a full estimate had the $p=4/3$ power already available for one of our restricted sectors, its remaining scale cost would have to satisfy **$a<1/2$** to improve the seed. This is an acceptance threshold, not a claim that the full estimate exists.

For fixed $a\ge0$ and $p<2$, repeated use tends to
\[
\kappa_\infty=\frac{a}{2-p}.
\]
Thus a one-time strict improvement does not imply RH. To approach $\kappa=0$, one needs $a=0$, or a justified sequence of estimates whose residual costs tend to zero while the useful contraction survives. Every changing family, mask, smoothing order, and target-extraction cost must remain within the corresponding estimates.

The small script [hybrid_exponent_budget.py](checks/hybrid_exponent_budget.py) checks this arithmetic and the actual MHB32 obstruction with exact rational numbers. Its hypothetical scenarios are explicitly labeled as such.

## 6. A family extension should preserve the target from the start

The external proof's family is effective because it includes the principal target in a way that can be extracted, and because it is stable under the transforms used in the proof. Our L-family work already warns that controlling nonprincipal members alone does not control zeta.

If building a hybrid character family for the native source, specify:

- The actual coefficient sequence for each character, including local zeros and finite prime exclusions.
- The exact completed support and the inverse operation recovering the desired source.
- Every auxiliary character introduced by reciprocity, reflection, or a Poisson transform.
- The bound on the sum over transformed rows, with constants uniform in the moving ranges.
- A quantitative extraction of the principal source with the extraction loss written into the exponent budget.

Over the Eisenstein field, base-change factorization transfers a zero-free theorem to zeta. It does not identify the ideal-Möbius energy with the real-integer Newton energy. An explicit coefficient or Mellin adapter is needed before transplanting our finite-prefix inequalities.

## 7. How to use the stronger $7/8$ proof without extrapolating its parameters

The September 30 manuscript has a useful general continuation criterion for arbitrary proposed boundary $\sigma_0\in(1/2,1)$. The current constructions verify its hypotheses only at their stated boundaries. This offers an organized route for improvement:

1. Keep the abstract continuation theorem unchanged.
2. Derive the actual compensated probe and moment capacities at a proposed new boundary.
3. Recompute every row range, exceptional inducing-character contribution, principal residue and contour error.
4. Produce a uniform positive margin in the final exponent inequalities.
5. Show the needed moments are proved at those capacities, rather than treating an optimized inequality as an analytic theorem.

The existing $7/8$ endpoint has a small exact margin, $49/440640$. It is useful for verifying the stated proof, but not evidence of unused room all the way to $1/2$. A numerical search that adjusts endpoint parameters may discover candidates; the outputs still need the analytic estimates that make those parameters admissible.

A promising direction is a stronger **joint** inverse/plain estimate, retaining their common row character and common height, instead of paying their costs separately. This is close to our concern with full coupled covariance. There is no such improved estimate established in this packet.

## 8. Other branches retain supporting roles

The Schur and heat approaches can organize and detect what a new cancellation theorem must control. Their full positivity remains open even if all possible off-line zeros are confined to a narrower strip. Finite numerics can expose a source mismatch or a bad parameter choice, but cannot certify the all-height hypothesis.

The separate Siegel-zero determinant proof is a second structural source worth reading, particularly for the existing Sylvester work. Its anisotropic interpolation and Frobenius divisibility should first be isolated as precise lemmas. There is presently no proved construction turning them into an upper bound on $S_Y$.

Family 007's claimed ordinary two-point correlation theorem is another possible input to investigate separately. This import does not audit or import that family's formalization. Fixed-shift cancellation alone does not control our weighted growing shifts or quartic prefix covariance; the comparison note gives exact identities showing the mismatch.

## 9. Concrete next deliverable

A strong next research pass should return one of the following:

- A verified four-target formal build with the exact compiled axiom report and source identities.
- A fully specified native signed-allocation transfer whose complete exponent budget beats $3/4$.
- An exact obstruction showing why a proposed transfer cannot preserve the native kernel, thereby preventing another circular route.
- A new joint inverse/plain moment theorem with enough quantified capacity to improve the imported endpoint.

The mathematically most valuable outcome would be the second or fourth. The import supplies the sources, explicit current obstruction, and reusable checks needed to attempt them.
