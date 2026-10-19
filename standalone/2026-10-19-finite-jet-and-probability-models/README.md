# Riemann research pass: assessment, fixed-order zero insertion, and global model ambiguity

**Date:** 19 October 2026.

**Outcome:** No new ordinary-zeta zero-free boundary and no RH proof were obtained in this pass. The deliverable is a proposed pair of analytic component theorems, their proofs, exact finite regression checks, and a scoped assessment of the newest repository work. The requested main leap remains unachieved.

**Publication:** Local research packet only. No GitHub branch, commit, or PR was created in this session. The connected GitHub actions exposed here were read-only. Plugin discovery found the installed GitHub integration but no additional write action; the container has no authenticated GitHub CLI workflow established. Repository permissions shown by metadata do not by themselves constitute a usable publishing tool.

## 1. Assessment of the latest work

The initial read covered recent PR metadata back through #955 and selected proof files, not a line-by-line audit of every PR. The final live check included the newly appeared #1005. In particular, this pass did not independently reconstruct the external quasi-RH inputs or replay the repository's original complete theta certificates.

### #1005: a real parameter deduction, but exactly the tiny improvement the user rejects

At frozen head `d3b3d19573b8dc47ac6e37abd108d54982e9e5f1`, `correlated/UNIFORM_BOUNDARY.md` states a conditional ordinary-zeta and family conclusion at

`Re(s) > 43744333/50000000 = 0.87488666`.

It expressly assumes the analytic inputs of Xu–Sang, arXiv:2610.15291v2, including the imported family-wide 7/8 premise. Its improvement over the cited 0.8748867 is `4*10^-8`. The exact parameter arithmetic does not independently establish the upstream analytic inputs. This is not a substantially wider region or an unconditional resolution.

More strategically useful is the exact algebra in `correlated/DIRECT_ESTIMATE_FLOOR.md`. For the unchanged direct-comparison recipe,

\[
B_{\rm low}=\frac{13}{15}+\frac{17k}{60}
+d+\frac{3s_1+s_2}{60},\qquad k,d,s_1,s_2\ge0.
\]

Thus arbitrarily good estimates on the other side do not take this recipe to 5/6. A new direct saving of at least 1/30 is necessary for that target if the principal exponent remains fixed. This is a restriction of the specified estimate, not a theorem restricting actual zeta zeros.

### #1003: useful actual-family estimates, not a critical-line zero-free theorem

At `669b6a01f4d4858ae1ef806b07547be95c08c935`, the actual quadratic-family full-L tail estimate works on fixed compact subsets of `Re(s)>1/2` and admits growing mollifiers. But its optimized full-product residual tends to

\[
|\zeta(s)M_Z(s)-1|^2.
\]

At a hypothetical ordinary-zeta zero this is exactly one. Removing auxiliary random variance does not control the retained ordinary-zeta bias. The half-plane in this family approximation statement must not be called a zero-free half-plane.

The same packet pays a complete native high-frequency tail. Its low-frequency construction rules out a proposed contraction for a broad class of bounded squarefree-supported coefficients, but not for the actual Möbius function. Any successful arithmetic continuation must exploit the exact inversion identity `1*mu=delta_1`, not merely bounded coefficients, squarefree support, smooth balances, or a spectral cutoff.

### Theta: a genuine construction platform, with the all-order step still absent

The order-22/24/26 real-zero approximants are finite Taylor matches, not zero-free heights or real-zero theorems for xi itself. The weighted canonical consumer is a better target than insisting on a positive Ising realization at every stage: cofinal positive weighted power-sum matches would suffice. But those unbounded matches have not been supplied.

The new #1005 kernel-instability note already demonstrates how much finite matching can miss, even for smooth, positive, strongly log-concave perturbations of the actual theta kernel. The new notes here extend particular structural controls rather than claiming to discover the general finite-versus-infinite warning for the first time.

**Research judgment:** Dropping an all-number-fields requirement is sensible when it changes an estimate or the actual observable. Merely changing the name of the target family does not improve the direct exponent. Likewise, a larger finite theta order is not an adequate main progress metric without a source-specific extension mechanism.

## 2. New derivations in this packet

Read [FINITE_JET_ZERO_INSERTION.md](FINITE_JET_ZERO_INSERTION.md) for the first theorem.

A nonsingular fixed-order canonical model can absorb a conjugate node pair

\[
c=\frac1{v(T+iB)^2},\quad\bar c,
\]

while preserving its finite target jet **exactly**, keeping the old nodes positive, and retaining precisely the same envelope `exp(|z|^2/2)`. In physical coordinates the auxiliary function has four prescribed nonreal zeros `+/-T +/-iB`. The canonical quadratic-mass increase is exactly

\[
\frac{16T^2B^2}{v^2(T^2+B^2)^4}.
\]

Its theta application is through order 26 and depends on the frozen finite source result. This function is not asserted to be a characteristic function of a positive law.

Read [PROBABILITY_MODEL_AMBIGUITY.md](PROBABILITY_MODEL_AMBIGUITY.md) for the stronger probability construction.

Starting from a locally nonsingular finite ferromagnetic realization, attach a tiny three-point law, a harmonic Rademacher tail and a many-small-spin support correction, then retune the finite source cumulants exactly. This gives a nonnegative real-analytic probability density with the target finite moments, variance-controlled Gaussian envelope, all zeros confined to a prescribed strip, and arbitrarily high nonreal zeros on its boundary. The construction can simultaneously match both leading xi growth terms, both main zero-count terms (with an `O(sqrt(T))` remainder, not zeta's sharper remainder), and the leading theta logarithmic tail rate. An all-real-zero companion exists with the same stated data.

The theta application of this second theorem is through order **20**, consuming #994's finite Ising theorem. It must not be promoted to order 26 by combining the scopes of the two notes. Its very large finite model has not been numerically instantiated here.

These are auxiliary-model theorems, not the requested zeta boundary. Their role is to specify sharply which attractive finite/global-looking checks still leave the decisive all-order/source-specific issue untouched.

## 3. What was actually executed

Run from this directory:

```sh
python -I -S -B check.py
python -I -S -O -B check.py
```

The standard-library checker performs 25 recorded component checks, including 4,950 exact integer comparisons of two harmonic zero-count implementations and 15 exact complex-rational insertion checks. It also verifies a coarse bound on the source's twelve active-node separations, an explicit inverse-Vandermonde norm bound, a contraction perturbation budget and an exact synthetic four-moment probability repair.

The source excerpt is manually transcribed into coarse outward intervals. It is not a replacement for the original 128-node source or theta integration. The original Gaussian-reserve guard has not been independently replayed. The receipt therefore explicitly says `COMPONENT_CHECKS_PASS; THETA_SOURCE_REPLAY_NOT_RUN`.

The analytic proofs, the external inputs and the source finite realization have not been checked by an independent mathematician, a separate research agent, or a proof assistant in this session. Finite arithmetic checks do not upgrade their status.

## 4. The actual remaining work

The most direct arithmetic target is a genuinely new bound for the signed ordinary source or a new primary numerator estimate that changes the direct floor. A broad coefficient-norm estimate has already been excluded in the source packet, and a family-average residual still equal to one at a common zero does not close the argument.

On the theta side, the target should be one source-specific theorem that generates feasible positive moments at unbounded orders, or a strip-preserving approximation theorem with a proved expanding-domain error. The results here do not disprove either possibility. They explain why finite fitting, even decorated with matching leading growth, is not that theorem.

## 5. Source identities

* PR #1003: `669b6a01f4d4858ae1ef806b07547be95c08c935`; theta Gaussian proof, weighted canonical proof, power-sum extension, actual-family proof, and low-frequency attack.
* PR #994: `c93ca65a510b6acaf167f929b9bf7e67d742b05a`; `theta/PROOF20.md`.
* PR #1005: `d3b3d19573b8dc47ac6e37abd108d54982e9e5f1`; `correlated/UNIFORM_BOUNDARY.md`, `correlated/DIRECT_ESTIMATE_FLOOR.md`, and `theta/KERNEL_STRIP_INSTABILITY.md`.
* Newman and Wu, *Constants of de Bruijn-Newman type in analytic number theory and statistical physics*, arXiv:1901.06596v2. Primary full text: https://arxiv.org/html/1901.06596v2 . Used for the classical theta/Lee-Yang context, not as a proof of any RH premise.

The package is add-only and changes no inherited repository file. The included manifest authenticates these local bytes, not publication to GitHub or independent mathematical acceptance.
