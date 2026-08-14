# L-91671 — An atomwise provenance partition is the exact native root-ledger certificate

Claim ID: `L-91671`  
Status: **PROVED ABSTRACT SUFFICIENCY AND FINITE FARKAS ALTERNATIVE**  
Created: 2026-08-14  
Depends on: `R-91671`; positive native producer maps imported by the factor-54 programme  
RH status: **unproved**

## 1. Ordered native datum

Let `V` be the real vector space containing, in one fixed normalization,

```text
target;
literal entropy score;
every exact component row;
every ordinary capacity column;
every radix-four capacity column;
the shared endpoint-port coordinate;
all declared boundary reserves.
```

Let `K subset V` be the product cone of nonnegative reserve coordinates and write `u <= v` when `v-u in K`.

Let `E` be the finite set of root source occurrences. Each occurrence has nonnegative weight `w_e` and one unit native datum `v_e in K`. The complete root source is

\[
 \mathcal N=\sum_{e\in E}w_ev_e.
 \tag{L-91671.1}
\]

The labels must include every repaired base occurrence, in particular the `d=1`, `d=2`, and `d=5` packets identified by the independent review.

## 2. Local producer packets

Let the current channel set be

\[
 \mathcal C=
 \{\mathrm{Hall},\mathrm{outer},\mathrm{collar},
   \mathrm{mismatch},\mathrm{omission},\mathrm{shared\ port}\}.
\]

Also retain the recursive-child and terminal/stopping channels.

For every channel `c` and source occurrence `e`, a local producer certificate consists of a coefficient `x_{c,e}>=0`, an output datum `y_{c,e}`, and a nonnegative local remainder `r_{c,e} in K` satisfying

\[
 \boxed{x_{c,e}v_e=y_{c,e}+r_{c,e}.}
 \tag{L-91671.2}
\]

Thus the local producer is checked in the same target/score/row/capacity/port coordinates as the root datum. Any target-null positive row bonus is included inside `y_{c,e}`; it is not an uncharged extra row.

## 3. Atomwise nonduplication

Assume residual coefficients `ell_e>=0` satisfy

\[
 \boxed{
 \ell_e+\sum_{c\in\mathcal C}x_{c,e}+x_{{\rm child},e}+x_{{\rm stop},e}=w_e
 \qquad(e\in E).
 }
 \tag{L-91671.3}
\]

The common endpoint port is one member of `C`, not one independently available port for each producer.

Summing (L-91671.2) and (L-91671.3) gives the exact decomposition

\[
 \boxed{
 \mathcal N=\mathcal L+\mathcal D_{\rm current}+\mathcal D_{\rm child}+\mathcal D_{\rm stop}+\mathcal R_{\rm local}.
 }
 \tag{L-91671.4}
\]

where `L` and `R_local` lie in the native positive cone. Consequently

\[
 \boxed{
 \mathcal D_{\rm current}+\mathcal D_{\rm child}+\mathcal D_{\rm stop}\preceq\mathcal N.
 }
 \tag{L-91671.5}
\]

Every native coordinate is controlled simultaneously. No extra tensorization, normalization inference, or sum-before-quantize argument is needed.

## 4. Exact native-root theorem

Suppose the local certificates additionally identify:

```text
the actual causal child coefficient and same-index child datum;
the repaired base packets d=1,2,5;
the P_61 / rough-threshold-67 endpoint-port adapter;
every Hall, outer, collar, mismatch, and omission row;
the one-use terminal stopping charge.
```

Then (L-91671.4) is exactly the native root current ledger required by the reviewed factor-54 composition. Combined with the already verified causal reset and total recursive coefficient below `1/8`, it supplies the first open producer hypothesis of `T-91652`.

This lemma proves sufficiency. It does not construct the coefficients `x_{c,e}` for the live root packet.

## 5. Finite primal certificate

After the finite source occurrences and producer templates have been fixed, the unknown allocation coefficients form a finite vector `x>=0`. The exact ledger has the form

\[
 Bx=b,\qquad Gx\le c,\qquad x\ge0.
 \tag{L-91671.6}
\]

where `Bx=b` records exact target, score, component-row, and provenance identities, while `Gx<=c` records atomwise, ordinary, radix-four, boundary, and port capacities. A rational solution is a replayable proof certificate.

## 6. Exact Farkas alternative

Introduce nonnegative slack `s`. Exactly one of the following holds:

1. the primal ledger (L-91671.6) is feasible;
2. there exist a free vector `y` and `z>=0` such that

\[
 \boxed{
 B^Ty+G^Tz\ge0,
 \qquad
 b^Ty+c^Tz<0.
 }
 \tag{L-91671.7}
\]

The second object is an exact dual separator. Therefore the root theorem is fail-closed once its live finite templates are exported: return either the atomwise allocation or one rational obstruction.

## 7. Why this is stronger than coordinatewise checking

A coordinatewise capacity check without source labels can conceal the same source occurrence in several producer rows. Equation (L-91671.3) forbids that before the native vectors are summed. Conversely, once the atomwise partition and local identities hold, every coordinate follows by positivity and linearity.

Thus source provenance is the minimal common invariant connecting causal packet accounting, Hall flow, finite row positivity, ordinary/radix-four capacity, literal entropy, and one common endpoint port.

## 8. Exact boundary

```text
atomwise partition + local native identities -> root ledger   PROVED
combined current/child/stop capacity                           PROVED
finite primal/dual alternative                                PROVED
live L-91659 allocation coefficients                           OPEN / FINITE PRODUCER
T-91652                                                       CONDITIONAL
Riemann Hypothesis                                             UNPROVEN
```
