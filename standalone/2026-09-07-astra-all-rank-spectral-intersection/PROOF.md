# TSR26 — The full rational tensor/symmetric-power intersection at every rank

Status: PROPOSED COMPLETE COMPONENT PROOFS WITH AN EXACT FINITE TORSION
CLASSIFICATION; independent review pending. No RH, GRH, automorphy, or
compatible-family theorem is asserted. Date: 2026-09-07. Author: Astra.

The monomial theorem on PR #752 already identifies two universal graph loci.
The missing step was not a larger coefficient elimination: equality of FULL
spectra itself forces a monomial lift unless the target has finite order.
Rational raw traces then reduce every remaining rank to three tiny cyclotomic
alphabets. The rank dependence is handled exactly, not extrapolated from a
bounded sweep. We credit the preceding graph theorem and reproduce its short
proof where needed. No external priority claim is made.

## 1. Objects, normalization and main theorem

For a nonzero complex number u, Std(u) has eigenvalues u,u^(-1), and
Sym^r(v) has eigenvalues v^(r-2j), 0<=j<=r. Define the multisets

    T_r(u,v) = { u^epsilon v^(r-2j): epsilon=+1,-1, 0<=j<=r },
    S_r(w)   = { w^(2r+1-2k): 0<=k<=2r+1 }.                  (1)

Every multiplicity in (1) is retained. The question is equality of these
complete 2r+2-element multisets, not equality of one trace, a few moments,
or an unspecified coefficient prefix. We assume r is an integer >=1.

Write D_0(z)=2, D_1(z)=z, D_(n+1)(z)=zD_n(z)-D_(n-1)(z). Thus
D_n(w+w^(-1))=w^n+w^(-n). For normalized traces

    x=u+u^(-1), y=v+v^(-1), z=w+w^(-1),

the two graph loci, including the allowed central signs, are

    G1: x=sigma^r D_(r+1)(z), y=sigma z;
    G2: x=sigma^r z,          y=sigma (z^2-2), sigma in {+1,-1}. (2)

Independent inversion of u,v,w does not change their trace coordinates.
There are up to four signed graph curves, not literally two irreducible
curves after the central signs have been distinguished.

**TSR26.T2 (complete rational raw classification).** Let q>0 be rational,
choose its POSITIVE square root, and let A,B,C be arbitrary rational numbers.
No Hasse bound or finite-field realization hypothesis is needed. Put

    x=A/sqrt(q), y=B/sqrt(q), z=C/sqrt(q).

For the degree-two factor P_t(T)=1-tT+qT^2, form the tensor and symmetric-power
factors using their full eigenvalue multisets. Then

    P_(Std(A) tensor Sym^r(B))(q^(r/2) T)
        = P_(Sym^(2r+1)(C))(T)                              (3)

if and only if at least one of the graph conditions (2) holds, OR

    r == 3 (mod 4),       A=0,       B^2=C^2=2q.              (4)

The exceptional family (4) is disjoint from the graphs for those ranks.
It is possible over rational raw data exactly when 2q is a rational square.

The power q^(r/2) in (3) is compulsory. Before that dilation the tensor's
spectral weight is r+1 and the target's is 2r+1. With the positive square
root fixed, both sides of (3) have eigenvalues of common scale
q^((2r+1)/2), multiplied respectively by the multisets in (1). This proves
the equivalence between the raw question and (1). It also records the
square-root convention when r is odd.

The theorem concerns characteristic polynomials/semisimple spectra. It
neither compares nonsemisimple Jordan blocks nor constructs a homomorphism
between the full ambient representations.

## 2. The missing generic step: take one eigenvalue ratio

**TSR26.T1 (noncyclotomic rigidity and a torsion bound).** For any u,v,w in
C* and r>=1, if T_r(u,v)=S_r(w) and w is not a root of unity, then (2)
holds. More generally every nongraph solution has w a root of unity of order

    ord(w) <= (2r+1)(2r+2).                                 (5)

In particular all positive-dimensional components of the REDUCED trace
intersection lie on the signed graphs (2). There are no isolated
noncyclotomic solutions either. The statement does not classify scheme
multiplicities or list every cyclotomic residual over arbitrary complex data.

Proof. The two adjacent source eigenvalues uv^r and uv^(r-2) both occur in
the target, so for odd integers e0,e1 in [-(2r+1),2r+1],

    uv^r=w^e0,    uv^(r-2)=w^e1.

Dividing gives v^2=w^(e0-e1)=w^(2d), with d=(e0-e1)/2 an integer and
|d|<=2r+1. Therefore for some sigma=+1 or -1,

    v=sigma w^d,     u=sigma^r w^a,     a=e0-rd.             (6)

The central sign cancels in every tensor eigenvalue:

    u^epsilon v^(r-2j)=w^(epsilon a+d(r-2j)).

If w has infinite order, equality of the spectral multisets is exactly

    { +a+d(r-2j), -a+d(r-2j): 0<=j<=r }
       = {-(2r+1),-(2r-1),...,2r+1}.                       (7)

Independent sign changes in a,d preserve the left multiset. Neither is zero,
because that would repeat a weight whereas the target is multiplicity-free.
Taking the largest integer weight gives |a|+r|d|=2r+1. Thus |d| is 1 or 2,
and respectively |a| is r+1 or 1. This is the predecessor's maximum-weight
proof; substituting in (6) gives exactly (2).

Both families suffice for every w, torsion or not. For (a,d)=(r+1,1), the
two progressions are the positive and negative odd halves of the target.
For (a,d)=(1,2), they are its alternating-indexed progressions. Central
signs in (6) still cancel, and inversions preserve the multiset.

For the uniform bound (5), (6) also holds when w is torsion. Its integer
exponents obey

    |a|<= (r+1)(2r+1),
    |epsilon a+d(r-2j)| <= (2r+1)^2.

Choose a multiplicity-preserving matching with the target exponents. If all
matched exponent differences are zero as INTEGERS, (7) holds and the solution
is a graph solution. Otherwise a nonzero integer h satisfies w^h=1 and
|h|<=(2r+1)^2+(2r+1). Hence ord(w)<=|h|, proving (5).

Finally, (6) makes u,v take only finitely many values over any fixed torsion
w. The bounded set of exceptional orders in (5) therefore gives only finitely
many nongraph points for each fixed r. Passing through the finite trace map
preserves this finiteness. All positive-dimensional reduced components are
among the curves already exhibited in (2). No coefficient elimination,
Groebner basis or dimension inference from numerical samples is used.

## 3. Rational raw traces reduce torsion to four square classes

Suppose now that w is torsion and the raw hypotheses of T2 hold. Formula (6)
shows that u and v are torsion as well. If v is a root of unity and
Y=v+v^(-1) with Y^2 rational, then

    Y^2-2 = v^2+v^(-2)

is both rational and an algebraic integer. It is a real integer in [-2,2].
Consequently Y belongs to {0,+/-1,+/-sqrt(2),+/-sqrt(3),+/-2}.
Apply this to x,y,z, whose squares A^2/q,B^2/q,C^2/q are rational.
Since the raw traces themselves are rational, all three normalized traces
must lie in ONE of these four alphabets:

| square class of q in Q*/Q*^2 | allowed normalized traces |
|---|---|
| 1 | -2,-1,0,1,2 |
| 2 | -sqrt(2),0,sqrt(2) |
| 3 | -sqrt(3),0,sqrt(3) |
| any other positive class | 0 |

For example a nonzero sqrt(2) trace requires 2q to be a square, and a nonzero
sqrt(3) trace requires 3q to be a square. The three nonzero classes are
disjoint: 2,3,6 are not rational squares. The alphabets follow even without
a Hasse bound, since a torsion eigenvalue already has absolute value one.

All associated eigenvalues lie in the 24th roots of unity. With
zeta24=exp(2pi i/24), one may choose the following representatives (the inverse
representative gives the identical two-point eigenvalue multiset):

    square:  -2 ->12, -1 ->8, 0 ->6, 1 ->4, 2 ->0;
    class 2: -sqrt2 ->9, 0 ->6, sqrt2 ->3;
    class 3: -sqrt3 ->10,0 ->6, sqrt3 ->2;
    other:   0 ->6.                                         (8)

The integers in (8) are exponents of zeta24, not traces.

## 4. Complete torsion classification, with an all-rank proof contract

Two symmetries are useful in displaying the complete table:

    (x,y,z) -> (sigma^r x,sigma y,z),
    (x,y,z) -> (-x,y,-z).                                   (9)

The first leaves the tensor spectrum unchanged. The second multiplies both
spectra by -1, since the target degree of symmetry is odd. We can take z>=0,
y>=0; when z=0 we can also take x>=0. Entries not listed below do not solve
(1). Signs not fixed by this normalization are explicitly retained.

### Square class 1

- At z=2: (x,y)=(2,2) for every r.
- At z=0: (x,y)=(0,2) for every r; additionally (0,0) for even r and (2,0)
  for odd r.
- At z=1, y must be 1, and the allowed x values are:

| r mod 6 | 0 | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|---|
| x | 1 | -1 | -2 or 1 | -1 | 1 | -1 or 2 |

### Square class 2

- At z=0: only (x,y)=(0,0), and only for even r.
- At z=sqrt2 and y=0: x=sqrt2 for even r, and x=+/-sqrt2 for odd r.
- At z=sqrt2 and y=sqrt2: x=sqrt2 when r==0 or6(mod8), x=-sqrt2
  when r==2 or4(mod8), and x=0 for odd r.

### Square class 3

- At z=0: only (x,y)=(0,0), and only for even r.
- At z=sqrt3: y=sqrt3, r is even, and the allowed x is:

| r mod 12 | 0 | 2 | 4 | 6 | 8 | 10 |
|---|---|---|---|---|---|---|
| x | sqrt3 | 0 | -sqrt3 | -sqrt3 | 0 | sqrt3 |

### All other square classes

The only possible triple is (0,0,0), and it works precisely when r is even.

### Why checking the finite table proves every rank

We give a precise finite proof of completeness rather than testing many r and
assuming periodicity. For chosen exponents a,b,c from (8), define an integer
vector with coordinates h modulo24:

    F_r(h)=sum_(epsilon=+1,-1, j=0,...,r)
               1_(h == epsilon a+b(r-2j) mod24)
           -sum_(j=0,...,2r+1)1_(h == c(2r+1-2j) mod24).      (10)

Equality of the full spectra is equivalent to F_r=0. Write r=r0+24k with
1<=r0<=24 and k>=0. Increasing r by24 leaves the phases of the old terms
unchanged and adds24 terms to each source progression and48 to the target.
The respective steps are -2b and -2c modulo24, so each added block is a
whole number of cycles. Its residue counts are unchanged on the next
increase by24. Hence exactly

    F_(r0+24k)=F_r0+k Delta_r0,
    Delta_r0=F_(r0+24)-F_r0.                                (11)

The full table can therefore be checked by finite INTEGER arithmetic:
for each of the 125+27+27+1 triples and each r0=1,...,24, solve the vector
equation F_r0+k Delta_r0=0 for all integers k>=0. If Delta=0, either all
k work or none do. Otherwise one nonzero coordinate prescribes the only
possible rational k; check its integrality, sign and every other coordinate.
This procedure does not impose a cutoff on k.

The supplied standard-library checker executes all 4320 such affine rows.
It compares their complete solution sets, not merely r0, with the displayed
table. Every admitted row has F_r0=Delta_r0=0; there are no isolated positive
k solutions. As a compact audit, the following counts include all signs:

| r mod 6 | square class 1 | class 2 | class 3 | other |
|---|---:|---:|---:|---:|
| 1 | 12 | 8 | 0 | 0 |
| 2 | 15 | 7 | 5 | 1 |
| 3 | 12 | 8 | 0 | 0 |
| 4 | 11 | 7 | 5 | 1 |
| 5 | 16 | 8 | 0 | 0 |
| 0 | 11 | 7 | 5 | 1 |

The class2 count is 8 at every odd rank and7 at every even rank, regardless
of the displayed modulus6; this parity interpretation is part of the table.
All counts are small finite proof data, not finite-field or curve counts.

A direct way to verify the table by hand is to count the progressions in
(10) after each full root cycle. For instance at z=1, y=0 or2 cannot reproduce
the target's three odd residue classes. At y=1 the six possible rank residues
give the square-class-one row above. Formula (11) is a complete common
verification method for every table row, including exceptional low ranks.

## 5. Identify exactly the two graphs and the extra family

For a torsion target, D_n(z)=2cos(n theta) in the corresponding small cycle.
Substituting those values in (2) reproduces every entry of the table except

    x=0, y=+/-sqrt2, z=+/-sqrt2, r ==3 (mod4).                (12)

Indeed in square class2 the row x=0,y=z=sqrt2 works at every odd r. It
belongs to G1 exactly when D_(r+1)(sqrt2)=0, equivalently r==1(mod4).
G2 has y=0 at z=sqrt2 and so cannot produce (12). All other table entries
are the stated graphs. The exact checker separately computes the Dickson
polynomials in Z[sqrt2] and Z[sqrt3], rather than substituting floating
cosines, and verifies this comparison at every affine row. The graph
conditions and (12) are periodic modulo24 on these alphabets, so (11)
proves it for every r. Returning to raw traces gives (4), completing T2.

For r=4k+3, the additional family really works: take a primitive eighth root
w, v=w or its sign/inverse, and u=i. The target odd exponents give each odd
eighth root with multiplicity2k+2. The two tensor progressions have exactly
those same multiplicities. Their normalized factor is (1+T^4)^((r+1)/2).
Consequently the raw common factor is

    (1+q^(4r+2) T^4)^((r+1)/2).                             (13)

For example q=2,r=3,A=0,B=C=2 gives (1+2^14 T^4)^2. It is a nongraph
point for the rational raw problem, not a counterexample to an odd-prime
statement. The full eighth-root multiplicities are used, not just a vanishing
first trace.

## 6. A global obstruction: the torus graphs cannot extend through SL2

The classification is not a positive global transfer. It also gives a useful
negative one, which can be proved without assuming a square-root Tate character.

**TSR26.T3 (nonabelian monodromy obstruction).** Let G be a reductive algebraic
group over an algebraically closed characteristic-zero field. Let U,V,W be
rational two-dimensional representations with common determinant character d.
Assume the image of G^0 under W contains SL2. For any r>=1 there is NO
Zariski-dense subset of G on which the typed local spectral identity (3) holds,
with q replaced by d(g) and a choice of square root made pointwise.

Proof. Squaring all eigenvalues in the asserted local equality removes the
square-root choice and gives the regular-function identity

    tr(Sym^(2r+1) W(g^2))
        = d(g)^r tr(U(g^2)) tr(Sym^r V(g^2)).                 (14)

A dense set would make (14) hold on all of G. The derived Lie algebra of G^0
is a direct sum of simple factors. Since its image through W is sl2, one
simple factor maps isomorphically onto sl2. Pull back through the simply
connected SL2 covering of that factor. On this SL2, W is the standard
representation and d is trivial. Each two-dimensional representation U,V
is either standard or the sum of two trivial representations: these are
all dimension-two possibilities by the elementary highest-weight
classification for sl2. On the diagonal torus diag(t,t^(-1)), the right
side of (14) has largest exponent at most 2r+2. The left has largest exponent
4r+2 with coefficient one. Since r>=1, the Laurent polynomials cannot agree.
This proves the theorem.

The reductivity and dense-set assumptions are explicit. For a Galois-family
application one must establish the relevant joint algebraic monodromy and the
density of the Frobenius set separately. In the usual non-CM elliptic setting,
standard big-monodromy theorems are the additional input connecting that setting
to the SL2 hypothesis; this packet does not reprove or silently assume them for
every family. No assertion about arbitrary positive-density subsets is made.

The argument handles odd r too: it used a squared-eigenvalue polynomial identity,
not the unproved existence of a global half-Tate twist. Thus the warning that
angle powers are not representation homomorphisms has an exact obstruction
under stated nonabelian hypotheses. Abelian/CM-type and finite-monodromy
realizations remain separate questions, not ruled out or constructed here.

## 7. Consequences for the repository's open tasks

**Odd q.** If q is any positive odd integer and A,B,C are integers, 2q cannot
be a square. Thus the signed graphs (2) classify the full intersection for
EVERY r>=1. This strictly extends the frozen rank2/rank3 converses in scope.
The same conclusion holds for positive rational q outside square class2.

**Characteristic-two nonsquare bases.** If q=2^(2k+1) with k>=0 an integer, r is odd and the raw
traces are integral, all solutions are the eight triples

    (A,B,C)=(0, +/-2^(k+1), +/-2^(k+1))
         or (+/-2^(k+1),0, +/-2^(k+1)),                     (15)

with the indicated signs independent. To see completeness, G1/G2 with odd
r at a nonsquare q force either a Dickson zero or C^2=2q. A Dickson zero
makes w torsion, so the class2 table applies; (15) is its full odd-rank row.
Alternatively irrationality of q^(r/2) times a nonzero rational A in G1
forces A=0, then D_(r+1)(z)=0; the table lists exactly the resulting points.
The first four are nongraph only at r==3(mod4). No assertion of simultaneous
elliptic-curve realization or a compatible family is added.

**The r=4 noncyclotomic question.** It is resolved without an elimination:
T1 excludes every nongraph noncyclotomic point at every r. T2 also excludes
all nongraph rational raw points at r=4. This is new proof, not validation
of the old unretained exploratory script or its reported search totals.

**Positive-dimensional geometry.** T1 identifies the reduced positive-
dimensional support for every rank. It does not compute a uniform short
coefficient prefix, embedded components or scheme multiplicities. The full
arbitrary-complex torsion residual has the bound (5), not a claimed minimal
list of its orders for every r.

The prior all-rank Hasse formulas count the graph loci. Theorem T2 now shows
that those loci exhaust the odd-prime raw intersection, provided each counting
formula is used with its own separately established hypotheses and review.
This packet does not rerun or re-audit that entire counting/realization corpus.
Local spectral equality does not imply global Euler-product equality, a
representation homomorphism, automorphy, GRH or RH.

### A recognition algorithm without constructing the large factors

Put calD_n(C,q)=q^(n/2)D_n(C/sqrt(q)). These are rational polynomials defined
by calD_0=2, calD_1=C, calD_(n+1)=C calD_n-q calD_(n-1). Then G1 becomes

    B=sigma C,     q^(r/2)A=sigma^r calD_(r+1)(C,q),

and G2 becomes

    A=sigma^r C,   sqrt(q)B=sigma(C^2-2q).

If q is not a rational square, an equality between a nonzero rational and
sqrt(q) times a rational is impossible. This treats the odd-rank cases
without rounded radicals. The exceptional predicate is (4).

Finally calD_n(C,q) is the trace of the nth power of the 2-by-2 matrix
[[C,-q],[1,0]]. Binary powering evaluates it in O(log(r+2)) rational arithmetic
operations. Thus recognition of the complete spectral equality does not
require expanding either degree-(2r+2) characteristic polynomial. This is
an arithmetic-operation count, not a bit-complexity or memory bound; exact
rational numerators and denominators can grow with r. The supplied checker
uses this test only on explicitly bounded data and compares it with a
separate complete-power-trace construction.

## 8. Proof and computation boundaries

The eigenvalue-ratio reduction, maximum-weight argument and rational
cyclotomic descent are paper proofs. The small torsion table is completed
by exact finite affine-class enumeration whose unbounded-rank validity is
proved in (11). The checker does not infer an infinite claim from a numerical
ladder. All roots are handled by integer residue multiplicities; no algebraic
number is rounded. Independent Newton/power-trace tests and explicit residual
controls are additional bounded regressions, not substitutes for completeness.

The supplied proofs are proposed for independent review. The general
representation-theoretic weights and elementary algebraic-integer facts are
classical, and the two graph formulas are credited to the frozen predecessor. T3 additionally
uses the classical simple-factor and highest-weight structure of reductive
algebraic groups, at its explicitly stated scope.
No exhaustive literature-priority claim is made for this classification.
