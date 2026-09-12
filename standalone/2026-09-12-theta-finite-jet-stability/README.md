# Finite-jet theta stability: a tested attempted completion

**Proposed component proof, not an RH proof. Independent review required.**

The preceding whole-theta cumulant packet was uploaded at
`4558dce9cb981a2e8c0e3e058b21a5b17f6a1cf5`. Its all-degree Hankel sign is still
unproved. This continuation tests the proposed passage from finite positive
matrices to that infinite sign, using the exact theta source.

For any prescribed finite moment order, an even differential perturbation can
preserve those moments exactly, preserve both xi endpoint values and the full
real zero divisor, and be arbitrarily small in every fixed exponentially
weighted derivative-integral norm. It remains a positive smooth density, yet
its transform acquires nonreal zeros. The full source is changed, so these are
NOT zeros of zeta, and its extra zeros need not all stay in the critical strip.
Neither the literal theta identity nor the Euler product is preserved.

## An explicit complete example

With `D=d/dt`, take

```
A=D^40(D^2-1/4), R=2^324, eta=1/4,
c=[(R+i/4)^2]^20[(R+i/4)^2+1/4],
a=Re(1/c), b=1/|c|^2,
phi_R=phi+2a A phi+b A^2 phi.
```

The paper and exact polynomial bounds give, on the WHOLE real line,

```
phi_R > (1-2^-72) phi >0,
|phi_R-phi| <2^-13231 exp(-t^2).
```

All moments through degree 39 are unchanged. The entire transform is exactly
`Xi(z)*(1-f(z^2)/c)*(1-f(z^2)/conj(c))`, with `f(v)=v^20(v+1/4)`.
The multiplier is positive for every real `v`, so it preserves every real xi
zero and its multiplicity. It equals one at `v=0,-1/4`. It has 21 distinct
conjugate nonreal `v`-root pairs, including the prescribed quartet corresponding
to `s=1/4 +/- iR, 3/4 +/- iR`.

Thus the original finite G9/J9 certificates are inherited exactly but do not
prevent later negative cumulant directions for this changed source. No new
native matrix order, actual zeta zero, or numerical theta integration is claimed.

Read **PROOF.md**, then **REVIEW.md**. The Schur remainder for the next native
Hankel extension is explicitly stated in Section 1; no lower bound for it or
all-order propagation has been proved.

## Reproduce the bounded arithmetic

```
python -I -S -B check.py --check result.json
python -I -S -B -O check.py --check result.json
```

The checker reconstructs derivative polynomials through order 84, proves the
complete rational majorant inequalities, and verifies the inserted Gaussian-
rational root. Its other finite controls independently reconstruct low-order
derivatives, moment-annihilation identities and Schur algebra. These executions
are not a machine proof of Fourier integration, source asymptotics, or the
parent's infinite index theorem. `--emit` produces a record without authenticating
the inventory and is not an accepting replay.
