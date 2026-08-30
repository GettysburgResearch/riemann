# Independent review of positive holonomy defect and critical circle

Reviewed commit: `6b4f0f4a53bc9ff5bc6b84a2b6e3f603a04f2336`.

Review object: `POSITIVE_DEFECT_AND_CRITICAL_CIRCLE.md` and
`tests/test_holonomy_polarization.py`, the two-file sequel to the separately
reviewed marked-holonomy source at
`e7fc8b0af2c42ce43384543972df2ed44f343300`.

Verdict: no mathematical or implementation blocker found for the stated
finite unitary operator identities, reciprocal determinant law, spectral
circle, and permutation principal-kernel obstruction. These are classical
finite-model mechanisms, with no claimed arithmetic transfer.

## Evidence boundary

I read both frozen files in full and reconstructed the identities. I did
not execute tests, a producer, linter, numerical eigenvalue calculation,
or build. The implementation agent reports Ruff, fourteen marked-holonomy
tests in ordinary and optimized Python (nine earlier plus five new), and
unchanged original producer checks in both modes passing. Its original
proof-object digest remains
`bf2d2af9fae943db5e538ca02885d871eddec9d53548cebf256d4093d4ca52b6`.
These are reported execution results, not independent executions by this
reviewer.

The earlier canonical JSON is not represented as authenticating these two
new files. They are a separately frozen proof/test sequel; this exact Git
commit and review identify the extension.

## Mathematical audit

For A=UV and B=VU, K=A*B is unitary. Expanding either Gram product gives

`H=I-(K+K*)/2=(A-B)*(A-B)/2=(I-K)*(I-K)/2`.

Thus H is positive semidefinite, with kernel exactly ker(UV-VU) and
ker(I-K). Simultaneous conjugation of the based representation conjugates
H. The earlier real third-trace gap is exactly 3 tr(H), so its positivity
comes from an explicitly defined positive operator.

For the full automata, T0^3=I and T1 is unitary. The Hermitian part of
T0^3-T1^3 is therefore the displayed Gram operator. Its three diagonal
blocks are unitarily conjugate to H because the cyclic return products
are related by unitary edge labels. Independent vertex-fibre basis changes
preserve that operator statement. The common based holonomy marking remains
part of the source.

Each transfer matrix is unitary because its block rows and columns contain
exactly one unitary label. Every determinant root consequently lies on
|t|=1, without using those roots to define the source. The three-cycle
block permutation has positive sign and the label determinant product is
one, so det(T0)=det(T1)=1.

The general unitary determinant factorization gives

`D(t)=(-t)^N det(T) conjugate(D(1/conjugate(t)))`.

Substitution of N=3d and det(T)=1 proves the stated reciprocal law. The
sign and complex conjugation are necessary. The manuscript correctly calls
this self-inversive reciprocity and does not infer real coefficients. This
is a finite spectral circle, not an arithmetic critical-line theorem or
functional equation with gamma factors.

For a permutation K, diagonalizing each cyclic shift gives eigenvalues
`1-cos(2*pi*j/ell)` for H. Equivalently H is half the cyclic-shift
Laplacian `2I-K-K*`; this formula also fixes the length-one and length-two
conventions. Nullity is the number of permutation cycles and rank is d
minus that number. Constants on each cycle, including the global principal
constant line, are killed by H.

The examples are correct: the degree-three witness has H spectrum
{0,3/2,3/2}, trace response nine, and a surviving zero principal line;
the orthogonal anticommuting two-dimensional example has H=2I and response
twelve. A positive total defect therefore does not supply a lower bound on
the principal line. This is a substantive scope boundary, not a claim that
the positive form is a nondegenerate polarization in all representations.

## Exact test inspection

- The new tests verify the reviewed holonomy producer's normalized content
  hash before import; that producer in turn authenticates its matrix library.
- Both Gram factorizations are compared directly for the declared S3 and
  held-out S4 pairs using rational arithmetic.
- The S3 row-sum kernel, trace, determinant polynomial, and identity
  H^2=(3/2)H independently pin the displayed spectrum without numerical
  diagonalization.
- The orthogonal positive-definite example and an abelian zero example
  distinguish semidefiniteness from universal positive definiteness.
- Full transfer unitarity, the Gram identity for I-T^3, and determinant
  reciprocity are checked in real dimension six. Odd-dimensional and
  complex-unitary reciprocal laws rely on the complete prose proof, not
  that finite even-dimensional control.
- Rational orthogonal conjugation checks covariance of the positive defect.

No defect was found in these five bounded controls. They do not
machine-prove the all-dimensional theorem or establish arithmetic meaning
for the representation.

## Remaining scope

The same predeclared finite source now exhibits an Euler/trace law,
reciprocal determinant symmetry, a spectral circle, and an explicit
positive operator. Its principal-kernel example also shows why possession
of those structures alone does not control a desired principal member.

The missing arithmetic step remains a source-defined, observable-preserving
map into this holonomy model, together with any required transfer of the
positive form. No archimedean factor, conductor, purity, automorphy,
arithmetic explicit formula, RH/GRH theorem, numerical stability result,
or external mathematical novelty is established by this sequel.
