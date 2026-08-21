# X-21501 — Exact prime-polygon tangent contraction

**Status:** exact finite arithmetic / synthetic regression. No Riemann-data verdict is retained in this packet.

`verify.py` checks the finite implication in `T-21501`:

\[
W_j(r)
=2A_j\log r-4r-\kappa\log r-C_0
 +4\sum_{k\ge1}\frac{r^{-(4k+1)}}{(4k+1)^2}-B_j>0
\]

implies a negative value of the zeta screw function and therefore disproves RH.
The checker uses Python integers and `fractions.Fraction` only. The positive
series is enclosed by a retained partial sum and a geometric upper tail.

## Trust boundary

A `RIEMANN_DIRECTED` certificate must bind an external producer for:

- the complete duplicate-free prime-power prefix;
- directed enclosures of `A_j` and `B_j`;
- the trial radius and its logarithm;
- directed enclosures of `kappa` and `C0`;
- the manifest, transcendental producer, and constant-source SHA-256 digests.

The checker contracts those inputs exactly. It does not enumerate primes or
evaluate transcendental constants itself. A `SYNTHETIC_MODEL` verdict is never
reported as an RH verdict.

## Replay

```bash
python3 verify.py certificates/synthetic.json \
  --output results/synthetic-verification.json
python3 -m unittest discover -s tests -v
```

The retained synthetic packet exercises a strict positive tangent. Seven
mutation/interface tests cover interval order, support radius, series count,
classification bindings, and decisive/nondecisive branches.
