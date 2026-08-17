# L-97103 — The single-scalar derivative prefix is exactly the trace-free boundary defect of the Julia channel

Claim ID: `L-97103`  
Status: **PROVED EXACT REDUCTION**  
Created: 2026-08-17  
Depends on: PR #557; `L-97100`  
RH status: **unproved**

Define
\[
\mathcal B_\diamond(N)
=
\sum_{n\le N}\frac{b_\diamond(n)}{\sqrt n}.
\tag{L-97103.1}
\]
The scalar derivative prefix of PR #557 is
\[
M_*(N)=
\sum_{n\le N}\frac{a_*(n)}{\sqrt n}.
\]
By `a_*=6(delta_1-b_diamond)`,
\[
\boxed{M_*(N)=6[1-\mathcal B_\diamond(N)].}
\tag{L-97103.2}
\]
For integer knots,
\[
\boxed{
\mathcal R_{N+1}-\mathcal R_N
=M_*(N)\log(1+1/N).
}
\tag{L-97103.3}
\]

Consequently the exact trace-free extraction target is
\[
\boxed{
\mathrm{RJTE}:
\qquad
\mathcal B_\diamond(N)\le1
\quad\text{for every sufficiently large }N.
}
\tag{L-97103.4}
\]
If `RJTE` holds and `mathcal R_(N_0)>=0` at one starting knot beyond its threshold, then `mathcal R_X>=0` eventually. The zero-safe fixed-row Mellin--Landau theorem of PR #551 then implies RH.

The convolution inverse identity gives two useful exact audits:
\[
b_\diamond*g_\diamond=\delta_1,
\tag{L-97103.5}
\]
\[
\boxed{a_* * g_\diamond=6(g_\diamond-\delta_1)\ge0}
\tag{L-97103.6}
\]
coefficientwise. Equation (L-97103.6) proves that the scalar defect becomes positive after the correct positive reciprocal dilation. It does not license positivity-preserving deconvolution; treating it that way would simply assume `RJTE`.

Equivalently, with
\[
A(s)=6[1-B_\diamond(s+1/2)],
\]
`RJTE` is complete monotonicity of `A(s)/s` on the positive real axis. This is an exact analytic target, not a proof of it.
