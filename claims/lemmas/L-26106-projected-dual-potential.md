# L-26106 — Monotone projected-dual potential for annular carry transport

Claim ID: `L-26106`  
Title: Projected ascent on the annular Hilbert–Farkas dual is a globally monotone recursive flow producer  
Status: **PROPOSED COMPLETE FINITE CONVEX-ANALYTIC LEMMA**  
Authoring agent: `gpt56-pro-22`  
Created: 2026-08-08  
Issue: #261  
Depends on: `L-26105`  
Scope: exact recursive invariant; no arithmetic estimate and no RH claim

## 1. Dual energy

Let

\[
 K_X=A_XA_X^*
\]

and define, on the nonnegative prime-power cone,

\[
\boxed{
 \mathscr D_X(\lambda)
 =\langle\lambda,r_X\rangle
 -\frac12\langle\lambda,K_X\lambda\rangle
 =\langle\lambda,r_X\rangle
 -\frac12\|A_X^*\lambda\|_2^2.
}
\tag{L-26106.1}

By `L-26105`,

\[
 \sup_{\lambda\ge0}\mathscr D_X(\lambda)
 =\frac12\mathcal R_X^2.
 \tag{L-26106.2}

The gradient is

\[
 \nabla\mathscr D_X(\lambda)
 =r_X-K_X\lambda.
 \tag{L-26106.3}

This is exactly the current prime-power constraint residual of the primal flow

\[
 F=A_X^*\lambda.
 \tag{L-26106.4}

## 2. Projected ascent

Let

\[
 L_X=\|K_X\|_{2\to2}
\]

and choose

\[
 0<\tau_X\le L_X^{-1}.
 \tag{L-26106.5}

Starting from `lambda^(0)=0`, define

\[
\boxed{
 \lambda^{(n+1)}
 =\left[
  \lambda^{(n)}
  +\tau_X\bigl(r_X-K_X\lambda^{(n)}\bigr)
 \right]_+,
}
\tag{L-26106.6}

where the positive part is taken coordinatewise. The associated primal flow is

\[
 F^{(n)}=A_X^*\lambda^{(n)}.
 \tag{L-26106.7}

Thus every iterate is an exact divisor-rich annular flow. Its coordinate formula is

\[
 F^{(n)}_j
 =2\sum_{q\mid j}\lambda^{(n)}_q
 -\sum_{q\mid j-1}\lambda^{(n)}_q
 -\sum_{q\mid j+1}\lambda^{(n)}_q.
 \tag{L-26106.8}

## 3. Exact monotone potential

Put

\[
 \Delta_n=\lambda^{(n+1)}-\lambda^{(n)}.
\]

The defining property of Euclidean projection onto the nonnegative cone gives

\[
 \left\langle
  \nabla\mathscr D_X(\lambda^{(n)}),
  \Delta_n
 \rightangle
 \ge\frac1{\tau_X}\|\Delta_n\|_2^2.
 \tag{L-26106.9}

Since `mathscr D_X` is a concave quadratic,

\[
\begin{aligned}
 \mathscr D_X(\lambda^{(n+1)})
 -\mathscr D_X(\lambda^{(n)})
 &=\left\langle
   \nabla\mathscr D_X(\lambda^{(n)}),
   \Delta_n
  \rightangle
  -\frac12\langle\Delta_n,K_X\Delta_n\rangle\\
 &\ge
 \left(\frac1{\tau_X}-\frac{L_X}{2}\right)
 \|\Delta_n\|_2^2\\
 &\ge\frac1{2\tau_X}\|\Delta_n\|_2^2.
\end{aligned}
 \tag{L-26106.10}

Therefore

\[
\boxed{
 \mathscr D_X(\lambda^{(n+1)})
 \ge\mathscr D_X(\lambda^{(n)}),
}
\tag{L-26106.11}

with strict increase unless the iterate is stationary.

The dual deficit

\[
 \mathscr P_n
 =\frac12\mathcal R_X^2
 -\mathscr D_X(\lambda^{(n)})
 \tag{L-26106.12}

is the desired recursive Lyapunov potential. It decreases monotonically to zero whenever the annular repair is feasible.

## 4. Stationary points and feasibility

The fixed-point condition for (L-26106.6) is

\[
 \lambda\ge0,
 \qquad
 r_X-K_X\lambda\le0,
 \qquad
 \lambda_q(r_X-K_X\lambda)_q=0.
 \tag{L-26106.13}

With

\[
 F=A_X^*\lambda,
\]

these are precisely the KKT conditions

\[
 A_XF\ge r_X,
 \qquad
 \lambda\ge0,
 \qquad
 \lambda_q((A_XF)_q-r_X(q))=0
 \tag{L-26106.14}

for the minimum-norm primal repair.

Standard finite-dimensional projected-gradient convergence for a smooth concave quadratic implies convergence of the dual objective to (L-26106.2); the unique primal minimum-norm flow is recovered in the image `A_X^*lambda`.

If the primal system is infeasible, Farkas supplies a positive null direction and the dual energy is unbounded above.

## 5. Correction to the half-step leakage heuristic

The active-set half-step of `L-26103` reduces the currently active residual coordinates exactly, but newly activated rows can make the total positive-residual norm increase temporarily. Floating source runs exhibit such steps.

Therefore the former assertion

\[
 \|(r^{(n+1)})_+\|_2
 \le\rho\|(r^{(n)})_+\|_2
 \quad\text{at every half-step}
\]

is withdrawn as an intended invariant.

The correct globally monotone quantity is the dual energy (L-26106.1). The active-set construction remains useful as a fast finite producer, but it is not load bearing in the proof architecture.

## 6. What remains arithmetic

The iteration always solves the finite convex program in the limit. What is not automatic is the required bound

\[
 \mathcal R_X=X^{o(1)}.
\]

By `L-26105`, that bound is exactly the Annular Dual Frame inequality `ADF`.

Thus the proof obligations are cleanly separated:

```text
recursive construction and monotone potential    closed here;
subpower size of the optimum                     ADF / open;
annular transfer to the prime ramp               L-26102 / closed;
RH composition                                   conditional.
```

## 7. Proof boundary

Exact in this file:

- the projected-dual iteration;
- the divisor-rich primal formula;
- monotonicity and quantitative increase of the dual energy;
- KKT characterization;
- correction of the overstrong per-step positive-residual invariant.

Open:

- `ADF`;
- the subpower annular flow bound;
- RH.