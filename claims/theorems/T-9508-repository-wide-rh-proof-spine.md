# T-9508 — Repository-wide proposed proof spine for RH

Claim ID: `T-9508`  
Title: The critical signed-correlation estimate implies the Riemann Hypothesis through the analytic-totient energy  
Status: **PROPOSED PROOF CANDIDATE — blocked at open lemma `L-9515`; RH is not claimed proved**  
Authoring agent: `gpt56-08`  
Created: 2026-08-07  
Frozen dependencies: PR #202 square screw; PRs #216/#222/#224 prime energy;
PR #217 variance defect; PR #218 transport; PR #226 analytic-totient energy;
PR #229 common-gate synthesis

## 1. Exact arithmetic state

Define
\[
E^{\rm AN}(x)
=
\frac12\left(
1+\sum_{d=1}^{\infty}\mu(d)\left\{\frac xd\right\}^{2}
\right).
\]

`L-9512` proves
\[
E^{\rm AN}(x)
=
-\left[
\sum_{n<x}\frac{\varphi(n)}n(x-n)-\frac3{\pi^2}x^2
\right].
\]

For \(\Re s>2\),
\[
\boxed{
\int_1^\infty E^{\rm AN}(x)x^{-s-1}\,dx
=
-\frac{\zeta(s-1)}{s(s-1)\zeta(s)}
+\frac{3/\pi^2}{s-2}.
}
\tag{T-9508.1}
\]

The apparent pole at \(s=2\) cancels. Every nontrivial zero \(\rho\) of
\(\zeta\) produces a genuine pole at \(s=\rho\), because
\(\zeta(\rho-1)\ne0\).

## 2. Positive moment criterion

Assume
\[
\boxed{
\int_X^{2X}|E^{\rm AN}(t)|^2\,dt
\ll_\varepsilon X^{2+\varepsilon}
}
\tag{T-9508.2}
\]
for every \(\varepsilon>0\).

Fix \(\sigma>1/2\) and choose
\(\varepsilon<2\sigma-1\). Cauchy–Schwarz on a dyadic block gives
\[
\int_Y^{2Y}|E^{\rm AN}(x)|x^{-\sigma-1}\,dx
\ll_\varepsilon
Y^{-(\sigma-1/2-\varepsilon/2)}.
\]
The dyadic series converges normally. Therefore the Mellin integral in
(T-9508.1) is holomorphic throughout
\[
\Re s>\frac12.
\]

A zero \(\rho\) with \(\Re\rho>1/2\) would create a genuine pole in that
half-plane, contradiction. Functional-equation symmetry then places every
nontrivial zero on the critical line. Hence (T-9508.2) implies RH.

This is the complete transfer theorem `T-9506`.

## 3. Production of the moment from the critical correlation lemma

Insert a smooth dyadic partition in the denominator variable in the exact
fractional-part representation of \(E^{\rm AN}\). Keep the two nonperiodic
Mertens tails and the periodic Bernoulli channels in the same packet.

For each denominator block:

1. Fourier-expand the periodic channel;
2. group equal rational frequencies;
3. evaluate the exact-resonance contribution through the Jordan-totient square
   of `L-9513`;
4. bound separated frequencies by integration by parts and the ordinary large
   sieve;
5. apply `L-9515` to the critical near-resonance cluster.

The exact resonance is \(O(D^2)\) on an interval of length \(D\). The separated
and Fourier-tail pieces have the same bound. `L-9515` supplies it for the only
remaining cluster. Summing the logarithmically many dyadic blocks and absorbing
logarithms into \(X^\varepsilon\) yields (T-9508.2).

Therefore
\[
\boxed{
L\text{-9515}\Longrightarrow T\text{-9508.2}\Longrightarrow\mathrm{RH}.
}
\tag{T-9508.3}
\]

## 4. Independent repository cross-checks

The same missing estimate is represented elsewhere as:

- eventual/subpolynomial square-screw negativity (`T-19801`);
- the constant square-support D-0001 coordinate (PR #208);
- balanced signed semiprime Type-II cells (PR #222);
- locally uniform vertical prime Hardy energy (PR #224);
- dyadic transport reserve minus Bregman curvature (PR #218);
- the common correlation gate `L-23002` (PR #229).

The off-line-zero consequence is independently phase-free:
\[
D_{\rm off}
=
4\sum_{\delta>0,\gamma>0}
m_\rho\frac{\gamma^2-\delta^2}{(\gamma^2+\delta^2)^2}
\ge0,
\]
with equality exactly under RH (`T-21702`).

These are consistency checks on normalization and scope. None substitutes for
`L-9515`.

## 5. Why this is not currently a proof

The chain after `L-9515` is complete. The proof attempt inside `L-9515`,
however, stops at the critical balanced Type-II/major-arc estimate. That estimate
has not been obtained from an accepted dispersion, Kuznetsov, large-sieve or
Möbius-correlation theorem.

It would be mathematically incorrect to call (T-9508.3) an unconditional proof
of RH until that step is supplied.

## 6. Reviewer order

1. `L-9512` and the Mellin normalization;
2. `T-9506` / Section 2 above;
3. `L-9513` exact resonance factorization;
4. `R-9506` coefficient-blind obstruction;
5. `L-9515`, especially its Step 5;
6. the dyadic assembly in Section 3;
7. cross-check against `L-23002` and `T-23001`.

## 7. Exact verdict

```text
Repository-wide conditional proof spine: complete
Exact resonance and far-frequency pieces: complete
Critical signed near-resonance estimate: open
Full proposed resolution of RH: not reached
RH: not proved
```
