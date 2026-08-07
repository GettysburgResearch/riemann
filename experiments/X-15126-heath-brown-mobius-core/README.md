# X-15126 — Exact Möbius core of the Heath–Brown packet

This standard-library experiment verifies the finite identities used by
`L-15159`:

```text
A_(K,V)
 = sum_(j=1)^K (-1)^(j-1) C(K,j)
   mu_V^(*j) * 1^(*(j-1))
 = mu                         through V^K,

A_(K,V) * log = Lambda        through V^K.
```

It also checks that fixing the final logarithmic variable at `q=2` leaves the
exact coefficient `mu(m) log 2`.

Retained cases:

```text
K=2, V=5, X=25
K=3, V=4, X=64
K=4, V=3, X=81
```

Run:

```bash
python verify.py results/exact-verification.json
python -m unittest discover -s tests -v
```

Retained digest:

```text
21a807fdd5b4fbd0fe4017816cb2660dc1bc645c52e0d8a8285eb84b72647eb1
```

The experiment is finite algebra only. It deliberately does not claim a
subexponential Möbius-energy estimate, `CP(K)`, or RH.
