# A based holonomy source repairs the gauge boundary

Status: exact finite model, proposed for programmes #763 and #764.
RH and GRH remain unproved. No arithmetic adapter or external novelty is claimed.

The [earlier fixed-label response](../fixed-label-cycle-response/README.md)
depends on a numerical identification of distinct vertex fibres. Here the
additional source data are explicit: a representation of a based free group,
and two marked word-cycle automata. The response is then a well-defined
function on the unitary representation space modulo simultaneous conjugation.
It is not a descent theorem for the earlier unmarked graph problem.

## Source, clock, and exact theorem

Let F be the free group on a,b. Declare c=(ab)^(-1), independently of any
representation, and take two directed three-cycle automata with ordered
edge labels (c,a,b) and (c,b,a). Each edge has clock length one. These are
primitive cycles of the automata even when their group words reduce.
**Clock length is not reduced free-group word length.**

For any unitary representation rho:F -> U(V), dim V=d, put
U=rho(a), V0=rho(b), C=(U V0)*. The labels are group images, never fitted
eigenvalues. With the block-row convention of the earlier packet, set

    T0 = [[0,C,0], [0,0,U], [V0,0,0]],
    T1 = [[0,C,0], [0,0,V0], [U,0,0]].

Write K=(U V0)*(V0 U). Then the following identities hold for every d:

    det(I-t T0) = (1-t^3)^d,
    det(I-t T1) = det(I-t^3 K),
    tr(T0^n) = tr(T1^n) = 0                 if 3 does not divide n,
    tr(T0^(3r)) = 3d,
    tr(T1^(3r)) = 3 tr(K^r),                r >= 1,
    Re tr(T0^3-T1^3) = (3/2) ||U V0-V0 U||_F^2.

The third-trace response is therefore nonnegative and vanishes exactly
when the image of this two-generator representation is abelian. The two
zeta functions Zj(t)=det(I-t Tj)^(-1) agree exactly in that case. Every
one-dimensional representation, and hence all word-holonomy data factoring through the
abelianization F -> Z^2, is blind to the comparison. For a subgroup
H <= U(d), all assignments U,V0 in H are blind if and only if H is abelian.

### Proof

Tj^3 is block diagonal. Its three diagonal blocks are the cyclic rotations
of CUV0 or CV0U, respectively. Invertible labels make these rotations
similar, so their powers have equal trace. Other powers have no diagonal
blocks. CUV0=I and CV0U=K give the trace identities. The formal identity
log det(I-tT)=-sum(n>=1)tr(T^n)t^n/n gives the determinants, with constant
term one; alternatively eliminate two block rows. Consequently

    Z1(t) = exp(sum(r>=1) tr(K^r) t^(3r)/r).

This is the twisted primitive-cycle Euler factor and trace formula of the
same declared automaton. For permutation representations it is also the
ordinary Euler product of the finite lifted directed cycles. These formal
identities converge analytically for |t|<1 because K is unitary.

For A=UV0 and B=V0U, unitarity gives
||A-B||_F^2=2d-2 Re tr(A*B). Substitution proves the energy identity and its
vanishing criterion. Equality of the determinants forces equality of their
t^3 coefficients, hence Re tr(K)=d and U V0=V0 U. Conversely commuting
matrices give K=I. Applying this to all pairs in H proves the subgroup
claim. No finite census is used in this argument.

## Gauge covariance and what was added

Replacing rho by Q* rho Q conjugates U,V0,C,K simultaneously and conjugates
both Tj by diag(Q,Q,Q). All the stated observables therefore descend to
Hom(F,U(d))/U(d). There is no chosen basis left in this quotient.

Independent changes of basis Q0,Q1,Q2 on the three automaton fibres also
preserve the comparison: transform **each already defined transfer matrix**
by diag(Q0,Q1,Q2). Equivalently its edge (i,j) transforms as Qi* Aij Qj.
Both determinants and the trace gap remain unchanged. The common based
representation determines how the two automata use the same holonomies;
it is part of the source and cannot be discarded and reconstructed from
one unmarked cover. Reusing old numerical labels after changing only one
cover is a different operation, already refuted in the earlier packet.

Thus this construction answers a narrower, operational question: what
extra source data makes this family comparison natural? It does not prove
that the original scalar determinant determines the enrichment, or that
an arithmetic source has such a representation. The scalar observation
of any abelianized representation is identical for both words, but their
unitary character responses can differ. No scalar postprocessing can
restore information absent from every one-dimensional character.

## Sharp controls and held-out prediction

For U=(12), V0=(23) in the degree-three permutation representation, K is a
three-cycle. The determinant pair is

    (1-t^3)^3  versus  1-t^9,

and the first trace gap is 9. Every degree-one or degree-two permutation
image is abelian; degree three is the minimum permutation degree for a
distinction. General unitary labels differ: the real orthogonal matrices

    U = [[0,1],[1,0]],  V0 = [[1,0],[0,-1]]

give K=-I and determinant pair (1-t^3)^2 versus (1+t^3)^2, with trace gap
12. General unitary dimension two is therefore already sufficient, while
dimension one never is.

The degree-three source predicts its complete lifted cycle structure:
the first automaton lifts to three 3-cycles, the second to one 9-cycle.
For an arbitrary permutation K with cycle lengths l1,...,lr, the second
lift has lengths 3l1,...,3lr, so its determinant is the product of
(1-t^(3li)). The producer checks this against literal sparse walks of the
lifted graph, alongside determinant expansion and Newton traces, on all 36
ordered degree-three pairs and three predeclared degree-four hold-outs.
The held-outs were copied unchanged from the earlier source manifest;
none was selected by the present result.

## Replay and provenance

`source.json` is the declared primitive word/clock/fixture contract and must
equal the compiled specification. The producer uses the earlier exact
rational matrix library, pins its original source commit and content hash,
and binds both this note and its focused tests by LF-normalized SHA-256.
The complete canonical output is recomputed, not accepted from internally
consistent input JSON. Computation is capped at degree four; full transfer
matrices are only built through degree two (dimension six); sparse lifted
graphs have at most twelve vertices. No zero search,
growing graph census, numerical eigenvalues, or symbolic package is used.

```text
python -B research/exploratory/marked-holonomy-response/holonomy_response.py --check
python -B -O research/exploratory/marked-holonomy-response/holonomy_response.py --check
python -B -m unittest discover -s research/exploratory/marked-holonomy-response/tests
python -B -O -m unittest discover -s research/exploratory/marked-holonomy-response/tests
```

Unit tests are finite adversarial controls; the all-dimensional theorem is
the proof above. The based-word and matrix-weighted zeta ideas are classical.
[Matsuura and Ohta](https://arxiv.org/abs/2208.14032) give a primary-literature
baseline for unitary matrix-weighted graph zetas and Wilson loops. Their
Bartholdi conventions and large-N conclusions are not imported here. The
contribution is an explicit reviewed repair and reusable boundary model,
not discovery of a new graph-zeta theory.

The remaining arithmetic gate is a source-defined map to this based
holonomy object that preserves a specified native observable. Without it,
the model yields no gamma factor, arithmetic functional equation, purity,
RH estimate, or new L-function. No further finite scan resolves that gate.
