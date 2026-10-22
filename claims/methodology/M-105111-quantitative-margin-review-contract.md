# M-105111 — Review contract for quantitative edge margins

Claim ID: M-105111

Status: **HOSTILE REVIEW CONTRACT**

Created: 2026-08-23

Depends on: L-105109; L-105110; L-105111; R-105111

RH status: **unproved**

## Anchored log-drop ledger

- Parametrize the compact arc and include the anchor in the maximization, so
  \(D_G\ge0\).
- Use the signed subarc integral from the anchor to each point.  Reversing a
  subarc changes the integration limits automatically.
- The exact quantity is the downward variation of \(\log|G|\), not an upper
  bound for \(|G'/G|\).
- The total real logarithmic-modulus variation is a sufficient relaxation.
  The full complex log-variation is valid but generally weaker.
- Authenticate nonvanishing before using \(G'/G\).

## Denominator identities

- Use \(L=F'/F\), \(A=F''/F\), and \(B=F'''/F\).
- Check
  \(L'=A-L^2\) and
  \((LA)'=A^2+LB-2L^2A\).
- The product log density is
  \(A/L+B/A-2L\), not the first density and not a bound for \(L\) alone.
- Exact weighted-sup equalities require the L-105107
  constant-boundary-modulus optimum.  For an arbitrary weight, use its edge
  norm and retain only an inequality.

## Disk-cover contract

- Every closed disk must lie inside the holomorphy domain of \(G\).
- The disks must cover the complete edge, including endpoints.
- Center lower bounds and derivative upper bounds must be independently
  certified.
- Every slack \(\mu_j=a_j-r_jM_j\) must be strictly positive.
- A positive slack proves local nonvanishing; no prior zero-free assumption
  for \(G\) is needed on that disk.
- For \(LA\), use the product derivative identity.  A first-denominator
  certificate cannot be silently reused.

## Exact-fixture checks

- For \(F_0=e^{z-z^2/8}\), use \(u=1-z/4\).
- Verify exact margins \(3/4\) and \(15/64\), and exact drop ratios
  \(4/3\) and \(16/5\).
- Verify both radius-\(1/4\) disks and the four center/derivative fractions
  before accepting the product slacks.
- The first sharp family fixes the anchor while its variation grows.
- The product firewall keeps \(m_1\) positive while \(m_{12}\) collapses.

## Stable-manifest firewall

- In the \(Q_S\) family, the complete **first** manifest is globally
  \(\{0\}\), the target residue is one, and the first selector is one.
- The finite \(G_1,G_{12}\) anchor values are fixed, but the values between
  anchors collapse.
- Do not use an edge through zero; the exact fixture uses \([1/2,1]\).
- Do not claim a stable second-derivative manifest.
- The family refutes anchor-only reasoning, not the log-drop or disk-cover
  theorems.  The first log-drop grows.  For the product, either \(A_C\)
  acquires an edge zero, or its log-drop grows on any zero-free parameter
  range; the disk derivative/slack debt remains valid in both cases.

## Scope firewall

- No Xi anchor, disk, variation, third-normalized-derivative, disk-count, or
  slack estimate is supplied.
- No Green--Gram absorption, pole-subtracted remainder, corner control,
  cofinal passage, strict coherence, RCMV104530, or RH conclusion follows.
