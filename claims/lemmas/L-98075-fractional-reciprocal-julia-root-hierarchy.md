# L-98075 — Fractional reciprocal-Julia roots give a positive hierarchy

Claim ID: `L-98075`  
Status: **PROVED COEFFICIENTWISE POSITIVITY; EXTRACTION STILL OPEN**  
RH status: **unproved**

Let
\[
G_\diamond(z)=
\frac{\zeta(z)}{(1-2^{-z})(1-2^{-z-1})},
\qquad B_\diamond=G_\diamond^{-1}.
\]
For `tau>0` define
\[
P_\tau=G_\diamond^\tau,\qquad Q_\tau=G_\diamond^{-\tau}.
\]

Prime-by-prime binomial coefficients satisfy coefficient majorization
\[
p_\tau(n)\ge|q_\tau(n)|.
\]
Hence `P_tau +/- Q_tau` have nonnegative Dirichlet coefficients and define
positive two-channel Julia matrices.

For `tau=1/k`,
\[
Q_{1/k}^{*k}=B_\diamond,
\]
so the native scalar defect has an exact `k`-step positive fractional-root
state realization.

This does not close the trace-free extraction: every nonzero positive channel
containing `G_\diamond^\tau` retains the real zeta pole at `z=1`.
