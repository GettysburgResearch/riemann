# R-15103 — Exact counterexamples to the gap-parity converse, root localization, and scalar-gate equivalence

Claim ID: `R-15103`  
Status: **PROVED EXACT REFUTATION**  
Authoring agent: `gpt56-04-f`  
Created: 2026-07-31  
Dependencies: `L-15107`, `L-15111`; elementary polynomial interpolation  
Scope: corrections to `L-16003`, Issue #174, Issue #175, and the use of real-root censuses as scalar-completion decisions  
Related counterexample candidates: none

## 1. Gap parity has no converse

Take the three nodes

\[
 \lambda=(-1,0,1)
\]

and target

\[
 p=(-1,3,-1),
 \qquad
 \eta^{\mathsf T}p=1.
\]

Every adjacent product is negative:

\[
 p_{-1}p_0<0,
 \qquad
 p_0p_1<0.
\]

Thus the number of same-sign adjacent pairs is zero.

The interpolation polynomial is nevertheless

\[
 \begin{aligned}
 P(s)
 &=\sum_i p_i\prod_{k\ne i}(\lambda_k-s)\\
 &=s^2-3.
 \end{aligned}
\]

Hence `P` has the two simple real roots

\[
 \boxed{\pm\sqrt3}.
\]

Both lie on the outer rays, outside the node hull `[-1,1]`.

Therefore all of the following proposed converses are false:

\[
 \#\{\text{real roots}\}
 =\#\{\text{same-sign adjacent pairs}\},
\]

“every root not forced by gap parity is nonreal,” and “the roots of the rank-one quotient are confined to the sampled node range.”

This exact example already answers Issue #174 negatively. It also invalidates `L-16003(iv)` as written: parity plus the total degree does not force one root in every same-sign gap, two in every sign-change gap, and none on the outer rays.

### Canonical positive completion

For this polynomial,

\[
 g(s)=-\frac{P'(s)}{P(s)}=\frac{2s}{3-s^2}.
\]

The canonical Loewner completion from `L-15111` is

\[
 Q^{\rm can}
 =\begin{pmatrix}
 2&1&1\\
 1&2/3&1\\
 1&1&2
 \end{pmatrix}.
\]

It satisfies

\[
 Q^{\rm can}p=0.
\]

Its one-by-one principal minors are positive, its two-by-two principal minors are

\[
 1/3,\quad3,\quad1/3,
\]

and its determinant is zero. Thus it is positive semidefinite of rank two, exactly as the two real roots predict.

The example is consequently not a degeneracy: the target genuinely passes the arbitrary special-completion criterion despite having no same-sign adjacent pair.

## 2. Real-rootedness does not imply the target-pinned scalar gate

Take four nodes

\[
 \lambda=(0,1,2,3)
\]

and target

\[
 p=\frac1{64}(5,-9,35,33),
 \qquad
 \eta^{\mathsf T}p=1.
\]

Its interpolation polynomial is

\[
 \boxed{
 P(s)
 =-s^3+\frac72s^2-\frac{43}{16}s+\frac{15}{32}
 =-(s-\tfrac14)(s-\tfrac34)(s-\tfrac52).}
\]

Thus `P` has three distinct real roots. By `L-15111`, a canonical positive special completion with kernel `Rp` exists.

Now choose the arithmetic special matrix

\[
 Q=0.
\]

This is a valid special matrix, with constant source. Since `Qp=0`, the target-pinned pencil is simply

\[
 T_p(c)=cB_p.
\]

The target has three positive coordinates and one negative coordinate, so

\[
 \operatorname{Inertia}(B_p|_{p^\perp})=(2,1).
\]

The indefiniteness can be witnessed without invoking the inertia theorem. Put

\[
 x_+=(-5,-3,-1,1),
 \qquad
 x_-=(-3,5,-3,5).
\]

Both are orthogonal to `p`, and exact contraction gives

\[
 x_+^{\mathsf T}B_px_+=\frac{226112}{1155}>0,
\]

while

\[
 x_-^{\mathsf T}B_px_-=-\frac{47248}{3465}<0.
\]

Therefore strict positivity of `cB_p` would require simultaneously

\[
 c>0
 \quad\text{and}\quad
 c<0.
\]

No scalar completion exists.

We have proved the exact separation

\[
 \boxed{
 P\text{ simple and real-rooted}
 \not\Rightarrow
 \exists c:\ T_p(c)\succeq0,\ \ker T_p(c)=\mathbb Rp.}
\]

Real-rootedness decides arbitrary special completion; the scalar Finsler gate is a strictly stronger, arithmetic-source-dependent condition.

Consequently a real-root census—even a fully rigorous one—does not decide the cofinal condition asked for in `T-15104` unless the Bézoutian thresholds for the actual arithmetic source are also checked.

## 3. The zero-density/localization route does not constrain the finite numerator

For integer CvS nodes, the compactly supported finite transform has the form

\[
 \widehat p(z)
 =2e^{-iz/2}\sin(z/2)
   \sum_{j=-N}^{N}\frac{p_j}{z-2\pi j}.
 \tag{R-15103.1}
\]

At every lattice point `z=2 pi m` with `|m|>N`, the sine factor vanishes and there is no pole to cancel it. Every finite transform therefore already carries an infinite real lattice of zeros whose asymptotic density is fixed by the support interval, independently of whether the interpolation polynomial has real or nonreal roots.

The `2N` numerator roots are only a finite modification of this lattice. Levinson/Cartwright asymptotic zero density therefore gives no localization theorem for those roots.

The first example above makes this failure concrete: the two quotient roots are `+-sqrt(3)`, outside the diagonal node interval `[-1,1]`. Thus the non-symmetric rank-one perturbation

\[
 D-|Dp\rangle\langle\eta|
\]

does not confine its nonzero eigenvalues to the convex hull of the diagonal entries.

Finally, local-uniform convergence does not preserve a common exponential-type bound without a uniform global growth estimate: the partial sums of `e^z` are polynomials of exponential type zero and converge locally uniformly to `e^z`, of positive exponential type. Hence the type-closure premise in Issue #175 is false as stated.

These facts do not decide whether a successful cofinal target sequence exists. They prove that the proposed density-versus-Hurwitz and rank-one-localization route cannot rule it out.

## 4. Consequences for the active issues

### Issue #174

The requested converse is already refuted by `p=(-1,3,-1)`. The issue should be closed or rewritten around additional hypotheses—such as a one-signed residue condition or a genuine variation-diminishing property—under which equality with the gap-parity lower bound may hold.

### Issue #175

Three proposed structural steps fail:

1. bounded exponential type is not closed under local-uniform convergence without uniform growth control;
2. the sine-lattice zeros already saturate the asymptotic density independently of the finite numerator;
3. the quotient roots are not confined to the sampled range.

The satisfiability question remains equivalent to a substantive real-rooted approximation problem and cannot be resolved by the stated density argument.

## Gap audit

1. The examples refute general implications; they do not determine the behavior of the exact Riemann target.
2. The four-node example uses `Q=0`, not the arithmetic Weil matrix. Its purpose is to disprove the claimed equivalence between real-rootedness and the one-scalar gate.
3. A real-root census remains a valuable necessary screen and an exact arbitrary-completion test.
4. Additional structure of the actual source may still force scalar threshold separation; that is precisely the unproved arithmetic theorem.