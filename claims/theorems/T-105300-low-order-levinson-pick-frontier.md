# T-105300 — Low-order Levinson–Pick record frontier

Claim ID: `T-105300`
Status: **UNCONDITIONAL FINITE ALGEBRA; XI WINDOW ESTIMATE OPEN**
Created: 2026-08-23
Depends on: `L-105300`, `L-105301`, `L-105302`, `L-105303`, `R-105300`
RH status: unproved

## 1. What is now closed

For every finite real monic squarefree polynomial with squarefree derivative,
there is a coefficient-computable symmetric matrix

\[
H_{p,w}=\langle1\rangle\oplus
\left[
\operatorname{Tr}_{\mathbb R[x]/(p')}
\bigl(-p(p'')^{-1}w^2x^{i+j}\bigr)
\right]_{0\le i,j<n-1}
\]

for every polynomial `w` coprime to `p'`. Its signature is exactly the number
of real roots of `p`, and its negative index is exactly half the number of
nonreal roots.

The same inertia localizes directly to a regular entire-function rectangle by `L-105303`. Thus the actual one-step Levinson descent is no longer represented only by a lossy scalar coherence or by separately estimated nonreal/debt corrections. It is one exact endpoint-aware Hermite inertia problem.

## 2. Rank--trace and resolvent gates

Define

\[
\Theta(p,w)
=\frac{(\operatorname{tr}H_{p,w})_+^2}
{n\operatorname{tr}(H_{p,w}^2)}.
\]

Then

\[
\frac{N_\mathbb R(p)}n\ge2\Theta(p,w)-1.
\]

The complete sign-resolvent identity is

\[
N_\mathbb R(p)
=\frac2\pi\int_0^\infty
\operatorname{tr}\bigl(H_{p,w}(H_{p,w}^2+t^2I)^{-1}\bigr)\,dt.
\]

The rank--trace statistic is the first two-moment certificate; rational
minorants to the sign function give a strict hierarchy beyond that ceiling.

## 3. Two explicit record-breaking gates

### Direct Hermite--Pick gate `LHRT105300`

Use the exact Xi-window contour compression `C_T` from `L-105303`, with a sign-blind source-owned test family, and prove

\[
\boxed{
\liminf_{T\to\infty}
\frac{(\operatorname{tr}C_T)_+^2}
{N_{\Xi'}(T,2T)\operatorname{tr}(C_T^2)}
>0.83625.
}
\]

After controlling multiplicities, common zeros, and the explicit endpoint ledger, this gives a line-zero
proportion strictly greater than `0.67250`.

### Xi-prime transfer gate `LEXI105301`

Use the unconditional quartic-window Xi-prime proportion `0.86864` and prove
that more than `77057/86864` of all real Xi-prime critical points are
Rolle-generating. The clean stronger target `9/10` yields the explicit bound

\[
0.694912.
\]

The trace form is preferred because it counts signs exactly and treats every
nonreal critical pair as one positive and one negative square.

## 4. Analytic programme on the persistent PR

The next passes on this PR should attack, in order:

1. identify an Anthropic-compatible source-owned analytic compression of the exact Xi window trace form;
2. compute its trace and Hilbert--Schmidt norm on a safe horizontal line;
3. optimize a low-degree source-owned preconditioner inside the frozen quartic taper family;
4. if the first-two-moment ratio stalls below `0.83625`, a rational
   sign-resolvent minorant using the third and fourth critical-residue trace
   moments;
5. endpoint and winding terms on the same matrix ledger.

## 5. Boundary

```text
finite Levinson--Hermite trace form          PROVED EXACT
entire-window trace form and compression      PROVED EXACT
wrong-extremum/nonreal-pair inertia          PROVED EXACT
coefficient-computable quotient matrix       PROVED EXACT
polynomial preconditioning                   PROVED EXACT
rank--trace real-root certificate            PROVED EXACT
sign-resolvent hierarchy                     PROVED EXACT
Anthropic 0.86864 -> 0.694912 bridge          PROVED CONDITIONAL
LHRT105300                                    OPEN / RECORD-BEARING
LEXI105301                                    OPEN / RECORD-BEARING
Riemann Hypothesis                            UNPROVED
```
