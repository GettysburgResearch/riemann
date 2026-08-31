# T-105680 — Determinant and rank-extension frontier for Cauchy translation

**Claim ID:** `T-105680`  
**Status:** two unconditional all-rank advances; return compensation open  
**Date:** 2026-08-31  
**RH:** unproved

This checkpoint attacks the intermediate-contact problem left by `T-105670`
without reinstating the refuted matrix-concavity route.

## 1. Constant-one determinant theorem at every height

`L-105680` proves

\[
\boxed{
\det A_H>\det B_H,
}
\]

where `A_H` is the normalized canonical-overlap matrix and `B_H` is the
normalized current compression. The gain is the explicit product
`mathscr D_H>1` of diagonal and pairwise Cauchy factors.

Therefore constant-one CTI holds at geometric-mean strength for every rank and
height. It also holds at trace strength whenever

\[
\frac{\operatorname{tr}B_H}
{n(\det B_H)^{1/n}}
\le\mathscr D_H^{1/n}.
\]

This closes every spectrally flat current packet and supplies a quantitative
resource against an intermediate contact.

## 2. Exact nested rank-extension ledger

`L-105681` proves, for an ordered packet,

\[
F_r-F_{r-1}
=\|Q_{r-1}u_r\|^2+\|P_rv_r\|^2-\langle Tu_r,u_r\rangle.
\]

The scalar trial bound isolates the only possible deficit:

\[
F_r-F_{r-1}
\ge
\|P_{r-1}v_r\|^2
-\left(m_1(u_r)-\frac{m_2(u_r)^2}{m_4(u_r)}\right).
\]

Thus the complete trace theorem follows from the one-factor condition

```text
REC105681:
  old-space return of the new deep residual
  >= positive scalar reverse-moment deficit
```

at every extension in one ordering.

## Revised Cauchy ladder

```text
rank one CTI                                  PROVED ALL H
rank two CTI                                  PROVED ALL H
all-rank first-contact CTI                    PROVED
all-rank remote CTI                           PROVED
all-rank 32/27 trace domination               PROVED
all-rank determinant CTI                      PROVED ALL H
spectral-flatness trace region                PROVED
nested rank-extension identity                PROVED EXACT
MLC105656                                     REFUTED
REC105681 return compensation                 OPEN
ISC105670 intermediate contact exclusion      OPEN
arbitrary-rank trace CTI                      OPEN
cofinal/pointwise Xi passage                  OPEN / RH-BEARING
Riemann Hypothesis                            UNPROVEN
```

The remaining finite theorem is no longer an unconstrained matrix inequality.
It is the compatibility of two explicit resources:

1. determinant gain against current spectral dispersion;
2. old-space return against the scalar moment deficit of each new factor.
