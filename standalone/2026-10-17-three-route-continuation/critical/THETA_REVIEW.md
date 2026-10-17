# Review of the proposed 9081/10000 theta comparison

Status: source-qualified review of the new composition. No defect was found in the new interpolation-to-contour adapter, the displayed scale exponents, the finite density partition, the contour regions, or the loss ordering, assuming the explicitly stated imported analytic interfaces. This is not a recertification of the CT metaplectic foundation, the BGL actual-family mean, the de Faveri density theorem, or the complete proof of PR #965.

Reviewer scope: the reviewer derived and authored the separate interpolation component, so this report is NOT an independent review of that component itself. It is an independent review and independently coded exponent replay of the new theta comparison, including how that component is applied. A separate reviewer must assess the interpolation proof before the composed statement is approved.

## 1. Frozen files reviewed

| File | SHA-256 at review |
|---|---|
| `research_work/theta/THETA_COMPARISON.md` | `8b9aaed9e48a596d7cb9f71bef72a93928d8efa83866a599d83179684f478201` |
| `research_work/theta/verify_theta.py` | `d2c77035fd5cfa7ceea2217d3fc51cc99bcec44b74220073efaf1df11a72fc98` |
| `research_work/critical/review_theta_independent.py` | `475c92bd05f7f5a2261928ad2f82684829bb699b8d2e515c4c3c74044d57ca75` |

The exact inherited proof is PR #965, head `d58e3282a9379b6ae165681bc2e21e4f9fd18c26`, `standalone/2026-10-17-subcritical-dedekind/PROOF.md`, read from the frozen local copy `research_work/concurrent/proof965.md`. Its earlier proposed 91/100 zero-free conclusion is not needed as an input.

Concurrent PR #966 is outside this review. Nothing in the reviewed 9081/10000 composition depends on its new fourth-moment or density assertions.

## 2. Import boundary and the new analytic adapter

The comparison states its imported interfaces accurately: the actual original theta sum; its additive second moment; the full reflected `T+T^2/Z` estimate; the literal three-variable Poisson integral; the correction domain; the joint, rather than separate, Gaussian decay; the principal numerator; and the actual finite-order family mean and density theorem. Those are substantive hypotheses for this composition and cannot be replaced by a finite bookkeeping output.

I reread #965's reconstruction of the reflected estimate. Its positive auxiliary loss b makes the n sum with exponent `1+3b/2` convergent. Its dyadic profile argument explicitly covers effective lengths below one. Retaining the diagonal T term is necessary when M<1. I found no new compatibility problem caused by substituting `M=2243/2500`. I did not independently rebuild CT's exact reflection formula, fixed-profile assertion, or quadratic-family sieve.

The interpolation component is used within its scope. The rows are the actual sixth-free indices ordered by full norm; the selected subsets may depend on denominator zeros; only numerator absolute values are averaged. The primitive conductor is O(U), the archimedean types belong to a fixed finite list, and the omitted Euler factors have a product bounded by a fixed power of U. The primitive functional equation thus costs `U^(1/2-y)` with an additional arbitrarily small loss, exactly as accounted for.

The intermediate-line estimate is used only at fixed `0<y<1/2`. The final y=e class uses individual convexity instead. Complex conjugation causes no missing-family issue: the central mean for the conjugate functions follows directly by replacing t with -t, without having to relabel conjugate characters inside the index set.

The document retains the needed limitation: the actual central mean, including the finite S-unit twists, is imported through #965's adapter. The interpolation argument does not independently authenticate that adapter or prove a reciprocal mean.

## 3. Scale and principal-residue normalization

The literal scale monomial gives

    a=2243/5000, h=2757/5000, theta=a/2=2243/10000,
    b=5/6-a/3=3419/5000,
    b+theta=9081/10000.

These are consistent with `X=Y=Z^a` and the full physical second moment. In particular `2a<1`, so the T term dominates, giving `I<<Z^(a/2+eta)`. The shifted detector in the proof uses the new b; it has not retained #965's old 17/25 shift.

For the principal row, keeping Re xi=1+e avoids dependence on a previous proposed zero-free conclusion. The two remainder exponents are

    h/6+(1+h)e,
    theta+(1+h)e.

The required contour paths stay in the stated correction domain. The residue at w=1 is taken before the subsequent z=1/6 residue, and the w remainder stays to the right of that z pole. The unchanged principal H(s) is invoked only in its imported nonvanishing domain Re s>2/3.

## 4. Density partition and quantifier order

The 2673 thresholds produce exactly 2674 disjoint classes. The middle class `E_j minus E_(j+1)` is counted at its lower threshold and shifted to the line allowed by its upper threshold. The last exceptional class remains on the Euler-convergent reciprocal line. No numerator independence or monotonicity assumption beyond the nested zero-selected sets is used.

The order of choices is valid:

1. fix the field, local data, scales, finite grid and one positive e;
2. choose rho small enough for the finitely many density-height exponents;
3. choose the density loss, and thereby fix the exceptional sets;
4. only then choose the later reciprocal, correction, mean and norm-conversion losses.

The zero-free rectangles cover the truncated xi rectangles. Their radii and the fixed shift e leave the required strict gaps for the analytic-logarithm argument. For each fixed e, the constants may depend on those gaps. No uniform limit as e tends to zero is needed.

The intermediate y values satisfy both `x+y>1` and `3x+y>5/2`: the maximum in the selected y line retains the second inequality when it is stronger. This is essential in the part below x=3/4. All other correction-domain inequalities are also satisfied.

## 5. Independent replay of every row exponent

The new checker `review_theta_independent.py` does not import `verify_theta.py`. It reconstructs g from its q=2sigma-1 rational formulas, reconstructs each numerator exponent directly, and computes the complete polynomial in e for all 2674 classes. Its full-interval argument differs from the main checker's Bernstein argument: it bounds each positive coefficient contribution by its value at e=10^(-6), while retaining every negative constant margin. The affine domain inequalities are checked by their two limiting endpoints, allowing zero at e=0 only because the positive interval excludes zero.

The independent replay found:

- 173 central-mean classes;
- 1700 interpolated classes;
- 801 convexity classes;
- positive U exponents in every class;
- valid correction-domain vertices and hence segments by convexity;
- `E+(h+e)R < theta+4e` on the whole interval `0<e<=10^(-6)`;
- the same minimum constant margin as the main checker.

The limiting middle class is `middle-1358`, with lower threshold `4043/5000` and upper threshold `8087/10000`. Its constant margin is exactly

    20321474869/416197180000000.

Its complete growth polynomial has coefficients

    93332705999131/416197180000000,
    2242386652871381/1040492950000000,
    -76347867793/208098590000,
    -1.

This matches the main checker and the written proof. The middle-class margin is small but strictly positive rationally; no floating-point optimization is a premise.

I also inspected and ran the main checker. Its explicit failing checks remain active with Python optimization, and its nonnegative Bernstein-coefficient test is a valid sufficient positivity proof for the stated e interval. Its ten density monomial checks are algebraic checks of the imported detector's exponents; they are not an authentication of the detector theorem itself.

## 6. Small norms and all tail ranges

The new small-norm cutoff is necessary. At `U<=Z^(1/1000)`, the exponent is

    (2/5)h+(1/1000)(5/4-2/5)+e
       =22141/100000+e,

strictly below theta for sufficiently small e in the stated interval. Reusing 1/100 gives a constant exponent 0.22906, exceeding theta=0.2243; the negative control is mathematically relevant.

The horizontal and original-line tails are compatible with the smaller cutoff. The coarse bound is at most `Z^2 U^2<=Z^(3.12)` since U<Z^(14/25). After fixed polynomial height factors are absorbed into a sufficiently large Schwartz order, `U>Z^(1/1000)` and the displayed order `>6000/rho` give more than `Z^(-6)` decay. This leaves ample room for `O(Z^(-1))` and dyadic logarithms. The joint Gaussian/Schwartz split correctly accounts for the region Im z approximately equals -Im xi. No Gaussian decay in xi alone is substituted.

For large U, the initial x=y=4 lines use absolute convergence, not a convexity formula outside its stated strip. With `L=10/e+2`, the exact lower-endpoint exponent is

    a/2+3+3a+hL+(h+e)(1-L)=-9757/2000-e.

The positive e gap between the lower cutoff and h is retained. L is fixed after e, so its possibly large constants do not create an uncontrolled Z-dependent choice. The rightward z shift crosses no pole and stays in the correction domain.

These regions cover the principal row, bounded and small nonprincipal norms, the full intermediate range, all truncated xi edges and original tails, and the large norms. I found no omitted range introduced by the new partition or scales.

## 7. One wording correction, applied and rechecked

The initial Section 8 said the good-class correction domain "requires a>4/9." With the proof's arbitrarily small positive e losses, the precise necessary bound is `a>=4/9` in the zero-loss limit. The choice `a=4/9`, lower threshold `sigma_0=2/3`, and actual contour `x=2/3+e` can satisfy the strict correction domain while its exponent is covered by the allowed small loss. The author applied this correction. The corrected paragraph has been reread, and reversing this sole paragraph change and terminal whitespace reproduces the initially reviewed file's SHA-256 `d44664164c5313c5436cdb10c052ec7d4b2a0466b22ff37a2f69f08aba31bf43`. The table above binds the corrected file.

The conclusion that this comparison, with its INHERITED correction domain, cannot pass BELOW `49/54` remains correct. The new separate `LOCAL_DOMAIN.md` investigation changes that correction-domain interface and requires its own review and any future contour comparison. It is not an input to the frozen 9081/10000 proof reviewed here.

## 8. Mellin continuation, descent, and the resulting scope

Given the comparison and the imported principal numerator properties, the Mellin argument is sound. Flatness at zero and the bound at infinity give holomorphy in `Re s>b+theta+5e`. An initial right-line Mellin inversion identifies the transform, and the nonzero principal numerator excludes a denominator zero. At s=1 the reciprocal supplies a zero; no pole is mistaken for a target zero.

For an individual point to the right of 9081/10000, choosing one fixed e with `5e` smaller than its boundary distance is sufficient. The proof does not require a constant uniform in e. The abelian extension `K(mu_12)/K` and finite-order class-field factorization support the stated descent, provided the fixed-field analytic inputs hold. No general Artin holomorphy is invoked.

The strongest justified disposition is therefore:

    No defect found in this proposed new composition from its explicitly
    stated inherited analytic interfaces; the exact new exponent bookkeeping
    has an independent rational replay.

This is not an unconditional external certification of every upstream analytic input, a verified endpoint theorem, or a full RH proof. The proposed result must remain labeled as proposed until the exact imported sources and the separately authored interpolation component have completed independent mathematical review.
