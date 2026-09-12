# Connected harmonic-star completion of theta moment seeds

Status: proposed component proofs; independent mathematical review required.
**Not an RH proof.** This family still has a proved nonzero sixteenth-moment
error. It is a whole-law construction with the right large-field and tail
scales, not an all-order theta realization.

Start with [PROOF.md](PROOF.md). Parent: PR #863, exact head
`0640c9c59be0bf20c18258460a7517fb09728e82`. All prior files are preserved.

For every sufficiently large starting index N, the proposed theorem constructs
ONE connected infinite Ising star with positive weights and couplings. Its
finite connected approximants and its limit match the exact theta moments
2,4,6,8,10,12,14. The Fourier transform is even entire of order one with only
real zeros, and the limiting law has an analytic density. Its logarithmic mgf
has exactly the three growing terms

    (h/2)log h -(h/2)[1+log(2*pi)] +(7/4)log h,

and its full right probability tail satisfies

    exp(-2x) log P(X>=x) -> -pi.

These are the corresponding constants of the actual theta law. The additive
mgf constant, whole transform, and higher moments are NOT identified with Xi.
The standardized sixteenth-moment error remains in (0.20,0.21) for all
sufficiently large N.

## Mechanism

Use the 272-spin regular seed. Designate a dimer spin as the root and connect
its formerly independent spins with positive couplings N^-2. Attach infinitely
many leaves of weight 1/(2n) and root correlation 7/(4n), n>=N. Attach a finite
ballast of N^2 tiny leaves; its total observable weight is

    H_(N-1)/2-EulerGamma-log2-A_core.

It is positive for sufficiently large N. The harmonic sum controls the
h log h and log h terms. The ballast sets the h term exactly while perturbing
fixed moments arbitrarily little. A uniform C1 perturbation and the inherited
strict seven-variable root retune the core to preserve all seven moments.

The infinite model is defined by independent edge-sign variables conditional
on its root. Its complete complex product converges. No absolutely summable
infinite Hamiltonian is claimed: the sum of root couplings diverges. No finite
cutoff is substituted for the full law. The analytic construction proves
existence for sufficiently large N; a numerical threshold N0 and a retuned
parameter instance were NOT computed.

The limit as N increases is the old finite seed, NOT the theta law. Large-field
asymptotics are not uniform in N. The next problem is still arbitrary-order
source-specific reachability. A fixed-order implicit-function theorem cannot
be iterated without a new target-reachability proof.

## Replay and evidence

    python -I -S -B check.py --check result.json
    python -I -S -B -O check.py --check result.json
    python -I -S -B test_rejections.py
    python -I -S -B -O test_rejections.py

The new checker verifies bounded exact algebra only. The unchanged parent's
full theta integration was separately replayed in both modes, at pinned source
bytes. See [VALIDATION.md](VALIDATION.md) and [SOURCES.json](SOURCES.json).
No new numerical theta moment, infinite product, retuned large graph, zero
census, whole repository build, or formal proof was computed. Classical
Lee--Yang, Euler--Maclaurin, implicit-function and tilting mechanisms are
credited; no exhaustive novelty claim is made.
