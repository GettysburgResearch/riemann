# L-32405 — The all-order Selberg hierarchy resums to a Jordan-totient Hermitian square

Claim ID: `L-32405`  
Title: Exponentiating the complete positive Selberg hierarchy gives the positive Jordan source `zeta(s-tau)/zeta(s)`, and reflected subtraction is exactly the square of its nontrivial source  
Status: **PROPOSED COMPLETE EXACT ALGEBRAIC/ANALYTIC LEMMA — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-sol`  
Created: 2026-08-08  
Dependencies: the coefficient hierarchy `C_r=mu*(1 log^r)`; generalized reflected product algebra  
Scope: all-order resummation and reflected square; no bound for the resulting Jordan source

## 1. All-order coefficient hierarchy

For `r>=0`, define

\[
 C_r(n)=[\mu*(\mathbf1\log^r)](n).
\tag{L-32405.1}
\]

For a real parameter `tau>0`, exponential summation gives

\[
\begin{aligned}
 \sum_{r\ge0}{\tau^r\over r!}C_r(n)
 &=\sum_{d\mid n}\mu(d)
   \exp\!\left(\tau\log{n\over d}\right)\\
 &=\sum_{d\mid n}\mu(d)(n/d)^\tau.
\end{aligned}
\]

Define

\[
\boxed{
 J_\tau(n)
 =\sum_{d\mid n}\mu(d)(n/d)^\tau
 =n^\tau\prod_{p\mid n}(1-p^{-\tau}).
}
\tag{L-32405.2}
\]

Thus

\[
\boxed{
 J_\tau(n)
 =\sum_{r\ge0}{\tau^r\over r!}C_r(n).
}
\tag{L-32405.3}
\]

For every `tau>0`,

\[
\boxed{J_\tau(n)>0\qquad(n>=1).}
\tag{L-32405.4}
\]

For integer `tau=k`, this is the classical Jordan totient `J_k`.

## 2. Dirichlet series

Initially for `Re s>1+tau`, finite convolution gives

\[
\boxed{
 \sum_{n\ge1}{J_\tau(n)\over n^s}
 ={\zeta(s-\tau)\over\zeta(s)}.
}
\tag{L-32405.5}
\]

Equivalently, because

\[
 {(-1)^r\zeta^{(r)}(s)\over\zeta(s)}
 =\sum_n{C_r(n)\over n^s},
\]

Taylor's theorem resums the complete Selberg hierarchy:

\[
 \sum_{r\ge0}{\tau^r\over r!}
 {(-1)^r\zeta^{(r)}(s)\over\zeta(s)}
 ={\zeta(s-\tau)\over\zeta(s)}.
\tag{L-32405.6}
\]

Thus the positive coefficient hierarchy is not merely formal: its exact generating object is one shifted zeta quotient with positive arithmetic coefficients.

## 3. Independent reflected twists

For real independent `t,u`, put

\[
 J_{\tau,t}(n)=J_\tau(n)n^{-it},
 \qquad
 J_{\tau,-u}(n)=J_\tau(n)n^{iu}.
\]

Their Dirichlet series are

\[
 R_{\tau,t}(s)
 ={\zeta(s-\tau+it)\over\zeta(s+it)},
\]

and

\[
 R_{\tau,-u}(s)
 ={\zeta(s-\tau-iu)\over\zeta(s-iu)}.
\]

For the product reflected source, the ratio is the product of these two ratios. Hence the coefficient identity

\[
\boxed{
\begin{aligned}
 &J_{\tau,t}*J_{\tau,-u}
 -J_{\tau,t}
 -J_{\tau,-u}
 +\varepsilon\\
 &\qquad=
 (J_{\tau,t}-\varepsilon)
 *(J_{\tau,-u}-\varepsilon).
\end{aligned}}
\tag{L-32405.7}
\]

is tautological but crucial: every term has two arithmetic legs after subtraction.

## 4. Exact Hermitian square

On a real vertical line set `u=t`. Taking Dirichlet series in (L-32405.7) gives

\[
\boxed{
\begin{aligned}
 &{\zeta(\sigma-\tau+it)\zeta(\sigma-\tau-it)
    \over
    \zeta(\sigma+it)\zeta(\sigma-it)}\\
 &\quad-
 {\zeta(\sigma-\tau+it)\over\zeta(\sigma+it)}
 -{\zeta(\sigma-\tau-it)\over\zeta(\sigma-it)}+1\\
 &=\left|
 {\zeta(\sigma-\tau+it)\over\zeta(\sigma+it)}-1
 \right|^2.
\end{aligned}}
\tag{L-32405.8}
\]

Thus the **complete all-order reflected Selberg hierarchy is already a literal Hermitian square**. No packetwise Cauchy--Schwarz, source-cone lift, or missing unit-source leg is required at this algebraic level.

## 5. Relation to the finite-order identities

Expand both sides of (L-32405.8) in `tau` at zero. The coefficient of `tau^2` is the ordinary reflected Selberg square. The coefficient of `tau^3` is the reflected third-order differential identity, and all higher orders are fixed simultaneously.

The strict finite-row power reserves of `L-32402` are therefore one finite-order shadow of a much simpler all-order object.

## 6. New obstruction exposed by the resummation

The ratio (L-32405.5) has a real pole at

\[
 s=1+\tau
\]

coming from the numerator. That real pole lies to the right of every nontrivial denominator zero and is the Landau-compatible leading singularity of the positive coefficient series.

Therefore coefficient positivity alone cannot exclude denominator zeros. A physical RH criterion must cancel this declared real pole without canceling any zero of `zeta(s)` in the critical strip.

`T-32401` supplies one explicit compact safe filter for `tau=2` and records the resulting positive-source RH criterion.

## 7. Proof boundary

Closed exactly:

- positive Jordan coefficients and their generating formula;
- the shifted-zeta quotient;
- independent reflected source identity;
- the exact Hermitian square (L-32405.8);
- all-order resummation of the finite Selberg hierarchy.

Open:

- a subexponential physical energy estimate after the real pole is filtered;
- RH.
