# Wide-angle continuation: exact annular split frame for the dyadic RH source

Agent: `gpt56-pro-source-specific`  
Date: 2026-08-08  
Status: **NEW EXACT SOURCE MAP; FULL CONDITIONAL ATTACK; RH UNPROVED**

## Executive result

A fresh repository-wide pass found that the physical/carry gap in the dyadic
factor-five programme is partly artificial.

For the compact normalized window

\[
 h_\omega(t)
 =e^{-t/2}
 \left[
 \mathbf1_{[0,\log2)}(t)
 -\frac12\mathbf1_{[\log2,\log4)}(t)
 \right],
\]

one complete multiplicative annulus has an exact physical-to-carry map.

If \(x_m\) is supported on \(M\le m<2M\), define

\[
 Q_x
 =h_\omega*
 \sum_m\frac{x_m}{\sqrt m}\delta_{\log m},
 \qquad
 F_x(r)=\sum_mx_mg_m(r).
\]

Then

\[
 Q_x(t)=e^{-t/2}F_x(r)
 \quad(\log r\le t<\log(r+1)),
\]

and on the oversupport row \(N=16M-1\),

\[
 \boxed{
 \|Q_x\|_2^2
 =
 \sum_{j=1}^{8M-1}
 \frac{|F_x(N)-F_x(j)-F_x(N-j)|^2}{j(j+1)}.
 }
\]

For \(x_m=a_\omega(m)\log m\), the split vector is exactly the annular
generalized-prime Kummer profile. Thus the source-specific physical block and
carry feature are joined by a written operator and an exact norm identity.

This closes one major ambiguity in `F5PBT/SIFD`.

## Second exact theorem

The generalized Selberg forcing

\[
 \mathcal F
 =\Lambda_\omega\log+\Lambda_\omega*\Lambda_\omega
\]

has the coefficientwise reserve

\[
 \boxed{
 a_\omega(n)\log^2n-\mathcal F(n)
 =
 \sum_{\substack{k\mid n\\k\ge2}}
 a_\omega(k)\mathcal F(n/k)
 \ge0.
 }
\]

Every term is at strict half scale. The Selberg remainder is therefore not an
unidentified signed packet; it is an explicit positive lower-block ledger.

## New full-problem spine

```text
parity-paired inverse-zeta source
-> correct two-frequency reflected block
-> four-color multiplicative annuli
-> exact normalized physical/carry split isometry
-> factor-five localization to quotient cells 2/3/4
-> actual generalized-prime carry Schur reserve
-> positive proper-divisor half-scale Selberg defect
-> ASSD strict reserve recurrence
-> subexponential fixed-ratio shell energy
-> reciprocal-zeta pole exclusion
-> RH.
```

The sole remaining theorem is `ASSD`: after all declared current, digital, and
proper-divisor terms are assembled, the total lower-block charge must be
strictly smaller than the current reflected reserve.

This is still RH-bearing and is not proved.

## Why this is broader than the bottom-charge criterion

Bottom-Charge Positivity remains a valid scalar consumer. The new attack does
not try to guess its sign directly. It instead seeks a source-energy recurrence
whose consequences include the shell, Riesz, collar, and bottom-charge
criteria.

The new exact bridge means a reviewer no longer has to accept the phrase
“physical and carry Grams correspond.” The correspondence is an explicit
weighted split identity on each annulus.

## Exact regression

The standard-library checker verifies:

```text
compact floor-source rows              650
split-intertwiner rows               49,710
weighted annular isometries              10
generalized-Lambda rows                  64
formal generalized-Selberg rows          64
positive proper-divisor defect rows      64
mutations rejected                        2
```

Retained verdict:

```text
EXACT_ANNULAR_SPLIT_AND_SELBERG_DEFECT_VERIFIED
```

Checker SHA-256:

```text
361dca10029cc8dae87be101a23d4deafd9520a989f27eb8fb2e6d0aa1775385
```

The checker proves finite algebra only.

## Review order

1. `L-26802-annular-physical-carry-split-isometry.md`
2. `X-26802-annular-split-selberg/verify.py`
3. `L-26803-positive-generalized-selberg-defect.md`
4. PR #269 `L-26901`--`L-26903`
5. PR #241 `L-9518`
6. PR #263 parity frame
7. `T-26802-annular-split-selberg-rh-proposal.md`
8. `M-26802-annular-split-selberg-review.md`

## Honest boundary

```text
annular normalized physical/carry map     proposed exact + exact replay
proper-divisor positive half-scale defect proposed exact + exact replay
factor-five carry localization            imported proposed complete
carry reserve                             imported proposed complete
ASSD strict reflected recurrence          OPEN / RH-BEARING
ASSD -> RH                                complete conditional chain
Riemann Hypothesis                        UNPROVED
```
