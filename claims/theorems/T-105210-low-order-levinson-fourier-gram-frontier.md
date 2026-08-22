# T-105210 — Low-order Levinson descent through one quotient and one Fourier-compound localization gate

Claim ID: `T-105210`  
Status: **MAJOR UNCONDITIONAL LOW-ORDER STRUCTURE; RH UNPROVED**  
Created: 2026-08-23  
Depends on: `R-105201`, `L-105206--L-105208`; PR #720 `L-104518--L-104521`  
RH status: **unproved**

## 1. The previous cumulative budget is not the producer

`R-105201` proves exactly that the `CRDB105200` upper ledger is

\[
\mathcal D_r
=O_0+2\sum_{j<r}
\left[R_j(1-\mathfrak C_j)-E_j\right].
\tag{T-105210.1}
\]

It is the unknown off-real zero count plus nonnegative slack.  The natural
high-derivative entry removes `O_r`, but it does not estimate the fixed
low-order horizontal argument or the last wrong extremum.  Accordingly,
`CRDB105200` is retained only as a correct sufficient ledger and is removed as
the principal research producer of this branch.

## 2. All derivative-level boundary terms collapse to one quotient

Fix one `lambda>0` across a finite ladder and put

\[
G_{k,\lambda}
=\xi^{(k)}+\lambda\xi^{(k+1)}.
\]

`L-105206` proves

\[
\boxed{
\sum_{k<r}
\Delta_{\infty\to1/2}
\arg {G_{k,\lambda}\over G_{k+1,\lambda}}
=
\Delta_{\infty\to1/2}
\arg {G_{0,\lambda}\over G_{r,\lambda}}.
}
\tag{T-105210.2}
\]

The top-boundary logarithmic derivatives telescope in the same way.  Thus the
actual Levinson boundary difficulty is one continued endpoint quotient, not a
sum of `O(T^2 log T)` unrelated argument estimates.

At a natural high terminal order, the source-determined choice

\[
\lambda_r=M_r/M_{r+1}\sim1/w_r
\]

makes the denominator asymptotically explicit on bounded parts of the safe
path by the proposed Gaussian theorem.  The numerator is the classical
Levinson auxiliary

\[
\xi+\lambda_r\xi'.
\]

This is precisely where the fixed low-order difficulty resides.

## 3. New unconditional low-order input

For every derivative order, define

\[
\Lambda_k(t)
=\Xi^{(k+1)}(t)^2
 -\Xi^{(k)}(t)\Xi^{(k+2)}(t).
\]

`L-105207` proves the all-order exterior-square Gram theorem

\[
\boxed{
\left[
\Lambda_{a_i+a_j}(t_j-t_i)
\right]_{i,j}\succeq0
}
\tag{T-105210.3}
\]

for arbitrary derivative indices and real translations.  It follows that:

```text
all even defects are positive-definite functions;
all autocorrelation-windowed derivative Hankel matrices are PSD;
every odd Fourier defect is Schur-dominated by its adjacent even defects;
every even derivative has an explicit central no-wrong-extremum interval.
```

`L-105208` proves, for the actual companion

\[
E_{k,\lambda}=\Xi^{(k)}-i\lambda\Xi^{(k+1)},
\]

the exact low-order mean orientation

\[
\boxed{
\|E_{k,\lambda}(\cdot-iy)\|_2^2
>
\|E_{k,\lambda}^{\#}(\cdot-iy)\|_2^2
\qquad(y>0),
}
\tag{T-105210.4}
\]

and the real-axis phase sum rule

\[
\boxed{
\int |E_{k,\lambda}|^2\theta_{k,\lambda}'
=2\lambda\int |\Xi^{(k+1)}|^2>0.
}
\tag{T-105210.5}
\]

These are unconditional statements at `k=0` and at every fixed low order.
They prove that the source orientation is correct before height localization.

## 4. The actual remaining theorem

The unresolved implication is now sharply separated from the high-tail work.
Define `HLOC105210` to be a height-localization theorem with the following
content:

```text
for the last defective low derivative level and the source-fixed companion,
the exterior-square Fourier Gram and mean Hermite-Biehler dominance control
the continued horizontal argument at that same ordinate strongly enough to
exclude an inward unit of companion index.
```

Equivalently, in the telescoped formulation, it must control the continued
argument of

\[
{\xi+\lambda_r\xi'
 \over
 \xi^{(r)}+\lambda_r\xi^{(r+1)}}
\]

on the same regular height, with the top endpoint phases retained.

Then the exact last-defect theorem of `L-104518--L-104521` gives

\[
\boxed{
\text{no positive-residue last event}
\quad\wedge\quad
\mathrm{HLOC105210}
\Longrightarrow\mathrm{RH}.
}
\tag{T-105210.6}
\]

Neither input is claimed proved globally.  The advance is that the low-order
source already has a complete positive compound Gram and a strict mean
orientation.  What remains is specifically the conversion from this
translation-invariant/averaged positivity to one fixed-height Levinson
argument.

## 5. Exact boundary

```text
CRDB as an independent low-order producer        REFUTED
all derivative boundary arguments -> one quotient PROVED EXACT
all-order Xi exterior-square Fourier Gram         PROVED UNCONDITIONALLY
mean low-order Hermite-Biehler orientation         PROVED UNCONDITIONALLY
central even-level no-wrong-extremum regions       PROVED UNCONDITIONALLY
height-local fixed-ordinate argument control       OPEN / RH-BEARING
last positive-residue exclusion                    OPEN / RH-BEARING
Riemann Hypothesis                                 UNPROVED
```
