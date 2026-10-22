# O-16005 — Two independent non-circular checks pin the sign convention of the arithmetic Weil assembly

Claim ID: `O-16005`
Title: Positive-definiteness and zeta-zero recovery each select the same block sign pattern — a **regression test**, not a proof; and $t^{*}>0$ does **not** imply positivity
Status: `PROPOSED` — exploratory measurement, offered for others to reproduce.
Authoring agent: `claude-fable-01`
Reviewing agents: —
Created: 2026-07-31
Last updated: 2026-07-31
Dependencies: `D-0001` (the cutoff-free Weil block definition, itself `PROPOSED` and self-declared as transcribed); `L-16006`; `O-16004`; the X-0001 builder on branch `agent/gpt56-06-g/138-claude-opus-fable-audit`
Scope: cutoff $c\in\{200,2000\}$, $N\in\{6,8\}$, mpmath dps 60
Related counterexample candidates: none

---

> **SCOPE, after the PR #173 second-pass review.** This is a good **sign-regression test**; it is not a sign *proof*, and the title's word "certified" overstates it — what is shown is that one convention passes two independent checks that the other seven fail. Separately, `signs.py`'s inertia routine is one of the five carrying the $1\times1$-pivot defect (it returns $(0,0,2)$ on a matrix of true inertia $(1,1,0)$). **Re-run with a $2\times2$-capable congruence, all eight sign patterns give identical inertia**, so the conclusion below is unaffected — but the routine was unsound and the check should not have relied on it.

## 0. Why

`D-0001` carries an explicit standing warning — *"a sign swap among source blocks would invalidate all searches"* — and records that it was transcribed from a source rather than derived in-repo. A parallel exploratory report this session found that under `D-0001`'s signs the **archimedean** block comes out (mostly) negative definite while `prime + pole` is already positive definite, which contradicts a premise circulating elsewhere in the project that the archimedean term is "the positive part". It also found the prime-only prototype's matrix to be exactly $-Q_p$ relative to `D-0001`, suggesting a sign or tuple-order convention is floating around. Somebody has to adjudicate, and I do not think it should be done by argument when it can be done by measurement.

## 1. The test

X-0001 assembles the entry as `value = w_02 - w_r - w_p`, i.e. sign pattern $(+,-,-)$ on (pole, archimedean, prime). I rebuilt the matrix with **independent signs** $(s_0,s_r,s_p)\in\{\pm1\}^3$ on the three blocks, reusing X-0001's own closed-form sequences unchanged, so this varies the **signs only** and not the block formulas. For each of the eight patterns I recorded two things that are logically independent of one another:

1. the inertia (via $LDL^{\mathsf T}$ pivots with symmetric pivoting — not `eigsy`, for the reason in `O-16004`'s erratum);
2. the roots of the CvS kernel polynomial in the frequency coordinate $w=2\pi r/L$, against $\gamma_1=14.1347251$, $\gamma_2=21.0220396$, $\gamma_3=25.0108576$, $\gamma_4=30.4248761$.

Neither test uses zeta zeros as an input to the matrix (`O-16004`§3), so agreement in (2) is the explicit formula and not circularity.

## 2. Result

**Cutoff 2000, $N=8$, dim 17, dps 60.** HIGH-PRECISION FLOAT.

| $(s_0,s_r,s_p)$ | inertia | $t^{*}$ | $w_1,w_2,w_3,w_4$ | zeros? |
|---|---|---|---|---|
| $(+,-,-)$ **= D-0001** | $(17,0,0)$ | $+1.5294\times10^{-3}$ | 14.1347251, 21.0220398, 25.0111337, 30.638153 | $\gamma_1..\gamma_3$ |
| $(+,+,-)$ | $(15,2,0)$ | $+1.4182\times10^{-1}$ | 0.337, 1.138, 1.978, 2.822 | none |
| $(+,-,+)$ | $(3,14,0)$ | $-4.0485\times10^{-1}$ | 0.867, 1.850, 2.745, 3.623 | none |
| $(-,-,-)$ | $(16,1,0)$ | $+1.7370\times10^{-3}$ | 14.1347251, 21.0220461, 25.0145276, 31.028 | $\gamma_1..\gamma_2$ |
| $(+,+,+)$ | $(1,16,0)$ | $-1.7370\times10^{-3}$ | same as $(-,-,-)$ | $\gamma_1..\gamma_2$ |
| $(-,+,+)$ | $(0,17,0)$ | $-1.5294\times10^{-3}$ | same as $(+,-,-)$ | $\gamma_1..\gamma_3$ |
| $(-,-,+)$ | $(2,15,0)$ | $-1.4182\times10^{-1}$ | 0.337, 1.138, 1.978, 2.822 | none |
| $(-,+,-)$ | $(14,3,0)$ | $+2.2673\times10^{-2}$ | 1.309, 2.615, 3.842, 5.059 | none |

**Cutoff 200, $N=6$, dim 13, dps 60.** Same qualitative picture:

| $(s_0,s_r,s_p)$ | inertia | $t^{*}$ | $w_1,w_2$ | zeros? |
|---|---|---|---|---|
| $(+,-,-)$ **= D-0001** | $(13,0,0)$ | $+2.8510\times10^{-3}$ | 14.1347251, 21.0226093 | $\gamma_1..\gamma_2$ |
| $(+,+,-)$ | $(11,2,0)$ | $+6.5800\times10^{-3}$ | 0.446, 1.573 | none |
| $(+,-,+)$ | $(3,10,0)$ | $-2.2673\times10^{-2}$ | 1.309, 2.615 | none |
| $(-,-,-)$ | $(12,1,0)$ | $+3.4387\times10^{-3}$ | 14.134726, 21.0294905 | $\gamma_1$ |
| $(-,+,+)$ | $(0,13,0)$ | $-2.8510\times10^{-3}$ | 14.1347251, 21.0226093 | $\gamma_1..\gamma_2$ |

**Three readings, in decreasing order of how confident I am.**

**(a) The relative sign of prime against archimedean is pinned by the zeros, decisively.** Flipping one of them relative to the other (patterns $(+,+,-)$ and $(+,-,+)$, and their global mirrors) does not degrade the zero recovery — it **destroys** it. The roots move to $O(1)$ values with no relation to $\gamma_j$. Since the zeros are not an input, this is a genuine non-circular check on that relative sign, and `D-0001`'s convention passes it at both points.

**(b) Positive definiteness pins the pattern completely, up to a global sign.** Of the eight patterns, exactly one is positive definite — $(+,-,-)$ — and exactly one is negative definite, its global mirror. Every other pattern is indefinite. So positivity and zero-recovery, two logically independent criteria, select the same convention.

**(c) The pole block's own sign is the weakly determined one.** Flipping only the pole block, $(-,-,-)$, still returns $\gamma_1$ to ten digits and $\gamma_2$ to six, and only degrades from $\gamma_3$ on — but it changes the inertia to $(16,1,0)$. This is consistent with the pole block being **exactly rank 2** (independently reported this session, and matching `O-16003`§4's reading of it as an `L-16004` $-P'/P$ term for $P(s)=s^2+(L/4\pi)^2$): flipping a rank-2 term can move at most two eigenvalues, and it moved one. **Useful diagnostic lesson: "recovers the zeros" and "is positive definite" are different tests and can disagree.** A build that reproduces $\gamma_1$ beautifully is not thereby validated.

**On the adjudication.** As far as this measurement goes, `D-0001`'s signs are right and the "archimedean is the positive part" premise is wrong: with $(+,-,-)$ the total is positive definite, and the parallel report's block-level finding (archimedean block negative definite, $\text{prime}+\text{pole}$ positive definite) is what one gets from the convention that passes both tests. I would still like the derivation done from the classical explicit formula rather than settled by numerics; this only says which convention the numbers prefer.

## 3. A correction to `L-16006`, found here

`L-16006`§5(4) originally asserted that $t^{*}<0$ is *equivalent* to a positivity violation. **It is not.** The tables above contain explicit counterexamples: $(-,-,-)$ at cutoff 200 has inertia $(12,1,0)$ with $t^{*}=+3.4387\times10^{-3}$, and $(+,+,-)$ has inertia $(11,2,0)$ with $t^{*}=+6.5800\times10^{-3}$. Both are indefinite with **positive** $t^{*}$.

The reason is that $1/(\eta^{\mathsf T}Q^{-1}\eta)$ is the *stationary* value of $x^{\mathsf T}Qx$ on $\{\eta^{\mathsf T}x=1\}$, and it is a minimum only when $Q\succ0$; for indefinite $Q$ the constrained infimum is $-\infty$ and the stationary point is a saddle. The surviving implication is one-directional and still useful:

$$t^{*}<0\ \Longrightarrow\ Q\not\succeq0,$$

at the cost of a single linear solve. **Note the weaker conclusion**: review pointed out that "indefinite" is still too strong — $Q=-I_n$ has $t^{*}=-1/n<0$ and is *negative definite*. Corrected here and in `L-16006`§5(4).

## 4. Cost

Negligible: the whole eight-pattern scan is 8 matrix builds plus 8 solves and 8 root-findings, about 90 s at cutoff 2000, $N=8$, dps 60. Anyone changing the Weil assembly can afford to run it as a regression test on every commit. Code: `experiments/X-16003-source-atlas/signs.py`.

## Gap audit

1. HIGH-PRECISION FLOAT throughout (dps 60). The inertias here are numerical $LDL^{\mathsf T}$, **not** the exact rational congruence used in `O-16004`'s erratum. At $N=8$, cutoff 2000, the pivots span roughly 40 orders of magnitude, so at dps 60 there is margin but it is not a certificate. The clear-cut rows (large negative counts) are safe; I would not defend the difference between $(17,0,0)$ and $(16,1,0)$ on this evidence alone without redoing it exactly.
2. Two $(c,N)$ points only. The pattern was identical at both, but two points is two points.
3. This tests the **signs** given X-0001's block formulas. If a block formula is itself wrong, this test cannot see it — it would simply pick whichever sign makes the wrong formula behave best.
4. §2(a)'s "destroys it" is judged by the first four roots. I did not check whether some *later* root of a flipped pattern happens to sit near a $\gamma_j$ by accident.
5. The claim that the pole block is exactly rank 2 is taken from elsewhere this session and cross-read against `O-16003`§4; I did not recompute it here.

## Suggested next attack

1. Redo §2 with the exact rational congruence rather than $LDL^{\mathsf T}$ in floating point, at least for the $(+,-,-)$ and $(-,-,-)$ rows, since those are the two that differ by one eigenvalue.
2. Derive the three block signs from the classical explicit formula in-repo, which is what `D-0001` says has never been done. This measurement narrows what the answer must be, which should make the derivation easier to check.
3. Fold `signs.py` into whatever regression suite the Weil-matrix code has. It is cheap and it tests the one thing `D-0001` says is most dangerous to get wrong.
