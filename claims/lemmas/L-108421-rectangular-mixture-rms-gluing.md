# L-108421 — Positive rectangular source pieces glue with an RMS Hellinger cost

Claim ID: `L-108421`  
Status: **PROVED EXACT POSITIVE-MEASURE GLUING THEOREM**  
Created: 2026-08-31  
Depends on: `L-108400`, `L-108412`, `L-108420`  
RH/GRH status: **not assumed**

Let a grouped live shared-conductor fibre be decomposed into finitely many
source-authorized positive rectangular pieces indexed by `a`. For each piece,
let

\[
\mu_a
\]

be its literal physical occupancy and let

\[
\bar\mu_a
\]

be the corresponding orbitwise Frobenius-symmetric comparator. Assume the two
measures have the same mass

\[
N_a>0.
\]

Put

\[
\mu=\sum_a\mu_a,
\qquad
\bar\mu=\sum_a\bar\mu_a,
\qquad
N=\sum_aN_a,
\qquad
w_a={N_a\over N}.
\tag{L-108421.1}
\]

For the one-sided multiplicity distributions of rectangle `a`, define the
normalized character energies

\[
\mathcal V_{L,a}
={1\over L_a^2}
\sum_{\chi\ne1}|\widehat l_a(\chi)|^2,
\qquad
\mathcal V_{R,a}
={1\over R_a^2}
\sum_{\psi\ne1}|\widehat r_a(\psi)|^2.
\tag{L-108421.2}
\]

## 1. Exact positive gluing

By `L-108412`,

\[
{H^2(\mu_a,\bar\mu_a)\over N_a}
\le
\mathcal V_{L,a}+\mathcal V_{R,a}.
\tag{L-108421.3}
\]

The positive-mixture theorem `L-108420` therefore gives

\[
\boxed{
{H^2(\mu,\bar\mu)\over N}
\le
\sum_aw_a
\left(
\mathcal V_{L,a}+\mathcal V_{R,a}
\right).
}
\tag{L-108421.4}
\]

Applying the positive-trace stability theorem `L-108400`,

\[
\boxed{
\left|
\operatorname{tr}Q(\mu)_+
-
\operatorname{tr}Q(\bar\mu)_+
\right|
\le
2N
\sqrt{
\sum_aw_a
(\mathcal V_{L,a}+\mathcal V_{R,a})
}.
}
\tag{L-108421.5}
\]

This is an RMS gluing law. It is never worse than paying the pieces
separately:

\[
2N\sqrt{\sum_aw_a\eta_a}
\le
2\sum_aN_a\sqrt{\eta_a}
\]

is generally false in that direction; rather Cauchy gives

\[
\sum_aw_a\sqrt{\eta_a}
\le
\sqrt{\sum_aw_a\eta_a},
\]

so the globally mixed bound in (L-108421.5) is the natural single-quotient
payment, while piecewise trace comparison can be sharper when the quotient
itself splits. The theorem records the exact safe global payment and makes no
unsupported direct-sum claim.

## 2. Physical pushforward may be postponed

If the rectangles are first compared in the owner/cofactor source space and
then sent through the physical residue or squareclass map `pi`,
`L-108420.3` gives

\[
H^2\left(
\pi_*\sum_a\mu_a,
\pi_*\sum_a\bar\mu_a
\right)
\le
\sum_aH^2(\mu_a,\bar\mu_a).
\tag{L-108421.6}
\]

Thus collision of different rectangles after physical pushforward creates no
additional positive Hellinger debt.

## 3. Exact scope of `RECTGLUE107300`

Equations (L-108421.4)--(L-108421.6) close the abstract rectangle-gluing
problem for:

```text
nonnegative grouped occupancies;
positive parts of the shared-fibre Wick quotient;
orbitwise Frobenius comparators;
deterministic physical pushforward.
```

They do **not** close gluing for the signed principal-minus-Kummer current.
That current must first undergo its exact source-authorized signed
recombination. `R-108420` records this boundary.

## Scope

The theorem removes rectangle overlap and physical collision as separate
positive-trace obstructions. It does not prove the one-sided character-energy
bound, the live-mask estimate, or the quadratic/principal binding.
