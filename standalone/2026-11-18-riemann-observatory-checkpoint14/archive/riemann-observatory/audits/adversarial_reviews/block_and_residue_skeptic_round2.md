# Independent checks: discrete blocks and grouped residues

Reviewer: li_advocate. Date:2026-11-17. Reconstructed from statements sent by equivalences, before reading its proof files. No novelty or arithmetic summability is claimed.

## Discrete multicluster block bound

Let there be p groups of sizes m_a≤q, total m, residual degree L≥m, local offsets |ν|≤R, and basis φ_(a,j)(x)=exp(iμ_a x)h_(a,j)(x), with the normalized confluent divided-difference h from the fixed-cluster theorem. Let δ_* be a valid common lower bound for the continuous local Grams and D_*=max_a2m_a(R+m_a), so L≥2D_*/δ_* gives each empirical diagonal Gram eigenvalue at leastδ_*/2.

For different groups, put z=exp(i(μ_a−μ_b)/L) and f_k=h_(a,j)(k/L)overline(h_(b,l)(k/L)). Then |f_k|≤1 and total variation ∑|f_k−f_(k−1)|≤2(q−1+R). The exact Abel identity

(1−z)∑_(k=0)^L z^k f_k=f_0−z^(L+1)f_L+∑_(k=1)^L z^k(f_k−f_(k−1))

therefore bounds each normalized cross entry by2(q+R)/σ_L, where

σ_L=min_(a≠b)(L+1)|1−exp(i(μ_a−μ_b)/L)|.

The operator norm of the whole off-diagonal-block perturbation is at most ε_L=2m(q+R)/σ_L, by the entrywise row-sum bound. If ε_L≤δ_*/4, the full Gram has eigenvalue at leastδ_*/4. Its inverse differs from the block-diagonal inverse by at most8ε_L/δ_*², using inverse norms4/δ_* and2/δ_*.

The interpolation target has one unit coordinate per group, hence squared norm p. The minimum-norm formula, including the common factor1/(L+1), gives

|L E_total−∑_a L E_(a,local)|≤8pε_L/δ_*².

The local problem must use the same residual degree L, so its quotient degree is≤L−m_a. Reusing the same quotient degree N for every local problem would be an indexing error and is not the statement checked here.

Positive definiteness also excludes hidden phase aliases and literal crossgroup collisions: either would make the union of sampled local value/jet rows dependent. Within-group exact repeats are represented by the confluent basis. The bound is thus compatible with actual polynomial multiplicities under the stated conditioning hypotheses.

If every center difference has absolute value≤πL and S=min_(a≠b)|μ_a−μ_b|, then |sin x|≥2|x|/π for |x|≤π/2 yields σ_L≥2S/π. This restriction is material: an ordinary large separation near2πL can give a tiny phase gap and does not ensure decoupling. The resulting joint error has the form O(1/L+1/σ_L), or O(1/L+1/S) under this no-wrap restriction, with parameters of the local theorem held fixed. Classification: constants and scope independently checked with no issue found.

## Local grouped-residue/divided-difference identity

Let U be convex, exclude the ζ pole1, contain a finite multiset C of zeros of ζ counted with full local multiplicities, and contain no other zeros. Put q_C(z)=∏_(ρ∈C)(z−ρ) and g_C(z)=ζ(z)/q_C(z). Then g_C is analytic and nonvanishing on U. Let N>1, s∉U and

F(z)=N^(z−s)/[(z−s)²g_C(z)].

The local sum of residues of N^(z−s)/[(z−s)²ζ(z)] at C equals the confluent divided difference DD_C F, of order m−1 for m=|C|. This follows directly from the contour formula for divided differences, including repeated nodes. There is no missing factorial in this equality. For complex nodes, Hermite–Genocchi along their convex hull gives

|DD_C F|≤sup_(conv C)|F^(m−1)|/(m−1)!.

If the closed r-neighborhood of the hull is compactly contained in U, Cauchy's estimate supplies |F^(m−1)|/(m−1)!≤sup_neighborhood|F|/r^(m−1). If d=dist(s,neighborhood)>0, M=sup_neighborhood|1/g_C| and b=max_neighborhood Re(z−s), this gives

|DD_C F|≤N^b M/[d²r^(m−1)].

The factorial from Cauchy's derivative estimate cancels the Hermite–Genocchi factorial. The neighborhood and distance hypotheses are essential; 's outside U' together with compact containment guarantees positive d. For m=1 the r power is0 and the identity reduces to an ordinary simple-zero residue. For m>1 it handles all local principal parts automatically. No uniform bound on M as clusters move, no summation over infinitely many clusters, and no global ζ contour argument follow from this local identity. Classification: independently checked classical identity specialization, with no issue in inspected constants or domains.
