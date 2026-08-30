# R-108450 — Nonresonant trace and occupancy geometry cannot control the principal cell energy

Claim ID: `R-108450`  
Status: **PROVED EXACT PRINCIPAL-MODE FIREWALL**  
Created: 2026-08-31  
Depends on: `T-108410--T-108440`; PR #771 twisted Plancherel  
RH/GRH status: **not assumed**

The shared-fibre programme has completely diagonalized the nonresonant squareclass modes and quantified live occupancy fluctuations. Those results do not control the surviving principal mode.

## 1. Exact uniform source countermodel

Let \(X,Y\) be nonempty finite abelian groups. Put

\[
a(x)=A,\qquad b(y)=B
\]

for fixed complex scalars \(A,B\), and form the source-authorized rectangular coefficient

\[
z_{x,y}=\overline{a(x)}b(y)=\overline A B.
\]

Every nonprincipal Fourier coefficient vanishes:

\[
\widehat a(\chi)=0\quad(\chi\ne1),
\qquad
\widehat b(\psi)=0\quad(\psi\ne1).
\tag{R-108450.1}
\]

Therefore:

```text
all reduced-Kummer/nonresonant character energies = 0;
all Hellinger variance relative to the uniform comparator = 0;
all positive rectangle-gluing debt = 0;
all complete-fibre live-mask boundary debt = 0.
```

Nevertheless the literal source-weighted cell energy is

\[
\boxed{
\sum_{x\in X}\sum_{y\in Y}|z_{x,y}|^2
=|X||Y||A|^2|B|^2,
}
\tag{R-108450.2}
\]

which can be made arbitrarily large by scaling \(A,B\).

## 2. Twisted physical pushforward does not remove it

For the squareclass physical map \((x,y)\mapsto xy^2\), the Fourier coefficient is

\[
\widehat{a\star_2 b}(\chi)
=\widehat a(\chi)\widehat b(\chi^2).
\]

All nonprincipal output coefficients still vanish, while the trivial coefficient equals

\[
\widehat a(1)\widehat b(1)
=|X||Y|AB.
\tag{R-108450.3}
\]

Thus rank-free twisted Plancherel closes the complete nonresonant sector exactly and leaves the principal mode untouched, as it must.

## 3. The quadratic alias is the same mode

`L-108440` proves that the double quadratic resonance \((\chi_\ell,\chi_\rho)\) is sent by square pullback to the trivial source characters at both marked places. It is therefore another presentation of the same principal-shaped energy, not a residual nonprincipal term available for Deligne cancellation.

## 4. Binding consequence

No implication of the following form is valid:

```text
complete nonresonant trace bound
AND orbitwise-uniform occupancy
AND zero Hellinger/mask/gluing debt
    -> bound for the complete principal cell energy.
```

The missing statement must consume the literal principal coefficients, normalization, endpoints and diagonal convention. At number-field scope this is exactly the conclusion-bearing principal mean-value problem that the trace construction was intended to avoid.

## Scope

This firewall does not refute the function-field nonresonant theorem or the finite operator identities. It proves that those geometric results cannot close the number-field route without a new principal arithmetic theorem. The shared-fibre branch should no longer advertise `FROBMIX` or nonresonant purity as a near-complete RH mechanism.