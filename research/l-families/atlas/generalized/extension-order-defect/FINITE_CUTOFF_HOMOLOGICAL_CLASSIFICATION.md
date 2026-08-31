# Finite source cuts are maximal Cohen--Macaulay but not perfect

Status: proof-only consequence of the exact normalization/minimal-generator
packet at `03b1a04df3427a09781cdf4d43a9326671a2e566`. The C6 source
input is `d4fcbe331751e1e506cc2f38864c0c1580df92e8`. No new computation,
curve census or minimal-resolution acquisition is used in this corollary.

Keep characteristic zero, the split group G=C3, the actual even Segre
algebra A, and the positive grading of the preceding packet. Let S be a
**finite-dimensional** graded G-representation, with character dimensions
r0,r1,r2. Put P=Sym(S), B'=A^G tensor P^G and C=(A tensor P)^G, and let
m=B'_+ be the homogeneous vertex.

**Theorem.** C is finite over B', and both B'_m and C_m have depth
4+r0+r1+r2. Its exact number of minimal generators at m is

    mu(C_m)=1+8[r1+r2+binom(r1+1,2)+binom(r2+1,2)].           (1)

If r1+r2>0, its generic rank is3 and its projective dimension over B'_m
is infinite. If r1=r2=0, C=B', its rank is1 and its projective dimension
is zero. The trivial directions r0 change the depth and dimension but
do not change the number in (1).

**Proof.** Orbit polynomials and Reynolds averaging prove finiteness, as
in the normalized source construction. The C6 proof establishes that A
is Cohen--Macaulay and finite over A^G. Choose four homogeneous parameters
x in A^G. They are parameters in A, hence form an A-regular sequence.
Likewise choose r0+r1+r2 homogeneous parameters y in P^G. Since P is a
polynomial ring finite over P^G, they form a P-regular sequence. The
concatenated sequence x,y is regular on A tensor P: tensoring over a field
preserves each of the required injections and successive quotients.

All parameters are independently invariant. Exact Reynolds projection
identifies invariants of each successive quotient with the corresponding
quotient of invariants, so the same sequence is regular on C and on B'.
It is a system of parameters for both, of length4+r0+r1+r2. This proves
the stated depth equality and the graded maximal Cohen--Macaulay property
at the vertex. These are the usual finite Noetherian parameter arguments;
see [Stacks, Cohen--Macaulay rings](https://stacks.math.columbia.edu/tag/00N7).

The preceding exact minimal-quotient theorem gives

    C/B'_+C = k direct-sum Abar1 tensor Pbar2
                  direct-sum Abar2 tensor Pbar1,
    dim(Abar1)=dim(Abar2)=8,
    Pbar1=S1 direct-sum Sym^2(S2),
    Pbar2=S2 direct-sum Sym^2(S1).

Taking dimensions proves (1), including any repeated internal grades.
Localization at m does not change this residue-field quotient. If either
nontrivial summand is nonzero, the prescribed independent actions are
faithful and the fixed-field theorem gives generic rank3. Formula (1)
is then at least17, so C_m is not free: a free module would have its
minimal number of generators equal to its generic rank.

If its projective dimension were finite, the classical
[Auslander--Buchsbaum formula](https://stacks.math.columbia.edu/tag/090U)
and the equal depths above would force projective dimension zero. A
finite projective module over a local ring is free, a contradiction.
Thus its projective dimension is infinite. When S is wholly trivial,
invariants act only on A, and C=A^G tensor Sym(S)=B'; the remaining
assertions follow directly. QED.

For an actual even Lie cutoff N>=2, write
k_N=sum_(2<=n<=N, n even) C_n. Each standard summand supplies one of each
nontrivial C3 character, while the sign summands are trivial. Therefore

    mu(C_N)=1+8 k_N(k_N+3),   generic rank(C_N)=3,
    pd_((B'_N)_m)((C_N)_m)=infinity.                          (2)

Here k_N>=1 because the authenticated degree-two standard multiplicity
is1. Equation (2) is a consequence of the full minimal polynomial already
replayed by the preceding packet. It needs no further numerical fitting.

This theorem concerns finite cuts and their own full invariant bases. It
does not assign a depth or Cohen--Macaulay property to the infinite,
potentially non-Noetherian algebra. It neither supplies a whole-base
periodic free resolution nor turns the relative A2 matrix factorization
into one. The no-branch-divisor statement of the original two-variable
chart is not extended to all S: one nontrivial variable already gives an
ordinary branched cubic chart. Finally, the source normalization and this
homological classification do not select an analytic determinant frame
or enlarge the earlier operator's convergence domain.
