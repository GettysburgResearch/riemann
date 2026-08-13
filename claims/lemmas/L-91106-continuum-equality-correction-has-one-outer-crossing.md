# L-91106 — The critical equality correction is positive outside one explicit \(1.8444\%\) inner core

Claim ID: `L-91106` (provisional research range)  
Title: The continuum seed which exactly saturates the critical carry target minus the parabolic seed has one certified crossing on the fifty-fourth quotient cell; it is positive on the complete proportional outer region, and the exact finite equality correction converges to it with an explicit \(O(X^{-1/2})\) error  
Status: **PROPOSED COMPLETE EXACT CELL / FINITE-TRANSFER THEOREM — DIRECTED CERTIFICATE PROVIDED, INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-pro`  
Date: 2026-08-11  
Depends on: `L-91105`; finite Möbius inversion; elementary sum-integral comparison  
Scope: unconditional outer equality-correction geometry; no positive endpoint-weight realization and no RH conclusion

## 1. The continuum equality seed

For \(0<\theta\le1\), define
\[
 \mathscr D(\theta)
 =\theta^{-1/2}
 \sum_{k\le1/\theta}
 \frac{\mu(k)}{\sqrt k}
 \log\frac1{k\theta}.
\tag{L-91106.1}
\]

This is the continuum form of the exact multiples-Möbius inverse in `L-91105.23`. Define its tail seed
\[
\boxed{
 \mathscr B^\star(\theta)
 =\int_\theta^1\mathscr D(u)\,du.
}
\tag{L-91106.2}
\]

Switching the finite \(k\)-sum with the integral gives
\[
\boxed{
 \mathscr B^\star(\theta)
 =\sum_{k\le1/\theta}\frac{\mu(k)}k
 \left[
 4(1-\sqrt{k\theta})
 +2\sqrt{k\theta}\log(k\theta)
 \right].
}
\tag{L-91106.3}

The normalized parabolic seed is
\[
 \mathscr B(\theta)
 =2\sqrt\theta\left[
 \log\frac1\theta-2(1-\sqrt\theta)
 \right].
\tag{L-91106.4}

Put
\[
\boxed{
 \mathscr F(\theta)=\mathscr B^\star(\theta)-\mathscr B(\theta).
}
\tag{L-91106.5}

Thus \(\mathscr F\) is the proportional-scale correction from the positive parabolic seed to the exact critical carry-equality seed.

## 2. Exact quotient-cell formula

Fix \(N\ge1\) and
\[
 \frac1{N+1}\le\theta\le\frac1N.
\]
Define the finite Möbius coordinates
\[
 a_N=\sum_{k\le N}\frac{\mu(k)}k,
 \qquad
 m_N=\sum_{k\le N}\frac{\mu(k)}{\sqrt k},
 \qquad
 \ell_N=\sum_{k\le N}\frac{\mu(k)\log k}{\sqrt k}.
\tag{L-91106.6}

Equation (L-91106.3) gives
\[
 \mathscr B^\star(\theta)
 =4a_N-4\sqrt\theta\,m_N
 +2\sqrt\theta\,[\ell_N+m_N\log\theta].
\tag{L-91106.7}

Therefore
\[
\boxed{
 \mathscr F_N(\theta)
 =4(a_N-\theta)
 +\sqrt\theta\left[
 4(1-m_N)+2\ell_N+2(m_N+1)\log\theta
 \right].
}
\tag{L-91106.8}

With \(x=\sqrt\theta\),
\[
\boxed{
 \mathscr F_N(x)
 =4a_N-4x^2
 +x\left[
 4(1-m_N)+2\ell_N+4(m_N+1)\log x
 \right].
}
\tag{L-91106.9}

Its first two derivatives are
\[
\boxed{
 \mathscr F_N'(x)
 =-8x+8+2\ell_N+4(m_N+1)\log x,
}
\tag{L-91106.10}
\]
\[
\boxed{
 \mathscr F_N''(x)
 =-8+\frac{4(m_N+1)}x.
}
\tag{L-91106.11}

The entering \(k=N\) summand in (L-91106.3), and its first derivative, both vanish at \(N\theta=1\). Hence the cell formulas join \(C^1\) at every reciprocal knot.

## 3. Shape reduction on every cell

If \(m_N+1\le0\), equation (L-91106.11) is strictly negative.

If \(m_N+1>0\), the second derivative changes sign at most once, from positive to negative, at
\[
 x=\frac{m_N+1}{2}.
\]
Thus \(\mathscr F_N'\) has no interior minimum: its minimum on a closed quotient cell occurs at one of the two endpoints.

Consequently:

- positivity of the two endpoint derivatives proves monotonic increase on the whole cell;
- when the derivative is negative throughout, the minimum of \(\mathscr F_N\) is the right endpoint;
- when the derivative changes from positive to negative, the only interior extremum of \(\mathscr F_N\) is a maximum, so its minimum is again an endpoint.

This reduces the complete outer sign theorem to finitely many directed knot and derivative inequalities.

## 4. Directed finite certificate and the unique crossing

The companion exact checker uses:

- `Fraction` arithmetic;
- integer-square-root enclosures with denominator \(10^{90}\);
- the positive rational `atanh` series for logarithms with an exact geometric tail;
- the exact Möbius values through \(55\).

It proves:

1. every reciprocal knot satisfies
   \[
   \mathscr F(1/N)>0
   \qquad(2\le N\le54);
   \tag{L-91106.12}
   \]
2. the next knot is negative:
   \[
   \mathscr F(1/55)<-0.0007143;
   \tag{L-91106.13}
   \]
3. both endpoint derivatives are positive on every cell \(6\le N\le54\), with the uniform certified lower margin
   \[
   \mathscr F_N'(x)>0.0840;
   \tag{L-91106.14}
   \]
4. cells \(1,\ldots,5\) have the required one-extremum geometry and positive endpoint minima;
5. on the \(N=54\) cell, the values at the rational points
   \[
   \frac{1844367547103}{10^{14}},
   \qquad
   \frac{1844367547105}{10^{14}}
   \]
   have opposite strict signs.

Therefore there is one and only one zero
\[
\boxed{
 c_0
 =0.0184436754710385148014\ldots
}
\tag{L-91106.15}

on the cell
\[
 \frac1{55}<c_0<\frac1{54},
\]
with certified bracket
\[
\boxed{
 0.01844367547103<c_0<0.01844367547105.
}
\tag{L-91106.16}

The complete certified sign is
\[
\boxed{
 \mathscr F(\theta)<0
 \quad\left(\frac1{55}\le\theta<c_0\right),
}
\tag{L-91106.17}
\]
\[
\boxed{
 \mathscr F(\theta)>0
 \quad(c_0<\theta<1),
 \qquad
 \mathscr F(1)=0.
}
\tag{L-91106.18}

No statement is made here about \(0<\theta<1/55\); that region contains the unbounded Möbius depth.

Thus the exact continuum equality correction is already favorable on more than \(98.1556\%\) of the proportional endpoint range. The only first obstruction lies in the inner factor
\[
 c_0^{-1}=54.2191279\ldots .
\]

## 5. Exact finite equality seed

For an integer endpoint \(X\), define as in `L-91105`
\[
 d_X^\star(m)
 =\sum_{k\le X/m}\mu(k)
 \frac1{\sqrt{km}}
 \log\frac X{km},
\tag{L-91106.19}
\]
\[
 b_X^\star(n)=\sum_{m=n}^{X}d_X^\star(m).
\tag{L-91106.20}

Then
\[
 v_q(b_X^\star)=w_X(q)
\]
exactly. Put
\[
 F_X^\star(n)=b_X^\star(n)-b_X(n).
\tag{L-91106.21}

Let
\[
 \theta=\frac nX\ge\frac1{55},
 \qquad
 N=\left\lfloor\frac Xn\right\rfloor\le55.
\]
Switching the finite \(k\)-sum gives
\[
 b_X^\star(n)
 =\sum_{k\le N}\frac{\mu(k)}{\sqrt k}
 \sum_{m=n}^{\lfloor X/k\rfloor}
 m^{-1/2}\log\frac X{km}.
\tag{L-91106.22}

For fixed \(k\), the summand is nonnegative and decreasing on its support. Hence its left Riemann sum differs from the corresponding integral by a number between zero and its first value. Therefore
\[
\begin{aligned}
&\left|
 b_X^\star(n)-\sqrt X\,\mathscr B^\star(n/X)
 \right|\\
&\qquad\le
 n^{-1/2}
 \sum_{k\le N}\frac{|\mu(k)|}{\sqrt k}
 \log\frac X{kn}.
\end{aligned}
\tag{L-91106.23}

The directed checker proves the explicit corridor
\[
 \sqrt{55}
 \sum_{k\le55}\frac{|\mu(k)|}{\sqrt k}\log\frac{55}{k}
 <113.
\tag{L-91106.24}

Since \(b_X(n)=\sqrt X\,\mathscr B(n/X)\) exactly,
\[
\boxed{
 \left|
 F_X^\star(n)-\sqrt X\,\mathscr F(n/X)
 \right|
 <\frac{113}{\sqrt X}
 \qquad(n\ge X/55).
}
\tag{L-91106.25}

This is a finite theorem, not only a weak convergence statement.

## 6. Cofinal outer positivity

Fix any
\[
 \varepsilon>0.
\]
On the compact interval
\[
 [c_0+\varepsilon,1-\varepsilon],
\]
the continuous function \(\mathscr F\) has a positive minimum \(m_\varepsilon\). Equation (L-91106.25) gives
\[
 F_X^\star(n)>0
\]
whenever
\[
 (c_0+\varepsilon)X\le n\le(1-\varepsilon)X
\]
and
\[
 X>113/m_\varepsilon.
\]
Thus
\[
\boxed{
 F_X^\star(n)>0
 \quad\text{uniformly on every compact proportional subband of }(c_0,1).
}
\tag{L-91106.26}

The top \(o(X)\) collar can be treated directly from the finite formula and is separated from this proportional theorem.

## 7. Exact scale-contraction consequence

Let \(K\) be an integer and truncate the equality correction by
\[
 F_{X,\ge K}^\star(n)
 =F_X^\star(n)\mathbf1_{n\ge K}.
\]
For every column \(q\ge K\), all nodes \(kq\) and \(kq+1\) entering its carry response are at least \(K\). Therefore
\[
\boxed{
 v_q(F_{X,\ge K}^\star)=v_q(F_X^\star)
 \qquad(q\ge K).
}
\tag{L-91106.27}

The same is true after the radix-four detail because \(4q\ge q\ge K\):
\[
\boxed{
 \mathcal D_4v_q(F_{X,\ge K}^\star)
 =\mathcal D_4v_q(F_X^\star)
 \qquad(q\ge K).
}
\tag{L-91106.28}

Hence a positive admissible realization of the outer correction resolves every detail column above \(K\) exactly and leaves only columns below \(K\).

Choosing
\[
 K=(c_0+o(1))X
\]
would contract the unresolved scale by the fixed factor
\[
\boxed{c_0<0.018444.}
\tag{L-91106.29}

This nominates a radically shorter all-generation programme:

```text
realize the positive equality correction on the outer 98.15% by shadow butterflies;
pass the unresolved inner core to the next generation;
repeat after a factor >54 scale contraction;
pay only the finite collars and shadow-killing discrepancy.
```

The number of generations is \(O(\log X/\log54)\), and much smaller in practical scale than binary or factor-four recurrences.

## 8. What remains

This theorem proves positivity of the **seed correction**, not automatically positivity of:

- the bidiagonal butterfly intensities;
- the resulting endpoint weights;
- every low-column residual after truncation.

Those are the exact finite shadow-realization questions isolated by `L-91105`.

The new information is that the difficult arithmetic depth has been localized to an inner \(1.8444\%\) proportional core, while the complete outer equality correction is elementary, finite-depth, positive, and admits an explicit \(O(X^{-1/2})\) transfer.

## 9. Proof boundary

Closed exactly, subject to review:

1. the continuum equality seed and cell formula;
2. \(C^1\) knot matching;
3. the one-crossing theorem and certified root bracket;
4. positivity on the complete proportional outer region;
5. the exact finite equality seed;
6. the explicit uniform finite-transfer error;
7. cofinal finite outer positivity away from collars;
8. exact contraction of unresolved columns after outer truncation.

Still open:

1. nonnegative butterfly realization of the outer correction;
2. endpoint-weight positivity after the shadow move;
3. a coefficient-one recursive residual theorem for the inner core;
4. the score accounting across generations;
5. RH.
