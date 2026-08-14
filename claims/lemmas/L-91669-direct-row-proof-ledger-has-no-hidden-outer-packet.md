# L-91669 — The one-use equality realization and the direct arithmetic child form one nonduplicating reset

Claim ID: `L-91669`  
Status: **PROPOSED COMPLETE CAPACITY/SCORE COMPOSITION ON FROZEN INPUTS — INDEPENDENT RECONSTRUCTION REQUIRED**  
Created: 2026-08-14  
Final hardening correction: the reciprocal-zeta equality weight is used only on
its certified finite positive window; the outer equality producer remains
load bearing as the one-use score/realization front door and is not deleted or
added as a second copy of native capacity.  
Primary inputs: `L-91107`, `L-91110`, `L-91111`, `L-91114`, `L-91115`,
`L-91320`, `L-91540`, `L-91545`, `L-91554`, `L-91556`, `L-91557`,
`L-91559`, `L-91560`, `L-91621`, `L-91622`, `L-91663`, `L-91666`,
`L-91668`, `L-91665`  
RH status: **unproved pending reconstruction**

## 1. Two representations of one root datum

There are two load-bearing descriptions of the same root equality datum.

### Score/endpoint representation

`L-26204/L-91557` give the exact continuum equality state.  At physical scale
\(X\), its critical score is

\[
 \boxed{J_{\rm eq}(X)=4\sqrt X.}
 \tag{L-91669.1}
\]

The reciprocal-zeta equality weight is

\[
 L_*(u)=
 \sum_{n\le e^u}\frac{\mu(n)}{\sqrt n}
 \left(2e^{(u-\log n)/2}-1\right).
 \tag{L-91669.2}
\]

No global sign is assumed.  `L-91107` proves only the finite-window statement

\[
 \boxed{
 L_*(u)>0.3186
 \quad
 0\le u\le\log(c_0^{-1}),
 \qquad
 c_0=0.01844367547104\ldots .
 }
 \tag{L-91669.3}
\]

This is the positive outer equality window used at each reset.  The unresolved
inner state is passed to a contracted generation; the same signed inverse is
not continued beyond its certified window.

### Exact finite-row representation

For real \(Y\ge1\), let \(Q_Y\) be the literal positive component row, and put

\[
 \boxed{
 c_X(j)=
 \sum_{n\le X}\frac{\mu(n)}{\sqrt n}Q_{X/n}(j).
 }
 \tag{L-91669.4}
\]

`L-91663` proves exactly

\[
 \boxed{
 \Gamma(c_X;q)=w_X(q),
 \qquad
 \Xi(c_X;q)=\Omega_X(q).
 }
 \tag{L-91669.5}
\]

`L-91668` supplies the labelled arithmetic source identity whose observation is
exactly (L-91669.4), rather than merely a scalar packet with the same target.

The score representation and the finite-row representation are not added.
The endpoint-frame construction is the one-use realization map which turns the
root equality datum into the finite source/row packet consumed below.  A
reviewer must reject the proposal if the source identity used in `L-91557` and
the finite identity used in `L-91668` are not the same normalized datum.

## 2. The current endpoint realization is used once

Put

\[
 K=\lceil c_0X\rceil,
 \qquad W=10000.
 \tag{L-91669.6}
\]

On the positive window, `L-91110` performs one martingale/B-spline
quantization of the equality density.  Its endpoint weights are nonnegative,
it reproduces both endpoint-frame modes exactly in the inherited bulk, and it
is score-favorable.

The remaining current terms are:

```text
one width-three positive quantization collar;
one finite/continuum mismatch packet;
one interior safety factor sigma_K=(1+175/K)^(-1);
one fixed top omission and terminal-annulus packet;
one corrected P_61/67 boundary port when that adapter is invoked.
```

`L-91111`, `L-91114`, `L-91115`, and `L-91320` prove that these terms have
nonnegative endpoint ownership, consume the physical outer and boundary
capacities at most once, and have one-generation score charge bounded by an
effective absolute constant \(C_{\rm cur}\).

All current continuum terms are summed before the single quantization.  They
are then part of the complete current row.  They are never:

```text
quantized separately by rough color;
reintroduced on a child;
added on top of a second copy of c_X;
or charged once per Hall leaf.
```

This is the exact meaning of “one-use current packet.”

## 3. Explicit labelled arithmetic entry

`L-91330` gives the atomwise positive two-channel split.  `L-91333` gives the
nonduplicating least-prime tree.  `L-91668` now explicitly supplies the source
identity antecedent of `L-91621`, proves unique fixed-\(X\) ownership, and
identifies the observed root row with \(c_X\).

Apply the exact native cocycle and frozen no-upward Hall transport separately on
every stopped leaf.  The complete finite parent row has the literal identity

\[
 \boxed{
 R_{\rm parent}
 =R_{\rm pre}
 +R_s(c_s)+R_h(c_h)+B_s+B_h,
 }
 \tag{L-91669.7}
\]

where every term is coefficientwise nonnegative, \(c_s,c_h\) are positive
target-bearing source measures, and \(B_s,B_h\) are target-null positive
current rows.  Hall is chosen leafwise before summation and is never commuted
through the rough tree.

The label of every term records:

```text
endpoint-frame owner;
least-prime leaf;
source index;
survival/hazard type;
generation.
```

No label has two owners.

## 4. Same-index child replacement after the complete current sum

Restrict both positive residual sources to their canonical fixed-\(67\) child,
and let \(R_{\rm ch}\) be the complete canonical child row.  Let
\(d_{\rm ch}\) be an arbitrary row feasible for the complete child capacities.
After all current endpoint, mismatch, collar, terminal, port, and Hall terms
have been summed once, define

\[
 \boxed{
 d_X=R_{\rm parent}-R_{\rm ch}+d_{\rm ch}.
 }
 \tag{L-91669.8}
\]

Endpoint monotonicity gives \(d_X\ge0\).  `L-91559/L-91663` give, for every
physical integer column \(q\ge2\),

\[
 \boxed{
 \Gamma(d_X;q)
 =\Gamma(R_{\rm parent};q)-\Gamma(R_{\rm ch};q)
 +\Gamma(d_{\rm ch};q)
 \le\Gamma(R_{\rm parent};q),
 }
 \tag{L-91669.9}
\]

\[
 \boxed{
 \Xi(d_X;q)
 =\Xi(R_{\rm parent};q)-\Xi(R_{\rm ch};q)
 +\Xi(d_{\rm ch};q)
 \le\Xi(R_{\rm parent};q).
 }
 \tag{L-91669.10}
\]

The outer-current realization and the arithmetic direct row are stages of the
single parent row in (L-91669.8), not independent capacity copies.  The child
is inserted at the same literal row indices.  No affine lift, fractional
column, scalar child surrogate, duplicated small-prime block, or formal
coordinatewise complement is used.

## 5. Physical columns are exhausted explicitly

The complete current parent row is feasible by the following exhaustive
partition.

```text
q<K:          exact inherited bulk reproduction and native child identity;
K<=q<=X/4:   L-91114 mismatch-plus-collar safety inequality;
X/4<q<X:     L-91115 fixed top-omission inequality;
q>=X:        triangular zero.
```

Equations (L-91669.9)--(L-91669.10) then replace the canonical child without
increasing either response.  Hence the final row satisfies

\[
 \boxed{
 \Gamma(d_X;q)\le w_X(q),
 \qquad
 \Xi(d_X;q)\le\Omega_X(q)
 \quad(q\ge2).
 }
 \tag{L-91669.11}
\]

This is one displayed simultaneous inequality for the complete summed row.  It
is not inferred from a list of heterogeneous local feasibility claims.

## 6. Nonterminal score transfer

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
 \ge5(\sqrt Z-\sqrt{Z/67}).
 }
 \tag{L-91669.13}
\]

After multiplication by the exact branch coefficients
\(\kappa_s=1-p^{-1}\) and \(\kappa_h=p^{-1}\), the literal current row pays the
complete row-budgeted declared-score difference with coefficient one.  No
positive score debt is charged on a nonterminal arithmetic edge.

## 7. Terminal and generation accounting

At a terminal quotient \(1\le Z<67\), `L-91622` gives

\[
 \boxed{
 [J_{\rm term}(Z)-\mathcal S_{\rm term}(Z)]_+
 \le2M_{\rm term}(Z).
 }
 \tag{L-91669.14}
\]

Equivalently, `L-91554` supplies an independent fixed-Euler sourcewise bound
(`<3600` for `P_61`).  Source disjointness implies that terminal target is
spent once.  Thus terminal debt is charged to total terminal mass, never to the
number of stopped leaves.  In the root normalization its all-depth contribution
is \(O(\log X)\); if the exact target normalization \(M_0=\log X\) is used, the
bound is at most \(2\log X\).

The current analytic/discrete charge \(C_{\rm cur}\) is incurred once per
factor-\(67\) generation.  There are at most

\[
 1+\left\lceil\frac{\log X}{\log67}\right\rceil
 \tag{L-91669.15}
\]

generations.  Therefore the complete row realizes the root equality score up
to logarithmic debt:

\[
 \boxed{
 \mathcal S_X(d_X)
 \ge4\sqrt X-C_1\log X-C_2
 }
 \tag{L-91669.16}
\]

for effective absolute constants \(C_1,C_2\).  This is the exact scope needed
by the endpoint consumer; no absolute all-depth score transfer is asserted.

## 8. What the corrected composition uses

```text
finite-window positivity of L_*                     yes, load bearing
global positivity of L_*                            no, forbidden
outer equality producer and one quantization        yes, current only
finite mismatch/collar/top omission                 yes, current only
corrected P_61/67 port                               at most once per generation
labelled arithmetic source tree                     yes
leafwise Hall                                       yes
same-index child replacement                        yes
outer packet added as second c_X copy               no
terminal constant per leaf                          no
score debt                                           O(log X)
Riemann Hypothesis                                   unproved pending review
```

## 9. Exact falsifiers

Reject this lemma immediately if any of the following occurs:

```text
L_* is used outside the certified first 54.2 quotient cells;
the continuum equality datum and finite c_X datum have different normalization;
one current endpoint packet is quantized twice;
one current mismatch, collar, omission, or port is copied to a child;
one arithmetic source appears in two stopped leaves;
Hall is commuted through the rough tree;
the complete current row is not summed before child subtraction;
one physical column range is omitted;
an outer-current row and c_X are charged as independent capacity copies;
C_cur depends on X or on the number of leaves;
terminal debt is charged per leaf instead of terminal mass;
L-91666 fails;
a child changes literal row indices.
```
