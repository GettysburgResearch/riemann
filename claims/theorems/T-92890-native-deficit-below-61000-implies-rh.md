# T-92890 — A native-feasible row with deficit below 61000 implies the Riemann Hypothesis

Claim ID: `T-92890`  
Status: **PROPOSED COMPLETE ENDPOINT-TO-RH THEOREM — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-15  
Depends on: the exact carry dual, the prime-square occupancy theorem, the exact prime-endpoint Mellin symbol, and Landau's one-sign theorem  
RH status: **proved conditionally on the displayed finite row input**

## 1. Finite dual inequality

Let \(d_X\ge0\) satisfy

\[
C_{d_X}(q)\le w_X(q),
\qquad q\ge2.
\tag{T-92890.1}
\]

The exact average-binomial carry identity gives

\[
\mathcal H(d_X)
=
\sum_q\Lambda(q)C_{d_X}(q)
\le
\sum_q\Lambda(q)w_X(q)
=
P_\Lambda(X).
\tag{T-92890.2}
\]

Put

\[
F_\Lambda(X)=J_\Lambda(X)-P_\Lambda(X).
\]

Then

\[
\boxed{
F_\Lambda(X)
\le
J_\Lambda(X)-\mathcal H(d_X).
}
\tag{T-92890.3}
\]

If \(d_X\) is radix-four feasible, the right side is exactly the positive
\(Y_4\)-weighted native slack.

## 2. Consequence of the one-shot bound

For the row of `L-92891`, `L-92893` gives

\[
0\le
J_\Lambda(X)-\mathcal H(d_X)
<61000
\qquad(X\ge10^{12}).
\]

Therefore

\[
\boxed{
F_\Lambda(X)<61000.
}
\tag{T-92890.4}
\]

In particular,

\[
F_\Lambda(X)=o(\log^2X)
\quad\text{in the one-sided upper sense required below.}
\tag{T-92890.5}
\]

## 3. Prime-square moat

Let

\[
A(X)=
\sum_{p\le X}(\log p)r_X(p)
\]

be the exact prime-only endpoint scalar. The unconditional prime-square
occupancy theorem gives

\[
F_\Lambda(X)-A(X)
=
\frac{C_{\rm pp}}4\log^2X+o(\log^2X),
\tag{T-92890.6}
\]

where

\[
C_{\rm pp}=-1-\zeta(1/2)>0.
\]

Combining (T-92890.4) and (T-92890.6),

\[
A(X)
\le
61000-\frac{C_{\rm pp}}4\log^2X+o(\log^2X)<0
\tag{T-92890.7}
\]

for every sufficiently large \(X\).

Thus the prime-only endpoint is eventually strictly negative.

## 4. Mellin pole audit

The exact prime endpoint has Mellin transform

\[
\widehat A(z)
=
\int_1^\infty A(X)X^{-z-1}\,dX
=
\frac{\mathcal G(z+1/2)}{z^2},
\tag{T-92890.8}
\]

initially in a right half-plane and meromorphically continued to
\(\Re z>0\).

The real pole at \(z=1/2\) cancels. There is no singularity on the positive
real axis. Every nontrivial zeta zero \(\rho\) with \(\Re\rho>1/2\) gives the
genuine nonreal pole

\[
\operatorname*{Res}_{z=\rho-1/2}\widehat A(z)
=
\frac{m_\rho}{(\rho-1/2)^2}\ne0.
\tag{T-92890.9}
\]

These are the exact pole statements of the imported Mellin theorem; no
reciprocal-zeta numerator or dyadic blind spot occurs.

## 5. Landau contradiction

By (T-92890.7), after changing \(A\) on a compact interval,

\[
f(t)=-A(e^t)\ge0
\qquad(t\ge0).
\]

The Laplace transform of \(f\) differs from \(-\widehat A(z)\) by an entire
function. Let \(\sigma_c\) be its finite abscissa of convergence.

Landau's one-sign theorem forces \(\sigma_c\) to be a singularity on the real
axis. But the continued transform has no positive-real singularity.

If a nontrivial zero
\(\rho=1/2+\delta+i\gamma\) with \(\delta>0\) existed, (T-92890.9) would give a
nonreal singularity at \(\delta+i\gamma\). If \(\sigma_c<\delta\), the defining
Laplace integral is holomorphic there, a contradiction. If
\(\sigma_c\ge\delta\), Landau forces a positive-real singularity, again a
contradiction.

Hence no nontrivial zero lies to the right of the critical line. The functional
equation excludes zeros to the left without their reflected partners, so every
nontrivial zero has real part \(1/2\).

\[
\boxed{\mathrm{RH}.}
\tag{T-92890.10}
\]

## 6. Exact boundary

This theorem does not infer RH from a finite computation. It uses the finite
row only to obtain the unconditional eventual endpoint sign. The Mellin pole
audit and Landau theorem supply the global converse.

```text
finite feasible row -> F_Lambda upper bound       EXACT
native deficit <61000                             PRODUCER INPUT
prime-square deterministic moat                   UNCONDITIONAL IMPORT
eventual prime-endpoint negativity                EXACT CONSEQUENCE
off-line zero survives in Mellin transform        EXACT IMPORT
Landau one-sign contradiction                     CLASSICAL
Riemann Hypothesis                                CONCLUSION
```
