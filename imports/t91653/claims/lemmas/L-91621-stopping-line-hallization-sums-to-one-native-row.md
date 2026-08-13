# L-91621 — Leafwise stopping-line Hallization sums to one global native row

Claim ID: `L-91621`  
Status: **PROVED EXACT SOURCE/ROW FUBINI THEOREM — LIVE ARITHMETIC INPUT MUST BE REPLAYED AT A FROZEN SHA**  
Created: 2026-08-13  
Depends on: the exact paired least-prime source recursion; the finite-block stopping-line regrouping; `L-91545`, `L-91556`, `L-91560`, `L-91562`  
RH status: **unproved**

## 1. Purpose

The corrected direct-row proposal already has an exact local one-prime
three-ledger cocycle and an exact target-Hall residualization.  The remaining
provenance question is whether those local constructions may be applied to all
stopped arithmetic leaves without either:

```text
copying a source atom;
commuting a nonlinear Hall choice through the rough tree;
or losing the exact literal parent-row identity.
```

This theorem proves that no commutation is needed.  Hall is performed separately
on source-disjoint complete leaves and the positive outputs are then summed.
The result is an exact global target and row identity and a global native-score
inequality.

## 2. Labeled positive stopping-line identity

Let `mathcal T` be a finite or countable rooted least-prime tree.  Work in the
**labeled** source space, so a source point is a pair `(v,n)` consisting of its
stopping-line leaf and its integer source index.  Let `mathcal L` be a stopping
line: no root-to-leaf path meets it twice, and every active infinite path either
meets it or terminates in the current finite/frontier packet.

Assume the exact positive source identity

\[
 \boxed{
 \boldsymbol\mu_{\rm root}
 =\boldsymbol\mu_{\rm cur}
  +\sum_{v\in\mathcal L}\boldsymbol\mu_v
 }
 \tag{L-91621.1}
\]

in the labeled source space, with all terms positive.  Because the labels are
part of the source space, the measures `boldsymbol mu_v` are mutually singular.
In particular, for every positive additive source mass `m`,

\[
 \boxed{
 m(\boldsymbol\mu_{\rm cur})
 +\sum_{v\in\mathcal L}m(\boldsymbol\mu_v)
 =m(\boldsymbol\mu_{\rm root}).
 }
 \tag{L-91621.2}
\]

The paired least-prime recursion proves (L-91621.1) by iteration and monotone
convergence.  It is stronger than an equality of total target masses.

## 3. Why every stopped leaf is a complete one-prime packet

Fix the finite small-prime block

\[
 P_{61}=\prod_{q\le61}q.
 \tag{L-91621.3}
\]

Choose the stopping line immediately after the last least rough prime `p>=67`
which moves the local child endpoint into

\[
 1\le y<67.
 \tag{L-91621.4}
\]

At a stopped leaf, unique factorization gives one complete Boolean block
`d|P_61`, one rough prime `p`, and no further active rough factor.  Indeed every
later rough prime is at least `67`, while its putative child endpoint is below
`67`.

Thus, after the finite Boolean states are regrouped before physical observation,
the leaf row is exactly the complete one-prime parent packet

\[
 \boxed{
 R_v^{\rm par}(j)
 =\sum_{d\mid P_{61}}
   \frac{\mu(d)}{\sqrt d}Q_{py/d}(j),
 }
 \tag{L-91621.5}
\]

with causal zero extension.  Its raw residual and unique exact raw child are

\[
 \boxed{
 R_v^{\rm res}(j)
 =\sum_{d\mid P_{61}}
  \frac{\mu(d)}{\sqrt d}
  \left[Q_{py/d}(j)-p^{-1/2}Q_{y/d}(j)\right],
 }
 \tag{L-91621.6}
\]

and

\[
 \boxed{
 R_v^{\rm child}(j)
 =p^{-1/2}
  \sum_{d\mid P_{61}}
  \frac{\mu(d)}{\sqrt d}Q_{y/d}(j).
 }
 \tag{L-91621.7}
\]

Therefore

\[
 \boxed{
 R_v^{\rm res}+R_v^{\rm child}=R_v^{\rm par}
 }
 \tag{L-91621.8}
\]

coefficientwise in every literal finite-row coordinate.  The identical identity
holds in the native target and native row-budgeted score ledgers.

## 4. Apply the controlled cocycle leafwise

Put

\[
 r=p^{-1/2},
 \qquad
 \kappa_s=1-r^2,
 \qquad
 \kappa_h=r^2.
 \tag{L-91621.9}
\]

`L-91560` is pointwise in the finite source coefficient `mu(d)/sqrt(d)`.
Consequently it gives, on every stopped leaf,

\[
 \boxed{
 (T_v^{\rm res},S_v^{\rm res},R_v^{\rm res})
 +(T_v^{\rm child},S_v^{\rm child},R_v^{\rm child})
 =
 (T_{v,s},\widetilde S_{v,s},R_{v,s})
 +(T_{v,h},\widetilde S_{v,h},R_{v,h}).
 }
 \tag{L-91621.10}
\]

Here

\[
 R_{v,s}=\kappa_sR_v^{\rm par},
 \qquad
 R_{v,h}=\kappa_hR_v^{\rm par},
 \qquad
 R_{v,s}+R_{v,h}=R_v^{\rm par}.
 \tag{L-91621.11}
\]

No rough monomial occurs twice: (L-91621.10) consumes the raw residual and its
unique child together.  The full binary score has an additional nonnegative
target-null surplus, but the native row budget in (L-91621.10) is exact.

## 5. Leafwise Hall residualization

For a branch type `tau in {s,h}`, let its positive and negative finite source
nodes be `E_v` and `O_v`.  The unchanged target-Hall graph has a no-upward
transport `t^v_(o,e)` satisfying

\[
 \sum_e t^v_{o,e}=b^v_oT_{v,\tau}(o),
 \qquad
 \sum_o t^v_{o,e}\le a^v_eT_{v,\tau}(e),
 \qquad
 t^v_{o,e}>0\Longrightarrow e\le o.
 \tag{L-91621.12}
\]

Define

\[
 c^v_{\tau}(e)
 =a^v_e-
  \frac1{T_{v,\tau}(e)}
  \sum_o t^v_{o,e}\ge0.
 \tag{L-91621.13}
\]

The target-per-native-score ratio and the target-normalized literal row profile
are nondecreasing along every Hall edge by `L-91562`.  Hence `L-91545` gives

\[
 \boxed{
 T(c^v_\tau)=T(E_v)-T(O_v),
 }
 \tag{L-91621.14}
\]

\[
 \boxed{
 \widetilde S(c^v_\tau)
 \ge\widetilde S(E_v)-\widetilde S(O_v),
 }
 \tag{L-91621.15}
\]

and

\[
 \boxed{
 R(E_v)-R(O_v)
 =R(c^v_\tau)+B^v_\tau,
 \qquad
 B^v_\tau\ge0,
 }
 \tag{L-91621.16}
\]

coefficientwise.  Every `B^v_tau` is a target-null current-generation positive
row bonus.

## 6. Global Fubini identity

Define the disjoint positive residual source

\[
 \boldsymbol c_\tau
 =\bigoplus_{v\in\mathcal L}c^v_\tau
 \tag{L-91621.17}
\]

and the global row bonus

\[
 B_\tau=\sum_{v\in\mathcal L}B^v_\tau.
 \tag{L-91621.18}
\]

For a finite stopping line, summing (L-91621.14)--(L-91621.16) is ordinary
finite linear algebra.  For a countable stopping line, all residual sources and
bonuses are nonnegative.  Truncate to finitely many leaves and use monotone
convergence.  Finiteness of the parent target supplies the required domination
for the signed left sides.

Combining the two branch labels and the local cocycle gives

\[
 \boxed{
 T(\boldsymbol c_s)+T(\boldsymbol c_h)
 =T_{\rm stopped,parent},
 }
 \tag{L-91621.19}
\]

\[
 \boxed{
 \widetilde S(\boldsymbol c_s)
 +\widetilde S(\boldsymbol c_h)
 \ge S_{\rm stopped,parent},
 }
 \tag{L-91621.20}
\]

and the exact literal row identity

\[
 \boxed{
 R_{\rm stopped,parent}
 =R(\boldsymbol c_s)+R(\boldsymbol c_h)
  +B_s+B_h.
 }
 \tag{L-91621.21}
\]

Adding the positive pre-stopping current packet from (L-91621.1) yields the
same three statements for the complete root packet.

This is the desired one-use provenance theorem.  Hall was never commuted with
the rough tree.  It was chosen leafwise and only its positive outputs were
summed.

## 7. Measurable continuum endpoint version

Suppose the root packet is integrated against a positive endpoint parameter
measure `lambda`.  On the fixed finite Hall graph, choose the deterministic
greedy no-upward transport: process demands in increasing source order and fill
eligible capacities in increasing order.  Its entries are obtained from the
input target atoms by finitely many applications of `+`, `-`, division by a
strictly positive target atom, and `min`.  They are therefore Borel measurable
in the endpoint parameter.

Apply Sections 3--6 first to positive simple endpoint measures.  Approximate an
arbitrary positive `lambda` monotonically by simple measures.  Component rows,
targets, residual sources and Hall bonuses are positive kernels on the compact
reset window, so monotone convergence gives (L-91621.19) and (L-91621.21).
Fatou's lemma gives the score inequality (L-91621.20).

Thus the theorem applies to the positive continuum endpoint packets used by the
factor-54 equality-density reset, not only to one discrete endpoint.

## 8. Consequence and firewall

The exact source/tree obligation may now be separated cleanly from the physical
child replacement:

```text
paired stopping-line source identity
 -> complete one-prime leaves
 -> exact native controlled cocycle
 -> leafwise target Hall
 -> global positive residual sources + positive row bonuses
 -> one global literal parent-row identity.
```

The theorem does not assert that the fixed-67 child should be affinely dilated.
That operation is refuted by `R-91558`.  Every later child replacement must use
the direct nested identity theorem `L-91559`.

It also does not certify that a moving branch still contains the exact finite
source formulas cited above.  A live promotion must freeze the current parent
SHA and replay (L-91621.5)--(L-91621.8) from its source definitions.

```text
stopping-line source disjointness                      EXACT
complete P_61 one-prime leaf form                      EXACT
raw residual + unique child provenance                 EXACT
leafwise native three-ledger cocycle                    EXACT
leafwise Hall source/row decomposition                 EXACT
countable/global target and row identity               EXACT
continuum endpoint Fubini extension                    EXACT
nonlinear Hall/tree commutation                         NOT NEEDED
fixed-67 physical child replacement                    SEPARATE / L-91559
live frozen arithmetic replay                          REQUIRED
Riemann Hypothesis                                     UNPROVEN
```
