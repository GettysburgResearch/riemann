> Part of the [PR #766/#769/#781 proof-oriented synthesis packet](README.md).

# 5. Classical imported inputs versus potentially new synthesis

## Classical/imported

1. Finiteness of the full Segre ring over the Chow coordinate ring and the normalization description.

2. Cohen–Macaulayness of the modules of covariants over the Chow ambient polynomial ring, the projective-dimension formula, and canonical-module duality.

3. The ternary-cubic invariant-sector resolution, its Hessian component, skew middle map, and self-duality.

4. Koszul complexes, equivariant Hilbert-series Euler characteristics, change-of-rings spectral sequences, Schur–Weyl duality, character orthogonality, standard tensor-cycle trace identities, equivariant contractions, and the homological perturbation lemma.

5. [Rubei's property-\(N_p\) theorem](https://arxiv.org/abs/math/0404417) for Segre products with at least three nontrivial factors: property \(N_p\) holds exactly for \(p\le3\).

6. [Oeding--Raicu--Sam](https://arxiv.org/abs/1708.03803) on sharp Segre syzygy nonvanishing, including the first quadratic-strand class \(K_{4,2}\), and split functoriality under enlarging the factor spaces.

7. [Snowden's finite-master-syzygy theorem](https://arxiv.org/abs/1006.5248) for fixed ambient homological degree, and the Lascoux/[Netay](https://arxiv.org/abs/1108.3733) descriptions for the two-factor ambient Segre problem.

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

5. The exact source-bound rank-65 transgression
   \[
   d^2_{2,1,4}:E^2_{2,1,4}\twoheadrightarrow B_{2,4},
   \]
   proving nondegeneration at \(E^2\) and killing the complete first nonlinear Chow strand.

6. The finite transferred model
   \[
   \left(\Lambda C\otimes B,
   \Delta_1+\Delta_2+\Delta_3+\Delta_4\right)
   \]
   together with the exact classification of six ordinary action slots and twelve support-allowed higher operations.

7. A noncomputational proof that the Chow Koszul complex is not formal as a derived \(S_C\)-module. Geometry forces the disappearance of \(B_{2,4}\); the exact replay identifies the responsible page-two source.

8. The degree-six representation identity
   \[
   [K_{4,2}]-[K_{5,1}]=\mathscr D_6,
   \qquad
   \dim K_{5,1}-\dim K_{4,2}=61370,
   \]
   and the split-functorial master embedding
   \[
   S_{(3,3)}V_1\boxtimes S_{(3,3)}V_2\boxtimes S_{(3,3)}V_3
   \hookrightarrow K_{4,2},
   \]
   which gives \(\dim K_{4,2}\ge1000\) and \(\dim K_{5,1}\ge62370\) in rank three.

9. The precise canonical interpretation of the PR #769 top relation as a Hessian-dual map, together with the correction separating its canonical quotient class from its particular 379-term marked lift.

---

# 6. Corrected statements and counterexamples

1. **False:** \(N_{m,d}\) should be a determinant or superdeterminant of a naturally inferred finite representation because its reciprocal specialization factors into quadratics.  
   **Correct:** \(N_{m,d}\) is an additive alternating Tor character over \(S_W\). PR #766's cyclotomic-at-identity obstruction rules out the proposed natural finite determinant interpretation in explicit cases.

2. **False:** the ambient Segre Tor table and the Chow-base Tor table are the same resolution.  
   **Correct:** they are resolutions over \(S_E\) and \(S_W\), connected by a genuinely nondegenerate spectral sequence.

3. **False:** after the Chow homology is known, ambient Tor is termwise \(\Lambda C\otimes B\).  
   **Correct:** the differential transfers to four arities. At least one higher operation is forced, and the first source-bound \(d^2\) is nonzero and surjective.

4. **False:** the individual transferred maps \(\delta_r\) are canonical matrices.  
   **Correct:** their filtered gauge class and induced spectral-sequence differentials are canonical; literal representatives depend on the chosen contraction.

5. **False:** the coefficient \(-61370\) of the ambient numerator is the negative dimension of one degree-six syzygy module.  
   **Correct:** it is
   \[
   \dim K_{4,2}-\dim K_{5,1},
   \]
   and both modules are nonzero in the rank-three ternary case.

6. **Unproved:** the 1000-dimensional master submodule is all of \(K_{4,2}\). The packet proves an embedding and lower bound, not equality or the full character.

7. **False:** the ordinary alternant determines the \(S_m\)-isotypic structure.  
   **Correct:** it determines only the identity class trace. Twisted cycle-index alternants are required.

8. **False:** the 379-term top vector is automatically the unique equivariant top differential.  
   **Correct:** its quotient class is canonical; the vector can differ from the unique equivariant lift by an old relation.

9. **False:** the stable linear correction-layer law continues for all depths.  
   **Correct:** PR #781 refutes the original law at depths \(5\) and \(6\); the corrected large-part head is period four and returns at depths \(7\) and \(8\).

10. **Unproved:** the full odd-\(m\) torsion multiplicity law without separation/transversality, and the even-\(m\) correction. The exact atlas is strong evidence, not a general theorem.

---

# 7. Ranked continuation list

## 1. Highest priority: split internal degree six

Decompose the four-term complex in `INTERNAL_DEGREE_SIX_CLOSURE.md` into \(GL_3\times S_3\) multiplicity spaces, determine its transferred differential, and compute the full characters

\[
K_{4,2}=\operatorname{Tor}^{S_E}_4(R,k)_6,
\qquad
K_{5,1}=\operatorname{Tor}^{S_E}_5(R,k)_6.
\]

This is the first degree where the Euler polynomial does not determine the actual modules, and it contains eleven of the twelve possible higher operations.

## 2. Replace the total rank-65 certificate by four irreducible nonvanishing proofs

The target is

\[
[552]\otimes\mathbf1
\oplus[552]\otimes\sigma
\oplus[642]\otimes\varepsilon
\oplus[543]\otimes\varepsilon.
\]

Construct one highest-weight cycle for each summand, evaluate the \(d^2\) zig-zag, and prove the four resulting scalar pairings are nonzero. Schur's lemma then explains the full surjection representation by representation.

## 3. Prove cyclic/self-dual transfer before exploiting duality

Choose a contraction compatible with the Chow Gorenstein pairing, prove the resulting transferred model is cyclic or self-dual in the required graded sense, and only then use adjointness to relate opposite higher blocks. This should reduce the number of independent maps and control the sole higher slot first appearing in internal degree seven.

## 4. Canonicalize the 379-term top map

Add accepted marked \(\mathfrak{sl}_3\) and factor-permutation action matrices, apply the intrinsic projector, primitively normalize, and compare the result with the dual Hessian coefficient map.

## 5. Secondary algebraic programs

- Compute uniform low Chow-base strands from the functorial Chow-Koszul complexes.
- Extend the cycle-index reconstruction to \(m=4\).
- Determine the stable correction core where all elementary indices are at most the layer depth.
- Attack the remaining torsion-multiplicity boundary and transversality questions.

These remain worthwhile, but none should replace the central task of splitting \(K_{4,2}\) from \(K_{5,1}\).

---

# 8. Bottom line

The strongest synthesis is now derived rather than merely additive:

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
\operatorname{Tor}^{S_E}(R,k)
=H\!\left(\Lambda C\otimes B,
\Delta_1+\Delta_2+\Delta_3+\Delta_4\right).
}
\]

The completed Chow table supplies every homology strand \(B_{q,j}\). The rank-65 transgression proves that their derived gluing is nontrivial. Internal degree six is the first place where that gluing must be determined rather than hidden inside an Euler characteristic; it already contains all but one possible higher operation.

No automorphy, analytic continuation, RH, or GRH conclusion follows.