# T-97010 — All-depth scalar Hall is the surviving factor-67 producer

Claim ID: `T-97010`  
Status: **UNCONDITIONAL REDUCTION; PRODUCER OPEN**  
Base: PR #561  
Uses: PR #559 scalar Mellin identity; `L-97010`; `R-97010`  
RH status: **unproved**

Define

\[
\mathcal R_X=5c_X(2)+3c_X(3).
\]

The exact fixed-row formulas give, with `z=s+1/2`,

\[
\int_1^\infty \mathcal R_X X^{-s-1}\,dX
=
\frac6{s^2}
-
\frac{3(1-2^{-z})(2-2^{-z})}{s^2\zeta(z)}.
\tag{T-97010.1}
\]

Indeed, if `x=2^{-z}` and `y=3^{-z}`, the row numerators satisfy

\[
P_2(z)=2x-1-y,
\qquad
3P_3(z)=5y-x-1-3x^2,
\]

so

\[
5P_2(z)+3P_3(z)
=-3(x-1)(x-2)
=-3(1-x)(2-x).
\tag{T-97010.2}
\]

For `Re z>0`, `|x|<1`; hence the numerator in (T-97010.1) is nonzero.

Let `ASHP67` denote the following single producer statement.

> **All-depth scalar Hall producer (`ASHP67`).** For every `X>=1`, expand the
> complete parity-labelled native source through the exact least-owner
> factor-67 recursion without imposing a fixed depth. Combine all finite
> `P_61` colors before observation and combine all rough histories before the
> scalar observation. The resulting common-source scalar packing is positive
> and equals `mathcal R_X`.

Then

\[
\boxed{\mathrm{ASHP67}\Longrightarrow \mathcal R_X\ge0\ (X\ge1)
\Longrightarrow \mathrm{RH}.}
\tag{T-97010.3}
\]

The second implication is the exact scalar Mellin–Landau consumer: a zeta zero
with `Re z>1/2` would create a non-real-abscissa singularity of the Mellin
transform of a nonnegative function, while (T-97010.2) prevents numerator
cancellation; functional-equation symmetry then gives RH.

## Exact route disposition

The reduction is unconditional, but `ASHP67` is open. It is strictly narrower
than PR #561's two-row `GPHT23` because only one scalar target is required, and
strictly stronger than PR #559's published leafwise proposal because it retains
all accumulated parity and forbids observation at any fixed rough depth.

Any claimed successor must therefore provide one of:

1. an exact finite representation of the all-depth scalar sum with preserved
   source ownership;
2. a convergent projective/Abel limit with a justified interchange of grouping,
   observation, and limit;
3. a finite dual certificate proving the full all-depth scalar cone feasible.

A leafwise, colorwise, or bounded-depth certificate is excluded by `R-97010`.
