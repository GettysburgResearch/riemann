# L-90413 — The mean carry mode is a zero-safe prime-ramp scalar

Claim ID: `L-90413`  
Title: The zeroth Fourier coordinate of the compact-Q4 carry field has an explicit Mellin transform retaining every open-strip zeta-zero pole  
Status: **PROPOSED COMPLETE EXACT REDUCTION — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-11  
Dependencies: `L-90411`, `L-90412`; elementary Mellin integration  
Scope: one scalar coordinate; no sign or critical-growth theorem is proved

## 1. Exact mean coordinate

For real \(X\ge1\), define

\[
\boxed{
M_\circ(X)
=
\sum_{m\le X}
c_\circ(m)\left(\frac{2m}{X}-1\right),
}
\tag{L-90413.1}
\]

where \(c_\circ=\mathbf1*i_\circ\) is given by `L-90412`.

At integer \(X=N\), formula `L-90411.4` gives exactly

\[
\boxed{
M_\circ(N)=\widehat Q_{\circ,N}(0).
}
\tag{L-90413.2}
\]

Thus the constant carry-position coordinate is a compact signed
prime-power ramp.

## 2. Mellin transform

For \(\Re z>1\), absolute convergence permits termwise integration:

\[
\begin{aligned}
\int_1^\infty M_\circ(X)X^{-z-1}\,dX
&=
\sum_{m\ge1}c_\circ(m)
\int_m^\infty
\left(\frac{2m}{X}-1\right)X^{-z-1}\,dX\\
&=
\frac{z-1}{z(z+1)}
\sum_{m\ge1}\frac{c_\circ(m)}{m^z}.
\end{aligned}
\]

Using `L-90412.2`,

\[
\boxed{
\begin{aligned}
\int_1^\infty M_\circ(X)X^{-z-1}\,dX
={}&
\frac{z-1}{z(z+1)}
\Bigg[
(1-4^{1-z})
\left(-\frac{\zeta'}{\zeta}(z)\right)\\
&\qquad\qquad
+3(\log4)\frac{4^{-z}}{1-4^{-z}}
\Bigg].
\end{aligned}
}
\tag{L-90413.3}
\]

## 3. Every open-strip zero survives

If \(\rho\) is a nontrivial zeta zero, the logarithmic derivative has a
pole at \(\rho\). Its coefficient in (L-90413.3) cannot vanish in the
open critical strip:

\[
1-4^{1-\rho}=0
\quad\Longrightarrow\quad
4^{1-\Re\rho}=1
\quad\Longrightarrow\quad
\Re\rho=1.
\]

The rational Mellin prefactor is also nonzero at a nontrivial zero, and
the four-adic term is holomorphic there. Hence

\[
\boxed{
\text{every zeta zero with }0<\Re\rho<1
\text{ is visible in }M_\circ.
}
\tag{L-90413.4}
\]

In particular, a bound

\[
M_\circ(X)=O_\epsilon(X^{1/2+\epsilon})
\qquad(\epsilon>0)
\tag{L-90413.5}
\]

would continue (L-90413.3) holomorphically to every half-plane
\(\Re z>1/2+\epsilon\) and exclude all zeros with real part \(>1/2\).
Functional-equation symmetry would then give RH.

## 4. Consequence for PIG

`L-90412` shows that only the mean and \(O(\sqrt N)\) low additive
residue classes remain after the unconditional bulk estimate. This lemma shows
that the mean is not a harmless collar: by itself it retains the full zeta-zero
obstruction.

Therefore a successful major-mode proof must either:

1. prove the critical growth of \(M_\circ\) directly;
2. combine it with the nonzero low residues in an exact cancellation that
   remains zero-safe; or
3. apply an additional annular/filter architecture and prove its sign or norm.

No such estimate is claimed here.
