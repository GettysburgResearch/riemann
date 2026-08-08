# L-30901 — The first activated boundary has logarithmic central-flow debt

Claim ID: `L-30901`  
Title: The complete stopped-power boundary has linear divisor-source atomic norm but only `O(log X)` weighted first-difference debt in its native central-flow coordinate  
Status: **PROPOSED COMPLETE ELEMENTARY THEOREM — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-08  
Frozen parent: PR #305 at `df3cbe232b5fea3aea4e7b385148bf8f1e52a58b`  
Dependencies: PR #305 `L-30501/L-30502`; the exact central residual identity of PR #280; elementary calculus  
Scope: complete first aggregate boundary and one exact central packing stage; no all-generation recurrence or RH conclusion

## 1. Complete first boundary

Put

\[
 p(x)=x^{-1/2},
 \qquad
 w_X(x)=x^{-1/2}\log(X/x)\mathbf1_{x\le X},
\]

and let

\[
 (\mathscr Cf)(q)
 =\sum_{k\ge1}
 \left[f(2kq-1)-f((2k+1)q)\right].
\tag{L-30901.1}
\]

For

\[
2\le q\le M:=\left\lfloor\frac{X+1}{2}\right\rfloor,
\]

PR #305 proves that the complete first activated cutoff boundary is

\[
\boxed{
 b_X(q)
 =\log\frac{X}{2q-1}\,\mathscr Cp(q)
 -\mathscr Cw_X(q).
}
\tag{L-30901.2}

Set `b_X(M+1)=0`.

PR #305 proves that the unique divisor source of this boundary has atomic norm
`Omega(X)`.  The present theorem retains the boundary in the column/flow
coordinate in which it was produced.

## 2. Exact paired representation

For real `q>=2`, put

\[
 c=2q-1,
 \qquad
 a_k=2kq-1,
 \qquad
 d_k=(2k+1)q,
\]

and define

\[
 \Psi_X(x,c)
 =x^{-1/2}\log\frac{\min(x,X)}c,
 \qquad x\ge c.
\tag{L-30901.3}

Then the complete boundary has the exact absolutely paired representation

\[
\boxed{
 b_X(q)
 =\sum_{k\ge1}
 \left[
  \Psi_X(a_k,c)-\Psi_X(d_k,c)
 \right].
}
\tag{L-30901.4
}

### Proof

Write

\[
L=\log(X/c).
\]

For one shifted-even argument `a`, its contribution to (L-30901.2) is

\[
 a^{-1/2}
 \left[L-\mathbf1_{a\le X}\log(X/a)\right]
 =a^{-1/2}\log\frac{\min(a,X)}c.
\]

The odd argument has the same formula with the opposite sign.  Summing the
already paired even/odd terms proves (L-30901.4).

For large `k` both arguments exceed `X`; the pair is then

\[
 \log(X/c)\,[a_k^{-1/2}-d_k^{-1/2}]
 =O\left(q^{-1/2}k^{-3/2}\log(X/c)\right),
\]

so the paired series converges absolutely.

## 3. Differential bounds for one pair

Away from `x=X`, the partial derivatives are

\[
 \partial_c\Psi_X(x,c)=-\frac1{c\sqrt x},
\tag{L-30901.5}
\]

and

\[
 |\partial_x\Psi_X(x,c)|
 \le
 x^{-3/2}\left[1+\frac12\log(x/c)\right].
\tag{L-30901.6}
\]

On each side of `x=X`,

\[
 |\partial_x^2\Psi_X(x,c)|
 \le
 2x^{-5/2}[1+\log(x/c)].
\tag{L-30901.7}
\]

The first derivative has one jump of magnitude exactly `X^(-3/2)` at `x=X`.

Let

\[
 P_k(q)=\Psi_X(a_k,c)-\Psi_X(d_k,c).
\]

Since

\[
 a_k'=2k,
 \qquad d_k'=2k+1,
 \qquad c'=2,
\]

one has, at every ordinary differentiability point,

\[
\begin{aligned}
 P_k'(q)={}&
 2k\,[\Psi_x(a_k,c)-\Psi_x(d_k,c)]
 -\Psi_x(d_k,c)\\
 &+2[\Psi_c(a_k,c)-\Psi_c(d_k,c)].
\end{aligned}
\tag{L-30901.8}

For `q>=2`,

\[
 a_k\ge kq,
 \qquad
 d_k-a_k=q+1\le\frac32q,
 \qquad
 c\ge\frac32q,
\tag{L-30901.9}
\]

and

\[
 \log(d_k/c)\le\log(2k+1).
\tag{L-30901.10}

Equations (L-30901.5)--(L-30901.10), followed by the mean-value theorem, give

\[
 |P_k'(q)|
 \le
 Cq^{-3/2}k^{-3/2}[1+\log(2k+1)]
 +2kX^{-3/2}\mathbf1_{a_k<X<d_k}
\tag{L-30901.11}

for one absolute constant `C`.

The intervals `[a_k,d_k]` are disjoint.  Thus, for fixed `q`, at most one index
can contribute the cutoff-jump term.  For that index,

\[
 k\le\frac{X+1}{2q},
\]

so

\[
 2kX^{-3/2}\le\frac{2}{q\sqrt X}.
\tag{L-30901.12}

Because

\[
 \sum_{k\ge1}k^{-3/2}[1+\log(2k+1)]<\infty,
\]

termwise differentiation of the paired series is legitimate on every compact
subinterval away from its finitely many cutoff kinks, and

\[
\boxed{
 |b_X'(q)|
 \le
 C_1q^{-3/2}+\frac{C_2}{q\sqrt X}
}
\tag{L-30901.13}

for absolute constants `C_1,C_2`.  The function itself is continuous at every
cutoff kink, so no variation atom is omitted.

## 4. Logarithmic weighted variation

For every integer `2<=n<=M-1`, absolute continuity between consecutive cutoff
kinks gives

\[
 |b_X(n+1)-b_X(n)|
 \le
 \int_n^{n+1}|b_X'(q)|dq.
\]

Using (L-30901.13),

\[
\begin{aligned}
 &\sum_{n=2}^{M-1}
 \sqrt n\,|b_X(n+1)-b_X(n)|\\
 &\qquad\le
 C_1\sum_{n=2}^{M-1}\frac1n
 +\frac{C_2}{\sqrt X}
  \sum_{n=2}^{M-1}\frac1{\sqrt n}\\
 &\qquad=O(\log(2X)).
\end{aligned}
\tag{L-30901.14}

The final endpoint term is also bounded.  Indeed `2M-1>=X-1`, so the exact
formula contains only a bounded number of active arguments and gives

\[
 \sqrt M\,|b_X(M)|=O(1).
\tag{L-30901.15}

Therefore

\[
\boxed{
 \mathcal V_X(b)
 :=\sum_{n=2}^{M}
 \sqrt n\,|b_X(n)-b_X(n+1)|
 =O(\left(1+\log X\right)).
}
\tag{L-30901.16
}

This is the norm separation promised by PR #305: the divisor-source value norm
is linear, while the native central first-difference norm is logarithmic.

## 5. Exact first-generation signed flow

Define the central first-difference flow

\[
 d_X^{\partial}(n)
 =b_X(n)-b_X(n+1)
\tag{L-30901.17}

on the split

\[
 [n,\lfloor n/2\rfloor].
\]

The exact central residual identity gives

\[
\boxed{
 L_q(d_X^{\partial})
 =b_X(q)-(\mathcal T_Mb_X)(q),
}
\tag{L-30901.18}

where

\[
 (\mathcal T_Mb)(q)
 =\sum_{k\ge1}
 [b(2kq-1)-b((2k+1)q)]
\]

with zero extension beyond `M`.

Every central split is uniformly balanced, and its capacity weight obeys

\[
 \omega_n\le2\sqrt n.
\]

Consequently its negative capacity debt satisfies

\[
\begin{aligned}
 \mathcal N_\omega(d_X^{\partial})
 &\le
 2\sum_{n=2}^{M}
 \sqrt n\,[b_X(n+1)-b_X(n)]_+\\
 &\le2\mathcal V_X(b).
\end{aligned}
\]

Hence

\[
\boxed{
 \mathcal N_\omega(d_X^{\partial})
 =O(1+\log X).
}
\tag{L-30901.19}

This is a complete proof-producing first-generation boundary certificate.  No
reviewer reconstruction, source inversion, or finite numerical extrapolation is
being requested.

## 6. What remains after this theorem

The boundary has not yet been saturated completely: the exact lower-scale
residual is `T_M b_X`.  A full proof must establish a recurrence for the same
coupled variation/debt norm along the support-halving residual chain.

The present theorem removes the first macroscopic obstruction and proves that
the linear atomic source is an artifact of the wrong coordinate.  It does not
assert the all-generation recurrence.

## 7. Proof boundary

Closed here:

1. the exact paired representation of the complete activated boundary;
2. a uniform derivative estimate including every cutoff crossing;
3. logarithmic weighted discrete variation;
4. an explicit signed balanced central flow;
5. logarithmic first-generation negative capacity debt;
6. exact export of only the strict half-scale residual.

Open:

1. a uniform recurrence for the exported residuals;
2. polylogarithmic all-generation Cycle Debt;
3. the sharp prime ramp and RH.
