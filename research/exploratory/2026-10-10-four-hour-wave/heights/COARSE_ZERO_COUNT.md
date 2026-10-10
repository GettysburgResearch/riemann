# A coarse complete zero count from the positive theta source and Jensen

Status: proposed native derivation, with one finite primitive input.

Scope: `N_+(T)<T log T` for every real T>=1024, counting all upper-half-plane
zeros of actual xi with analytic multiplicity. This count supplies the
complete tails in the compact Pick lemmas. It is much weaker than standard
Riemann--von Mangoldt estimates and makes no novelty claim for the bound.

Imported classical inputs: the entire completed xi function and its
functional equation/conjugation symmetry; its complete zero correspondence
with nontrivial zeta zeros in `0<Re(s)<1`; the positive theta integral
representation; Jensen's formula; Euler's integral for Gamma and the
ordinary zeta Dirichlet series on s>1.

Finite primitive input: `xi(1/2)>=1/4`. A directed Arb evaluation is enough
to establish this single positive real inequality. It is not a numerical
zero count, nor an all-height primitive.

## 1. The maximum-modulus bound uses the actual theta source

Write `E(z)=xi(1/2+z)`. Its classical representation has the form

\[
E(z)=\int_0^\infty\Phi(u)\cosh(zu)\,du,\qquad\Phi(u)>0.
\]

The standard exponentially decaying theta density justifies the integral
at every complex z. Since `|cosh(zu)|<=cosh(|Re(z)|u)`,

\[
\max_{|z|\le R}|E(z)|\le E(R)=\xi(1/2+R)\quad(R\ge0).              \tag{Z1}
\]

The normalization of Phi cancels in this comparison; it is nevertheless
the density of the actual entire xi, not a positive surrogate.

## 2. An elementary real-axis growth bound

For x>=1, write the Gamma integral as a product of
`t^(x-1)e^(-t/2)` and `e^(-t/2)`. The first factor is at most
`[2(x-1)/e]^(x-1)`, with its value at x=1 interpreted as one. Since e>2,

\[
\Gamma(x)\le2[2(x-1)/e]^{x-1}\le2x^{x-1}.            \tag{Z2}
\]

For real s>=2, integral comparison gives
`zeta(s)<=1+1/(s-1)<=2`. Dropping the factor `pi^(-s/2)<=1` in the correct
completed formula gives

\[
0<\xi(s)\le s(s-1)\Gamma(s/2)
           \le2s^{s/2+1}.                           \tag{Z3}
\]

These inequalities retain Gamma and zeta in their domains of absolute
convergence; no complex growth bound or unproved cancellation is invoked.

## 3. Jensen catches the complete upper zero set

Every zero with ordinate at most T, and its lower conjugate, has centered
modulus at most `sqrt(T^2+1/4)<T+1`, by the classical strip. Apply Jensen to
E at zero with outer radius `2(T+1)`. Every one of these `2N_+(T)` zeros
contributes at least log 2. From (Z1), (Z3), and `E(0)>=1/4`,

\[
2N_+(T)\log2
\le\log8+(T+9/4)\log(2T+5/2).                     \tag{Z4}
\]

Zeros on the outer circle cause no difficulty: apply Jensen at a slightly
larger nonexceptional radius and pass down by continuity of the growth
bound. The inner zero set is unchanged. No upper or lower zero location
is omitted, and multiplicities are exactly Jensen multiplicities.

For T>=1024, the elementary inequalities

`log2>2/3`, `log2<1`, `log3<3/2`

imply `log T>20/3`, `2T+5/2<3T`, and

\[
\begin{split}
\log8+(T+9/4)\log(2T+5/2)
 &< \left(\frac9{20480}+\frac{4105}{4096}\frac{49}{40}\right)T\log T\\
 &=\frac{201217}{163840}T\log T
 <\frac43T\log T.
\end{split}                                                       \tag{Z5}
\]

For completeness, `log2>2/3` follows by integrating the strict tangent
lower bound to 1/t at t=3/2 over [1,2]. The inequality `log2<1` follows
from 1/t<1 there, and `log3=log2+log(3/2)<1+1/2`. The final numerical
comparison in (Z5) is the exact integer inequality `603651<655360`.

Combining (Z4), (Z5), and `2log2>4/3` proves

\[
\boxed{N_+(T)<T\log T\qquad(T\ge1024).}
\]

Thus the compact theorem's counting input can be supplied from the actual
positive theta source and a single directed positive xi value. Its
finite-height zero-free input remains the separately imported
Platt--Trudgian computation. This proof does not rerun that computation.
