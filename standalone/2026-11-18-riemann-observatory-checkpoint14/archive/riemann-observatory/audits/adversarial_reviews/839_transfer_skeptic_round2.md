# Independent reconstruction of the seven-point transfer

Reviewer: search_skeptic. Date:2026-11-17. This review treats `LocalInequality` as an input; it does not repeat the finite search, validate the zeta second moment or audit the entire paper.

Sources: Knausgård, [arXiv2610.08965v1](https://arxiv.org/abs/2610.08965v1), local data and Lemma2.5 on pp10–11, Proposition3.3 on pp15–16; pinned repository commit `0e961ea199b425010843bc8044676d4ad29fe031`, `lean/Distinct839/Defs.lean`, `Spec.lean`, and all four files of `Transfer/`. Original proof inspected and reconstructed. No source error was found. A stronger finite boundary estimate is derived below; independent parent review was requested, and literature novelty is not established.

## Exact source statement

Fix the first-window kernel K and table data. Let θ=17/20, α=6219/10^6, x=54350/10^6, y=69433/10^6, b=6α and Ω=15882/10^6. A label has multiplicity m=1 or2 and reward x or y. The seven-point local inequality has position-dependent nonnegative rewards h_{i,m}, pair weights W_{ij}^{m,m'}, and adjacent-gap corrections B_r^{m,m'}.

For each index distance s=1,…,6, the sum of the corresponding W coefficients is at most2mm'. Rewards sum to x or y over the seven local positions and h_{i,1}≤h_{i,2}. For every fixed pair type and t, Σ_{r=0}^5 B_r(t)=0. All these are exact finite-table conditions, not asymptotic hypotheses.

Let ℓ be any nonnegative integer, y_0<…<y_{ℓ−1} a θ-separated chain, labels m_i∈{1,2}, ε≥0, and R≥0 an upper bound on its spread. Paper Lemma2.5 assumes symmetric nonnegative near-pair energies e_ij≥K(y_j−y_i)^2−ε for0<|i−j|≤6 and concludes

E_near ≥ Σ_i reward(m_i)−bR−(6y+Ω)−48εℓ,

where E_near=Σ_{0<|i−j|≤6} m_i m_j e_ij. The constant6y+Ω is2703/6250=0.432480.

The formal `TransferStatement` instead concludes a lower bound for **all** ordered off-diagonal energies, assumes e_ij≥0 and the kernel approximation for every off-diagonal pair, and does not require e_ij=e_ji. Its proof averages the two orientations. The formal statement is consistent with the paper's near-pair result because nonnegative far terms can be added. These are distinct hypothesis packages and should not be silently interchanged.

## Four parts of the source transfer

For ℓ=n+6, use the n seven-point windows starting at w=0,…,n−1. The identities below also hold at n=0. Chains shorter than six are treated directly.

**Rewards.** A fixed local position i visits exactly n of the n+6 sites, omitting six. Since every omitted reward is at most h_{i,2}, summing over i loses at most6Σ_i h_{i,2}=6y. Thus the sum of local rewards is at least the global reward minus6y. This loss is uniform in n, R and the label pattern.

**Pressure.** If g_p=y_{p+1}−y_p, then

Q:=Σ_w Σ_{r=0}^5 g_{w+r}=Σ_{r=0}^5(y_{n+r}−y_r)≤6R.

Multiplication by α≥0 gives the source's bR bound. The exact identity, rather than just this upper bound, is useful for the improvement below.

**Correction state.** Put A_q^{m,m'}(t)=Σ_{r=0}^q B_r^{m,m'}(t), q=0,…,4, and

Φ(w)=Σ_{q=0}^4 A_q^{m_{w+q},m_{w+q+1}}(g_{w+q}).

The corrections of window w equal Φ(w)−Φ(w+1): the coefficient of each interior gap is A_r−A_{r−1}=B_r, and the last is −A_4=B_5. A physical gap keeps the same labels in every window; optimizing labels independently for different windows would break this argument. Summation gives P=Φ(0)−Φ(n). Partial-potential knot ranges are bounded by

upper=(2124,2113,0,1790,1914)/10^6,

lower=(−1914,−1790,0,−2113,−2124)/10^6.

The hat functions are nonnegative and sum to at most1; each lower bound is nonpositive and each upper bound nonnegative, so these bounds remain valid outside the support as well. Hence P≤Ω. This is a boundary term, rather than a correction loss proportional to the number of windows.

**Pairs and errors.** A fixed physical pair of index distance s≤6 appears with the same endpoint labels and a subset of the local weights W_{i,i+s}. Nonnegative weights and the exact budget give total coefficient at most2m_i m_j≤8. The factor2 corresponds to the two ordered orientations in E_near. There are Σ_{s=1}^6 max(ℓ−s,0)≤6ℓ unordered near pairs, so replacing K² by energies costs at most48εℓ. The error is linear in the number of sites because only bounded index distance is used. Bounding errors over all ℓ² pairs at this step would discard that advantage.

## A valid finite hypothesis weakening

The near-pair proof needs neither symmetry nor individual nonnegativity of e. For each unordered near pair i<j, define u_ij=(e_ij+e_ji)/2. It suffices to have numbers δ_ij≥0 such that

K(y_j−y_i)^2≤u_ij+δ_ij.

Then u_ij+δ_ij≥0 automatically, which is exactly what the weight-budget step needs. The resulting exact defect is

D_δ=2Σ_{i<j, j−i≤6}m_i m_j δ_ij.

Thus the transfer remains valid with D_δ in place of48εℓ. Uniform δ=ε gives D_δ≤8εΣ_{s=1}^6 max(ℓ−s,0)≤48εℓ. No kernel approximation for far pairs is needed. For ℓ≤6, E_near+D_δ≥0 follows from the same nonnegative u+δ, while the reward-minus-boundary expression is nonpositive; it is incorrect to reuse E_near≥0 after allowing signed entries.

To extend this near-pair conclusion to an all-pairs conclusion, nonnegative symmetrized far-pair energies suffice. Some such control is necessary. An exact witness against simply deleting positivity from the all-pairs formal statement is:

- ℓ=100, all labels simple, y_i=7i and R=693;
- ε=1 and every off-diagonal e_ij=−1;
- K(7k)=0 for every nonzero integer k, because the six-mode sinc expansion has no nonzero term at these integers.

The lower kernel inequality holds with equality, but the old all-pairs conclusion would assert −9900≥−2410428041/500000, which is false. This is a counterexample to an altered statement, not an error in the paper or repository.

## Development history: joint boundary labels

The source bounds reward loss and correction state separately. Let the labels of a boundary block be a_0,…,a_5. The exact left and right omitted rewards are

D_L=Σ_{p=0}^5 Σ_{i>p} h_{i,a_p},

D_R=Σ_{j=0}^5 Σ_{i≤j} h_{i,a_j}.

The combined loss is D_L+Φ(0)+D_R−Φ(n). Independent maximization over64 six-label patterns at each end gives213400/10^6 per end, attained by all-double labels. Hence a first finite improvement is426800/10^6=0.426800. When n<6 the endpoint blocks overlap, but relaxing them independently still gives a valid upper bound. This correct intermediate bound is superseded by retaining pressure slack.

Ω itself is sharp as a state oscillation: the maximum7941/10^6 is attained by labels(2,2,2,1,1,1) and gaps(9/8,9/8,θ,7/4,7/4); the minimum is its sign reversal, attained by labels(1,1,1,2,2,2) and gaps(7/4,7/4,θ,9/8,9/8). These boundary states can coexist in a12-site chain. Thus reducing the isolated Ω bound would be the wrong target; combining it with other losses is what helps.

## Stronger pressure-aware finite boundary bound

For ℓ=n+6≥6, write spread=y_{n+5}−y_0. The exact pressure deficit is

Δ:=6spread−Q

=Σ_{q=0}^4(5−q)g_q+Σ_{q=0}^4(q+1)g_{n+q}.

This identity remains valid for n<6, where some gaps occur in both sums. Their coefficients then add correctly. The coefficient sums on each side are15.

For these particular frozen potentials, exact knot inequalities imply, for every pair type, q=0,…,4 and t≥θ,

A_q(t)≤α(5−q)(t−θ),

−A_q(t)≤α(q+1)(t−θ).

The functions are piecewise linear. Checking t=θ and every subsequent knot proves each inequality between knots; outside the support the potential is0 and the right side increases. The first two knot values are0, so A_q(θ)=0. These are finite rational checks, independent of the local search.

Adding the two boundary bounds gives

P=Φ(0)−Φ(n)≤αΔ−30αθ.

Consequently the **combined** pressure and correction term satisfies

αQ+P≤6αspread−30αθ≤bR−30αθ.

Using the same reward loss6y gives the strengthened constant

C*=6y−30αθ=516027/2000000=0.2580135.

Therefore, conditional on the original local inequality, the first-window finite transfer theorem holds with C* replacing6y+Ω, including the directed/signed near-pair formulation with exact defect D_δ above. Under the original formal assumptions the all-pairs conclusion has the same improved constant.

For1≤ℓ≤6, separation gives R≥(ℓ−1)θ and

Σ rewards−bR≤ℓ y−6α(ℓ−1)θ≤6y−30αθ=C*,

because y−6αθ>0. The empty chain is immediate. For signed near energies, combine this with E_near+D_δ≥0. This closes the small-chain cases without an asymptotic argument.

All-double labels and uniform gapsθ attain the resulting bookkeeping cost C* for ℓ≥6: the reward deficit is6y, all potentials vanish, and Δ=30θ. This establishes sharpness for this particular reward/pressure/state bookkeeping bound. It does **not** establish that C* is the best constant in the full energy inequality, since other inequalities in the proof may have slack.

## Evidence and limits

`experiments/code/839_transfer_skeptic_checks.py` checks the exact weight caps, rewards, state extrema,21 fractional-gap chain identities including n=0, and450 rational domination evaluations (the knot points, θ and one outside-support point). Its result is `experiments/results/839_transfer_skeptic_checks.json`.

A standalone Lean file, `experiments/code/839_transfer_boundary_core.lean`, was actually checked locally with Lean4.33.0-rc2 and Std only, exit0 in2.28s. It checks the data shape, zero initial/endpoint knots,390 integer knot inequalities, six small-chain inequalities and the final constant arithmetic. The endpoint and knot proofs use only `propext`; the other printed declarations use no axioms. It uses `decide`, with no `native_decide`, `sorry` or custom axiom. Exact output, source SHA256 and limits are recorded in `experiments/results/839_transfer_boundary_core.json`.

The integer inequality checked at knot k≥1 is40 A_int≤6219 w(5k−4), since t_k−θ=(5k−4)/40. The Lean file checks this finite certificate; it does not formalize the piecewise-linear interpolation argument, the chain bookkeeping or the entire transfer theorem. Those are reconstructed above and were submitted for independent parent review.

This is an O(1) finite improvement. It changes no asymptotic density constant or claim about RH. Novelty has not been checked against all literature or private development history. A practical next step is to formalize the two domination inequalities and the combined pressure identity in the transfer module, then carry the smaller boundary constant through any effective finite-height application. No result about the analytic zeta bridge is claimed here.

## Negative knowledge from the generic extension

The frozen inequality y≥6αθ must be retained when generalizing this pressure-aware constant to all chain lengths. It is necessary already for a single double point with R=0: its energy is0, so a conclusion with C*=6y−30αθ would require y≤C*, equivalently y≥6αθ.

The parent independently supplied an exact witness showing neither the local inequality nor C*>0 implies this guard. Set θ=1, α=1/100, x=y=11/200, give each of the seven local positions reward y/7 for either label, and set W=B=0. Every seven-point frame has α·span≥6/100≥y, so the local inequality and potential domination hold. Yet C*=3/100>0 and a one-point chain would require0≥y−C*=1/40, which is false. This refutes the unguarded generic extension; it does not affect the frozen first-window strengthening, where y−6αθ=377161/10^7>0.

## Minor negative exploration: the uniform kernel-error coefficient

The parent enumerated the128 labelings and recorded `experiments/results/839_transfer_error_budget.json`. I independently checked all21 frozen coefficient triples are nonnegative and monotone from simple/simple to mixed to double/double. Therefore the maximum local total weight is attained by all-double labels without any search: its exact sum is47999993/1000000, while the all-simple sum is11999992/1000000.

For the original nonnegative near-energy assumptions, applying K²≤e+ε inside each local frame before the pair cap gives an error at most (47999993/1000000)ε·max(ℓ−6,0). This improves the source's coarse48εℓ bookkeeping only marginally in the worst label pattern. The per-frame coefficient gain relative to48 is7/48000000, and it produces no asymptotic proportion improvement. This particular coefficient refinement is not asserted for the signed-energy extension: there the safe statement remains the exact per-pair shifted-energy defect D_δ documented above. The failed expectation of a substantial uniform gain is preserved as negative knowledge.
