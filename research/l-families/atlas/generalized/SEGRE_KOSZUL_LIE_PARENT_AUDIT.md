# Independent audit: Segre Koszul--Lie parent

Status: exact-source review passed. Accept the classical constructive
realization and strict all-grade sign theorem within their stated scope.
No analytic completion, positive Euler parent, automorphy or RH consequence
is accepted or claimed.

Reviewed source: 39f19e361c476c77cd016d314662448f43df7a80.
Programme copy: 834819bf96ce6611db5bc988c2ae88aa401c4656.
Review date: 2026-08-31.

The root read the complete proof, producer, tests and source manifest,
reconstructed the duality and sign argument, and reran the frozen checks.
A separate exact-SHA reviewer read all five artifacts and both parent
notes, verified the relevant primary literature and independently rebuilt
the small algebraic controls. No repair to the frozen packet was needed.

## Frozen identities

The note, producer, fixture, manifest and test have Git blobs, respectively:

- 6036546493e416fdb44e57e6c9746e9a92844a5c;
- d7452ee72b35aa0fa15a2cd1d20cb55d696bb236;
- 9836bf23250087bedacee2877bf44da07f61637b;
- 635f70f3b4833cff5aac9b83fdab2824d15446cb;
- c5d13f16d7cb3e2ff1f6982f4e26871de43df7af.

Canonical payload:
1e0d5ddfa65dd5a98d12cbf4c95204eb5152a17dcb8305b7da295486264dd300.

All five programme artifacts match the frozen source. Both declared
parent bindings authenticate by commit, Git blob and LF hash, including
the current parent-file bytes. Neither earlier proof is modified.

## Mathematical acceptance

1. Coordinatewise multiplication independently defines the product-group
   Segre ring before any scalar specialization. The sorting quadrics have
   a terminating normal form, and distinct chain monomials have distinct
   images. This is a genuine presentation, not fitted Hilbert-series data.
2. The quadratic sorting/PBW criterion gives Koszulity. The all-degree
   statement invokes the classical theorem; the finite bar complexes are
   falsification and consistency controls, not its proof.
3. The image of the dual multiplication lies in Sym^2(E-star), the degree
   two part of the free odd Lie superalgebra. It therefore gives actual
   Lie relations. The universal-property identification
   U(g)=T(E-star)/(Q)=R-dual and the primitive-relation explanation are
   consistent, including square terms in characteristic zero.
4. The equivariant Koszul resolution and super PBW give exactly
   W_d=(-1)^(d+1)[g_d-star]. The dual cannot be omitted. Central scalars,
   polynomial multidegrees, odd exterior factors and even symmetric
   factors all have the stated signs.
5. Super Jacobi reduces every bracket word to nested degree-one brackets.
   Thus g_d=[g_1,g_(d-1)], and one zero grade forces all later grades to
   vanish. The frozen noncyclotomic/finite-parent obstruction then proves
   nonvanishing in every equal-rank nonexceptional grade, not only
   eventual scalar sign alternation.
6. The polynomial/rank-one cases and the separately defined k=0 convention
   agree with the original coefficient powers. For two rank-two factors,
   the single even degree-two generator is central by the odd Jacobi
   identity. No higher Lie grades remain.
7. The complete unequal-rank (2,3) cubic character identifies
   (V_1 tensor det V_1) tensor det V_2. Its two dimensions alone would not
   identify that representation. Tor over the Segre ring and linear
   syzygies over Sym(E) remain different constructions.

These accept GLO764.SEGRE_KOSZUL_LIE_REALIZATION_V1 and
GLO764.SEGRE_STRICT_ALL_GRADE_SIGNS_V1. They do not extend the stated
equal-rank finite-parent classification to arbitrary unequal ranks.

## Prior art

This is a classical construction. The root verified the quadratic-dual
Lie mechanism in
[Gorbounov--Schechtman, section 3.4](https://sigma-journal.com/2009/034/sigma09-034.pdf)
and
[Cederwall and collaborators, sections 3.2.1--3.2.3](https://link.springer.com/article/10.1007/s00220-024-04990-z).
The sorting presentation is also explicitly given by
[Morales, Theorem 4 and Lemma 3](https://arxiv.org/pdf/1306.6910);
[Priddy, Theorem 5.3](https://math.mit.edu/~hrm/palestine/priddy-koszul-resolutions.pdf)
provides the PBW-to-Koszul implication.

The separate reviewer also checked the declared general syzygy context
in Gorodentsev--Khoroshkin--Rudakov. That context is not needed to infer
the displayed rank-16 linear-syzygy calculation. No Borcherds presentation
or previously unknown L-function theory has been constructed here.

## Independent computation and scope

The root reran 25 tests in each of normal and optimized Python, both
producer checks, Ruff lint and format checks, and the full introduced
whitespace diff. All passed. The producer also passed after import.

The separate reviewer reported, in both Python modes:

- 34 independently constructed bar complexes, including all 16 published
  complexes, using multiset monomial bases and SymPy rational matrix ranks;
- 11 independently constructed cubic Lie quotients, including all five
  published panels and their full torus-weight multiplicities;
- the independent 56-by-18 variable-times-minor matrix, rank 16, with
  exactly the two displayed independent linear syzygies;
- all 156 supported rank/degree preflight panels, with 144 accepted,
  12 rejected, and maximum accepted allocation 11158 basis slots;
- all source and artifact identity checks.

These additional controls use independent bases/elimination, not the
producer's Hilbert-series inversion; in fact the producer does not use
such inversion for its bar or Lie ranks. The unequal (2,3) degree-four
Tor dimension is 81, while the corresponding ring piece has dimension 75.

The caps are pre-allocation structural bounds, not CPU-time or bit-size
certificates. Rational elimination is exact; typed canonical replay,
duplicate-key/nonfinite rejection, byte limits and explicit runtime
requirements remain effective under Python -O.

## Unchanged analytic boundary

The infinite product is T-adic. The actual graded modules are signed:
even grades do not become a positive Euler parent. The construction does
not change the scalar divisor-power coefficients, the existing natural
boundary, the finite-gamma obstruction, or the ordered global graded
product's convergence threshold. A regularized grade sum is not the
original ordinary Euler product. RH and GRH remain open.

The proof's historical proposed/awaiting-review label remains untouched;
this separate audit records its later acceptance.

