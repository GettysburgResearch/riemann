# Scaled SHARP activation certificate for every m>=19/15

Status: **Root-reviewed component theorem with completed directed
certificates.** Root independently accepted the full analytic argument and
source implementation on 2026-10-10. All 250 real rectangles and ten
whole infinite tails pass in normal and optimized Python modes with
byte-identical outputs. Root independently replayed all five source-control groups in both modes. The reviewed contracts (E1)--(E10) and
(P-A1)--(P-A7) are used unchanged, with a larger finite cutoff. Critical
power one and RH remain open.

**Component theorem A-LPA1.** H_m(x)>0 for every real m>=19/15 and every
real x>=1.

Fix N=100000000, B=N/2=50000000. The ordinary prime list through B
contains 3001134 primes, last 49999991, plus the extra labelled 67. Every
label of a selected product at levels two, three, four or six is <=B.
The ordinary and marked finite moments are therefore complete for their
selected products <=N. Their exponents, cutoffs and levels are bound
explicitly in the engines. No finite list replaces the infinite V.

For the activation upper envelope, the bin edges are B,3N/4,N,5N/4,3N/2.
The complete prime list through 150000000 contains 8444396 primes, last
149999957. The final omitted tail is V(a)-C_(1,0)(a,B) minus all four
finite bin masses. Its directed upper mass multiplies the positive
representative kernel at 3N/2. The ratio C_i/N is unchanged from the
root-reviewed proof: v<15/16 on every real x>=N, and the degree-32
binomial omitted-tail bound is 16 b_32 v^32. The positive normalized
whole-tail numerator (P-A7) consequently has degree at most 38.

## Exact continuous coverage

The eleven exact power points are

\[
 19/15,1.267,1.2675,1.2682,1.2692,1.2706,1.2726,
 1.2754,1.2794,1.284,9/7.
 \tag{L-A1}
\]

Ten consecutive closed slabs cover [19/15,9/7]. The 26 endpoint points
are the complete chain (S-W2) through 10^7, followed by 2*10^7,4*10^7,
8*10^7,10^8. Its 25 consecutive closed intervals cover [1,N]. Each
slab/endpoint rectangle is bounded by the complete four-level margin
(S-E2), using upper odd levels one and three at its lower power/right
endpoint, and lower even levels two and four at its upper power/left
endpoint. The selected three-label source is complete. When an endpoint
exceeds B, the complete omitted single-label tail is explicitly added
to its upper bound. Monotonicity in both real variables, including native
activation jumps, is the already reviewed proof (T1), (E9), and (S-E2).

For each slab, the polynomial (P-A7) proves the entire tail x>=N by a
complete Bernstein coefficient certificate on 0<=z<=N^-1/2. The cap is
rounded outward to a forty-bit exact dyadic rational; exact subdivisions
cover both halves and every entire Bernstein coefficient ball must be
positive. A failed guard rejects the slab. No finite endpoint scan or
asymptotic interpolation is used.

Thus 250 real rectangles plus ten complete unbounded-tail certificates
suffice for [19/15,9/7]. The preceding A-PA1 packet covers every m>=9/7,
so their union yields A-LPA1. Every stated finite guard passed; root
independently reviewed the parameterized source implementation.

## Source controls and actual execution

`exclusion_power_data.py` changes only the finite cutoff/endpoint inputs
of the existing reviewed ordinary/marked prefix and kernel routines.
`verify_large_activation_stitch.py` fixes the above complete coverage and
prime census guards. Arb precision is 192; all powers, endpoints, bin
edges and acceptance conditions are exact rational or directed-ball
operations. Normal and optimized JSON outputs must be byte-identical.

`test_exclusion_power_data.py` compares the parameterized builder's
four-level lower bound with literal native beta sums obtained by independent
trial factorization at two powers and six endpoints, including duplicate
67 activation. It checks ordinary/marked cutoff, exponent and level
metadata, the explicit complete single-label tail, and invalid power,
cutoff and endpoint domains. All three groups pass normal and optimized
modes. The existing four marked-prefix controls and four prime-activation
controls remain required inputs; their executed receipts are separate.

`test_large_source_oracle.py` adds two stronger source-control groups.
Independent trial factorization of every integer through 40000 reconstructs
the positive projection multiplicity and its exact static used-label mark,
without the engine sieve, label list, recursive subset enumeration, prefix
queries or caches. At two powers it compares all seven ordinary and marked
moments at levels two, four and six, including active six-label products.
It also compares the actual normalized source levels at six endpoints,
including the complete larger-prime source beyond N/2. Both modes pass
these two groups. The original three groups and these two are separately
recorded, rather than counted as an independent infinite theorem proof.

The first directed single-power tail at m=19/15 used one Bernstein leaf
with positive lower scale 0.0067614191113. This is reconnaissance for the
full theorem; it is not used as a substitute for the complete power-slab
certificates. At N=10^8 the zero-defect comparisons at m=5/4 and m=1.26
were negative (-0.0255532 and -0.00553412 respectively), so neither lower
power is claimed. The fixed three-pair architectural floor in
`FIXED_PAIR_BARRIER.md` further explains why this finite mechanism cannot
by itself reach the native critical limit.

`LARGE_ACTIVATION_EXECUTION.json` binds the completed run hashes, interval
counts and review status. Each whole slab used one Bernstein leaf. The
first slab [19/15,1.267] has positive lower scale 0.0057052076290034481.
Both outputs have SHA-256
`75667457c8d6202d4afa09191f7620396948241a17a5ab21f31369a9b13cdf6a`. The infinite analytic contracts remain manually
proved, rather than machine-proved by these finite execution receipts.
