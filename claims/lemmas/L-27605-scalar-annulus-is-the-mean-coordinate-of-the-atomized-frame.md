# L-27605 — The scalar prime annulus is the mean coordinate of the atomized carry frame

Claim ID: `L-27605`  
Title: Averaging all carry positions gives the top-quarter commutator exactly, while squaring first gives a stronger positive vector energy  
Status: **PROPOSED COMPLETE EXACT ANALYTIC LEMMA PENDING INDEPENDENT REVIEW**  
Authoring agent: `gpt56-08`  
Created: 2026-08-08  
Dependencies: `L-27601`--`L-27603`; PR #297 `L-29001`  
Scope: exact scalar/vector bridge; no bound for the vector energy and no RH conclusion

## 1. Atomized carry field

For `0<=theta<=1`, let

\[
C(x,\theta)
=\lfloor x\rfloor-\lfloor\theta x\rfloor
 -\lfloor(1-\theta)x\rfloor
\]

and

\[
H_\theta(u)=e^{-u/2}C(e^u,\theta)\mathbf1_{u\ge0}.
\tag{L-27605.1}
\]

Put

\[
s=z+\frac12,
\qquad
N_\theta(s)=\frac{1-\theta^s-(1-\theta)^s}{s}.
\tag{L-27605.2}
\]

The exact transform is

\[
\widehat H_\theta(z)=\zeta(s)N_\theta(s).
\tag{L-27605.3}
\]

Let

\[
E(s)=(1-2^{-s})(1-2^{-s-1})
\]

and use the opposite-parity source `Omega_2=E/zeta`. After applying the ordinary von Mangoldt measure, define the pole-preserving atomized field

\[
\mathfrak P_\theta(t).
\]

Its transform is

\[
\boxed{
\widehat{\mathfrak P_\theta}(z)
=-E(s)N_\theta(s)\frac{\zeta'}{\zeta}(s).
}
\tag{L-27605.4}
\]

## 2. Uniform carry average

For `Re(s)>-1`,

\[
\int_0^1\theta^s\,d\theta
=\int_0^1(1-\theta)^s\,d\theta
=\frac1{s+1}.
\]

Therefore

\[
\boxed{
\int_0^1N_\theta(s)\,d\theta
=\frac{s-1}{s(s+1)}
=:R(s).
}
\tag{L-27605.5}
\]

This is the transform version of the exact physical average

\[
\int_0^1H_\theta(u)\,d\theta=k(u)
\]

proved in `L-27601`.

Linearity of every source and prime convolution gives

\[
\boxed{
\mathfrak P(t)=\int_0^1\mathfrak P_\theta(t)\,d\theta,
}
\tag{L-27605.6}
\]

where `mathfrak P` is exactly the scalar top-quarter prime-annulus field of
`L-27603/T-27601`. Indeed its transform is

\[
-E(s)R(s)\frac{\zeta'}{\zeta}(s).
\]

Thus no extra kernel or approximation separates the scalar and atomized routes: the former is the mean coordinate of the latter.

## 3. Energy domination

Define

\[
\mathfrak E(J)=\int_J^{J+1}|\mathfrak P(t)|^2\,dt
\tag{L-27605.7}
\]

and the full atomized energy

\[
\boxed{
\mathscr E_0(J)
=\int_J^{J+1}\int_0^1
 |\mathfrak P_\theta(t)|^2\,d\theta\,dt.
}
\tag{L-27605.8}
\]

Since the `theta` interval has measure one, Cauchy--Schwarz applied to
(L-27605.6) gives pointwise

\[
|\mathfrak P(t)|^2
\le\int_0^1|\mathfrak P_\theta(t)|^2\,d\theta.
\]

Hence

\[
\boxed{
\mathfrak E(J)\le\mathscr E_0(J).
}
\tag{L-27605.9}
\]

Consequently any subexponential estimate for the atomized energy proves PAE and therefore RH through `T-27601`.

The converse is neither asserted nor needed: one mean coordinate may be small while transverse carry-position modes remain large.

## 4. The full frame retains every zero

Let `rho` be a nontrivial zero. Its residue vector in the atomized field is

\[
-m_\rho E(\rho)N_\theta(\rho).
\]

The squared frame norm is

\[
\mathfrak A_0(\rho)
=\int_0^1|N_\theta(\rho)|^2\,d\theta.
\tag{L-27605.10}
\]

It is strictly positive. If it vanished, `N_theta(rho)` would be zero almost everywhere and therefore, by analyticity in `theta`, identically on `(0,1)`. Differentiating

\[
1-\theta^\rho-(1-\theta)^\rho=0
\]

would give

\[
\theta^{\rho-1}=(1-\theta)^{\rho-1}
\]

on an interval, forcing `rho=1`, impossible for a nontrivial zero.

Thus the vector-valued energy has no common zero direction. Averaging before squaring can produce cancellation between positions; retaining the frame removes that artificial loss.

## 5. Exact finite Gram

At a finite scale `X=e^t`, PR #297 gives

\[
\mathfrak P_\theta(\log X)
=\frac1{\sqrt X}
 \sum_{m\le X}\Lambda(m)Z_{X,m}(\theta),
\tag{L-27605.11}
\]

with the explicit factor-four wavelets `Z_(X,m)`. Therefore

\[
\boxed{
\int_0^1|\mathfrak P_\theta(\log X)|^2d\theta
=rac1X\sum_{m,n\le X}
 \Lambda(m)\Lambda(n)
 \int_0^1Z_{X,m}(\theta)Z_{X,n}(\theta)d\theta.
}
\tag{L-27605.12}
\]

The right side is one finite positive-semidefinite carry-position Gram. This is the correct setting for a completed Selberg absorption argument; the raw scalar Mellin multiplier in `R-27601` has no positive-square factorization.

## 6. Revised proof target

The scalar PAE route is now subsumed by the stronger exact target

\[
\boxed{
\mathscr E_0(J)=e^{o(J)}.
}
\tag{L-27605.13}
\]

The endpoint source packet of this frame is controlled on PR #297. The remaining obstruction there is the complete coupled interior source matrix, not a Hardy factorization of the averaged annulus.

## 7. Proof boundary

Closed exactly or by elementary Hilbert-space inequalities:

1. transform average (L-27605.5);
2. physical mean identity (L-27605.6);
3. energy domination (L-27605.9);
4. nonvanishing residue frame (L-27605.10);
5. exact finite carry Gram (L-27605.12).

Open:

1. a source-complete coupled interior estimate for the atomized Gram;
2. the subexponential vector-energy theorem;
3. RH.
