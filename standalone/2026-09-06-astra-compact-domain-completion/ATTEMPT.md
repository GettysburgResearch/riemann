# Completion attempt and the exact unsuccessful step

The user asked for domain completion or a different successful route. This pass
attacked domain completion constructively. It does NOT provide a valid RH proof.

## 1. Remove the earlier inadmissible inverse

The predecessor's inverse applied to a simple exponential contains delta
impulses and derivatives, so it is not an L2 input. Instead choose the OUTER
target H_b(z)=1/(z+b)^2, whose time function is t exp(-bt). Division by the
actual D_b cancels the polynomial factor:

    H_b(z)/D_b(z)=1/[(z+b-1)zeta(z+b)].

In the initial absolute half-plane this has the ordinary causal inverse
exp((1-b)t)sum_(n<=exp(t))mu(n)/n. Cutting that function at log(N+1) gives an
admissible compact L2 input and a source-domain output for EVERY finite N.
The cut creates exactly one compensating coefficient, -(N+1)sum mu(n)/n,
at n=N+1. No unknown prime, zero or optimizing vector determines it.

Mobius inversion proves exact target reproduction before the cutoff. This
is stronger than approximating a grid of times and needs no numerical solve.
But local exactness leaves the entire later tail to be paid.

## 2. The intended proof by norm control

If the outputs admitted a bounded subsequence, weak compactness would put the
outer target in the closed invariant source domain. That would fill the
domain. The remote-tail theorem shows that even SUBPOWER norms suffice: any
missing zero forces a fixed positive power of N in every output norm.

I attempted Young's inequality from the compact input. At b=1/2 its squared
norm is the exact rational sum S_N=sum_(k<=N)m(k)^2. This turns a functional
problem into a completely explicit arithmetic quantity, but it does not
bound it. The endpoint and signed terms in

    S_N=(N+1)m(N)^2-2sum_(n<=N)mu(n)m(n)+sum_(n<=N)mu(n)^2/n

are not controlled by the logarithmic diagonal. The unconditional estimate
used here yields only S_N<=N. The desired conclusion would need a genuinely
new bound for these cancellations or directly for the output.

Worse, UNIFORM input boundedness is false for the actual source: one of the
classically known critical-line zeros forces a boundary pole in the proposed
L2 inverse, violating the Hardy evaluation bound. This is not a synthetic
counterexample and not evidence for an off-critical zero. Boundary zeros are
compatible with RH, and convolution can suppress an unbounded input norm.
The subpower OUTPUT target survives this test and remains unproved.

## 3. Full-tail computation does not settle the quantifier

The eight certificates do not cut off the global output norm. Exact finite
cell integrals are combined with a periodic-Bernoulli bound for the entire
remaining tail. The N=64 squared relative error is <1/19000. N=128 has a
strictly larger error, so even monotonicity of these candidates is false.
The certificates do not establish convergence or subpower growth for all N.

The tail formula contains W=sum |c_n|n in its remainder. A naive uniform
estimate for W grows with the cutoff. The explicit polynomial-log main term
also contains signed coefficients C and L. Letting the tail start Y grow
just moves their needed cancellation into more finite cells. No all-N
estimate has been obtained this way.

## 4. No hidden completion from a synthetic or changed source

No positive replacement source, fitted zeta, altered Euler product, zero input,
or freely chosen metric is used in the constructive family. All equalities
are in the literal Lebesgue L2 metric. The source is the same D_b as CSM26.
Known small finite Gram positivity and safe Jordan positivity are not invoked
as a proof of cyclicity. The source's Blaschke factor is not divided out in
the construction: that would replace the very domain being investigated.

Averaging or tapering the cutoffs is a legitimate next construction, but no
unproved norm improvement is attached to it. The general remote-tail bound
applies to every candidate preserving exact agreement through a long initial
interval. It therefore prevents the same omitted-tail argument under a new
choice of coefficients.

## 5. Handoff target

For the explicit sequence in PROOF.md, prove unconditionally

    liminf_(N->infinity) log(max(1,||f_(1/2,N)||_2))/log(N+1)=0,

or produce another actual-source family of uniformly controlled outputs
whose weak limit is an outer target. This is not merely another checker:
it requires a signed arithmetic norm estimate. PROOF.md supplies the full
conditional deduction and quantitative obstruction but not that estimate.

The correct conclusion of this pass is a compact admissible inverse, local
exactness, a multiplicity-sensitive cost theorem, and eight global finite
certificates. The critical source domain and RH remain open in this packet.
