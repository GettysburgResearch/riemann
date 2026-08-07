# Local-to-Bohr universality addendum

Date: 2026-08-07  
Agent: `gpt56-05-l`  
Status: every new theorem/connection here is `PROPOSED` pending independent review; **RH is not claimed proved or disproved**

## 1. Why this addendum exists

The preceding frozen route report was written while several global branches were still advancing. Two important developments arrived immediately afterward:

1. PR #158 independently repaired its own proposed Selberg–Mourre completion, added the same exact Mellin gauge as `L-15443`, and refuted the universal block-normalized inverse it had previously hoped to use.
2. PR #226 identified an exact positive Bohr/Jordan factorization for the analytic summatory-totient packet and reduced RH to one critical local second moment.

Together with `L-15444/L-15445`, these developments reveal a stronger repository-wide conclusion: the newest global routes have independently reached the **same local-to-Bohr metric obstruction**.

## 2. Updated heads read

The relevant heads at the time of this addendum were:

```text
PR #158  668f10a87eb8b8d0521edf8b5156334e287747f0
PR #165  advanced during this addendum; final head reported in the PR comment
PR #216  b76eef1b769584aa9d66d082bfc6634126f986a2
PR #217  61c6f1129eb2848ce30750ec51c257945a7351c7
PR #218  aa82813aaebf998dce23fd7b0d7e9d2e5cce4bfe
PR #219  6fbd5ea4c27c180f162e7827fd830b801ac751ff
PR #222  bd2a1ce27dea41d32f53688609385cbd38c1559a
PR #224  ca40331114e74b57c1a805a0f1b1b008e70c7404
PR #226  53f2cba370fa518d5d12488b5b9948c1826bba88
```

These are mutable draft heads. Every classification below is attached only to the displayed snapshot.

## 3. The Selberg route has self-corrected to the exact hinge

PR #158 now records:

```text
exact front half:
    scale-subtracted Selberg equation,
    dilation commutator,
    second-order elimination,
    complete Lambda_2 support,
    Mellin gauge;

refuted shortcut:
    universal block-normalized polynomial SM(J) inverse;

remaining theorem:
    localized source-specific Selberg–Poincare / physical metric control.
```

This agrees exactly with `L-15443/L-15444`.

For

\[
m(z)=(1+z)\zeta(1+z),
\]

one has

\[
\mathcal M\mathcal L\mathcal M^{-1}
=-m^{-1}\partial_zm.
\]

The global coefficient/gauge form diagonalizes and has only a finite first-annulus negative ledger. What fails is a universal conversion from this Bohr/gauge energy to the local identity-orbit energy. PR #158's new refutation is therefore not a collapse of the route; it identifies the same missing metric theorem independently.

## 4. The totient route is the inverse-zeta coordinate of the prime route

PR #226 writes the analytic totient error transform as

\[
\mathcal T(s)
=-{\zeta(s-1)\over s(s-1)\zeta(s)}
+{3/\pi^2\over s-2}.
\]

`L-15445` proves that the raw dyadic Chebyshev transform satisfies

\[
\boxed{
\mathcal Q(s)
=(1-4^{1-s})(s-1){\zeta'(s)\over\zeta(s-1)}
\left[
 \mathcal T(s)-{3/\pi^2\over s-2}
\right].}
\]

The multiplier is regular at the zeta pole and has no zero or pole that can hide an off-line zeta zero in

\[
1/2<\Re s<1.
\]

Thus the analytic totient error is exactly an inverse-zeta metric carrier for the same dyadic prime ray. The two second-moment criteria are not merely analogous:

```text
prime coordinate:
    local norm after multiplying the inverse-zeta packet by a safe prime numerator;

totient coordinate:
    local norm of the inverse-zeta packet itself.
```

## 5. Both global Bohr forms are already positive

### Prime/Selberg gauge

`L-15444` gives

\[
\mathfrak Q_{a,\sigma}^{\rm Bohr}
=\sum_{n\ge2}
\log n(\log n-\log a)
|b_a(n)|^2n^{1-2\sigma}.
\]

The entire negative part is finite; at scale four it comes only from `n=2,3`.

### Möbius/Farey packet

PR #226 gives

\[
\begin{aligned}
\mathcal B_D={}&{1\over12}\sum_{q\le D}J_2(q)
\left(\sum_{q\mid d\le D}{\mu(d)\over d}\right)^2\\
&+{1\over180}\sum_{q\le D}J_4(q)
\left(\sum_{q\mid d\le D}{\mu(d)\over d^2}\right)^2
\ll D.
\end{aligned}
\]

Both full-period/coefficient energies have the conjectured critical scale unconditionally. Neither controls the required physical interval because near-resonant logarithmic/Farey frequencies remain coherent there.

## 6. Exact common obstruction

The repository's newest full routes now share the diagram

```text
exact global coefficient factorization
        |
        |  OPEN: ray-specific local-to-Bohr transference
        v
critical physical interval / vertical-line energy
        |
        v
rightmost-zero exponent and RH.
```

The same open arrow appears as:

- PR #158: localized source-specific Selberg–Poincare estimate;
- PRs #216/#222: signed balanced semiprime common-cell dispersion;
- PR #224: restricted critical prime-ray `H1`/Carleson estimate;
- PR #226: Möbius-weighted near-resonant Farey local-to-Bohr estimate;
- `L-15443/L-15444`: gauge-to-physical metric conversion;
- `L-15445`: critical local multiplier estimate between the totient and prime coordinates.

The universal version of this arrow is false. Every viable proof must use the exact arithmetic ray.

## 7. What may have crossed already

The following pieces appear to have crossed from speculative structure to exact theorem-quality algebra, although they remain formally `PROPOSED` until independent review:

1. the Selberg–Volterra Mellin gauge;
2. the complete coefficient support and finite-boundary Bohr diagonalization;
3. the analytic-totient/parabolic-Riesz identity;
4. the full-period Möbius/Jordan square factorization;
5. the safe transform bridge between the totient and dyadic-prime signals;
6. the rightmost-zero exponent transfers, subject to their Hardy/Mellin audits.

No inspected route has crossed the local-to-Bohr arrow. Therefore no inspected route has yet proved RH.

## 8. Best combined finish-line attack

The most promising synthesis is not to prove a universal embedding. It is to exploit the special arithmetic relation in `L-15445` and prove a **joint two-coordinate local inequality**.

A proof-facing target is:

\[
\boxed{
\begin{aligned}
&\int_{X}^{2X}|E^{\rm AN}(t)|^2dt\\
&\qquad+\int_X^{2X}
\left|{\psi(t)\over t}-{\psi(t/4)\over t/4}\right|^2dt
\ \le\ X^{2+o(1)}
+\mathcal R_X,
\end{aligned}}
\]

where `R_X` is expressed as the same signed near-resonant semiprime/Farey block in two dual bases. The goal is to make the problematic off-diagonal term cancel or become a positive square **between the two coordinates**, rather than bound it separately in either one.

The raw materials are now present:

1. exact prime common-cell cubic kernels on PR #222;
2. exact product-scale `H1` semiprime convolution on PR #224;
3. exact Möbius/Farey covariance and Jordan squares on PR #226;
4. exact multiplier relation `L-15445`;
5. exact safe boundary factors and finite first-annulus ledger `L-15444`.

This coupled-square construction is a genuinely new connection. It may still fail, but it attacks the actual RH-strength metric conversion rather than another equivalent endpoint.

## 9. Status boundary

```text
All requested artifacts on GitHub:          yes
Exact global coefficient factorizations:    substantial and convergent
Universal local-to-Bohr embedding:          refuted
Ray-specific local-to-Bohr theorem:         open
Inspected proposal already proving RH:      none
Riemann Hypothesis:                         not proved or disproved
```

The correct final step is now sharply identified: construct the joint prime/Möbius local square, or prove the equivalent restricted signed semiprime/Farey Carleson estimate.