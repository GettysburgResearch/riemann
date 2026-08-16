# L-94121 — The live native endpoint fibre satisfies the projective gluing hypotheses

Claim ID: `L-94121`  
Status: **PROPOSED COMPLETE NATIVE SPECIALIZATION WITH DETERMINISTIC REPLAY**  
Created: 2026-08-16  
Inputs: `L-91355`, `L-91362`, `L-91402`, `L-91403`, `L-91650`, `L-93783`, `L-94120`; live 94020 registry  
Frozen directed input: PR #508 `4ae97dffd1f76ed3244b8f3028560ffa80663caf`  
RH status: **unproved pending hostile reconstruction**

## 1. Actual source fibre

For global endpoint `X` and endpoint parameter `s`, put

\[
x=X/s.
\]

The paired native source occurrence has the exact root profiles

\[
E_x(k)=k^{-1/2}(2\sqrt{x/k}-1),
\qquad
R_x(k)=k^{-1/2}(\sqrt{x/k}-1),
\]

\[
T_x(k)=E_x(k)+2R_x(k),
\qquad
S_x(k)=2E_x(k)+R_x(k).
\]

The equality channel carries the component row and all ordinary responses; the
reserve channel is row-zero.  One arithmetic occurrence coefficient is used in
both channels.

The exact finite anchored source is labelled by

```text
(endpoint cell, P61 divisor, parity, ordered rough history,
 first rough owner, causal path, equality/reserve channel).
```

The retained 94020 source registry enumerates the complete `X=536` instance,
including all `327` squarefree native labels and all `2473` finite endpoint
occurrences.  It is imported byte-for-byte under `imports/t94120/94020-live-source`.

## 2. Atomwise stopped-hazard map

Write a squarefree native colour uniquely as

\[
k=d p_1\cdots p_t,
\qquad d\mid P_{61},
\qquad 67\le p_1<\cdots<p_t.
\]

The map to the stopped tree keeps exactly this tuple.  The coefficient carried
by the path is the original occurrence coefficient; the source compiler does
not multiply it again.  At a causal edge `p`, the actual child incidence carries
one factor `p^(-1/2)` and one parity swap.  Therefore the coefficient and parity
on either side of the commuting square (L-94120.4) agree atom by atom.

The exact hazard coefficients split the incoming parent incidence once: the
survivor plus all current coefficients sum to one, and each recursive child
coefficient is the matching current coefficient times its unique rough-prime
factor.  Grouping by complete rough history then telescopes every nonterminal
current incidence into the next stopped node.  The only current incidences
observed are those whose final child quotient is below `67`; these are exactly
the terminal `(p,y)` leaves of Section 3.  The remaining incidences are the
actual oriented source frontier and have total target mass `<1/8`.

This proves the native marginal statement absent from synthetic fixtures:
stopping, hazard allocation, recursion and terminal leaf coupling partition the
literal source incidence measure rather than a row-first rough lift.

## 3. Terminal leaf map

At a terminal leaf `(p,y)`, `p>=67` and `1<=y<67`.  For every `d|P61`, the leaf
has target, score and component row

\[
K_T(d)=d^{-1/2}[T(py/d)-p^{-1/2}T(y/d)],
\]

\[
K_S(d)=d^{-1/2}[S(py/d)-p^{-1/2}S(y/d)],
\]

\[
K_R^{(j)}(d)=d^{-1/2}
[Q_{py/d}(j)-p^{-1/2}Q_{y/d}(j)].
\]

PR #508's directed complete Arithmetic Vector–Lorenz theorem supplies one
leftmost coefficient vector `u_d` satisfying simultaneously

\[
\sum_{\mu(d)=1}u_dK_T(d)
 =\sum_{\mu(d)=-1}K_T(d),
\]

\[
B_j=\sum_{\mu(d)=1}u_dK_R^{(j)}(d)
 -\sum_{\mu(d)=-1}K_R^{(j)}(d)\ge0,
\]

and a nonnegative declared-score surplus.  The same `u_d` is used in target,
score, every row, ordinary `q`, and ordinary `4q`.

The imported `(67,13)` proof object contains all `229` active divisor atoms and
all native coordinates.  It is a live leaf of the same source registry, not a
toy vector.

## 4. The q=2 obstruction is bypassed, not contradicted

The oriented child incidence is never sent to the physical cone.  It remains
inside the paired terminal leaf until the `u_d` transport has formed the
nonnegative row bonus and residual source.  The separate positive terminal
child in the causal budget is outer because its scale is below `67` and is
realized by the directed equality/reserve fibre.

Consequently the negative q=2 child witness from PR #512/#514 is retained as a
regression while the complete source marginal still closes.

```text
native occurrence marginal              literal / atomwise
rough-lift parent                        absent
first owner                              unique
path coefficient                         original / one application
intermediate child observation           absent
terminal TL coefficient vector           common in every coordinate
outer terminal fibre                     directed positive
```
