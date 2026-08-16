# L-94051 — The Q4 adjoint square removes two powers of the critical prime saddle per level

Claim ID: `L-94051`  
Status: **PROPOSED COMPLETE UNCONDITIONAL ESTIMATE — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-16  
Depends on: `L-94050`; the elementary Chebyshev bound `psi(x) << x`; the standard Stirling lower bound for the archimedean density  
Scope: pointwise phase-blind prime envelope and gamma reserve for the filtered scalar; no signed cancellation theorem

## 1. A shell lemma

Let \(g\in C^1(\mathbb R)\) and assume

\[
G(u)=e^{u/2}g(u)
\]

belongs to \(W^{1,1}(\mathbb R)\). The elementary Chebyshev estimate

\[
\psi(y)\ll y
\tag{L-94051.1}
\]

implies

\[
\boxed{
\sum_{n\ge2}{\Lambda(n)\over\sqrt n}|g(\log n)|
 \ll \|G\|_{L^1}+\|G'\|_{L^1}.
}
\tag{L-94051.2}
\]

To prove this, split the integers into \(e^j\le n<e^{j+1}\). The total
von-Mangoldt mass in one shell is \(O(e^j)\), and

\[
e^{j/2}\sup_{j\le u\le j+1}|g(u)|
 \ll \sup_{j\le u\le j+1}|G(u)|.
\]

Summing the unit-interval Sobolev inequality gives (L-94051.2). This uses no
prime-number-theorem error estimate.

## 2. Fixed derivative bounds

Recall

\[
H_q(u)=e^{u/2}h_q(u)
 =e^{q/4}
  \left(1-{u^2\over2q}\right)
  e^{-(u-q)^2/(4q)}.
\tag{L-94051.3}
\]

For each integer \(r\ge0\), there is an effective constant \(A_r\) such that,
for every \(q\ge1\),

\[
\boxed{
\|H_q^{(r)}\|_1+\|H_q^{(r+1)}\|_1
 \le A_r e^{q/4}q^{3/2-r/2}.
}
\tag{L-94051.4}
\]

Indeed, set

\[
v={u-q\over2\sqrt q}.
\]

Then \(H_q\) is \(e^{q/4}e^{-v^2}\) times a quadratic polynomial whose
coefficients are \(O(q)\). Every fixed derivative is a finite combination of
Hermite polynomials times \(e^{-v^2}\), and the change of variables contributes
the displayed power of \(q\).

A uniform form sufficient for growing order is

\[
\boxed{
\|H_q^{(r)}\|_1+\|H_q^{(r+1)}\|_1
 \le A e^{q/4}q^{3/2-r/2}
       (A\sqrt{r+2})^{r+2}
}
\tag{L-94051.5}
\]

with one absolute effective constant \(A\). It follows from

\[
\int_{\mathbb R}|\operatorname{He}_k(v)|e^{-v^2}dv
 \le A^{k+1}\sqrt{k!}.
\tag{L-94051.6}
\]

by Cauchy–Schwarz and the exact Hermite \(L^2\) norm.

## 3. Finite-difference gain

For every \(r\ge1\),

\[
\|(I-T_L)^rF\|_{W^{1,1}}
 \le L^r\left(\|F^{(r)}\|_1+\|F^{(r+1)}\|_1\right).
\tag{L-94051.7}
\]

This is the repeated integral representation of a finite difference.
Moreover,

\[
\|(4I-T_{-L})^r\|_{L^1\to L^1}\le5^r.
\tag{L-94051.8}
\]

Combining (L-94050.16), (L-94051.4), and the shell lemma gives, for each fixed
integer \(m\ge0\),

\[
\boxed{
|S_m(q,x)|
 \le C_m e^{q/4}q^{3/2-m}
\qquad(q\ge1,\ x\in\mathbb R).
}
\tag{L-94051.9}
\]

The estimate is pointwise in the carrier. Cancellation is taken only inside the
explicit scale-four finite difference before absolute values.

For growing order, take \(r=2m\) in (L-94051.5). The factors
\(L^{2m}5^{2m}\), the Hermite term
\((A\sqrt{2m+2})^{2m+2}\), and the harmless extra polynomial factor in
\(m\) are absorbed into \((C_0m)^m\), using \(m\le2^m\). Hence one
absolute effective \(C_0\) satisfies, whenever

\[
1\le m\le q/C_0,
\]

\[
\boxed{
|S_m(q,x)|
 \le C_0 e^{q/4}q^{3/2}
 \left({C_0m\over q}\right)^m.
}
\tag{L-94051.10}
\]

The restriction on \(m\) is used only to keep the displayed ratio in the
finite-difference gain regime; all constants are independent of \(q,x,m\).

## 4. Gamma reserve

On the real line, \(P(u)^{2m}\ge1\). The archimedean density in the exact
explicit formula satisfies

\[
\mu(t)\ge c\log(2+|t|)-C.
\tag{L-94051.11}
\]

Restricting to \(|u|\le q^{-1/2}\), and bounding the remaining constant part by
\(P(u)^{2m}\le9^{2m}\), gives

\[
\boxed{
\operatorname{gamma}_m(q,x)
 \ge c_0q^{-3/2}\log(2+|x|)-C_mq^{-3/2}
}
\tag{L-94051.12}
\]

for \(|x|\ge2q^{-1/2}\). For growing order the error is

\[
C e^{C m}q^{-3/2}.
\tag{L-94051.13}
\]

## 5. Pole term

The two pole arguments lie in the closed strip \(|\Im u|\le1/2\), where

\[
|P(u)|\le10.
\]

Consequently

\[
\boxed{
|\operatorname{pole}_m(q,x)|
 \le C e^{Cm}(1+x^2)e^{-q(x^2-1/4)}.
}
\tag{L-94051.14}
\]

It is negligible in every high-centre regime below.

## 6. Exact pointwise positivity condition

Equations (L-94050.13), (L-94051.10), and (L-94051.12) imply positivity whenever

\[
\boxed{
{q\over4}-\log\log(2+|x|)
 +{3\over2}\log q
 -m\log {q\over C_0m}
 \longrightarrow-\infty,
}
\tag{L-94051.15}
\]

with

\[
m=o(\log\log(2+|x|)).
\tag{L-94051.16}
\]

All inputs in this condition are unconditional and phase blind. No zero-free
region, zero-density theorem, Selberg integral at macroscopic length, CPBD, or
RH estimate has entered.

## 7. Proof boundary

Established unconditionally:

1. Chebyshev shell transfer;
2. fixed and growing derivative bounds;
3. exact order-`2m` finite-difference gain;
4. pointwise filtered prime envelope;
5. filtered gamma reserve;
6. explicit positivity condition.

Not established:

1. a fixed positive improvement of the leading constant four;
2. signed carrier cancellation beyond the absolute envelope;
3. RH.
