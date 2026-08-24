# L-105511 — Polynomial Wick energy and the 92.10% reserve

Claim ID: `L-105511`  
Status: **PROVED FROM THE PNT AT THE FROZEN MODEL SCOPE**  
Created: 2026-08-24  
Depends on: `L-105510`; the prime-simplex argument of `L-105321`

Write

\[
\frac{P_2(x)^2}{1-x}=\sum_{m\ge0}q_mx^m.
\]

By `L-105510`,

\[
q_0=1,
\qquad q_1=q_2=0,
\qquad q_3=\frac18,
\qquad q_m=\frac9{64}\quad(m\ge4).
\tag{L-105511.1}
\]

Define

\[
a_{P,L}(n)=
\sum_{m=3}^{\Omega(n)}q_mL^{-m}\Lambda^{*m}(n).
\tag{L-105511.2}
\]

The same squarefree-simplex, repeated-prime, and dominated-convergence proof
as `L-105321` gives

\[
\mathcal D_P
:=
\lim_{L\to\infty}
\sum_{n\le e^L}\frac{a_{P,L}(n)^2}{n}
=
\frac1{64}\frac{3!}{6!}
+
\frac{81}{4096}
\sum_{m\ge4}\frac{m!}{(2m)!}.
\tag{L-105511.3}
\]

Put `t_m=m!/(2m)!`.  Since

\[
\frac{t_{m+1}}{t_m}=\frac1{2(2m+1)}\le\frac1{18}
\quad(m\ge4),
\]

we obtain the exact rational bound

\[
\boxed{
\mathcal D_P
\le
\frac1{7680}
+
\frac{81}{4096}\frac{18}{17}\frac1{1680}
=
\frac{1669}{11698176}
<\frac1{7000}.
}
\tag{L-105511.4}
\]

The Hermitian two-sided frozen symbol therefore has mean square

\[
1+2\mathcal D_P<\frac{3501}{3500},
\]

and normalized effective rank strictly greater than

\[
\boxed{\frac{3500}{3501}.}
\tag{L-105511.5}
\]

Under the same explicit 99% trace / 101% Hilbert--Schmidt comparison used in
`T-105500`,

\[
\eta_T
\ge
\frac{3500}{3501}\left(\frac{99}{101}\right)^2
=
\frac{3811500}{3968189}.
\tag{L-105511.6}
\]

The full-signature descent of `L-105500` then gives

\[
\boxed{
\liminf\frac{N_0}{N}
\ge
\frac{3654811}{3968189}
=0.921027451\ldots .
}
\tag{L-105511.7}
\]

Its exact margin above ninety percent is

\[
\frac{834409}{39681890}>0.
\tag{L-105511.8}
\]

The PNT/model calculation is proved; the actual-Xi 99/101 comparison is not.
