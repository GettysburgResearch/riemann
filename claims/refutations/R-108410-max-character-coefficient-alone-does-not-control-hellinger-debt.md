# R-108410 — A small maximum character coefficient does not control Hellinger debt without spectral summation

Claim ID: `R-108410`  
Status: **PROVED EXACT FINITE COUNTERMODEL FAMILY**  
Created: 2026-08-31

Let

\[
X=(\mathbf Z/2\mathbf Z)^{2d},
\qquad
m=|X|=2^{2d},
\]

and define the quadratic bent sign

\[
s(x)=(-1)^{x_1x_2+\cdots+x_{2d-1}x_{2d}}.
\]

Every Walsh coefficient of `s` has absolute value

\[
\sqrt m.
\]

Moreover

\[
\sum_xs(x)=\sqrt m.
\]

Define the nonnegative occupancy

\[
n(x)=1+s(x)\in\{0,2\}.
\]

Its total mass is

\[
N=m+\sqrt m.
\]

For every nontrivial character,

\[
{ |\widehat n(\chi)|\over N}
={\sqrt m\over m+\sqrt m}
={1\over\sqrt m+1}
\longrightarrow0.
\tag{R-108410.1}
\]

Nevertheless the normalized Hellinger debt from the uniform occupancy tends
to a positive constant:

\[
\boxed{
{H_X(n)^2\over N}
\longrightarrow
2-\sqrt2.
}
\tag{R-108410.2}
\]

Indeed, asymptotically half the cells have occupancy zero and half occupancy
two, while the uniform mean tends to one.

Thus a rank-free bound for the **largest** nonprincipal Fourier coefficient
cannot by itself prove `FROBHELL108400`; one must retain the complete spectral
energy, a source `L^2` normalization, or another theorem preventing many small
modes from accumulating.

This does not contradict PR #771. Its complete deep theorem includes its own
normalized source and operator ledger. The firewall forbids exporting only the
max-coefficient statement into a live incomplete occupancy argument.
