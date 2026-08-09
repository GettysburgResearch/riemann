# Extra-high redo and shake-up — Gamma–carry martingale route

Date: 2026-08-08  
Agent: `gpt56-sol`  
Issue: #331  
Status: **NEW UNCONDITIONAL THEOREM + FULL CONDITIONAL FINITE-LIFT PROPOSAL; RH UNPROVED**

## 1. Why the previous pass was redone

The live repository moved materially after the earlier band/Pascal pass. The redo begins from the newest status rather than from the stale frontier.

The relevant corrections are:

1. PR #323 proves that radix-five residue states contain genuine nonprincipal Dirichlet-`L` channels. A finite five-state automaton is therefore not a harmless bookkeeping device.
2. PR #323 proves that the eta-comb multiplier is exactly one at every zeta-zero mode. Source-blind translation-invariant strict contraction cannot contain the RH-bearing physical mode.
3. PR #324 closes a strict analytic shifted-power contraction but leaves the propagated cap-interface channel open.
4. PRs #311/#315/#317 establish that absolute atomwise boundary norms can be macroscopically wrong; recombination before variation is essential.
5. PR #276 identifies `WSTS` as RH-equivalent, so merely producing another scalar shell estimate is not progress unless a new mechanism proves it.

These facts rule out treating the last pass's generic collector-Sobolev contraction as a completed route.

## 2. New theorem: the carry law sits below an exponential

For the exact carry variable

\[
T=\log\frac{M(M+1)}{M+U},
\qquad
M=\lfloor V^{-2}\rfloor,
\]

with independent `Beta(2,1)` variables `U,V`, `L-33101` proves

\[
\boxed{\mathbb P(T>t)\le e^{-t}.}
\]

The proof is one line after writing `x=e^t=m+y`:

\[
x^2+m(m+1-x)^2-(m+1)x
=(m+1)y(y-1)\le0.
\]

This is an exact all-scale statement, not asymptotics or numerical reconnaissance.

## 3. New theorem: centered carry is below Gamma in convex order

The exact carry mean is

\[
\mathbb ET=\frac32-\gamma.
\]

Let

\[
C=\frac52+\gamma,
\]

so `E(T+C)=4`. For

\[
G\sim\operatorname{Gamma}(2,1/2),
\]

`L-33101` proves, by complete stop-loss comparison,

\[
\boxed{T+C\le_{\rm cx}G.}
\]

The proof uses only:

- the exact tail theorem above;
- `SL_T(b)<=e^{-b}`;
- the explicit Gamma stop-loss
  \[
  SL_G(a)=(a+4)e^{-a/2};
  \]
- the elementary bound `0<gamma<1` and an explicit series proof `e^2<15/2`.

Consequently there is a martingale coupling

\[
X\overset d=T+C,
\qquad
Y\overset d=G,
\qquad
\mathbb E[Y\mid X]=X.
\]

This is strictly stronger than the previously used scalar Laplace order and structurally different from the still-open independent convolution factor `GCF`.

## 4. The Gamma law is already Pascal geometry

`L-33102` gives the finite/continuum dictionary.

Choose a uniform split ratio `R`. Follow a uniformly selected unit of parent mass into one of the two children. The selected fraction `V` has density

\[
2v\,dv,
\]

so `V~Beta(2,1)`.

At finite parent size `n`, choose `J` uniformly from `0,...,n` and then follow a size-biased child. Its exact size law is

\[
\boxed{\mathbb P(K=k)=\frac{2k}{n(n+1)}}.
\]

Thus the two `Beta(2,1)` variables generating the Gamma target are precisely the scaling limits of two size-biased uniform Pascal splits.

The sharp Gamma target is therefore not an unrelated smoothing distribution. It belongs to the same fragmentation geometry as the atomized carry cone.

## 5. New full proposal: Martingale Pascal Lift

The natural replacement for independent convolution is now:

```text
carry law
 -> exact mean shift
 -> convex-order martingale to Gamma
 -> exact finite size-biased Pascal state
 -> Pascal fundamental cycles
 -> subpower cycle debt
 -> sharp prime ramp
 -> square-screw/Landau
 -> RH.
```

`T-33101` defines the finite certificate `MPL(X)`.

It must preserve every carry column exactly and export a subpower optimized negative-capacity debt. A scale-stationary scalar residual is forbidden: that would simply return to `GCF`.

The continuum martingale theorem is **proved in this branch**. The finite arithmetic martingale-to-Pascal lift is not.

## 6. Why this is genuinely different from the recent contraction routes

The new theorem does not claim that the eta operator, a radix-five residue automaton, or a source-blind analytic norm contracts the RH-bearing zero mode. PR #323 rules such claims out.

Instead the Gamma target is reached by a mean-preserving spread. Martingale transport is permitted to move state in both directions around the centered carry variable, while retaining exact barycenters. This is the type of state dependence that the scalar convolution route erased.

The proposal is therefore compatible with the known zero-mode firewall.

## 7. Exact regression

`X-33101` replays 51,600 rational instances of the exact tail polynomial identity and the rational exponential-series bound

```text
e^2 < 1663/225 < 15/2.
```

Retained proof-object digest:

```text
cafe6bbaeeac3fd6eedb18ff225f5637f3f76b08c46d57320f0c5b1d62b5f4cc
```

The checker verifies finite algebra only; the stop-loss proof itself is analytic and written completely in `L-33101`.

## 8. Honest global status

```text
extra-high live-repo redo                    COMPLETE
five-adic harmless-automaton assumption      REJECTED BY LIVE CHARACTER FIREWALL
source-blind eta contraction                 REJECTED AT ZERO MODES
Gamma-carry tail theorem                     PROPOSED COMPLETE EXACT
centered convex-order theorem                PROPOSED COMPLETE EXACT
finite Pascal size-biased dictionary         PROPOSED COMPLETE EXACT
martingale coupling existence                STANDARD CONSEQUENCE
finite cofinal Martingale Pascal Lift        OPEN / RH-BEARING
MPL -> prime ramp -> RH                      COMPLETE CONDITIONAL COMPOSITION
Riemann Hypothesis                           UNPROVED
```

A full unconditional RH proof is **not** claimed. The shake-up has produced a new proved structural theorem and moved the search from strict contraction/independent convolution to martingale transport inside the exact Pascal geometry.
