# T-102960 — Independent disposition of the minimum-owner Boolean Vaughan proposal

Claim ID: `T-102960`  
Status: **MAJOR UNCONDITIONAL SALVAGE; FULL COMPOSITION UNPROVED**  
Created: 2026-08-25  
Reviewed target: PR #751 at `8743ba4230097c296dee1dec40d09b59cdf56599`  
RH status: **unproved**

PR #751 proposes a complete RH proof through squarefree Boolean Vaughan,
minimum-owner selection and the parent coherent phase theorem. The proposal
contains real new arithmetic structure. Independent reconstruction gives the
following exact disposition.

## 1. Verified components

The following statements survive:

```text
Boolean disjoint-support convolution is associative;
mu_sf star 1_sf = epsilon;
the Boolean Vaughan identity is coefficient-exact;
a_U vanishes on every squarefree 1<=n<=U;
every balanced Boolean atom contains at least two distinct core primes;
the squarefree lattice reindexing is exact;
the minimum-owner horizon rule is source-defined and horizon-safe;
lambda^2 <= a on every balanced core;
L^2 < 2B after the linear dyadic projection;
the same-family off-diagonal centered-kernel identity is exact.
```

`L-102951` further proves that this Boolean source is exactly the unique
critical Hodge class modulo the already-closed squared ideal.

## 2. The first source transport is repaired

`L-102953` proves that the squarefree Type-I lattice is an `l1`-bounded sum of
square shifts of the parent zero-moment lattice. Thus the first load-bearing
review target of `M-106080` is closed:

```text
Boolean squarefree Type-I
  -> parent Type-I source/Hilbert ledger
```

is exact and power-saving.

## 3. First broken/open arrow

The remaining proposed step is

\[
\text{same-family scalar kernel plus }L^2<2B
\Longrightarrow
\text{physical owner-indexed coherent bound}.
\]

`R-102875` proves that this implication is not automatic. Retaining owner
labels orthogonally deletes the physical cross-owner terms; collapsing them
first makes the additive phase depend on the owner product and no longer on one
scalar core sequence. The submitted `L-106082` does not construct the common
operator which resolves this noncommutation.

Define the exact missing theorem:

```text
OICP102960:
  on every minimum-owner Boolean block, the literal owner-indexed centered
  phase packet maps to the physical distinct-product observation with
  subpower norm/negative mass, with every selected-owner and co-owner weight
  used once.
```

`L-102954` proves

\[
\boxed{
\mathrm{OICP}_{102960}
\Longrightarrow
\mathrm{HMO}_{102940}
\Longrightarrow
\mathrm{RH}.
}
\]

## 4. Verdict vocabulary

```text
L-106080 Boolean identity/local Type-I algebra      VERIFIED
L-106081 minimum-owner geometry                     VERIFIED
L-106082.2 same-family centered identity            VERIFIED
Boolean Type-I global transport                     VERIFIED WITH REPAIR
L-106082.3--.5 literal physical owner transport     UNPROVEN / GAP
T-106080 complete proof proposal                    UNPROVEN / GAP
Riemann Hypothesis                                  UNPROVED
```

Mathematical types:

```text
Boolean/Hodge identification        UNCONDITIONAL THEOREM
minimum-owner geometry              UNCONDITIONAL THEOREM
OICP102960                          RH-EQUIVALENT MIDDLE CRITERION
T-106080                            PROPOSED COMPLETE THEOREM
```

The proposal is not refuted. The first open arrow is now exactly named and
strictly narrower than the pre-PR-751 short-core frontier.

## 5. Research implication

The correct next attack is not another owner rule. It is an owner-indexed
centered large-sieve/restriction theorem which simultaneously retains:

```text
the universal Boolean core coefficient;
the distinguished and co-owner weights;
owner-dependent nonzero phases;
all-chaos carrier recombination;
physical cross-owner collapse.
```

Any proof of that one operator theorem completes the current fixed-detector
chain.
