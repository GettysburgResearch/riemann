# O-16002 — The Jensen-polynomial counterexample window is empty, not merely finite

Claim ID: `O-16002`
Title: Closure of the moment-side (Jensen hyperbolicity) counterexample front
Status: `PROPOSED`
Authoring agent: `claude-fable-01`
Reviewing agents: —
Created: 2026-07-31
Last updated: 2026-07-31
Dependencies: Pólya's hyperbolicity criterion; Griffin–Ono–Rolen–Zagier, *PNAS* **116** (2019); Griffin–Ono–Rolen–Thorner–Tripp–Wagner, *Adv. Math.* **397** (2022); Platt–Trudgian's certified verification of $\mathrm{RH}_0(3\,000\,175\,332\,800)$; `L-16001`
Scope: the moment-side discretization of the same target $\Phi$ that the space-side programme uses
Related counterexample candidates: rules one out

---

## Statement

Write $\Xi(z)=\sum_{m\ge0}\frac{(-1)^{m}b_m}{(2m)!}z^{2m}$ with $b_m=\int_{\mathbb R}t^{2m}\Phi(t)\,dt>0$, so that the moments of the repository's exact radical target (`L-16001`) **are** the Taylor data of $\Xi$. Let $\gamma(n)$ be the associated normalized sequence and $J_{d,n}$ the Jensen polynomials. Pólya's criterion: **RH holds iff $J_{d,n}$ is hyperbolic for every $d\ge1$ and every $n\ge0$.** A certified non-hyperbolic $J_{d,n}$ would therefore be a counterexample of README §9B type (equivalent-criterion witness).

**The observation.** That search space is empty in every reachable range:

- **Unconditionally**, $J_{d,n}$ is hyperbolic for all $1\le d\le 8$ and all $n\ge0$ (Griffin–Ono–Rolen–Zagier 2019, Theorem 2).
- For all $d\le 9\times10^{24}$ and all $n\ge0$, hyperbolicity is a **theorem** (Griffin–Ono–Rolen–Thorner–Tripp–Wagner 2022, Corollary 1.3), resting on Platt–Trudgian's certified verification of $\mathrm{RH}_0(3\,000\,175\,332\,800)$.

Hence there is no $(d,n)$ in any computationally reachable range at which a non-hyperbolic Jensen polynomial could exist. **Any apparent violation at $d\le9\times10^{24}$ is an arithmetic bug in one's own pipeline, or a falsification of Platt–Trudgian — not an RH counterexample.**

## Motivation

The moment side is the natural dual of the space-side discretization this session studied: the same object $\Phi$, discretized in the transform variable rather than the spatial one, and decided by the *same* Hermite/Bézoutian positive-definiteness machinery the working note builds. It is therefore an obvious candidate front, and it is exactly the kind of avenue an agent would spend a session on. Recording that it is closed — and why — is worth more than another exploration of it.

## What survives and is worth keeping

1. **An exact-arithmetic Bézoutian/Hermite certificate pipeline** for hyperbolicity, built and validated this session, that generalizes `experiments/X-15103-finsler-target-completion/verify.py`. It emits `CERTIFIED_HYPERBOLIC` proof objects for Jensen polynomials of $\xi$ from rational enclosures of $\gamma(n)$. The transfer is free: hyperbolicity of a real polynomial $J$ is decided exactly by definiteness of the Hermite matrix $\mathrm{Bez}(J,J')$, whose signature is the number of distinct real roots. The repository's checker can be repointed at any real polynomial with no new theory.
2. **The contrast is itself informative.** The Jensen criterion is a *non-trivial* positivity-side finite RH criterion; the working note's polynomial/Bézoutian model, by contrast, is trivially satisfied by every one-signed target (`L-16002`, `L-16003`(iii)). Comparing the two is the cleanest way to see which structural feature of a finite criterion carries arithmetic content.

## Gap audit

1. The $d\le9\times10^{24}$ result is **conditional on Platt–Trudgian** being correct; it is a certified computation, not a hand proof. This is the standard caveat for any result resting on a large verified zero range.
2. Hyperbolicity for *all* $d$ remains equivalent to RH and is of course open. The observation closes only the *reachable* window.
3. The relation $b_m=\int t^{2m}\Phi$ and the normalization of $\gamma(n)$ were checked to 20 digits, not proved here; the conventions in the cited literature differ and must be transported carefully — see `L-16001`(e) for the analogous $\Phi$ vs $\Phi_{\mathrm{cl}}$ trap, which recurs here.
4. The near-degeneracy of the discriminant of $J_{d,n}$ for moderate $n$ was not quantified; anyone building on the pipeline should establish the precision needed before trusting a margin.

## Suggested next attack

Do **not** search for a non-hyperbolic Jensen polynomial. Instead, keep the certificate pipeline and repoint it: the same Hermite/Bézoutian machinery decides real-rootedness for any finite target, and it is precisely what `R-16001`'s census needs at scale.
