# L-104504 — High Xi derivatives are real-rooted in every fixed original-height strip

Claim ID: `L-104504`  
Status: **PROVED UNCONDITIONALLY**  
Created: 2026-08-22  
Depends on: the classical positive Fourier kernel of Xi; elementary Laplace concentration  
RH status: **not assumed**

This theorem upgrades the fixed-scaled-box result `L-104503` to the fixed
**original** `t`-plane boxes needed by the reverse-Rolle cascade.

## 1. Positive tilted Fourier measure

Use the classical representation

\[
\Xi(z)=2\int_0^\infty \Phi(u)\cos(zu)\,du,
\tag{L-104504.1}
\]

where

\[
\Phi(u)=
\sum_{m\ge1}
\left(2\pi^2m^4e^{9u/2}-3\pi m^2e^{5u/2}\right)
 e^{-\pi m^2e^{2u}}.
\tag{L-104504.2}
\]

Every summand is positive for `u>=0`, and `Phi` is rapidly decreasing.
For `n>=1`, put

\[
Z_n=\int_0^\infty u^{2n}\Phi(u)\,du
\]

and let `nu_n` be the probability measure

\[
d\nu_n(u)=Z_n^{-1}u^{2n}\Phi(u)\,du.
\]

Then

\[
\boxed{
{(-1)^n\Xi^{(2n)}(z)\over(-1)^n\Xi^{(2n)}(0)}
=\int_0^\infty\cos(zu)\,d\nu_n(u).
}
\tag{L-104504.3}
\]

## 2. Absolute saddle concentration

The `m=1` term in (L-104504.2) dominates with all derivatives.  As `u->infty`,

\[
\log\Phi(u)
=-\pi e^{2u}+{9\over2}u+\log(2\pi^2)+O(e^{-2u}),
\tag{L-104504.4}
\]

and the first three derivatives may be differentiated termwise:

\[
(\log\Phi)'(u)
=-2\pi e^{2u}+{9\over2}+O(e^{-2u}),
\]

\[
(\log\Phi)''(u)
=-4\pi e^{2u}+O(e^{-2u}),
\]

\[
(\log\Phi)'''(u)
=-8\pi e^{2u}+O(e^{-2u}).
\tag{L-104504.5}
\]

Let

\[
S_n(u)=2n\log u+\log\Phi(u).
\]

Its global maximum is attained at a point `w_n -> infinity`.  The saddle
equation and (L-104504.5) give

\[
2\pi e^{2w_n}={2n\over w_n}+O(1),
\qquad
w_n={1\over2}\log n+O(\log\log n),
\tag{L-104504.6}
\]

and

\[
-S_n''(w_n)
={4n\over w_n}\left(1+O(1/w_n)\right).
\tag{L-104504.7}
\]

Put

\[
\sigma_n=\sqrt{w_n/n}.
\]

The derivative estimates above imply the following uniform Laplace bounds.
There are absolute `c,C>0` such that, for large `n`,

\[
S_n(w_n+v)-S_n(w_n)
\le -c{n\over w_n}v^2
\qquad(|v|\le1),
\tag{L-104504.8}
\]

and

\[
S_n(w_n+v)-S_n(w_n)
\le-c{n\over w_n}
\qquad(1\le|v|\le w_n/2).
\tag{L-104504.9}
\]

Indeed, on `[w_n-1,w_n+1]`, (L-104504.5)--(L-104504.7) give
`-S_n''(u)\asymp n/w_n`.  On the rest of `[w_n/2,3w_n/2]`, `S_n'` is
strictly decreasing, so the value is bounded by one of the two points
`w_n-1,w_n+1`.  The two complementary tails have mass `O(e^{-cn})`
relative to the central Laplace mass.  Integrating these estimates, and using
a matching lower bound on `|v|<=sigma_n`, gives for every fixed `H>0`

\[
\boxed{
\int e^{H|u-w_n|}|u-w_n|\,d\nu_n(u)
\ll_H \sigma_n
\longrightarrow0.
}
\tag{L-104504.10}
\]

For completeness, the tail argument is elementary:

- on `u<=w_n/2`, the factor `u^(2n)` loses at least `2^{-2n}` relative to
  the saddle;
- on `u>=3w_n/2`, the term `exp(-pi e^(2u))` gives a still stronger loss;
- on the middle interval, (L-104504.5) makes `S_n` strictly concave and
  yields (L-104504.8).

Thus the tilted Fourier frequency collapses in **absolute**, not merely
relative, width.

## 3. Original-scale cosine approximation

For fixed `T,H>0` and

\[
R_{T,H}=\{z:|\Re z|\le T,\ |\Im z|\le H\},
\]

(L-104504.10) and

\[
|e^{iz(u-w_n)}-1|
\le |z|\,|u-w_n|e^{H|u-w_n|}
\]

give, uniformly on `R_(T,H)`,

\[
\boxed{
\left|
{(-1)^n\Xi^{(2n)}(z)\over(-1)^n\Xi^{(2n)}(0)}
-\cos(w_nz)
\right|
\le \varepsilon_n(T,H)e^{w_n|\Im z|},
}
\tag{L-104504.11}
\]

where `epsilon_n(T,H)->0`.

## 4. Rouché on all growing-frequency cells

Fix `0<rho<pi/4`.  The zeros of `cos(w_nz)` are

\[
x_{j,n}={(j+1/2)\pi\over w_n}.
\]

Take the disjoint disks

\[
D_{j,n}=\{|z-x_{j,n}|<\rho/w_n\}
\]

whose centres meet the slightly enlarged rectangle `R_(T+1,H+1)`.
On `partial D_(j,n)`,

\[
|\cos(w_nz)|=|\sin(\rho e^{i\theta})|
\ge m_\rho>0,
\]

while the right side of (L-104504.11) is at most
`epsilon_n e^rho`.  Rouché therefore gives exactly one derivative zero in
each disk.

On the complement of the disks, use

\[
|\cos(x+iy)|^2=\cos^2x+\sinh^2y.
\tag{L-104504.12}
\]

If `w_n|Im z|>=rho/2`, then

\[
|\cos(w_nz)|\ge c_\rho e^{w_n|\Im z|}.
\]

If `w_n|Im z|<rho/2`, exclusion from the disks gives a fixed positive lower
bound for `|cos(w_n z)|`.  Hence (L-104504.11) excludes all other zeros for
large `n`.

The normalized derivative is real entire.  A nonreal zero in a
conjugation-invariant disk would bring its distinct conjugate, contradicting
the Rouché count one.  Therefore each disk zero is real and simple.

## 5. The theorem

For every fixed `T,H>0`, there exists `n_0(T,H)` such that for `n>=n_0` every
zero of

\[
\Xi^{(2n)}(z)
\]

in `R_(T,H)` is real and simple.

Equivalently,

\[
\boxed{
\text{every fixed original-height complex rectangle is eventually
off-real-zero-free under even differentiation.}
}
\tag{L-104504.13}

Taking `H>1/2` supplies the high-derivative entry for every fixed Riemann
critical-strip height.  No RH assumption and no derivative-zero proportion is
used.

## Scope

The theorem does not descend this zero-free rectangle back to Xi.  The exact
remaining obstruction is the cumulative Riccati–Pick/endpoint/winding charge
of `L-104501`.
