# L-91840 — Restriction before quadrature closes partial-cell ownership

Claim ID: `L-91840`  
Status: **PROVED EXACT MEASURE/ADJACENT-CARRY LOCALIZATION THEOREM**  
Created: 2026-08-15  
Primary inputs: `L-91733`; the signed finite/continuum defect measure on each endpoint cell  
Preferred specialization: the whole-cell support of PR #487 / `L-91754`  
RH status: **unproved**

## 1. The interface that must be typed

Let

\[
I_n=[n,n+1),\qquad n\in\mathbb Z_{\ge1},
\]

and let `eta_X` be the signed finite-versus-continuum defect measure on the
endpoint line. A retained quotient collar generally pulls back to a Borel set
`A_X` which may cut some integer endpoint cells. The correct retained adjacent
error is therefore not the full-cell number from an intersected cell. It is

\[
\boxed{
 \varepsilon_X^{A}(n)=\eta_X(A_X\cap I_n).
}
\tag{L-91840.1}
\]

The restriction is performed before cell integration and before the ordinary
carry map.

## 2. Cumulative seed and exact adjacent identity

Define

\[
 E_X^{A}(m)=\sum_{n\ge m}\varepsilon_X^{A}(n),
\tag{L-91840.2}
\]

where the sum is finite on the truncated endpoint support. Then

\[
\boxed{
 E_X^{A}(m)-E_X^{A}(m+1)=\varepsilon_X^{A}(m).
}
\tag{L-91840.3}
\]

There is no artificial lower-cutoff atom and no full-cell error is assigned to
a retained subcell.

For every physical ordinary column `q>=2`, the adjacent-carry functional gives

\[
\begin{aligned}
 v_q(E_X^{A})
 &=\sum_{j\ge1}[E_X^{A}(jq)-E_X^{A}(jq+1)]\\
 &=\boxed{\sum_{j\ge1}\eta_X(A_X\cap I_{jq})}.
\end{aligned}
\tag{L-91840.4}
\]

The radix-four response is obtained by applying (L-91840.4) at `q` and `4q`
separately and then subtracting.

## 3. Additivity and source ownership

If `A_X=A_1\dot\cup\cdots\dot\cup A_r` is a disjoint Borel partition, then

\[
 \varepsilon_X^A(n)=\sum_h\varepsilon_X^{A_h}(n),
 \qquad
 v_q(E_X^A)=\sum_hv_q(E_X^{A_h}).
\tag{L-91840.5}
\]

Thus retained, omitted, current-owned and child-owned portions of a cut cell
may be recorded separately without duplicating its finite/continuum defect.

If the frozen cellwise total-variation estimate is

\[
 |\eta_X|(I_n)<\frac{19}{2}n^{-3/2},
\tag{L-91840.6}
\]

then restriction only decreases total variation, so every all-column estimate
proved from that majorant remains valid with `epsilon_X(n)` replaced by
`epsilon_X^A(n)`.

## 4. Whole-cell specialization

PR #487 chooses a retained endpoint interval which is a union of complete
integer cells. Then `A_X cap I_n` is either `I_n` or empty and (L-91840.1)
reduces exactly to the retained-cell seed of `L-91733`. No partial-cell theorem
is load-bearing in that preferred one-shot route.

This lemma records the more general interface which the earlier collar-based
composition needed and shows why the operation order must be

```text
restrict the signed defect measure;
form adjacent cell masses;
form the cumulative seed;
apply ordinary carry at q and 4q;
form radix-four detail.
```

## 5. Boundary

```text
partial-cell ownership                         exact by measure restriction
synthetic cutoff atom                          absent
ordinary carry of retained defect              exact
radix-four response                            exact from q and 4q
whole-cell PR #487 route                       immediate specialization
cellwise total-variation majorant              frozen analytic input
Riemann Hypothesis                             unproved
```
