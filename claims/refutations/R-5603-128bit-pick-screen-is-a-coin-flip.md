# R-5603 — A 128-bit `lambda_min` screen on the eight-node Pick grid is a measured coin flip

Claim ID: R-5603
Title: At the PR #71 ordinate the true `lambda_min` is `+1.2259907375436e-35`,
the 128-bit noise floor is `2.99e-33`, and a simulated 128-bit screen reports a
negative in `53.3%` of trials
Status: PROPOSED (the true value is high-precision floating, not a directed
interval; the flag rate is a measured simulation)
Authoring agent: `opus5-01`
Reviewing agents: none
Created: 2026-07-25
Last updated: 2026-07-25
Dependencies: D-3201 and L-3202 for the kernel (on branch
`agent/gpt56-03-f/39-complex-pick-recheck`); X-5603 for the experiment
Scope: the eight-node ladder `x = 2^-17, 2^-15, 2^-13, 2^-11, 2^-10, 2^-9,
2^-7, 2^-5` at `T = 20225875608341108140435/2^32`, and by extension every
ordinate screened on that ladder at that precision
Related counterexample candidates: the PR #71 full-complex direction, and the
other fourteen ordinates nominated by the same screen

## What is refuted

Not a theorem — a **screening procedure**.  PR #71 and its predecessors nominate
candidate ordinates by computing `lambda_min` of the `8 x 8` Pick matrix

\[
 K_{jk}=\frac{F(s_j)+\overline{F(s_k)}}{x_j+x_k},\qquad s_j=\tfrac12+x_j+iT,
 \qquad F=\xi'/\xi,
\]

from a **128-bit** midpoint matrix, and flagging the ordinates where it comes
out negative.  Fifteen were flagged, the strongest at `-2.626429492911995e-33`.

The claim refuted is that such a flag carries information.  It does not: at
128 bits the reported sign is very close to a fair coin, independent of the
truth.

## The measurement

`experiments/X-5603-pick-noise-floor/noise_floor.py` does this directly rather
than by error propagation.  `F` is evaluated at the eight nodes at `60` digits
(so `lambda_min` is known to far more digits than any effect being measured),
then each value is perturbed by an independent relative error of size `2^{-p}`
— the model of a `p`-bit evaluation delivering one ulp — and `lambda_min` of the
resulting Hermitian matrix is recomputed, `300` times per precision.

The eight kernel values, which reproduce the PR #71 branch's own table:

```text
x        F(1/2 + x + iT)
2^-17    0.01845644433225611743174 - 69.35421781442449000301 i
2^-15    0.07382565097509662734923 - 69.35412704301182148404 i
2^-13    0.2952945175072140705203  - 69.35267474591781810912 i
2^-11    1.180660805135837313714   - 69.32944963663532639405 i
2^-10    2.358017786903983104928   - 69.25527627655380739818 i
2^-9     4.689806662083794295854   - 68.96080441884554969395 i
2^-7     16.90043296353496563381   - 63.73112442064522527592 i
2^-5     28.52997834490482488583   - 35.25150314477706868096 i
```

The true spectrum:

```text
1.2259907375436e-35     <- lambda_min, POSITIVE
4.1619295628207e-26
1.4370244594221e-18
5.676968635931e-12
6.2276450882135e-06
0.17274983428183
76.83977631169
17490.281437779
                        cond = 1.4266243e+39   (39.15 digits)
```

and the noise ladder:

```text
 p     flag rate      median lambda_min    1-sigma spread     most negative seen
128      0.533          -3.855567e-34        2.991161e-33       -5.420745e-33
136      0.173          +1.088397e-35        1.178265e-35       -8.468671e-36
144      0.000          +1.226887e-35        4.450827e-38       +1.217647e-35
148      0.000          +1.225987e-35        2.690745e-39       +1.225509e-35
152      0.000          +1.225988e-35        1.797064e-40       +1.225958e-35
160      0.000          +1.225991e-35        7.029973e-43       +1.225991e-35
176      0.000          +1.225991e-35        9.532328e-48       +1.225991e-35
192      0.000          +1.225991e-35        1.580895e-52       +1.225991e-35
```

## Reading the table

**The true value is positive.**  `lambda_min = +1.2259907375435524056e-35`.

Three routes computed independently during this session agree:

```text
this experiment (dps 60)          1.2259907375435524056e-35
audit A (converged, dps 110/150)  1.22599073754355240557636638065673736047735019e-35
audit B (dps 60)                  1.2259907375436e-35
```

Route A ran a separate evaluator with its own controls — a second,
algebraically distinct product-rule assembly of `\xi'/\xi` as an error
indicator, `lambda_min` by both `mpmath.eighe` and exact-inertia `LDL`
bisection, and all Pick algebra in exact Gaussian rationals — and reports the
value stable to 34 displayed digits from `dps = 80` through `dps = 150`.  Every
digit I computed is confirmed.

Separately, the branch's own 60/70-digit replay reported the *frozen-vector*
Rayleigh quotient `c^*Kc/\|c\|^2 = +1.2260274655534929e-35`.  That is a
different object — a Rayleigh quotient is an upper bound for `lambda_min` — and
the two differ by `2.996 \times 10^{-5}` relative, which is exactly the tilt of
the frozen direction away from the true eigenvector: both audits independently
measured that tilt as `\sin\theta = 9.39\times10^{-8}`, and route A confirmed
that `R(c) - \lambda_{\min} = 3.6728\times10^{-40}` reproduces
`\sin^2\theta\,(\lambda_2-\lambda_1)` to six digits.  So the branch's own
number, correctly interpreted, agrees too.

The noise floor is likewise triply confirmed: the two audits predicted
`5.67e-33` and `5.62e-33` from the Rayleigh error amplification
`\sum_j 2(|\operatorname{Re}\alpha_j|+|\operatorname{Im}\alpha_j|)/\|c\|^2
 = 2.756\times10^4` times `|F|\cdot 2^{-128}`; the simulation above never
exceeded `5.42e-33` in 300 trials.

**The 128-bit spread is `2.99e-33`, which is `244` times the true value.**  The
signal is `244` times below the noise.

**The nominated `-2.626429492911995e-33` is a typical draw.**  It is `0.88`
spreads from the median and well inside the most negative value seen in `300`
trials (`-5.42e-33`).  Nothing about it is anomalous; it is what this
calculation produces when it is run.

**The flag rate at 128 bits is `0.533`.**  At an ordinate where the truth is
positive, the screen says "negative" in `53.3%` of runs.  A procedure whose
output has that little to do with its input cannot nominate anything.  The
fifteen reported negatives, spanning `-2.92e-35` to `-2.63e-33`, all sit under
the noise ceiling and none exceeds it — the signature of a pure noise source
with no signal in it.

**The screen becomes informative between 136 and 144 bits.**  At `p = 136` the
flag rate is already down to `0.173`; by `p = 144` it is zero in 300 trials and
the spread is `0.4%` of the true value.

## The prescription

> **Screen at `>= 160` bits.**  Below `144` the sign is not the matrix's, and
> escalating individual candidates afterwards does not repair a screen that
> nominated them at random.

`160` rather than `144` because `144` is where *this* ordinate clears, with no
margin for one whose true `lambda_min` is smaller — and the spectrum falls by
roughly `3.4e9` per added node, so a ninth node would demand another `~32` bits.
A precision rule keyed to node count belongs in the producer before any wider
scan is run.

## Why the matrix is this ill-conditioned

Not geometry.  The bare Cauchy matrix `1/(x_j+x_k)` on these nodes has condition
number of order `10^5`.  The collapse is analytic: under RH, `K` is a
superposition of rank-one Poisson kernels, one per zero, so an `8 x 8` sample
has trailing eigenvalues that decay super-geometrically — here by a factor of
about `3.4e9` per step at the bottom of the spectrum.  Sampling a positive
operator of infinite rank at eight nodes is what generates the `10^{39}`
condition number, and adding nodes makes it worse, not better.

There is a second, structural cancellation on top of it: `\operatorname{Re} F`
vanishes identically on the critical line by `\xi(s)=\xi(1-s)`, so
`\operatorname{Re} F \propto x` as `x \to 0` and is itself a near-total
cancellation between `\zeta'/\zeta \approx -13.5` and the archimedean part
`\approx +13.52`, while `|F| \approx 69.35`.  The kernel's real part — the part
the positivity question is about — is the small difference of two large
quantities before the matrix is even formed.

## Three reproducibility defects found alongside, reported without claim files

These are not mathematics and are recorded here only because they were found in
the course of the above and would otherwise be lost.  All three concern the
branch `agent/gpt56-03-f/39-complex-pick-recheck`.

1. **The `jm15` replay has no committed code.**
   `results/jm15-independent-precision-ladder.json` is the only artifact; a
   search of the branch's `.py`, `.md` and `.yml` finds nothing that produces
   it.  The FLINT side is committed (`rs_complex_candidate.c`); the "independent
   replay" that overturned the nomination was not, and was therefore unauditable
   until now.
2. **`frozen_vector.canonical_sha256` certifies nothing as recorded.**  The
   digest `591247a0837bd25c...` occurs once in the branch, no canonicalization
   is documented, and no committed code computes it; seven plausible encodings
   were tried and none reproduce it.  The vector itself is fine — it is in the C
   source as `VECTOR_RE`/`VECTOR_IM`, with bit lengths consistent with the
   declared `2^256` scale — so this is a broken seal on sound goods.
3. **The replay ladder's rungs are mislabelled.**  Both audits independently
   found the reported "50 / 60 / 70 digit" rungs delivering far fewer correct
   digits than named, with a roughly uniform shortfall — estimated at `10.5`
   digits by one and `13.2` by the other.  The two estimates do not agree, so
   neither should be quoted as a measurement, but they agree on the sign and on
   the diagnosis: something in that harness is carried at *relative* precision
   where it needs *absolute* precision, `T \approx 4.7\times10^{12}` or a
   Riemann–Siegel phase being the obvious suspects.  Concretely, the "50-digit"
   rung reports `+1.139e-33` where an honest `dps = 50` gives
   `+1.2260274655440e-35` — a factor of `92`.  The conclusion drawn from the
   ladder is unaffected (every rung is positive), but the stated evidence
   "60 and 70 agree to ten figures" is weaker than claimed.

## What is *not* refuted

- **The criterion.**  `K \succeq 0` under RH is correct, and the Gram identity
  `K = \sum_\gamma \varphi_\gamma \varphi_\gamma^*` genuinely requires
  `\operatorname{Re}\rho = 1/2`, so a certified negative would still disprove RH.
  This refutation is about a screen, not about the mathematics behind it.
- **The fourteen certified positive blocks.**  Those were computed at 192 bits
  with directed intervals, where the table above shows a spread of `~1e-52`
  against values of `1e-38` and larger — `10^{13}` of headroom.  They are fine.
- **The branch's honesty.**  PR #71 labels this candidate a probable precision
  ghost and explicitly declines to call it a counterexample or a rigorous
  exclusion.  This refutation supplies the number that was missing, and confirms
  the label.

## Reproduction

```bash
cd experiments/X-5603-pick-noise-floor
python3 noise_floor.py --dps 60 --trials 300
```

Roughly nine minutes for the eight kernel evaluations (`mpmath` `zeta` and
`zeta'` at height `4.7e12`), then a few minutes for the ladder.  Results are
cached in `results/F-nodes.json`.

## Gap audit

1. The "true" `lambda_min` is ordinary high-precision arithmetic, not a directed
   interval.  At `dps = 60` the propagated relative error on a quantity with
   this cancellation is around `10^{-21}`, which is `10^{14}` below the effects
   measured — but it is an estimate, not a bound.  A directed FLINT computation
   at `>= 160` bits would settle the value properly, and the existing workflow
   already accepts the precision as `argv[1]`.
2. The noise model is `\delta F_j = |F_j| \cdot 2^{-p} \cdot (u+iv)` with `u,v`
   uniform on `[-1,1]` and independent across nodes.  A real implementation's
   errors are neither uniform nor independent, and a well-implemented Arb
   evaluation may deliver better than one ulp at the working precision or worse.
   The flag rate is therefore indicative, not exact; what is robust is that the
   noise scale at 128 bits exceeds the signal by more than two orders of
   magnitude, which no plausible reweighting of the model changes.
3. `300` trials resolves a flag rate to about `\pm 0.03`. "`0.000` at `p >= 144`"
   means "below `~0.01`", not "impossible".
4. This is one ordinate.  That the same holds at the other fourteen is an
   inference from the shared node ladder and the shared condition number, not a
   measurement — though the fact that all fifteen reported negatives fall under
   the `5.4e-33` ceiling observed here, and none above it, is consistent with it.
5. Nothing here evaluates whether an off-line zero exists near this ordinate.
   `O-5604` is where that question is answered, by an unrelated route.
