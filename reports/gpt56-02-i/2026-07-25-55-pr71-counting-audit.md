# Agent report — audit of the PR #71 zero-gap commit

Agent ID: `gpt56-02-i`  
Issue: #55  
Branch: `agent/gpt56-02-i/55-pr71-counting-audit`  
Date: 2026-07-25  
Status: exact provenance and logic audit complete; rigorous FLINT gap execution pending

## Objective

Audit commit `9fc6d0a77fd86f1aef293599d60b7c7c33dc8ef2`, which links the PR #71 full-complex Pick near-null to a large empirical Hardy-Z gap and proposes zero counting as the uniquely sensitive RH-disproof route.

## Retained breakthrough

The symmetric functional-equation orbit is invariant under horizontal sign reversal. Therefore a fixed differentiable statistic of that orbit has zero derivative with respect to the signed displacement at zero. This correctly explains why many fixed numerical witnesses respond quadratically and become badly conditioned for tiny horizontal splitting.

The empirical PR #71 zero geometry is also meaningful. One zero is very close below the exact sampled height and the next reported zero is far above it. Under the proposed Pick Gram representation, that makes one resolvent vector unusually dominant. Exact complex directions can annihilate the dominant low-rank response, while high-order moments suppress remote terms, leaving a tiny positive tail. This explains the precision ghosts without suggesting an off-line zero.

## Refutations and scope corrections

### Counting is not unique

Smooth even statistics such as `eta^2` distinguish every nonzero displacement. Adaptive smooth families can retain order-one response at an arbitrarily small target scale. Parity therefore controls conditioning of a fixed statistic; it does not prove that all smooth methods are blind.

### Sign changes are not a zero count with multiplicity

A double zero on the critical line contributes multiplicity two but no sign change. Hence a deficit between a Turing total count and sampled Hardy-Z sign changes does not prove RH false.

The correct finite witness is

```text
N(a,b) - N0(a,b) > 0,
```

where both counts include multiplicity.

### Local zero geometry does not determine a global Pick form

Even a rigorous proof that every zero in `[T-H,T+H]` lies on the line controls only a local block of the Hadamard/Gram representation. A direct outward Pick contraction or a proved global tail decomposition remains necessary.

## Exact input defect

The PR #71 input is

```text
20225875608341108140435 / 2^32
= 4709203636353.16214999998919665813446044921875.
```

X-5602 instead parses the nearest binary64 value

```text
4709203636353.162109375.
```

The exact shift is

```text
174483 / 2^32
= 0.00004062498919665813446044921875.
```

The binary64 ulp at this height is `1/1024`. The committed absolute zero ordinates are produced by binary64 addition and lie on that grid. They therefore cannot encode the stated `~1e-9` absolute refinement. This does not refute the large gap; it narrows the claim to the precision actually retained.

## New proof units

- `R-5602`: scope correction for parity, counting exclusivity, sign changes, local closure, and exact input.
- `L-5605`: exact total-minus-line zero-slab discrepancy criterion.
- `L-5606`: dominant-rank Gram conditioning lemma.
- `X-5603`: standard-library exact provenance audit, retained output, tests, a FLINT Platt/Turing consecutive-zero producer, and precision nesting checker.

## Verification performed

```text
2 exact standard-library tests pass
retained JSON regenerates byte-for-byte
compile checks pass
```

FLINT was not available locally. The package gateway failed, and the new GitHub workflow had not exposed an execution when this report was written. No FLINT output is claimed.

## Correct offensive target

A large line-zero gap becomes a counterexample only if an independent total-zero count proves that the corresponding full critical-strip slab contains a zero while the critical line is empty there. The branch therefore calls FLINT's `acb_dirichlet_platt_zeta_zeros` at the exact dyadic target and asks for consecutive total-zero balls.

If the returned total zeros bracket the target consecutively, the local gap is certified empty of all zeros. If a total zero is found inside a rigorously line-empty interval, `L-5605` gives an unconditional RH counterexample.

## Candidate status

None.

The referenced commit is promising as a **nomination and conditioning diagnostic**, not as a current counterexample. The most load-bearing claims attached to its smooth census require the scope corrections above.
