> Part of the [PR #766/#769/#781 proof-oriented synthesis packet](README.md).

# 5. Classical imported inputs versus potentially new synthesis

## Classical/imported

1. Finiteness of the full Segre ring over the Chow coordinate ring and the normalization description.

2. Cohen–Macaulayness of the modules of covariants over the Chow ambient polynomial ring, the projective-dimension formula, and canonical-module duality.

3. The ternary-cubic invariant-sector resolution, its Hessian component, skew middle map, and self-duality.

4. Koszul complexes, equivariant Hilbert-series Euler characteristics, change-of-rings spectral sequences, Schur–Weyl duality, character orthogonality, and standard tensor-cycle trace identities.

5. [Snowden's finite-master-syzygy theorem](https://arxiv.org/abs/1006.5248) for fixed ambient homological degree, and the Lascoux/[Netay](https://arxiv.org/abs/1108.3733) descriptions for the two-factor ambient Segre problem.

## New or new-in-repository synthesis proved here

External novelty is not asserted without a dedicated literature audit.

1. The all-\((d,m)\) repository dictionary
   \[
   N_{m,d}=K_R^{S_W}
   \]
   together with the explicit canonical Chow-Koszul strands and the change-of-rings spectral sequence linking them to ambient Segre Tor.

2. The representation-valued top-coefficient lift
   \[
   B_{c,N-d}
   =
   \det(\operatorname{Sym}^mV)(\det V)^{-m}
   \otimes\operatorname{sgn}^{d-1},
   \]
   and its exact match with PR #766's scalar top coefficient.

3. The cycle-index alternant theorem reconstructing the full
   \(GL(V)\times S_m\) alternating Tor character from twisted Hadamard alternants.

4. The exact term-by-term rank-three/power-three reconciliation in the representation ring, plus the no-go theorem showing why the ordinary alternant alone cannot recover \(S_3\)-types.

5. The precise canonical interpretation of the PR #769 top relation as a Hessian-dual map, together with the correction separating its canonical quotient class from its particular 379-term marked lift.

---

# 6. Corrected statements and counterexamples

1. **False:** \(N_{m,d}\) should be a determinant or superdeterminant of a naturally inferred finite representation because its reciprocal specialization factors into quadratics.  
   **Correct:** \(N_{m,d}\) is an additive alternating Tor character over \(S_W\). PR #766's cyclotomic-at-identity obstruction rules out the proposed natural finite determinant interpretation in explicit cases.

2. **False:** the ambient Segre Tor table and the Chow-base Tor table are the same resolution.  
   **Correct:** they are resolutions over \(S_E\) and \(S_W\), connected by the spectral sequence in Theorem I.

3. **False:** the ordinary alternant determines the \(S_m\)-isotypic structure.  
   **Correct:** it determines only the identity class trace. Twisted cycle-index alternants are required.

4. **False:** the 379-term top vector is automatically the unique equivariant top differential.  
   **Correct:** its quotient class is canonical; the vector can differ from the unique equivariant lift by an old relation.

5. **False:** the stable linear correction-layer law continues for all depths.  
   **Correct:** PR #781 refutes it at depth \(5\) and again at depth \(6\).

6. **Unproved:** the full odd-\(m\) torsion multiplicity law without separation/transversality, and the even-\(m\) correction. The exact atlas is strong evidence, not a general theorem.

---

# 7. Ranked continuation list

## 1. Highest priority: implement and review the cycle-index alternant theorem

For each conjugacy class of \(S_m\), produce the exact twisted numerator

\[
D_W\sum_r\prod_{c}h_r(A^{|c|})T^r
\]

from the existing multilinear alternant engine, then invert the \(S_m\) character table. For \(m=3\), verify symbolically that it reproduces every \(GL_3\times S_3\) row in PR #769, not only dimensions or sampled class traces. This is finite, theorem-driven, and directly checks Theorem II.

## 2. Canonicalize the 379-term top map

Apply the \(S_3\)-invariant and \(SL_3\)-isotypic projector to the marked degree-seven kernel, remove the old subspace, primitively normalize, and compare the resulting column with the dual Hessian coefficient map. This determines whether the existing 379-term column is already canonical or differs by an explicit old relation.

## 3. Compute the first Chow-base strands uniformly

Use the complexes

\[
\Lambda^\bullet(\operatorname{Sym}^mV)
\otimes(\operatorname{Sym}^{j-\bullet}V)^{\otimes m}
\]

to derive closed Schur formulas for \(B_{0,j}\) and \(B_{1,j}\) for the first fixed internal degrees, separating stable from small-rank exceptions. Snowden's ambient \(\Delta\)-module results should be treated as comparison data, not silently transferred across the change-of-rings spectral sequence.

## 4. Analyze degeneration/nondegeneration of the spectral sequence

Find the first \((d,m)\) where a higher differential is forced by comparing ambient and Chow-base Tor characters. A nondegeneration theorem in a stable range would be major; an explicit nonzero differential would also be valuable and would block naive tensor-product strand formulas.

## 5. Stable correction layers

Rewrite the square-defect alternant in a plethystic-logarithm or partition-lattice basis and prove or refute the observed shifted head for all \(j\ge5\). The already-refuted linear law must not be revived.

## 6. Torsion multiplicities

Replace cellwise separation by an equivariant discriminant/intersection calculation on the quotient of residue classes by \(c\mapsto-c\). First solve the odd-\(m\) boundary-free case globally; then add the fixed classes and ramification at \(z=\pm2\) for even \(m\).

---

# 8. Bottom line

The strongest synthesis is algebraic rather than analytic:

\[
\boxed{
\text{recurrence numerator}
=
\text{Chow-base Tor Euler character}
}
\]

and

\[
\boxed{
\text{ambient Segre Tor}
\quad\text{is linked to it by a change-of-rings spectral sequence.}
}
\]

The alternant computes the identity class trace of that Euler character. Cycle-index alternants recover the full tensor-factor representation. In the ternary cube, the top one-dimensional class is canonically the Gorenstein dual of the Hessian component; the 379-term relation is a valid marked lift of that class, but literal canonicality still requires projection and comparison.

No automorphy, analytic continuation, RH, or GRH conclusion follows.
