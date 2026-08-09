# L-90005 — Dyadic shell one-crossing and even-endpoint z-collapse

Claim ID: `L-90005` (provisional range 90001+; allocate at registry before integration)  
Status: **PROPOSED COMPLETE LEMMA — analytic proof; finite decimal brackets are non-load-bearing conveniences and can be replaced by rational log/square-root brackets**  
Authoring agent: `gpt56-sol`  
Date: 2026-08-09  
Extends: `O-90004` §1 (Lemma S, previously `NUMERICAL_ONLY`)  
Depends on definitions in `T-90001`; no prime-number theorem or zero information is used.

## 1. Statement

Retain the parabolic bridge profile
\[
E(\theta)=F(\theta)-\theta^{-1/2}\log(1/\theta)
\]
and put, at the exact dyadic ratio,
\[
E_{1/2}(\theta)=E(\theta)-\sqrt2\,E(2\theta)\mathbf 1_{\theta\le1/2}.
\]
There is a unique number
\[
\boxed{c_*=0.1408520350138399254409579889\ldots}
\tag{L-90005.1}
\]
in \((1/8,1/7)\) such that
\[
E_{1/2}(\theta)>0\quad(0<\theta<c_*),\qquad
E_{1/2}(\theta)<0\quad(c_*<\theta\le1/2).
\tag{L-90005.2}
\]
Thus the `0.1408512...` value recorded in `O-90004` is only a coarse numerical approximation; (L-90005.1) is the root of the stated `N=7/N'=3` cell equation.

More importantly, let `X` be an **even integer**, `Y=X/2`, and let the exact finite shell residual be
\[
s_X(q)=r_X(q)-r_Y(q),\qquad 2\le q\le Y.
\]
Then the continuum sign survives the floor discretization with a uniformly bounded transition width:
\[
\boxed{
q\le c_*X-1\Longrightarrow s_X(q)>0,
\qquad
q\ge c_*X+158\Longrightarrow s_X(q)<0.}
\tag{L-90005.3}
\]
The constant `158` is deliberately crude: it makes the proof completely analytic with no finite exhaustive base case. Direct high-precision enumeration gives a much narrower transition (empirically `+3` suffices on the tested range), but no such sharpening is needed below.

Consequently, for even `X`, if
\[
T_X(z)=\sum_{z\le p\le X}(\log p)s_X(p),
\qquad B_X=\max_z[T_X(z)]_+,
\]
then
\[
\boxed{
B_X=[T_X(2)]_+ + O(X^{-3/2}\log(2X)).}
\tag{L-90005.4}
\]
The implied constant is absolute.  Thus on even endpoints the `z`-max is rigorously redundant up to a vanishing error; no RH input enters this collapse.

This lemma does **not** bound `T_X(2)`.  The surviving scalar is the RH-bearing ramp deficit identified in `T-90001`/`O-90004`.

## 2. Exact cell reduction

On
\[
\frac1{N+1}<\theta\le\frac1N,
\qquad N\ge2,
\]
put `M=floor(N/2)` and
\[
D_N=S_N-S_M,
\]
\[
C_N=A_N-A_M+4D_N-(S_M+1)\log2,
\]
\[
K_N=4(N-\sqrt2 M).
\]
Writing `x=sqrt(theta)`, direct subtraction of the two exact `E`-cell formulas gives
\[
\boxed{
P_N(x):=\sqrt\theta E_{1/2}(\theta)
=C_N+2D_N\log x-K_Nx.}
\tag{L-90005.5}
\]
Hence
\[
P_N''(x)=-\frac{2D_N}{x^2}<0.
\tag{L-90005.6}
\]
Every quotient cell is therefore strictly concave.

At the reciprocal knots define
\[
Q_N=P_N(N^{-1/2}).
\]
Continuity gives `P_N((N+1)^(-1/2))=Q_(N+1)`, and subtracting the two endpoints of (L-90005.5) yields the exact increment
\[
\boxed{
Q_{N+1}-Q_N
=K_N\left(N^{-1/2}-(N+1)^{-1/2}\right)
-D_N\log(1+1/N).}
\tag{L-90005.7}
\]
The entire infinite sign problem is reduced to this scalar increment.

## 3. The knot values are strictly increasing

Set
\[
a=1-2^{-1/2},\qquad
\mathcal F(h)=\frac{1-(1+h)^{-1/2}}{\log(1+h)}.
\]
We first record the elementary bound
\[
\boxed{\mathcal F(h)\ge\frac12-\frac h8\qquad(h>0).}
\tag{L-90005.8}
\]
Indeed, put `y=sqrt(1+h)`.  The desired inequality is
\[
\frac{y-1}{y}\ge\frac{5-y^2}{4}\log y.
\]
If `y^2>=5` the right side is nonpositive.  Otherwise use
\[
\log y\le\frac{y-y^{-1}}2
\]
(which is `sinh(log y)>=log y`) and
\[
(5-y^2)(y+1)\le8\qquad(y\ge1);
\]
the last function has equality at `y=1` and decreases thereafter.

### Odd `N`

Let `N=2m+1`, `h=1/N`.  Monotone integral comparison gives
\[
D_N=\sum_{k=m+1}^{N}k^{-1/2}
\le2(\sqrt N-\sqrt m)
=2\sqrt N\left(1-2^{-1/2}\sqrt{1-h}\right).
\tag{L-90005.9}
\]
Also
\[
K_N/\sqrt N=4\sqrt N(a+2^{-1/2}h).
\]
By (L-90005.8), it is enough to compare the right side of (L-90005.9) with
\[
2\sqrt N(a+2^{-1/2}h)(1-h/4).
\]
Using
\[
\sqrt{1-h}\ge1-h/2-h^2/2\qquad(0\le h\le1)
\]
(the squared difference is `h^2(h-1)(h+3)/4<=0`), the gap after division by `2 sqrt(N)` is at least
\[
h\left(\frac1{2\sqrt2}-\frac a4-\frac{3h}{4\sqrt2}\right)>0
\qquad(h\le1/3).
\tag{L-90005.10}
\]
Thus (L-90005.7) is positive for every odd `N>=3`.

### Even `N`

Let `N=2m`, `h=1/N`.  Convexity of `x^(-1/2)` and midpoint Jensen give
\[
D_N\le\int_{m+1/2}^{2m+1/2}x^{-1/2}dx
=2\sqrt N\left(\sqrt{1+h/2}-2^{-1/2}\sqrt{1+h}\right).
\tag{L-90005.11}
\]
Here `K_N/sqrt(N)=4 sqrt(N)a`.  For `h<=1/8`, (L-90005.8) reduces the needed inequality to
\[
\sqrt{1+h/2}-2^{-1/2}\sqrt{1+h}<a(1-h/4).
\tag{L-90005.12}
\]
Use
\[
\sqrt{1+h/2}\le1+h/4,
\qquad
\sqrt{1+h}\ge1+h/2-h^2/8;
\]
the latter follows by squaring, since the excess is `h^3(h-8)/64<=0`.  The right-minus-left margin in (L-90005.12) is at least
\[
h\left(\frac{3\sqrt2-4}{8}-\frac{h}{8\sqrt2}\right)>0
\qquad(0<h\le1/8).
\tag{L-90005.13}
\]
Thus (L-90005.7) is positive for every even `N>=8`.  The three remaining even increments `N=2,4,6` are direct substitutions in (L-90005.7) and are positive.

Therefore
\[
\boxed{Q_{N+1}>Q_N\quad\text{for every }N\ge2.}
\tag{L-90005.14}
\]

Directed high-precision brackets (used only to avoid printing several lines of rational log bounds) are
\[
Q_7\in(-0.004857,-0.004856),
\qquad
Q_8\in(0.032916,0.032918).
\tag{L-90005.15}
\]
For the only cells where concavity could create an interior positive bump while both endpoints are negative, direct substitution at `x_N^*=2D_N/K_N` gives
\[
\max P_2<-0.1960,\qquad
\max P_4<-0.0684,\qquad
\max P_6<-0.0043.
\tag{L-90005.16}
\]
For `N=3,5,7`, `x_N^*` lies to the left of the cell, so `P_N` is decreasing there.  Consequently cells `N<=6` are strictly negative, cells `N>=8` strictly positive, and cell `N=7` has exactly one zero.  This proves (L-90005.2).  Bisection of the explicit monotone `P_7` gives (L-90005.1); e.g.
\[
0.14085203501383<c_*<0.14085203501385.
\tag{L-90005.17}
\]
All finite inequalities in (L-90005.15)--(L-90005.17) have margins far larger than the displayed brackets and admit routine rational certification via the positive `atanh` series for logarithms.

## 4. Exact finite shell as a secant perturbation

Now take even `X`, `Y=X/2`, an integer `2<=q<=Y`, and put
\[
\lambda=X/q,\qquad h=1/q,\qquad N=\lfloor\lambda\rfloor,
\qquad M=\lfloor N/2\rfloor.
\]
Define the zero-extended scaled seed
\[
f_\lambda(x)=2\sqrt x\left(\log\frac\lambda x-2\left(1-\sqrt{x/\lambda}\right)\right)
\quad(0<x\le\lambda),
\]
with `f_lambda(x)=0` for `x>=lambda`, and the dyadic shell
\[
d_\lambda(x)=f_\lambda(x)-f_{\lambda/2}(x).
\]
Because `b_X(qx)=sqrt(q) f_lambda(x)`, the exact finite definition gives
\[
\boxed{
\sqrt q\,s_X(q)
=\frac1h\sum_{k=1}^{N}[d_\lambda(k)-d_\lambda(k+h)]-\log2.}
\tag{L-90005.18}
\]
On the other hand the continuum profile is exactly
\[
\boxed{
\sqrt{q/X}\,E_{1/2}(q/X)
=\sum_{k=1}^{N}[-d_\lambda'(k)]-\log2.}
\tag{L-90005.19}
\]
Subtracting, define the floor correction
\[
\mathcal C=\sqrt q\,s_X(q)-P_N(\sqrt{q/X}).
\]
For each sampled interval
\[
R_k=d_\lambda'(k)-\frac{d_\lambda(k+h)-d_\lambda(k)}h
=-\frac1h\int_0^h(h-t)d_\lambda''(k+t)dt,
\qquad \mathcal C=\sum_kR_k.
\tag{L-90005.20}
\]
The two curvatures are exceptionally simple:
\[
d_\lambda''(x)=-\frac{\log2}{2x^{3/2}}\quad(x<\lambda/2),
\tag{L-90005.21}
\]
\[
d_\lambda''(x)=\frac{\log(x/\lambda)+2}{2x^{3/2}}
\quad(\lambda/2<x<\lambda),
\qquad 0<d_\lambda''(x)\le x^{-3/2}.
\tag{L-90005.22}
\]
Moreover `lambda/2=Y/q` and `lambda=X/q` have fractional parts that are integer multiples of `h=1/q`.  Hence no interval `[k,k+h]` straddles either curvature boundary in its interior.  This is the discrete fact that makes the transfer clean.

A lower-half interval therefore satisfies
\[
\frac{h\log2}{4}(k+h)^{-3/2}\le R_k
\le\frac{h\log2}{4}k^{-3/2},
\tag{L-90005.23}
\]
and an upper-half interval satisfies
\[
-\frac h2 k^{-3/2}\le R_k\le0.
\tag{L-90005.24}
\]

## 5. Positivity for every `N>=8`

If `q` does not divide `Y`, the lower intervals are `k=1,...,M` and the upper intervals are `k=M+1,...,N`.  Since `h<=1/2`, (L-90005.23)--(L-90005.24) give
\[
\frac{\mathcal C}{h}\ge
\frac{\log2}{4}\sum_{k=1}^{M}(k+1/2)^{-3/2}
-\frac12\sum_{k=M+1}^{N}k^{-3/2}.
\tag{L-90005.25}
\]
For `N<=2M+1`, integral comparison bounds the right side from below by
\[
F(M)=\frac{\log2}{2}\left(\sqrt{\frac23}-\frac1{\sqrt{M+3/2}}\right)
-\left(\frac1{\sqrt{M+1/2}}-\frac1{\sqrt{2M+3/2}}\right).
\tag{L-90005.26}
\]
For `M>=5`, `F(M)>0`: `F(5)>0.0155`, and
\[
F'(M)=\frac{\log2}{4}(M+3/2)^{-3/2}
+\frac12(M+1/2)^{-3/2}-(2M+3/2)^{-3/2}>0.
\]
The remaining cases `N=8,9` are direct in (L-90005.25); the respective lower margins are `>0.0067` and `>0.0364` (for `N=8` the integral bound may be used directly).

If `q|Y`, then `lambda=N=2M` is an even integer.  The lower intervals are `1,...,M-1`; the upper intervals are `M,...,2M-1`; the top interval at `2M` contributes exactly zero.  The same integral argument gives `F(M-1)>0` for `M>=6`; `N=10` is directly positive.  At the sole exceptional estimate `N=8`,
\[
\mathcal C/h>-0.003612,
\]
so, because `h<=1/2` and `P_8>=Q_8>0.032916`, one still has `sqrt(q)s_X(q)>0.031`.

Thus
\[
\boxed{N=\lfloor X/q\rfloor\ge8\Longrightarrow s_X(q)>0}
\tag{L-90005.27}
\]
for every even `X` and every `q>=2`.

## 6. The transition cell and the negative cells

On the `N=7` cell, `P_7` is decreasing and
\[
\frac{dP_7}{d\theta}\le-1.7
\qquad(1/8\le\theta\le c_*),
\tag{L-90005.28}
\]
(the exact value at `1/8`, where the magnitude is smallest, is `-1.730568...`).  In this cell the lower indices are `1,2,3` and upper indices `4,5,6,7`, so (L-90005.23)--(L-90005.24) give
\[
-0.169h<\mathcal C<0.268h.
\tag{L-90005.29}
\]
Since `q>X/8`, `h<8/X`.  Therefore
\[
q\le c_*X-1\Longrightarrow
P_7\ge1.7/X,\quad \mathcal C>-1.352/X,
\]
which is positive after addition.  This proves the first implication in (L-90005.3), together with (L-90005.27).

For `N<=6`, (L-90005.16) gives the uniform continuum margin
\[
P_N<-0.0043.
\]
Only lower intervals can raise the secant correction, and by (L-90005.23)
\[
\mathcal C<0.268h<\frac{1.876}{X}
\qquad(N\le6).
\tag{L-90005.30}
\]
Hence `s_X(q)<0` on all `N<=6` cells once `X>=438`.  On `N=7`, (L-90005.28)--(L-90005.29) already give negativity whenever `q>=c_*X+2`.

Finally, if even `X<438`, then
\[
c_*X+158>X/2,
\]
so there is no integer `q<=Y` satisfying the second antecedent of (L-90005.3).  This proves the negative implication globally, without a finite computer check.

## 7. Removing the `z`-maximum on even endpoints

Outside the integer window
\[
\mathcal W_X=\{q: c_*X-1<q<c_*X+158\}
\]
all exact shell weights have a single sign: positive below, negative above.  The window contains at most 159 integers.  For large `X` it lies inside the `N=7` neighborhood; (L-90005.20)--(L-90005.24) and (L-90005.28) then give uniformly
\[
\max_{q\in\mathcal W_X}|s_X(q)|\ll X^{-3/2}.
\tag{L-90005.31}
\]
The finitely many smaller `X` are absorbed into the constant.

As the tail threshold `z` moves upward through primes below the window it removes nonnegative terms and can only decrease `T_X(z)`; above the window it retains only nonpositive terms and cannot create a positive maximum.  Therefore the only possible change from the `z=2` value is caused by primes in `mathcal W_X`:
\[
0\le B_X-[T_X(2)]_+
\le\sum_{p\in\mathcal W_X}(\log p)|s_X(p)|
\ll X^{-3/2}\log(2X).
\]
This proves (L-90005.4).

## 8. Boundary and next target

This closes the deterministic `z`-collapse mechanism on exact dyadic/even endpoints.  It does **not** estimate the surviving scalar
\[
T_X(2)=\sum_{p\le X}(\log p)s_X(p),
\]
which `T-90001` identifies, after dyadic telescope/Stirling, with the one-sided prime-ramp deficit.  Thus the next RH-bearing task is no longer a max-over-tails geometry problem: it is the single endpoint scalar itself.

Two natural follow-ups are:

1. extend (L-90005.3) from even `X` to `Y=floor(X/2)` with the same bounded transition by a one-step endpoint perturbation estimate; and
2. attack `T_X(2)` directly, or equivalently the zero-safe low-row scalar isolated in PR #326.

No claim of RH or WSTS is made here.