# L-99901 — Layer-cake decomposition confines unresolved cube mass to the activation collar

Claim ID: `L-99901`  
Status: **PROVED EXACT POSITIVE-MEASURE REDUCTION**  
Created: 2026-08-20  
Depends on: `L-99703`, `L-99900`  
RH status: **not assumed**

Let \(\phi\) be the normalized factor-67 logarithmic-box potential of PR #658.
It is nonnegative, increasing, zero at one, and admits the Stieltjes
representation

\[
\phi(y)=\int_{[1,y]}d\nu(t),
\qquad d\nu\ge0.
\tag{L-99901.1}
\]

Fix an outside source coefficient \(a\ge0\), a remaining quotient \(Y\ge1\),
and a labelled block \(B\). For \(S\subseteq B\), write

\[
p_S=\prod_{i\in S}p_i,
\qquad
r_S=\prod_{i\in S}r_i,
\qquad
P_B=\prod_{i\in B}p_i.
\]

The weighted source occurrence has mass

\[
a r_S\phi(Y/p_S)
=
\int_1^Y a r_S\mathbf1_{p_S\le Y/t}\,d\nu(t).
\tag{L-99901.2}
\]

For every layer

\[
t\le Y/P_B,
\]

all subsets are active. `L-99900` therefore supplies an exact Hasse flow on
that complete cube. Integrating those flows gives a source-faithful transport
on all complete layers.

Let \(\rho_{B,Y}\) denote the remaining unmatched negative mass when no claim
is made on partial layers. Then

\[
\boxed{
\rho_{B,Y}
\le
 a\Delta_B\phi(Y/P_B)
+
 a\prod_{i\in B}(1+r_i)
 [\phi(Y)-\phi(Y/P_B)].
}
\tag{L-99901.3}
\]

The first term is the exact complete-cube parity bias. The second is the
complete possible mass of the partial-activation collar.

For the actual factor-67 box, on \(y\ge67\),

\[
\phi(y)=8(1-67^{-1/2})-3\log67\,y^{-1/2}.
\]

Hence, whenever \(Y/P_B\ge67\),

\[
\boxed{
\phi(Y)-\phi(Y/P_B)
=
3\log67\,\frac{\sqrt{P_B}-1}{\sqrt Y}.
}
\tag{L-99901.4}
\]

Thus the activation collar is explicit and may be power-small. The parity-bias
term is separate and cannot be paid by the collar estimate.
