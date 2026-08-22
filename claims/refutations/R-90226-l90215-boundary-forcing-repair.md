# R-90226 — The positive divisor forcing must retain its sub-four boundary state

Claim ID: `R-90226`  
Status: **PROPOSED COMPLETE EXACT REPAIR — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-10  
Repairs: `L-90215.12`--`L-90215.20`  
Scope: exact boundary bookkeeping; the positive-forcing route survives, but no sign theorem or RH conclusion is added

## 1. Setup

Retain

\[
 \omega=(\varepsilon-\delta_2)*(2\varepsilon-\delta_2)*\mu,
\]

\[
 \mathcal H(x)
 =-3\sum_{2\le q\le x}\omega(q)
 \left(q^{-1/2}-x^{-1/2}\right),
\]

and

\[
 (\mathcal P f)(x)=\sum_{d\le x}d^{-1/2}f(x/d).
\]

The convolution identity

\[
 1*\omega=2\varepsilon-3\delta_2+\delta_4
\]

is exact.

## 2. Exact piecewise forcing

Put

\[
 J(x)=\sum_{d\le x}d^{-1/2}
      -\frac{\lfloor x\rfloor}{\sqrt x}.
\]

The complete forcing

\[
 \widetilde\Phi(x):=(\mathcal P\mathcal H)(x)
\]

is

\[
\boxed{
\widetilde\Phi(x)=
\begin{cases}
0,&1\le x<2,\\[1mm]
6J(x)-6+\dfrac9{\sqrt2}-\dfrac3{\sqrt x},
   &2\le x<4,\\[3mm]
6J(x)-\dfrac{15}{2}+\dfrac9{\sqrt2},
   &x\ge4.
\end{cases}}
\tag{R-90226.1}
\]

### Proof

For the complete hinge transform

\[
 \mathcal R_\omega(x)
 =\sum_{q\le x}\omega(q)(q^{-1/2}-x^{-1/2}),
\]

one has

\[
 \mathcal R_\omega(x)
 =2(1-x^{-1/2})-\frac13\mathcal H(x).
\]

Finite switching gives

\[
\mathcal P\mathcal R_\omega(x)=
\sum_{n\le x}\frac{(1*\omega)(n)}{\sqrt n}
-\frac1{\sqrt x}\sum_{n\le x}(1*\omega)(n).
\]

Using `1*omega=2 epsilon-3 delta_2+delta_4`, this is

\[
\mathcal P\mathcal R_\omega(x)=
\begin{cases}
2-2x^{-1/2},&1\le x<2,\\
2-3/\sqrt2+x^{-1/2},&2\le x<4,\\
5/2-3/\sqrt2,&x\ge4.
\end{cases}
\]

Since

\[
 \mathcal P(1-x^{-1/2})=J(x),
\]

formula (R-90226.1) follows.

## 3. Positivity is retained

On the two boundary cells the forcing simplifies to

\[
 \widetilde\Phi(x)
 =15\left(\frac1{\sqrt2}-\frac1{\sqrt x}\right)
 \qquad(2\le x<3),
\]

and

\[
 \widetilde\Phi(x)
 =\frac{15}{\sqrt2}+\frac6{\sqrt3}-\frac{21}{\sqrt x}
 \qquad(3\le x<4).
\]

Both are nonnegative, and the second is already positive at `x=3` and
increases on its cell. For `x>=4`, positivity is exactly the elementary
estimate proved in `L-90215`. Hence

\[
 \boxed{\widetilde\Phi(x)\ge0\quad(x\ge1),}
\]

with equality precisely on `[1,2]` at this assurance scope.

## 4. Exact global Möbius inversion

The valid all-scale inversion is

\[
 \boxed{
 \mathcal H(x)
 =\sum_{d\le x}\frac{\mu(d)}{\sqrt d}
   \widetilde\Phi(x/d).
 }
\tag{R-90226.2}
\]

The large-cell expression

\[
 \Phi_\infty(x)=6J(x)-\frac{15}{2}+\frac9{\sqrt2}
\]

may not be substituted for `widetilde Phi(x/d)` when `x/d<4`.

## 5. Mutation rejecting the uncorrected inversion

At `x=2`, the true scalar is

\[
 \mathcal H(2)=0.
\]

Using `Phi_infinity` at every descendant instead gives

\[
 \Phi_\infty(2)-\frac1{\sqrt2}\Phi_\infty(1)
 =\frac32(\sqrt2-1)>0,
\]

so the unqualified form of `L-90215.20` is false.

## 6. Consequence

The positive-forcing programme survives exactly, but its boundary state is
load-bearing. The corrected status is

```text
positive divisor forcing:      retained on every scale;
Möbius inversion:              retained with the piecewise forcing;
global use of the x>=4 line:   refuted;
final scalar sign:             still open / RH-bearing.
```
