# A parameter-range extension and an exact scalar improvement candidate

Status: VERIFIED_EXACT_SCALAR_CERTIFICATE_AND_REVIEWED_CONDITIONAL_ADAPTER. The full source-qualified deduction is in `KAPPA_EXTENSION_CONDITIONAL.md` and has passed independent mathematical review.
Scope: the same finite-order Hecke family over Q(sqrt(-3)) and Dirichlet transfer as the cited sources; no RH claim.
Sources: OpenAI September 30, 2026, commit `fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb`; Baiying Liu October 8, 2026, commit `7d10420de90efa2f082a06a342fc7accbd57ab37`.
What was actually run: exact SymPy rational polynomial identities and coefficient signs, all unchanged scalar geometry gates, and rational isolation of sqrt(921).
Smallest remaining gap: independently rebuild the imported analytic proofs. The reviewed written adapter and scalar computation do not replace those inputs or supply an unconditional verification of their L-function conclusions.

## Prior-art boundary

Repository PR #910 at exact commit `670a76c1a3a8f325c43c1755b1cfc24d313a3e3c` already derives the variable-geometry low bound, the enlarged principal Euler domain, a fixed-kappa=3/4 conditional improvement to 139999/160000, and the exact algebraic geometry ceiling (1507-2sqrt(921))/1653. Liu independently supplies the full endpoint geometry at that ceiling. Those shared arguments are credited and reused here. PR #910 explicitly declines substitution below kappa=3/4. The additional step developed in this wave is the parameter-range proof adapter and the resulting generalized prime capacity, followed by a rational certificate below that ceiling. Its standalone inverse-Mobius fourth-moment target is a different moment estimate from the plain fourth moment extended here.

## The precise imported barrier

Liu's algebraic endpoint is

    B_new = (1507 - 2sqrt(921))/1653 = 0.8749570697991687...

The September 30 fourth-moment lemma (Lemma 18.1, label `lem:plain`) assumes `3/4 <= kappa <= 1`. With positive prime-slot length z it requires

    n_1 + n_2 + 6 kappa z <= M,
    beta_* <= (1+kappa)/2  (when kappa<1),

and retains the source's common character, mask, finite-ray coefficient, disjoint-prime-support, mesh, and exceptional-inducing-family hypotheses. With no slots it has its separate unrestricted-length statement.

The new bound B_new does **not** authorize substitution kappa=2B_new-1 into that lemma: this value is below its stated admissible range. The displayed analytic proposition must first be extended.

## Minimal extension suggested by the proof

The candidate is the same lemma on `13/18 <= kappa <= 1`, keeping every other hypothesis and conclusion unchanged. In the September 30 proof, all explicit uses of its lower bound occur in the following places (source labels identify the frozen text).

1. `old-eq:3.6`: since A=n_1+n_2+z>=z, the slot condition gives z<=M/(6kappa) and kappa z<=M/6. The proof's terminal exponent uses only the latter bound. The auxiliary bound z<=2M/9 becomes z<=3M/13 in the enlarged range, with no change to the terminal loss rho/6.
2. In the comparison stage before `old-eq:3.11`, A>5M/6 and (6kappa-1)z<=M-A give z<M/[6(6kappa-1)]. For kappa>=13/18, 6kappa-1>=10/3, so z<M/20 still holds. The original comparison bounds A_comp<=23M/30+xi and A_comp+(6kappa-1)z<=14M/15+xi, including their margins, remain valid.
3. The prime-polynomial bound `old-eq:3.5` uses s_kappa=(1+kappa)/2>=beta_* and its contour shift. The enlarged interval does not weaken this hypothesis. Its normalized squared prime exponent remains kappa z.
4. The greedy slot removal uses a decrease of 6kappa times removed length and a cost of kappa times that length, hence the same cost/defect ratio 1/6. The positivity kappa>0 remains uniform.
5. The affine ledger bound `old-eq:2.1j` needs 0<=6kappa-1<=5. This remains true. The final mesh and finite-induction choices may use the new compact interval [13/18,1].

The full written induction adapter has passed a separate source review, retaining the reflected comparison, finite Poisson, masking, finite-family exceptional and seminorm interfaces in their original coefficient class. Its arithmetic comparison and clipped-column bounds have separate compiled Lean adapters. This is a source-qualified deduction; the imported analytic proofs have not been independently rebuilt or formalized in this wave.

## Generalized row-count calculation

Let alpha=5/6, c=1/(6kappa), delta in [0,alpha], and x in [0,1/2]. The uncapped inverse and plain savings are

    F_I(r) = x + (1-x)r,
    F_S(r) = 2cx + (2-4cx)(t-r).

Set A_x=2-4cx, D_x=3-x-4cx, P_x=A_x(1-x), and J=(alpha-delta)D_x+delta P_x. Their crossing gives the short count

    R_short(t) = 1-delta + delta P_x/D_x (3/2-t).

Balancing it against the unchanged long count 1-delta+(alpha-delta)(t-1) gives

    R_kappa = 1-delta + (alpha-delta)delta P_x/(2J).

The high exponent at the central row scale h=(1+b+3ell)/2 is

    E = -1/4 + b/6 + 5ell/4 + (1/2+ell)delta + ell x delta - h(1-R_kappa).

The direct/signal comparison uses B=11/12-ell/4. These are the source formulas with the actual prime capacity retained instead of clamping kappa to 3/4.

## A fully rational scalar certificate

Choose

    kappa = 749915/1000000 = 0.749915,
    B = 87495703/100000000 = 0.87495703,
    ell = 12512891/75000000,
    b = 1542571/12500000.

The imported B_new is below (1+kappa)/2 by more than 4.3020e-7, so the source's zero-free hypothesis would be supplied by a **previous**, separate theorem if the moment extension is proved. This finite use avoids a circular bootstrap. B is below B_new by about 3.97991687e-8.

Let v=1/2-x and Q=2J(-E). Exact expansion gives Q=A(v)delta^2+D(v)delta+G(v). Every coefficient of A(v) is positive. Every coefficient of the polynomial `Disc(v)=4A(v)G(v)-D(v)^2` is also positive, including its constant coefficient. The checker emits the exact rational coefficients. Thus, for all v>=0,

    4A(v)Q = (2A(v)delta + D(v))^2 + Disc(v) > 0.

On the required rectangle J>0, so E<0 everywhere, with no numerical-grid inference. Positive coefficients give A(v)<=A(1/2) and Disc(v)>=Disc(0). Also J<=5/2. Consequently

    -E >= Disc(0)/(20A(1/2))
       = 560828536677742722737 / 60751889795319776946000000000
       > 1/1000000000.

The unchanged geometric conditions are all strictly satisfied: lx=(1-b-ell)/2>ell, ly=(1+b-ell)/2>ell, ly-ell-11b/6>0, 1-3ell>0, ell<1/5, ell/h>7/37, 5ell>h, and B>=437/500. The available prime-supply reserve ell/h-7/37 is approximately 0.016287; the proposed perturbation does not spend that reserve.

The expanded checker also verifies every floor, intermediate, small-row transport and principal reserve displayed in Liu's geometry scope. It checks the exact generalized crossing identities: r*(3/2)=1, m*(3/2)=1/2, r*(1) decreases in x, and its minimum exceeds 23/37 by 204/68440565. Thus the inverse strict width margin remains at least 9/37; the plain length remains at least 1/3 and its capacity is at most c/3<7/37. No larger prime-supply assumption is introduced.

The global scalar certificate and independently reviewed parameter/transport adapters give the specific conditional corollary Re(s)>0.87495703, under the exact imported analytic hypotheses enumerated in `KAPPA_EXTENSION_CONDITIONAL.md`. The coordinator checked its continuation accounting against the frozen Liu and PR #910 interfaces. This is a complete written source-qualified implication; it is not an independent rebuild of the imported zero-free theorem.

## Conditional limiting endpoint

At x=1/2 the critical count R_kappa=2/3 makes the coefficient of b vanish. E=0 gives ell=(5-6delta)/(9+18delta). If one additionally seeks the formal fixed point kappa=2B-1, then

    kappa=(5+18delta)/(9+18delta),
    1188delta^3 - 2160delta^2 + 171delta + 190 = 0.

The admissible root is approximately 0.3885833542660347, leading to B approximately 0.874957019420099. This root only locates a candidate endpoint; it is not a proof of the whole-class estimate or of analytic continuation there. A single finite use of kappa=2B_new-1 yields approximately 0.8749570194791584 before possible further iteration. The rational certificate above deliberately keeps a uniform strict reserve.

## Reproduction

Run `source /workspace/.riemann-tools/activate.sh`, then from this directory run `python3 -B check_kappa_candidate.py kappa-candidate-certificate.json`. Every predicate uses an explicit exception. Normal and `python3 -O -B` runs produced byte-identical JSON, verified with `cmp`. The checker uses exact rational arithmetic. Its reviewed-adapter flag records the independent written proof review; imported-analysis rebuild and RH flags remain false.
