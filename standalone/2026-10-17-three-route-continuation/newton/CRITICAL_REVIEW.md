# Cross-review: principal diagonal finite part

Reviewer: the separate `native_critical` agent. Date: 17 October 2026.

Disposition: **no correctness defect found in the stated component theorem**.
The factorization, diagonal nonvanishing, and renormalized finite-part
identity are supported by the written argument and the checks below. This
review does not establish the missing signed physical projection estimate,
an RH result, or the full source paper's Poisson theorem.

## Exact reviewed files

- `research_work/critical/DIAGONAL_FINITE_PART.md`, SHA-256
  `38e47a053c78d54349ea1e623d008ce6db1e78e5853862c60936db64201fb8d9`.
- `research_work/critical/verify_diagonal.py`, SHA-256
  `7c474148354e8acfd43ba624661bfb8ac3d478be290e9cefc5341b603662d185`.

The review is of these file contents before publication; no frozen remote
commit for the new packet was supplied. A change to a load-bearing formula
requires a corresponding review update.

## Independent source check

I independently fetched both declared sources through GitHub:

- PR #962 at `b2032c663736ecd1e3872559d160ce069664ea06`,
  `PRINCIPAL_TWO_VARIABLE_FACTOR.md`; returned blob
  `77389da2603732d9bd51ba50f6711025ff3a2c88`.
- OpenAI/math at `1581d4cbdd69a0faf34b2089614fe2a814316a6a`,
  `preprints/Primitive-roots-for-every-admissible-integer-base-October-4-2026/build/sections/05-poisson.tex`;
  returned blob `c8526f74b281d37fda034c17195c4bb5afd5f79b`.

The primary formula `eq:Euler-good-exact`, its preceding definitions, and
the definition of the local correction reproduce equation (1) exactly
after specializing the source's TARGET character and Poisson row to the
principal cases. The note's distinct ANGULAR character notation is
explicitly distinguished. At `z=1/2`, `V=Q^(-3)` and
`E=eta(p) Q D^6` are correct.

The primary global arithmetic prefactor is
`zeta_F^S(6z) zeta_F^S(w) H_1 / zeta_F^S(xi)` in that specialization.
Removing the fixed nonzero factor `zeta_F^S(3)` therefore gives exactly
the note's `A(xi,w)`. The physical monomial in equation (23) also matches
the primary Mellin formula, including the vanishing exponent of `X` and
the remaining `Y^v`.

## Mathematical findings

1. **Euler extraction is correct.** I checked the cleared numerator,
   its remainder after subtracting `H_p^0`, and the cancellation
   `(1-DW) H_p^0 - 1 = D^2 W(1-W)/(1-D)`.
   The resulting prime exponents in (10) are all strictly summable on
   fixed margins of `Re xi>1/3`, `Re w>0`, `2 Re xi+Re w>1`.
   Both denominators remain separated from zero. The derivative in `w`
   adds only logarithms, so the claimed holomorphy of `K` and `k1` follows.

2. **The diagonal has no local cancellation under the stated norm
   condition.** Substituting `DW=r` gives equation (11) exactly. The
   baseline lower bound `3/4` and the perturbation bound `317/1215`
   are valid for `Q>=3`; their strict difference is `2377/4860`.
   This proves every local factor is nonzero. Normal convergence gives
   a nonzero product. Uniform tail bounds and the same small-prime margin
   establish the claimed bounds for `k0` and its inverse on closed
   vertical substrips. The finite exterior-prime condition is explicit.

3. **The functional-equation normalization is correct.** For
   `Zeta(s)=E_S(s) zeta_F(s)`, the ratio in (16) has the correct orientation.
   Its gamma factors and all fixed finite-S factors are holomorphic and
   nonzero in the open strip. No zeta-zero-free assumption is used.

4. **The finite-part sign and multiplicities are correct.** Expanding
   (17) first at generic `xi` gives equation (21). Differentiating
   `Zeta(1-xi)=B_S(xi) Zeta(xi)` produces the minus sign in (22).
   Substitution gives (19), and at a zero of multiplicity `m` the
   renormalized finite part has residue `-m`. The unnormalized residue
   in (20) follows because its multiplier is holomorphic and nonzero.
   The note correctly declares these as meromorphic coefficient
   identities in `xi`: one should not first substitute a zero into
   the unexpanded two-variable quotient. This distinction is already
   covered by the current wording.

5. **The projection boundary is preserved.** Multiplication by `Y^v`
   adds `+log(Y)` times the normal residue. A further Mellin factor adds
   its transverse derivative times that residue, and a zero of its
   leading value can destroy a particular detector. The note retains
   this qualification and does not interchange a finite part, a physical
   integral, or an unestimated tail. The bare residue being holomorphic
   provides no signed upper bound for the first finite part.

## Replay and remaining obligations

Ran `python3 research_work/critical/verify_diagonal.py`: **PASS**.
I inspected the Laurent-polynomial implementation; its accepted identities
use exact rational coefficients, with no floating-point margin.

The replay checks algebraic identities and the strict rational margin.
It does not independently derive the primary finite local Gauss-sum
formula or authenticate the full physical Poisson expansion. My source
check verifies the declared specialization against that exact imported
formula. The analytic convergence and finite-part conclusions above were
reviewed mathematically, rather than inferred from the script's output.

No blocking change is requested. The remaining research obligation is
exactly the one stated in the note: a native signed estimate for the
first transverse finite part after its actual physical weights,
projections, and tails have been justified.
