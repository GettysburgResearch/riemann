# Near-square-root compression of the complete residual operator

**RH and the native arithmetic upper bound remain unproved.** This is a proposed
component theorem for independent review, not a complete RH proof.
Parent PR #803: `db175de165a9077e709b1cb482998171ffc0c6e7`.
All changes are additions. Earlier research is unchanged.

## The positive all-scale result

For balanced coefficient tails Y<=n<=N<=AY, A fixed, use the ORIGINAL metrics

    S(c)=sum |c_n|^2/n,
    R(c)=integral_1^infinity |sum c_n floor(x/n)|^2 dx/x^2.

On any subspace retaining the exact tangent constraints, the squared singular
values of this map satisfy, for every rank r,

    lambda_(r+1) <= C_A Y log(r+2)/(r+1)^2.

Thus rank O_A(sqrt(Y)log^2Y) leaves squared operator error O_A(1/log^3Y).
The argument accounts for the entire frequency line. It combines a rank-K
critical-jet Taylor approximation with a Hilbert--Schmidt tail, then uses the
trace bound to control the remaining large singular directions. The only
quantitative analytic import is the classical approximate functional equation;
the needed zeta second moment is reconstructed, including its moving cutoff.
No RH, reciprocal-zeta estimate, numerical zero or subconvexity input is needed.

The retained directions can be selected through the earlier finite RATIONAL
full-source comparison form. This is not an infinite zeta quadrature. Exact
logarithmic derivative constraints remain logarithmic, not rationalized. The
construction is mathematical; a high-rank solver is not implemented here.

## Source-preserving optimization consequence

Keep the actual Mobius prefix below Y, p(1)=0 and p'(1)=1. In the nonempty
coefficient budget S(p)<=130(1+logY), with N=4Y, compression about the coefficient-
norm affine minimizer preserves every constraint and decreases S. The minimum
of the COMPLETE residual norm, after restriction to the retained affine space,
differs in square root by at most C/log(2Y), tending to zero.

This is not an upper bound making that minimum subpower. Nor is it a statement
that the unrestricted physical optimizer has the specified coefficient budget.
The graph-to-physical power loss is confined to at most that many independent
high-gain modes, not erased: the retained arithmetic problem remains OPEN.

## Reading and replay

PROOF.md contains the arguments and exact stopping point; REVIEW.md identifies
the claims and open estimate. SOURCES.json records precise source identities
and the external import. VALIDATION.md records executed and unexecuted scopes.

    python -I -S -B verify.py --check result.json
    python -I -S -B -O verify.py --check result.json
    python -I -S -B test_rejections.py
    python -I -S -B test_rejections.py --optimized

The checker uses integer/Fraction arithmetic only. Its finite source, projection,
trace, moment, graph and period identities do not machine-prove an infinite
analytic theorem. No new physical minimum, positive interval or zero-free region
is numerically certified. General approximation/trace/projection mechanisms
are classical; no external priority claim is made.
