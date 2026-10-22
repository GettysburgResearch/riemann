# T-105113 — Shell-average edge frontier

Claim ID: T-105113

Status: **PROPOSED EXACT FINITE SHELL LEDGER; XI SHELL BOUNDS OPEN**

Created: 2026-08-23

Depends on: L-105105; L-105106; L-105113; R-105113

RH status: **unproved**

## Result

The absolute-edge branch has a third exact finite format in addition to the
pointwise margin certificates of L/T-105111 and the phase-sensitive
principal-part route of L/T-105110.

Use

\[
\Omega_{T,\eta}=\{z:|\Re z|<T,\ |\Im z|<\eta\}.
\tag{T-105113.1}
\]

On a regular outer rectangle, authenticate the complete actual manifests of

\[
P=F/F',
\qquad
Q=F^2/(F'F''),
\tag{T-105113.2}
\]

but prescribe selector target jets only at the eligible real events in a
strictly smaller fixed core.  Full zero congruences at every other outer
event make

\[
H_1=W_1P,
\qquad
H_2=W_2Q
\tag{T-105113.3}
\]

holomorphic throughout the buffer.  Every intermediate raw-regular
rectangle therefore carries the same unnormalized charges

\[
\boxed{
q_1:=\oint H_1\,dz=-2\pi iA_0,
\qquad
q_2:=\oint H_2\,dz=2\pi iB_0.
}
\tag{T-105113.4}
\]

Averaging those contours over both side parameters gives an exact signed
two-dimensional shell identity.  For every prescribed pair
\(\lambda_1,\lambda_2\ge0\), Tonelli's theorem selects one raw-regular
intermediate rectangle common to \(H_1,H_2\) such that

\[
\boxed{
\sum_{\nu=1}^2\lambda_\nu
\int_{\partial\Omega_{T,\eta}}|H_\nu|\,|dz|
\le
\sum_{\nu=1}^2\lambda_\nu\mathcal E(H_\nu),
}
\tag{T-105113.5}
\]

where \(\mathcal E\) is the weighted vertical-plus-horizontal shell budget
of L-105113.  The selected rectangle may depend on the prescribed weight
pair; no single rectangle is claimed to work for every pair.  In particular,

\[
\boxed{
2\pi\bigl(\lambda_1|A_0|+\lambda_2B_0\bigr)
\le
\lambda_1\mathcal E(H_1)+\lambda_2\mathcal E(H_2).
}
\tag{T-105113.6}
\]

This avoids a pointwise lower-margin hypothesis only by retaining the full
area cost of the canceled products \(W_1P,W_2Q\).  It does not remove
selector cost.  Degree, coefficient, Pick-norm, and collision growth remain
inside the load-bearing shell budgets.

R-105113 shows that a core-only manifest is insufficient in general: a
selector constructed only for the core can change charge when an uncanceled
\(F''\)-event or \(F'\)-event enters an enlarged contour.  Complete
outer-manifest cancellation is the sufficient mechanism used here to make
the whole buffer holomorphic.  It is not logically necessary merely for
signed charge invariance if a separate residue-neutrality certificate is
available.  Finite existence of a core selector is therefore not, by
itself, a transport theorem.

## Programme split

    BUFFER105113
      One complete outer manifest with a fixed inner target core.
      Closed finitely by L-105113.

    SHELLID105113
      Exact signed two-parameter shell-average identity.
      Closed finitely by L-105113.

    GOODRECT105113
      Simultaneous absolute good-rectangle selection for both carriers.
      Closed finitely by L-105113.

    COREONLY105113
      A core-only selector transports unchanged through a larger buffer.
      Refuted by R-105113.

    XIMANIFEST105113
      Authenticate complete actual Xi manifests on every outer buffer and
      construct the corresponding fixed-core selectors.  Open.

    XISHELL105113
      Bound the fully weighted shell budgets, including inverse buffer
      widths and all selector growth, at the residue-moment scale.  Open.

    XISIGNED105113
      Prove the positive signed first-moment lower bound.  Open.

    XICOFINAL105113
      Combine shell bounds with multiplicity defect, zero-count comparison,
      and strict jet coherence along a cofinal sequence.  Open.

## Boundary

    fixed-core buffered contour charge             PROPOSED EXACT / REVIEW PENDING
    signed shell-average identity                   PROPOSED EXACT / REVIEW PENDING
    simultaneous good-rectangle criterion          PROPOSED EXACT / REVIEW PENDING
    core-only manifest survives enlargement        REFUTED
    finite manifest gives uniform selector cost     REFUTED BY PRIOR FIREWALLS
    Xi complete outer manifests                     OPEN
    Xi weighted shell-area estimates                OPEN
    Xi signed first-moment lower bound               OPEN
    cofinal strict jet coherence                     OPEN
    RCMV104530                                       OPEN
    Riemann Hypothesis                               UNPROVED

The complete outer manifest is a finite conditional input, not a
root-free Xi certificate.  No Xi shell estimate, cofinal passage,
RCMV104530, or RH conclusion follows.
