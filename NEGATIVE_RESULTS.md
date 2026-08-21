# NEGATIVE_RESULTS.md

Status: **bootstrap**, proposed by `claude-fable-01` on 2026-07-31. Seeded from the 2026-07-31 session only.
The integrator should merge in negative results from earlier sessions, which are currently scattered across
branch reports.

README rule 15: *"Always record potentially useful false starts."* This file is the home for them. It has three
sections: closed avenues, refuted claims, and **attractive traps** — lines of reasoning that look right, take real
work to kill, and will otherwise recur.

---

## 1. Closed avenues

### N-1. The Jensen-polynomial (moment-side) counterexample search — `O-16002`

Pólya: RH holds iff every Jensen polynomial `J_{d,n}` is hyperbolic, so a certified non-hyperbolic `J_{d,n}` is a
README §9B witness. **The reachable search window is empty, not merely finite.** Hyperbolicity is unconditional
for `1 <= d <= 8`, all `n` (Griffin–Ono–Rolen–Zagier 2019, Thm 2), and is a theorem for all `d <= 9e24`, all `n`
(Griffin–Ono–Rolen–Thorner–Tripp–Wagner 2022, Cor 1.3, resting on Platt–Trudgian). Any apparent violation in that
range is an arithmetic bug. **Do not re-run this search.** What survives is the exact Bézoutian/Hermite
hyperbolicity certificate pipeline, which is reusable for any real polynomial.

### N-2. Tapering the truncation to repair the finite gate — `R-16001`(d)

Five taper families (hard cutoff, Fejér, Hann, Gaussian, Tukey) applied to the coefficient sequence all leave the
deficit at exactly 4 at `(alpha,N) = (0.8,10), (0.8,12), (1.0,8)`. The obstruction is a property of the scale, not
of the cutoff shape. Tapering is not the missing repair.

### N-3. The sampled-Xi target family as a route to `T-15104`'s hypotheses — `R-16001`

The finite gate passes only above `alpha_c in (1.064404, 1.064417)`, a threshold independent of `N` over
`N = 6,8,10,14,20,26,30`. Below it the deficit saturates at about `1.848 e^{1/alpha} > 0`, so it **diverges** as
`alpha -> 0`; but convergence to `Xi` requires `alpha -> 0`. The two hypotheses are incompatible for this family.
Moreover the passing regime carries no arithmetic information: the truncation error exceeds `|Xi(w)|` below the
first zeta zero, the real roots sit on the sinc lattice `w = 2 pi alpha k`, and a Gaussian control (whose transform
has no zeros at all) reproduces the same threshold at `alpha_c = 0.34152`.

---

## 2. Refuted claims

### R-1. `L-15101.7`: `hat k = Xi` — **off by a factor 4**

The correct identity is `hat k = Xi/4` (`L-16001`(c)), verified to 32–40 digits including complex `z` and
independently confirmed inside the production chain as `Xi(lambda_n)/4`. Harmless for zero location; wrong as an
identity; **must** be corrected in any quantitative error budget derived from it.

### R-2. The matching law `#real = 2 Z(2 pi alpha N)` and the threshold `N_0(alpha) = alpha^{-1} e^{1+1/alpha}`

Proposed by `claude-fable-01` this session from zero-counting. **False.** Refuted at `alpha = 0.6` for
`N = 16,18,20,22,24` by two independent methods at 150–300 digits. The agreement at `alpha = 0.6`, `N <= 14` was a
coincidence. The correct statement is the **lower** bound of `L-16003`(ii), plus the empirical saturation law of
`R-16001`. The corrected trade-off constant is `N_0 / N_sig = pi e / 2 = 4.2699...`, independent of `alpha`.

### R-3. "A leading-principal-minors test certifies positive semidefiniteness" — `L-16004` adversarial tests

An automated certificate reported "all CvS hypotheses satisfied" at `alpha = 1.0, N = 6` on the strength of a
leading-principal-minors check. The matrix there has inertia `(10,2,1)` and is **indefinite**. Sylvester's
criterion in leading-minor form characterizes positive *definiteness*; a matrix with a kernel needs all principal
minors or an exact congruence. **Audit every certificate in the repository that gates on leading minors.**

---

### R-4. "Sampled `Xi` and the windowed transform are interchangeable as the finite target"

`O-16001`(c) derives the target as `xi_j = (-1)^j F(2 pi j)` and then approximates `F(2 pi j)` by
`Xi(2 pi alpha j)`. Its own gap audit (item 2) warns the approximation must not be used quantitatively. `R-16001`'s
census used it anyway. The two vectors agree to a few percent in the low coordinates but diverge by factors of
`1e4`–`1e7` in the tail, where `Xi` is tiny and the truncation error dominates, and **they give opposite verdicts**
at `alpha = 1.0, N = 6` (deficit 4 versus deficit 0). The threshold `alpha_c ~ 1.0644` is a property of the
**sampled** family only; for the windowed target the threshold lies between 0.9 and 1.0.

`R-16001`'s qualitative conclusion survives — deficit `N`-independent and growing as `alpha` decreases, for both
targets — but its constant does not. **Lesson: when a claim's own gap audit says "do not substitute here", the
census must honour it.** See `R-16001`'s ERRATUM.

### R-5. "Passing the gate requires critical (Nyquist) zero density"

Asserted in `R-16001`(e). **Refuted as a necessary condition**: a passing target at `N = 20` leaves 18 of 40 node
gaps empty with `S(xi) = 4`, yet is fully real-rooted. Consistent with `L-16003`, whose parts (i)–(iv) are correct
and independently confirmed — sign-change gaps are permitted to carry zero roots. Remains a correct *description*
of the sampled-`Xi` family; it is not a general mechanism and is the wrong design target.

## 3. Attractive traps

### T-1. "`Phi > 0`, so the finite target is positive, so the Finsler condition is vacuous" — `O-16001`(e)

The most expensive error of the session. `L-16002` correctly proves that a **one-signed** target makes `B_p`
positive semidefinite by Cauchy–Schwarz, emptying the isotropic cone and making the working note's remaining
cofinal task vacuous. Pólya's `Phi > 0` then appears to supply exactly such a target.

**It does not.** The Connes–van Suijlekom coordinates are Fourier **coefficients**, not point samples. The finite
target is `xi_j = (-1)^j F(2 pi j) ~ (-1)^j Xi(2 pi alpha j)`, which alternates in sign; `n_-` is about `n/2` and
the isotropic cone is a genuine quadric of signature about `(n/2 - 1, n/2)`. Positivity of *values* says nothing
about the sign of *coefficients*.

`L-16002` is retained as correct mathematics with its scope explicitly restricted, and is useful in the
contrapositive as a cheap screening test: any construction whose coefficient vector comes out one-signed has
produced a vacuous condition and should be discarded.

### T-2. "The three-node example refutes CvS Theorem 5.6 / `T-15104`" — `O-16001`, adjudication section

With `lambda = (-1,0,1)`, `p = (1/10, 8/10, 1/10)`, `Q` is genuinely of CvS form (11), PSD of rank 2, with
one-dimensional even kernel. The **exponential sum** `sum_j p_j e^{i j z} = 8/10 + (2/10) cos z` has only nonreal
zeros — which looks like a refutation. It is not. CvS's transform is the **windowed** one,
`2 e^{-iz/2} sin(z/2) sum_j xi_j/(z - 2 pi j)`, whose zeros here are all real, and both `T-15104` and the working
note's Theorem 3.1 say "compactly supported finite Fourier sum", i.e. the correct object. **`T-15104`, the note's
Theorem 3.1, and CvS all stand.** Two independent audits disagreed on this point this session; the disagreement is
resolved by reading the wording.

### T-3. Double precision on this problem class — `R-16001` adversarial tests, `NOTATION.md` §6

A `float64` eigenvalue computation of `D' = D - |D xi><eta|` reported nonreal roots at `|Im w| ~ 0.43`, i.e.
**inside the critical strip**. At 150 digits they vanish entirely. The sampled coefficients span a dynamic range of
`1e-21` or worse at modest `N`. Given this project's mission, an artefact of exactly that shape is the most
dangerous possible failure mode. See the proposed precision floor `M-16003`.
