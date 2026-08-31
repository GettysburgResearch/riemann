# Arithmetic-shape activation as arity grows: preregistration

Status: discovery before execution; no claim for arity beyond the frozen r<=6 atlas.
The primitive object is the all-subset native activation source in
HIGHER_NATIVE_CLUSTER_ATLAS.md at 755b27c2c9747f3db255238c59c2622dee6cad8b.
Its arithmetic shape is x_i=i, i=0,...,r-1. The leading objective is
H(q)=sum_(|S|=|T|) q(S)q(T)|sum S-sum T| with the original physical
multiplier 8A epsilon/(4^r K). This scout never substitutes that leading
form for the exact finite kernel.

Run every r=2,...,16. Build exact incidence histograms
c_i(k,s)=#{S:|S|=k,sum S=s,i in S} by the generating polynomial
u v^i product_(j!=i)(1+u v^j). Independently build the full unmarked
polynomial and check sum_i c_i(k,s)=k*c(k,s) and each band mass.
No individual subset is discarded; dynamic programming evaluates this
complete finite polynomial exactly.

Build every matrix entry by two-sided prefix distance sums, retaining the
whole integer r-by-r matrix. For r<=8 independently enumerate every
subset and compute the cumulative-cut matrix, comparing every entry.
Do not reuse one matrix construction as the other.

Reflection preserves H; strict concavity from the frozen theorem makes
the unique optimizer reflection invariant. Enumerate every nonempty support
among its ceil(r/2) reflection groups, at most255. Solve each exact rational
KKT system with original pair-normalized group variables. Retain the unique
positive-support solution and check ALL original-coordinate inactive and
active gradients, not only reflection-restricted inequalities.

Hard caps: r<=16, every exact numerator/denominator <=1024 bits,
linear dimension<=9, <=255 support systems per row. No floating rank,
numerical optimizer, prime search or large scientific library. Root runs
the job alone under its monitored memory guard.

The pre-run hypothesis is that even arities keep the central two activations
and odd arities the central three, but this is not a required acceptance
condition. Every contrary outcome is retained. The known r=2,...,6 cases
are controls, r=7,...,16 are held-out exact discoveries. Positive inactive
slacks, zero slacks and any wider support are separately recorded. Any
all-arity theorem or finite-prime claim requires a separate proof.
