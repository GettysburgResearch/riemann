# Direct exact-xi spectral attempt

**RH is not proved.** This is a record of a direct attack on the complete xi
function, not a further compression of the residual solver. Read [PROOF.md](PROOF.md)
and [REVIEW.md](REVIEW.md). No independent acceptance or novelty is claimed.

For the literal positive even theta density phi, define V=-log(phi), C=V'/2,
and the positive self-adjoint confining operator H=-d²/dt²+C²+C'. The manuscript
establishes on its common operator domain

    P(z)=H-izC-z²/4,
    ker P(z) nonzero iff Xi(z)=0.

The two exact endpoint-decaying solutions have Wronskian -Xi(z), at every
complex parameter. Geometric nullity is one at a characteristic value; this
is not a claim that every xi zero is simple.

The attempted finish was spectral reality from positivity of H and parity.
It does not work: P(z) is not self-adjoint for nonzero real z, its factors are
not adjoints, and parity yields an indefinite metric. The exact state identity is

    integral V'(t)|y(t)|²dt = -Im(z) ||y||².

Showing that this integral vanishes for every characteristic state of the
UNMODIFIED source would finish RH. That assertion is not proved here. Replacing
the state at conjugate(z) by the state at z is the precise unjustified symmetry
step, not a missing technical estimate that a reviewer is asked to fill in.

There is an exact test of the broader positivity/modularity inference. For
any d>0 and 0<eta<1/2 the positive self-reciprocal heat trace in Section 7 gives

    Xi_(d,eta)(z)=Xi(z)[cosh(d eta)+cos(dz)]/[cosh(d eta)+cosh(d/2)].

It has the same reflection equation and endpoint normalization, is entire of
order one, and has a positive rapidly decreasing theta-type Fourier density,
yet has explicit nonreal zeros (2k+1)pi/d +/- i eta. Its multiplier is strictly
positive on the real axis, so it also retains the ENTIRE real zero divisor
and every real zero multiplicity of Xi. These are CHANGED-source
zeros, not zeta zeros. The modified trace has a positive atom below pi and
does not retain the exact integer-square theta spectrum. Its source converges
back to the original in every fixed exponentially weighted derivative norm as
d->0; the new zeros escape to unbounded heights.

This universal differential construction should not be sold as a new
Hilbert–Polya solution. Its value here is a precise complete-source test of the
proposed global spectral argument and a record of exactly why that argument
has not become a proof.

## Execution

    python -I -B check.py --check result.json
    python -I -B -O check.py --check result.json

Only bounded exact algebra is checked. Domain arguments, infinite theta sums,
Wronskian interpretation, and global zeros of the changed entire function are
paper derivations, not consequences of test counts. See [VALIDATION.md](VALIDATION.md).
The preceding gamma packet and all other branches remain unchanged.
