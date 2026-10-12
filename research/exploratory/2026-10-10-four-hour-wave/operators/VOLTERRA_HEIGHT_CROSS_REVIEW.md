# Independent hostile audit of the Volterra height refinement

Verdict: **ACCEPT at the stated complete-source/imported-input scope.**
Reviewed V0--V9 in
[VOLTERRA_RATIONAL_REFINEMENT.md](../heights/VOLTERRA_RATIONAL_REFINEMENT.md)
at SHA256
`a9cf619b13278b71ae7662f55aa25607f1fd8507970b6f8028922abad8e779c9`,
and its checker at SHA256
`793635294b003ec68d124390e08ba7225538d66788443704f228fa6fad12e59a`.
Review time: 2026-10-10 14:40 UTC. The same reviewer previously accepted
the full W1--W19 dependency in
[HEIGHT_WEIGHTED_CROSS_REVIEW.md](HEIGHT_WEIGHTED_CROSS_REVIEW.md).
No mathematical correction was found.

Independent normal and optimized Python checker replays produced
byte-identical receipts `/tmp/operator_volterra_normal.json` and
`/tmp/operator_volterra_optimized.json`, SHA256
`9230f84ca62b1060f356d1cfe7378b01789b186f85a4f4608679fd9ca1af78cb`.
These exact controls accompany the analytic proof; they do not replace the
complete source or independently replay its published inputs.

The endpoint rank-one bound V2 is valid for complex vectors: diagonal
unitary conjugation removes all phases, zero entries may be removed, and
the normalized constant-function compression of upper Volterra is exactly
the strict upper matrix plus half the interval masses on its diagonal.
Both matrices are nonnegative entrywise, so the norm domination is valid
even though their difference is not positive semidefinite. Compression
cannot increase the Volterra norm. Even reflection of an H1 function with
the one specified endpoint zero gives the Dirichlet interval inequality
with constant 2L/pi, and the cosine ground state attains it. No extra
Neumann endpoint condition is silently imposed.

For the weighted polynomial dilation matrix, its diagonal is exactly
0,...,n-1. Taking strict upper parts of D+D*=E-M gives the improved
rank-one endpoint bound plus the strict-upper Hermitian noise. The latter's
squared Frobenius norm is at most half the complete squared Frobenius norm.
This yields the stated sqrt(n/2) term. The real rational prefactor adds
at most n+1, giving the final 2n term. The rational endpoint guard proves
the uniform .6382 bound for every n>=850000; no asymptotic substitution
is used below that range.

The count constant .236393 follows literally from the same published
argument bound and native theta remainder as the accepted dependency:
log u>28, loglog u<=log u/8, pi>3 give the displayed remainder, and the
remaining rational margin is exactly 1/7000000. One-sided limits of
nonzero-ordinate values preserve the bound required for a tail excluding
the atom at T. The integration-by-parts endpoint and derivative terms
retain factor 2 and give exactly ell=2*c_E*(1+2d).

For independently varying complex source displacements, the full
polynomial exponential acts on a fixed denominator and a polynomial of
unchanged degree. Discrete Minkowski, coefficient suprema and sampling
upper bounds apply to every D^jP. The signed-pole prefactor is retained
in the whole exponential. The exact exponential-tail guard proves the
amplification 1.185 uniformly on every Taylor path. The first and second
derivative identities are the same complete identities as W14. Their
coefficients are bounded by d*n^2+3n and
d^2*n^4+(6n+1)*d*n^2+9n^2+7n, respectively; |b/z|<=1 makes these bounds
valid with the real ordinate factors b and b^2. Both endpoint constants
.6383 and .4074 have decreasing correction terms and pass exact guards.

The complete-source product-rule payment has two outer derivative terms
and one middle term, with coefficient 2*(C2+C1^2). Conjugate groups cancel
the first Taylor term. The factor A^2/2<=1/8 then gives the displayed
quarter coefficient. Both reflected upper members, all multiplicities,
critical zero displacement and the exact 2*dN_+ reference measure remain
present. The scalar lower polynomial decreases with q, so its worst
endpoint is q=2631/10000. Its exact strictly positive gap, global 888000
guard, maximal even order 888424 at H0, and independent old-count fallback
866000 were all replayed exactly.

The accepted consequence is finite global Pick order 888000 under the
published complete critical-line census, and increasing complete-tail
orders under 10000*n^2<=2631*T for n>=850000. Adding smaller orders by
appending distinct positive nodes is valid. Increasing tail orders concern
changing kernels and supply neither all-order positivity nor RH.
