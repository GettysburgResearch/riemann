# X-23801 — Greedy carry residual regression

This experiment accompanies the one-sided carry-envelope proposal.
It keeps proof-grade finite algebra separate from floating-point discovery.

## Exact section

Using Python integers and `fractions.Fraction`, the verifier checks through
`n=50`:

```text
carry closed form = carry floor-sum form           1225 cases
Mobius affine carry transform                       1225 cases
minimum sum_(q<=n) beta_(nq)/q                      1/6
```

The last value is stronger than the proof threshold `1/16`.

## Binary64 reconnaissance

The nonexact section checks:

- the signed inverse coefficients through `X=10^5`;
- their weighted mass relative to `8 sqrt(X)`;
- the actual greedy producer through `X=2000`;
- the proposed sharper row potential `2-q^(-1/2)` through `n=5000`.

In the retained scan, the greedy producer takes no off-diagonal pivot through
`X=2000` and leaves no positive residual above the binary64 tolerance. The
signed inverse scan finds no coefficient below `-10^(-12)` through `X=10^5`.
These are discovery facts only.

A separate optimized C++ replay reached `X=10^7` with no coefficient below
`-10^(-10)` and weighted-mass ratio

```text
1.0006950924140714.
```

That larger replay is not an interval certificate and is not used by any claim.

## Run

```text
python3 verify.py
python3 -m unittest discover -s tests -v
```

Retained payload SHA-256:

```text
29ff992a02247305bd7404236aaca32f566bd2b32dc34386af0ba7b0541124fa
```

## Proof boundary

The experiment does not prove:

- Carry Saturation;
- the Greedy Residual theorem;
- a symbolic pivot-charging or quotient-layer bound;
- RH.

Only the exact section verifies mathematical identities. Every other output row
is labelled `BINARY64_RECONNAISSANCE_ONLY`.
