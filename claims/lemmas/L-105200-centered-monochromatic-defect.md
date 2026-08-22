# L-105200 — Centered monochromatic defect for the Xi derivative chain

Claim ID: `L-105200`
Status: **PROVED FROM THE CLASSICAL POSITIVE FOURIER KERNEL**
Created: 2026-08-23
Depends on: `L-104504`, `L-104516`, `L-104517` at PR #720 head `10bba584c01277e880aaa21e1fea09f396ca7246`
RH status: **not assumed**

Let

\[
\Xi(z)=2\int_0^\infty \Phi(u)\cos(zu)\,du,
\qquad \Phi(u)>0,
\]

and

\[
M_j=\int_0^\infty u^j\Phi(u)\,du.
\]

For an integer `m>=1`, set

\[
\kappa_m^2={M_{m+1}\over M_{m-1}},
\qquad
\Delta_m(z)=\Xi^{(m+1)}(z)+\kappa_m^2\Xi^{(m-1)}(z).
\tag{L-105200.1}
\]

The quantity `Delta_m` is the exact failure of three consecutive Xi
derivatives to lie in one monochromatic harmonic recurrence.

## 1. Exact centered Fourier representation

Let

\[
d\nu_{m-1}(u)=M_{m-1}^{-1}u^{m-1}\Phi(u)\,du,
\]

and write

\[
\mu=\int u\,d\nu_{m-1}(u),
\qquad
\sigma^2=\int (u-\mu)^2\,d\nu_{m-1}(u).
\]

Then

\[
\kappa_m^2=\int u^2\,d\nu_{m-1}(u).
\tag{L-105200.2}
\]

For the one-sided Fourier companions of `L-104516`,

\[
\mathscr D_m(z)
:=\mathscr E_{m+1}(z)+\kappa_m^2\mathscr E_{m-1}(z)
=i^{m-1}M_{m-1}
\int(\kappa_m^2-u^2)e^{izu}\,d\nu_{m-1}(u).
\tag{L-105200.3}
\]

The coefficient has zero mean. Therefore

\[
\boxed{
\mathscr D_m(z)
=i^{m-1}M_{m-1}
\int(\kappa_m^2-u^2)
\bigl(e^{izu}-e^{iz\mu}\bigr)
\,d\nu_{m-1}(u).
}
\tag{L-105200.4}
\]

Since `(-1)^(m+1)=(-1)^(m-1)`, reflected recovery gives

\[
\Delta_m(z)
=\mathscr D_m(z)+(-1)^{m-1}\mathscr D_m(-z).
\tag{L-105200.5}
\]

This centering is load bearing. An uncentered triangle inequality loses one
full standard deviation and gives only a nonsummable derivative-order error.

## 2. Quantitative defect bound

For real `x`,

\[
|e^{ixu}-e^{ix\mu}|\le |x|\,|u-\mu|.
\]

Also, with `V=u-mu`,

\[
u^2-\kappa_m^2=2\mu V+(V^2-\sigma^2).
\]

Hence

\[
\begin{aligned}
\int|u^2-\kappa_m^2|\,|u-\mu|\,d\nu_{m-1}
&\le 2\mu\sigma^2
 +\int|V|^3d\nu_{m-1}
 +\sigma^2\int|V|d\nu_{m-1}.
\end{aligned}
\tag{L-105200.6}
\]

The same saddle estimates used in `L-104504` give, for every fixed integer
`r>=1` and fixed `H`,

\[
\int e^{H|u-\mu|}|u-\mu|^r\,d\nu_j(u)
\ll_{r,H}
\left({\log(j+2)\over j+1}\right)^{r/2},
\tag{L-105200.7}
\]

and

\[
\mu\asymp\log(m+2),
\qquad
\kappa_m^2\asymp\log^2(m+2).
\tag{L-105200.8}
\]

Indeed the Gaussian bound around the saddle integrates every fixed moment;
changing the center from the saddle to the mean costs only one standard
deviation.

Combining (L-105200.4)--(L-105200.8), uniformly for real `|x|<=T_m`,

\[
\boxed{
|\Delta_m(x)|
\ll
M_{m+1}{T_m\over m}
}
\tag{L-105200.9}
\]

whenever

\[
T_m\sqrt{{\log m\over m}}\longrightarrow0.
\tag{L-105200.10}
\]

The implied constant is absolute for fixed upper bounds in the saddle strip.
For fixed `T`, (L-105200.9) is `O_T(M_(m+1)/m)`.

## 3. Interpretation

A pure frequency satisfies

\[
f^{(m+1)}+\omega^2 f^{(m-1)}=0.
\]

Equation (L-105200.9) proves that the high Xi derivative chain satisfies the
same recurrence up to a *centered* relative defect `O(T_m/m)` on every
admissible original-height window. The error is one full square root better
than the source-blind width estimate.

## Scope

This lemma is an unconditional high-derivative theorem. It neither controls a
fixed low derivative order nor proves RH. Its use is to make the
reverse--Rolle residue loss summable in derivative order.
