# T-105107 — Boundary-optimal jet-observable frontier

Claim ID: T-105107

Status: **PROPOSED EXACT FIXED-WINDOW OPTIMUM; COFINAL CONTROL OPEN**

Created: 2026-08-23

Depends on: L-105105; L-105106; L-105107; R-105107

RH status: **unproved**

## Result

Exact pole annihilation no longer requires accepting the boundary norm of the
reduced polynomial selector.  Factoring the zeros forced by the complete
actual-pole manifest gives

\[
W=I_0H,
\qquad
H(c)=\gamma_c/\beta_c.
\tag{T-105107.1}
\]

The exact minimum selector norm \(\tau\) is characterized by

\[
\boxed{
\left[
\frac{\tau^2-y_j\overline y_k}
{1-c_j\overline c_k}
\right]\succeq0
}
\tag{T-105107.2}
\]

at the first singular positive-semidefinite threshold.  The extremal selector
has constant boundary modulus \(\tau\), degree at most \(D-1\) in disk
coordinates, and preserves the L-105105 moment identities.

For a rectifiable simply connected Jordan window, conformal transport gives
the same theorem in \(A(\Omega)\).  On every edge,

\[
\left|\frac1{2\pi i}\int_EW_*h\right|
\le
\frac{\operatorname{len}(E)}{2\pi}\tau\|h\|_E.
\tag{T-105107.3}
\]

The theorem is boundary-optimal for the selector alone.  It neither estimates
\(\tau\) on changing Xi windows nor controls the quotient \(h\).

## Programme split

    FINPICK105107
      Forced-inner reduction and exact finite Pick optimum.
      Closed algebraically by L-105107.

    RECTA105107
      Disk-algebra transport, symmetry, and rectifiable-Jordan residue
      bridge.  Closed at the stated regularity by L-105107.

    XIPICKNORM105107
      Authenticate the Xi manifest and bound the changing conformal radii,
      pseudohyperbolic products, and full Pick eigenvalue.  Open.

    XIQUOTEDGE105107
      Estimate the unweighted boundary quotients F/F' and
      F^2/(F'F'') strongly enough after multiplication by tau(T).  Open.

    XICOFINAL105107
      Control exterior poles or recompute selectors, pass through the
      changing rectangles, and retain a strict jet-coherence margin.  Open.

## Boundary

    forced-inner top-jet reduction                 PROPOSED EXACT / REVIEW PENDING
    finite Pick optimal selector norm              PROPOSED EXACT / REVIEW PENDING
    constant-modulus extremal and degree bound      PROPOSED EXACT / REVIEW PENDING
    rectifiable-Jordan residue transport            PROPOSED EXACT / REVIEW PENDING
    reduced polynomial always boundary-optimal      REFUTED
    diagonal target bounds replace full Pick PSD    REFUTED
    Xi event and conformal manifest                 OPEN
    cofinal Xi Pick-norm estimate                   OPEN
    Xi quotient edge estimates                     OPEN
    cofinal strict jet coherence                    OPEN
    RCMV104530                                      OPEN
    Riemann Hypothesis                              UNPROVED

Accepted low-order actual-Xi Pick matrices are a different kernel and are not
used.  No RCMV104530 or RH conclusion follows.
