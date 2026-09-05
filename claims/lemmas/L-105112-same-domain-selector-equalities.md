# L-105112 — Same-domain selector equalities

Claim ID: L-105112

Status: **PROPOSED EXACT REPAIR / ERRATUM**

Created: 2026-08-23

Depends on: L-105107; L-105109; L-105111

RH status: **unproved**

## 1. Repair notice

The literal constant-modulus wording in the frozen T-105109 packet is
overbroad or ambiguous unless its phrase “every boundary arc” is read as
“every boundary arc of the exact domain used to construct the selector.”
In particular, the issue occurs in L-105109.5 and is repeated or summarized
in the frozen L/T/M/metadata/report/PR-body documents:

- `claims/lemmas/L-105109-log-derivative-edge-margins.md`;
- `claims/theorems/T-105109-quotient-edge-frontier.md`;
- `claims/methodology/M-105109-quotient-edge-review-contract.md`;
- `PACKET_METADATA_105109.json`;
- `reports/codex/2026-08-23-log-derivative-edge-obstruction.md`;
- `PR_BODY_105109_ADDENDUM.md`.

This checkpoint does not silently modify those frozen artifacts or their
historic proof-object digest.  It records the intended same-domain reading
and replaces the broad literal formula prospectively.  No retrospective
verification of T-105109 is claimed.

## 2. Exact same-domain theorem

Let \(\Omega\) be the exact bounded simply connected Jordan selector domain
used to construct an L-105107 optimal selector \(W_*\).  Thus

\[
W_*\in A(\Omega)
=\operatorname{Hol}(\Omega)\cap C(\overline\Omega),
\qquad
\|W_*\|_{\overline\Omega}=\tau,
\qquad
|W_*|=\tau\quad\hbox{on }\partial\Omega.
\tag{L-105112.1}
\]

Let \(E\subset\partial\Omega\) be a compact rectifiable arc.  Suppose \(F\)
is holomorphic in a neighborhood of \(E\) and \(F,F',F''\) are nonzero on
\(E\).  Write

\[
L=\frac{F'}F,
\qquad
A=\frac{F''}F,
\qquad
m_1(E)=\inf_E|L|,
\qquad
m_{12}(E)=\inf_E|LA|.
\tag{L-105112.2}
\]

For the first and second optimal selectors constructed on this same
\(\Omega\), with boundary norms \(\tau_1,\tau_2\), respectively,

\[
\boxed{
\left\|W_{1,*}\frac F{F'}\right\|_E
=\frac{\tau_1}{m_1(E)},
\qquad
\left\|W_{2,*}\frac{F^2}{F'F''}\right\|_E
=\frac{\tau_2}{m_{12}(E)}.
}
\tag{L-105112.3}
\]

Indeed, \(|W_{j,*}|=\tau_j\) pointwise on this \(E\), and compactness plus
nonvanishing makes each positive infimum a minimum.  Therefore

\[
\sup_E\frac{|W_{1,*}|}{|L|}
=\tau_1\sup_E\frac1{|L|}
=\frac{\tau_1}{m_1(E)},
\tag{L-105112.4}
\]

with the identical argument for \(LA\).  The domain identity in the first
sentence is load bearing: L-105107 proves constant modulus on
\(\partial\Omega\), not on the boundary of every other region and not on
arbitrary interior arcs.

## 3. The general edge statement

Let \(E\) instead be any compact set on which a weight \(W\) and the relevant
quotient are continuous and the denominator does not vanish.  The exact
pointwise formula gives only

\[
\boxed{
\left\|W\frac F{F'}\right\|_E
\le \frac{\|W\|_E}{m_1(E)},
\qquad
\left\|W\frac{F^2}{F'F''}\right\|_E
\le \frac{\|W\|_E}{m_{12}(E)}.
}
\tag{L-105112.5}
\]

The product bound can be strict because the maximum of \(|W|\) need not
occur where the denominator modulus is smallest.  It can also be attained
without \(|W|\) being the global constant \(\tau\).

If \(W=W_*\in A(\Omega)\) and \(E\subset\overline\Omega\), the maximum
modulus principle and boundary continuity give \(\|W_*\|_E\le\tau\).
Consequently

\[
\boxed{
\left\|W_{1,*}\frac F{F'}\right\|_E
\le \frac{\tau_1}{m_1(E)},
\qquad
\left\|W_{2,*}\frac{F^2}{F'F''}\right\|_E
\le \frac{\tau_2}{m_{12}(E)}.
}
\tag{L-105112.6}
\]

For \(E\not\subset\overline\Omega\), membership in \(A(\Omega)\) does not
even define \(W_*\) on \(E\); an independently authenticated continuation
and its actual edge norm would be required.

## 4. Exact counterexample to the broad literal reading

Take

\[
\Omega=\mathbb D,
\qquad
F(z)=\exp(z^4/4),
\qquad
L(z)=\frac{F'}F=z^3.
\tag{L-105112.7}
\]

The first quotient is \(F/F'=z^{-3}\).  Its complete manifest in
\(\mathbb D\) is the single order-three target at zero with leading
coefficient one.  Every admissible first selector has the form
\(z^2H(z)\), \(H(0)=1\).  Hence the exact optimum is

\[
W_*(z)=z^2,
\qquad
\tau=1,
\qquad
|W_*|=1\quad\hbox{on }\partial\mathbb D.
\tag{L-105112.8}
\]

For \(0<r\le1\), let

\[
E_r=\{re^{it}:0\le t\le\pi\}.
\tag{L-105112.9}
\]

Here \(F'=z^3F\) and

\[
F''=z^2(z^4+3)F.
\tag{L-105112.10}
\]

Thus \(F,F',F''\) are nonzero on every \(E_r\): for \(r\le1\),
\(|z^4+3|\ge3-r^4\ge2\).  Exact norms are

\[
m_1(E_r)=r^3,
\qquad
\|W_*\|_{E_r}=r^2,
\qquad
\left\|W_*\frac F{F'}\right\|_{E_r}=\frac1r.
\tag{L-105112.11}
\]

On the upper semicircle of radius \(1/2\), the broad formula would predict

\[
\frac\tau{m_1(E_{1/2})}=8,
\tag{L-105112.12}
\]

but the actual weighted norm is

\[
\left\|W_*F/F'\right\|_{E_{1/2}}=2.
\tag{L-105112.13}
\]

The repaired product inequality is sharp there:
\(\|W_*\|_{E_{1/2}}/m_1(E_{1/2})=(1/4)/(1/8)=2\).
On the unit upper semicircle \(E_1\subset\partial\Omega\), the same-domain
equality gives \(1=\tau/m_1(E_1)\), exactly as required.

## 5. Boundary of the repair

The T-105109 exterior-critical fixture takes its relevant arcs on the unit
circle of the same unit-disk selector problem.  Its actual same-domain
weighted-sup divergence is therefore not overturned by this repair.  The
repair only rejects use of the scalar \(\tau\) as a pointwise modulus on an
arc not authenticated as part of that selector domain's boundary.

No Xi collar, denominator margin, selector-growth absorption, oriented-edge
cancellation, strict coherence, RCMV104530, or RH conclusion follows.
