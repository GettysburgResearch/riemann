# X-106191 — Connected Kummer and source-dual centered-incidence replay

This light finite replay checks the exact algebra in:

- `L-106190` connected two-modulus Kummer–Möbius inversion;
- `L-106191` source-dual rescaling and centered double-incidence expansion;
- the one-prime total even-character weight `q-1` used in `R-106124` and
  binding `R-106131`;
- the atomic coefficient cancellation
  `(ell-1)(rho-1)+ell+rho-ell*rho=1`.

Run from the repository root:

```bash
python experiments/X-106191-centered-incidence-replay/verify.py
```

The script uses only the Python standard library. It tests 240 deterministic
complex packets over six pairs of distinct odd primes, performs 1,680 numerical
identity checks, and also performs exact rational character-weight and integer
atomic-cancellation checks. The committed result is
`results/verification.json`.

## Scope firewall

A passing finite replay authenticates the finite identities and catches sign,
normalization and diagonal-counting errors. It does **not** estimate the global
least-prime conductor family. In particular it does not prove:

```text
WCCORR106191 / WCADD106140;
WCEQ106191 or WCDIST106191;
WCKUM106140;
BCI102990;
the Riemann Hypothesis.
```

The replay records explicitly that for prime reduced cores `c=ell,d=rho`, the
rescaled atom has `u=v=1` and therefore no individual least-prime decay. That
is the reason the bounded centered kernel cannot be closed by a source-blind
free-energy estimate.
