# R-108430 — Unweighted occupancy fluctuation is not the native positive source debt

Claim ID: `R-108430`  
Status: **PROVED EXACT SOURCE-BLINDNESS FIREWALL**  
Created: 2026-08-31  
Depends on: `L-108430`  
RH/GRH status: **not assumed**

Let the physical cell space contain `m>=2` cells. Put all `2r` literal atoms
in one cell and give them coefficients

\[
(1,-1,1,-1,\ldots,1,-1).
\]

Then

\[
Rz=0,
\qquad
\boxed{\langle z,(B_R)_+z\rangle=0.}
\tag{R-108430.1}
\]

Nevertheless the unweighted occupancy is

\[
n=(2r,0,\ldots,0).
\]

Against the uniform occupancy of the same mass, its squared Hellinger debt is

\[
\boxed{
H^2(n,\bar n)
=4r\left(1-{1\over\sqrt m}\right),
}
\tag{R-108430.2}
\]

which is a positive fixed proportion of the total occupancy and tends to the
maximal normalized value as `m` grows.

Thus neither unweighted Hellinger fluctuation nor its complete nonprincipal
Fourier variance is a necessary lower proxy for the positive charge of the
literal native coefficient vector.

The conclusion is not that `FROBMIX108420` is false: it remains a valid
uniform sufficient theorem. The conclusion is that it is source-blind and
can overpay arbitrarily. A proof programme for the one native source should
first estimate the assembled coefficient-cell energy of `L-108430`, retaining
all cancellations before taking a norm.

This firewall is directly relevant to the live fixed-conductor rectangles on
PR #770: support and multiplicity growth alone do not determine the weighted
source contribution.
