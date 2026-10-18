# A degree26 complete-theta realization by one additional positive edge

**Status: PROPOSED computer-assisted finite theorem.** A full directed
contraction certificate proves a connected finite ferromagnet matches the
original standardized theta moments through degree26. It extends the
degree24 tree in theta/PROOF24.md. No unbounded-order realization, improved
global zeta zero-free boundary, or RH conclusion is asserted.

## The finite graph and exact cyclic moment map

Start with the degree24 hub-and-dimer architecture, whose counts are

    [2,10,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,127].

There are306 observed spins and one unobserved fair hub. The306 existing
edges form a connected tree. Attach one additional edge between the roots
of the single copies of component types2 and3, using zero-based component
indices. The result has307 vertices,307 edges, and exactly one cycle.
Every observed weight is strictly positive. Every edge coupling is finite
and strictly ferromagnetic. All root-to-hub biases are eta=10^(-10).

As in the tree construction, dimer type i has physical weights
(A_i+B_i)/2 and (A_i-B_i)/2, and its internal alignment probability is
p_i in (1/2,1). Conditional on the hub being positive, write mu_i,n for
the n-th raw moment of its observable and tau_i,n for the root-spin
weighted raw moment. With V_i,n=p_i A_i^n+(1-p_i)B_i^n,

    mu_i,n = V_i,n times (1 if n even, eta if n odd),
    tau_i,n = V_i,n times (eta if n even, 1 if n odd).

Both formulas include n=0, where V_i,0=1. Components are independent
before the new edge. If q=tanh(J) is its correlation parameter, multiplying
the conditional law by the exact positive edge factor 1+q sigma_i sigma_j
gives the merged pair moments

    mu_pair,n(q) = [conv(mu_i,mu_j)_n+q conv(tau_i,tau_j)_n]
                     /(1+q eta^2),

where conv(a,b)_n=sum_(r=0)^n binomial(n,r)a_r b_(n-r).
This retains the complete partition correction; it is not a first-order
response in q. The partition correction is identical for the two hub
signs, so the hub remains fair after the new edge is inserted.

Replace the conditional cumulants of those two copies by the merged pair
cumulants. Add all other conditional cumulants with their complete
multiplicities, recover conditional moments, and average the two hub
signs. The odd unconditional moments vanish. The even moments and
cumulants are exact rational functions of the finite graph parameters.
The implementation is cyclic_model.py. Its generic quotient derivative
retains derivatives of the partition correction as well.

## Complete source, finite witness, and directed existence proof

The source is exactly the original complete theta density of
theta/PROOF22.md and theta/PROOF24.md. source_extended.py freshly
reconstructs orders0,2,...,26 using the pinned320-bit outward integer
primitive, all98 cells, all six explicit theta indices, and the complete
Taylor/time/index tails. No saved optimizer residual or source midpoint
is an acceptance premise.

The rational parameter center and a fixed rational13-by13 preconditioner
R are in parameters26_cycle.json. The active chart is

    [6,51,15,21,3,27,48,9,12,5,18,53,54],

where the last coordinate is the new edge correlation. Every other
coordinate is fixed. The cube radius is r=10^(-30). At the rational
center the new edge bias is approximately

    q = 0.06364023671573725485302823876257592737748608935428.

Let F be the13 complete source-normalized cumulant residuals. Fresh
outward interval evaluation proves, on the entire cube,

    beta=||R F(c)||_infinity < 6.171 * 10^(-33),
    L=sup ||I-R DF(x)||_infinity < 0.000512454,
    beta+L r < 0.01 r < r.

Indeed beta/r<0.006171 and L<0.000513. The certified invariance margin
therefore exceeds0.99r.

For clarity, only beta+Lr<r and L<1 are needed mathematically. The
checker enforces the stronger beta<r/100, L<1/1000, and invariance margin
greater than0.99r. The initial trial r=10^(-32) had beta approximately
6.17*10^(-33); it failed the selected center-displacement guard. The
published witness uses the larger rational cube above and freshly checks
its complete Jacobian. No failed trial is presented as a certificate.

Since ||I-R DF(c)||<1, R DF(c) is invertible by a Neumann series.
Both matrices are square, so R is invertible. The contraction
x -> x-RF(x) maps the full cube into itself. Its unique fixed point
therefore satisfies F(x)=0. The triangular cumulant/moment identities and
symmetry give equality of every original standardized theta moment
through26 at this exact graph parameter.

Whole-cube guards verify all physical weights positive, all edge biases
in (10^(-11),1-10^(-9)), total support below12, and the conditional
normalizer greater than0.99. The finite weighted Lee--Yang theorem thus
gives real Fourier zeros for this finite law. The zero-observable hub is
handled by adding a positive hub weight and taking the finite-law
complex-uniform limit, as in theta/PROOF22.md.

## Reproduction and independent finite checks

From the repository root:

```text
python standalone/2026-10-18-three-direction-sprint/reviews/certify_cyclic.py --parameters standalone/2026-10-18-three-direction-sprint/reviews/parameters26_cycle.json --check standalone/2026-10-18-three-direction-sprint/reviews/certificate26_cycle.json
```

The emitter passed with canonical JSON/LF output SHA256

    1902199f7739161368517f566eb749fb1183dec64615a768c620352610966b05

and bounds beta=6.170153825140304e-33,
L=0.0005124538802249338. The certificate contains all source intervals,
all input identities, the exact rational finite witness, and the strict
invariance margin. Replay requires fresh equality of the entire output,
not merely comparison of printed decimal summaries.

The printed output hash is computed before Windows text-file newline
translation. It identifies canonical sorted JSON with one LF terminator;
it can differ from the raw saved-file byte hash. The packet manifest
records raw-file SHA256 values separately. Input hashes inside the
certificate always hash the actual input-file bytes.

check_cyclic_model.py independently enumerates complete small physical
spin fixtures and tests root/child endpoints, repeated component copies,
raw moments and derivatives. theta/cycle_independent_controls.py adds a
separate full-hub enumeration with explicit analytic probability and
observable derivatives, and a complete307-vertex scaled-integer raw-EGF
assembly. Its full26 receipt has SHA256
6ba1cbdb1c529c5d009dd935c69a1691782a4abe34de6637781431b624543282.
That assembly does not reuse the conditional cumulant recurrence or
the normalized pair-quotient implementation. These checks corroborate
the finite graph identity; the directed contraction supplies existence.

Increasing the finite degree is useful only if the source is retained and
the graph remains legal. This certificate checks both. It does not settle
the separate cofinal existence requirement needed to identify an entire
limit with xi or transfer a global zero-location conclusion.
