# PFR-T5 — Actual-Xi Gamma-resolvent abscissa

Status: **AUTHOR-PROVED EXACT ANALYTIC THEOREM / REVIEW PENDING / EXTERNAL NOVELTY UNESTABLISHED**

Scope: global actual `xi`; no height localization. RH remains unproved.

## 4. A future Gamma resolvent of the real zero response

Let the nontrivial zeros of `zeta` be denoted by `rho`, with multiplicity, and
put

\[
\lambda_\rho=\rho-\frac12.
\tag{4.1}
\]

Define the supremal off-critical displacement

\[
B_\xi
=
\sup_\rho |\operatorname{Re}\lambda_\rho|
=
\sup_\rho\operatorname{Re}\rho-\frac12.
\tag{4.2}
\]

The second equality follows from the functional-equation symmetry.  RH is
exactly `B_xi=0`.

For a rate

\[
a>\frac12
\]

and an integer

\[
m\geq2,
\]

define the future Gamma resolvent

\[
(\mathcal G_{a,m}F)(t)
=
\frac1{\Gamma(m)}
\int_0^\infty u^{m-1}e^{-au}F(t+u)\,du.
\tag{4.3}
\]

On an exponential mode it acts diagonally:

\[
\boxed{
\mathcal G_{a,m}(e^{\lambda t})
=
\frac{e^{\lambda t}}{(a-\lambda)^m},
\qquad \operatorname{Re}\lambda<a.
}
\tag{4.4}
\]

The strict inequality `a>1/2` handles every possible nontrivial zeta zero and
makes the prime-side formula below absolutely convergent.  Choosing `a`
bounded away from `1/2` accelerates numerical convergence.

---

## 5. PFR-T5 — actual-Xi source-defined resolvent abscissa

Define, for `t>0`,

\[
\boxed{
\mathcal R_{a,m}(t)
=
\sum_\rho
\frac{e^{(\rho-1/2)t}}
     {(a+1/2-\rho)^m}.
}
\tag{5.1}
\]

### 5.1 Absolute convergence and reality

The classical estimate `N(T)=O(T log T)` gives

\[
\sum_\rho |a+1/2-\rho|^{-m}<\infty
\qquad(m\geq2).
\]

Hence (5.1) converges absolutely and locally uniformly for real `t`.  It is a
real-valued function because the zeros occur in conjugate pairs.

### 5.2 Entirely real prime-side definition

On positive frequencies, `PFR-T4` gives the distribution

\[
\sum_\rho e^{(\rho-1/2)t}
=
A(t)-
\sum_{n\geq2}\frac{\Lambda(n)}{\sqrt n}
\delta(t-\log n),
\tag{5.2}
\]

where

\[
A(t)
=e^{t/2}+e^{-t/2}
-\frac{e^{-t/2}}{1-e^{-2t}}
=e^{t/2}+e^{-t/2}
-\sum_{k\geq0}e^{-(2k+1/2)t}.
\tag{5.3}
\]

Applying (4.3) term by term yields

\[
\boxed{
\begin{aligned}
\mathcal R_{a,m}(t)
={}&
\frac{e^{t/2}}{(a-1/2)^m}
+
\frac{e^{-t/2}}{(a+1/2)^m}\\
&-
\sum_{k\geq0}
\frac{e^{-(2k+1/2)t}}
     {(a+2k+1/2)^m}\\
&-
\frac{e^{at}}{(m-1)!}
\sum_{n\geq2}
\frac{\Lambda(n)}{n^{a+1/2}}
(\log n-t)_+^{m-1}.
\end{aligned}
}
\tag{5.4}
\]

Every quantity on the right is real.  Both sums are absolutely convergent:
`m>=2` handles the archimedean series, while `a+1/2>1` handles the prime-power
source.

To justify the passage from (5.2) to (5.4), truncate the future-Gamma kernel
in `u`, smooth its single join at `u=0`, and apply the positive-frequency
explicit formula to the resulting compactly supported smooth tests.  The
zero side is dominated by

\[
\sum_\rho |a-\lambda_\rho|^{-m},
\]

the prime side by a convergent logarithmically weighted series with exponent
`a+1/2>1`, and the archimedean side by `e^{-(a-1/2)u}`.  Dominated convergence
then removes both the smoothing and the truncation.  This also makes clear why
`a>1/2` and `m>=2` are structural rather than numerical choices.

Equation (5.4) is the required source definition.  It contains no zero
locations and can be evaluated from the primes and elementary archimedean
data alone.

### 5.3 Safe Taylor-remainder transform

There is a second zero-free description of the meromorphic Laplace transform
of the response.  Put

\[
\mathcal E(w)=\xi\!\left(\frac12+w\right),
\qquad
F(w)=\frac{\mathcal E'(w)}{\mathcal E(w)}
=\frac{\xi'}{\xi}\!\left(\frac12+w\right).
\tag{5.4a}
\]

For `z` away from the centered zeros, define the normalized Taylor remainder

\[
\boxed{
\mathcal M_{a,m}(z)
=
\frac{(-1)^m}{(z-a)^m}
\left[
F(z)-
\sum_{k=0}^{m-1}\frac{F^{(k)}(a)}{k!}(z-a)^k
\right].
}
\tag{5.4b}
\]

The apparent singularity at `z=a` is removable.  The scalar geometric-
remainder identity

\[
\frac1{(a-\lambda)^m(z-\lambda)}
=
\frac{(-1)^m}{(z-a)^m}
\left[
\frac1{z-\lambda}
-
\sum_{k=0}^{m-1}
\frac{(-1)^k(z-a)^k}{(a-\lambda)^{k+1}}
\right]
\]

and the Hadamard logarithmic derivative give

\[
\boxed{
\mathcal M_{a,m}(z)
=
\sum_\rho
\frac1{(a-\lambda_\rho)^m(z-\lambda_\rho)}.
}
\tag{5.4c}
\]

All Hadamard regularization constants disappear under Taylor subtraction, and
the remaining series is normally convergent.  Thus a finite-order Taylor
remainder of the completed-zeta logarithmic derivative at the safe real point
`1/2+a>1` already contains every zero as a nonremovable pole with a prescribed
nonzero residue.  Equation (5.13) below says that it is exactly the Laplace
transform of the real prime-defined response.

### 5.4 Exact weighted-energy abscissa

For real `sigma`, put

\[
\mathcal E_{a,m}(\sigma)
=
\int_0^\infty
 e^{-2\sigma t}|\mathcal R_{a,m}(t)|^2\,dt.
\tag{5.5}
\]

Then

\[
\boxed{
\begin{aligned}
\sigma>B_\xi
&\Longrightarrow
\mathcal E_{a,m}(\sigma)<\infty,\\
\sigma<B_\xi
&\Longrightarrow
\mathcal E_{a,m}(\sigma)=\infty.
\end{aligned}
}
\tag{5.6}
\]

No assertion is needed at the boundary.  In particular,

\[
\boxed{
B_\xi
=
\inf\{\sigma:\mathcal E_{a,m}(\sigma)<\infty\}.
}
\tag{5.7}
\]

For `sigma>B_xi`, absolute convergence also gives the exact Cauchy--Gram
expansion

\[
\boxed{
\mathcal E_{a,m}(\sigma)
=
\sum_{\rho,\rho'}
\frac{
 (a-\lambda_\rho)^{-m}
 (a-\overline{\lambda_{\rho'}})^{-m}
}{
 2\sigma-\lambda_\rho-\overline{\lambda_{\rho'}}
}.
}
\tag{5.8}
\]

The same displacement is the pointwise exponential type:

\[
\boxed{
B_\xi
=
\limsup_{t\to\infty}
\frac1t\log|\mathcal R_{a,m}(t)|.
}
\tag{5.9}
\]

### Proof of the abscissa theorem

Write

\[
c_\rho=(a-\lambda_\rho)^{-m}.
\]

Absolute convergence gives the uniform upper bound

\[
|\mathcal R_{a,m}(t)|
\leq
\left(\sum_\rho|c_\rho|\right)e^{B_\xi t}.
\tag{5.10}
\]

This proves convergence in (5.6) for `sigma>B_xi`.

Now use the Taylor-remainder meromorphic function
`M_{a,m}=mathcal M_{a,m}` from (5.4b)--(5.4c).  Because a summand is
`O(|gamma|^{-m-1})`, its zero expansion is normally convergent on compact sets
away from the centered zeros.  At a zero
`lambda_0` of multiplicity `q` its residue is

\[
\frac{q}{(a-\lambda_0)^m}\neq0.
\tag{5.12}
\]

For `Re z>B_xi`, termwise Laplace transformation gives

\[
\int_0^\infty e^{-zt}\mathcal R_{a,m}(t)\,dt
=M_{a,m}(z).
\tag{5.13}
\]

Suppose that `E_{a,m}(sigma)` were finite for some `sigma<B_xi`.  By
Cauchy--Schwarz, the left side of (5.13) would define an analytic function on

\[
\operatorname{Re}z>\sigma.
\]

It agrees with `M_{a,m}` on the smaller half-plane `Re z>B_xi`, so analytic
continuation would remove every pole of `M_{a,m}` in `Re z>sigma`.  But the
definition of the supremum supplies a zero with

\[
\operatorname{Re}\lambda_0>\sigma,
\]

and (5.12) says its pole is nonremovable.  This contradiction proves the
second half of (5.6).

The same pole argument proves (5.9): any pointwise exponential bound with
exponent strictly below `B_xi` would continue the Laplace transform across a
nonremovable zero pole.

### 5.5 Real-only RH equivalences

For every fixed `a>1/2` and integer `m>=2`, the following are equivalent:

\[
\boxed{
\begin{aligned}
&\text{RH};\\
&B_\xi=0;\\
&\mathcal R_{a,m}\text{ is bounded on }[0,\infty);\\
&\mathcal E_{a,m}(\sigma)<\infty
  \text{ for every }\sigma>0;\\
&\limsup_{t\to\infty}t^{-1}\log|\mathcal R_{a,m}(t)|=0.
\end{aligned}
}
\tag{5.14}
\]

Under RH, all exponential modes are purely oscillatory and the absolutely
summable coefficients make the response bounded.  Conversely, (5.7) or (5.9)
forces `B_xi=0`.

This is an actual-zeta, entirely real observable.  Its source formula is (5.4),
and its growth threshold is the horizontal zero displacement.

---
