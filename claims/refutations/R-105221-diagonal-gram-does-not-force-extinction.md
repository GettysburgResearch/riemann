# R-105221 — Diagonal or trace control of the exterior Gram cannot force residue extinction

Claim ID: `R-105221`  
Status: **PROVED EXACT METHOD FIREWALL**  
Created: 2026-08-23  
Depends on: `L-105225`  
RH status: **not assumed**

The centered cross term in `L-105225` cannot be discarded.

Take three unit weights. In the first Hilbert-space configuration let

\[
y_1=e_1,\qquad y_2=e_2,\qquad y_3=e_3.
\]

In the second let

\[
y_1=y_2=y_3=e_1.
\]

The two Gram matrices have identical diagonal entries and identical trace:

\[
\operatorname{diag}K=(1,1,1),
\qquad
\operatorname{tr}K=3.
\tag{R-105221.1}
\]

Nevertheless their weighted centered energies are respectively

\[
\boxed{3\operatorname{tr}K-\mathbf1^TK\mathbf1=6}
\tag{R-105221.2}
\]

and

\[
\boxed{3\operatorname{tr}K-\mathbf1^TK\mathbf1=0.}
\tag{R-105221.3}
\]

Equivalently, with

\[
L=I-\frac13\mathbf1\mathbf1^T,
\]

the centered Gram operators have norms \(1\) and \(0\).

Thus no estimate using only

```text
individual curvature-normalized sample norms;
the diagonal of K;
or the uncentered trace of K
```

can establish the subunit extinction threshold. A valid proof must retain the
same-source translation overlaps in

\[
\mathbf w^TK\mathbf w
\]

or an equivalent phase-sensitive centered operator. This firewall applies
equally to source-blind diagonal large-sieve and independent-sample
Cauchy--Schwarz closures.
