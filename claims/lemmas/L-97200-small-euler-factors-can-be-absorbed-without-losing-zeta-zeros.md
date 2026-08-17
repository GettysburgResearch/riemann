# L-97200 — Small Euler factors can be absorbed without losing any off-line zeta zero

Claim ID: `L-97200`  
Status: **PROVED EXACT ANALYTIC INTERFACE THEOREM**  
Created: 2026-08-17  
Depends on: the 5:3 scalar algebra of PR #557; no positivity theorem  
RH status: **not assumed**

## 1. Rough Euler product

Put

\[
Z_{<67}(z)=\prod_{p\le61}(1-p^{-z})^{-1},
\qquad
M_{67}(z)=\prod_{p\ge67}(1-p^{-z}).
\]

For \(\Re z>1\), Euler products give

\[
\boxed{M_{67}(z)=\frac{Z_{<67}(z)}{\zeta(z)}.}
\tag{L-97200.1}
\]

Both sides continue meromorphically. The finite factor \(Z_{<67}\) is analytic
and nonzero in \(\Re z>0\), because \(|p^{-z}|<1\) there.

## 2. Rough-only 5:3 source

The positive 5:3 source dictionary is

\[
q_*(1)=0,
\quad q_*(2)=15,
\quad q_*(3)=6,
\quad q_*(4)=3,
\quad q_*(n)=6\ (n\ge5),
\]

with Dirichlet series

\[
Q_*(z)=6\zeta(z)-3(1-2^{-z})(2-2^{-z}).
\tag{L-97200.2}
\]

Sieve only the rough primes. The resulting Dirichlet series is

\[
\boxed{
Q_*(z)M_{67}(z)
=Z_{<67}(z)
\left[6-
\frac{3(1-2^{-z})(2-2^{-z})}{\zeta(z)}\right].
}
\tag{L-97200.3}
\]

Thus every prime below 67 remains in the positive source. It is not assigned a
signed terminal colour. Its entire analytic effect is the fixed nonvanishing
factor \(Z_{<67}\).

## 3. Boundary-null source

Define a second positive dictionary

\[
q_\partial(1)=0,
\qquad q_\partial(2)=1+\sqrt2,
\qquad q_\partial(n)=1\quad(n\ge3).
\tag{L-97200.4}
\]

Its Dirichlet series is

\[
Q_\partial(z)=\zeta(z)-(1-2^{1/2-z}).
\tag{L-97200.5}
\]

After the same rough-only sieve,

\[
\boxed{
Q_\partial(z)M_{67}(z)
=Z_{<67}(z)
\left[1-
\frac{1-2^{1/2-z}}{\zeta(z)}\right].
}
\tag{L-97200.6}
\]

For \(z=s+1/2\), the numerator is \(1-2^{-s}\), which is nonzero whenever
\(\Re s>0\).

## 4. Annular Mellin consumer

Let

\[
H_X(n)=\min\!\left(\log4,\log\frac Xn\right)_+
\]

and let \(G_X=\sum_n a(n)n^{-1/2}H_X(n)\), where \(a\) is either rough-only
coefficient sequence above. Initially in a right half-plane,

\[
\boxed{
\int_1^\infty G_X X^{-s-1}\,dX
=\frac{1-4^{-s}}{s^2}A(s+1/2).
}
\tag{L-97200.7}
\]

At a hypothetical zero \(\rho\) with \(\Re\rho>1/2\), set
\(s=\rho-1/2\). The scale multiplier, the finite Euler factor, and the relevant
finite numerator are all nonzero. Hence the transform has a nonremovable pole.

For completeness, the continued expression has no singularity on the positive
real axis. For real \(z>1\), \(\zeta(z)>0\). For \(0<z<1\), the alternating
eta series is strictly positive and
\(\zeta(z)=\eta(z)/(1-2^{1-z})<0\). At \(z=1\), the reciprocal-zeta term
vanishes across the pole. Thus no real \(z>1/2\) is a zeta zero or an imported
singularity.

If either rough-only annular state is eventually nonnegative, Landau's theorem
forces its Mellin abscissa to be at most zero. The hypothetical nonreal pole is
then impossible. Functional symmetry gives RH.

The theorem is an exact change of consumer, not a proof of either required
annular sign. Its point is compositional: the `P_61` colours disappear from the
physical parity problem without disappearing from the analytic identity.
