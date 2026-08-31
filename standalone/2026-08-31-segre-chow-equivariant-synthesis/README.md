# Proof-oriented synthesis of Riemann PRs #766, #769, and #781

**Repository:** `gfreund123/riemann`  
**Status:** proposed theorem synthesis; independent mathematical review required before integration or claim promotion.  
**Publication scope:** the initial analysis pass was read-only. This branch adds only this standalone packet; it does not modify the three source PRs, their claims, code, or exact atlases.  
**PR heads checked on 2026-08-31:**

- PR #766: `17c7624a0bd56c5356d00278b2a846d2efdbdccc`
- PR #769: `f36576faf7853a56bd1f64edd29c4df662cae849`
- PR #781: `ea282c4e73ecd2d8cad44587da5ffa135df67e98`

**Analytic status:** RH and GRH remain unproved. Nothing in this packet proves or materially advances either conjecture.

**Review target:** verify Theorem I's change-of-rings and duality bookkeeping, Theorem II's cycle-index reconstruction, Theorem III's uniqueness/Hessian-dual identification, the four-arity transferred model, and the degree-six split/master-class argument. The packet distinguishes imported classical inputs from the proposed new synthesis and records the exact points where stronger formulations fail.

## Packet map

### Core synthesis

- [Theorem I — master Segre–Chow cofactor, canonical Tor strands, change of rings, and duality](THEOREM_I.md)
- [Theorem II — cycle-index alternants and the full tensor-factor character](THEOREM_II.md)
- [Theorem III — canonical top syzygy and Hessian-dual identification](THEOREM_III.md)
- [Imported inputs, proposed new content, corrected statements, and ranked continuation](SCOPE_AND_CONTINUATION.md)

### Chain-level and derived continuation

- [First nonzero ternary Segre–Chow transgression](CHAIN_LEVEL_TERNARY_TRANSGRESSION.md)
- [Finite transferred Koszul model and non-formality theorem](TRANSFERRED_KOSZUL_MODEL.md)
- [Internal degree six: first nonlinear closure problem](INTERNAL_DEGREE_SIX_CLOSURE.md)
- [All-cycle Frobenius alternant](FROBENIUS_CYCLE_INDEX_ALTERNANT.md)
- [All-depth stable correction head](STABLE_LAYER_HEAD_THEOREM.md)
- [Canonical top projection protocol](CANONICAL_TOP_PROJECTION.md)
- [Current continuation results and ranked next target](CONTINUATION_RESULTS.md)
- [Focused validation and review ledger](VALIDATION.md)

The current algebraic endgame is no longer “compare two numerators.” The completed Chow homology transfers to

\[
\left(\Lambda C\otimes B,\Delta_1+\Delta_2+\Delta_3+\Delta_4\right),
\]

and internal degree six contains eleven of the twelve support-allowed higher operations. Its only possible homology is

\[
K_{4,2}\quad\text{and}\quad K_{5,1},
\]

with

\[
\dim K_{5,1}-\dim K_{4,2}=61370,
\qquad
\dim K_{4,2}\ge1000.
\]

Determining those two modules, not another Euler characteristic, is the highest-priority closure target.

---

## 0. Notation and the four objects that must not be conflated

Let \(k\) be a characteristic-zero field, let \(\dim V=d\), and let \(m\ge 2\). Put

\[
E:=V^{\otimes m},\qquad W:=\operatorname{Sym}^mV\subset E,
\qquad C:=E/W,
\]

where \(W\hookrightarrow E\) is the canonical symmetrization summand. Put

\[
S_E:=\operatorname{Sym}(E),\qquad S_W:=\operatorname{Sym}(W),
\]

and

\[
R=R_{d,m}:=\bigoplus_{r\ge0}(\operatorname{Sym}^rV)^{\otimes m}.
\]

The full tensor space \(E=R_1\) generates \(R\) as an algebra, so \(R\) is a quotient of \(S_E\). The smaller symmetric summand \(W\subset R_1\) does not generally generate \(R\), but \(R\) is finite over \(S_W\).

For \(A\in GL(V)\), write

\[
F_{d,m}(A,T)=\sum_{r\ge0}
\operatorname{Tr}\!\left(A\mid\operatorname{Sym}^rV\right)^mT^r.
\]

There are two different equivariant \(K\)-polynomials:

\[
K_R^E(A,T):=\det(1-TA\mid E)\,F_{d,m}(A,T),
\]

the **ambient Segre \(K\)-polynomial over \(S_E\)**, and

\[
K_R^W(A,T):=\det(1-TA\mid W)\,F_{d,m}(A,T),
\]

the **Chow/recurrence-base \(K\)-polynomial over \(S_W\)**. The latter is exactly the universal recurrence numerator

\[
N_{m,d}(A,T)=K_R^W(A,T).
\]

Thus the base-independent phrase “the \(K\)-polynomial of \(R\)” is unsafe here. The base must be specified.

---

# 1. Precise audit of what is already proved

## 1.1 PR #766

Principal files read:

- `research/l-families/atlas/generalized/SEGRE_RECURRENCE_SYZYGY_BRIDGE.md`
- `research/l-families/atlas/generalized/SIXHOUR_PASS3_RESULTS.md`
- the independent audit `SEGRE_RECURRENCE_SYZYGY_BRIDGE_AUDIT_4A317EA5.md`

The branch proves, with the stated exact-computation and review boundaries:

1. The ambient Hilbert numerator is the additive equivariant Tor Euler characteristic over \(S_E\):
   \[
   K_R^E=\sum_{i,j}(-1)^i
   \operatorname{ch}\operatorname{Tor}^{S_E}_i(R,k)_j\,T^j.
   \]

2. The universal recurrence denominator is
   \[
   D_W(A,T)=\det(1-TA\mid\operatorname{Sym}^mV),
   \]
   and
   \[
   N_{m,d}=D_WF_{d,m}.
   \]

3. In characteristic zero, the symmetric summand splits from \(E\), and
   \[
   K_R^E(A,T)=N_{m,d}(A,T)\det(1-TA\mid C).
   \]
   This scalar/character cofactor identity is already proved.

4. Generic partial fractions, specialization through pole collisions, exact degree
   \[
   \deg_TN_{m,d}=\dim(\operatorname{Sym}^mV)-d,
   \]
   the top coefficient, reciprocity with \(A^{-1}\), cancellation strata, and the reduced Hankel-rank statement are proved.

5. A finite-superdeterminant interpretation of \(N_{m,d}\) from natural representation actions is refuted in the exhibited cases: at \(A=I\), such determinant products would be cyclotomic, while the relevant numerators have non-cyclotomic roots.

6. In rank three/power three the branch computes an actual low-degree **ambient** Segre syzygy character over the 27-variable base \(S_E\), and gives examples where the recurrence denominator collapses while the ambient syzygy module does not. This is an exact warning against reading a reduced numerator spectrum as an actual syzygy action.

Not proved there:

- a uniform description of the canonical Tor strands over the smaller base \(S_W\);
- a termwise relationship between the ambient and Chow-base Tor modules;
- degeneration of a change-of-rings spectral sequence;
- a finite superdeterminant formula for \(N_{m,d}\);
- any RH/GRH conclusion.

## 1.2 PR #769

Principal files read:

- `research/l-families/atlas/generalized/segre-hadamard-source/COMPLETED_TERNARY_CUBE_RESOLUTION.md`
- `research/l-families/atlas/generalized/SIX_HOUR_GRADED_SOURCE_PROGRESS.md`
- `TERNARY_CUBE_TOR_CHARACTERS.md`
- `tor_characters.verification.json`
- `REVIEW_47890a7a.md`

Here \(d=m=3\), \(W=\operatorname{Sym}^3V\), and the polynomial base is the ten-variable ring \(S_W\), not the 27-variable ambient tensor ring.

The branch proves an exact minimal resolution

\[
0\to F_3\to F_2\to F_1\to F_0\to R\to0
\]

with degree lists

\[
\begin{aligned}
F_0&=S\oplus S(-1)^{17}\oplus S(-2)^{11},\\
F_1&=S(-2)^{20}\oplus S(-3)^{65},\\
F_2&=S(-4)^{65}\oplus S(-5)^{20},\\
F_3&=S(-5)^{11}\oplus S(-6)^{17}\oplus S(-7).
\end{aligned}
\]

It also proves the complete \(GL_3\times S_3\) Tor table. Writing \([abc]\) for the Schur module \(S_{(a,b,c)}V\), and \(\mathbf 1,\varepsilon,\sigma\) for the trivial, sign, and standard representations of the tensor-factor \(S_3\), the nonzero terms are

\[
\begin{array}{c|c|l}
i&j&B_{i,j}\\ \hline
0&0&[000]\otimes\mathbf1\\
0&1&[210]\otimes\sigma+[111]\otimes\varepsilon\\
0&2&[222]\otimes\mathbf1+[330]\otimes\varepsilon\\
1&2&[411]\otimes\sigma\\
1&3&[522]\otimes(\mathbf1+\sigma)+([531]+[432])\otimes\varepsilon\\
2&4&[552]\otimes(\mathbf1+\sigma)+([642]+[543])\otimes\varepsilon\\
2&5&[663]\otimes\sigma\\
3&5&[555]\otimes\mathbf1+[744]\otimes\varepsilon\\
3&6&[765]\otimes\sigma+[666]\otimes\varepsilon\\
3&7&[777]\otimes\mathbf1.
\end{array}
\]

The resolution is self-dual:

\[
B_{3-i,\,7-j}\cong
B_{i,j}^{\vee}\otimes(\det V)^7.
\]

Its alternating character is exactly

\[
N_{3,3}(A,T)=
\det(1-TA\mid\operatorname{Sym}^3V)
\sum_{r\ge0}\operatorname{Tr}(A\mid\operatorname{Sym}^rV)^3T^r.
\]

At \(A=I\), this is

\[
1+17T-9T^2-65T^3+65T^4+9T^5-17T^6-T^7.
\]

The branch also supplies an actual 379-term integral degree-seven relation, proves that its class is nonzero in the one-dimensional top Tor quotient, and completes the explicit minimal resolution.

Important retained limitation: the chosen 379-term marked lift is not claimed to be a preferred \(GL_3\)-equivariant lift. Its quotient class is canonical; its literal coordinate representative need not be.

## 1.3 PR #781

Principal files read:

- `claims/theorems/T-108515-segre-defect-bridge.md`
- `claims/theorems/T-108522-alternant-defect-closed-form.md`
- `claims/observations/O-108523-torsion-multiplicity-law.md`
- `claims/lemmas/L-108524-multiplicity-transversality.md`
- the two associated standalone proof packets;
- exact JSON atlases for alternants, stable layers, rank-three Betti data, torsion multiplicities, and branch slopes.

What is proved:

1. For \(d=2\) and all \(m\), the ambient Segre \(K\)-polynomial factors as the defect numerator times explicit ballot/plethysm excess determinants.

2. The \(d=2,m=3\) ambient Segre Betti table over \(S_E\) is computed exactly. This is a different resolution from PR #769.

3. For \(m=2\) and all \(d\),
   \[
   K_R^E=N_{2,d}\det(1-TA\mid\Lambda^2V).
   \]

4. T-108522 proves an explicit divided-difference/alternant expression for \(N_{2,d}\), and a general multilinear partial-fraction formula that yields every \(N_{m,d}\).

5. Stable square-defect correction layers at depths \(3,4,5,6\) are established in the branch's exact-symbolic sense. The tempting linear rule valid at depths \(3,4\) is **refuted** at depth \(5\), and remains refuted at depth \(6\). The shifted leading-part pattern at depths \(5,6\) remains an observation, not an all-depth theorem.

What is not proved:

1. O-108523 is an observation: the odd-\(m\) torsion multiplicity formula fits all 96 recorded exact cells.

2. L-108524 proves the interior contribution only under explicit separation and transversality hypotheses, certified in seven cells. It does not remove those hypotheses globally.

3. The even-\(m\) correction, including fixed and boundary classes and square-root branching at \(z=\pm2\), is open.

4. No RH/GRH conclusion is present.

---