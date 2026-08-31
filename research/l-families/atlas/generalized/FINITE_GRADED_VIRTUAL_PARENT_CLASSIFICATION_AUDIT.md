# Independent review of the finite-graded virtual-parent classification

Reviewed source: 7c9e7bde7980c4cfc0b3c3e521fa022319244caa.

Reviewer: root / codex-two-programmes, independent of the author.

Verdict: PASS in the stated universal algebraic-representation and
T-adic formal scopes. No scientific repair was required.

The reviewed note, producer, and default fixture have Git blobs
3932273279d43ffa34d929247152cb43b932fa1d,
974a13aa9c04d1f6732910eeadde65b411891723, and
b98cb5e2eb83e41f2b6bbd2b1b2fa7bd8e362b31 respectively.
The review read all five packet files, including the complete tests and
source manifest. The frozen source is preserved separately from this
review's identity.

## Independent mathematical reconstruction

At the identity of GL_n every genuine representation acts by identity,
including both summands used to define a virtual representation.
A finite collection of positive grades therefore produces only
root-of-unity zeros and poles. This remains true after cancellation.

The numerator differential recursion in Section 2 has exactly the claimed
coefficient rule. In each later cycle its new leading coefficient is
positive because q-m=a-j+1>0. The alternating signs at the old simple
negative roots, the sign at zero, and the leading sign at negative
infinity give all m+1 distinct negative roots. The constant-polynomial
base case is included. This proves the theorem for all fixed n,k, not
just the machine rectangle.

There is also a genuinely independent obstruction: H(0)=1 and roots
of unity would force the absolute first coefficient to be at most the
degree. Writing a=n-1, the excess is
(1+a)^k-1-(2k-1)a. It is a(a-1) at k=2; at k>=3 its quadratic term
already exceeds the remaining negative linear term. Exactly (n,k)=(2,2)
escapes among n,k>=2.

The rank-two exception is a character identity on the dense semisimple
set and hence coefficientwise on all GL_2. Its second grade is the
negative character -(det V)^2; it is not an effective extra state.
The identity also holds for Jordan matrices. The elementary n=1 and
k=0,1 cases and the polynomial convention at k=0 are explicit.

The T-adic factorization follows by a triangular coefficient elimination
using sigma_t(W)=1+Wt+O(t^2). No division in the representation ring
is required. The second class is the negative sum of the nonempty
even flip-parity summands of the tensor square. This is a nonzero
actual relation representation with negative sign when n,k>=2.
Uniqueness excludes an all-effective infinite escape already at grade
two. Outside the finite chambers infinitely many virtual classes are
nonzero by the finite-parent theorem, not by inspection of scalar tails.

The Zariski-dense version is legitimate because every coefficient is a
regular function on GL_n, including determinant-negative algebraic
characters. Evaluating at identity introduces no singular parameter.
The theorem does not constrain independently assigned scalar Frobenius
eigenvalues or finite matrix-coefficient resolvents.

## Exact replay

The root reviewer reproduced:

- all 21 tests in normal Python and all 21 under -O;
- the canonical producer in both modes;
- the hard-max 30-row census through grade 16, as part of those tests;
- the Sturm repeated-root, positive-root, and nonreal countercontrols;
- the independent triangular Euler-product reconstruction;
- direct tensor determinant controls for Jordan, rotational, rational,
  and nonsquare-spectrum matrices;
- the source-authentication-before-import and pre-arithmetic cap guards;
- the raw trailing-zero type rejection tests;
- Ruff lint, Ruff format check, and Git whitespace check.

The source worktree remained clean. The arithmetic classes are the
canonical MIXED combination of EXACT_RATIONAL and
CERTIFIED_INTEGER_COVERAGE. No floating root finder, fitted tail,
directed transcendental evaluation, or scientific assert is used.

The source lock authenticates three frozen primitive files and their
current LF-normalized bytes. The checker binds the complete typed
manifest, artifact hashes, and canonical rebuilt payload. Its operation
cap is explicitly a bound on named coefficient-update loops, not a
claim about bit complexity or elapsed time.

## Prior art and retained boundary

The reviewer checked the matching equal-factor specializations of
Corollary 1, Theorem 6, and Corollary 4 in
[Morales, Segre embeddings, Hilbert series and Newcomb's problem](https://arxiv.org/pdf/1306.6910).
The degree, Eulerian interpretation, and quadratic-relation count are
established mathematics. The packet itself gives a native interlacing
proof rather than depending on an unavailable full copy of Simion's
paper. No priority claim follows from this audit.

The result answers a finite universal parent question. The infinite
escape is only formal. Analytic convergence, a global Euler product,
canonical completion, automorphic or motivic realization, and all
RH/GRH-facing conclusions remain outside the theorem.

The smallest invalidating change would be allowing arbitrary extra
Frobenius eigenvalues at the group identity: that would destroy the
root-of-unity obstruction. Such extra operators are explicitly excluded,
not silently ruled out.
