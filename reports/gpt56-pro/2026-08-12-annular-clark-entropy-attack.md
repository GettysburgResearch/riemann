# Annular Clark-entropy attack

Date: 2026-08-12  
Base: PR #419 at `1bba24ab1cadc7ca4529d6e345ed2be1afd71b07`  
RH status: **unproved**

## Motivation

The one-node route had already replaced the crossed-zero obstruction by an
additive logarithmic Green mass.  The remaining mismatch was conceptual: the
arithmetic route was being described by source innovations and returned-state
norms, while the model obstruction was a logarithm of a Blaschke factor.

The present pass identifies the model logarithm as the same Clark-resolvent
entropy that appears in the prime Julia cascade.

## Exact advances

1. Every crossed zero has an explicit scalar Julia defect at the fixed node.
2. Its Green charge is the exact resolvent-integrated entropy of that defect.
3. The complete annular log mass is the sum of these positive charges.
4. The log mass is also an exact resolvent average of the one-node hyperbolic
   port.
5. Approximate source exhaustion now gives explicit depth-height zero-free
   boxes through a quantitative Green moat.

## Quantitative moat

For a crossed zero `x+iy`,

```text
g_eta(x+iy)
 >= 4 eta x / [ (eta+x)^2 + y^2 ].
```

At zeta depth `x>=delta`, height offset `|y|<=Y`, this is uniformly at least

```text
4 eta delta / [ (eta+1/2)^2 + Y^2 ].
```

Thus a certified source/model entropy mismatch below this number excludes the
entire box.

## Hostile correction

A scalar entropy equality is not a source-identification theorem.  Positive
mass may be redistributed between an undeclared stable output and a hidden
hyperbolic output.  Even the full scalar resolvent curve depends only on one
number and does not restore provenance.

The factorization must be common and source ordered.

## New final target

`CEAE_j` asks for one multiplicative source-to-model factorization per dyadic
annulus,

```text
arithmetic entropy
 = critical entropy
 + stable entropy
 + annular Blaschke entropy
 + auxiliary entropy,
```

followed by exact or cofinal exhaustion by the first two outputs.

The route is now naturally compatible with the additive prime Clark generator
of sibling `L-91610`.
