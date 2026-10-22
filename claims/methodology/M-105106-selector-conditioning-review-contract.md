# M-105106 — Review contract for selector conditioning

Claim ID: M-105106

Status: **HOSTILE REVIEW CONTRACT**

Created: 2026-08-23

Depends on: L-105103; L-105105; L-105106

RH status: **unproved**

## Manifest and cardinal formula

- The manifest contains distinct actual pole nodes with their full
  post-cancellation orders from L-105103.
- Raw zeros of \(F'F''\) may not replace actual pole orders.
- Every target belongs to the complete manifest.
- The selected datum is the top local primary jet \(d_c-1\).
- Every summand contains \(M_c/M_c(c)\); omitting the normalization must fail.
- Replacing \(d_c-1\) by \(d_c\), or radicalizing a repeated nontarget, must
  fail its local congruence.
- The reduced representative has degree less than \(D\), and its leading
  coefficient agrees with the signed barycentric formula.

## Conditioning bounds

- Exact products \(|M_c(c)|^{-1}\) are recorded before any minimum-separation
  relaxation.
- Coefficient bounds use an explicitly centred weighted \(\ell^1\) norm.
- Boundary radius, node radius, node separation, and multiplicity exponents
  remain distinct quantities.
- Sign or conjugation symmetry may force coefficient cancellation but may not
  be used to discard absolute conditioning products.
- The clustered real-even fixture must attain degree \(D-1\) and the
  \(\delta^{-(D-1)}\) scale.
- The Blaschke lower bound must rule out escape by a higher-degree holomorphic
  selector.

## Weighted edges

- The edge bound is derived from \(W/M\), not by silently treating \(h\) as
  pole-free.
- \(G=Mh\) is a separate holomorphic factor and must remain visible.
- Target-to-edge distance appears with exponent one after pole cancellation.
- Bounds for individual edges are not inferred from the closed-contour
  residue identity.
- Adding a holomorphic remainder preserves pole/principal-part data and can
  enlarge individual edge norms arbitrarily; event data alone do not bound
  \(G\).
- Draft PR #720 L-104519 is unweighted and fixed-ladder.  It is not a theorem
  about \(W_1F/F'\) or \(W_2F^2/(F'F'')\).

## Prior-art firewall

- Earlier branch checkpoints L-105101--L-105105 may be used within their
  stated proposed scopes.
- Draft PR #720 at `10bba584c01277e880aaa21e1fea09f396ca7246` is
  post-freeze, unmerged context.
- Integrated registry row 71 marks L-92302 `GAP_BLOCKED` / `QUARANTINE`; no
  moving-order Vandermonde estimate is imported from it.
- Historical finite cardinal and Hermite identities are reconnaissance only,
  not load-bearing dependencies.

## Scope firewall

- A computable fixed-window envelope is not a cofinal Xi estimate.
- No Xi event census, separation law, barycentric-product bound,
  pole-cancelled holomorphic-factor estimate, or weighted edge asymptotic is
  inferred.
- No multiplicity-defect estimate, strict coherence margin, RCMV104530, or RH
  conclusion follows formally.
