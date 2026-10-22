# L-90006 — A resident prime-ramp Landau consumer for WSTS

Claim ID: `L-90006` (provisional range 90001+; allocate at registry before integration)  
Status: **PROPOSED COMPLETE CONDITIONAL THEOREM — self-contained analytic consumer; independent review required**  
Authoring agent: `gpt56-sol`  
Date: 2026-08-09  
Depends on: the definitions and per-modulus bridge/profile bound of `T-90001`; classical Euler product / meromorphic continuation / functional equation of `zeta`; Landau's one-sign theorem.  
Scope: proves `WSTS => RH`; it does not prove WSTS.

## 1. Statement

Let
\[
P(X)=\sum_{p\le X}\frac{\log p}{\sqrt p}\log\frac Xp,
\qquad X\ge1,
\tag{L-90006.1}
\]
with the empty sum interpreted as zero.  If WSTS holds, then for every
\(\varepsilon>0\),
\[
\boxed{4\sqrt X-P(X)\ll_\varepsilon X^\varepsilon.}
\tag{L-90006.2}
\]
The bound is one-sided and holds for all real \(X\ge1\) after enlarging the
constant.

Conversely, (L-90006.2) for every \(\varepsilon>0\) implies the Riemann
Hypothesis.  Hence
\[
\boxed{\mathrm{WSTS}\Longrightarrow\mathrm{RH}.}
\tag{L-90006.3}
\]

This supplies a physically resident replacement for the missing session-journal
consumer flagged in `T-90001` §6.  It does not use the old square-screw stack,
the `\widehat E` Mellin variant, or real-\(X\) interpolation of the auxiliary
quantity `A_X`.

## 2. WSTS telescopes to the undifferenced endpoint

Retain
\[
A_X=\sum_{p\le X}(\log p)r_X(p),
\qquad Y=\lfloor X/2\rfloor.
\tag{L-90006.4}
\]
At the endpoint `z=2`, the shell definition gives the exact identity
\[
\boxed{T_X^s(2)=A_X-A_Y.}
\tag{L-90006.5}
\]
Since
\[
B_X=\max_z[T_X^s(z)]_+,
\]
we have, without taking any positive part prematurely,
\[
A_X-A_Y\le B_X.
\tag{L-90006.6}
\]
Iterate
\[
X_0=X,
\qquad X_{j+1}=\lfloor X_j/2\rfloor
\]
until a fixed bounded endpoint.  If WSTS holds, then for every
\(\varepsilon>0\),
\[
A_X
\le O(1)+\sum_j B_{X_j}
\ll_\varepsilon
1+\sum_jX_j^\varepsilon
\ll_\varepsilon X^\varepsilon.
\tag{L-90006.7}
\]
Thus WSTS controls the **undifferenced** endpoint scalar.  No shell-frequency
blind spot can survive this telescope.

## 3. The parabolic seed has ordinary-prime objective `4 sqrt(X)+polylog`

Put
\[
J_{\mathbb P}(X)=\sum_{p\le X}(\log p)v_p(b_X)
\tag{L-90006.8}
\]
and introduce the complete prime-power objective
\[
J_\Lambda(X)=\sum_{q\le X}\Lambda(q)v_q(b_X).
\tag{L-90006.9}
\]
By divisor switching and
\(\sum_{q\mid n}\Lambda(q)=\log n\),
\[
\begin{aligned}
J_\Lambda(X)
&=\sum_{n=2}^{X}\log n\,[b_X(n)-b_X(n+1)]\\
&=\boxed{
\sum_{n=2}^{X}b_X(n)\log\frac n{n-1}}.
\end{aligned}
\tag{L-90006.10}
\]
Here `b_X(X+1)=0` by the declared zero extension.

For the analytic formula
\[
\widetilde b_X(t)
=2\sqrt t\left(\log\frac Xt-2\left(1-\sqrt{t/X}\right)\right)
\qquad(1\le t\le X),
\]
one has
\[
\widetilde b_X'(t)
=t^{-1/2}\left(\log\frac Xt-4\right)+\frac4{\sqrt X}.
\tag{L-90006.11}
\]
Since
\[
\log\frac n{n-1}=\int_{n-1}^{n}\frac{dt}{t},
\]
(L-90006.11) gives
\[
J_\Lambda(X)
=\int_1^X\frac{\widetilde b_X(t)}t\,dt+O(\log(2X)).
\tag{L-90006.12}
\]
Indeed, on `[n-1,n]`,
\[
\frac{|\widetilde b_X(n)-\widetilde b_X(t)|}{t}
\ll
(n-1)^{-3/2}\left(1+\log\frac X{n-1}\right)
+\frac1{\sqrt X(n-1)},
\]
and the sum over `n` is `O(log(2X))`.

The integral is elementary:
\[
\boxed{
\int_1^X\frac{\widetilde b_X(t)}t\,dt
=4\sqrt X-4\log X-\frac4{\sqrt X}.}
\tag{L-90006.13}
\]
Therefore
\[
\boxed{J_\Lambda(X)=4\sqrt X+O(\log(2X)).}
\tag{L-90006.14}
\]

It remains only to remove higher prime powers.  The per-modulus bridge in
`T-90001`, together with the elementary cell bound
\[
|E(\theta)|\ll\theta^{-1/2}(1+\log(1/\theta)),
\]
gives uniformly for `2<=q<=X`
\[
|v_q(b_X)|
\ll q^{-1/2}\left(1+\log\frac Xq\right).
\tag{L-90006.15}
\]
Hence, bounding primes by all integers,
\[
\begin{aligned}
|J_\Lambda(X)-J_{\mathbb P}(X)|
&\le
\sum_{p^k\le X,\ k\ge2}(\log p)|v_{p^k}(b_X)|\\
&\ll
(1+\log X)
\sum_{p^k\le X,\ k\ge2}\frac{\log p}{p^{k/2}}\\
&\ll \log^3(2X).
\end{aligned}
\tag{L-90006.16}
\]
Thus
\[
\boxed{J_{\mathbb P}(X)=4\sqrt X+O(\log^3(2X)).}
\tag{L-90006.17}
\]

By definition,
\[
A_X=J_{\mathbb P}(X)-P(X).
\tag{L-90006.18}
\]
Combining (L-90006.7), (L-90006.17), and (L-90006.18) proves, for integer `X`,
\[
4\sqrt X-P(X)\ll_\varepsilon X^\varepsilon.
\tag{L-90006.19}
\]

## 4. Integer-to-real interpolation is elementary at the ramp level

Let `N=floor(X)` and `N<=X<N+1`.  No new prime occurs in the open interval, and
the contribution of a possible prime `N` is zero at `X=N`.  Therefore
\[
P(X)-P(N)
=\log\frac XN\sum_{p\le N}\frac{\log p}{\sqrt p}.
\tag{L-90006.20}
\]
Using only the comparison with all integers,
\[
\sum_{p\le N}\frac{\log p}{\sqrt p}
\le\sum_{n\le N}\frac{\log n}{\sqrt n}
\ll\sqrt N\log(2N),
\]
and `log(X/N)<=1/N`, we get
\[
P(X)-P(N)\ll\frac{\log(2N)}{\sqrt N}.
\tag{L-90006.21}
\]
Also
\[
\sqrt X-\sqrt N\ll N^{-1/2}.
\]
Thus (L-90006.19) extends immediately to all real `X>=1`, proving
(L-90006.2).  This is why the old auxiliary `A_X` real-interpolation flag is
not needed by the resident consumer.

## 5. Exact Mellin transform of the prime ramp

Define the deficit
\[
F(X)=4\sqrt X-P(X).
\tag{L-90006.22}
\]
For `Re z>1/2`, absolute convergence permits Fubini, and
\[
\int_p^\infty\log\frac Xp\,X^{-z-1}dX
=\frac{p^{-z}}{z^2}.
\]
Hence, with `s=z+1/2`,
\[
\int_1^\infty P(X)X^{-z-1}dX
=\frac1{z^2}\sum_p\frac{\log p}{p^s}.
\tag{L-90006.23}
\]
Write
\[
Q(s)=\sum_p\sum_{k\ge2}\frac{\log p}{p^{ks}}.
\tag{L-90006.24}
\]
The series for `Q` converges locally uniformly, hence is holomorphic, in
\[
\Re s>1/2.
\tag{L-90006.25}
\]
For `Re s>1`, the Euler product gives
\[
\sum_p\frac{\log p}{p^s}
=-\frac{\zeta'}{\zeta}(s)-Q(s),
\]
so meromorphic continuation yields
\[
\boxed{
\widehat F(z)
:=\int_1^\infty F(X)X^{-z-1}dX
=
\frac4{z-1/2}
+\frac1{z^2}\frac{\zeta'}{\zeta}\left(z+\frac12\right)
+\frac1{z^2}Q\left(z+\frac12\right).}
\tag{L-90006.26}
\]
Initially this is an integral identity for `Re z>1/2`; the right side gives a
meromorphic continuation to `Re z>0`.

### The real pole cancels

At `z=1/2`, `s=1` and
\[
\frac{\zeta'}{\zeta}(s)=-\frac1{s-1}+O(1).
\]
Since `z^{-2}=4+O(z-1/2)`, the residue of the second term in
(L-90006.26) is `-4`, exactly cancelling the residue `+4` of the first term.
Thus
\[
\boxed{z=1/2\text{ is regular}.}
\tag{L-90006.27}
\]

### Every off-line zero survives

If `rho` is a nontrivial zero of multiplicity `m_rho` and
\[
\Re\rho>1/2,
\qquad z_\rho=\rho-1/2,
\]
then `z_rho!=0` and
\[
\operatorname*{Res}_{z=z_\rho}\widehat F(z)
=\boxed{\frac{m_\rho}{z_\rho^2}\ne0.}
\tag{L-90006.28}
\]
The prime-power remainder `Q` is holomorphic there.  No `1/zeta` factor is
introduced, so there is no derivative-dependent cancellation.

### There is no positive-real singularity

For real `z>0`, `s=z+1/2>1/2`.  On `(1/2,1)`, the alternating eta series is
strictly positive and
\[
\eta(s)=(1-2^{1-s})\zeta(s),
\]
so `zeta(s)<0`; for `s>1`, `zeta(s)>0`.  Hence there is no real zeta zero in
this interval.  The only real singularity at `s=1` was removed by
(L-90006.27), while `Q` is holomorphic.  Therefore
\[
\boxed{\widehat F\text{ has no singularity on }(0,\infty).}
\tag{L-90006.29}
\]

## 6. Landau contradiction

Assume (L-90006.2) for every positive exponent and suppose, for contradiction,
that
\[
\rho=\beta+i\gamma,
\qquad \delta=\beta-1/2>0,
\]
is a nontrivial zero.  Choose
\[
0<\varepsilon<\delta.
\]
By (L-90006.2), after enlarging the constant if necessary on a compact interval,
there is `C=C_epsilon>0` such that
\[
G_\varepsilon(X)=CX^\varepsilon-F(X)\ge0
\qquad(X\ge1).
\tag{L-90006.30}
\]
A crude bound
\[
P(X)\ll\sqrt X\log^2(2X)
\]
shows
\[
G_\varepsilon(X)\ll\sqrt X\log^2(2X)+X^\varepsilon,
\]
so the Laplace/Mellin transform
\[
\mathcal G_\varepsilon(z)
=\int_1^\infty G_\varepsilon(X)X^{-z-1}dX
\tag{L-90006.31}
\]
has a finite abscissa of convergence `sigma_c<=1/2`.

For `Re z>1/2`,
\[
\boxed{
\mathcal G_\varepsilon(z)
=\frac C{z-\varepsilon}-\widehat F(z).}
\tag{L-90006.32}
\]
The right side gives a meromorphic continuation to `Re z>0`.  By
(L-90006.29), it has no positive-real singularity except the explicit simple
pole at `z=epsilon`.

Now put `X=e^t`.  Equation (L-90006.31) is the ordinary Laplace transform of the
nonnegative function `G_epsilon(e^t)`.  Landau's one-sign theorem says that a
finite abscissa of convergence is a singular point on the **real** axis.

- If `sigma_c>epsilon`, Landau forces a singularity at the positive real point
  `sigma_c`, contradicting (L-90006.32).
- If `sigma_c<epsilon`, the defining integral is holomorphic at `z=epsilon`,
  contradicting the genuine pole in (L-90006.32).

Therefore
\[
\boxed{\sigma_c=\varepsilon.}
\tag{L-90006.33}
\]
The defining nonnegative transform is consequently holomorphic throughout
`Re z>epsilon`.  But the hypothetical zero gives, by (L-90006.28), a genuine
nonreal pole of (L-90006.32) at
\[
z_\rho=\rho-1/2,
\qquad\Re z_\rho=\delta>\varepsilon.
\]
Uniqueness of analytic continuation from the common half-plane `Re z>1/2`
contradicts this pole.  Hence no nontrivial zero can satisfy `Re rho>1/2`.
The functional equation then gives
\[
\boxed{\mathrm{RH}.}
\tag{L-90006.34}
\]

## 7. What this closes and what it does not

Closed here, subject to independent review:

1. exact `z=2` WSTS telescope to the undifferenced endpoint;
2. elementary `4 sqrt(X)+O(log^3 X)` ordinary-prime seed objective;
3. the sharp one-sided prime-ramp consequence of WSTS;
4. direct real-endpoint interpolation at the ramp level;
5. exact prime-ramp Mellin transform with a holomorphic higher-prime-power remainder;
6. cancellation of the zeta pole at `s=1`;
7. survival of every hypothetical zero with `Re rho>1/2`;
8. the Landau one-sign contradiction.

Not closed:

1. WSTS itself;
2. any unconditional estimate of the surviving prime-ramp deficit at subpower scale;
3. RH.

The theorem is a **consumer**, not a producer: it removes a review-residency gap
without weakening the remaining RH-bearing burden.