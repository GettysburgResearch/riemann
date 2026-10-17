# Verification, source boundaries and exact publication scope

Status: proposed mathematics; independent mathematical review required.
The proofs and this checker have the same author. No Lean build, external
referee report, full-repository validator or remote CI result is claimed.

## What was actually executed

From this directory:

```sh
python verify.py > normal.json
python -O verify.py > optimized.json
cmp normal.json CHECKS.json
cmp optimized.json CHECKS.json
python run_mutations.py > mutated.json
cmp mutated.json MUTATIONS.json
python verify_manifest.py
```

All these commands were executed successfully after the final mathematical
payload was frozen. Both checker outputs equal CHECKS.json byte for byte.
The eight separately executed corrupted optimized processes reproduce
MUTATIONS.json. The scripts syntax-compile. A fresh ZIP-extraction replay
also runs the manifest, both checker modes and the mutation processes; the
outer publication receipt records its result. Output files from the above
illustrative commands are not members of this sealed packet.

The total is **12,040 finite predicates including repeated setup/guards**.
The per-group counts are in CHECKS.json. In particular 4,224 checks concern
full-strip conductor exponents and 2,816 check the dual-conductor identity.
They are not that many independent analytic cases, and none is a numerical
measurement of an L-value, zero, physical theta value or infinite moment.

## Primitive and finite coverage

1. The quadratic test uses all odd squarefree rational integers in each of
   22 stated column dyads: C=2,4,8 at orders k=1,...,6 and C=16 at k=1,...,4.
   Each coefficient is mu(c)/c, hence at most 1/sqrt(c) in modulus. Every
   odd squarefree row d<=31 occurs. An explicit ordered-product expansion
   is compared with iterative convolution before stripping squares. There
   are 325 distinct product columns counted across these cases. These are
   actual rational Jacobi-symbol examples, not a number-field theta census.

2. Square stripping retains v=e*r^2 with shared primes and the literal
   factor 1_((d,r)=1). Unit columns do not erase the nonunit mask. Tests
   reject both erasing that mask and imposing the false condition (e,r)=1.

3. Sextic tests use exact Z[zeta_6] arithmetic at the rational primes 7 and
   13, with primitive generators 3 and 2 respectively. Complete integer row
   caps 64,128,256 are used with the FOUR named columns 1,7,13,91, at orders
   2,4,6,8. All rows at those caps are present; the columns are a fixed
   two-prime fixture, NOT all ideals under a norm bound. Row regrouping
   u=a*b^6 and its original zero extension are compared exactly. Additional
   large sixth-power rows and local masks are stated explicitly by the code.

4. All integers through 512 are tested for the unique powerful/squarefree
   factorization. Rational exponent identities include the powerful-part
   tail at fixed orders, the fourth-theta-moment example N=Z^(2/3), and the
   all-order support thresholds. The proof, not those finitely many orders,
   establishes Theorem T for every fixed k.

5. Numerator exponent tests run through r=16 and a stated finite rational
   grid of sigma and actual conductor scales. They retain the negative
   conductor factor and both AFE endpoints. The asymmetric-AFE comparison
   and finite-anchor calculations are exact rational identities. The
   complete arguments in NUMERATOR_HIERARCHY.md establish their all-order
   scope; no optimizer or finite grid is promoted to an infinite theorem.

6. The subunit-tail tests concern an exact geometric majorant model. They
   do not evaluate CT's profiles or certify a transcendental tail. The
   all-tail estimates in THETA_ALL_MOMENTS.md are written analytic proofs
   conditional only on the explicitly named imported profile/reflection
   interfaces. The 121 optimistic-budget checks support an algebraic dual
   identity whose proof is supplied separately; 8/9 is NOT asserted as a
   new zero-free theorem.

## Actually executed negative controls

Eight corrupted copies of the finite model are separately run with python -O:

- dropped quadratic square mask;
- an invented coprimality condition between square kernel and squarefree part;
- collapsed product-column length;
- omitted sixth-power row copies;
- replacing an actual negative conductor power by a power of the larger cutoff;
- omitted Holder support cost;
- a falsely diagonal critical numerator anchor;
- deletion of a nonempty subunit profile tail.

Each process fails at its intended explicit gate. There are no assertions
whose removal by -O would silently turn failure into success. These are
local finite-model mutation controls, not a proof-assistant kernel or a
complete adversarial proof search.

## Source and review boundary

Goldmakher--Louvel Theorem 1.1/Corollary 1.2 were freshly inspected in the
primary PDF, including its rendered theorem page. De Faveri's Theorem 1.1,
character construction and complete-index conventions were freshly read in
primary HTML. BGL's AFE/zero-detector page was freshly rendered and inspected.
The deep proofs of those inputs were not reconstructed in their entirety.

Fresh access to CT v2 failed in this session. The full source-faithful
reflection and local majorants are adopted from the byte-pinned, previously
delivered REFLECTED_MOMENT.md, whose complete text was read. Its identification
with CT's actual metaplectic source remains a load-bearing analytic import.
The new proof reconstructs the powering, square-removal and infinite-tail
steps above that interface, not the metaplectic theory below it.

The #974 principal finite-part proof was read live at its exact pinned head.
Its -zeta'/zeta identity is credited, not rebranded as a new estimate. No
bound for its signed physical projection was supplied by this pass.

Specific review priorities are: the exact CT quadratic-family identification;
the mask-preserving powering lemma; the full n tail before the ramified sums;
fixed-order dependence of the beta mass; the actual-conductor AFE and finite-
vector interpolation; and the distinction between native and theta moments.
An analytic import or adapter error would invalidate its dependent theorem
regardless of every finite predicate passing.

## Recovery versus new mathematics

The preceding eighth-moment packet is preserved byte-for-byte under the
separate archive recovery directory. Its original manifest and complete
normal/optimized checker were freshly replayed, matching the archived 9,959
predicates. Its historical mutation-generation report was not newly produced.
The recovery does not approve the proposed 163/180 composition. Historical
NOT PUSHED labels are preserved and superseded only by the new recovery
receipt. No old proof, main or integrated scientific status is overwritten.

This new packet contains an all-even THETA theorem, a full-strip NUMERATOR
hierarchy and a noncritical all-even NATIVE upper theorem. The cofinal native
estimate OPEN-N is still unproved. Neither a fixed-order support exponent
approaching 1/2 nor the optimistic-budget number 8/9 is a new zeta boundary.
