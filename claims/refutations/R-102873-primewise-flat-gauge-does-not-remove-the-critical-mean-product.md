# R-102873 — Primewise flat gauges do not remove the critical mean product

Claim ID: `R-102873`  
Status: **PROVED EXACT SCOPE FIREWALL**  
Created: 2026-08-25  
Depends on: `L-102901--L-102904`; `R-102872`  
RH status: **not assumed**

Primewise complementary temperatures and endpoint colors provide exact source
factorizations of the fixed midpoint product. They do not change that product.

## 1. The native first-chaos sum is invariant

At every labelled prime the two complementary first-chaos coefficients are

\[
-(1-t_p),\qquad -t_p.
\]

Their sum is always

\[
\boxed{-1.}
\]

No primewise temperature vector can delete the native critical carrier. It can
only decide which factor carries what fraction of it.

## 2. The midpoint is already the energy optimum

`L-102902` proves

\[
|1-t_p|^2+|t_p|^2
=\frac12+2|t_p-1/2|^2.
\]

Thus moving temperatures away from the midpoint cannot improve the free local
energy. Sparse endpoint moves are useful for exact owner placement, not for a
source-blind contraction.

## 3. Endpoint-color averaging leaves one critical mean

The exact Walsh identity of `L-102904` moves every nonempty color variance into
squared activity, but leaves

\[
\bigotimes_p M_p\otimes M_p
\]

as the sole critical mean coordinate. That coordinate is the arithmetic
midpoint square and is related to the geometric midpoint square by a
subcritical signed gauge. Its fixed outer observation remains conclusion-
bearing.

## 4. Physical sign remains nonfunctorial

Even when each factor observation is positive, their arithmetic convolution
observation can be negative, as shown by `R-102872`. The same counterfixture
applies after primewise gauge selection.

Therefore none of the following implications is valid:

```text
primewise flatness -> midpoint product positivity;
endpoint owner uniqueness -> physical negative-mass bound;
Walsh variance is squared -> arithmetic midpoint square is positive;
free energy minimization -> RH.
```

A valid closure still requires a source-faithful physical orientation theorem
for the remaining midpoint core. The gauge results merely remove owner,
assignment, and color-variance ambiguities from that theorem.
