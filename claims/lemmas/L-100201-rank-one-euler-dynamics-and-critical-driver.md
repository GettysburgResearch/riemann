# L-100201 — Rank-one Euler dynamics and the exact critical driver

Claim ID: `L-100201`  
Status: **PROVED EXACT MATRIX AND MELLIN IDENTITIES**  
Created: 2026-08-20  
Depends on: `L-100200`  
RH status: **unproved**

Let

\[
u_N=\binom{1}{-\sqrt N}.
\]

Passing from \(N-1\) to \(N\) changes the cell state by the exact rank-one law

\[
\boxed{
M_N=M_{N-1}-\frac{\beta(N)}{N^{3/2}}u_Nu_N^{\mathsf T}.
}
\tag{L-100201.1}
\]

Moreover,

\[
z_N^{\mathsf T}u_N=1,
\]

so the activation jump of the normalized envelope is exactly

\[
\boxed{
D(N+)-D(N-)=-\frac{\beta(N)}{N^{3/2}}.
}
\tag{L-100201.2}
\]

This recovers the jump-reserve calculation inside the complete two-dimensional state.

Put

\[
\kappa_N=\det M_N.
\]

The rank-one determinant lemma gives

\[
\boxed{
\kappa_N=\kappa_{N-1}-\frac{\beta(N)}{N^{3/2}}\mathcal L(N),
}
\tag{L-100201.3}
\]

where

\[
\mathcal L(N)=NR_{3/2}(N-1)+2\sqrt N\,A_1(N-1)-A_{1/2}(N-1).
\tag{L-100201.4}
\]

Define the positive piecewise kernel

\[
K(y)=
\begin{cases}
y,&0<y<1,\\
2\sqrt y-1,&y\ge1.
\end{cases}
\]

Then finite splitting at \(n=N\) gives

\[
\boxed{
\mathcal L(N)=\sum_{n\ge1}\frac{\beta(n)}{\sqrt n}K(N/n).
}
\tag{L-100201.5}
\]

Its Mellin multiplier is

\[
\boxed{
\widehat K(s)=-\frac1{2s(s-\frac12)(s-1)}
\qquad\left(\frac12<\Re s<1\right).
}
\tag{L-100201.6}
\]

Therefore the determinant driver retains every off-line reciprocal-zeta pole:

\[
\mathcal M\mathcal L(s)=
\frac{1-67^{-(s+1/2)}}{\zeta(s+1/2)}\widehat K(s).
\tag{L-100201.7}
\]

This is a binding diagnostic. The jump combinatorics are solved, but the determinant is driven by an explicit critical scalar. A proof of `CEHC100200` must orient this rank-one evolution; ordinary positivity of \(\mathfrak H_2\), jump reserve alone, or source-blind matrix norm estimates do not do so.