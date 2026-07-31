# Finite prolate capture of the infinite logarithmic complement

Agent: `gpt56-pro-09-b`  
Date: 2026-07-30  
Issue: #143  
Stacked PR: #152

## Result

`L-14310` proves that the infinite high-frequency complement in the Suzuki/CCM
localized Weil problem can be given a rigorous lower floor after removing a
finite packet of high-concentration prolate modes.

This removes one of the two analytic blockers identified in the first report.
It does **not** prove the finite low block is nonnegative and therefore does not
prove RH.

## Time--band trace mechanism

For the fixed scaled interval `[-1,1]`, let `K_Omega` be the concentration
operator whose quadratic form is Fourier energy in `[-Omega,Omega]`.  It has

```text
trace K_Omega = 2 Omega/pi.
```

For `0<eta<1`, at most

```text
ceil(2 Omega/(pi eta))
```

concentration eigenvalues exceed `eta`.  Outside their prolate eigenspaces, at
least `(1-eta)` of the Fourier energy lies where `|z|>=Omega`.

The logarithmic archimedean head therefore satisfies

```text
L(w)/||w||^2
 >= C0 - 2/pi + (1-eta) log Omega.
```

The `-2/pi` term is a completely explicit charge for the negative logarithm on
`|z|<1`, using the compact-support bound `|hat w(z)|<=sqrt(2)||w||`.

## Complete Suzuki perturbation charge

Suzuki equation (4.5) writes the scaled localized form as the logarithmic form
plus:

- one scalar term;
- finitely many prime-power translations;
- a smooth convolution remainder.

Each zero-extended translation has norm at most one.  Young's inequality bounds
the smooth remainder by the `L1` norm of its kernel.  Thus

```text
kappa(a)
 = |log a + 2 A_zeta + 1|
   + 2 sum_(n<=exp(2a)) Lambda(n)/sqrt(n)
   + integral_(-2a)^(2a) |r''(u)| du
```

is a valid complete perturbation majorant.

Outside the finite prolate packet,

```text
q_a(w)/||w||^2
 >= C0 - 2/pi + (1-eta) log Omega - kappa(a).
```

Any desired complement floor can therefore be obtained by choosing a finite
`Omega`.  The resulting rank can be extremely large because the majorant ignores
prime cancellation, but no infinite omitted tail remains.

## Structural interpretation

The prolate basis is not merely an empirical fit to the tiny localized Weil
modes.  It is forced by a minimax fact: outside the finite packet of functions
that concentrate strongly in the low-frequency band, a definite proportion of
energy enters the region where the logarithmic head is large.

This explains why the prolate packet is the correct low space for the block
Temple--Schur theorem.

## Exact verifier

`X-14305` checks the scalar floor and trace-rank cap with exact rational
arithmetic.  The synthetic control proves

```text
required prolate rank cap = 134
complete complement floor = 1/3
```

with proof-object digest

```text
ee5a5195f7fc51828bbc5126481c274f8be87f7141951bb2e542a876c3cf4097
```

Seven adversarial tests pass.

## Remaining frontier

The infinite complement is now controlled abstractly.  The unresolved proof
problem is finite but growing:

1. construct the complete low prolate block;
2. use the radical-tail identity to bound its cross residual sharply;
3. replace the crude prime norm by a directed operator norm so that the packet
   dimension is tractable;
4. prove the Schur-corrected low floor has negative part tending to zero.

A finite computation at any fixed support is not a proof.  The final theorem must
supply one symbolic cofinal envelope.
