# L-96103 — The PR #542 Mellin–Landau consumer is valid for the discrete-tail row, conditional only on its global positivity

Claim ID: `L-96103`  
Status: **PROVED CONDITIONAL ANALYTIC CONSUMER WITH ROW-TYPE FIX**  
Created: 2026-08-16  
Frozen source: PR #542 at `ca5fb69c15cda29b3b589660f9be44ea2f440677`  
Depends on: `L-96100`; standard Landau abscissa theorem  
RH status: **conditional on the open global positivity producer**

## 1. The row and its full Möbius transform

Fix `j>=2` and use the discrete-tail row of `L-96100`:

\[
 Q_X^{\rm tail}(j)
 =\sum_{m\le X}\frac{q_j(m)}{\sqrt m}\log\frac Xm.
\]

Put

\[
 f_j(X)=
 \sum_{k\le X/j}
 \frac{\mu(k)}{\sqrt k}Q_{X/k}^{\rm tail}(j).
\tag{L-96103.1}
\]

A trivial absolute estimate gives

\[
 |f_j(X)|\ll_j\sqrt X\log(2X),
\tag{L-96103.2}
\]

so its Mellin integral has a finite abscissa of convergence.

## 2. Exact transform

For `Re s>1/2`, all sums and integrals are absolutely convergent and

\[
 \int_m^\infty\log\frac Xm\,X^{-s-1}\,dX
 =\frac{m^{-s}}{s^2}.
\]

With `z=s+1/2`, define

\[
 H_j(z)=
 A_jj^{-z}-B_j(j+1)^{-z}
 +C_j\sum_{m\ge j+2}m^{-z},
\]

and

\[
 P_j(z)=
 A_jj^{-z}-B_j(j+1)^{-z}
 -C_j\sum_{m=1}^{j+1}m^{-z}.
\]

Then

\[
 H_j(z)=C_j\zeta(z)+P_j(z).
\]

Substituting `X=kY` in (L-96103.1) gives

\[
 \boxed{
 \int_1^\infty f_j(X)X^{-s-1}\,dX
 =\frac{C_j}{s^2}
 +\frac{P_j(s+1/2)}{s^2\zeta(s+1/2)}.
 }
\tag{L-96103.3}
\]

This is exactly the algebraic statement of `L-96000`, with the row source
corrected from “parabolic” to “discrete tail.”

The right-hand side is meromorphic on `Re s>0` and analytic at every positive
real `s`: zeta has no real zero for real argument greater than `1/2`, and its
pole at one becomes a zero of `1/zeta`.

## 3. Noncancellation at an off-line zero

If `0<Re rho<1`, `rho!=1`, and `zeta(rho)=0`, Euler–Maclaurin at that fixed
`rho` gives

\[
 \boxed{
 P_j(\rho)
 =-\frac{\rho(\rho+1)}{1-\rho}
   j^{-\rho-1}
 +O_\rho(j^{-\Re\rho-2}).
 }
\tag{L-96103.4}
\]

The leading coefficient is nonzero at every nontrivial zeta zero. Therefore,
for that fixed zero, `P_j(rho)!=0` for every sufficiently large fixed `j`.
No effective uniform bound in `rho` is needed.

## 4. Landau implication

Assume the open producer theorem

\[
 f_j(X)\ge0
 \qquad(X\ge1,\ j\ge2).
\tag{L-96103.5}
\]

Fix one `j` and let `sigma_j` be the real abscissa of convergence of the
Mellin integral in (L-96103.3). Landau's theorem for a nonnegative Mellin
kernel says that a finite real abscissa is a singular point of the transform.
Since (L-96103.3) is analytic at every positive real point,

\[
 \sigma_j\le0.
\tag{L-96103.6}
\]

Thus the defining integral, not merely its continuation, is holomorphic in
`Re s>0`.

If `zeta(rho)=0` with `Re rho>1/2`, choose `j` from (L-96103.4) and put

\[
 s_\rho=\rho-\frac12.
\]

Then `Re s_rho>0`, while the right-hand side of (L-96103.3) has a nonremovable
pole at `s_rho`. This contradicts holomorphy of the defining integral. Hence no
zeta zero lies to the right of the critical line; the functional equation gives
RH.

## 5. Exact boundary

```text
discrete-tail Mellin transform             exact
reciprocal-zeta factor                     exact
positive-real-axis analyticity             exact
large-j zero noncancellation               exact
Landau implication after f_j>=0            exact conditional consumer
parabolic endpoint row                     not used
universal f_j>=0                            OPEN / load-bearing
Riemann Hypothesis                          UNPROVED
```
