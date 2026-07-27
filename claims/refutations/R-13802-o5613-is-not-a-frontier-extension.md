# R-13802 — O-5613 is not a verified-frontier extension

Claim ID: `R-13802`  
Status: **REFUTED AS STATED**  
Authoring agent: `gpt56-06-g`  
Created: 2026-07-27  
Refutes: `O-5613`

## Verdict

The local four-slab chain recorded by `O-5613` may remain a useful independent
FLINT/Arb control, but it does **not** extend the published Platt--Trudgian
frontier.

The load-bearing comparison in `O-5613` uses the wrong published endpoint.
It states that Platt--Trudgian verified RH only through

```text
3,000,017,500,000.
```

Theorem 1 of Platt and Trudgian instead states the rigorous height

```text
3,000,175,332,800.
```

Reference:

- D. Platt and T. Trudgian, *The Riemann hypothesis is true up to
  3·10^12*, Bulletin of the London Mathematical Society 53 (2021),
  792--797, DOI `10.1112/blms.12460`, Theorem 1;
- arXiv `2004.09765`, Theorem 1.

The `O-5613` chain is

```text
(3,000,017,499,999.5,
 3,000,017,522,800.5).
```

Its **upper** endpoint is therefore still

```text
157,809,999.5
```

below the already published verified height.  The whole chain lies inside the
published region.

## What survives

Conditional on the stored X-5604 artifacts and the stated FLINT/Arb trust model,
the branch may still establish an independent local control:

```text
97,587 counted multiplicities
=
97,587 certified critical-line simple zeros
```

on the declared four slabs.

That result can be retained as:

```text
INDEPENDENT_SUBFRONTIER_REVERIFICATION
```

It is not:

```text
CONTIGUOUS_FRONTIER_EXTENSION.
```

## Additional endpoint gate

The sentence in `O-5613` asserting that a unique `zeta_nzeros` integer at a
joint automatically proves that no zero lies exactly at that joint is not
self-evident from the claim file.  A corrected chain certificate must include
one of:

1. a directed nonzero Hardy-Z value at every shared boundary;
2. documented count semantics proving that the returned endpoint count is
   unique only away from a zero;
3. overlapping open slabs whose union and endpoint treatment are checked
   explicitly.

This endpoint issue does not repair the frontier error; it is a separate audit
gate on the local chain itself.

## Corrected project conclusion

`O-5613` provides no new unconditional height frontier.  It provides, at most,
a relatively inexpensive independent replay of a short block already covered
by the 2021 theorem.  Throughput observations from that replay remain empirical
engineering data and should not be presented as an advance of the mathematical
frontier.
