# Moving auxiliary primes and local zero buffers: two exact no-gain audits

Status: exploratory, source-specific obstruction calculations. No new zero-free region.
Scope: the existing separated positive-norm direct comparison and the existing M2 recursion. Neither calculation rules out a signed joint estimate for the physical probe.
Source baseline: GettysburgResearch/riemann PR #1012, commit `64cb43c038d1828a478cb97cbc32e435e111d2d2`; Liu, arXiv:2610.26835v1; the original Eisenstein source `_source-original-quasi.tex` at OpenAI commit `1581d4cbdd69a0faf34b2089614fe2a814316a6a`.
Actually run: the exact rational auxiliary-digit and exponent identities now included in `verify_algebra.py`; source reads of Liu Sections 12.4–12.8 and 13.2–13.5, and original-source definitions `eq:general-probe`, `eq:low-separated`, `eq:local-full-coefficient`, `eq:probe-poisson-identity`, `prop:probe-gram`. The script checks scalar algebra only, not the proposed growing-prime analytic estimates.
Smallest remaining gap: an estimate that retains the correlation between the additive and completed-theta factors, or a transform that retains a buffered-row selector.

## 1. Candidate: shift the exceptional additive frequencies with a moving auxiliary prime

The original Eisenstein probe permits a primitive nontrivial auxiliary residue character at a prime `p` in the identity ray class of the fixed supplementary group. Write `q=Np`, let `chi_p` be the sextic residue character, and choose `xi_p=chi_p^d`, `d in {1,2,3,4,5}`. This is initially a fixed-prime identity; a uniform analytic theorem for growing `p` is **not** inferred from the fixed-data theorem.

At this prime, reciprocity gives the following exact local digits:

| Object | Digit modulo six |
|---|---:|
| Additive column coefficient `chi_s(p)/xi_p(s)` | `1-d` |
| Theta coefficient `Xi(A)^(-1)`, `Xi(A)=xi_p(A)chi_A(p)` | `-d-1` |
| Frequency needed to make the additive residual character principal | `e=d-1 mod 6` |

All original zero extensions at `p` remain. In particular, `d=5` makes the theta twist unramified at `p`, apart from its zero mask, and forces an exceptional additive frequency to have valuation `4 mod 6` at `p`. Because the original additive columns are prime to `p`, the common column-support factors cannot cancel this necessary valuation.

This initially looks useful: replacing the old exceptional class `j=a^6` by `j=p^4 a^6` reduces its count by `q^(-4/6)`, or eliminates it when the dual frequency cutoff lies below `q^4`.

The physical normalization must also be changed. The same original probe has

    Q = q_b XY,      I = Q^(-1/2) sum_m A_m B_m

up to fixed profiles and bounded phases, where `q_b` includes the new factor `q`. The high-side coefficient contains a factor `sqrt(q_b) tau xi(A) overline(xi(H/s))`; this cancels the displayed denominator and auxiliary phases in `eq:local-full-coefficient`. Consequently the high principal reciprocal receives **no compensating positive power of q**. This is coefficientwise, before estimates.

Let `q=Z^r`, `X=Z^lx`, `Y=Z^ly`, and `b=ly-lx>=0`. Grant the candidate every favorable unproved analytic interface: completed-theta energy at its enlarged row scale at most `Q Z^epsilon`; zero cost for the moving extra column puncture; and the sharpened exceptional additive count with `e=d-1`. Discard all nonexceptional error terms, since doing so only improves this proposed method. The resulting best direct exponent permitted by these grants is

    L_e(r) = lx/2 + r/2 + max(0, [b-(e+1)r]/12).

Indeed, the additive diagonal contributes `Q/Y=qX`, its exceptional ratio is `(Y^2/Q)^(1/6) q^(-e/6)`, and Cauchy takes a square root; the `Q^(-1/2)` prefactor cancels the square root of the granted theta energy.

The inherited exponent is `L_old=lx/2+b/12`. For every `r>=0`, `b>=0`, and `0<=e<=4`,

    L_e(r)-L_old = (5-e)r/12             if (e+1)r<=b,
    L_e(r)-L_old = r/2-b/12 >=(5-e)r/12  if (e+1)r>=b.

Hence it is nonnegative, and positive when `r>0`. The most favorable legitimate choice `d=5,e=4` still loses at least `r/12`. Even granting the illegitimate principal auxiliary character `d=0,e=5` would only make the first branch tie the old exponent.

This proves a no-gain theorem for the stated separated-estimate proposal, **not a lower bound for the true probe**. It does not prove the optimistic growing-prime theta energy or the sharpened global Gram asymptotic. Extra conductor costs and nonexceptional errors would worsen the same calculation. A signed estimate of `sum_m A_m B_m`, or a coherent average over auxiliary primes before taking norms, is outside this obstruction.

## 2. Candidate: replace the global M2 parameter by the original row's buffered zero parameter

The simultaneous detector in Liu Lemma 13.3 gives a local zero parameter `a=(1+delta)/2` for every presentation in its original row's finite family, and buffered bounds for those original characters. It is tempting to replace the global parameter `kappa=2 beta_*(F)-1` by `delta` in M2's prime cost `6 kappa z`.

The source proof does not license that substitution:

1. In Section 12.5, immediately before Lemma 12.8, the squared norm of the whole centered difference is enlarged to the **unrestricted positive row ball** before Poisson. The original buffered subset has been discarded.
2. In Section 12.7.1, equation (12.2), the new presentations are `tau_C=tau chi_bullet(er) xi_r` and `tau_D=tau chi_bullet(er) conjugate(xi_r)`. The second transform introduces new frequency twists. There is no assertion that these induced characters belong to the original row's buffered family.
3. Section 12.8.1 restores overlength selected-prime factors by Lemma 12.7 on those transformed rows. That lemma explicitly uses the common global zero-free premise `beta_*(F)<=(1+kappa)/2` for every moving presentation and its fixed coefficient twists.

A selector-preserving positive lift or a source-specific estimate for these new rows would be a new theorem. The original local hypothesis alone cannot simply be reapplied after the positive enlargement.

There is also an elementary obstruction to stripping additional prime factors only on the original class. If their total logarithmic length is `z`, the buffered pointwise cost is `U^(delta z+epsilon)` in the squared moment. At the boundary-determining amplitude `x=1/2`, the actual lower amplifier gain is exactly

    U^(2 g z)=U^(delta z),      g=delta/2.

The added local cost cancels that extra lower bound. This cannot create a strict count improvement at the binding class. For `g<delta/2` this particular operation is worse. This is an exact exponent statement; it is not a claim that the prime polynomials attain their upper bounds.

Finally, the current centering implementation assumes `kappa>=13/18`. Its numerical purpose is stated in Section 12.5: `6 kappa-1>=10/3` puts the comparison product in a lower-rank range. Thus using the critical `delta≈0.4693` would also require a new centering argument, independently of the missing family-buffer transport.

## 3. A remaining nonpositive route

The `d=5` choice has an additional useful structural feature: outside the new prime, its theta coefficient has no new primitive local twist. A coherent sum over such auxiliary primes therefore couples them mainly through the additive coefficient and row phase, while the main theta block can potentially be kept common. Its prime coefficient is a normalized sextic Gauss phase times `chi_p(s^2/m)`; via the source Gauss relations it can be rewritten as a quadratically twisted cubic Gauss coefficient.

This identifies a possible signed joint problem, not a bound. It is precisely where a quadratic-conductor average and the full divisor masks must be retained. Estimating every prime separately or taking two independent positive norms returns to Section 1. No coherent auxiliary-prime estimate of sufficient strength was proved in this audit.
