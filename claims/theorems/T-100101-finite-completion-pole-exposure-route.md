# T-100101 — Route B: finite-completion pole exposure closes RH

Claim ID: `T-100101`  
Status: **UNCONDITIONAL INTEGRATOR / ONE UNIFORM POLE-EXPOSURE THEOREM OPEN**  
Created: 2026-08-20  
Depends on: `L-100101--L-100102`; PRs #676 and #677  
RH status: **unproved**

Let `C3` be PR #676's cubic critical scalar and put

\[
\mathcal C_{3;Z,k}=\mathscr A_{Z,k}\mathcal C_3.
\]

Unlike the compact SHARP kernel, the cubic kernel is positive for every
positive argument and decays linearly at zero.  Every finite completion shift
is therefore physically present at every endpoint; the full multiplier of
`L-100101` is the correct Mellin multiplier.

## 1. Unconditional corridor and fixed-cutoff sign changes

For every finite `Z,k`:

1. `mathcal C_(3;Z,k)` retains every off-line reciprocal-zeta pole because
   `mathcal A_(Z,k)` is zero-free in the open strip;
2. if RH is false, Landau forbids eventual nonnegativity of
   `mathcal C_(3;Z,k)`;
3. for every `A<A_k^*`, `L-100101` proves

   \[
   \mathcal C_{3;Z,k}(X)>0
   \qquad(1\le X\le Z^A)
   \]

   for sufficiently large `Z`.

Let

\[
N_{Z,k}=\inf\{X\ge1:\mathcal C_{3;Z,k}(X)<0\}.
\tag{T-100101.1}

Under failure of RH, `N_(Z,k)<infinity`, while

\[
N_{Z,k}>Z^A\qquad(A<A_k^*)
\tag{T-100101.2}

for all sufficiently large `Z`.

## 2. Exact remaining theorem

Define `QPET100101` by

\[
\boxed{
\exists k\ge2:\quad
\liminf_{Z\to\infty}
\frac{\log N_{Z,k}}{\log Z}<A_k^*.
}
\tag{QPET100101}

The statement is to be proved under the temporary assumption that the base
Mellin transform has a nonreal pole in the translated open strip.  It is a
quantitative sign-change-location theorem, not another positivity assumption.

If RH fails and `QPET100101` holds, choose `A` strictly between the liminf and
`A_k^*`.  Infinitely many cutoffs then satisfy `N_(Z,k)<=Z^A`, contradicting
the unconditional positive corridor.  Hence

\[
\boxed{
\mathrm{QPET100101}\Longrightarrow\mathrm{RH}.
}
\tag{T-100101.3}

## 3. Pole-exposure mechanism

`L-100102` proves that, at an off-line zero `rho=beta+i gamma`, the completed
pole residue is alternately amplified and suppressed like

\[
\exp\!\left(\pm c_\rho Z^{1-\beta}/\log Z\right).
\]

A sufficient analytic version of the open theorem is:

```text
UPE100101:
  on one amplified cutoff subsequence and one A<A_k^*, the exposed pole
  dominates all competing poles and the moving-cutoff contour remainder at a
  phase-matched point X in [Z,Z^A].
```

`UPE100101` implies `QPET100101`.  The remaining difficulty is uniform contour
dominance when `Z` and `X` grow together; multiplier cancellation and source
activation are already closed by choosing the cubic carrier.

```text
arbitrary finite completion                 PROVED EXACT
positive corridor to A_k^*                  PROVED
finite multiplier zero-free                 PROVED
residue amplification/suppression           PROVED ON CLASSICAL PNT
Landau sign-change existence for fixed Z    PROVED
uniform pole exposure QPET/UPE               OPEN / RH-BEARING
Riemann Hypothesis                           UNPROVED
```
