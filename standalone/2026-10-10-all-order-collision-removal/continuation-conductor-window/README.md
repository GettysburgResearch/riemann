# Fourth checkpoint: bound a genuine part of the signed covariance

**PROPOSED COMPONENT PROOFS. The high-conductor signed estimate remains OPEN. No new full fourth/sixth moment, 17/24 boundary, or RH proof.**

Parent: PR #916 at `f5c089e33ccce4eae4307d4f6475b9977485cb78`. All predecessor files and sibling branches are preserved.

Read [the complete proof](ROW_SMOOTHING_AND_CONDUCTOR.md). It gives an actual upper bound for a part of the previous signed integrated covariance, not only a new sufficient condition.

## New bound

Keep the previous balanced squarefree product columns and fixed exclusion set. Replace the sharp row indicator by the positive radial weight

    V(Nu/H) = (1-Nu/(2H))_+^8.

This retains every replica row of norm at most H with weight at least 1/256. The whole old positive energy is at most 256 times the new one. Original nonunit zeros, bad-prime row factors, and all divisor allocations remain present.

For r!=s, the finite character conductor is

    q(r,s)=N(r/gcd(r,s)) N(s/gcd(r,s)).

At sigma=1/2+delta, 0<delta<1/2, the **absolute** scale-integrated covariance in Q<q<=2Q is bounded, uniformly in the horizon D, by a subpower factor times

    Q<=H:        H^(-2delta) Q^(1+delta),
    H<=Q<=H^2:  Q^(1-delta),
    Q>=H^2:     H Q^(1/2-delta).

Consequently the whole q<=H sector is O(H^(1-delta+epsilon)); the larger q<=H^(1/(1-delta)) sector is O(H^(1+epsilon)). The first is a power saving for the actual off-diagonal at every fixed delta>0. The diagonal remains O(H).

Radial unit orthogonality additionally makes the kernel **exactly zero unless Nr=Ns modulo 36**. This is a six-block identity, not a power-saving claim.

The remaining signed statistic now contains only q>H^(1/(1-delta)) and matched norm classes. A useful one-sided bound for it would still give the conditional boundary

    Re(s)>1/2+delta+(lambda+5h/6)/(2k),  H=D^h.

The proof also gives a loss-budget-adapted larger conductor cutoff. It does NOT bound the remaining high-conductor statistic. The estimates are independent of the imported OpenAI analytic foundation; the final zero-free implication uses the parent's explicitly stated integrated reduction.

## Actual arithmetic, rather than only formal phase fixtures

[arithmetic_probe.py](arithmetic_probe.py) constructs genuine Eisenstein ideals and sextic residue symbols, with both split-prime F_p and inert-prime F_(p^2) cross-checks. The retained run has D=H=96, all 684 nonzero rows of norm <192, 27 squarefree input ideals, 21 good prime ideals and 153 balanced product columns. Every original row mask is checked.

It reconstructs the complete integrated covariance and every dyadic conductor band in exact rational/cyclotomic arithmetic. Normal and optimized execution agree on **3,522,979 successful finite checks**, reject three deliberate errors, and reject a separately tampered output. The full reconstructed output is bound by its SHA-256 in [the verification record](verification_record.json).

The diagnostic uses the box window 1_(1/2,1] and scale weight X^(-3) dX/X, not the parent's smooth W_*. It tests the sector algebra, not the infinite arithmetic premise. This tiny input range has squarefree factor depth at most two; it is not an asymptotic campaign.

A useful warning from the data: the signed covariance is about 0.0972% of the full diagonal, but about 22.48% of the diagonal in the top scale interval [48,96]. The small cumulative ratio is dominated by the short scales and is **not** evidence that the growing-scale problem is solved. Some conductor bands have negative signed contributions. Both cumulative and annular measurements are retained.

## Reproduction

    python -I -S -B arithmetic_probe.py --D 96 --H 96 --write actual.json > actual.stdout
    python -O -I -S -B arithmetic_probe.py --D 96 --H 96 --check actual.json > optimized.stdout
    cmp actual.stdout optimized.stdout

Then compare SHA-256(actual.stdout) with `full_output_sha256` in verification_record.json. The checker rebuilds all arithmetic from the lattice and prime residue definitions before accepting a supplied JSON. It does not merely check consistency of derived fields.

See [source and validation scope](VALIDATION_AND_SOURCES.md). No independent mathematical review, Lean build, or external peer review is claimed. The smallest open theorem is (6.3) of the proof, on the explicitly retained high-conductor sector.
