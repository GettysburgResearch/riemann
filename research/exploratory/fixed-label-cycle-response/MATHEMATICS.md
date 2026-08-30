# Fixed-label cycle lifts and the information lost by scalar determinants

Status: proposed exact theorem and synthetic structural countermodel.
Scope: finite directed colored sources, formal power series over C, and
finite matrix or permutation lifts. All infinite products below are formal.
Arithmetic class of the replay: EXACT_RATIONAL / EXACT_INTEGER.
External novelty: not established; standard graph-zeta and matrix algebra
are explicitly imported or reproved. No RH/GRH implication is claimed.

## 1. A source-defined parent and two of its shadows

A source is a finite vertex set with a finite list of directed edges. Every
edge has a color in a fixed finite alphabet. Parallel edges and loops are
permitted; there is no nonbacktracking restriction. Use the row-to-column
adjacency convention, and let A_i be the adjacency matrix for color i.

For commuting indeterminates x_i, define

    M(x) = sum_i x_i A_i,
    D_G(t,x) = det(I-t M(x)),    Z_G(t,x) = D_G(t,x)^(-1).

All determinants have constant term one, so their inverses are defined in
C[x][[t]]. The parent (the colored graph) precedes either scalar shadow.

**RSGLO.CYCLE.EULER_TRACE (classical, reproved).** If [p] runs over primitive
nonempty directed closed edge words, modulo cyclic rotation but not reversal,
and w(p) is the product of their commuting color weights, then

    Z_G(t,x) = exp(sum_{r>=1} tr(M(x)^r) t^r/r)
             = product_[p] (1-w(p)t^len(p))^(-1).

Indeed matrix multiplication enumerates rooted walks. Every rooted closed
word is a repetition of a unique primitive cyclic edge word. A primitive
word of length l contributes l rooted words at each repetition number k;
the exponential logarithm therefore gives w(p)^k t^(kl)/k. Summation over
k is -log(1-w(p)t^l). At every degree only finitely many walks contribute.
The determinant equality follows either from formal Jacobi differentiation
and the constant term, or from the formal trace-log identity. This proves
both the cycle Euler product and the determinant/trace law from one source.

For declared d by d matrices U_i, retain the same fixed copy C^d at every
vertex and define the matrix lift

    T_G(U) = sum_i A_i tensor U_i.

Its determinant is again defined before its zeros. The twisted primitive
cycle formula is

    det(I-t T_G(U))^(-1)
      = product_[p] det(I-t^len(p) U(p))^(-1),

where U(p) is the ordered product of its edge matrices. The proof is the
same walk expansion with tr(U(p)^k). A cyclic change of base point preserves
the factor since det(I-AB)=det(I-BA). No reordering of different labels is
allowed. When U_i are permutation matrices, T is the adjacency matrix of
the literal d-sheet lift with vertices (v,sheet). These are directed graph
covers; invertible edge labels give the required local bijections.

## 2. Every commutative scalar shadow misses reversal

Let G^op retain the vertices and colors but reverse every directed edge.
Its matrices are A_i^T.

**RSGLO.CYCLE.COMMUTATIVE_TRANSPOSE_BLINDNESS.** For every finite source,

    D_(G^op)(t,x) = D_G(t,x)

as a polynomial in all the commuting variables, not merely after x_i=1.
This is the identity det(B^T)=det(B). Equivalently the reversed cyclic word
has the same commutative weight. This statement concerns reversal, not a
claim that all graphs with equal scalar zeta are reversals.

If the finite matrices U_i commute pairwise, they are simultaneously upper
triangularizable over C. After ordering the tensor basis by sheet coordinate,
T_G(U) is block upper triangular with diagonal blocks sum_i lambda_(i,j) A_i.
For G^op the corresponding diagonal blocks are their transposes. Multiplying
their determinants proves

    det(I-t T_G(U)) = det(I-t T_(G^op)(U)).

This permits nonsemisimple commuting matrices. It does NOT say that every
cover with an abelian based-loop monodromy group is invisible: open-edge
label matrices can fail to commute in a chosen trivialization even when
the based-loop group is abelian.

## 3. The two-vertex, three-color source

Take vertices 0,1 and edges

    a:0->1,    b:1->0,    c:0->0.

The reversed source has a:1->0, b:0->1 and the same loop. Thus

    M_G(x,y,z)     = [[z,x],[y,0]],
    M_(G^op)(x,y,z)= [[z,y],[x,0]],
    D_G = D_(G^op) = 1-zt-xy t^2.

The two colored sources are not color-preservingly isomorphic: the unique
c-loop fixes vertex 0, after which the a-edge orientations disagree.
Their uncolored adjacency matrices at x=y=z=1 are actually identical.

For labels U,V,W on a,b,c, respectively, the lifted matrices are

    T = [[W,U],[V,0]],      T_op = [[W,V],[U,0]].

The block Schur complement, using the identity bottom-right block, gives

    det(I-tT)    = det(I-tW-t^2 UV),
    det(I-tT_op) = det(I-tW-t^2 VU).

This calculation takes place over C[t]; no division by t or by a singular
matrix is used. In particular tr(T)=tr(T_op), tr(T^2)=tr(T_op^2), and

    tr(T^3)-tr(T_op^3) = 3 tr(WUV-WVU).                 (3.1)

The factor three counts the three possible roots of the mixed length-three
cycle. These identities hold for arbitrary square label matrices of one size.

## 4. An exact positive response to noncommuting labels

**RSGLO.CYCLE.COMMUTATOR_ENERGY.** Let U,V be arbitrary unitary d by d
matrices and declare W=(UV)^*=V^*U^*. This is a fixed operation on the
labels, with no reference to a target spectrum. Then

    Re(tr(T^3)-tr(T_op^3)) = (3/2) ||UV-VU||_F^2.       (4.1)

The right side is nonnegative, and vanishes exactly when U and V commute.
In particular any noncommuting pair separates the two determinant inverses,
although every commutative scalar shadow of the sources agrees.

Proof. Put K=(UV)^*(VU)=V^*U^*VU. Equation (3.1) is 3(d-tr K). Since
UV and VU are both unitary,

    ||UV-VU||_F^2
      = tr((UV-VU)^*(UV-VU)) = 2d-2 Re tr K.

Substitution proves (4.1). The Frobenius norm is zero exactly for a zero
matrix. The equality of the first two traces and inequality of the third
imply different determinants: the first three coefficients of the formal
log determinant are -tr(T^r)/r. This is an exact finite-model positivity
identity, not an independently polarized arithmetic operator or RH theorem.

The energy is invariant under simultaneous conjugation of all labels by
one unitary. It compares the products UV and VU using the declared common
sheet-space identification. It is NOT claimed invariant under independent
vertexwise gauge changes. Such changes alter the numerical label assignment
and the fixed identification used for the reversed-source comparison.
The alignment condition itself is preserved: under gauges G_0,G_1,
U'=G_0^*UG_1, V'=G_1^*VG_0 and W'=G_0^*WG_0 still obey W'=(U'V')^*.
For example G_0=I,G_1=U^* gives U'=I,V'=UV and hence zero fixed-label
energy, even if the original energy was positive. The original lifted
determinant remains unchanged by that gauge; the fixed-label reversed
comparison does not. This is an explicit limit on the claimed observable.

**Corollary (label-group criterion).** For a subgroup H<=U(d), the fixed
graph pair is indistinguishable for every label triple in H if and only if
H is abelian. The forward implication applies (4.1) to arbitrary U,V in H
and W=(UV)^(-1) in H. The reverse implication is Section 2. This is a
criterion for the image of the edge-label group, not for a deck group.

## 5. Smallest permutation lift, and a different dimension threshold

For d=1,2 all permutation matrices commute. Section 2 shows that every
assignment of such matrices fails to distinguish G from G^op.

For d=3 choose U for (12), V for (23), and W=(UV)^(-1). Put R=UV;
R is a three-cycle and VU=R^(-1)=W. Then

    D_lift(t)    = det(I-tR^(-1)-t^2R) = 1-4t^3-t^6,
    D_lift_op(t) = det(I-(t+t^2)R^(-1)) = 1-(t+t^2)^3.

For the first equality, diagonalize the order-three permutation with
eigenvalues 1,omega,omega^2, or expand its three by three determinant.
The second equality is the characteristic identity of a three-cycle.
The length-three closed-walk counts are respectively 12 and 3.
Therefore permutation sheet degree three is both sufficient and minimal
for this graph pair. Both actual lifted graphs have six vertices.

The standard two-dimensional summand already sees the difference. The
common invariant constant sheet vector gives the shared base factor
1-t-t^2. Dividing yields

    D_standard    = 1+t+2t^2-t^3+t^4,
    D_standard_op = 1+t+2t^2+2t^3+t^4.

This is the ordinary decomposition of the permutation representation into
constants and sum-zero vectors. The principal scalar factor being unchanged
does not mean a signed sum-zero trace estimate controls it.

The threshold for general unitary labels is instead dimension two. Use

    U=[[0,1],[1,0]], V=[[1,0],[0,-1]], W=(UV)^T.

They are real orthogonal, UV=-VU, and

    D_lift=1+(t-t^2)^2,   D_lift_op=1+(t+t^2)^2.

The third-trace gap is 12. Dimension one cannot detect the pair because
scalars commute. Matrix-label dimension and permutation-cover degree are
different assertions; neither is an infinite-dimensional limitation.

## 6. A precise failure of reconstruction from the scalar shadow

**RSGLO.CYCLE.COVER_DOES_NOT_DESCEND.** For the fixed three-sheet assignment
in Section 5, there is no function f of the commutative determinant
polynomial alone such that, for every finite colored directed source H,

    det(I-t T_H(U,V,W)) = f(D_H(t,x,y,z)).

Proof: G and G^op have identical arguments of f and different required
outputs. This is a two-source contradiction, without regularity assumptions
on f. It also rules out determining the fixed-label operation from all
commuting scalar specializations of the determinant. It does not rule out
reconstruction from richer noncommutative word data, marked paths, or the
original graph. Nor does it exclude reconstruction on a restricted source
class that omits one member of this pair.

Thus a parent carrying a fixed-label lift operation contains information
that its whole commutative determinant family forgets. This gives a concrete
structural test for #763 and a non-scalar parent comparison for #764. It is
not a construction attached to the Riemann zeta function.

## 7. Natural transpose duality is not broken

For every complex label assignment,

    T_(G^op)(U_i^T) = T_G(U_i)^T.

Hence reversing the source AND transposing its labels preserves the
determinant exactly. With real permutation labels, transpose is inverse.
For complex unitary labels inverse is conjugate transpose; because the
source adjacency matrices are real,

    T_(G^op)(U_i^(-1)) = T_G(U_i)^*,
    D_dual(t) = conjugate(D_G(conjugate(t))).

The latter need not equal D_G(t). The packet separates fixed-label response
from these natural simultaneous dualities. It does not manufacture a
contradiction by silently holding one half of a duality fixed.

## 8. Replay and withheld tests

The bounded producer checks the source incidence, characteristic polynomials
by exact permutation expansion, independently multiplied matrix traces,
closed-walk counts by edge-list dynamic programming, and primitive-cycle
Euler products by direct cyclic-word enumeration. Equality of derived JSON
alone is not acceptance: the full fixture must equal source recomputation.

Controls include all assignments in S_1 and S_2, the predeclared S_3 witness,
all 36 ordered S_3 pairs with W=(UV)^(-1), and independently chosen S_4 pairs.
S_4 is withheld from the derivation: its predictions follow (4.1) without
retuning the parent. Orthogonal rational two-dimensional labels check the
dimension distinction. Wrong unitarity and wrong alignment are rejected as
outside the energy theorem, and the simultaneous transpose is a duality
control. Caps precede enumeration; no dense parameter scan or numerical
eigenvalue calculation occurs.

The manuscript proves the universal quantifiers. Finite fixtures do not
certify analytic continuation, all-graph spectral reconstruction, arithmetic
completion, novelty, or a number-field transfer. They do not define zeros
first and fit a matrix afterward.

## 9. Primary literature and the exact contribution claimed

Directed-cycle determinant formulas and cover factorizations are classical.
Mizuno and Sato, *Zeta functions of digraphs* (2001),
https://doi.org/10.1016/S0024-3795(01)00318-4, is a direct reference; the
publisher fetch was unavailable in this pass, so it is not used as an
unread load-bearing theorem. Sections 1 and 3 contain complete proofs here.

Foata and Zeilberger, *A Combinatorial Proof of Bass's Evaluations of the
Ihara-Selberg Zeta Function for Graphs*, https://arxiv.org/abs/math/9806037,
is a primary determinant/cycle baseline. Its undirected Ihara conventions
must not be substituted for the directed convention of this packet.

Storm, *Some graph properties determined by edge zeta functions*,
https://arxiv.org/abs/0708.1923, already demonstrates information in richer
graph-zeta variables that a scalar specialization can lose. Its abstract
was read. The general slogan that a richer parent has more information is
not claimed new here; our pair agrees in ALL commuting color variables.

Matsuura and Ohta, *Graph Zeta Functions and Wilson Loops in Kazakov-Migdal
Model*, https://arxiv.org/abs/2208.14032, treats matrix-weighted graph zetas
and Wilson loops. Its abstract was read. Matrix edge weights are not a new
ontology invented by this packet.

The programme contribution claimed is the explicit fixed-label pair, the
all-size commutator-energy identity, sharp sheet/dimension thresholds,
and the precise no-descent statement with its duality and gauge limits.
No external priority claim is made for this combination. A specialist
novelty review remains a separate step. The two-source obstruction is
self-contained even if its precise packaging has appeared before.
