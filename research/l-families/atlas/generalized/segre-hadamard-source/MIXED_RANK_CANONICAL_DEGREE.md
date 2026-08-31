# Mixed-rank Chow bases, canonical characters, and a degree loss without pole collision

Status: proposed exact source sequel; no new run is claimed here.
All vector spaces have characteristic zero. This note applies classical
Segre/Chow and canonical-module constructions to the grouped pointwise-power
source. Its new repository comparison is the leading canonical character and
the distinction between its vanishing, pole collisions, and Betti changes.
It is not a priority claim for Segre Cohen--Macaulayness.

## 1. Grouped source and the polynomial base

Fix groups `g=1,...,k`, dimensions `d_g>=2`, and multiplicities `m_g>=1`.
Let `V_g` have dimension `d_g`. Set

    R_r = tensor_g (Sym^r V_g)^{tensor m_g},
    W   = tensor_g Sym^{m_g} V_g,
    S'  = Sym(W),
    s_g = binom(d_g+m_g-1,m_g),        s=product_g s_g,
    D   = 1+sum_g m_g(d_g-1),          c=s-D,
    M   = max_g d_g.                                      (1.1)

Within each group, include symmetric tensors by their orbit sums, then tensor
these inclusions to obtain `W -> R_1`. This defines the multiplication of the
`S'`-module, equivariantly for `product_g GL(V_g)` and the within-group factor
permutations. The scalar series is

    F(A_1,...,A_k;T)=sum_r product_g h_r(A_g)^{m_g} T^r,
    Q=det(1-T tensor_g Sym^{m_g} A_g),     N=QF.            (1.2)

The equal-rank single-group construction is classical; see
[Raicu--Sam--Weyman, Proposition 2.7](https://arxiv.org/abs/2108.10910).
For the grouped version, the same basepoint argument works without further
homological assumptions. A geometric tuple determines one nonzero product
of linear forms in each group, and their tensor product is nonzero. Hence
the linear system `W` has no basepoint on the product of projective spaces.
Graded Nakayama gives finiteness of `R` over `S'`. It is a module supported on
the product of Chow varieties followed by a Segre embedding; `S' -> R` is
not generally surjective or injective.

The diagonal section ring is Cohen--Macaulay. Indeed for `O(r,...,r)` on
this product of positive-dimensional projective spaces, negative `r` gives
either zero cohomology or only the top degree, and nonnegative `r` gives only
degree zero. Kunneth supplies the intermediate-cohomology vanishing. Thus
`pdim_{S'} R=c`, and `N` is the alternating character of the actual finite
`Tor^{S'}` spaces. This remains an additive K-polynomial, not a multiplicative
finite determinant construction.

## 2. The leading canonical character

**Theorem SHM1.** The universal numerator has degree at most `s-M`. Its
coefficient in degree `s-M` is

    (-1)^c product_g (det A_g)^{m_g(s/d_g-1)}
                    h_{M-d_g}(A_g^{-1})^{m_g}.            (2.1)

Every displayed determinant exponent is an integer. The coefficient is
nonzero generically, so the generic degree deficit `deg Q-deg N` is `M`.
Unlike the equal-rank case, the leading character can vanish at an invertible
specialization. This vanishing does not remove the underlying top Tor space.

**Proof.** The canonical module has graded components

    (omega_R)_r = tensor_g
       (Sym^{r-d_g} V_g tensor det V_g)^{tensor m_g},      (2.2)

where a symmetric power of negative degree is zero. Its first nonzero degree
is `M`. Its lowest graded piece is therefore an actual representation, not a
scalar recovered from a recurrence. The determinant of the polynomial base is

    det W = product_g (det V_g)^{m_g s/d_g}.              (2.3)

For each group, `m_g s_g/d_g` is the determinant exponent of
`Sym^{m_g} V_g`; multiplying by the other dimensions proves integrality.

Apply `Hom_{S'}(-,S'(-s) tensor det W)` to a minimal resolution. By
Cohen--Macaulay duality the only cohomology is `omega_R` in degree `c`.
Minimality identifies the top-degree terminal Tor space with

    Tor_c^{S'}(R,k)_{s-M} = (omega_R)_M^* tensor det W.    (2.4)

There are no terminal terms in larger degree. Equivalently the regularity is
`D-M`, so no term anywhere in the resolution has internal degree exceeding
`c+(D-M)=s-M`. Taking (2.4)'s trace, with the Euler sign `(-1)^c`, proves
(2.1). The lowest canonical piece is nonzero at identity, establishing the
generic degree assertion. QED.

When factor-permutation actions are retained, the canonical module additionally
has the product of the signs `sgn_{m_g}^{d_g-1}`. Formula (2.1) evaluates only
the diagonal `GL(V_g)` action, so no such sign is suppressed in its claimed
domain. The formula is compatible with the maximum-rank degree-deficit law in
[T-108510](https://github.com/gfreund123/riemann/blob/ac1cc5eaf229087b6d805e908897c7c8c99a58b7/claims/theorems/T-108510-defect-codimension-law.md),
but provides the actual leading representation and its exceptional zero locus.

**Corollary SHM2.** The Segre ring `R` is Gorenstein if and only if all the
dimensions `d_g` agree. If they agree, (2.2) is one shifted copy of `R` with
a determinant twist. If they do not, its least-degree piece has dimension

    product_g binom(M-1,d_g-1)^{m_g} > 1.                 (2.5)

It cannot then be a cyclic canonical module. There is consequently no
unconditional same-source Gorenstein palindrome in mixed unequal ranks.
This concerns the ring's canonical module; it is not a claim that the last
`S'`-resolution term has only one grading degree or that all Betti numbers
can be recovered from `N`.

## 3. Two preregistered mixed comparisons

The following predictions are declared before this sequel's first execution.
They are exact consequences of (2.1), tested against independently formed
source character coefficients and tensor-symmetric weights.

### Two binary copies and one ternary copy

Use `(d_1,m_1)=(2,2)`, `(d_2,m_2)=(3,1)`. Then

    (s,D,c,M,deg N)=(9,5,4,3,6),
    [T^6]N=(det A)^5(det B)^2(tr A)^2.                   (3.1)

The leading Tor space has dimension four at identity. On the deformation
`A=diag(1,t)`, its character has a double zero at `t=-1`. It remains a
four-dimensional source representation at that value.

For `A=diag(1,-1)`, put `D_B(T)=det(1-TB)`. The complete symmetric trace of
`A` is one in even degree and zero in odd degree. Thus, directly from the
source,

    F = (1+e_2(B)T^2)/(D_B(T)D_B(-T)),
    Q = D_B(T)^2 D_B(-T),
    N = D_B(T)(1+e_2(B)T^2).                            (3.2)

Here the scalar numerator generically drops to degree five, and a denominator
collision also occurs. Those are separate statements. The replay uses
`A=(2,3), B=(5,7,11)` for the generic comparison and `(1,-1)` for (3.2).

### One binary copy and two ternary copies

Use `(d_1,m_1)=(2,1)`, `(d_2,m_2)=(3,2)`. This is the multiplicity-reversed
heldout for this sequel, with the same generic diagonal entries. Then

    (s,D,c,M,deg N)=(12,6,6,3,9),
    [T^9]N=(det A)^4(det B)^6 tr A.                      (3.3)

At `A=diag(1,-1)` the source series is the even part of the ternary square
series. The numerator must be even and its degree-nine term is zero. The
bounded replay records its actual degree instead of inferring all lower
coefficients from (3.3). The original source module is unchanged.

## 4. A degree loss with eight distinct poles and no cancellation

**Theorem SHM3.** Let

    A = [[0,-1],[1,1]],
    B = diag(b_1,b_2,b_3,b_4),

where the `b_i` are pairwise distinct positive real numbers. Use one copy of
each space, so `W=V_2 tensor V_4`. Then

    Q(T)=product_i(1-b_i T+b_i^2 T^2),
    N(T)=1-e_2(B)T^2+e_3(B)T^3.                         (4.1)

The denominator has eight distinct roots, is the minimal recurrence
denominator, and is coprime to `N`. Nonetheless `deg N=3` rather than the
generic value four: the degree deficit has increased from four to five.

**Proof.** The characteristic polynomial of `A` is `X^2-X+1`. Therefore
`h_0(A)=h_1(A)=1`, `h_2(A)=0`, and the recurrence is
`h_r=h_{r-1}-h_{r-2}`. The general source theorem gives degree at most four;
its degree-four coefficient from (2.1) is

    -det(A) det(B) h_2(A)=0.                             (4.2)

The first four coefficients obtained from this source recurrence and the
product defining `Q` give (4.1). This is an all-degree identity because the
already proved degree bound leaves no further coefficients to determine.
The cubic coefficient is nonzero since `e_3(B)>0`.

Write the two eigenvalues of `A` as `alpha,beta`; their ratio is a nonreal
primitive cube root of unity. The eight products `alpha b_i,beta b_i` are
distinct because the `b_i` are positive and pairwise distinct. Each of the
two exponential coefficients in the complete-symmetric sequence of `A`
is nonzero. The same holds for all four exponential coefficients of the
complete-symmetric sequence of `B`. Their products are the eight nonzero
coefficients in `h_r(A)h_r(B)`. Linear independence of distinct exponential
sequences proves that all eight poles survive; hence `Q` is minimal and
`gcd(Q,N)=1`. QED.

The replay uses `B=diag(5,7,11,13)`, forms `h_r(A)` by the integer recurrence,
forms `h_r(B)` independently by multiplication of geometric series, and
checks the exact polynomial identity and rational polynomial gcd. No
approximate roots or numerical pole classifications are used.

This example prevents a false inference in either direction: a leading
K-character can vanish without a pole collision, and its vanishing does not
mean the canonical top Tor space has disappeared. It also shows why a
generic degree-deficit statement must retain its generic qualifier.

## 5. Boundaries

The finite source and its canonical module remain the parents throughout.
Specializing matrices changes their traces. A change in those traces is not
a change in the module's Betti table or a proof of a new operator realization.
The grouped base also retains the compatibility constraint from the first
packet: independent operators within one symmetric group must be proportional
to preserve that canonical symmetric subspace. Independent actions between
the declared groups are allowed.

No finite superdeterminant, global arithmetic continuation, or ramified
fixed-generator replacement is asserted. The explicit positive-real condition
in SHM3 is used to keep its eight products distinct; removing it requires
rechecking pole collisions. All bounded checks are parent-serialized, and
no execution result is claimed before the companion record is written.
