# T-91302 — The completed Poisson/Fisher tangent has an explicit two-sided Hardy colligation

Claim ID: `T-91302`  
Status: **PROVED EXACT TANGENT COLLIGATION; ZETA-SCREW DEFECT IDENTIFICATION OPEN**  
Created: 2026-08-12  
Depends on: `T-91301`, `L-91306`, `L-91307`, `L-91312`, `L-91313`  
RH status: **unproved**

## 1. Statement

At any safe scale `a>1/2`, the completed boundary phase tangent of Suzuki's
inner family admits an explicit positive-metric conservative realization

\[
 \boxed{
 \mathcal U_a^{\rm tan}:
 \mathcal R_a^{\rm phase}
 \longrightarrow
 \mathcal H_{a,+}^{\rm Hardy}
 \oplus\mathcal H_{a,-}^{\rm Hardy}
 \oplus\mathcal E_a^{\rm phase},
 }
 \tag{T-91302.1}
\]

where:

- the ordinary-prime source-linear component is the positive atomic first
  chaos `beta_a` of `L-91307`;
- its causal Hardy output is the exact tail-Hankel operator
  `H_(beta_a)`;
- reflection supplies the anti-causal output;
- the gamma/pole completion is the skew moving-unitary connection of
  `L-91306`;
- the complete prime-plus-gamma tangent is the score observation of the
  vector-valued Fisher phase symbol of `L-91313`;
- the auxiliary output is the explicit orthogonal score complement.

The construction preserves arbitrary finite carrier, orientation and positive
delay polarizations.

## 2. Conservative identity

Let `mathscr H_a` and `mathscr E_a` be the vector-valued Hardy operators of
`L-91313`, and let `mathcal J_a` be Suzuki's canonical model-space shape. Then

\[
 \boxed{
 2\mathscr H_a^*\mathscr H_a
 =\mathcal J_a^*\mathcal J_a
  +2\mathscr E_a^*\mathscr E_a.
 }
 \tag{T-91302.2}
\]

On the ordinary-prime summand at `a=4`, the source side has the further
explicit Julia decomposition

\[
 \boxed{
 \|g\|^2
 =\|\mathsf H_{\beta_4}g\|^2
 +\|D_0g\|^2+\|D_1g\|^2+\|D_2g\|^2.
 }
 \tag{T-91302.3}
\]

Therefore no unidentified source-linear Poisson output remains.

## 3. Exact source ordering

The realization is assembled in the order

```text
prime-power Poisson score
 -> compensated first chaos
 -> positive tail-Hankel Julia dilation
 -> causal/anti-causal Hardy direct sum
 -> completed gamma/pole covariant connection
 -> score projection plus orthogonal Fisher auxiliary.
```

Higher Poisson chaoses are orthogonal unused environment by `L-91036`; they do
not contribute to an exactly source-linear target.

## 4. What “completion” means here

The requested embedding is now complete at the level at which a linear Hardy
output can exist:

\[
 \boxed{
 \text{prime Poisson-Fock output}
 \hookrightarrow
 \text{completed two-sided Hardy tangent}
 \oplus
 \text{explicit positive auxiliary}.
 }
 \tag{T-91302.4
}

The completion retains:

```text
ordinary-prime first-chaos coefficients;
all carrier cross terms;
both Hardy orientations;
positive delay fibres;
the gamma factor;
the pole factor;
the moving radial connection;
coefficient-one normalization.
```

## 5. The sole remaining RH-bearing equality

The conservative auxiliary produced by the explicit source embedding is

\[
 \boxed{
 \mathcal D_a^{\rm Fisher}
 =2\mathscr E_a^*\mathscr E_a\succeq0.
 }
 \tag{T-91302.5}
\]

CDFHGI requires the transfer defect on the corrected delayed core to be the
zeta screw/Weil kernel

\[
 \mathbb K_a^{\rm del}.
\]

The remaining theorem is therefore not another embedding construction. It is
the source-specific defect identification

\[
 \boxed{
 \mathcal D_a^{\rm Fisher}
 =\mathbb K_a^{\rm del}
 }
 \tag{T-91302.6}
\]

or an exactly equivalent coefficient-one identity in the Suzuki screw
normalization.

If (T-91302.6) holds, the right side is positive, the corrected fixed-scale
criterion gives RH, and the proof closes.  It has not been established.

## 6. Firewall

A generic positive auxiliary cannot be renamed the zeta screw defect.  The
identity must be proved by replaying both sides through the same
Guinand--Weil/Suzuki normalization, including the delayed bridge and opposite
Hardy orientation.

Likewise, the normalized Jordan curvature measure cannot replace the actual
Suzuki score measure; see `R-91301`.

## 7. Exact boundary

```text
prime Poisson source-linear output                     EMBEDDED EXACTLY
ordinary-prime Hardy Julia dilation                    EXACT
completed gamma/pole covariant connection              EXACT
vector Fisher phase Hardy colligation                  EXACT
two orientations and delays                            EXACT
explicit positive auxiliary                            EXACT
auxiliary = zeta screw/Weil defect                     OPEN / RH-EQUIVALENT
Riemann Hypothesis                                     UNPROVED
```
