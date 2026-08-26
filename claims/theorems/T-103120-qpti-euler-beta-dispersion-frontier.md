# T-103120 — QPTI Euler–Beta dispersion frontier

Claim ID: `T-103120`  
Status: **EXACT GLOBAL NORMAL FORM; ONE RH-BEARING SIGNED CORE DISPERSION ESTIMATE OPEN**  
Created: 2026-08-26  
Supersedes no proved claim; sharpens `T-103110`  
Depends on: `L-103120`, `R-103120`, `L-103110--L-103112`, parent `T-102940--T-102990`; corrected PR #730 bounded-current symbol; PR #756 physical-squareclass firewall  
RH status: **unproved**

## 1. Exact QPTI field

For the complete canonical equal-pair harmonic source, define

\[
\mathscr E(s)
=
\sum_{p<q}
\sum_{\substack{c\ {m squarefree}\\(c,pq)=1}}
{\mu(c)\over\binom{\omega(c)+2}{2}}
(pq)^{-s-1/2}c^{-2s-1}.
\tag{T-103120.1}
\]

On every finite horizon this is a finite source polynomial.  In the absolute
half-plane it has the exact Euler–Beta form

\[
\boxed{
\mathscr E(s)
=
\int_0^1(1-\theta)P_\theta(s)
\bigl(A_\theta(s)^2-B_\theta(s)\bigr)d\theta,
}
\tag{T-103120.2}
\]

with the factors defined in `L-103120`.

Let `E_live` denote the same source after only the frozen root, first-chaos,
repeated-label, squared-activity and terminal subtractions.  The direct bounded
current is

\[
\boxed{
\widehat H_{\rm QP}(s)
=
\widehat K_L(s)\mathscr E_{\rm live}(s),
}
\tag{T-103120.3}
\]

where

\[
\widehat K_L(s)
=
{4(s-1)(1-2^{-s})^2(1-\sqrt2\,2^{-s})
 \over s(s-1/2)}.
\tag{T-103120.4}
\]

The quarter-power cutoff no longer appears in (T-103120.3): its exact role was
to prove that the complementary Type-I coordinate equals this field.

## 2. Exact remaining arithmetic theorem

For a squarefree core `c`, let

\[
\mathcal S_c(X)
=
{1\over\binom{\omega(c)+2}{2}}
\sum_{\substack{p<q\\(pq,c)=1}}
{1\over\sqrt{pq}\,c}
K_L\!\left({X\over pqc^2}\right),
\tag{T-103120.5}
\]

with the frozen carrier, phase, marked-prime and closed-ledger projections
understood exactly as in `T-102990`.  Then coefficientwise

\[
\boxed{
H_{\rm QP}(X)
=
\sum_{c\ {m squarefree}}\mu(c)\mathcal S_c(X)
+H_{\rm closed}(X).
}
\tag{T-103120.6}
\]

Define

```text
EBD103120:
  on every dyadic horizon,

    integral_Y^(2Y)
      ( sum_c mu(c) S_c(X) )_-
      dX/X
    = Y^o(1),

  with all frozen source and carrier recombinations performed before the
  negative part.
```

Then

\[
\boxed{
\mathrm{EBD}_{103120}
\Longleftrightarrow
\mathrm{QPTI}_{103112}
\Longleftrightarrow
\mathrm{BCI}_{102990}
\Longleftrightarrow
\mathrm{HMO}_{102940}
\Longrightarrow
\mathrm{RH}.
}
\tag{T-103120.7}
\]

This is an exact change of coordinates, not a new assumption weaker than
QPTI.

## 3. What has now been removed from the problem

The following are no longer candidate gaps:

```text
adaptive-cutoff compatibility;                 exact support identity;
Boolean Vaughan algebra;                       exact;
canonical pair normalization;                  exact Beta Green;
owner/core physical representation;            injective;
shared labels and prime powers;                 frozen closed ledger;
bounded detector multiplier;                   direct exact symbol;
historical common-mother multiplier mismatch;  bypassed by direct K_L;
```

The live problem is one signed recombination of the nonzero owner polynomials
`S_c` across different Möbius core layers.

## 4. Binding exclusions

`R-103120` proves that the Beta coefficient does not cancel a fixed core's
owner mode.  Therefore none of the following proves EBD/QPTI:

```text
uniform fixed-owner Type-I estimates followed by a triangle inequality;
same-occurrence pair multiplicity;
owner-block counting;
a source-blind Gram or modulus square;
a character-family average without principal individualization;
absolute values before the mu(c) recombination.
```

## 5. Two viable closure mechanisms

A direct proof may now target either of two concrete statements.

### Direct signed dispersion

Prove a bilinear estimate in which two different physical owner fibres are
correlated while the `mu(c)` sum is still inside the form.  The modulus must
see the full products `pqc^2`; a bound for owner labels alone is insufficient.

### Connected family individualization

Embed (T-103120.6) into the connected physical-squareclass family of PR #756,
retain the varying-core signs and Wick subtraction, and prove an amplifier or
rigidity theorem whose loss is subpower for the principal zeta member.

Both routes are genuinely arithmetic.  No remaining kernel, cutoff, or owner
normalization can supply the cancellation by itself.

## Exact status

```text
quarter-power support annihilation              PROVED EXACT
fixed-owner Type-I endpoint                     PROVED SUBPOWER
Euler-Beta owner-core transform                 PROVED EXACT
bounded-current Mellin symbol                   PROVED EXACT
fixed live-core owner mode                      NONZERO
cross-core signed dispersion EBD103120          OPEN / RH-BEARING
QPTI103112 / BCI102990                          OPEN / RH-BEARING
Riemann Hypothesis                              UNPROVEN
```
