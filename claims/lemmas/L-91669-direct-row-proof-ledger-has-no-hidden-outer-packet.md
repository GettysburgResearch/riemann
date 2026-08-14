# L-91669 — The direct-row ledger has no hidden outer packet and loses at most \(2\log X\) of equality score

Claim ID: `L-91669`  
Status: **PROPOSED COMPLETE ALL-DEPTH SCORE/CAPACITY THEOREM ON FROZEN INPUTS — INDEPENDENT RECONSTRUCTION REQUIRED**  
Created: 2026-08-14  
Supersedes in the direct-row route: the vague recurrence constant and the
historical outer/collar/port ownership table in `L-91667`  
Primary inputs: `L-26204`, `L-91540`, `L-91545`, `L-91554`, `L-91556`,
`L-91559`, `L-91622`, `L-91663`, `L-91666`, `L-91668`  
RH status: **unproved pending reconstruction**

## 1. Normative normalization

Put

\[
 t=\log X.
 \tag{L-91669.1}
\]

The equality-density theorem `L-26204` has the normalized target equation

\[
 \boxed{(L_*\ast\varrho)(t)=t}
 \tag{L-91669.2}
\]

and exact critical score

\[
 \boxed{
 2\int_0^\infty e^{-u/2}L_*(u)\,du=4.
 }
 \tag{L-91669.3}
\]

After physical scaling, the root equality packet \(P_X^{\rm eq}\) therefore has

\[
 \boxed{
 M_X(P_X^{\rm eq})=\log X,
 \qquad
 J_X(P_X^{\rm eq})=4\sqrt X.
 }
 \tag{L-91669.4}
\]

Here \(M\) is the target ledger used in `L-91540/L-91622`, and \(J\) is the
row-budgeted declared score.  Equation (L-91669.4) is not a change of
normalization: `L-91556`, `L-91621`, and `L-91557` use this same native target
and score normalization.  A review which finds a scalar rescaling between
these files rejects this theorem.

## 2. Positive root entry

`L-91668` supplies a positive source-disjoint realization of the exact native
row

\[
 c_X(j)=\sum_{n\le X}\frac{\mu(n)}{\sqrt n}Q_{X/n}(j),
 \tag{L-91669.5}
\]

with

\[
 \Gamma(c_X;q)=w_X(q),
 \qquad
 \Xi(c_X;q)=\Omega_X(q).
 \tag{L-91669.6}
\]

The leafwise Hall output is a positive direct sum of survival and hazard typed
packets, together with positive target-null current row bonuses.  It preserves
the root target exactly and superordinates the root declared score:

\[
 \sum_\alpha M_X(P_{\alpha,X})=\log X,
 \tag{L-91669.7}
\]

\[
 \sum_\alpha J_X(P_{\alpha,X})\ge4\sqrt X.
 \tag{L-91669.8}
\]

The sum in (L-91669.7) is over positive source-disjoint typed packets after the
Hall step.  Hall bonuses are not assigned target mass and have nonnegative
literal score.

## 3. Fixed-\(67\) source restriction

For one positive typed packet \(P=(\tau,\nu,Y)\), restrict the source to

\[
 \nu^{\rm ch}=\nu|_{\{n\le Y/67\}}
 \tag{L-91669.9}
\]

and evaluate it at endpoint \(Y/67\), retaining the same type.  Write
\(P^{\rm ch}\) for this canonical child.  Target positivity gives the exact
split

\[
 \boxed{
 M_Y(P)
 =
 M_{Y/67}(P^{\rm ch})+M_Y^{\rm term}(P),
 \qquad
 M_Y^{\rm term}(P)\ge0.
 }
 \tag{L-91669.10}
\]

The term \(M_Y^{\rm term}(P)\) includes both source atoms which leave the child
support and the positive target residual of surviving atoms.  For a positive
direct sum, (L-91669.10) is summed before normalization.

Iterate until the endpoint is below \(67\).  Since every target term is positive
and every child belongs to exactly one parent, telescoping gives

\[
 \boxed{
 \sum_{r\ge0}M_r^{\rm term}=M_0=\log X.
 }
 \tag{L-91669.11}
\]

There is no factor equal to the number of leaves or the number of generations.
Equation (L-91669.11) is the global source-disjoint terminal-mass firewall.

## 4. Nonterminal score is paid coefficient one

For one source atom with local quotient \(Z\ge67\), its literal component
entropy is

\[
 E(Z)=
 \sum_{2\le m\le Z}
 \frac{\log m}{\sqrt m}\log(Z/m).
 \tag{L-91669.12}
\]

`L-91666` proves globally

\[
 \boxed{
 E(Z)-E(Z/67)
 \ge
 5\left(\sqrt Z-\sqrt{Z/67}\right).
 }
 \tag{L-91669.13}
\]

After multiplication by either exact branch coefficient

\[
 \kappa_s=1-p^{-1},
 \qquad
 \kappa_h=p^{-1},
 \qquad
 \kappa_s+\kappa_h=1,
 \tag{L-91669.14}
\]

the canonical current row difference pays the complete declared-score
difference of that source atom.  Consequently no positive score debt is
charged on any nonterminal edge.

## 5. Terminal debt is at most twice terminal target

At a terminal quotient \(1\le Z<67\), the exact physical corridor in
`L-91540/L-91622` gives

\[
 \boxed{
 [J_{\rm term}(Z)-\mathcal S_{\rm term}(Z)]_+
 \le2\,M_{\rm term}(Z).
 }
 \tag{L-91669.15}
\]

Sum (L-91669.15) over all terminal atoms, labels, and depths.  Source
disjointness and (L-91669.11) give

\[
 \boxed{
 \Delta_{\rm terminal}(X)
 \le
 2\sum_{r\ge0}M_r^{\rm term}
 =
 2\log X.
 }
 \tag{L-91669.16}
\]

This replaces both of the following unsafe estimates:

```text
constant per stopped leaf;
constant per depth times the root target.
```

The finite-Euler bound \(<3600\) in `L-91554` remains a valid independent
sourcewise cross-check, but it is not needed for the global asymptotic.  The
load-bearing global charge is (L-91669.16).

## 6. All-depth same-index physical assembly

At one parent packet, let \(R_Y(P)\) be its canonical literal row and let
\(R_{Y/67}(P^{\rm ch})\) be the canonical child row, placed at the same integer
row indices.  Endpoint monotonicity gives

\[
 R_Y(P)-R_{Y/67}(P^{\rm ch})\ge0.
 \tag{L-91669.17}
\]

If \(d_{\rm ch}\) is feasible for the complete child capacities, define

\[
 d_Y(P)
 =
 R_Y(P)-R_{Y/67}(P^{\rm ch})+d_{\rm ch}.
 \tag{L-91669.18}
\]

`L-91559/L-91663` give, for every physical integer column \(q\ge2\),

\[
 \Gamma(d_Y(P);q)
 \le\Gamma(R_Y(P);q),
 \tag{L-91669.19}
\]

\[
 \Xi(d_Y(P);q)
 \le\Xi(R_Y(P);q).
 \tag{L-91669.20}
\]

Start at the finite terminal layer and apply (L-91669.18) upward.  The tree is
finite for fixed \(X\), all row differences are nonnegative, and all Hall
bonuses are nonnegative current rows.  Summing the typed packets at each common
endpoint gives one finite row \(d_X\ge0\) such that

\[
 \boxed{
 \Gamma(d_X;q)\le w_X(q),
 \qquad
 \Xi(d_X;q)\le\Omega_X(q)
 \quad(q\ge2).
 }
 \tag{L-91669.21}
\]

The child is inserted by the identity on row indices.  No affine lift,
fractional column, small-prime reintroduction, or formal residual complement is
used.

## 7. Explicit score lower bound

The root declared score is at least \(4\sqrt X\) by (L-91669.8).  Every
nonterminal declared-score difference is paid by literal entropy, every Hall
bonus has nonnegative literal score, and the entire terminal deficit is bounded
by (L-91669.16).  Therefore the row constructed in Section 6 satisfies

\[
 \boxed{
 \mathcal S_X(d_X)
 \ge4\sqrt X-2\log X.
 }
 \tag{L-91669.22}
\]

For the finitely many endpoints \(1\le X<67\), enlarge the right side by one
absolute finite-base constant if desired.  This does not affect any asymptotic
conclusion.

## 8. The direct route has one physical row, not two

The load-bearing capacity row is exactly the row built in Section 6.  The
following historical objects are **not added as row summands** in this route:

```text
continuum outer equality producer;
B-spline quantization;
width-three collar;
finite/continuum mismatch packet;
top-omission packet;
common endpoint port.
```

Those objects remain valuable independent constructions and audits for the
older `T-91101/T-91561` architecture.  They are not needed after the exact native
row response, positive leafwise realization, and same-index child replacement
have been proved.

The equality-density transform `L-26204` is consumed only for the exact root
target and score in (L-91669.4).  It does not contribute a second finite row or
consume a second copy of native capacity.

## 9. Review falsifiers

Reject this theorem on the first occurrence of any of:

```text
the target in L-26204 is not the target ledger of L-91556/L-91622;
the root target is not exactly log X in that normalization;
a source atom appears in two terminal layers;
terminal target masses do not telescope to the root target;
the terminal deficit bound exceeds 2T;
a nonterminal fixed-67 entropy difference fails;
a child is inserted at changed row indices;
an outer/collar/mismatch/port row is added on top of d_X;
ordinary or radix-four capacity is overdrawn in one column.
```

```text
root target                                      log X, exact
root declared score                              4 sqrt(X), exact
source-disjoint terminal target sum              <= log X, exact
all-depth terminal score debt                    <= 2 log X
nonterminal score debt                           zero
ordinary/detail physical assembly                exact same-index
final finite-row score                           >=4 sqrt(X)-2 log(X)
historical outer packet                          not load bearing
Riemann Hypothesis                               unproved pending review
```
