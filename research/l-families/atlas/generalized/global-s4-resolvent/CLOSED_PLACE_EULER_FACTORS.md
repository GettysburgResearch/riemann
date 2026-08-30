# S4 Euler factors at actual closed places

This sequel constructs the closed-place Euler products for all four
nontrivial S4 representations of the fixed Bring-quartic cover. The
source geometry and all-field determinant identification are those of
`S4_RESOLVENT_AND_RAMIFIED_FROBENIUS.md`. The new finite replay multiplies
local denominators at actual Frobenius orbits, independently of Newton
reconstruction from extension point counts.

Write t=T^deg(v). At an unramified closed place the local denominators
det(1-t F_v | rho) are:

| class | sign | two | std | tw |
|---|---|---|---|---|
| identity | 1-t | (1-t)^2 | (1-t)^3 | (1-t)^3 |
| transposition | 1+t | 1-t^2 | (1-t)(1-t^2) | (1-t)(1+t)^2 |
| double transposition | 1-t | (1-t)^2 | (1-t)(1+t)^2 | (1-t)(1+t)^2 |
| three-cycle | 1-t | 1+t+t^2 | 1-t^3 | 1-t^3 |
| four-cycle | 1+t | 1-t^2 | (1+t)(1+t^2) | (1-t)(1+t^2) |

These are determinants of the original permutation actions: std is the
four-root permutation representation with its constant line removed;
two is the three-pair-partition permutation representation with its
constant line removed; tw=sign tensor std. Their construction therefore
does not rely on deciding eigenvalues from a single character value.

At a finite branch let epsilon=chi_(k(v))(-2). In the same order the
invariant local denominators are

    1,     1-t,     (1-t)(1-epsilon*t),     1-epsilon*t.

At infinity, which is a degree-one place, let delta=chi_k(-1). They are

    1-delta*T,   (1-T)(1-delta*T),   1-T,   1-delta*T.

The trivial representation always has denominator 1-t. In particular,
the full infinity correction in the two-dimensional representation is
1-T^2 over Q=3 mod4. The finite negative tw factor is 1+t, even though
the invariant space is one-dimensional. Replacing either of those
factors with its invariant-dimension approximation gives a different
Euler product.

For each of the three frozen source curves, the replay enumerates every
affine closed point of degrees one through four using complete Frobenius
orbits in the declared field model. It reconstructs every minimal
polynomial, checks its irreducibility, and verifies the exact number
(1/d) sum_(e|d) mu(d/e) Q^e of degree-d places. Each orbit's source class
is evaluated over its own residue field. This ensures that the quadratic
characters are chi_(Q^d), not incorrectly frozen at chi_Q.

Multiplying reciprocal local factors, including infinity, in Z[T]/T^5
gives P_D,P_R,P_E,P_tw through degree four, and the trivial product gives
1/((1-T)(1-QT)). The degree-eight factor is only verified through degree
four by this replay. Its complete determinant and the two held-out
extension checks remain supplied by the precursor.

The artifact records class/factor multiplicities for each degree, a
canonical digest of all enumerated minimal-polynomial/class records,
and the final truncated Euler products. The producer reconstructs this
data from the primitive source before acceptance; the digest is not used
as an input oracle. Every field has at most 2401 elements and the cutoff
is fixed at four before allocation. Finite source, code and output
identities are all authenticated and typed JSON comparisons distinguish
booleans, integers and floats.

The proof of the all-place equality uses the actual l-adic sheaves of
the source and the trace formula. As usual the Euler product converges
absolutely in |T|<1/Q and the cohomological polynomial supplies its
continuation. The bounded Euler multiplication is a separate check of
the ramification adapter and conventions; it is not a proof from finite
data of purity or the all-place identity.

Ruff, complete generation, ordinary and optimized producer checks, and
all 14 focused tests in each Python mode passed. The tests took about
0.027 seconds per mode. The independent reviewer read the proof, producer
and tests without claiming independent execution. Root serialized all
computation; no field allocation exceeded the stated cap.
