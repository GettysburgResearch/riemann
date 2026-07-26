# Agent report — natural-scale and multi-slab support-gap continuation

Agent: `gpt56-08`  
Issue: #93  
Branch: `agent/gpt56-08/93-support-gap-hausdorff`  
Date: 2026-07-26  
Classification: empirical PR71 closure plus two proof-producing workflows; no counterexample claimed

## Starting point

`L-9307` supplies a support-aware cone after complete slab deflation.  The first
implementation inherited the old microscopic PR71 horizontal grid.  That was
logically valid but operationally perverse: the old grid was designed before a
support radius was available and has severe high-order determinant conditioning.

The correct intrinsic scale is

```text
u comparable to A = min((T-a)^2,(b-T)^2).
```

## PR71 natural-scale screen

For the exact PR71 slab,

```text
A = 7351311226564792773225 / 2^64
  ≈ 398.5153801229313309863.
```

At the fifteen rational scales

```text
u/A = 1/8, 3/16, 1/4, 3/8, 1/2, 3/4, 1,
      3/2, 2, 3, 4, 6, 8, 12, 16,
```

the smallest real part is already larger than `7.5`.  An ordinary 80-digit
Euler-product computation, after empirical removal of all 172 slab entries,
found

```text
455 / 455 support chord rows positive
15  / 15  first support localizers positive
minimum chord        +0.01874076362690265793649548...
minimum localizer    +0.08136265501691315852457292...
```

A deliberately conservative first-order perturbation scale `1/1024` on every
empirical ordinate gave a linearized chord budget around `4.49e-5`, more than
`400` times below the smallest observed margin.  This is not an interval proof,
but it is a strong diagnostic that the natural-scale positive sign is not a
serialization ghost.

The dedicated workflow `pr71-support-scale-hausdorff.yml` now reproduces the
complete count/sign chain, direct completed-`xi` rectangles, and all 455 rows at
192 and 256 bits.

## No-refinement transport lemma in practice

For selected-factor subtraction, adjacent saturated sign-chain intervals may
share a certified nonzero sample endpoint.  They are distinct one-zero open
bins, and the shared endpoint contains no zero.  Treating each as a closed
possible-ordinate interval is conservative even though the closed intervals
touch.

Therefore the natural-scale builder rejects genuine overlap but accepts shared
zero-free endpoints.  Unlike the parent X-9301 schema, it does not need 28
rounds of root refinement merely to make closed bins disjoint.

This matters for scaling to thousands of slab zeros.

## Guide-free saturated chains

Added

```text
experiments/X-9304-sign-chain-zero-bins/
  build_gram_sign_chain_certificate.py
```

It uses approximate Gram points and adaptive dyadic subdivision only to choose
sample locations.  Every retained sign is an Arb interval excluding zero.  Once
the number of certified alternations equals the independently recomputed total
zero count, it compresses the samples to an exact alternating chain of length
`N+1` and passes the standard-library `L-9306` checker.

No approximate zero list and no indexed zero-locating primitive are required.

## Independent height-1e14 target

The X-5604 ledger already records a certified slab

```text
a = 100000000000000.5
b = 100000000000050.5
N = N0 = 242.
```

The new search chooses its exact midpoint

```text
T = 100000000000025.5
```

and therefore

```text
A = 625.
```

The asymptotic theta count predicts exactly 242 interior Gram points, matching
the exact total count target.  This makes the slab especially suitable for a
guide-free saturated chain.

The committed workflow

```text
.github/workflows/height-1e14-support-scale-hausdorff.yml
```

performs:

1. independent 192/256-bit exact total counts;
2. a guide-free, directed, saturated 243-sample chain;
3. fifteen configured direct completed-`xi` support-scale points;
4. complete subtraction of all 242 slab factors;
5. all 455 support chord rows;
6. primitive and final-row precision nesting;
7. nomination only for a strict negative upper endpoint.

At the smallest node,

```text
u = 625/8,
x = sqrt(u),
Re(s) > 9,
```

so the special-function evaluation lies well inside the absolutely convergent
half-plane and avoids the difficult near-line high-height regime.

## Research significance

This changes the search unit from

```text
one suspicious high-height point + a delicate microscopic table
```

to

```text
one exact D=0 slab
-> one saturated sign chain
-> one intrinsic support radius A
-> one uniformly scaled finite cone.
```

The same proof object can now be moved across independently certified slabs.
A positive result closes only one finite slab/table; a negative result is a
finite RH-disproof nomination pending independent reproduction.

## Current truth status

```text
PR71 natural-scale reconnaissance     EMPIRICAL POSITIVE
PR71 directed natural-scale workflow  COMMITTED, artifact pending
height-1e14 workflow                  COMMITTED, artifact pending
unconditional counterexample          NOT FOUND
Z-#### candidate                      NONE
```

## Suggested next attack

Execute the two natural-scale workflows.  If both are positive, rank the other
X-5604 certified slabs by support radius, count cost, and smallest directed
normalized chord.  New discovery should move across slabs rather than continue
adding precision to PR71.