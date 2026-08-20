# T-99722 — Corrected OCE67: all diagonal and cross-owner costs close, one cross-core Gram remains

Claim ID: `T-99722`  
Status: **UNCONDITIONAL REDUCTION + CONDITIONAL RH THEOREM; ONE GLOBAL GATE OPEN**  
Created: 2026-08-20  
Depends on: `L-99720--L-99722`; `R-99721`; PRs #653, #658, #659  
RH status: **unproved**

## 1. Scope correction

There are two materially different readings of an owner-Carleson embedding.

```text
UOCE67:
    a subpower operator bound for every finite future-prime profile;

SOCE67:
    a subpower bound for the one complete native scalar orbit, retaining
    the small-prime base, every future-prime coefficient, and all cross-core
    covariance before physical collapse.
```

`R-99721` proves that `UOCE67` is false with polynomial loss on an actual
rough-prime interval. Only `SOCE67` can be conclusion-producing.

## 2. Exact owner reduction

Let `K` be the compact ratio-eight zero-safe kernel and write the complete
native rough source in first-owner form. For owner `i`, put

\[
A_i(X)=
\sum_A(-1)^{|A|}r_A
\left[K(X/n_A)-K(X/(p_i n_A))\right].
\tag{T-99722.1}
\]

Convex first ownership gives

\[
\boxed{
|\mathcal K h(X)|^2
\le
s_k|K(X)|^2+
\sum_i\lambda_i|A_i(X)|^2.
}
\tag{T-99722.2}
\]

For `X>8`, the root term vanishes. By `L-99722`,

\[
|A_i(X)|^2=D_i(X)+C_i(X),
\qquad
D_i(X)<60,
\]

and hence

\[
\boxed{
|\mathcal K h(X)|^2
\le
60+
\sum_i\lambda_i[C_i(X)]_+.
}
\tag{T-99722.3}
\]

Every cross-owner term and every diagonal future-profile term has therefore
been paid unconditionally. The only unresolved quantity is the signed
near-collision form

\[
C_i(X)=
\sum_{A\ne B}
(-1)^{|A|+|B|}r_Ar_B
\,d_{i,A}(X)d_{i,B}(X).
\tag{T-99722.4}
\]

The pairs `A,B` are incomparable squarefree future products whose ratios lie
inside the compact observation window. This is exactly the cross-core
arithmetic omitted by a source-blind collapse.

## 3. Correct source-orbit embedding

Define **SOCE67** to be the block estimate obtained after the same positive
inverse filter as in PR #659:

\[
\boxed{
\sum_{k=0}^{L+1}b_{L,k}
\int_{2^{L-k}}^{2^{L+1-k}}
\left(
60+
\sum_i\lambda_i[C_{i,L}(y)]_+
\right)^{1/2}
\frac{dy}{y}
=2^{o(L)}.
}
\tag{T-99722.5}
\]

Here `C_(i,L)` is formed from the fixed order-`M_L` compact packet, and the
coefficients `b_(L,k)` are the exact positive inverse coefficients of PR #659.
The owner ordering, native activities, dyadic base, duplicated 67 fibre, and
endpoint kernel are fixed before the sign is observed.

Then (T-99722.3), the positive inverse, and Cauchy--Schwarz give subpower
logarithmic negative mass for the zero-safe compact scalar. PR #653's
specialized Mellin--Landau theorem therefore yields

\[
\boxed{\mathrm{SOCE67}\Longrightarrow\mathrm{RH}.}
\tag{T-99722.6}
\]

## 4. Reconciliation with the other live frontiers

The residual form (T-99722.4) is the same arithmetic boundary seen in three
languages:

```text
PR #658: live prime-exchange min-cut / PXGC99700;
PR #659: signed Poisson off-diagonal packing / GPMOC99800;
this PR: first-owner near-collision Gram / SOCE67.
```

The diagonal, local spectral gap, activation-safe filtering, and first-owner
coefficient algebra are no longer open. A proof must control covariance
between distinct squarefree cores on the complete source orbit.

## 5. Scientific boundary

```text
native first-owner coefficient identity        PROVED EXACT
native Littlewood--Paley identity               PROVED EXACT
convex cross-owner decoupling                    PROVED EXACT
compact owner diagonal                          PROVED UNIFORMLY BOUNDED
universal branchwise OCE                         REFUTED
SOCE67 cross-core embedding                      OPEN / RH-BEARING
Riemann Hypothesis                               UNPROVEN
```

The theorem is a conclusion-complete reduction, not a proof of SOCE67. Any
claim that the labelled square function alone closes the physical scalar must
pass the prime-interval separator of `R-99721`.
