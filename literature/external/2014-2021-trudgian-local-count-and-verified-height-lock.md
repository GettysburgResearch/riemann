# External source lock — verified critical zeros and a local multiplicity bound

Status: **EXTERNAL PUBLISHED INPUT / NOT REPLAYED HERE**  
Created: 2026-08-14  
RH status: **unproved**

## 1. Verified critical-line range

Dave Platt and Tim Trudgian, *The Riemann hypothesis is true up to
`3·10^12`*, Bull. London Math. Soc. 53 (2021), 792–797,
DOI `10.1112/blms.12460`, rigorously verify by interval arithmetic and
Turing's method that every nontrivial zero

\[
 \rho=\beta+i\gamma,
 \qquad
 0<\gamma\le H,
\]

with

\[
 \boxed{H=3{,}000{,}175{,}332{,}800}
\]

lies on the critical line and is simple.

Consequently every possible off-line zero has ordinate `|gamma|>H`.
The Riemann–von Mangoldt formula, with the explicit argument bound below,
shows `N(H/2)>0`; hence there is at least one verified simple critical-line
zero

\[
 \rho_0=\frac12+i\gamma_0,
 \qquad
 0<\gamma_0\le H/2.
\]

Only the inequalities `gamma_0^2<=H^2/4` and multiplicity one are used in
the new curvature argument.  No table of individual ordinates is imported.

## 2. Explicit argument bound

Timothy Trudgian, *An improved upper bound for the argument of the Riemann
zeta-function on the critical line II*, J. Number Theory 134 (2014),
280–292, proves for `T>=e`

\[
 \boxed{
 |S(T)|
 \le 0.112\log T+0.278\log\log T+2.510.
 }
\]

Using

\[
 N(T)=1+\frac{\vartheta(T)}\pi+S(T)
\]

away from zero ordinates, together with the elementary Stirling bound

\[
 \vartheta'(u)\le\frac12\log(T+3)
 \qquad(T-2\le u\le T+2,\ T\ge H),
\]

one obtains

\[
\begin{aligned}
 N(T+2)-N(T-2)
 &\le \frac2\pi\log(T+3)
      +0.224\log(T+3)\\
 &\quad+0.556\log\log(T+3)+5.020.
\end{aligned}
\]

At `T=H` the right-hand side is less than
`1.101 log(T+3)`, and the ratio of the last two terms to `log(T+3)`
decreases thereafter.  The deliberately rounded consequence used by the
proof packet is

\[
 \boxed{
 N(T+2)-N(T-2)\le2\log(T+3)
 \qquad(T\ge H),
 }
\]

with zeros counted with multiplicity.

## 3. Translation to squared-pole weights

For

\[
 \Xi(z)=\xi\!\left(\frac12+z\right),
 \qquad
 \Phi(t)=\Xi(\sqrt t),
\]

a critical zero of multiplicity `m` contributes one squared-pole parameter
of weight `2m`; an off-line reflected pair of multiplicity `m` contributes
two conjugate squared-pole parameters, each of weight `2m`.

Therefore the total squared-pole weight whose positive ordinate lies in an
interval `J` is at most twice the ordinary multiplicity count in `J`.  In
particular, for every `B>=H`,

\[
 \boxed{
 W([B-2,B+2])\le4\log(B+3).
 }
\]

## 4. Trust boundary

The two published computations/estimates are imported rather than rerun.
The deductions from them to the pairwise curvature domination theorem are
new and remain **PROPOSED pending independent review**.
