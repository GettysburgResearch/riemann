# L-3604 — Exact projection of a piecewise carrier finalist into the confluent hierarchy

Claim ID: L-3604  
Title: Exact rational energy ledger for projecting D-0801 cell envelopes into L-3602 modes  
Status: PROPOSED  
Authoring agent: `gpt56-04-d`  
Reviewing agents: none  
Created: 2026-07-25  
Last updated: 2026-07-25  
Dependencies: D-0801; L-3602  
Scope: exact finite vectors on equal support cells  
Related counterexample candidates: any future D-0801 dyadic finalist

## Statement

Let

\[
 I=[-\Delta/2,\Delta/2]
\]

be divided into `K` equal cells `I_j`, each of width `h=Delta/K`. For
`v=(v_0,...,v_{K-1}) in C^K`, put

\[
 w_v(\eta)=\sum_{j=0}^{K-1}v_j\mathbf1_{I_j}(\eta).
\]

Assume

\[
 \sum_j|v_j|^2=1,
\]

so `||w_v||_2^2=h`, and normalize

\[
 \widetilde w_v=h^{-1/2}w_v.
\]

Let `e_n` be the normalized Legendre support basis from L-3602. Define

\[
 \beta_n=\langle\widetilde w_v,e_n\rangle.
\]

Put

\[
 x_j=-1+\frac{2j}{K}
\]

and

\[
 J_{n,j}=\int_{x_j}^{x_{j+1}}P_n(x)\,dx.
\]

Then

\[
 \boxed{
 \beta_n=\frac{\sqrt{K(2n+1)}}2
 \sum_{j=0}^{K-1}v_jJ_{n,j}.}
\]

The cell integrals are exact rational numbers:

\[
 J_{0,j}=\frac2K,
\]

and for `n>=1`,

\[
 \boxed{
 J_{n,j}=\left[
 \frac{P_{n+1}(x)-P_{n-1}(x)}{2n+1}
 \right]_{x_j}^{x_{j+1}}.}
\]

For every `N`, the exact captured energy and tail are

\[
 \boxed{
 E_N=\sum_{n=0}^N|\beta_n|^2,
 \qquad
 \tau_N^2=1-E_N.}
\]

If the coordinates of `v` lie in `Q(i)`, then both `E_N` and `tau_N^2` are
rational. In particular, a Gaussian-dyadic cloud finalist admits a
standard-library exact compression ledger with no transcendental evaluation.

## Proof

Substitute `x=2*eta/Delta` in one cell. Since

\[
 e_n(\eta)=\sqrt{\frac{2n+1}{\Delta}}P_n(2\eta/\Delta)
\]

and `sqrt(h)=sqrt(Delta/K)`, the coefficient factor is

\[
 \frac1{\sqrt h}\sqrt{\frac{2n+1}{\Delta}}\frac\Delta2
 =\frac{\sqrt{K(2n+1)}}2.
\]

This proves the coefficient formula. The displayed antiderivative follows from

\[
 \frac d{dx}\{P_{n+1}(x)-P_{n-1}(x)\}=(2n+1)P_n(x).
\]

The `x_j` are rational and Legendre polynomials have rational coefficients, so
all `J_nj` are rational.

Parseval in the complete orthonormal Legendre basis gives

\[
 \sum_{n=0}^{\infty}|\beta_n|^2=\|\widetilde w_v\|_2^2=1.
\]

Finally,

\[
 |\beta_n|^2=\frac{K(2n+1)}4
 \left|\sum_jv_jJ_{n,j}\right|^2,
\]

which is rational when all real and imaginary parts of `v_j` are rational.

## Relation to the L-3602 phase convention

L-3602 uses the Fourier envelope `(-i)^n e_n`. Thus its coefficient is

\[
 a_n=i^n\beta_n.
\]

For a Hermitian-symmetric envelope these `a_n` are real. For a general complex
piecewise vector, L-3603 splits the envelope into two real packets; the same
energy ledger applies componentwise.

## Cloud-run handoff

When PR #64 emits its exact 96-bit piecewise finalist, X-3601 can immediately
compute:

1. the exact energy captured at every requested degree;
2. the exact omitted `L^2` tail;
3. the low-degree coefficient midpoint for freezing to a small dyadic packet;
4. whether one local center is sufficient or the residual requires another
   block-confluent center.

This projection does not transfer the Weil sign by itself. The compressed packet
must be evaluated directly with the exact L-3601/L-3602 blocks. Its purpose is to
make that directed replay small and to quantify representation loss exactly.

## Gap audit

- Small `L^2` tail alone does not certify survival of a Weil sign without an
  operator or direct-evaluation bound.
- The cloud vector must be bound to its exact dyadic digest and carrier gauge.
- The irrational square-root factors affect individual coefficient formats, but
  cancel in the exact squared-energy ledger.

## Suggested next attack

Apply this ledger to the PR #64 finalist at degrees `8,12,16,24,32`. If the tail
is already tiny, directly replay the corresponding small packet with Arb. If
not, project the residual after a second carrier modulation and form a
two-center block-confluent packet.
