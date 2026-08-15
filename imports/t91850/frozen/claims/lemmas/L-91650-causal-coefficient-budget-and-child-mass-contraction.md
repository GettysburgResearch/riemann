# L-91650 — Exact causal coefficient budget

Claim ID: `L-91650`  
Status: **PROVED EXACT ALGEBRAIC THEOREM**  
Created: 2026-08-13  
Depends on: `L-91355`  
RH status: **unproved**

Let `67<=p_1<...<p_k`, put `r_i=p_i^(-1/2)`, and define

\[
s_0=1,
\quad s_i=\prod_{h\le i}(1-r_h),
\quad \lambda_i=r_i s_{i-1},
\quad \alpha_i=r_i\lambda_i.
\]

Then

\[
\boxed{s_k+\sum_i\lambda_i=1}.
\]

For a packet family with child placement `A_(p_i)`, define

\[
C_i(P_X)=P_X-r_iA_{p_i}P_{X/p_i}.
\]

Linearity gives the exact realized identity

\[
\boxed{
P_X=s_kP_X+\sum_i\lambda_iC_i(P_X)
       +\sum_i\alpha_iA_{p_i}P_{X/p_i}.
}
\]

The child terms cancel because `-lambda_i r_i+alpha_i=0`; the parent
coefficient is one.

Moreover

\[
\boxed{
\sum_i\alpha_i
\le r_1\sum_i\lambda_i
<67^{-1/2}<1/8.
}
\]

Every child endpoint is at most `X/67`. Tail-prime provenance is advanced with
the child, so no excluded prime is reintroduced.

The equality is an identity after the realization map defined in `L-91652`; it
is not an equality of free certificate coefficient vectors.