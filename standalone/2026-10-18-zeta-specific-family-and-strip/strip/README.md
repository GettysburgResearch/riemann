# Strip-confined models for the original xi function

Read [PROOF.md](PROOF.md) for the statements and complete arguments.

The main native results are:

1. **Elementary-product obstruction.** Finite products of symmetric
   three-point cosine factors, even with Gaussian factors and unrestricted
   parameters, cannot converge locally uniformly on the whole plane to
   normalized xi. A zero-persistence argument would force a full arithmetic
   progression of critical-line zeta zeros, contradicting Li--Radziwill.
2. **A larger admissible model class.** A ferromagnetic Ising observable with
   `|h_i| <= b w_i` has its Fourier zeros in `|Im z| <= b`. If its zero-field
   reference variance is V0, its entire characteristic function is bounded by
   `exp(V0 (b+|Im z|)^2/2)`. This proves a direct compactness theorem for these
   strip models.
3. **A conditional all-order route.** Cofinal theta moment matching inside
   that class, with fixed b and uniformly bounded V0, gives the zeta boundary
   `Re s <= 1/2+b`. The cofinal construction remains open.
4. **A finite source-bound example.** An 18-spin model has the original theta
   moments 2 and 4, reference variance below 1/20, and genuinely nonreal Fourier
   zeros with imaginary height strictly between 0.30 and 0.31. Its field/weight
   cap is below 1/3 in the original xi coordinate.
5. **A source-qualified local continuation.** Assuming the proposed T20D
   theorem and invertible Jacobian of PR #994, opposite small fields on two
   identical leaves admit an analytic retuning preserving theta moments
   through degree 20. No explicit continuation radius or higher order is
   claimed.

These are proposed results for independent review. They establish neither a
new unconditional zeta strip nor RH.

## Run the finite checker

In the repository, from this directory:

```bash
python check_strip.py
```

The default source directory is the sibling inherited packet
`../../2026-10-18-theta20-and-native-cancellation/theta/`. The source is bound to
PR #994 at commit `c93ca65a510b6acaf167f929b9bf7e67d742b05a` by exact Git blob
identities, verified before importing its modules:

| File | Required Git blob |
|---|---|
| `pr886_primitive.py` | `c32015f110d10186538ffabcb4689ba5bbc060d0` |
| `theta_source.py` | `fc51d49fe2bdbbde3fcb3928f1d82fd8baffbf53` |

For a different checkout layout, pass the exact source directory explicitly:

```bash
python check_strip.py --source /path/to/exact/theta
```

The run reconstructs every required theta constant from the primitive, writes
`theta_source_replay.json`, checks strict directed inequalities, verifies the
dimer Gibbs identity by all four configurations, and independently compares
all 32 spin correlations of a five-spin tree to all 16 high-temperature edge
subsets. It writes [certificate.json](certificate.json).

The primitive is the same 320-bit outward integer backend as the inherited
packet. This is a fresh primitive replay, **not** a second independent
transcendental implementation. The source also reconstructs moments through 20
because that is its frozen interface; only moments 2 and 4 are used in the new
finite example. Moment-interval overlap is a diagnostic; the exact algebraic
formula in PROOF.md proves the two claimed moment equalities.

The analytic all-order theorems and the conditional degree-20 continuation are
not established by the finite checker.
