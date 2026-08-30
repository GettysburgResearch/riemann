# L-108400 — Positive shared-fibre trace is Hellinger-stable under occupancy transport

Claim ID: `L-108400`  
Status: **PROVED EXACT FINITE OPERATOR THEOREM**  
Created: 2026-08-31  
Depends on: T-108100 on PR #776  
RH/GRH status: **not assumed**

Let \(\mathcal S\) be a finite declared residue-cell space and let

\[
0\le S\le I
\]

be the centered marked-place cell operator. Let \(d>0\) be its diagonal
subtraction and, for any nonnegative diagonal occupancy matrix \(D\), put

\[
Q(D)=D^{1/2}SD^{1/2}-dI_{\mathcal S}.
\tag{L-108400.1}
\]

Zero diagonal entries are allowed. They contribute the strictly negative
block \(-dI\) and hence no positive trace.

For two occupancies \(D,E\), define the Hellinger transport distance

\[
\mathfrak h(D,E)
=
\|D^{1/2}-E^{1/2}\|_{\mathcal S_2}.
\tag{L-108400.2}
\]

## 1. Positive-trace Lipschitz theorem

For Hermitian \(A,B\),

\[
|\operatorname{tr}A_+-\operatorname{tr}B_+|
\le\|A-B\|_{\mathcal S_1}.
\tag{L-108400.3}
\]

Indeed,

\[
\operatorname{tr}A_+
=
\max_{0\le P\le I}\operatorname{tr}(PA),
\]

and the variational formula gives (L-108400.3).

Now

\[
\begin{aligned}
Q(D)-Q(E)
={}&(D^{1/2}-E^{1/2})SD^{1/2}\\
&+E^{1/2}S(D^{1/2}-E^{1/2}).
\end{aligned}
\]

Schatten Hölder and \(\|S\|\le1\) therefore give

\[
\boxed{
\left|
\operatorname{tr}Q(D)_+
-
\operatorname{tr}Q(E)_+
\right|
\le
\bigl(\sqrt{\operatorname{tr}D}
+\sqrt{\operatorname{tr}E}\bigr)
\mathfrak h(D,E).
}
\tag{L-108400.4}
\]

This estimate has no atom-multiplicity or family-rank factor beyond the
literal occupancy mass.

## 2. Orbitwise partial-Frobenius comparator

Let a finite group \(\Gamma\) act on \(\mathcal S\) by cell permutations
commuting with \(S\). Define

\[
\bar D
=
{1\over|\Gamma|}
\sum_{\gamma\in\Gamma}P_\gamma DP_\gamma^*.
\tag{L-108400.5}
\]

Then \(\bar D\) is constant on every \(\Gamma\)-orbit and has the same total
mass as \(D\). Hence

\[
\boxed{
\operatorname{tr}Q(D)_+
\le
\operatorname{tr}Q(\bar D)_+
+
2\sqrt{\operatorname{tr}D}\,
\mathfrak h(D,\bar D).
}
\tag{L-108400.6}
\]

The defect vanishes exactly when occupancy is constant on every orbit. Thus
\(\mathfrak h(D,\bar D)\) is a quantitative relaxation of PR #776's exact
partial-Frobenius lift criterion.

## 3. Source order

The occupancy matrix must be formed **after** the source-authorized
same-arithmetic-tuple history recombination of PR #765. Internal ordered
histories already paid by that theorem may not be reintroduced as independent
occupancy variance. Distinct retained arithmetic groups and distinct retained
labels remain distinct.

## Scope

This theorem transports the conclusion-facing positive trace from a live
occupancy to a Frobenius-symmetric comparator. It does not prove that the
actual arithmetic occupancy has small Hellinger defect, control the resonant
rows, bind the principal member, or prove RH/GRH.
