# L-27904 — Cofinal finite dyadic shell-crossing rigidity

Claim ID: `L-27904`  
Title: Every sufficiently large finite dyadic shell residual has one sign crossing, with transition ratio converging to the unique continuum interface  
Status: **PROPOSED COMPLETE ANALYTIC THEOREM — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-08  
Frozen parent: PR #276 at `a65a02b9463c1cc3a10d0af03ab359a637e357cd`  
Dependencies: `L-27901`, `L-27902`; elementary Euler–Maclaurin and Hurwitz-zeta estimates  
Scope: finite shell sign order; no estimate of the total weighted shell and no RH conclusion

## 1. Statement

For an integer `X>=4`, put

\[
Y=\lfloor X/2\rfloor
\]

and

\[
s_X(q)
=r_X(q)-\mathbf1_{q\le Y}r_Y(q),
\qquad 2\le q\le X.
\tag{L-27904.1}
\]

Then there is an integer `X_0` such that, for every `X>=X_0`, one can choose an integer threshold `q_*(X)` with

\[
\boxed{
 s_X(q)>0\quad(2\le q<q_*(X)),
}
\tag{L-27904.2}
\]

and

\[
\boxed{
 s_X(q)\le0\quad(q_*(X)\le q\le X).
}
\tag{L-27904.3}
\]

Moreover

\[
\boxed{
{q_*(X)\over X}\longrightarrow
\theta_*=0.1408520350138\ldots,
}
\tag{L-27904.4}
\]

where `theta_*` is the unique zero of `L-27901`.

This is `FSCR` from `T-27901`.

## 2. Uniform finite-to-continuum formula

Let

\[
c_X=Y/X.
\]

`L-27902` proves

\[
\boxed{
 s_X(q)
=X^{-1/2}E_{c_X}(q/X)
+\varepsilon_X(q),
\qquad
|\varepsilon_X(q)|\le Cq^{-3/2},}
\tag{L-27904.5]
\]

with one absolute constant and every `2<=q<=X`. Here

\[
E_c(\theta)
=E(\theta)-c^{-1/2}E(\theta/c)
 \mathbf1_{\theta\le c}.
\]

The closing bracket in tag (L-27904.5) is typographical only.

Since

\[
c_X=1/2+O(1/X),
\tag{L-27904.6}
\]

the functions `E_(c_X)` and their first two derivatives converge uniformly to the dyadic defect `D=E_(1/2)` on every closed reciprocal cell away from zero.

## 3. A normalized positive moat down to zero

Put

\[
K(\theta)=\sqrt\theta\,D(\theta).
\]

The reciprocal-cell Euler expansions

\[
S_N=2\sqrt N+\zeta(1/2)+O(N^{-1/2}),
\]

and

\[
A_N
=2\sqrt N\log N-4\sqrt N-\zeta'(1/2)
+O(N^{-1/2}\log N)
\]

in the exact formula of `L-27901` give

\[
\boxed{
\lim_{\theta\downarrow0}K(\theta)
=-(\zeta(1/2)+1)\log2.}
\tag{L-27904.7}
\]

The value is positive. Indeed

\[
\eta(1/2)=(1-\sqrt2)\zeta(1/2),
\]

and the eighth even partial sum of the alternating eta series is already larger than `sqrt(2)-1`; hence `zeta(1/2)<-1`.

By `L-27901`, `D(theta)>0` on `(0,1/8]`. Equation (L-27904.7) makes `K` continuous and positive on the compact interval `[0,1/8]`. Therefore

\[
\boxed{
\kappa:=\min_{0\le\theta\le1/8}K(\theta)>0.}
\tag{L-27904.8}
\]

Uniform convergence in `c_X` gives, for all sufficiently large `X`,

\[
E_{c_X}(\theta)
\ge{\kappa\over2\sqrt\theta}
\qquad(0<\theta\le1/8).
\tag{L-27904.9}
\]

Combining (L-27904.5) and (L-27904.9),

\[
s_X(q)
\ge{\kappa\over2\sqrt q}-{C\over q^{3/2}}.
\tag{L-27904.10}
\]

Thus there is one absolute integer `Q` such that

\[
\boxed{
q>=Q,\quad q/X<=1/8
\Longrightarrow s_X(q)>0}
\tag{L-27904.11}
\]

for every sufficiently large `X`.

## 4. Every fixed low coordinate is eventually positive

It remains to treat the finite set `2<=q<Q`.

For the exact half shell, decompose the continuum derivative near zero as

\[
g_{1/2}(u)=-(\log2)u^{-1/2}+h(u),
\]

where `h` has bounded variation on `[0,1]` and

\[
\int_0^1g_{1/2}(u)du=0.
\]

For fixed `q`, Euler summation with the shifted lattice `k+t/q` gives

\[
\boxed{
\lim_{X\to\infty}s_X(q)
=-{\log2\over\sqrt q}
\left[
1+\int_0^1
\zeta\!\left({1\over2},1+{t\over q}\right)dt
\right].}
\tag{L-27904.12}
\]

The estimate is uniform for `q` in any fixed finite set. A direct proof uses

\[
\sum_{k=1}^{N}(k+a)^{-1/2}
=2\sqrt{N+a}
+\zeta(1/2,1+a)+O(N^{-1/2})
\]

uniformly for `a` in a compact interval; the leading square-root term cancels against the bounded-variation part because the complete shell derivative has integral zero.

For `a>=1`,

\[
{\partial\over\partial a}\zeta(1/2,a)
=-{1\over2}\zeta(3/2,a)<0.
\]

Hence

\[
\zeta(1/2,1+t/q)
\le\zeta(1/2)<-1.
\]

The bracket in (L-27904.12) is strictly negative, and therefore

\[
\boxed{
\lim_{X\to\infty}s_X(q)>0
\qquad(q\ge2\text{ fixed}).}
\tag{L-27904.13}
\]

Since only finitely many `q<Q` remain, there is one common threshold beyond which all of them are positive.

Combining with Section 3,

\[
\boxed{
s_X(q)>0
\qquad(2\le q\le X/8)}
\tag{L-27904.14}
\]

for every sufficiently large `X`.

## 5. The transition cell is strictly decreasing

On the reciprocal cell

\[
1/8<q/X<1/7,
\]

one has

\[
\lfloor X/q\rfloor=7,
\qquad
\lfloor Y/q\rfloor=3
\]

for all sufficiently large endpoints, with the boundary convention handled separately.

Extend the exact finite shell formula to a real variable `x` inside this cell by retaining the seven source differences and the three lower-endpoint differences. Differentiating the integral form used in `L-27902` gives

\[
\boxed{
X^{3/2}{d\over dx}s_X(x)
=D'(x/X)+O(1/X),}
\tag{L-27904.15}
\]

uniformly across the cell. The error follows from the bounded second derivative of the shell profile there:

\[
{d\over dx}\varepsilon_X(x)
=O(x^{-5/2}).
\]

`L-27901` gives

\[
\max_{1/8\le\theta\le1/7}D'(\theta)<0.
\tag{L-27904.16}
\]

Therefore the exact finite shell sequence is strictly decreasing throughout quotient cell seven once `X` is sufficiently large.

Its left endpoint is positive by (L-27904.14). Its right endpoint is negative by Section 6 below. Thus it has exactly one integer sign transition, and the uniform convergence gives

\[
q_*(X)/X\to\theta_*.
\]

## 6. The upper sector is nonpositive

On each compact reciprocal cell `N=2,...,6`, `L-27901` supplies a strict negative continuum moat. Equation (L-27904.5), with `q` comparable to `X`, shows

\[
\boxed{
s_X(q)<0
\qquad(1/7\le q/X\le1/2)}
\tag{L-27904.17}
\]

for every sufficiently large `X`.

For `q>X/2`, the lower endpoint is absent and `s_X(q)=r_X(q)`. Put

\[
b_X(t)=2\sqrt t[\log(X/t)-2(1-\sqrt{t/X})].
\]

On `[X/2,X]`,

\[
-b_X'(t)
={4-\log(X/t)\over\sqrt t}-{4\over\sqrt X}
\]

is decreasing. Hence

\[
b_X(q)-b_X(q+1)
\le -b_X'(q).
\]

The elementary inequality

\[
\log(X/q)
\ge2(1-\sqrt{q/X})
\]

then gives

\[
-b_X'(q)
\le {\log(X/q)\over\sqrt q}.
\]

Therefore

\[
\boxed{s_X(q)=r_X(q)\le0
\qquad(q>X/2),}
\tag{L-27904.18}
\]

including the zero endpoint `q=X`.

## 7. Conclusion

Sections 3--6 prove a positive lower sector, one strictly decreasing transition cell, and a nonpositive upper sector. Hence (L-27904.2)--(L-27904.4) follow.

The proof is cofinal and uses no finite sign scan. The committed reconnaissance remains useful only as an independent mutation check.

## 8. Proof boundary

Closed here, subject to review:

- the normalized positive moat at ratio zero;
- eventual positivity of every fixed coordinate;
- uniform positivity of the remaining low-ratio bulk;
- strict finite monotonicity in quotient cell seven;
- the negative upper sector;
- cofinal `FSCR` and convergence of its crossing ratio.

Open:

- the sign or subpower size of the complete logarithmically weighted shell;
- `EPD` or its dyadic weakening;
- WSTS and RH.
