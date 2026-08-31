# Coordinate-permutation representations in the native curvature source

This proof-only note concerns the permutation action on the three
independent schedule variables. Its group \(S_3\) is not being identified
with the Galois group of a separate arithmetic cover. The curvature is
the actual native polynomial curvature, with the original factor two.

The input kernel calculation is
NATIVE_TRANSPOSE_AND_PRIMITIVE_CONSTRAINTS.md at
059d54f23b39b692c23f375338d9ad443b56b74f, blob
990f0f1e25fddced653b16b651bc5f2cdd02b7e2. The finite-horizon scope check
also uses SOURCE_CURVATURE_HORIZON_FILTRATION.md at
2952d7c0c9fd0fbbbf04fa6321cc2ff4bb392c8a, blob
e6489149479e68ee20bd042c4f03bab58e3e48bf, and the bounded physical-rank
certificate at a4d610431d5edaf26b00bae903bb9111837e4c31
(native_horizon_rank_certificate.json, blob
5e1e3471e9428b339d652440b04cda829673b54d).

No numerical acquisition or new execution is needed for the representation
calculation below.

## 1. An equivariant source quotient

Work over \(\mathbb R\), or any characteristic-zero field. Put
\[
 V=\operatorname{span}\{1,u,v,w,uv,uw,vw,uvw\},\qquad
 W=\operatorname{im}\mathcal K,\qquad
 \mathcal K(f\wedge g)=2\,df\wedge dg .
\]
For \(\sigma\in S_3\), define \(\rho(\sigma)u_i=u_{\sigma(i)}\) and
\(\rho(\sigma)du_i=du_{\sigma(i)}\), and extend to polynomials and
differential forms. Exterior differentiation commutes with this action,
so \(\mathcal K\) is equivariant. These are continuous polynomial
variables; no relation \(u_i^2=u_i\) is imposed.

The native squarefree-index coefficients are nonzero scalar multiples of
all eight monomials. Thus this is an action on the actual curvature
carrier, rather than a representation assigned only to its dimension.
The frozen source calculation gives the exact sequence
\[
 0\longrightarrow K\longrightarrow\Lambda^2V
       \overset{\mathcal K}{\longrightarrow}W\longrightarrow0,
 \qquad
 K=(1\wedge\bar V)\oplus\mathbb Rq,                         \tag{1.1}
\]
where
\[
 \bar V=\operatorname{span}\{u,v,w,uv,uw,vw,uvw\},\qquad
 q=u\wedge vw+v\wedge uw+w\wedge uv .
\]
The seven-dimensional summand is invariant, and \(q\) is fixed: a
coordinate permutation simply permutes its three displayed summands.
Consequently \(K\cong\bar V\oplus\mathbf1\cong V\) as ungraded
\(S_3\)-modules. This is not a grading-preserving identification:
the extra invariant \(q\) has total differential degree three.

## 2. The exact irreducible decomposition

Use class order identity, transposition, three-cycle. A fixed monomial
corresponds to a subset which is a union of permutation cycles, hence
\(\chi_V=(8,4,2)\). For a linear operator \(g\), diagonalizing over
\(\mathbb C\) gives
\[
 \operatorname{tr}(\Lambda^2g)
       =\frac{\operatorname{tr}(g)^2-\operatorname{tr}(g^2)}2.
\]
Additivity of trace in (1.1) therefore gives the following complete table.

| Module | Identity | Transposition | Three-cycle |
| --- | ---: | ---: | ---: |
| \(V\) | 8 | 4 | 2 |
| \(\Lambda^2V\) | 28 | 4 | 1 |
| \(K\) | 8 | 4 | 2 |
| \(W\) | 20 | 0 | \(-1\) |

The three irreducible real characters are
\((1,1,1)\), \((1,-1,1)\), and \((2,0,-1)\).
Taking character inner products with class sizes \(1,3,2\) gives
\[
 \boxed{W\cong3\,\mathbf1\oplus3\,\operatorname{sgn}
                       \oplus7\,\operatorname{Std}.}       \tag{2.1}
\]
The isotypic dimensions are \(3,3,14\). In the same convention
\(V\cong4\,\mathbf1\oplus2\,\operatorname{Std}\) and
\(\Lambda^2V\cong7\,\mathbf1\oplus3\,\operatorname{sgn}
\oplus9\,\operatorname{Std}\).

There is a finer source grading. Give \(u_i\) and \(du_i\) multidegree
\(e_i\). The following sums of multidegree spaces are \(S_3\)-stable.

| Multidegree orbit | Dimension | Module |
| --- | ---: | --- |
| permutations of \(110\) | 3 | \(\operatorname{sgn}\oplus\operatorname{Std}\) |
| permutations of \(210\) | 6 | \(\mathbf1\oplus\operatorname{sgn}\oplus2\operatorname{Std}\) |
| \(111\) | 2 | \(\operatorname{Std}\) |
| permutations of \(211\) | 6 | \(\mathbf1\oplus\operatorname{sgn}\oplus2\operatorname{Std}\) |
| permutations of \(221\) | 3 | \(\mathbf1\oplus\operatorname{Std}\) |

Here the \(110\) piece is the exterior square of the three-dimensional
permutation module. The six distinct \(210\) degrees form a free
permutation orbit. At \(111\), the three variable/complement wedges form
a permutation module with the invariant line \(q\) removed. At \(211\),
the stabilizing transposition acts on the two-dimensional component with
eigenvalues \(1,-1\): representatives \(u\wedge uvw\) and \(uv\wedge uw\)
show this at degree \(211\). Inducing that regular \(S_2\)-module gives
the regular \(S_3\)-module. At \(221\), its stabilizer fixes the one
curvature line, giving the three-dimensional permutation module.

In total differential degree, the corresponding trace polynomials are
\[
 \begin{array}{c|c}
 1&3t^2+8t^3+6t^4+3t^5\\
 (12)&-t^2+t^5\\
 (123)&-t^3 .
 \end{array}                                               \tag{2.2}
\]
This polynomial grading is not the arithmetic product-horizon cutoff.

## 3. Source-defined central projectors

Let
\[
 S=\rho((12))+\rho((13))+\rho((23)),\qquad
 C=\rho((123))+\rho((132)).
\]
On \(W\) define
\[
 P_{\mathbf1}=\frac{I+S+C}{6},\qquad
 P_{\rm sgn}=\frac{I-S+C}{6},\qquad
 P_{\rm Std}=\frac{2I-C}{3}.                                \tag{3.1}
\]
They are central elements of the actual permutation group algebra.
The group multiplication rules, or their values on the three
irreducible characters, give
\(P_i^2=P_i\), \(P_iP_j=0\) for \(i\ne j\), and \(\sum P_i=I\).
Their ranks on \(W\) are \(3,3,14\), respectively. They preserve total
polynomial degree and commute with the curvature quotient map from
\(\Lambda^2V\).

Thus the isotypic splitting is specified by the source action itself.
An individual choice of the three trivial, three sign, or seven standard
copies is not specified by these central projectors. Nor does algebraic
orthogonality \(P_iP_j=0\) assert orthogonality for the physical norm.

## 4. The original fixed-prime observation is a separate structure

The formal coordinate action can relabel an actual schedule path.
However, at fixed primes \(2,3,5\), the prime weights, frequency ratios,
and product-horizon cutoff are still attached to their original labels.
Source equivariance does not by itself intertwine this observation.

There is an exact finite-horizon obstruction, not just an absence of a
proof. The frozen filtration states
\[
 W_H=\bigoplus_{2^{d_1}3^{d_2}5^{d_3}\le H}W_d.
\]
At \(H=25\), the nonzero degree \(201\) component is present, at cost
\(20\), whereas its image under the coordinate swap \(u\leftrightarrow w\)
has degree \(102\) and cost \(50\), so is absent. Hence \(W_{25}\) is not
\(S_3\)-invariant.

The independent bounded rank certificate gives physical rank six at
this horizon, equal to \(\dim W_{25}\). Physical ratio rows lie in
\(W_{25}\), so they span it. On the twenty-dimensional variation space
\(W^*\), the physical observation therefore has kernel
\(W_{25}^{\perp}\), meaning its algebraic annihilator. This kernel is
not invariant under the dual \(S_3\)-action. Distinct frequencies are
independent on any interval where the original observation density is
positive, so this statement also concerns the original Hilbert norm,
with all ratio aliases retained.

In fact each of the three central projectors fails at this horizon.
Take \(0\ne\omega\in W_{201}\). Its six permutation images have six
distinct multidegrees, because the coordinates of \(201\) are distinct.
Both \(P_{\mathbf1}\omega\) and \(P_{\rm sgn}\omega\) have a nonzero
\(W_{102}\) component, with coefficient \(1/6\) or \(-1/6\) times the
image under \(u\leftrightarrow w\). There is no other term of that
degree to cancel it. The two three-cycle images have degrees \(120\)
and \(012\); therefore \(P_{\rm Std}\omega\) has a nonzero \(W_{012}\)
component with coefficient \(-1/3\). Its cost is \(75>25\).
None of the three projectors preserves \(W_{25}\).

For precision, let \(P_i^\vee\) act on the variation space \(W^*\)
by precomposition with \(P_i\). The annihilator
\(L=W_{25}^{\perp}\) is invariant under \(P_i^\vee\) if and only if
\(W_{25}\) is invariant under \(P_i\). This follows directly by pairing,
or by taking annihilators twice in finite dimension. Thus none of the
three dual projectors preserves the actual physical observation kernel.
Choose an \(S_3\)-invariant reference inner product on \(W^*\), for
example by averaging, and let \(G_{25}\) be the pulled-back physical
Gram operator in that reference metric. If \(G_{25}\) commuted with
\(P_i^\vee\), its kernel \(L\) would be \(P_i^\vee\)-invariant.
Consequently
\[
               [G_{25},P_i^\vee]\ne0
       \quad(i=\mathbf1,\operatorname{sgn},\operatorname{Std}). \tag{4.1}
\]
The algebraic central projectors are self-adjoint for the chosen
invariant reference metric, so this also rules out an orthogonal
physical splitting by any of these projected summands at \(H=25\).
It rules out the full group symmetry there as well.

This statement uses the Gram form on \(W^*\), not an identification
of curvature forms with current coordinates. It does not prove
noncommutation at infinity or at every other horizon. No such
physical conclusion is inferred from the character table alone.

## 5. Isotypic projection is not automatically a path operation

Individual coordinate permutations preserve the class of monotone
paths, but linear combinations of their currents need not be currents
of one path. This distinction already appears in the full matrix
carrier from the transpose theorem:
\[
 M_{a,b}(\gamma)=2\int_\gamma f_b\,df_a,\qquad
 M_{0,a}=0,\quad M_{a,0}=2\quad(a\ne0).                     \tag{5.1}
\]
Simultaneous permutation of its two indices is the source group action.
The right-unit column in (5.1) is invariant. Its projection to either
the sign or standard isotypic part is zero. Consequently either such
projection of the full current matrix violates (5.1) and cannot itself
be the literal current of an admissible path.

The invariant average retains these necessary endpoint constraints;
no assertion that it is always, or never, realizable by one path is
made. The projectors on the curvature quotient \(W\), and their duals
on linear variations, likewise do not supply an admissible nonlinear
operation on paths without an additional construction.

These are representations of polynomial differential forms and their
source quotient. They are not Boolean Walsh projectors, Wick sectors,
an inertia character table for another source, or a new normalization
of the primitive observation.

## 6. An exact one-form quotient in every number of coordinates

There is a stronger source description for any \(r\ge1\). Let \(V_r\)
be the span of squarefree monomials and define the finite-dimensional
one-form space
\[
 B_r=\bigoplus_{i=1}^r
  \operatorname{span}\!\left\{
       \prod_{j\ne i}u_j^{a_j}\,du_i:
                     a_j\in\{0,1,2\}\right\}.             \tag{6.1}
\]
Thus a coefficient of \(du_i\) is independent of \(u_i\), and has
degree at most two in every other variable. This is a vector space
of polynomial forms, not the unrestricted polynomial one-form module.
The source map
\[
 \Psi:\Lambda^2V_r\longrightarrow B_r,\qquad
                \Psi(f\wedge g)=f\,dg-g\,df              \tag{6.2}
\]
is well-defined and surjective, and \(d\Psi=\mathcal K\).

Here is a proof of surjectivity rather than a dimension comparison.
In multidegree \(d\in\{0,1,2\}^r\), the one-form basis is
\(u^{d-e_i}du_i\) for the indices with \(d_i=1\).
For squarefree \(a+b=d\), the coefficients of
\(\Psi(u^a\wedge u^b)\) in this basis are \(b_i-a_i\).
They run through every sign vector with entries \(1,-1\) on those
indices; all other coefficients vanish. These sign vectors span the
coordinate space over a characteristic-zero field. If there are no
such indices, the one-form component is zero. This proves (6.2).
In particular \(dB_r=\operatorname{im}\mathcal K=W_r\).

The resulting equivariant sequence is exact:
\[
 \boxed{\displaystyle
 0\longrightarrow V_r/\mathbb R
       \overset d\longrightarrow B_r
       \overset d\longrightarrow W_r\longrightarrow0.}   \tag{6.3}
\]
Only exactness in the middle remains to check. Write a closed form as
\(\omega=\sum_i b_i(u)\,du_i\in B_r\). Its polynomial potential
\[
 F(u)=\int_0^1\sum_i u_i b_i(tu)\,dt
\]
satisfies \(dF=\omega\): closedness gives
\[
 \partial_jF
 =\int_0^1\left[b_j(tu)+t\sum_i u_i\partial_i b_j(tu)\right]dt
 =b_j(u).
\]
Since \(b_i\) is independent of \(u_i\), every
\(\partial_i^2F\) vanishes. A characteristic-zero polynomial with
this property is multilinear, so \(F\in V_r\). Conversely \(dV_r\)
is visibly contained in \(B_r\) and closed, and only constants have
zero differential. This proves (6.3). The integral notation is simply
termwise division of polynomial coefficients by positive integers,
so the proof works over every characteristic-zero field.

Thus \(W_r\cong B_r/dV_r\) is a specified one-form quotient by actual
polynomial potentials. This does not provide a projection on paths.
For \(r=3\), \(\dim B_3=27\), and (6.2) has the single invariant
relation
\[
                  \ker\Psi=\mathbb R(q-1\wedge uvw).       \tag{6.4}
\]
Indeed both \(q\) and \(1\wedge uvw\) map to \(d(uvw)\), and
surjectivity gives kernel dimension \(28-27=1\).
This refines, and is consistent with, the eight-dimensional kernel
of the subsequent curvature map.

Let \(c(\sigma)\) be the number of cycles of \(\sigma\in S_r\) and
\(f(\sigma)\) its number of fixed coordinates. The character of \(V_r\)
is \(2^{c(\sigma)}\). To contribute to the trace on the monomial
one-form basis of \(B_r\), the differential index must be fixed.
For each such index the exponents must be constant on the remaining
cycles, with three choices per cycle. Hence
\[
 \chi_{B_r}(\sigma)=f(\sigma)3^{c(\sigma)-1}.
\]
Taking characters in (6.3) proves
\[
 \boxed{\chi_{W_r}(\sigma)
      =f(\sigma)3^{c(\sigma)-1}-2^{c(\sigma)}+1.}            \tag{6.5}
\]
In particular \(\dim W_r=r3^{r-1}-2^r+1\).
The original exterior-square sequence also determines the exact
curvature-kernel character:
\[
 \chi_{K_r}(\sigma)
 =\frac{2^{2c(\sigma)}-2^{c(\sigma^2)}}2-\chi_{W_r}(\sigma).
                                                                    \tag{6.6}
\]
For \(r=3\) this recovers (2.1); for \(r=4\) the curvature kernel has
dimension \(120-93=27\), so \(K\cong V\) is not promoted to general \(r\).

The same exact sequence is multigraded. At degree \(d\), put
\(E_d=\operatorname{span}\{e_i:d_i=1\}\). Exterior differentiation is
the coefficient map \(v\mapsto d\wedge v\), up to an overall sign,
and therefore
\[
                W_d\cong E_d/(E_d\cap\mathbb R d).         \tag{6.7}
\]
The intersection is zero when some \(d_i=2\), and is the line
\(\mathbb R d\) for a nonzero degree having only zeros and ones.
This also recovers the frozen multidegree dimensions and explains
why coordinate permutations preserve their total-degree sums.

All steps are permutation-functorial source linear algebra. The
irreducible-character and central-idempotent methods are classical;
the inputs being decomposed here are the specified native curvature
map, its exact kernel, and its actual polynomial grading. No larger
linear-change-of-variables symmetry or physical projector is asserted.
