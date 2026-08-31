# Preregistration: varying-prime physical conditioning

Registered before the new pair calculation. This is a refinement of the
already proved fixed-finite-prime injectivity theorem, not a duplicate proof
of it. Use exactly two distinct primes p,q and the three literal curvature
coordinates

    A = integral v du, C = integral v^2 du, D = integral u^2 dv.

Retain the original factor two and physical measure. With
`P_p=D(z_p) conjugate(A(z_p))`, the three direction fields must first be
checked from the source decoder as

    Z_A=2(P_p conjugate(P_q)-conjugate(P_p) P_q),
    Z_C=(P_p-conjugate(P_p)) |D(z_q)|^2,
    Z_D=|D(z_p)|^2(P_q-conjugate(P_q)).

Study the real normalized fields

    E_A=-i sqrt(pq) Z_A,
    E_C=4i q sqrt(p) Z_C,
    E_D=4i p sqrt(q) Z_D.

Primary theorem target: if p,q tend to infinity with q/p tending to a
fixed r>=1, their original-measure Gram converges to an explicit matrix in
terms of the frozen autocorrelation Gamma. If r=1, prove loss of uniform
conditioning. If r>1, prove positivity of the limiting matrix without
extrapolating from samples. Preserve the distinction between fixed-prime
injectivity and a growing-prime-set frame.

Directed numerical reconnaissance may use L=32 and the exact gamma branches
at the fixed prime pairs `(101,103)`, `(1009,1013)`, `(10007,10009)`, and
`(1000003,1000033)`. It is a check on orientation and convergence only.
No numerical panel proves the limit. Do not replace the physical norm by a
coefficient norm or call a linear whitening map a legal source morphism.
Memory cap 256 MiB, time cap 120 seconds, at most 16,000 frequency pairs per
panel. Fail rather than silently clipping a tail or support branch.
