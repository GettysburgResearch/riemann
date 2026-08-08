# L-30409 — The complete Selberg hierarchy is coefficientwise nonnegative at every order

Claim ID: `L-30409`  
Title: Every generalized coefficient `mu*(1 log^r)` is nonnegative, admits a positive recursion, and vanishes exactly below its squarefree rank  
Status: **PROPOSED COMPLETE EXACT THEOREM — INDEPENDENT REVIEW REQUESTED**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-08  
Dependencies: elementary divisor algebra  
Scope: all-order coefficient positivity and moment hierarchy; no asymptotic bound or RH conclusion

## 1. Generalized Selberg coefficients

For an integer `r>=0`, define

\[
\boxed{
C_r(n)
=[\mu*(\mathbf1\log^r)](n)
=\sum_{d\mid n}\mu(d)
 \left(\log{n\over d}\right)^r.}
\tag{L-30409.1}
\]

Use the convention `0^0=1` in the zeroth convolution. Thus

\[
C_0=\varepsilon,
\qquad
C_1=\Lambda,
\qquad
C_2=\Lambda\log+\Lambda*\Lambda.
\tag{L-30409.2}
\]

## 2. Exponential generating function

For every fixed integer `n`, finite divisor summation gives

\[
\begin{aligned}
\sum_{r=0}^\infty C_r(n){t^r\over r!}
&=\sum_{d\mid n}\mu(d)(n/d)^t\\
&=n^t\prod_{p\mid n}(1-p^{-t}).
\end{aligned}
\tag{L-30409.3}
\]

If

\[
n=\prod_{j=1}^k p_j^{a_j},
\qquad k=\omega(n),
\]

then

\[
\boxed{
 n^t\prod_{p\mid n}(1-p^{-t})
 =\prod_{j=1}^k
 \left[e^{a_j(\log p_j)t}
       -e^{(a_j-1)(\log p_j)t}\right].}
\tag{L-30409.4}
\]

For every `a>=1` and `L>0`,

\[
e^{aLt}-e^{(a-1)Lt}
=\sum_{r=1}^\infty
 {L^r[a^r-(a-1)^r]\over r!}t^r,
\tag{L-30409.5}
\]

and every displayed coefficient is strictly positive.

## 3. Complete positivity and rank support

Products of power series with nonnegative coefficients have nonnegative
coefficients. Equations (L-30409.3)--(L-30409.5) therefore prove

\[
\boxed{C_r(n)\ge0\qquad(r\ge0,n\ge1).}
\tag{L-30409.6}
\]

More precisely, every nontrivial factor in (L-30409.4) has zero constant term
and positive coefficients in all positive degrees. Hence

\[
\boxed{
C_r(n)=0\quad(r<\omega(n)),
\qquad
C_r(n)>0\quad(r\ge\omega(n)).}
\tag{L-30409.7}
\]

For `r=2`, this says that only prime powers and products of two distinct primes
can appear, matching the linear-plus-semiprime Selberg square. Higher orders add
exactly the squarefree ranks licensed by `r`.

## 4. Positive coefficient recursion

Let

\[
\mathcal C_r(s)=\sum_{n\ge1}{C_r(n)\over n^s}
={(-1)^r\zeta^{(r)}(s)\over\zeta(s)}
\tag{L-30409.8}
\]

in the absolute-convergence half-plane. Put

\[
D(s)=-{\zeta'(s)\over\zeta(s)}
=\sum_{n\ge1}{\Lambda(n)\over n^s}.
\]

Differentiation gives

\[
\mathcal C_{r+1}=D\mathcal C_r-\mathcal C_r'.
\tag{L-30409.9}
\]

Therefore, coefficientwise,

\[
\boxed{
C_{r+1}(n)
=C_r(n)\log n+(\Lambda*C_r)(n).}
\tag{L-30409.10}
\]

Starting from `C_0=epsilon`, this is a recursion using only nonnegative
operations. It supplies an independent inductive proof of (L-30409.6).

The first two nontrivial rows are

\[
C_1=\Lambda,
\tag{L-30409.11}
\]

\[
C_2=\Lambda\log+\Lambda*\Lambda,
\tag{L-30409.12}
\]

and

\[
\boxed{
\begin{aligned}
C_3={}&\Lambda(\log)^2
+3(\Lambda*(\Lambda\log))
+\Lambda*\Lambda*\Lambda.
\end{aligned}}
\tag{L-30409.13}
\]

The coefficient `3` follows by applying (L-30409.10) and the logarithmic
Leibniz identity for convolution.

## 5. Positive integral representation

Each factor also has the representation

\[
e^{aLt}-e^{(a-1)Lt}
=tL\int_{a-1}^{a}e^{uLt}\,du.
\tag{L-30409.14}
\]

Consequently, for `n>1`,

\[
\boxed{
\begin{aligned}
&n^t\prod_{p\mid n}(1-p^{-t})\\
&\quad=t^{\omega(n)}
\left(\prod_{p\mid n}\log p\right)
\int_{\prod_{p^a\Vert n}[a-1,a]}
 e^{t\sum_{p^a\Vert n}u_p\log p}\,d\mathbf u.
\end{aligned}}
\tag{L-30409.15}
\]

Thus `C_r(n)` is a positive mixed logarithmic moment of one explicit box. This
representation records all product collisions automatically and contains no
alternating Möbius sign after recombination.

## 6. All-order Möbius–Riesz moments

For the state of `L-30408`,

\[
\mathcal F_r(N)
=\sum_{m\le N}\mathfrak M_N(m)(\log m)^r,
\]

one has exactly

\[
\boxed{
\mathcal F_r(N)
=\sum_{n\le N}{C_r(n)\over\sqrt n}\ge0.}
\tag{L-30409.16}
\]

The parity-boundary recurrence of `L-30408.12` therefore has a complete positive
source coordinate at **every** logarithmic order, not only at orders one and
two.

## 7. Consequence for reflected proof design

The theorem supplies a canonical high-order replacement for informal phrases
such as “the higher Selberg terms are positive.” A production reflected
certificate may use the hierarchy

\[
C_{r+1}=C_r\log+\Lambda*C_r
\]

while preserving:

- every prime-power layer;
- every product collision;
- the exact squarefree-rank support;
- coefficientwise positivity;
- the strict dyadic source coefficient `rho_2` from `L-30407`.

What positivity does **not** do by itself is control the signed first boundary
moment. A valid proof still needs a correctly typed physical Schur or recurrence
which converts the positive hierarchy into a bound without deleting the
half-pole source.

## 8. Proof boundary

Proved exactly here:

- the exponential generating function;
- coefficientwise nonnegativity at every order;
- exact squarefree-rank support;
- the positive Selberg recursion;
- the positive box-moment representation;
- nonnegativity of every Möbius–Riesz logarithmic moment.

Not proved here:

- a physical inequality relating different orders;
- a subpower first-moment recurrence;
- Cycle Debt, WSTS, or RH.
