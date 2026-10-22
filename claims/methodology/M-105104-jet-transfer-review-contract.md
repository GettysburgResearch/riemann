# M-105104 — Hostile review contract for jet transfer

Claim ID: M-105104

Status: **REVIEW METHODOLOGY**

Created: 2026-08-23

RH status: **unproved**

Reject T-105104 if any item below fails.

## Primitive interval identity

- Distinct critical nodes include every real zero of \(f'\) in the open
  interval, at any finite order.
- The supplied critical manifest is authenticated against a separately frozen
  expected manifest; missing, duplicate, and extraneous nodes must fail closed.
- Parent zeros at common nodes are counted once in the distinct identity and
  with order \(r+1\) in the multiplicity identity.
- Strict sign-change edges never count a cell incident to a zero-valued
  critical node.
- Endpoint parent values are nonzero.

## Eligible jet dictionary

- Only noncommon odd-order critical events are turns.
- The carrier is
  \(\rho_c^{\mathrm{jet}}=r!f(c)/f^{(r+1)}(c)\).
- Negative carrier means good turn; positive means wrong turn.
- The \(P\)-leading power is \(-r\).
- The \(Q\)-leading power is \(-(2r-1)\), with coefficient
  \((\rho_c^{\mathrm{jet}})^2/r\).
- For \(r>1\), neither leading coefficient is called an ordinary residue.
- Even-order noncommon events enter \(\Delta_{\mathrm{mult}}\), not the
  turning count.

## Component and multiplicity accounting

- Splitting occurs only at real common critical points.
- The active-component count \(q\) is not replaced by one globally.
- Common parent multiplicity is
  \(\mathfrak m_{\mathrm{com}}+\#\mathcal C_{\mathrm{com}}\).
- The exact derivative split is

      N_mult(f') = m_com + R_jet + Delta_mult.

- The detailed and coarse signs are

      N_mult(f) >= m_com + #C_com + 2 G_jet - R_jet - q
      N_mult(f) >= m_com + 2 G_jet - R_jet - 1.

- Cauchy is applied to the jet carriers, not to merged ordinary residues.
- The simple noncommon case recovers draft L-104522.4 exactly.

## Mutation firewalls

- The bounded nonadjacent-wrong-turn enumeration has a sharp row.
- On \([-1,1]\), \(x^6\pm1/64\) have equal zero ordinary residue charges
  but zero counts zero and two; their jet carriers are \(\pm1/384\).
- \(x^4\) is counted with parent multiplicity four; a distinct-only mutation
  must fail.
- For \(x^4-2x^2\) on \([-5/4,5/4]\), the common zero splits the two good
  turns into \(q=2\) active components. Mutating \(q\) to one gives the
  false lower bound three while the exact multiplicity count is two.
- The fixture with derivative \((x^2-1/4)^2\) has only even-order stationary
  events and no parent zero on \((-1,1)\). Treating them as good turns must
  fail.
- Normal and optimized Python must return the same artifact.

## Scientific boundary

- The theorem is analytic, not an arbitrary \(C^2\) statement.
- Ordinary boundary residue charges do not reconstruct high-pole jet moments.
- An Xi proportion corollary retains the effective-turning proportion,
  common mass, multiplicity defect, total-count ratio, and strict margin as
  separate premises.
- No Xi jet estimate, RCMV104530, or RH conclusion follows formally.
