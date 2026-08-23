# R-104516 — Diagonal orbitwise Turán positivity does not close the mixed source

Claim ID: `R-104516`  
Status: **EXACT OPERATOR-CLASS REFUTATION**  
Created: 2026-08-23  
RH status: **not assumed**

The mixed matrix in `L-104532` cannot be replaced by positivity of its diagonal entries.

Take

\[
F_1(t)=\cos t,
\qquad
F_2(t)={1\over2}\cos 2t.
\]

Each separate frequency has strictly positive first Laguerre expression:

\[
(F_1')^2-F_1F_1''=1,
\]

\[
(F_2')^2-F_2F_2''=1.
\]

But for

\[
F=F_1+F_2
\]

one has at `t=pi`

\[
F(\pi)=-{1\over2},
\qquad
F'(\pi)=0,
\qquad
F''(\pi)=-1,
\]

and hence

\[
\boxed{
F'(\pi)^2-F(\pi)F''(\pi)=-{1\over2}<0.
}
\tag{R-104516.1}
\]

Both components are Fourier transforms of positive even discrete measures with no zero-frequency atom.  Thus the failure is not caused by a signed source or by a constant background.  It is entirely an independent-frequency cross term.

Consequences:

```text
entrywise diagonal Turán positivity       INSUFFICIENT
sum of individual orbit energies          INSUFFICIENT
scalar trace positivity                   INSUFFICIENT
absolute-value control of cross terms      GENERALLY POWER-LOSSY
common mixed-orbit Gram / Schur control     REQUIRED
```

The example does not refute `KPD104550` for the actual Riemann theta source.  It makes `MTSG104560` or an equivalent common-source row-sum theorem binding.