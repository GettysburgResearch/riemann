# Third pass: exact rational balance and a different norm target

**RH, the uniform full-source gain, and the subpower full-norm bound are NOT
proved.** This packet contains proposed component proofs and bounded directed
computation. Independent mathematical and implementation review is required.

Parent: PR #805, `0f8724bbd86c1de8f40eacbf30129321e0ebc8aa`.
All 22 predecessor files are unchanged. This is a separately labeled author
continuation, not an independent acceptance or canonical integration.

## Read the mathematics

[PROOF.md](PROOF.md) gives six component results and both attempted closures.
The earlier scalar normalization is now imposed exactly rather than estimated.
On all odd indices through M, a rational Jordan/Mobius formula constructs the
unique detail minimizer with `lambda_1=1` and `sum lambda_k/k=0`. Its constrained
detail error is `O(log^2(M)/M)`, and
`|lambda_k-mu(k)| <= 20 k (1+log M)^2/M` for M>=4096.

The actual original-dictionary source is

```
F_M = sum_(k odd <= M) lambda_(k,M) (h_(2k)-h_k),
F_M(n) = sum_(m odd <= n) sum_(k|m,k<=M) lambda_(k,M),
Mellin F_M(s) = (1-2^-s) zeta(s) P_M(s)/s.
```

`P_M(1)=0` cancels the pole exactly. The coefficients and source are fixed before
any hypothetical zero is considered. Nonsquarefree corrections are retained.
This is a particular trial in B_(2M), NOT the full B_(2M) optimizer.

The source converges to the target on a polynomial observation horizon. If a
zeta zero has real part beta>1/2, then its FULL energy obeys

```
liminf log(1+||F_M||^2)/log M >= (2 beta-1)/(2-beta).
```

Consequently `||F_M||^2=M^o(1)` would imply RH without the prior uniform doubling
gain theorem. That norm estimate is open. The unconditional bound supplied here
is only `||F_M||^2 <= 882 M(1+log M)^4` for M>=4096.

The full energy is also, up to `1+o(1)`, its finite middle sum on
`sqrt(M)<n<=M^3`. No broad evaluation of that sum is performed.

A coherent two-band source disproves a generic lifting argument even after
BOTH scalar constraints. Asymptotically detail-optimal perturbed sources can
converge on every fixed cell while their full squared norms grow at least like
`sqrt(M)`. This is not a refutation of the exact rational optimizer's subpower
conjecture, and it is not a refutation of RH.

## Reproduce the bounded evidence

Run from this packet root, with both unchanged sibling packets present:

```bash
python3 scripts/replay.py --check
python3 -O scripts/replay.py --check
PYTHONDONTWRITEBYTECODE=1 python3 scripts/test_replay.py
PYTHONDONTWRITEBYTECODE=1 python3 -O scripts/test_replay.py
```

The replay contains 3,884 executed controls, including exact independent KKT
solutions, primitive/divisor identities, constrained perturbations, and fixed
FULL infinite-Gram enclosures at M=4,8,16. The maximum consumed basis index is
30; the hard Gram cap is 32. Ten unit tests include twelve isolated actual CLI
corruption refusals in each interpreter mode. See [NUMERICS.md](NUMERICS.md)
and [VALIDATION.md](VALIDATION.md) for precise scope and omissions.

The primitive coefficients, all finite arithmetic, and interval endpoints use
integers/Fraction. No floating-point numerical value enters acceptance. Hashes
bind the input source and retained bytes; they do not establish the analytic
proofs. No claim of novelty or priority is made for classical ingredients.

## Review target

First review the rational affine minimizer, the unconditional coefficient bound,
and the zero-to-energy exponent (PROOF sections 1,2,5). Then review the complete
coherent counterconstruction (section 6), numerical remainders, and fixed-source
binding. The outstanding claim is explicitly BL26.E, not an unrecorded tail in
one of the finite numerical matrices.
