# Independent review of support pruning and its finite checker

Reviewer: `gauss_analytic`, independently of the root agent who authored the reviewed pruning note and checker.

| Reviewed file | SHA256 |
|---|---|
| `RAMANUJAN_SUPPORT_PRUNING.md` | `9a019b2253a0f35ade96455bf5d249cd1ca09285c4f2d7e17c475b5b5522c3ea` |
| `checks/check_support_algebra.py` | `568717cd7108be21b1f01361645e2bf0e42c6c5d906df0e368c3baf10ef724d1` |

Verdict: **PASS at the stated scopes.** The mathematical pruning result is conditional on the exact theta inputs and all-cusp adapter named in the packet. The checker verifies only its explicit finite algebraic cases; it does not certify those analytic inputs or any infinite moment theorem.

## Analytic and arithmetic review

I independently read the complete pruning note and reconstructed both applications of its support theorem. The signed identity over `a=dg` retains every Ramanujan allocation. The `e,f` splitting is exactly the unique assignment of a positive-divisibility prime to the squarefree theta index when possible and to the cube index otherwise. No negative-prime coprimality mask is introduced.

For the standard face, `phi_(k,d)` is an actual periodic Fourier multiplier modulo `Mkd`, including the good-primary selection and all k zeros. The coefficient identity is `S^+=81i I`, and its raw scale is `(Na)^2(Nk)^2/(27cB)`. Substitution into `X>3R(Nq)^2` yields exactly the displayed standard constant `81cR(NM)^2`. The full cube and squarefree sums, rather than separate dyads, are required for this cancellation.

For every source cusp, the geometric adapter uses the original reduced translation denominator `c_1|q`; it does not substitute the denominator of `gamma_sigma(beta)`. The raw scale `(Nc_0)^2(Nk)^2(Na)^2/B` therefore yields the factor `3R(NM)^2/(Nc_0)^2` in Section 5. The different constants 81 and 3 express the change from `Nn(Nb)^3` to `Nell=Nn(Nb)^3/27`; no factor 27 is missing or repeated.

The normalized Fourier table is exact: a constant -1 transforms to -1 at zero frequency only, while `q*delta_0` transforms to 1 everywhere. Reuniting the two leaves `1_(h!=0)`, restoring local activity at every original divisor prime. Thus the note correctly refuses to infer a smaller conductor for the reunited whole or a fourth-moment theorem.

## One independent checker run

Executed once:

`python standalone/2026-10-10-theta-support-descent/checks/check_support_algebra.py`

The run returned `PASS`, with these counts:

| Finite coverage | Count |
|---|---:|
| Primitive columns in the specified coordinate box | 450 |
| Matrix constructions over the three original cusps | 1,350 |
| Cases where the transformed denominator norm differs | 808 |
| Cases where the transformed denominator is zero | 12 |
| Ramanujan divisor identities | 1,554 |
| Positive-projection identities | 22,620 |
| Exact finite-field Fourier equalities | 192 |
| Rational scale cases | 96 |

The box is exactly `a,c in {-2,-1,0,1,2}^2` in the Eisenstein basis, with `c!=0` and unit gcd, followed by the three specified cusp matrices. The determinant, congruence, original first column, original denominator norm, and target cusp class are checked in every retained case. All construction cases and all target cusps occur. As an independent count check, there are 600 candidate nonzero-denominator pairs. Their only possible common prime factors have norms 3, 4 or 7 in this box. Inclusion-exclusion gives `72+72+6+6-6=150` nonprimitive pairs, leaving 450.

The divisor count is `sum_(s=1)^4 6^s=1554`; each additional divisor-allocation choice doubles the per-prime cases, giving `sum_(s=1)^4 12^s=22620` projection checks. The Fourier cases use residue fields of sizes 7, 13, 19 and 25; three identities per frequency give `3*(7+13+19+25)=192`. For size 25 the code implements the Eisenstein quotient over F_5, whose quadratic polynomial is irreducible, and uses its trace `2a-b`. It reduces integer coefficient polynomials modulo the exact prime cyclotomic polynomial, so no floating-point Gauss-sum tolerance is involved. The 96 scale cases use exact rational arithmetic with abstract positive norm variables; they are algebraic substitutions, not a claim that every sampled integer is an actual Eisenstein ideal norm.

The returned negative-mask example and the constant guards exhibit explicit failed alternative formulas. They should be described as such, not as a separate mutation-testing campaign. No extra optional tests were run for this review.

## Limits

The integer matrix computation is a finite diagnostic of the proven construction. The all-input matrix statement is supported by the CRT proof, not by extrapolation from the coordinate box. Likewise the finite local-field checks support their stated algebra but do not authenticate imported theta coefficients, Mellin continuation, contour shifts, infinite moments, or zero-free regions. These boundaries are correctly retained in the checker output and the pruning note.
