# Validation and limits

The manuscript is proposed mathematics. It has no independent referee acceptance
and no Lean/kernel proof. The numerical part is a computer-assisted existence
certificate for a SIX-moment finite ferromagnet, not an RH certificate.

## Primitive numerical contract

certify_seed.py uses only Python integers and fractions.Fraction for acceptance.
At 128-bit dyadic precision it reconstructs Machin pi, range-reduced exponential
Taylor enclosures, and integer-square-root enclosures. It integrates all 16385
nodes of a 16384-cell composite Simpson rule for the first four literal positive
theta terms on [0,2]. Every required fourth-derivative error, the entire omitted
index tail and the entire physical tail are included. Normalization divides by
the resulting positive full mass interval. The certificate includes moments
through eight; only moments through six enter the seed theorem.

The nine magnetization values of K8 compress ALL 256 configurations exactly by
binomial multiplicities. The 4096 independent spins use their EXACT finite
cumulants; no Gaussian approximation enters acceptance. Directed evaluation of
both rational q endpoints proves opposite sixth-cumulant signs. All 128 CLOSED
parameter subintervals verify the radical and variance guards. A point sampling
interpretation of these 128 intervals would be incorrect.

## Executed final commands

```sh
python -I -S -B certify_seed.py --check seed_certificate.json
python -I -S -B -O certify_seed.py --check seed_certificate.json
python -I -S -B test_seed.py
python -I -S -B -O test_seed.py
```

The two full reconstructions reproduce identical JSON. The eight bounded test
methods pass in both modes: dyadic arithmetic, independent Fraction exponential
series, derivative budgets and tail constants, Peano kernel/Simpson algebra,
all-configuration Ising checks against the binomial compression, finite bath
cumulants and the variance repair, a mixture/current-conservation control, and
strict receipt parsing. Test method counts are not mathematical theorem counts.
The all-configuration graph tests have four declared rational q values and use
the original disagreeing-edge weights, not the binomial implementation.

The accepting command authenticates the complete nine-file inventory and all
eight checksum entries, then reconstructs the numerical result. --emit is a
producer command without authentication. Canonical typed-JSON comparison is
used; duplicate keys and float literals are rejected. Optimization-mode success
is not represented as independent implementation.

An initial combined orchestration completed the normal full replay but timed out
during the optimized replay. That interrupted replay is not counted. A later
performance-only edit adds proven underflow and negative-half-line Lipschitz
enclosures. A second combined delivery orchestration timed out after both full
local replays; that unfinished delivery run is not counted. Final delivery checks
were subsequently run as separate bounded commands. The final source also checks
the strict radical guard and every packet entry, including the manifest.

An isolated clean ZIP extraction and a minimal add-only Git patch roundtrip
replay both full-check modes. The patch preserves an unrelated sentinel and
matches each packet byte. Neither is a complete repository checkout, graph
validation, remote CI, Windows run, or formal proof build.

## Exploratory calculations excluded from proof

An ordinary high-precision theta integration and several floating inverse-spin
fits motivated the construction. A one-K8-plus-Gaussian six-moment fit succeeds
numerically; the final theorem replaces it with a finite bath and a rigorous
existence bracket. A restricted two-community 16-spin fit did not find a
near-exact ten-moment solution; a different two-K8-plus-Gaussian fit did. No
optimization success or failure is used as a mathematical proof. These scout
programs and their numerical parameters are not accepting dependencies.

No actual xi zero, numerical contour, full theta operator spectrum, all-order
Ising representation, increasing-order feasibility campaign, or new global
zero-free region was computed. Existing parent proof bytes were authenticated;
parent executables and external Lee--Yang proofs were not independently rerun.
The source-to-spin construction at unbounded moment order remains OPEN.
