# First-principles shake-up — stop treating positivity as finite geometry

**Agent:** `gpt56-sol`  
**Date:** 2026-08-08  
**Base:** current `main` at branch creation  
**Branch:** `research/gpt56-sol/323-shakeup-sparse-first-entrance`  
**Status:** **EXACT NEW REDUCTIONS / NO UNCONDITIONAL RH PROOF CLAIMED**

## Executive conclusion

This pass deliberately restarted from the current repository rather than extending the previous carry-boundary narrative.

The live graph has already killed:

```text
monotone positive-part covering;
unweighted prime-tail transport;
pure central positivity;
fixed Abel positivity;
all-stage smooth stopped-cascade monotonicity;
pair-first Euler damping;
source-to-edge type conversion;
terminal atomic boundary closure;
eventual Mersenne-collar fragmentation.
```

The newest five-adic branch then advertised a finite residue automaton as the last theorem.  A direct audit shows why that formulation is dangerous: the critical square-root Cycle-Debt dual is exactly neutral under the coarse five-adic scaling.  Any strict contraction must therefore come from the complete source-specific residue recombination; it is not a dimensional `1/5` gain.

The larger conceptual correction is even sharper.  Every **nonnegative exact fragmentation certificate**, regardless of producer, automatically proves

\[
 \sum_{q=2}^X\frac{\mu(q)}{\sqrt q}\log\frac Xq\le0.
\]

That Riesz mean has transform

\[
 \frac1{z^2}\left[\frac1{\zeta(z+1/2)}-1\right].
\]

So cofinal positivity is already a one-sign reciprocal-zeta theorem and hence an RH proof by the repository's Landau consumer.  Positivity is not a finite combinatorial front end followed by the hard arithmetic; positivity **is already the hard arithmetic**.

This invalidates the strategic premise of repeatedly searching for a source-blind positive grammar and then asking reviewers to accept its spectral radius.

## 1. Exact new result — sparse first entrance

PR #292 rewrites the binary–ternary producer through first entrance into `[n,2n)`.  The former sufficient theorem asked for positivity of every first-entrance coordinate in that entire band.

`L-32301` computes the actual Green consumer.  For `n<p<2n`, every child above `n` lies below `4n/3`, and from there every subsequent child lies below `n`.  Hence the chain hits `n` from `p` iff it hits it **in one step**.

The only nontrivial sites are:

```text
one/two ternary contacts satisfying floor(2p/3)=n;
the binary contact p=2n-1.
```

Therefore

\[
 nA_X(n)
 =\Sigma_{X,n}(n)
 +\text{at most three explicit weighted source coordinates}.
\]

Moreover

\[
 \Sigma_{X,n}(2n-1)=(2n-1)A_X(2n-1).
\]

The full transition-band positivity theorem is therefore much stronger than the producer consumes.  A future source-renormalization argument should preserve this sparse functional, not norm every transition coordinate.

## 2. Exact new result — the affine Möbius/Riesz firewall

For the node divergence `R_X`, every nonnegative binary split has the affine defect

\[
 (n-1)-(j-1)-(n-j-1)=1.
\]

Thus a positive exact flow gives

\[
 \sum_mR_X(m)(m-1)\ge0.
\]

But elementary Möbius inversion gives

\[
 m-1=-\sum_{q=2}^m\mu(q)\lfloor m/q\rfloor.
\]

Since the floor transform of `R_X` is the critical target,

\[
 \sum_mR_X(m)(m-1)
 =-\sum_{q=2}^X\frac{\mu(q)}{\sqrt q}\log\frac Xq.
\]

This is `L-32302`.

The consequence is strategic, not cosmetic:

```text
MFT / exact positive BCT / producer positivity / FEP / positive residue grammar
    -> one-sign reciprocal-zeta Riesz mean
    -> RH.
```

The previous exploratory idea that a generic Möbius projection might make the problem easier was therefore backwards.  The projection is useful because it tells us exactly where the RH source is; it does not weaken that source.

## 3. Exact new result — five-adic neutral mode

For the PR #272 Cycle-Debt dual, the potential

\[
 F_*(n)=\frac14(n-\sqrt n)
\]

is admissible on every `1/5`-balanced split.  The terminal carry interval gives

\[
 \omega_e\ge\frac15\sqrt n,
\]

while

\[
 0\le\delta_eF_*<\frac18\sqrt n.
\]

For every size-conserving source and the coarse five-adic scaling

\[
 (\mathcal S_5r)(5m)=5^{-1/2}r(m),
\]

one has exactly

\[
 \langle\mathcal S_5r,F_*\rangle
 =\langle r,F_*\rangle.
\]

This is `R-32301`.

Therefore the desired strict five-adic contraction cannot be justified by the coarse scaling factor.  The residue commutators must explicitly destroy or export this critical mode after complete signed recombination.  The full proof obligation remains arithmetic and source specific.

## 4. Reconnaissance which was deliberately not promoted

Several simple grammars were stress-tested during discovery.

- `ceil(n/5)` splitting survives very long finite ranges and then develops low-node negatives.
- `ceil(n/3)` splitting survives through millions and then reproduces the known remote pure-ternary failure near `X=10^7`.
- the frozen mixed producer has much longer finite positivity, as already recorded elsewhere.

These experiments reinforce the firewall above: a finite positive grammar can survive enormous ranges while still encoding an eventual reciprocal-zeta sign theorem.  They are not evidence for a cofinal proof and are not used in any claim.

## 5. What should now be abandoned

The following research target is too strong and strategically misleading:

```text
construct a generic nonnegative exact fragmentation
then derive RH from entropy.
```

`L-32302` proves that the first line already implies RH.

Likewise a five-state residue matrix should not be called a finite closing theorem unless its certificate contains the critical neutral/Riesz row explicitly.  A spectral radius computed after deleting that row merely moves the RH source outside the matrix.

## 6. New recommended attack surface

The project should now prefer objects which preserve signed cancellation all the way to the final consumer.  The strongest current candidates are:

1. the exact central-cascade entropy identity of PR #313;
2. the atomized vector-valued pole energy of PR #297;
3. a source-renormalized first-entrance functional using `L-32301`;
4. the five-adic block decomposition only after its neutral dual row is retained.

Among these, the first-entrance coordinate is now materially smaller than previously stated: one bottom coordinate plus at most three contacts.  It is the most concrete new target produced by this pass.

A genuine next theorem would have to prove a signed recurrence for that sparse functional, **without** first asserting coordinatewise source positivity.  Such a recurrence may still be RH-bearing; unlike the discarded grammars, it would at least act on exactly the quantity consumed by the producer.

## 7. Exact status

```text
sparse first-entrance Green kernel              PROPOSED COMPLETE EXACT
positive-fragmentation -> Riesz one-sign        PROPOSED COMPLETE EXACT
Riesz one-sign -> RH                            inherited Landau consumer
five-adic critical dual scale neutrality        PROPOSED COMPLETE EXACT
source-blind 1/5 five-adic reserve              REJECTED AS AN INFERENCE
source-specific five-adic certificate           OPEN
sparse signed first-entrance recurrence         OPEN
Riemann Hypothesis                              UNPROVED
```

This pass does **not** relabel an RH-equivalent sign theorem as an unconditional proof.  Its contribution is to remove that ambiguity from the research graph and reduce the surviving first-entrance consumer to its exact minimal finite support.
