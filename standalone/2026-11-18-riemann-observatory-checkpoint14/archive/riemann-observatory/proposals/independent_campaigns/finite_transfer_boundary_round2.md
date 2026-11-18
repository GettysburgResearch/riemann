# Finite transfer campaign: spend the unused endpoint pressure

Status: independently derived finite strengthening; proposer and skeptic reconstructions completed, director adjudication requested. No novelty priority established. This improves a bounded finite-chain loss in a source lemma; it changes no asymptotic zero proportion and is not an RH proof.

## Goal and exact source interface

Source: Knausgård, arXiv2610.08965v1, Lemma2.5 pp11–12 and Proposition3.3; pinned first-window data in `experiments/inputs/839_first_window`. Let θ=17/20, α=6219/10^6, x=x1=54350/10^6 and y=x2=69433/10^6. Pair weights, local rewards and six potentials B0,...,B5 are exactly the frozen data; each potential interpolates its14 listed knot values at3/4+k/8 and is zero outside. Let A_r=Σ_{j=0}^r B_j for0≤r≤4, separately for each endpoint-label type.

Treat the seven-point local inequality as an input. Its first full reference search was reproduced; all kernel cells were independently checked; a separate skeptic reconstructed the search rules. That evidence is separate from this finite transfer proof.

The source transfer loss is6y+Ω=0.432480, Ω=15882/10^6. The new finite conclusion replaces that loss by

C*=6y−30αθ=516027/2000000=0.2580135.

For every finite θ-separated ordered chain with labels d_i∈{1,2}, and symmetric nonnegative e_ij≥K(yi−yj)^2−ε on near pairs0<|i−j|≤6, ε≥0,

Σ_near d_i d_j e_ij ≥ x n1+y n2−6α spread(Y)−C*−48εm.

All original local-data assumptions and the same original local inequality are retained. A more precise defect variant allows directed signed e: for every unordered near pair assume δij≥0 and Kij²≤(eij+eji)/2+δij; replace48εm by2Σ_{unordered near}d_i d_jδij. Nonnegative far-pair symmetrized energies are required only if one then enlarges the left side to all pairs.

## Exact finite hypotheses checked

For each r=0,...,4, each of the three label types, and every real t≥θ, the frozen prefix potentials satisfy

A_r(t)≤α(5−r)(t−θ),

−A_r(t)≤α(r+1)(t−θ).

These are rigorous finite checks because each A_r is piecewise linear on shared knots and zero outside the support; subtracting either target line remains linear between knots. At θ the value is0: θ is in the first zero segment. Check the13 later knots for each prefix/type and both signs, plus θ. Outside the support the right sides are nonnegative and increasing. The390 nontrivial knot inequalities pass in exact rational arithmetic, with minimum positive slack6219/40000000; the30 θ endpoint conditions are equalities. Also y≥6αθ, ensuring the small-chain bound below. No floating-point decision enters.

## Proposer proof

First suppose m≥7 and put n=m−6. Write gaps g_j=y_{j+1}−y_j. The sum of the n local frame spans is

S=Σ_{w=0}^{n−1}(y_{w+6}−y_w)=Σ_{r=0}^5(y_{n+r}−y_r).

Consequently the pressure not used when one bounds S by6spread is

Δ=6spread−S

=Σ_{r=0}^4(5−r)g_r+Σ_{r=0}^4(r+1)g_{n+r}.

This is an exact identity, not an asymptotic estimate. It follows by writing each difference from an endpoint as a sum of gaps. It remains valid when the two endpoint blocks overlap; in particular for m=6,n=0 it reduces to6spread=6Σg.

The summed potential correction telescopes to P=Φ_left−Φ_right, with Φ=Σ_{r=0}^4 A_r(g_r), preserving endpoint labels. Apply the two prefix inequalities in their respective endpoint states. Since the two coefficient lists each sum to15,

P≤αΔ−30αθ.

Thus the combined pressure and correction cost is

αS+P≤6αspread−30αθ.

The same reward-counting argument as the source loses at most6y at the two ends. The same nonnegative offset-weight budgets bound all local pair terms by near-pair energy plus the stated defect cost. Subtracting the combined costs gives exactly C*=6y−30αθ in the conclusion. This spends pressure that the source left unused; it does not strengthen or change the computer-assisted local inequality.

For1≤m≤6 there may be no full frame. The total reward is at most my and spread≥(m−1)θ. Since y≥6αθ, the function my−6αθ(m−1) increases with m, hence is at most its m=6 value C*. For the directed/signed variant, the approximation assumption gives near energy plus exact defect≥Σ_near d_i d_jKij²≥0. This replaces an invalid appeal to nonnegative e in that variant. For m=0 the statement follows from C*≥0. Therefore every finite chain length is covered.

## Independent reconstructions and experiments

The skeptic found the unused-pressure route while separately checking the source transfer lemma. This proposer independently derived Δ through the summed-endpoint identity, checked all390 rational knot inequalities and30 endpoint cases, verified small chains, and separately reconstructed a weaker joint-label bound. Results: `experiments/results/839_boundary_advocate.json`; code: `839_boundary_advocate.py`. Independent skeptic files retain their own derivation and finite certificate.

The proposer also checked Δ as a coefficient identity for chain lengths6 through80; those finite tests supplement the general identity proof and are not its justification. Every arithmetic comparison uses Python Fraction or integers.

The intermediate joint-label method gives0.426800 by separately maximizing reward deficit+Φ at the left end and reward deficit−Φ at the right, over64 six-label states. Each maximum is213400/10^6, attained at all-double labels. That valid intermediate improvement is superseded by the pressure-aware bound and preserved as development history.

## Limits and next mathematical steps

This is an O(1) boundary improvement of348933/2000000 over the source transfer lemma. After division by a zero count tending to infinity it disappears, so it cannot improve the stated asymptotic constants. The global analytic zeta bridge and explicit finite-T trace/smoothing errors are not proved by this campaign. No published result is contradicted, and no paper is characterized as erroneous.

To obtain a useful finite-height certificate, make the remaining analytic errors explicit and combine them with this boundary constant; determine whether this term affects the final numerical threshold at all. Another precise step is to generalize the endpoint-pressure bookkeeping to q-point windows and test the corresponding piecewise-linear prefix conditions against the second/third certificates. Any claim of publication novelty requires a prior-art search on finite transfer/coboundary boundary optimization.

## A tested counterexample to dropping the small-chain guard

The source-specific proof above uses y≥6αθ. Positivity of C* alone is insufficient for an unrestricted generic theorem. Set θ=1, α=1/100 and x=y=11/200; give each of the seven local positions reward11/1400 for either label and set every weight/potential to0. Every permitted seven-point frame has pressure at least6/100>11/200, so its local inequality is true, and all prefix-pressure bounds hold trivially. The candidate C*=6y−30αθ=3/100 is positive. But the one-point configuration would require0≥y−C*=1/40, which is false. This explicit witness preserves the need for a small-chain hypothesis in any generalization. It does not apply to the frozen source data, which pass that hypothesis.
