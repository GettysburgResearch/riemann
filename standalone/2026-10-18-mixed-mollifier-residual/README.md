# A stronger full-family estimate for the signed inverse residual

**Status: proposed analytic component proofs, not independently reviewed. RH
and the critical prescribed-member estimate are not proved.**

This continuation targets a quantity that is actually small because of Mobius
cancellation: `E_A=L M_A-1`. It does not introduce another positive surrogate
or a claimed zero-free fraction near 0.9. Every member remains in the residual
norm, including exceptional members and possible zeros. The reciprocal itself
is not bounded on every member.

## Main gain

For the specified sextic Hecke family and the genuine Mobius mollifier of
length `A=U^(3/5)`, the proposed theorem is

    sum_(Na<=U)^6-free |L_a(3/4+it)M_A(3/4+it,a)-1|^2
                         << U^(11/15+epsilon).

It is uniform for t in each fixed compact interval. #984's strongest directly
stated instance at 3/4 uses A=U^(1/4) and gives U^(7/8+epsilon). The new bound
improves the guaranteed error power by **17/120**, with a longer mollifier.
This is NOT a 3/4 zero-free theorem or a claim of best-known zero density.

The new operation is to use M6, R2, and R4 for the actual functional-equation
remainder R:

    sum |M R|^2 <= (sum |M|^6 * sum |R|^2 * sum |R|^4)^(1/3).

The respective family powers are U, U^(7/10), and U^(1/2). No false identity
turns chi(b)bar(chi(c)) into chi(bc). The actual conductor, subunit dual lengths,
shared primes, primitive principal exception and full analytic tails remain.
Using only the old pointwise M bound at these new scales would give U, with
no error power saving.

## Near-critical and all-order statements

For any fixed n>=3, set d=2sigma-1 with 0<d<=4/(5n). The explicit high-moment
choice in PROOF.md gives A=U^(nd/4) and

    sum |L_a(sigma+it)M_A(sigma+it,a)-1|^2
                         << U^(1-nd^2/4+epsilon).

For n=6 this triples #984's displayed error saving on each fixed line
1/2<sigma<=17/30. The moment parameter is fixed AFTER sigma; it tends to
infinity as sigma approaches 1/2. No critical endpoint uniformity follows.

Theorem C also proves an explicit complete residual-moment bound at EVERY
fixed even order, using only integer powering and legitimate interpolation.
At the 3/4 example its displayed high-order exponent becomes 3r/5 for r>=2;
it is not the missing sublinear-excess native hierarchy.

A compact-segment corollary gives relative approximation to the real reciprocal
values on a common quantitatively counted good set. The complementary rows
are not silently deleted from any claimed full reciprocal theorem.

## Read and replay

Read PROOF.md, particularly Sections 3--6, then SCOPE_AND_SOURCES.md.
Run `python replay.py` for both accepting modes, ten actually executed
negative controls, and the byte manifest. The finite checks are not an
analytic proof assistant or an independent mathematical referee.

No inherited file or scientific-status declaration is edited. The parent is
#984 at b6a29037a2be358294401d71d7305b0f402c2eea. The previous #980 work was
verified already published at 392223625496b6674795fa8e1c0eb9768688f1ef;
there is no newly missing payload to recover from this conversation.
