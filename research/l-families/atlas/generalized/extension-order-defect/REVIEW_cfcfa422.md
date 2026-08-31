# Independent review of general before-source radii and invariant bases

Reviewed freeze: `cfcfa42264a4ce5fc5846ac468c0c51c4cab9267`.
Reviewer: `/root/recent_landscape`, separate from the author.
Conclusion: **no blocker found in the stated mathematical or replay scope**.

I independently read both full proofs, the complete producer and all 28 tests,
then checked the final dependency pins and a clean path-restricted diff against
this freeze. I inspected artifact identity, counts and scope metadata, without
rerunning the 3044-row classification or any test. Exact Git identities are:

| file | blob |
|---|---|
| `GENERAL_FIELD_RAMIFICATION_EXPONENT.md` | `19ad8ad62254cd3e1d92c52aadce9cbba9b3635a` |
| `INVARIANT_GENERATOR_BASE.md` | `9174c003f6ab9c04d3ab4aa02afda45e28b96ad9` |
| `general_replay.py` | `fc5d6c11b381d7bf8af45ec8ff0b525d3586502f` |
| `general.verification.json` | `7be016bb78cc14c6ecc059549271a9a0c7c17b13` |
| `tests/test_extension_order_general.py` | `b381135a79ade1a88ced41d49c976e67dce8f2ed` |

The before-source proof retains both finite-source zero orders and the signed
old-branch correction. A leading integer exponent does not suffice when the
positive square-root term is present. In the removable first-circle case,
the nonsplit-infinity `-1/6` term cannot be canceled by the actual after-source
quarter lattice and degree-two old-branch quarter contributions. This gives
the exact second radius. The restoration of full bad factors and finite
arithmetic cancellation precedes the holomorphy claim; the ratio's isolated
denominators are not treated as new source poles.

The general invariant-base result uses a commutative connected graded algebra,
a grading-preserving finite-group action and characteristic zero. Augmentation
and dimension show that the original fixed-input base cannot give finiteness
when the added generator representation has nontrivial inertia. The full
invariant-generator base repairs finiteness by orbit integrality and Reynolds
projection. The concrete Segre refinement correctly distinguishes finite from
free: the repaired module has rank two but four minimal generators, in degrees
`0,3,3,3`. The original cokernel is explicitly **not** a module over the enlarged
base. The C3 normal-form relation and nonsplit swapped-monomial trace were also
checked; trace is not substituted for dimension.

The producer authenticates the frozen AFTER proof, code and artifact, the
infinite comparison proof and the finite comparison proof before executable
import. It reads all 3044 bound source rows but independently recounts only the
seven declared examples. Its artifact uses `general-before-extension-radius-v1`,
records 2647 first-radius and 397 second-radius rows, and 849 extension-order
changes. Those are finite atlas checks, not the all-grade proof. Hypothetical
second-circle sign patterns are labeled as such. Typed JSON-tree comparison
rejects numeric coercions, nonfinite numbers and non-JSON containers.

Root reports Ruff, ordinary write/check, optimized check, and **28 ordinary plus
28 optimized tests passed**. These are coordinator-reported runs; this reviewer
performed no scientific computation. Remaining limitations are explicit:
no ordinary boundary-cokernel determinant identity, no larger ordinary
trace-class domain, and no number-field/archimedean or full RH transfer.
The smallest invalidator would be a wrong generization/invariant-base map or
an omitted finite-source zero/Puiseux term; matching finite counts would not
repair either.
